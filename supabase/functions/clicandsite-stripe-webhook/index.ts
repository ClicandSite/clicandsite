import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";
// MyCreativeSite — webhook Stripe (06/11/2026).
// Reçoit les événements du compte Stripe MyCreativeSite (et seulement lui : signature vérifiée avec son secret).
// Met à jour clicandsite.subscriptions et le statut du site client : impayé/résilié → « suspendu », de nouveau payé → « en ligne ».
const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const res = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { "Content-Type": "application/json" } });
const enc = new TextEncoder();

async function verify(payload: string, header: string, secret: string) {
  const parts = Object.fromEntries(header.split(",").map(p => { const i = p.indexOf("="); return [p.slice(0, i), p.slice(i + 1)]; }));
  const t = parts["t"]; const sigs = header.split(",").filter(p => p.startsWith("v1=")).map(p => p.slice(3));
  if (!t || !sigs.length) return false;
  if (Math.abs(Date.now() / 1000 - Number(t)) > 600) return false;
  const key = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const mac = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(t + "." + payload)));
  const hex = [...mac].map(b => b.toString(16).padStart(2, "0")).join("");
  return sigs.some(s => s.length === hex.length && [...s].reduce((a, c, i) => a | (c.charCodeAt(0) ^ hex.charCodeAt(i)), 0) === 0);
}

Deno.serve(async (req) => {
  if (req.method !== "POST") return res({ error: "method" }, 405);
  const payload = await req.text();
  const { data: secret } = await db.rpc("cs_stripe_secret");
  if (!secret || !(await verify(payload, req.headers.get("stripe-signature") || "", secret as string))) return res({ error: "signature" }, 400);
  const ev = JSON.parse(payload); const o = ev.data?.object || {};
  let a: Record<string, unknown> = { p_event_id: ev.id, p_type: ev.type, p_sub: null, p_customer: null, p_email: null, p_company: null, p_phone: null, p_plan: null, p_status: null, p_period_end: null, p_ref: null };
  if (ev.type === "checkout.session.completed" && o.mode === "subscription") {
    const company = (o.custom_fields || []).find((f: any) => f.key === "entreprise")?.text?.value || null;
    a = { ...a, p_sub: o.subscription, p_customer: o.customer, p_email: o.customer_details?.email, p_company: company, p_phone: o.customer_details?.phone, p_plan: o.metadata?.plan || null, p_status: "active", p_ref: o.client_reference_id || null };
  } else if (ev.type.startsWith("customer.subscription.")) {
    const pe = o.current_period_end ?? o.items?.data?.[0]?.current_period_end ?? null;
    a = { ...a, p_sub: o.id, p_customer: o.customer, p_plan: o.metadata?.plan || null, p_status: ev.type === "customer.subscription.deleted" ? "canceled" : o.status, p_period_end: pe };
  } else if (ev.type === "invoice.payment_failed" || ev.type === "invoice.paid") {
    const sub = o.subscription || o.parent?.subscription_details?.subscription || null;
    a = { ...a, p_sub: sub, p_customer: o.customer, p_email: o.customer_email, p_status: ev.type === "invoice.paid" ? "active" : "past_due" };
  }
  const { data, error } = await db.rpc("cs_stripe_apply", a);
  if (error) return res({ error: error.message }, 500);
  // 08/11/2026 (Anthony) : Pack Auto & Immo et diffusion Abracadeal incluse — les infos saisies au paiement (SIRET, entreprise, adresse, téléphone, e-mail)
  // remplissent le profil du site, puis le compte Abracadeal est ouvert et relié tout de suite (sans attendre le cron).
  // (les paiements par lien Stripe n'ont pas toujours la formule dans metadata : le champ SIRET suffit à reconnaître le pack)
  if (ev.type === "checkout.session.completed" && o.client_reference_id && (String(o.metadata?.plan || "").toLowerCase() === "autoimmo" || (o.custom_fields || []).some((f: any) => f.key === "siret"))) {
    const cf = (k: string) => (o.custom_fields || []).find((f: any) => f.key === k);
    const siret = String(cf("siret")?.numeric?.value || cf("siret")?.text?.value || "").replace(/\D/g, "");
    const ad = o.customer_details?.address || {};
    const address = [ad.line1, ad.line2].filter(Boolean).join(", ") + (ad.postal_code || ad.city ? "\n" + [ad.postal_code, ad.city].filter(Boolean).join(" ") : "");
    await db.rpc("cs_abra_profile", { p_slug: o.client_reference_id, p_data: {
      siret: siret.length === 14 ? siret : "", company: cf("entreprise")?.text?.value || "", email: o.customer_details?.email || "",
      phone: o.customer_details?.phone || "", address: address.trim() } });
    const { data: ik } = await db.rpc("cs_abra_internal_key");
    const job = fetch(Deno.env.get("SUPABASE_URL") + "/functions/v1/cs-abracadeal-sync", { method: "POST",
      headers: { "Content-Type": "application/json", "x-cs-key": String(ik || "") }, body: JSON.stringify({ slug: o.client_reference_id }) }).catch((e) => console.error(e));
    // @ts-ignore EdgeRuntime existe sur Supabase : la synchro continue après la réponse à Stripe
    if (typeof EdgeRuntime !== "undefined") EdgeRuntime.waitUntil(job);
  }
  return res(data);
});
