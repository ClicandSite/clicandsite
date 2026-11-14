import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";
// MyCreativeSite — robot de recherche de pros (06/11/2026, méthode du robot Abracadeal).
// mode "search" : annuaire officiel des entreprises (recherche-entreprises.api.gouv.fr, gratuit), France entière,
//    département par département et page par page : VTC / taxis, restaurants, garages, agences immobilières, bâtiment, vétérinaires,
//    auto-écoles, coachs, photographes, toiletteurs, fleuristes, traiteurs, loueurs de bateaux, kinés, dentistes, bijouteries, professions libérales, services à domicile, événementiel, hébergement, tourisme, location,
//    et (09/11/2026) la liste d'Anthony rattachée aux modèles existants : paysagistes, serruriers, beauté, bien-être, snacks, commerces de bouche…
// mode "crawl" : 1) devine le site des pros (nom de domaine vérifié) ; 2) lit l'accueil puis les pages contact /
//    mentions légales (5 pages max) pour relever l'e-mail et le téléphone publiés, et classe le site (daté / moderne / en panne).
//    (OpenStreetMap / Overpass est saturé ou refuse les serveurs Supabase.)
// mode "nouveaux" : créations du jour au BODACC (garages, concessions auto et moto, agences immobilières), même avant ouverture.
// N'ENVOIE AUCUN MAIL. Les pros trouvés attendent dans le CRM MyCreativeSite (projet Supabase séparé, schéma clicandsite) la validation d'Anthony.
const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const db = createClient(SUPABASE_URL, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { "Content-Type": "application/json" } });
const UA = "Mozilla/5.0 (compatible; MyCreativeSiteBot/1.0; +https://mycreativesite.fr/)";

const NAF: Record<string, string> = {
  vtc: "49.32Z,49.39B",
  restaurant: "56.10A",
  garage: "45.20A,45.11Z,45.40Z",
  immobilier: "68.31Z",
  // Bâtiment : maisons, électricité, plomberie/chauffage, plâtrerie, menuiserie, carrelage, peinture, finition, couverture, maçonnerie
  batiment: "41.20A,43.21A,43.22A,43.22B,43.31Z,43.32A,43.33Z,43.34Z,43.39Z,43.91B,43.99C",
  // 09/11/2026 : cliniques et cabinets vétérinaires
  veterinaire: "75.00Z",
  // 09/11/2026 : lot 2 (codes larges filtrés par le nom, voir KEEP)
  autoecole: "85.53Z",
  coach: "85.51Z,93.13Z",
  photographe: "74.20Z",
  toiletteur: "96.09Z",
  fleuriste: "47.76Z",
  traiteur: "56.21Z",
  nautisme: "77.21Z,50.10Z",
  kine: "86.90E",
  dentiste: "86.23Z",
  bijouterie: "47.77Z,95.25Z",
  // 09/11/2026 : liste d'Anthony — clés de recherche rattachées à un modèle existant (voir MODEL), le métier précis va dans « segment »
  etancheite: "43.99A",
  paysagiste: "81.30Z",
  serrurier: "43.32B",
  multiservice: "81.10Z",
  depanneur_auto: "52.21Z",
  beaute: "96.02A,96.02B",
  tatoueur: "96.09Z",
  bienetre: "96.04Z,86.90F",
  restorapide: "56.10C",
  salon_the: "56.30Z",
  boulangerie: "10.71C,10.71D",
  boucherie: "47.22Z",
  poissonnerie: "47.23Z",
  epicerie_fine: "47.29Z",
  informatique: "95.11Z,95.12Z",
  electromenager: "95.22Z",
  diagnostic: "71.20B",
  decoration: "74.10Z",
  plongee: "93.29Z,85.51Z",
  video: "59.11B",
  // 09/11/2026 : lot 3 (nouveaux modèles)
  liberal: "69.10Z,69.20Z,70.22Z,66.22Z,66.19B,85.59A,74.30Z,71.11Z,71.12B",
  services: "81.21Z,88.10A,88.91B",
  couture: "95.29Z,14.13Z",
  cours: "85.59B",
  evenementiel: "82.30Z",
  animation: "93.29Z,90.01Z",
  hebergement: "55.20Z",
  conciergerie: "68.32A",
  tourisme: "79.90Z,79.12Z",
  velo: "77.21Z",
  location: "77.11A,77.12Z,49.42Z",
  infirmier: "86.90D",
};
// Modèle de site (colonne trade) de chaque clé de recherche (par défaut : la clé elle-même)
const MODEL: Record<string, string> = {
  etancheite: "batiment", paysagiste: "batiment", diagnostic: "batiment", decoration: "batiment",
  serrurier: "depannage", multiservice: "depannage", depanneur_auto: "depannage", informatique: "depannage", electromenager: "depannage",
  tatoueur: "beaute", restorapide: "restaurant", salon_the: "restaurant",
  boucherie: "boulangerie", poissonnerie: "boulangerie", epicerie_fine: "boulangerie",
  plongee: "nautisme", video: "photographe",
  couture: "services", cours: "services", animation: "evenementiel", conciergerie: "hebergement", velo: "tourisme",
};
// Métier précis (segment) : d'après le code NAF et le nom, pour un mail qui parle du bon métier
function segOf(key: string, naf: string, name: string): string | null {
  const n = name.toLowerCase(), c = naf.replace(/\./g, "");
  switch (key) {
    case "batiment":
      if (/solaire|photovolta/.test(n)) return "solaire";
      if (/piscin/.test(n)) return "pisciniste";
      if (/fa[cç]ad/.test(n)) return "facadier";
      if (/clim/.test(n)) return "climaticien";
      return ({ "4321A": "electricien", "4322A": "plombier", "4322B": "chauffagiste", "4331Z": "platrier", "4332A": "menuisier", "4333Z": "carreleur", "4334Z": "peintre", "4339Z": "renovation", "4391B": "couvreur", "4399C": "macon", "4120A": "renovation" } as Record<string, string>)[c] || null;
    case "paysagiste": return /jardin/.test(n) && !/paysag/.test(n) ? "jardinier" : "paysagiste";
    case "beaute":
      if (/barb/.test(n)) return "barbier";
      if (/ongl|nail/.test(n)) return "ongles";
      if (/maquill|make.?up/.test(n)) return "maquilleuse";
      return c === "9602A" ? "coiffeur" : "institut";
    case "bienetre": return /\bspa\b|thalasso|hammam/.test(n) ? "spa" : "masseur";
    case "coach": return /yoga|pilates/.test(n) ? "yoga" : null;
    case "restorapide": return /pizz/.test(n) ? "pizzeria" : /food.?truck|camion/.test(n) ? "foodtruck" : "snack";
    case "traiteur": return /\bchef\b/.test(n) ? "chef_domicile" : null;
    case "boulangerie": return c === "1071D" ? "patisserie" : null;
    case "toiletteur": return /[ée]ducat|dressage|comportement/.test(n) ? "educateur_canin" : /pet.?sit|garde/.test(n) ? "pet_sitter" : null;
    case "nautisme": return /jet.?ski/.test(n) ? "jetski" : /skipper/.test(n) ? "skipper" : null;
    case "garage": return /carross/.test(n) ? "carrosserie" : /lavage|wash|detail|clean/.test(n) ? "lavage" : null;
    case "decoration": return /home.?stag/.test(n) ? "home_staging" : /architect/.test(n) ? "archi_interieur" : "decorateur";
    case "liberal":
      return ({ "6910Z": "avocat", "6920Z": "expert_comptable", "7022Z": "consultant", "6622Z": "courtier_assurance", "6619B": "courtier_credit", "8559A": "formateur", "7430Z": "traducteur", "7111Z": "architecte", "7112B": "bureau_etudes" } as Record<string, string>)[c] || null;
    case "services": return ({ "8121Z": "nettoyage", "8810A": "aide_domicile", "8891B": "garde_enfants" } as Record<string, string>)[c] || null;
    case "evenementiel": return /mariage|wedding/.test(n) ? "wedding_planner" : "organisateur";
    case "animation": return /\bdj\b|disc.?jockey|sono|mix/.test(n) ? "dj" : "loisirs";
    case "hebergement": return /g[iî]te/.test(n) ? "gite" : /chambre|h[ôo]te|b&b|bnb/.test(n) ? "chambres_hotes" : null;
    case "tourisme": return /excursion|tour|circuit/.test(n) ? "excursions" : "guide";
    case "location": return c === "4942Z" ? "demenagement" : c === "7712Z" ? "location_utilitaires" : "location_voitures";
    case "couture": case "cours": case "conciergerie": case "velo":
      return key;
    case "plongee": case "video": case "tatoueur": case "salon_the": case "boucherie": case "poissonnerie": case "epicerie_fine": case "etancheite":
    case "serrurier": case "multiservice": case "depanneur_auto": case "informatique": case "electromenager": case "diagnostic":
      return key;
  }
  return null;
}
// Codes NAF trop larges : on ne garde que les noms qui correspondent au métier (ou on écarte ceux qui n'en sont pas)
const KEEP: Record<string, RegExp> = {
  toiletteur: /toilett|canin|chien|dog|pet|groom|poil|patte|toutou|f[ée]lin/i,
  nautisme: /bateau|boat|nauti|marin|jet.?ski|yacht|voil|plaisance|sea\b|mer\b|oc[ée]an|croisi|skipper|kayak|paddle|port\b/i,
  kine: /kin[ée]|physio|r[ée][ée]ducation/i,
  tatoueur: /tatou|tattoo|\bink\b|piercing/i,
  depanneur_auto: /d[ée]pann|remorq|fourri[eè]re|assistance auto/i,
  salon_the: /salon de th[ée]|tea.?room|tea.?time|th[ée]i[eè]re/i,
  epicerie_fine: /[ée]picerie fine|fine|d[ée]licat|fromag|cavist|truffe|terroir|traiteur|italia|bio\b|gourmet/i,
  diagnostic: /diagnos|dpe\b|amiante/i,
  decoration: /d[ée]co|int[ée]rieur|home.?stag|agencement|design/i,
  plongee: /plong|diving|subaqua|apn[ée]e/i,
  video: /vid[ée]o|film|drone|prod|motion/i,
  couture: /coutur|retouche|atelier de couture|tailleur/i,
  cours: /cours|soutien scolaire|prof|tutorat|r[ée]p[ée]tit|acad[ée]mie/i,
  animation: /\bdj\b|disc.?jockey|sono|anim|mariage|wedding|f[eê]te|escape|karting|paintball|accrobranche|laser|bowling|loisir/i,
  conciergerie: /concierg|airbnb|saisonn|\bbnb\b|holiday|vacances|cl[ée]s? en main/i,
  velo: /v[ée]lo|bike|cycl|vtt/i,
  hebergement: /g[iî]te|chambre|h[ôo]te|b&b|bnb|mas\b|domaine|maison|bastide|cottage|lodge|chalet/i,
  infirmier: /infirm|\bide\b|soins (à|a) domicile|cabinet de soins/i,
  bienetre: /mass|ost[ée]o|sophro|naturo|r[ée]flexo|shiatsu|spa\b|hammam|bien.?[êe]tre|relax|ayurv/i,
};
const DROP: Record<string, RegExp> = { fleuriste: /animal|animaux|aquari|zoo|graine|jardinerie|pet\b|croquette/i };
// Chaînes et réseaux : ils ont déjà un site national, inutile de les démarcher.
const CHAINS = /mc ?donald|burger king|kfc|subway|domino|pizza hut|quick|buffalo grill|hippopotamus|courtepaille|flunch|del arte|la boucherie|starbucks|brioche dor|o.?tacos|speedy|norauto|midas|feu vert|point s\b|euromaster|carglass|first stop|vulco|top garage|eurorepar|motrio|renault|peugeot|citro[eë]n|toyota|volkswagen|mercedes|bmw|audi|ford|nissan|kia|hyundai|fiat|dacia|opel|skoda|seat|tesla|aramis|orpi|century 21|lafor[eê]t|era immobilier|guy hoquet|st[ée]phane plaza|nestenn|foncia|citya|square habitat|cr[ée]dit agricole|\biad\b|capifrance|safti|optimhome|\buber\b|\bg7\b|heetch|sodexo|elior|compass group|accor|novotel|ibis|mercure|sushi shop|flam's|courtepaille|leon de bruxelles|big mamma|ninkasi|carrefour|leclerc|intermarche|auchan|casino|monoprix|leroy merlin|castorama|brico|point p\b|bouygues|vinci|eiffage|spie\b|engie|veolia|cegelec|socotec|france toitures|illico travaux|cuisinella|schmidt|mobalpa|lapeyre|tryba|art et fen[eê]tres|grosfillex|sevetys|anicura|evidensia|mon v[ée]to\b|vetocentre|v[ée]toadom|clinique v[ée]t[ée]rinaire des urgences|\becf\b|stych|ornikar|en voiture simone|lepermislibre|basic.?fit|fitness park|orange bleue|keep cool|\bon air\b|neoness|magic form|l'appart fitness|cmg sports|monceau fleurs|interflora|rapid.?flore|au nom de la rose|aquarelle|lenotre|potel et chabot|dentego|dentalvia|vertuo|addentis|centres? de sant[ée]/i;
const LEGAL = /\b(sarl|sas|sasu|eurl|sa|snc|sci|ste|societe|société|ets|etablissements|holding|groupe|ei|eirl|scp|selarl|selas|selasu|selurl|scm|sel)\b/gi;
const EMAIL_RE = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/gi;
const BAD = /(\.(png|jpe?g|gif|webp|svg|css|js)$)|example\.|sentry|wixpress|godaddy|domain\.com|email\.com|votre|your|nom@|prenom|@2x|noreply|no-reply|ovh\.net$|mediateur|cnil\.fr|dgccrf|economie\.gouv/i;
const FREE_HOST = /wixsite\.com|jimdosite|jimdofree|e-monsite|over-blog|site-solocal|solocal|pagesjaunes|business\.site|webnode|godaddysites|weebly|sitew\.|wordpress\.com|blogspot|free\.fr|orange\.fr|wanadoo/i;
function baseDomain(h: string) { return h.replace(/^www\./, "").split(".").slice(-2).join("."); }

function titleCase(x: string) { return x.toLowerCase().replace(/(^|[\s'’(-])([a-zà-ÿ])/g, (_m, a, b) => a + b.toUpperCase()); }
function cleanName(r: any, e: any) {
  const ens = (e?.liste_enseignes || []).find((x: string) => x && x.length > 1);
  let n = ens || e?.nom_commercial || r.nom_complet || "";
  const m = n.match(/\(([^)]{3,})\)\s*$/); if (!ens && m) n = m[1];
  n = n.replace(/\s+/g, " ").trim();
  return n === n.toUpperCase() ? titleCase(n) : n;
}
const deptOf = (cp: string) => cp.startsWith("97") ? cp.slice(0, 3) : cp.startsWith("20") ? null : cp.slice(0, 2);
async function sirene(dept: string, trade: string, page: number) {
  const rows: any[] = [];
  const u = `https://recherche-entreprises.api.gouv.fr/search?activite_principale=${NAF[trade]}&departement=${dept}&etat_administratif=A&per_page=25&page=${page}`;
  let r = await fetch(u, { headers: { "User-Agent": UA, "Accept": "application/json" }, signal: AbortSignal.timeout(20000) });
  if (r.status === 429) { await new Promise(x => setTimeout(x, 2000)); r = await fetch(u, { headers: { "User-Agent": UA, "Accept": "application/json" }, signal: AbortSignal.timeout(20000) }); }
  if (!r.ok) throw new Error("Annuaire HTTP " + r.status);
  const d = await r.json();
  for (const res of d.results || []) {
    const ets = (res.matching_etablissements || []).filter((e: any) => e.code_postal && (!e.etat_administratif || e.etat_administratif === "A") &&
      (dept.startsWith("2") && dept.length === 2 && /[AB]/.test(dept) ? e.code_postal.startsWith("20") : deptOf(e.code_postal) === dept));
    for (const e of ets.slice(0, 3)) {
      const name = cleanName(res, e); if (!name) continue;
      const full = name + " " + (res.nom_complet || "");
      if (KEEP[trade] && !KEEP[trade].test(full)) continue;
      if (DROP[trade] && DROP[trade].test(full)) continue;
      const naf = e.activite_principale || res.activite_principale || "";
      rows.push({
        source: "sirene", source_id: "siret:" + e.siret, siret: e.siret, trade: MODEL[trade] || trade, name,
        address: (e.adresse || "").replace(new RegExp("\\s*" + e.code_postal + ".*$"), "").trim() || null,
        postcode: e.code_postal, city: e.libelle_commune ? titleCase(e.libelle_commune) : null,
        lat: e.latitude ? +e.latitude : null, lon: e.longitude ? +e.longitude : null,
        phone: null, email: null, website: null,
        date_creation: res.date_creation || e.date_creation || null,
        segment: trade === "garage" ? (/^45\.11/.test(naf) ? "concession" : /^45\.40/.test(naf) ? "moto" : segOf(trade, naf, full) || "garage") : trade === "immobilier" ? "immobilier" : segOf(trade, naf, full),
        brand: CHAINS.test(name) || CHAINS.test(res.nom_complet || "") || (res.nombre_etablissements_ouverts || 0) > 5,
      });
    }
  }
  return { rows, total: Math.min(d.total_pages || 1, 400) };
}

const PARKED = /domain (is )?for sale|ce domaine est|nom de domaine est (à vendre|disponible)|parked|sedo|godaddy|dan\.com|buy this domain|hugedomains|site en construction|under construction|default web site page|index of \//i;
const noAccent = (x: string) => x.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
async function guessSite(p: { id: string; name: string; city: string | null; postcode?: string | null }) {
  const base = noAccent(p.name.toLowerCase()).replace(LEGAL, " ").replace(/&/g, " et ").replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
  if (base.length < 4) return null;
  const words = base.split(" ").filter(w => w.length >= 4);
  // 14/11/2026 : sans mot d'au moins 4 lettres (« B.w.b », « Ma.mo. »), impossible de vérifier → on ne devine pas
  if (!words.length) return null;
  const joined = base.replace(/ /g, ""), dashed = base.replace(/ /g, "-");
  const city = p.city ? noAccent(p.city.toLowerCase()).replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") : "";
  const cands = [...new Set([joined + ".fr", dashed + ".fr", joined + ".com", dashed + ".com", ...(city ? [dashed + "-" + city + ".fr", joined + city.replace(/-/g, "") + ".fr"] : [])])].filter(d => d.length <= 45).slice(0, 6);
  for (const d of cands) {
    try {
      const { html, url } = await get("https://" + d + "/");
      if (!html || PARKED.test(html.slice(0, 20000))) continue;
      const low = noAccent(html.toLowerCase());
      const hit = words.filter(w => low.includes(w)).length;
      const cityHit = p.city ? low.includes(noAccent(p.city.toLowerCase())) : false;
      const cpHit = p.postcode ? low.includes(String(p.postcode)) : false;
      // 14/11/2026 : la ville ou le code postal doit figurer sur la page, sauf si au moins 2 mots du nom y sont
      if (hit >= 1 && (cityHit || cpHit || (words.length >= 2 && hit >= 2))) return url;
    } catch { /* domaine absent */ }
  }
  return null;
}

async function get(url: string) {
  const r = await fetch(url, { headers: { "User-Agent": UA, "Accept": "text/html" }, redirect: "follow", signal: AbortSignal.timeout(9000) });
  if (!r.ok) throw new Error("HTTP " + r.status);
  const ct = r.headers.get("content-type") || "";
  if (!ct.includes("html") && !ct.includes("text")) return { html: "", url: r.url };
  return { html: (await r.text()).slice(0, 250_000), url: r.url };
}
function emailsIn(html: string) {
  const t = html.replace(/&#64;|&#x40;|\[at\]|\(at\)/gi, "@");
  const out = new Set<string>();
  for (const m of t.matchAll(EMAIL_RE)) { const e = m[0].toLowerCase().replace(/^mailto:/, "").replace(/\.$/, ""); if (!BAD.test(e) && e.length < 80) out.add(e); }
  return [...out];
}
function pickEmail(list: string[], host: string) {
  if (!list.length) return null; const dom = baseDomain(host);
  const sc = (e: string) => { const [l, d] = e.split("@"); let s = 0; if (baseDomain(d) === dom) s += 10; if (/^(contact|info|accueil|bonjour|hello|reservation|agence)/.test(l)) s += 3; if (/^(rgpd|dpo|webmaster|admin|support|compta|rh|jobs|privacy)/.test(l)) s -= 5; return s; };
  return [...list].sort((a, b) => sc(b) - sc(a))[0];
}
const phoneIn = (h: string) => (h.match(/(?:\+33\s?|0)[1-9](?:[\s.-]?\d{2}){4}/) || [null])[0];

function analyse(html: string, finalUrl: string) {
  html = html.slice(0, 150_000);
  const h = html.toLowerCase();
  const years = [...html.matchAll(/(?:©|&copy;|copyright)[^<]{0,40}?((?:19|20)\d{2})(?:\s*[-–]\s*((?:19|20)\d{2}))?/gi)].map(m => Math.max(+m[1], +(m[2] || 0)));
  const year = years.length ? Math.max(...years) : null;
  const gen = (html.match(/<meta[^>]+name=["']generator["'][^>]+content=["']([^"']+)/i) || [])[1] || null;
  const s = {
    https: finalUrl.startsWith("https://"),
    mobile: /<meta[^>]+name=["']viewport["']/i.test(html),
    year, generator: gen,
    free_host: FREE_HOST.test(finalUrl),
    frames: /<frameset|<frame\s/i.test(h),
    flash: /\.swf["']|shockwave/i.test(h),
    old_jquery: /jquery[.-]1\.[0-9]\b/i.test(h),
    words: h.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length,
  };
  const reasons: string[] = [];
  if (!s.mobile) reasons.push("pas adapté au téléphone");
  if (s.year && s.year <= new Date().getFullYear() - 4) reasons.push("copyright " + s.year);
  if (!s.https) reasons.push("pas sécurisé (http)");
  if (s.free_host) reasons.push("site gratuit / sous-domaine");
  if (s.frames || s.flash) reasons.push("technologie ancienne");
  if (s.old_jquery) reasons.push("code ancien");
  if (s.words < 60) reasons.push("presque vide");
  return { signals: { ...s, reasons }, dated: reasons.length > 0 };
}

const CONTACT_HINT = /contact|nous-contacter|contactez|mentions|legal|a-propos|qui-sommes|coordonn/i;
async function checkSite(p: { id: string; website: string; email: string | null }) {
  const u = new URL(p.website);
  let home: { html: string; url: string };
  try { home = await get(p.website); } catch {
    try { home = await get(u.origin + "/"); } catch (e) { return { id: p.id, site_status: "injoignable", signals: { error: String(e).slice(0, 120) }, email: null, phone: null }; }
  }
  if (!home.html) return { id: p.id, site_status: "injoignable", signals: { error: "pas une page web" }, email: null, phone: null };
  const a = analyse(home.html, home.url);
  const host = new URL(home.url).hostname;
  let emails = emailsIn(home.html); let phone = phoneIn(home.html);
  const good = () => pickEmail(emails, host)?.endsWith(baseDomain(host));
  if (!good()) {
    const links = new Set<string>();
    for (const m of home.html.matchAll(/href=["']([^"'#]+)["']/gi)) {
      try { const l = new URL(m[1], home.url); if (l.hostname.replace(/^www\./, "") === host.replace(/^www\./, "") && CONTACT_HINT.test(l.pathname)) links.add(l.href); } catch { /* lien invalide */ }
      if (links.size >= 6) break;
    }
    const origin = new URL(home.url).origin;
    for (const x of ["/contact", "/mentions-legales"]) links.add(origin + x);
    for (const l of [...links].slice(0, 4)) {
      try { const c = await get(l); emails = emails.concat(emailsIn(c.html)); phone ||= phoneIn(c.html); } catch { /* page absente */ }
      if (good()) break;
    }
  }
  return { id: p.id, site_status: a.dated ? "date" : "moderne", signals: a.signals, email: pickEmail([...new Set(emails)], host), phone };
}
function score(site: string, email: string | null, phone: string | null) {
  const e = !!email, t = !!phone;
  if (site === "aucun") return e ? 90 : t ? 70 : 40;
  if (site === "date") return e ? 85 : t ? 65 : 35;
  if (site === "injoignable") return e ? 60 : t ? 55 : 20;
  return 10;
}

async function search(body: any) {
  const { data: nx } = await db.rpc("cs_robot_next_page");
  const next = nx as { enabled: boolean; area: string | null; trade: string; page: number };
  if (!next.enabled && !body.manual) return { skipped: "robot arrêté" };
  if (!next.area) return { skipped: "France entière terminée" };
  const { area, trade } = next; let page = next.page, found = 0, inserted = 0, total = 1;
  try {
    for (let i = 0; i < 4; i++, page++) {
      const res = await sirene(area, trade, page); total = res.total;
      if (res.rows.length) {
        const { data: ins, error } = await db.rpc("cs_robot_upsert", { p_rows: res.rows });
        if (error) throw new Error(error.message);
        found += res.rows.length; inserted += (ins as number) || 0;
      }
      if (page >= total) { page++; break; }
      await new Promise(x => setTimeout(x, 300));
    }
    await db.rpc("cs_robot_page_done", { p_area: area, p_trade: trade, p_next: page, p_total: total, p_done: page > total });
    await db.rpc("cs_robot_log", { p_kind: "recherche", p_trade: trade, p_area: area, p_found: found, p_inserted: inserted, p_checked: 0, p_ok: true, p_error: null });
    return { area, trade, found, inserted, next_page: page, total };
  } catch (e) {
    await db.rpc("cs_robot_page_done", { p_area: area, p_trade: trade, p_next: page, p_total: total, p_done: false });
    await db.rpc("cs_robot_log", { p_kind: "recherche", p_trade: trade, p_area: area, p_found: found, p_inserted: inserted, p_checked: 0, p_ok: false, p_error: String(e).slice(0, 300) });
    return { area, trade, error: String(e) };
  }
}

// ── mode "nouveaux" : créations d'entreprises publiées au BODACC (journal officiel, gratuit, chaque jour) ──
// Garages, concessions auto, motos et agences immobilières qui viennent de s'immatriculer, souvent avant même
// d'ouvrir (date de début d'activité dans le futur) : ils n'ont presque jamais de site. Le crawl vérifie ensuite.
const BODACC = "https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records";
const BKEYS = ["véhicules", "véhicule", "automobiles", "automobile", "voitures", "motos", "motocycles", "scooters", "immobilier", "immobilière", "immobilières", "transactions"];
const na = (x: string) => noAccent((x || "").toLowerCase());
const GOODS = /piece|accessoire|equipement|pneu|produit|fourniture|jante|lubrifiant/;
function classify(raw: string): string | null {
  const t = na(raw).replace(/\s+/g, " ");
  const immo = /transactions? (sur )?(immeubles|immobilieres?)|agen(ce|t)s? immobili|mandataire[^.;]{0,30}immobili|negociat(ion|eur)s? immobili|intermediai(re|tion)[^.;]{0,50}immobili|entremise[^.;]{0,60}immobili|gestion locative|administration de biens|courtage[^.;]{0,30}immobili/.test(t)
    && !/hors (activite de )?transaction|sans exercice d.activites? de transaction/.test(t);
  if (immo) return "immobilier";
  const mo = /\bmotos?\b|motocycl|scooters?|deux[- ]roues/.test(t) && /(vente|negoce|commerce|reparation|entretien|mecanique|atelier|concession)/.test(t) && !/conseil[^.;]{0,40}moto/.test(t);
  let sale = false;
  for (const m of t.matchAll(/(achat|vente|revente|negoce|commerce(?: de detail| de gros)?|depot[- ]vente|import(?:ation)?)([^.;]{0,45}?)(vehicules?|automobiles?|voitures?)/g)) {
    const before = t.slice(Math.max(0, (m.index || 0) - 30), m.index);
    if (!GOODS.test(m[2]) && !/conseil|accompagnement|annonces/.test(before + m[2])) { sale = true; break; }
  }
  const repair = /(reparation|entretien|mecanique|carrosserie|diagnostic|maintenance|vidange)[^.;]{0,40}(vehicules?|automobiles?|voitures?|\bauto\b)|mecanique (generale|automobile)|garage automobile/.test(t)
    && !/sans (aucune )?(entretien|intervention|reparation|mecanique)|hors mecanique/.test(t);
  if (mo) return "moto";
  if (repair) return "garage";
  if (sale && !/sans achat ni (re)?vente|plateforme[^.;]{0,40}annonces/.test(t)) return "concession";
  return null;
}
function jparse(x: any) { try { return typeof x === "string" ? JSON.parse(x) : x; } catch { return null; } }
function bodaccRow(r: any) {
  const ets = jparse(r.listeetablissements)?.etablissement; const e = Array.isArray(ets) ? ets[0] : ets;
  const act = [e?.activite, ...(Array.isArray(ets) ? ets.slice(1).map((x: any) => x?.activite) : [])].filter(Boolean).join(" - ");
  const seg = classify(act); if (!seg) return null;
  const per = jparse(r.listepersonnes)?.personne; const pp = Array.isArray(per) ? per[0] : per;
  const one = (v: unknown) => String(Array.isArray(v) ? v[0] ?? "" : v ?? ""); // 09/11 : certains champs BODACC sont des listes
  let name = one(pp?.nomCommercial) || one(e?.enseigne) || one(pp?.denomination);
  if (!name && pp?.nom) name = `${one(pp.prenom).split(",")[0].trim()} ${one(pp.nom)}`.trim();
  if (!name) name = one(r.commercant); name = name.replace(/\s+/g, " ").trim(); if (!name) return null;
  if (name === name.toUpperCase()) name = titleCase(name);
  const ad = e?.adresse || {};
  const siren = ((r.registre || [])[0] || "").replace(/\D/g, ""); if (siren.length !== 9) return null;
  const acte = jparse(r.acte) || {};
  return {
    source: "bodacc", source_id: "siren:" + siren, siret: siren, trade: seg === "immobilier" ? "immobilier" : "garage", segment: seg,
    name, address: [ad.numeroVoie, ad.typeVoie, ad.nomVoie].filter(Boolean).join(" ") || null,
    postcode: ad.codePostal || r.cp || null, city: ad.ville ? titleCase(ad.ville) : (r.ville || null), lat: null, lon: null,
    phone: null, email: null, website: null, activite: act.slice(0, 600),
    date_creation: acte.dateImmatriculation || r.dateparution || null, date_debut: acte.dateCommencementActivite || null,
    brand: CHAINS.test(name) || /\b(iad|safti|capifrance|optimhome|megagence|proprietes privees)\b/i.test(na(act)),
  };
}
async function nouveaux(body: any) {
  const { data: cur } = await db.rpc("cs_robot_bodacc_cursor");
  const c = cur as { enabled: boolean; day: string; offset: number };
  if (!c?.enabled && !body.manual) return { skipped: "robot arrêté" };
  let day = c.day, off = c.offset || 0, seen = 0, kept = 0, inserted = 0;
  const today = new Date().toISOString().slice(0, 10);
  const where = (d: string) => `familleavis="creation" and dateparution=date'${d}' and (` + BKEYS.map(k => `search(listeetablissements,"${k}")`).join(" or ") + ")";
  try {
    for (let i = 0; i < 8; i++) {
      if (day > today) break;
      const u = `${BODACC}?where=${encodeURIComponent(where(day))}&order_by=numeroannonce&limit=100&offset=${off}&select=registre,commercant,cp,ville,dateparution,listepersonnes,listeetablissements,acte`;
      const r = await fetch(u, { headers: { "User-Agent": UA, "Accept": "application/json" }, signal: AbortSignal.timeout(25000) });
      if (!r.ok) throw new Error("BODACC HTTP " + r.status);
      const d = await r.json(); const res = d.results || []; seen += res.length;
      const rows = res.map(bodaccRow).filter(Boolean);
      kept += rows.length;
      if (rows.length) { const { data: n, error } = await db.rpc("cs_robot_upsert", { p_rows: rows }); if (error) throw new Error(error.message); inserted += (n as number) || 0; }
      if (res.length === 100 && off + 100 < 10000) off += 100;
      else if (day < today) { day = new Date(Date.parse(day) + 864e5).toISOString().slice(0, 10); off = 0; }
      else { off = 0; break; } // aujourd'hui : on repassera plus tard
    }
    await db.rpc("cs_robot_bodacc_save", { p_day: day, p_offset: off });
    await db.rpc("cs_robot_log", { p_kind: "nouveaux", p_trade: null, p_area: day, p_found: kept, p_inserted: inserted, p_checked: seen, p_ok: true, p_error: null });
    return { day, offset: off, seen, kept, inserted };
  } catch (e) {
    await db.rpc("cs_robot_bodacc_save", { p_day: day, p_offset: off });
    await db.rpc("cs_robot_log", { p_kind: "nouveaux", p_trade: null, p_area: day, p_found: kept, p_inserted: inserted, p_checked: seen, p_ok: false, p_error: String(e).slice(0, 300) });
    return { day, error: String(e) };
  }
}

async function crawl(body: any) {
  const { data: st } = await db.rpc("cs_robot_crawl_settings");
  if (!(st as any)?.enabled && !body.manual) return { skipped: "robot arrêté" };
  const out: Record<string, unknown> = {};
  // 1) retrouver le site des pros
  const { data: tg } = await db.rpc("cs_robot_to_guess", { p_limit: 4 });
  const glist = (tg as any[]) || []; let guessed = 0;
  const gres = await Promise.all(glist.map(async p => ({ id: p.id, w: await guessSite(p).catch(() => null) })));
  for (const r of gres) { await db.rpc("cs_robot_save_guess", { p_id: r.id, p_website: r.w }); if (r.w) guessed++; }
  out.sites_found = guessed;
  // 2) lire les sites (accueil + contact / mentions légales) et relever l'e-mail
  const { data: todo } = await db.rpc("cs_robot_to_check", { p_limit: 4 });
  const list = (todo as any[]) || []; let checked = 0, emails = 0;
  const res = await Promise.all(list.map(p => checkSite(p).catch(e => ({ id: p.id, site_status: "injoignable", signals: { error: String(e).slice(0, 120) }, email: null, phone: null }))));
  for (const r of res) {
    const src = list.find(x => x.id === r.id);
    await db.rpc("cs_robot_save_check", { p_id: r.id, p_site_status: r.site_status, p_signals: r.signals, p_email: r.email, p_phone: r.phone, p_score: score(r.site_status, src?.email || r.email, r.phone) });
    checked++; if (r.email) emails++;
  }
  out.checked = checked; out.emails = emails;
  if (checked || guessed) await db.rpc("cs_robot_log", { p_kind: "sites", p_trade: null, p_area: null, p_found: guessed, p_inserted: emails, p_checked: checked, p_ok: true, p_error: null });
  return out;
}

Deno.serve(async (req) => {
  const key = req.headers.get("x-internal-key") || "";
  const { data: ok } = await db.rpc("cs_robot_key_ok", { p_key: key });
  if (!ok) return json({ error: "forbidden" }, 403);
  const body = await req.json().catch(() => ({}));
  if (body.mode === "crawl") return json(await crawl(body));
  if (body.mode === "search") return json(await search(body));
  if (body.mode === "nouveaux") return json(await nouveaux(body));
  if (body.mode === "classify") return json((body.texts || []).map((t: string) => classify(t)));
  // lancement manuel depuis l'espace admin : une recherche puis une lecture de sites
  return json({ search: await search(body), crawl: await crawl(body) });
});
