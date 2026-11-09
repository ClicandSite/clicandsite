// 08/11/2026 (Claude, demande d'Anthony) — MyCreativeSite : paiement de la commande d'un site avec ses options.
// POST {slug} -> {url} : page de paiement Stripe (compte MyCreativeSite) avec, sur une seule facture :
//   abonnement de la formule + frais de mise en ligne + options choisies à la commande (logo et bannière 49 €, fiche Google 149 €,
//   adresse mail pro 5 €/mois, site bilingue 10 €/mois). Logo et bilingue sont déjà inclus en Premium et Boutique.
// Les prix sont recalculés ici d'après la fiche du site : rien ne vient du navigateur à part l'identifiant du site.
// Le webhook clicandsite-stripe-webhook relie ensuite le paiement au site (client_reference_id = slug).
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const SK = Deno.env.get("STRIPE_SECRET_KEY") || "";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const out = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json; charset=utf-8" } });

// Prix Stripe du compte MyCreativeSite (acct_1UYmIEEVjm0uqFCc)
const PLAN: Record<string, { monthly: string; setup: string }> = {
  essentiel: { monthly: "price_1UYmnNEVjm0uqFCcIEKLOLwA", setup: "price_1UYmdMEVjm0uqFCck39Xrsuj" },
  pro: { monthly: "price_1UZDbXEVjm0uqFCc5ed7JRlp", setup: "price_1UYmdNEVjm0uqFCcLvQUK9Tx" },
  premium: { monthly: "price_1UZDbYEVjm0uqFCcjq9X3VHV", setup: "price_1UYmdPEVjm0uqFCcNdD6SaXX" },
  boutique: { monthly: "price_1UZ76PEVjm0uqFCczretGSsA", setup: "price_1UYmdPEVjm0uqFCcNdD6SaXX" },
  // 08/11/2026 : Pack Auto & Immo — 99 €/mois + 490 € (même mise en ligne que Boutique, demande d'Anthony) ; annonces illimitées sur Abracadeal
  autoimmo: { monthly: "price_1UZdDdEVjm0uqFCcnQKR8aXu", setup: "price_1UYmdPEVjm0uqFCcNdD6SaXX" },
};
const OPTION: Record<string, string> = {
  logo: "price_1UZrJqEVjm0uqFCc5FvJc1nJ",      // logo et bannière, 49 € une fois (09/11/2026, avant 19 €)
  google: "price_1UZYzqEVjm0uqFCcjqQ0XeWb",    // 149 € une fois
  mail: "price_1UZYzsEVjm0uqFCc5UG4ygNb",      // 5 € / mois
  bilingue: "price_1UZYzuEVjm0uqFCcO2h9btCA",  // 10 € / mois
};
const INCLUDED: Record<string, string[]> = { premium: ["logo", "bilingue"], boutique: ["logo", "bilingue"] };

function form(o: Record<string, unknown>, pre = "", acc: string[] = []) {
  for (const [k, v] of Object.entries(o)) {
    if (v === undefined || v === null) continue;
    const key = pre ? `${pre}[${k}]` : k;
    if (typeof v === "object") form(v as Record<string, unknown>, key, acc);
    else acc.push(encodeURIComponent(key) + "=" + encodeURIComponent(String(v)));
  }
  return acc.join("&");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return out({ message: "Méthode non permise" }, 405);
  try {
    const { slug } = await req.json();
    if (typeof slug !== "string" || !/^[a-z0-9-]{3,60}$/.test(slug)) return out({ message: "Site inconnu" }, 400);
    const { data: s } = await db.rpc("cs_checkout_site", { p_slug: slug });
    if (!s) return out({ message: "Site inconnu" }, 404);
    if (s.paid || s.status === "en_ligne") return out({ message: "Ce site est déjà payé." }, 409);
    const plan = PLAN[String(s.plan || "").toLowerCase()];
    if (!plan) return out({ message: "Formule à choisir : écrivez-nous à contact@mycreativesite.fr." }, 400);
    if (!SK) return out({ message: "Paiement indisponible" }, 503);
    const inc = INCLUDED[String(s.plan).toLowerCase()] || [];
    const opts = (Array.isArray(s.options) ? s.options : []).filter((o: string) => OPTION[o] && !inc.includes(o));
    const items = [{ price: plan.monthly, quantity: 1 }, { price: plan.setup, quantity: 1 }, ...opts.map((o: string) => ({ price: OPTION[o], quantity: 1 }))];
    const back = "https://mycreativesite.fr/apercu/?s=" + encodeURIComponent(slug);
    const body: Record<string, unknown> = {
      mode: "subscription",
      line_items: items,
      client_reference_id: slug,
      success_url: back + "&paiement=ok",
      cancel_url: back,
      locale: "fr",
      allow_promotion_codes: "true",
      phone_number_collection: { enabled: "true" },
      metadata: { plan: String(s.plan).toLowerCase(), site: slug, options: opts.join(",") },
      subscription_data: { metadata: { plan: String(s.plan).toLowerCase(), site: slug, options: opts.join(",") } },
      custom_fields: [{ key: "entreprise", label: { type: "custom", custom: "Nom de votre entreprise" }, type: "text", text: { default_value: String(s.name || "").slice(0, 100) } }],
    };
    // 08/11/2026 (Anthony : « Abracadeal seulement à 99 € ») : Pack Auto & Immo et Boutique, diffusion Abracadeal incluse :
    // SIRET et adresse demandés au paiement pour ouvrir le compte Abracadeal automatiquement.
    if (/^(autoimmo|boutique)/.test(String(s.plan).toLowerCase())) {
      (body.custom_fields as unknown[]).push({ key: "siret", label: { type: "custom", custom: "SIRET de votre entreprise (14 chiffres)" }, type: "numeric", numeric: { minimum_length: 14, maximum_length: 14 } });
      body.billing_address_collection = "required";
    }
    if (s.email) body.customer_email = s.email;
    const r = await fetch("https://api.stripe.com/v1/checkout/sessions", {
      method: "POST", headers: { Authorization: "Bearer " + SK, "Content-Type": "application/x-www-form-urlencoded" }, body: form(body),
    });
    const j = await r.json();
    if (!r.ok) return out({ message: j?.error?.message || "Stripe " + r.status }, 502);
    return out({ url: j.url });
  } catch (e) {
    return out({ message: (e as Error).message || "Erreur" }, 500);
  }
});
