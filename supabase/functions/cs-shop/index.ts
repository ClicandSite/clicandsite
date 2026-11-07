// 07/11/2026 (Claude, demande d'Anthony) — Boutique MyCreativeSite : commandes et paiement par carte.
// L'argent va directement sur le compte Stripe du commerçant (Stripe Connect, compte « standard »).
// Actions (POST JSON) :
//   checkout  {slug, items[{i,t,q}], mode, name, email, phone, address, note, back}  -> {url} (paiement) ou {ok, card:false} (paiement au retrait/à la livraison)
//   confirm   {slug, session}                                                       -> {paid}
//   connect   {site, back}   (espace client, connecté)                              -> {url} page Stripe pour activer les paiements
//   status    {site}         (espace client, connecté)                              -> {account, card}
//   sweep     (en-tête x-cs-key)                                                     -> vérifie les paiements restés en attente
// Sans la clé STRIPE_SECRET_KEY (secret de la fonction), les commandes arrivent quand même dans « Mes demandes », à régler sur place.
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";

const URL_ = Deno.env.get("SUPABASE_URL")!;
const db = createClient(URL_, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const SK = Deno.env.get("STRIPE_SECRET_KEY") || "";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, apikey, content-type, x-cs-key", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const out = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json; charset=utf-8" } });
const fail = (m: string, s = 400) => out({ message: m }, s);

function form(o: Record<string, unknown>, pre = "", acc: string[] = []) {
  for (const [k, v] of Object.entries(o)) {
    if (v === undefined || v === null) continue;
    const key = pre ? `${pre}[${k}]` : k;
    if (typeof v === "object") form(v as Record<string, unknown>, key, acc);
    else acc.push(encodeURIComponent(key) + "=" + encodeURIComponent(String(v)));
  }
  return acc.join("&");
}
async function stripe(method: string, path: string, body?: Record<string, unknown>, account?: string) {
  const h: Record<string, string> = { Authorization: "Bearer " + SK };
  if (account) h["Stripe-Account"] = account;
  if (body) h["Content-Type"] = "application/x-www-form-urlencoded";
  const r = await fetch("https://api.stripe.com/v1/" + path, { method, headers: h, body: body ? form(body) : undefined });
  const j = await r.json();
  if (!r.ok) throw new Error(j?.error?.message || "Stripe " + r.status);
  return j;
}
const safeBack = (u: unknown) => { try { const x = new URL(String(u)); return x.protocol === "https:" || x.hostname === "localhost" ? x.origin + x.pathname : null; } catch { return null; } };

async function owner(req: Request, site: string) {
  const auth = req.headers.get("authorization") || "";
  const user = createClient(URL_, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: auth } }, auth: { persistSession: false } });
  const { data } = await user.rpc("cs_can_edit_site", { p_id: site });
  return data === true;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return fail("Méthode non permise", 405);
  let b: Record<string, any> = {};
  try { b = await req.json(); } catch { return fail("Requête invalide"); }
  const action = String(b.action || "");
  try {
    if (action === "checkout") {
      const back = safeBack(b.back);
      if (!back) return fail("Adresse de retour invalide");
      const ip = (req.headers.get("x-forwarded-for") || "").split(",")[0].trim();
      const { data: o, error } = await db.rpc("cs_shop_order_create", { p_slug: String(b.slug || ""), p_items: b.items || [], p_mode: String(b.mode || ""), p_name: b.name || "", p_email: b.email || "", p_phone: b.phone || "", p_address: b.address || "", p_note: b.note || "", p_ip: ip });
      if (error) return fail(error.message.replace(/^.*?: /, ""));
      if (!SK || !o.account) return out({ ok: true, card: false, total: o.total });
      const items: Record<string, unknown> = {};
      (o.lines as { t: string; q: number; u: number }[]).forEach((l, k) => { items[k] = { quantity: l.q, price_data: { currency: "eur", unit_amount: l.u, product_data: { name: l.t.slice(0, 250) } } }; });
      if (o.ship > 0) items[Object.keys(items).length] = { quantity: 1, price_data: { currency: "eur", unit_amount: o.ship, product_data: { name: "Livraison" } } };
      const s = await stripe("POST", "checkout/sessions", {
        mode: "payment", line_items: items, customer_email: o.email, locale: "fr",
        success_url: back + "?commande=ok&cs_session={CHECKOUT_SESSION_ID}#produits", cancel_url: back + "?commande=annulee#produits",
        metadata: { lead: o.lead, site: String(b.slug) }, payment_intent_data: { description: "Commande " + o.name, metadata: { lead: o.lead } },
      }, o.account);
      await db.rpc("cs_shop_order_ref", { p_lead: o.lead, p_ref: s.id });
      return out({ url: s.url });
    }
    if (action === "confirm") {
      const ref = String(b.session || "");
      if (!SK || !/^cs_[A-Za-z0-9_]+$/.test(ref)) return out({ paid: false });
      const { data: pend } = await db.rpc("cs_shop_pending");
      const p = (pend || []).find((x: { ref: string }) => x.ref === ref);
      if (!p) return out({ paid: true }); // déjà enregistrée (ou inconnue)
      const s = await stripe("GET", "checkout/sessions/" + ref, undefined, p.account);
      if (s.payment_status === "paid") { await db.rpc("cs_shop_order_paid", { p_ref: ref, p_amount: s.amount_total }); return out({ paid: true }); }
      return out({ paid: false });
    }
    if (action === "sweep") {
      const { data: ok } = await db.rpc("cs_shop_key_ok", { p_key: req.headers.get("x-cs-key") || "" });
      if (!ok) return fail("Accès refusé", 403);
      if (!SK) return out({ checked: 0 });
      const { data: pend } = await db.rpc("cs_shop_pending");
      let paid = 0;
      for (const p of pend || []) {
        try { const s = await stripe("GET", "checkout/sessions/" + p.ref, undefined, p.account); if (s.payment_status === "paid") { await db.rpc("cs_shop_order_paid", { p_ref: p.ref, p_amount: s.amount_total }); paid++; } } catch { /* on réessaiera */ }
      }
      return out({ checked: (pend || []).length, paid });
    }
    if (action === "selftest") { // vérification de la clé et de Connect, sans rien créer (clé interne requise)
      const { data: ok } = await db.rpc("cs_shop_key_ok", { p_key: req.headers.get("x-cs-key") || "" });
      if (!ok) return fail("Accès refusé", 403);
      if (!SK) return out({ key: false });
      const r: Record<string, unknown> = { key: true, mode: SK.includes("_live_") ? "live" : "test" };
      try { const x = await stripe("GET", "accounts?limit=1"); r.connect = "ok"; r.accounts = (x.data || []).length; } catch (e) { r.connect = (e as Error).message; }
      return out(r);
    }
    if (action === "connect" || action === "status") {
      const site = String(b.site || "");
      if (!/^[0-9a-f-]{36}$/.test(site) || !(await owner(req, site))) return fail("Accès refusé", 403);
      if (!SK) return fail("Le paiement par carte n'est pas encore ouvert sur MyCreativeSite. Écrivez-nous à contact@mycreativesite.fr.", 503);
      const { data: a } = await db.rpc("cs_shop_account", { p_site: site });
      let acc = a?.account as string | null;
      if (action === "status") {
        if (!acc) return out({ account: false, card: false });
        const x = await stripe("GET", "accounts/" + acc);
        await db.rpc("cs_shop_set_account", { p_site: site, p_account: acc, p_enabled: !!x.charges_enabled, p_details: { payouts: !!x.payouts_enabled, submitted: !!x.details_submitted } });
        return out({ account: true, card: !!x.charges_enabled, payouts: !!x.payouts_enabled, submitted: !!x.details_submitted });
      }
      const back = safeBack(b.back) || "https://mycreativesite.fr/espace/";
      if (!acc) {
        const x = await stripe("POST", "accounts", { type: "standard", country: "FR", email: a?.email, business_profile: { name: a?.name, url: a?.domain ? "https://" + String(a.domain).replace(/^https?:\/\//, "") : undefined }, metadata: { site } });
        acc = x.id;
        await db.rpc("cs_shop_set_account", { p_site: site, p_account: acc, p_enabled: false, p_details: {} });
      }
      const l = await stripe("POST", "account_links", { account: acc, type: "account_onboarding", refresh_url: back + "?stripe=reprendre", return_url: back + "?stripe=retour" });
      return out({ url: l.url });
    }
    return fail("Action inconnue");
  } catch (e) {
    return fail((e as Error).message || "Erreur", 502);
  }
});
