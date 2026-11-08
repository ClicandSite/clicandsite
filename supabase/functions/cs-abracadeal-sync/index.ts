// 08/11/2026 (Claude, demande d'Anthony) — Flux API direct MyCreativeSite → Abracadeal.
// Pack Auto & Immo (garages, agences) + diffusion incluse dans toutes les formules pour artisans, dépannage, beauté,
// bien-être (prestations → Services) et boutiques (produits → Maison / Mode / High-tech).
// Pour chaque site concerné et payé :
//   1) déclare l'entreprise chez Abracadeal (API partenaires) : son compte Pro est ouvert automatiquement,
//      avec les annonces illimitées incluses dans le pack ;
//   2) envoie son stock (véhicules ou biens du site) en mode « full » : ajouts, mises à jour et retraits automatiques ;
//   3) si le pack s'arrête (résiliation, changement de formule), arrête la diffusion : les annonces sont retirées.
// Appelée par le cron toutes les 10 min (clé interne x-cs-key = secret « abracadeal_sync_internal »). POST {slug} pour un seul site.
// N'envoie rien si le stock n'a pas changé (empreinte). Clé éditeur : table clicandsite.secrets (jamais dans le code).
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const API = "https://jplzvxmpbpjssyinozap.supabase.co/functions/v1/partner-api/v1";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const out = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json; charset=utf-8" } });

const sha = async (v: string) => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(v)))).map((b) => b.toString(16).padStart(2, "0")).join("");
const str = (v: unknown) => String(v ?? "").trim();
const num = (v: unknown) => { const n = Number(String(v ?? "").replace(/[^\d,.]/g, "").replace(/\s/g, "").replace(",", ".")); return Number.isFinite(n) && n > 0 ? n : null; };
const price = (v: unknown) => { const d = String(v ?? "").replace(/[^\d]/g, ""); return d ? Number(d) : null; };
const isUrl = (u: unknown) => typeof u === "string" && /^https:\/\/\S+$/i.test(u);

function address(profile: any) {
  const a = str(profile.address);
  const m = a.match(/(\d{5})\s+([^\n,]+)/);
  return { postal_code: m ? m[1] : "", city: m ? m[2].trim() : "" };
}

function photos(it: any) {
  const all = [it.img, ...(Array.isArray(it.photos) ? it.photos : [])].filter(isUrl);
  return [...new Set(all)].slice(0, 45);
}

// Référence stable : celle saisie par le pro, sinon une empreinte du titre et de la 1re photo.
async function reference(it: any, i: number) {
  const r = str(it.ref);
  if (r) return ("MCS-" + r).replace(/[^A-Za-z0-9._:-]/g, "-").slice(0, 80);
  return "MCS-" + (await sha(str(it.t) + "|" + (photos(it)[0] || "") + "|" + (photos(it).length ? "" : i))).slice(0, 16);
}

const sold = (it: any) => /vendu|loué|loue|sous compromis/i.test(str(it.tag));

async function vehicle(it: any, i: number, loc: any) {
  const meta = str(it.meta);
  const year = (meta.match(/\b(19[5-9]\d|20[0-4]\d)\b/) || [])[1];
  const km = (meta.match(/([\d\s.]+)\s*km/i) || [])[1];
  const mk = str(it.mk);
  let model = str(it.t);
  if (mk && model.toLowerCase().startsWith(mk.toLowerCase())) model = model.slice(mk.length).trim();
  const desc = [str(it.desc), str(it.feats) ? "Équipements :\n" + str(it.feats) : "", str(it.legal)].filter(Boolean).join("\n\n");
  return {
    reference: await reference(it, i), titre: str(it.t), marque: mk, modele: model || str(it.t), prix: price(it.p),
    annee: year ? Number(year) : null, kilometrage: km ? Number(km.replace(/\D/g, "")) : null, carburant: str(it.fuel) || null,
    description: desc, ville: loc.city || null, code_postal: loc.postal_code || null, photos: photos(it),
  };
}

async function estate(it: any, i: number, loc: any) {
  const meta = str(it.meta);
  const surf = (meta.match(/([\d\s,.]+)\s*m²/i) || [])[1];
  const typ = ({ appartement: "appartement", maison: "maison", terrain: "terrain", local: "local commercial", parking: "parking" } as Record<string, string>)[str(it.type)] || "autre";
  const desc = [str(it.desc), str(it.feats) ? "Caractéristiques :\n" + str(it.feats) : "", str(it.energy) ? "Dépenses d'énergie : " + str(it.energy) : "", str(it.legal)].filter(Boolean).join("\n\n");
  return {
    reference: await reference(it, i), transaction: str(it.tr) === "location" ? "location" : "vente", type_bien: typ,
    titre: str(it.t), description: desc, prix: price(it.p), surface: surf ? num(surf) : null, pieces: num(it.rooms),
    ville: str(it.city) || loc.city || null, code_postal: str(it.city) ? null : (loc.postal_code || null),
    dpe: /^[A-G]$/.test(str(it.dpe)) ? str(it.dpe) : null, ges: /^[A-G]$/.test(str(it.ges)) ? str(it.ges) : null,
    photos: photos(it),
  };
}

// ---- Métiers hors auto / immo (08/11/2026)
const SERVICE_SUB: Record<string, string> = { batiment: "artisans-travaux", depannage: "depannage", beaute: "beaute-bienetre", bienetre: "beaute-bienetre" };
const SHOP_RULES: [string, string, RegExp][] = [
  ["mode", "chaussures", /chaussure|basket|sneaker|botte|sandale|escarpin/i], ["mode", "sacs", /\bsacs?\b|pochette|maroquin/i],
  ["mode", "montres-bijoux", /bijou|montre|bague|collier|bracelet|boucle/i], ["mode", "vetements-femme", /femme|robe|jupe|chemisier/i],
  ["mode", "vetements-homme", /homme|chemise|costume/i], ["mode", "accessoires-mode", /accessoire|ceinture|écharpe|echarpe|chapeau|lunette/i],
  ["mode", "autre-mode", /v[êe]tement|mode|textile|t-shirt|pull|veste|manteau/i],
  ["hightech", "telephones", /t[ée]l[ée]phone|smartphone|iphone/i], ["hightech", "ordinateurs", /ordinateur|pc\b|laptop|macbook/i],
  ["hightech", "audio", /audio|enceinte|casque|écouteur|ecouteur/i], ["hightech", "accessoires-hightech", /chargeur|c[âa]ble|coque|high-?tech/i],
  ["maison", "luminaire", /lampe|luminaire|suspension|applique/i], ["maison", "cuisine", /cuisine|vaisselle|tasse|assiette|mug|bol\b/i],
  ["maison", "meubles", /meuble|table|chaise|fauteuil|canap|commode|étag|etag/i], ["maison", "linge-maison", /linge|coussin|plaid|drap|nappe/i],
  ["maison", "jardin", /jardin|plante|pot\b|fleur/i], ["maison", "decoration", /d[ée]co|vase|bougie|cadre|miroir|c[ée]ramique|poterie/i],
];
function shopClass(it: any) { const t = [it.meta, it.t, it.desc].map(str).join(" "); for (const [sec, sub, re] of SHOP_RULES) if (re.test(t)) return { sec, sub }; return { sec: "maison", sub: "autre-maison" }; }
function textPrice(v: unknown) { const m = String(v ?? "").replace(/\s/g, "").match(/(\d+(?:[.,]\d{1,2})?)/); if (!m) return null; const n = Math.round(Number(m[1].replace(",", "."))); return n > 0 ? n : null; }
function extraPhotos(s: any) { const out: string[] = []; for (const it of Array.isArray(s.items) ? s.items : []) out.push(...photos(it)); const h = s.photos?.hero; if (isUrl(h)) out.push(h); return [...new Set(out)]; }
async function serviceListings(s: any, loc: any) {
  const sub = SERVICE_SUB[s.trade];
  const cards = (Array.isArray(s.cards) ? s.cards : []).filter((c: any) => c && str(c.t));
  const fallback = extraPhotos(s);
  const src = cards.length ? cards.map((c: any) => ({ t: c.t, desc: c.d, p: c.p, img: c.img, photos: [] }))
    : (Array.isArray(s.items) ? s.items : []).filter((it: any) => it && str(it.t));
  const out = [];
  for (let i = 0; i < src.length; i++) {
    const it = src[i]; const ph = photos(it).length ? photos(it) : fallback.slice(0, 1);
    const title = (str(it.t) + (loc.city && !str(it.t).toLowerCase().includes(loc.city.toLowerCase()) ? " — " + loc.city : "")).slice(0, 100);
    out.push({ reference: await reference(it, i), titre: title, sous_categorie: sub, prix: textPrice(it.p),
      description: [str(it.desc), str(it.feats), str(it.p) && !textPrice(it.p) ? "Tarif : " + str(it.p) : ""].filter(Boolean).join("\n\n"),
      ville: str(it.city) || loc.city || null, code_postal: str(it.city) ? null : (loc.postal_code || null), photos: ph });
  }
  return out;
}
async function shopListings(s: any, loc: any) {
  const items = (Array.isArray(s.items) ? s.items : []).filter((it: any) => it && str(it.t) && !sold(it));
  const cls = items.map(shopClass);
  const count: Record<string, number> = {}; for (const c of cls) count[c.sec] = (count[c.sec] || 0) + 1;
  const sector = Object.entries(count).sort((a, b) => b[1] - a[1])[0]?.[0] || "maison";
  const out = [];
  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    out.push({ reference: await reference(it, i), titre: str(it.t).slice(0, 100), sous_categorie: cls[i].sec === sector ? cls[i].sub : "", prix: textPrice(it.p),
      description: [str(it.desc), str(it.feats)].filter(Boolean).join("\n\n"), ville: loc.city || null, code_postal: loc.postal_code || null, photos: photos(it) });
  }
  return { sector, listings: out };
}

async function call(key: string, method: string, path: string, body?: unknown) {
  const r = await fetch(API + path, { method, headers: { Authorization: "Bearer " + key, "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined, signal: AbortSignal.timeout(150000) });
  const d = await r.json().catch(() => ({}));
  return { status: r.status, data: d };
}

async function handle(key: string, s: any) {
  const agency = "mcs-" + s.slug;
  // Pack arrêté : diffusion arrêtée, annonces retirées.
  if (!s.eligible) {
    const r = await call(key, "DELETE", "/agencies/" + encodeURIComponent(agency));
    const ok = r.status === 200 || r.status === 404;
    await db.rpc("cs_abra_mark", { p_site: s.id, p_status: ok ? "stopped" : s.agency_status, p_hash: null, p_result: r.data, p_error: ok ? null : JSON.stringify(r.data).slice(0, 500) });
    return { slug: s.slug, action: "stop", ok };
  }
  const p = s.profile || {};
  const siret = str(p.siret).replace(/\s/g, "");
  if (!/^\d{14}$/.test(siret)) {
    await db.rpc("cs_abra_mark", { p_site: s.id, p_status: "missing_siret", p_hash: null, p_result: null, p_error: "SIRET manquant dans le profil du site (onglet Mon entreprise)." });
    return { slug: s.slug, action: "wait", reason: "siret" };
  }
  const loc = address(p);
  let sector = s.trade === "garage" ? "vehicules" : s.trade === "immobilier" ? "immobilier" : SERVICE_SUB[s.trade] ? "services" : "maison";
  let shop: any = null;
  if (s.trade === "boutique") { shop = await shopListings(s, loc); sector = shop.sector; }
  const ag = await call(key, "PUT", "/agencies/" + encodeURIComponent(agency), {
    siret, name: str(p.company) || s.name, sector, email: str(p.email) || s.owner_email, phone: str(p.phone), city: loc.city, postal_code: loc.postal_code, consent: true,
  });
  const st = ag.data?.agency?.status || (ag.status >= 400 ? "error" : "unknown");
  if (st !== "active") {
    await db.rpc("cs_abra_mark", { p_site: s.id, p_status: st, p_hash: null, p_result: ag.data, p_error: st === "pending" ? null : JSON.stringify(ag.data).slice(0, 500) });
    return { slug: s.slug, action: "agency", status: st };
  }
  const items = (Array.isArray(s.items) ? s.items : []).filter((it: any) => it && !sold(it));
  let listings = [] as any[];
  if (shop) listings = shop.listings;
  else if (sector === "services") listings = await serviceListings(s, loc);
  else for (let i = 0; i < items.length; i++) listings.push(await (sector === "vehicules" ? vehicle(items[i], i, loc) : estate(items[i], i, loc)));
  // Une prestation peut être « sur devis » (sans prix) ; un véhicule, un bien ou un produit doit avoir un prix.
  const send = listings.filter((l) => (l.prix || sector === "services") && l.photos.length);
  const hash = await sha(JSON.stringify(send));
  if (hash === s.last_hash && s.agency_status === "active") return { slug: s.slug, action: "unchanged" };
  if (!send.length) {
    // Plus aucun bien à diffuser : on retire ce qui est en ligne sans arrêter l'agence.
    const cur = await call(key, "GET", "/agencies/" + encodeURIComponent(agency) + "/listings");
    for (const l of cur.data?.listings || []) if (l.status === "online" || l.status === "in_review") await call(key, "DELETE", "/agencies/" + encodeURIComponent(agency) + "/listings/" + encodeURIComponent(l.reference));
    await db.rpc("cs_abra_mark", { p_site: s.id, p_status: "active", p_hash: hash, p_result: { sent: 0 }, p_error: null });
    return { slug: s.slug, action: "empty" };
  }
  let res: any;
  if (send.length <= 200) res = await call(key, "PUT", "/agencies/" + encodeURIComponent(agency) + "/listings", { mode: "full", listings: send });
  else {
    // Plus de 200 : envoi par lots, puis retrait de ce qui n'existe plus sur le site.
    const refs = new Set(send.map((l) => l.reference));
    const acc: any = { created: 0, updated: 0, unchanged: 0, rejected: 0 };
    for (let i = 0; i < send.length; i += 200) {
      const r = await call(key, "PUT", "/agencies/" + encodeURIComponent(agency) + "/listings", { mode: "partial", listings: send.slice(i, i + 200) });
      if (r.status >= 400) { res = r; break; }
      for (const k of Object.keys(acc)) acc[k] += Number(r.data?.[k] || 0);
    }
    if (!res) {
      const cur = await call(key, "GET", "/agencies/" + encodeURIComponent(agency) + "/listings");
      for (const l of cur.data?.listings || []) if (!refs.has(l.reference) && (l.status === "online" || l.status === "in_review")) await call(key, "DELETE", "/agencies/" + encodeURIComponent(agency) + "/listings/" + encodeURIComponent(l.reference));
      res = { status: 200, data: { ok: true, ...acc } };
    }
  }
  const ok = res.status < 400 && res.data?.ok !== false;
  await db.rpc("cs_abra_mark", { p_site: s.id, p_status: "active", p_hash: ok ? hash : null, p_result: { ...res.data, skipped_without_price_or_photo: listings.length - send.length }, p_error: ok ? null : JSON.stringify(res.data).slice(0, 500) });
  return { slug: s.slug, action: "sync", ok, sent: send.length, result: res.data };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return out({ message: "Méthode non permise" }, 405);
  try {
    const { data: ik } = await db.rpc("cs_abra_internal_key");
    if (!ik || req.headers.get("x-cs-key") !== ik) return out({ message: "Accès refusé" }, 403);
    const body = await req.json().catch(() => ({}));
    const only = typeof body?.slug === "string" ? body.slug.toLowerCase() : null;
    const { data: key } = await db.rpc("cs_abra_key");
    if (!key) return out({ message: "Clé Abracadeal absente" }, 503);
    const { data: targets, error } = await db.rpc("cs_abra_targets");
    if (error) throw error;
    const list = (targets || []).filter((s: any) => !only || s.slug === only);
    const results = [];
    for (const s of list) {
      try { results.push(await handle(String(key), s)); }
      catch (e) { results.push({ slug: s.slug, error: (e as Error).message }); await db.rpc("cs_abra_mark", { p_site: s.id, p_status: s.agency_status || "error", p_hash: null, p_result: null, p_error: (e as Error).message }); }
    }
    return out({ ok: true, checked: list.length, results });
  } catch (e) {
    return out({ message: (e as Error).message || "Erreur" }, 500);
  }
});
