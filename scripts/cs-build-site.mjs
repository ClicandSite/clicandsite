// MyCreativeSite · générateur des sites clients en vraies pages HTML (SEO) — 09/11/2026 (demande d'Anthony : « SEO béton »).
// Usage : node cs-build-site.mjs --slug garage-dupont --domain garage-dupont.fr --out ./site
//   options de test : --content contenu.json (au lieu de l'API), --base ./ (modèles et scripts lus en local)
// Produit : index.html (contenu du pro écrit dans la page, pas ajouté après coup), une page par véhicule / bien
// (/vehicules/… ou /biens/…), données structurées schema.org, balises de partage, sitemap.xml, robots.txt, 404.html, CNAME.
// Le site garde ses scripts (filtres, fiche, demandes « Mes clients ») et se remet à jour en direct entre deux générations.
import { JSDOM } from 'jsdom';
import fs from 'node:fs/promises';
import path from 'node:path';

const API = 'https://avcynjwcyygygkjuxsdt.supabase.co';
const KEY = 'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO';
const SITE = 'https://mycreativesite.fr';
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > 0 ? process.argv[i + 1] : d; };
const slug = arg('slug'), domain = (arg('domain') || '').replace(/^https?:\/\//, '').replace(/\/$/, ''), out = arg('out', './site'), base = arg('base');
if (!slug || !domain) { console.error('--slug et --domain obligatoires'); process.exit(2); }
const ORIGIN = 'https://' + domain;

async function get(rel) {
  if (base) return fs.readFile(path.join(base, rel), 'utf8');
  const r = await fetch(SITE + '/' + rel + (rel.includes('?') ? '&' : '?') + 't=' + Date.now()); if (!r.ok) throw new Error(rel + ' : ' + r.status); return r.text();
}
async function content() {
  const f = arg('content'); if (f) return JSON.parse(await fs.readFile(f, 'utf8'));
  const r = await fetch(API + '/rest/v1/rpc/cs_site_content', { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY }, body: JSON.stringify({ p_slug: slug }) });
  const c = r.ok ? await r.json() : null; if (!c) throw new Error('Site introuvable ou pas encore en ligne : ' + slug); return c;
}
async function siteInfo() {
  if (arg('content')) return JSON.parse(await fs.readFile(arg('content'), 'utf8'))._site || {};
  const r = await fetch(API + '/rest/v1/rpc/cs_site_public_info', { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY }, body: JSON.stringify({ p_slug: slug }) });
  return r.ok ? (await r.json()) || {} : {};
}

// ---- utilitaires
const clean = (s) => String(s ?? '').replace(/\s+/g, ' ').trim();
const cut = (s, n) => { s = clean(s); return s.length > n ? s.slice(0, n - 1).replace(/[\s,;:.]+\S*$/, '') + '…' : s; };
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const slugify = (s) => clean(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
const isUrl = (u) => typeof u === 'string' && /^https:\/\/\S+$/i.test(u);
const priceNum = (p) => { const d = String(p ?? '').replace(/\s/g, '').match(/(\d+(?:[.,]\d{1,2})?)/); return d ? Math.round(Number(d[1].replace(',', '.'))) : null; };
const today = new Date().toISOString().slice(0, 10);

// Adresse « 45 avenue X, 06110 Le Cannet » → éléments PostalAddress
function addr(a) { a = clean(a); const m = a.match(/^(.*?)[,\s]+(\d{5})\s+(.+)$/); return m ? { street: m[1].replace(/,$/, ''), cp: m[2], city: m[3] } : { street: a, cp: '', city: '' }; }
// Horaires « Lundi au vendredi » / « 8h–12h · 14h–18h30 » → openingHoursSpecification
const DAYS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'];
const DAY_EN = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
function hoursSpec(rows) {
  const spec = [];
  for (const r of rows || []) {
    const l = clean(r.l).toLowerCase(), v = clean(r.v).toLowerCase(); if (!l || /ferm/.test(v)) continue;
    let ds = [];
    const range = l.match(/(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\s*(?:au|-|–|à)\s*(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)/);
    if (range) { const a = DAYS.indexOf(range[1]), b = DAYS.indexOf(range[2]); for (let i = a; i <= b; i++) ds.push(i); }
    else DAYS.forEach((d, i) => { if (l.includes(d)) ds.push(i); });
    if (/tous les jours|7j|7 j/.test(l)) ds = [0, 1, 2, 3, 4, 5, 6];
    if (!ds.length) continue;
    if (/24\s*h|24\/24/.test(v)) { spec.push({ '@type': 'OpeningHoursSpecification', dayOfWeek: ds.map((i) => DAY_EN[i]), opens: '00:00', closes: '23:59' }); continue; }
    const t = (x) => { const m = x.match(/(\d{1,2})\s*h\s*(\d{2})?/); return m ? m[1].padStart(2, '0') + ':' + (m[2] || '00') : null; };
    for (const seg of v.split(/[·,\/]|\bet\b/)) { const p = seg.split(/[–-]|à/); if (p.length < 2) continue; const o = t(p[0]), c = t(p[1]); if (o && c) spec.push({ '@type': 'OpeningHoursSpecification', dayOfWeek: ds.map((i) => DAY_EN[i]), opens: o, closes: c }); }
  }
  return spec;
}
const TYPE = { garage: ['AutoRepair', 'AutoDealer'], immobilier: ['RealEstateAgent'], restaurant: ['Restaurant'], beaute: ['BeautySalon'], bienetre: ['HealthAndBeautyBusiness'], veterinaire: ['VeterinaryCare'], autoecole: ['DrivingSchool'], coach: ['SportsActivityLocation'], photographe: ['ProfessionalService'], toiletteur: ['LocalBusiness'], fleuriste: ['Florist'], traiteur: ['FoodEstablishment'], nautisme: ['LocalBusiness'], kine: ['MedicalBusiness'], dentiste: ['Dentist'], bijouterie: ['JewelryStore'], liberal: ['AccountingService'], services: ['HomeAndConstructionBusiness'], evenementiel: ['LocalBusiness'], hebergement: ['BedAndBreakfast'], tourisme: ['TravelAgency'], location: ['AutoRental', 'MovingCompany'], infirmier: ['MedicalBusiness'], boulangerie: ['Bakery'], batiment: ['GeneralContractor'], depannage: ['Plumber', 'Electrician'], boutique: ['Store'], vtc: ['TaxiService'] };
const METIER = { garage: 'Garage auto et moto', immobilier: 'Agence immobilière', restaurant: 'Restaurant', beaute: 'Coiffure et beauté', bienetre: 'Bien-être et soins', veterinaire: 'Clinique vétérinaire', autoecole: 'Auto-école', coach: 'Coach sportif', photographe: 'Photographe', toiletteur: 'Toilettage pour chiens et chats', fleuriste: 'Fleuriste', traiteur: 'Traiteur', nautisme: 'Location de bateaux', kine: 'Cabinet de kinésithérapie', dentiste: 'Cabinet dentaire', bijouterie: 'Bijouterie-horlogerie', liberal: 'Cabinet de conseil', services: 'Services à domicile', evenementiel: 'Organisation d\'événements', hebergement: 'Chambres d\'hôtes et gîte', tourisme: 'Tourisme et loisirs', location: 'Location et déménagement', infirmier: 'Cabinet infirmier', boulangerie: 'Boulangerie pâtisserie', batiment: 'Artisan du bâtiment', depannage: 'Plombier électricien, dépannage', boutique: 'Boutique', vtc: 'Chauffeur VTC' };

async function main() {
  const c = await content(), info = await siteInfo();
  const trade = info.trade || c._trade || 'garage';
  const conc = trade === 'garage' && c.concession === true;
  const tpl = await get('modeles/' + trade + '.html');
  const csEdit = await get('assets/cs-edit.js');
  const dom = new JSDOM(tpl, { runScripts: 'outside-only', url: ORIGIN + '/' });
  const { window } = dom, doc = window.document;
  window.eval(csEdit);
  window.CSEdit.apply(doc, c);
  const q = (s, r = doc) => r.querySelector(s), qa = (s, r = doc) => [...r.querySelectorAll(s)];
  const T = c.text || {};

  // ---- Nettoyage : tout ce qui n'a rien à faire sur un vrai site
  qa('meta[name="robots"], meta[name^="claude:"]').forEach((e) => e.remove());
  qa('.picker').forEach((e) => e.remove());
  qa('script').forEach((s) => { const t = s.textContent || '', src = s.getAttribute('src') || '';
    if (/pk-grid|concession=1|atelier=1|taxi=1|moto=1|cs-formule|classList\.add\("embed"\)/.test(t) || /cs-formule/.test(src)) s.remove(); });
  qa('style').forEach((s) => { if (/\.embed \.picker|pk-grid/.test(s.textContent)) s.remove(); });
  qa('.note').forEach((n) => { if (/exemple|d'exemple|Démonstration/i.test(n.textContent)) n.remove(); });
  qa('.ok').forEach((o) => { if (/Démonstration/i.test(o.textContent)) o.textContent = 'Merci, votre demande est envoyée. Nous vous recontactons rapidement.'; });
  doc.documentElement.setAttribute('lang', 'fr');
  if (c.style) doc.documentElement.setAttribute('data-style', String(c.style).replace(/[^a-z]/g, ''));

  // ---- Identité
  const name = clean(info.name) || clean(T.logo) || clean(q('header.top .logo')?.textContent) || domain;
  // Pied de page encore d'origine (« … d'exemple ») : nom du pro
  const ft = q('footer .wrap > span:first-child'); if (ft && /exemple/i.test(ft.textContent)) ft.textContent = '© ' + new Date().getFullYear() + ' ' + name;
  const A = addr(T.address || q('.addr .v')?.textContent);
  const city = A.city;
  const phone = (c.contacts || []).find((x) => /t[ée]l/i.test(x.l) || /^[+\d][\d\s.]{8,}$/.test(clean(x.v)))?.v;
  const email = (c.contacts || []).find((x) => /@/.test(x.v))?.v;
  const metier = trade === 'garage' ? (conc ? (c.moto === true ? 'Concession moto' : 'Concession automobile') : c.atelier === true ? 'Garage, entretien et réparation automobile' : 'Garage et concession auto et moto') : trade === 'vtc' && c.taxi === true ? 'Taxi' : METIER[trade] || '';
  const items = (Array.isArray(c.items) ? c.items : []).filter((o) => o && clean(o.t));
  const isCar = trade === 'garage', isImmo = trade === 'immobilier', withPages = isCar || isImmo;
  const dir = isImmo ? 'biens' : 'vehicules';
  const photosOf = (o) => [...new Set([o.img, ...(Array.isArray(o.photos) ? o.photos : [])].filter(isUrl))];
  const heroImg = isUrl(c.photos?.hero) ? c.photos.hero : items.map(photosOf).flat()[0] || null;

  // Pages des annonces : adresse stable et lisible
  const used = new Set();
  const pages = withPages ? items.filter((o) => !/vendu|loué|loue/i.test(o.tag || '')).map((o) => {
    let s = slugify([o.t, o.sp?.an, o.ref].filter(Boolean).join(' ')) || 'annonce'; let k = s, n = 2; while (used.has(k)) k = s + '-' + n++; used.add(k);
    return { o, url: '/' + dir + '/' + k + '/' };
  }) : [];
  const pageOf = new Map(pages.map((p) => [p.o, p.url]));

  // Lien vers la page de chaque annonce dans la carte (Google suit les liens ; le clic ouvre la page)
  qa('.vgrid > .car, .props > .prop').forEach((card, i) => { const o = items[i], u = o && pageOf.get(o); const h = q('h3', card);
    if (u && h && !q('a', h)) { const a = doc.createElement('a'); a.href = u; a.setAttribute('data-cs-page', ''); a.textContent = h.textContent; a.style.cssText = 'color:inherit;text-decoration:none'; h.textContent = ''; h.appendChild(a); } });
  // Images des cartes : la photo est un fond CSS ; on ajoute un texte alternatif lisible
  qa('.vgrid > .car .photo, .props > .prop .photo').forEach((p, i) => { const o = items[i]; if (o) { p.setAttribute('role', 'img'); p.setAttribute('aria-label', clean(o.t) + (city ? ' à ' + city : '')); } });

  // ---- Balises de la page d'accueil
  const title = cut(name + ' · ' + metier + (city ? ' à ' + city : ''), 65);
  const desc = cut([T.subtitle, isCar && pages.length ? pages.length + ' véhicule' + (pages.length > 1 ? 's' : '') + ' en stock.' : '', isImmo && pages.length ? pages.length + ' bien' + (pages.length > 1 ? 's' : '') + ' à vendre et à louer.' : '', city ? 'À ' + city + '.' : ''].filter(Boolean).join(' '), 158);
  const org = {
    '@context': 'https://schema.org', '@type': TYPE[trade] ? (conc ? ['AutoDealer'] : TYPE[trade]) : 'LocalBusiness', '@id': ORIGIN + '/#entreprise',
    name, url: ORIGIN + '/', description: cut(T.subtitle, 300) || undefined, telephone: phone ? clean(phone) : undefined, email: email ? clean(email) : undefined,
    image: heroImg || undefined, logo: isUrl(c.photos?.icon) ? c.photos.icon : undefined,
    address: A.street || A.city ? { '@type': 'PostalAddress', streetAddress: A.street || undefined, postalCode: A.cp || undefined, addressLocality: A.city || undefined, addressCountry: 'FR' } : undefined,
    areaServed: city || undefined, openingHoursSpecification: hoursSpec(c.hours).length ? hoursSpec(c.hours) : undefined,
    sameAs: [c.google?.url].filter(isUrl).length ? [c.google.url] : undefined,
  };
  const score = parseFloat(String(c.google?.score || '').replace(',', '.')), count = parseInt(c.google?.count, 10);
  if (score > 0 && score <= 5 && count > 0) org.aggregateRating = { '@type': 'AggregateRating', ratingValue: score, reviewCount: count, bestRating: 5 };
  setHead(doc, { title, desc, url: ORIGIN + '/', img: heroImg, type: 'website', jsonld: [org, pages.length ? { '@context': 'https://schema.org', '@type': 'ItemList', name: isImmo ? 'Biens à vendre et à louer' : 'Véhicules en stock', itemListElement: pages.map((p, i) => ({ '@type': 'ListItem', position: i + 1, url: ORIGIN + p.url, name: clean(p.o.t) })) } : null] });
  // Script du site : demandes « Mes clients » et mise à jour en direct du contenu
  const live = doc.createElement('script'); live.src = SITE + '/assets/cs-edit.js?v=27'; live.setAttribute('data-site', slug); live.defer = true; doc.body.appendChild(live); if (!q('script[src*="cs-date.js"]')) { const dj = doc.createElement('script'); dj.src = SITE + '/assets/cs-date.js?v=4'; dj.defer = true; doc.body.appendChild(dj); }
  // 10/11/2026 (Anthony) : lien discret « Espace pro » en bas du site (le pro modifie son site depuis son-domaine/admin)
  const fw = q('footer .wrap');
  if (fw && !q('a[data-cs-admin]', fw)) { const ap = doc.createElement('a'); ap.href = '/admin/'; ap.rel = 'nofollow'; ap.setAttribute('data-cs-admin', ''); ap.textContent = 'Espace pro'; ap.style.cssText = 'opacity:.55;font-size:.8em;color:inherit;text-decoration:none;margin-left:12px'; fw.appendChild(ap); }
  const home = dom.serialize();

  // ---- Pages des annonces
  const files = [['index.html', home]];
  for (const p of pages) files.push([p.url.slice(1) + 'index.html', itemPage(tpl, csEdit, c, p, { name, city, A, phone, email, trade, isImmo, org, domain })]);
  files.push(['404.html', `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=/"><title>${esc(name)}</title></head><body><a href="/">${esc(name)}</a></body></html>`]);
  files.push(['robots.txt', `User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /espace/\n\nSitemap: ${ORIGIN}/sitemap.xml\n`]);
  files.push(['sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>${ORIGIN}/</loc><lastmod>${today}</lastmod><priority>1.0</priority></url>\n${pages.map((p) => `  <url><loc>${ORIGIN}${p.url}</loc><lastmod>${today}</lastmod><priority>0.8</priority></url>`).join('\n')}\n</urlset>\n`]);
  files.push(['CNAME', domain + '\n']);
  // 10/11/2026 (Anthony) : son-domaine/admin (et /espace) mène directement à l'espace client du pro
  const toEspace = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=${SITE}/espace/?site=${encodeURIComponent(slug)}"><title>Espace pro · ${esc(name)}</title><script>location.replace(${JSON.stringify(SITE + '/espace/?site=' + encodeURIComponent(slug))});</script></head><body><a href="${SITE}/espace/?site=${encodeURIComponent(slug)}">Ouvrir mon espace pro</a></body></html>`;
  files.push(['admin/index.html', toEspace]); files.push(['espace/index.html', toEspace]);
  files.push(['.nojekyll', '']);
  // Les anciennes pages d'annonces (vendues, retirées) sont supprimées
  for (const d of ['vehicules', 'biens']) await fs.rm(path.join(out, d), { recursive: true, force: true });
  for (const [f, body] of files) { const fp = path.join(out, f); await fs.mkdir(path.dirname(fp), { recursive: true }); await fs.writeFile(fp, body); }
  console.log(JSON.stringify({ ok: true, slug, domain, pages: pages.length, files: files.length }));
}

function setHead(doc, m) {
  const head = doc.head, q = (s) => head.querySelector(s);
  let t = q('title'); if (!t) { t = doc.createElement('title'); head.appendChild(t); } t.textContent = m.title;
  const meta = (attr, k, v) => { if (!v) return; let e = head.querySelector(`meta[${attr}="${k}"]`); if (!e) { e = doc.createElement('meta'); e.setAttribute(attr, k); head.appendChild(e); } e.setAttribute('content', v); };
  meta('name', 'description', m.desc); meta('name', 'robots', 'index, follow, max-image-preview:large');
  meta('property', 'og:type', m.type); meta('property', 'og:title', m.title); meta('property', 'og:description', m.desc); meta('property', 'og:url', m.url); meta('property', 'og:locale', 'fr_FR'); meta('property', 'og:image', m.img);
  meta('name', 'twitter:card', m.img ? 'summary_large_image' : 'summary');
  let l = q('link[rel="canonical"]'); if (!l) { l = doc.createElement('link'); l.rel = 'canonical'; head.appendChild(l); } l.href = m.url;
  for (const j of (m.jsonld || []).filter(Boolean)) { const s = doc.createElement('script'); s.type = 'application/ld+json'; s.textContent = JSON.stringify(j, (k, v) => (v === undefined || (Array.isArray(v) && !v.length) ? undefined : v)); head.appendChild(s); }
}

// Page d'une annonce : même en-tête, mêmes couleurs, contenu complet écrit dans la page
function itemPage(tpl, csEdit, c, p, ctx) {
  const dom = new JSDOM(tpl, { runScripts: 'outside-only', url: 'https://x/' }); const { window } = dom, doc = window.document;
  window.eval(csEdit); window.CSEdit.apply(doc, c);
  const q = (s, r = doc) => r.querySelector(s), qa = (s, r = doc) => [...r.querySelectorAll(s)];
  const o = p.o, sp = o.sp && typeof o.sp === 'object' ? o.sp : {};
  const imgs = [...new Set([o.img, ...(Array.isArray(o.photos) ? o.photos : [])].filter(isUrl))];
  qa('meta[name="robots"], meta[name^="claude:"]').forEach((e) => e.remove());
  qa('.picker').forEach((e) => e.remove());
  // On ne garde que le style, l'en-tête et le pied de page
  qa('script').forEach((s) => { const t = s.textContent || ''; if (!/A=\["data-l"/.test(t)) s.remove(); });
  [...doc.body.children].forEach((e) => { if (!e.matches('header.top, footer, .cta, .mbar, script, style')) e.remove(); });
  qa('style').forEach((s) => { if (/\.embed \.picker|pk-grid/.test(s.textContent)) s.remove(); });
  const ft = q('footer .wrap > span:first-child'); if (ft && /exemple/i.test(ft.textContent)) ft.textContent = '© ' + new Date().getFullYear() + ' ' + ctx.name;
  if (c.style) doc.documentElement.setAttribute('data-style', String(c.style).replace(/[^a-z]/g, ''));
  doc.documentElement.setAttribute('lang', 'fr');
  qa('header.top a[href^="#"], .cta a[href^="#"], .mbar a[href^="#"]').forEach((a) => a.setAttribute('href', '/' + a.getAttribute('href')));
  const logo = q('header.top .logo'); if (logo && !q('a', logo)) { const a = doc.createElement('a'); a.href = '/'; a.style.cssText = 'color:inherit;text-decoration:none'; a.textContent = logo.textContent; logo.textContent = ''; logo.appendChild(a); }

  const price = clean(o.p), specs = String(o.specs || '').split('\n').map((l) => { const k = l.indexOf(' : '); return k > 0 ? [l.slice(0, k), l.slice(k + 3)] : null; }).filter(Boolean);
  const where = clean(sp.vi || o.city || ctx.city);
  const title = cut(clean(o.t) + (price ? ' · ' + price : '') + ' · ' + ctx.name + (where ? ' à ' + where : ''), 70);
  const desc = cut([clean(o.meta), clean(o.desc)].filter(Boolean).join('. '), 158) || title;
  const url = 'https://' + ctx.domain + p.url;
  const nb = priceNum(o.p);
  const sold = /réserv|compromis/i.test(o.tag || '');
  let ld;
  if (ctx.isImmo) {
    ld = { '@context': 'https://schema.org', '@type': 'RealEstateListing', name: clean(o.t), url, description: cut(o.desc, 1000) || undefined, image: imgs, datePosted: today,
      about: { '@type': o.type === 'maison' ? 'House' : o.type === 'appartement' ? 'Apartment' : 'Accommodation', numberOfRooms: Number(o.rooms) || undefined, floorSize: Number(String(sp.su || '').replace(',', '.')) ? { '@type': 'QuantitativeValue', value: Number(String(sp.su).replace(',', '.')), unitCode: 'MTK' } : undefined, address: { '@type': 'PostalAddress', addressLocality: where || undefined, postalCode: sp.cp || undefined, addressCountry: 'FR' } },
      offers: nb ? { '@type': 'Offer', price: nb, priceCurrency: 'EUR', businessFunction: o.tr === 'location' ? 'http://purl.org/goodrelations/v1#LeaseOut' : 'http://purl.org/goodrelations/v1#Sell', availability: sold ? 'https://schema.org/LimitedAvailability' : 'https://schema.org/InStock', seller: { '@id': 'https://' + ctx.domain + '/#entreprise' } } : undefined };
  } else {
    const moto = /moto|scooter/i.test(sp.ty || '');
    ld = { '@context': 'https://schema.org', '@type': moto ? 'Motorcycle' : 'Car', name: clean(o.t), url, description: cut(o.desc, 1000) || undefined, image: imgs,
      brand: sp.mk || o.mk ? { '@type': 'Brand', name: clean(sp.mk || o.mk) } : undefined, model: sp.mo || undefined, vehicleModelDate: sp.an || undefined, productionDate: sp.an || undefined,
      mileageFromOdometer: String(sp.km || '').trim() ? { '@type': 'QuantitativeValue', value: Number(String(sp.km).replace(/\D/g, '')), unitCode: 'KMT' } : undefined,
      fuelType: sp.fu || o.fuel || undefined, vehicleTransmission: sp.bo || undefined, color: sp.co || undefined, numberOfDoors: Number(sp.po) || undefined, seatingCapacity: Number(sp.pl) || undefined, bodyType: sp.ty || undefined,
      vehicleEngine: Number(sp.ch) ? { '@type': 'EngineSpecification', enginePower: { '@type': 'QuantitativeValue', value: Number(sp.ch), unitCode: 'BHP' } } : undefined,
      itemCondition: 'https://schema.org/UsedCondition',
      offers: nb ? { '@type': 'Offer', price: nb, priceCurrency: 'EUR', availability: sold ? 'https://schema.org/LimitedAvailability' : 'https://schema.org/InStock', itemCondition: 'https://schema.org/UsedCondition', seller: { '@id': 'https://' + ctx.domain + '/#entreprise' }, url } : undefined };
  }
  const crumbs = { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: [{ '@type': 'ListItem', position: 1, name: ctx.name, item: 'https://' + ctx.domain + '/' }, { '@type': 'ListItem', position: 2, name: ctx.isImmo ? 'Nos biens' : 'Nos véhicules', item: 'https://' + ctx.domain + '/#' + (ctx.isImmo ? 'biens' : 'vehicules') }, { '@type': 'ListItem', position: 3, name: clean(o.t), item: url }] };
  setHead(doc, { title, desc, url, img: imgs[0], type: 'product', jsonld: [ctx.org, ld, crumbs] });

  const main = doc.createElement('main'); main.className = 'cs-page';
  const back = ctx.isImmo ? 'Tous nos biens' : 'Tous nos véhicules';
  const dpe = (L, v, u) => /^[A-G]$/.test(L || '') ? `<div class="cs-en"><b class="cs-l cs-${L}">${L}</b><span>${v ? esc(v) + ' ' + u : ''}</span></div>` : '';
  main.innerHTML = `
  <div class="wrap">
    <nav class="cs-bc" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/#${ctx.isImmo ? 'biens' : 'vehicules'}">${back}</a> › <span>${esc(clean(o.t))}</span></nav>
    <div class="cs-grid">
      <div>
        <h1>${esc(clean(o.t))}</h1>
        ${clean(o.meta) ? `<p class="cs-meta">${clean(o.meta).split('·').map((s) => `<span>${esc(clean(s))}</span>`).join('')}</p>` : ''}
        ${imgs.length ? `<div class="cs-gal">${imgs.map((u, i) => `<img src="${esc(u)}" alt="${esc(clean(o.t) + (i ? ' – photo ' + (i + 1) : '') + (where ? ' – ' + where : ''))}" ${i ? 'loading="lazy"' : 'fetchpriority="high"'} width="1200" height="900">`).join('')}</div>` : ''}
        ${specs.length ? `<h2>${ctx.isImmo ? 'Le bien en détail' : 'Fiche technique'}</h2><dl class="cs-specs">${specs.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl>` : ''}
        ${clean(o.desc) ? `<h2>Description</h2>${String(o.desc).split(/\n+/).map((l) => clean(l)).filter(Boolean).map((l) => `<p>${esc(l)}</p>`).join('')}` : ''}
        ${clean(o.feats) ? `<h2>${ctx.isImmo ? 'Prestations' : 'Équipements'}</h2><ul class="cs-feats">${String(o.feats).split(/\n|·/).map((l) => clean(l)).filter(Boolean).map((l) => `<li>${esc(l)}</li>`).join('')}</ul>` : ''}
        ${ctx.isImmo ? `<h2>Performance énergétique</h2>${dpe(o.dpe, o.dpe_v, 'kWh/m²/an') + dpe(o.ges, o.ges_v, 'kg CO₂/m²/an') || '<p>DPE en cours de réalisation.</p>'}${clean(o.energy) ? `<p class="cs-small">Montant estimé des dépenses annuelles d'énergie pour un usage standard : ${esc(o.energy)}</p>` : ''}` : ''}
        ${clean(o.legal) ? `<h2>${ctx.isImmo ? 'Informations légales' : 'Bon à savoir'}</h2><p class="cs-small">${esc(o.legal)}</p>` : ''}
      </div>
      <aside class="cs-side">
        <div class="cs-px">${esc(price || 'Prix sur demande')}</div>
        ${clean(o.ref) ? `<div class="cs-ref">Réf. ${esc(o.ref)}</div>` : ''}
        <form id="csfiche-form" class="cs-form">
          <label for="csf-i">${ctx.isImmo ? 'Bien concerné' : 'Véhicule concerné'}</label><input id="csf-i" readonly value="${esc(clean(o.t) + (o.ref ? ' (réf. ' + o.ref + ')' : '') + (price ? ' · ' + price : ''))}">
          <label for="csf-m">Votre message (facultatif)</label><textarea id="csf-m" rows="3" placeholder="${ctx.isImmo ? 'Ex. : je souhaite visiter ce bien.' : 'Ex. : je souhaite l\'essayer, reprise de mon véhicule possible ?'}"></textarea>
          <button class="btn" type="submit">${ctx.isImmo ? 'Demander une visite' : 'Je suis intéressé'}</button>
        </form>
        ${ctx.phone ? `<a class="btn ghost" href="tel:${esc(clean(ctx.phone).replace(/[^\d+]/g, ''))}">Appeler ${esc(clean(ctx.phone))}</a>` : ''}
        <p class="cs-small">${esc(ctx.name)}${ctx.A.street ? '<br>' + esc(ctx.A.street) : ''}${ctx.A.city ? '<br>' + esc((ctx.A.cp ? ctx.A.cp + ' ' : '') + ctx.A.city) : ''}</p>
      </aside>
    </div>
    <p><a class="btn ghost" href="/#${ctx.isImmo ? 'biens' : 'vehicules'}">‹ ${back}</a></p>
  </div>`;
  const header = q('header.top'); if (header) header.after(main); else doc.body.prepend(main);
  const st = doc.createElement('style');
  st.textContent = `.cs-page{padding:28px 0 56px}.cs-bc{font-size:.85rem;color:var(--muted);margin-bottom:14px}.cs-bc a{color:inherit}.cs-grid{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:32px;align-items:start}.cs-page h1{font-family:var(--display);font-size:clamp(1.6rem,3.6vw,2.4rem);margin:0 0 10px;line-height:1.15}.cs-page h2{font-family:var(--display);font-size:1.25rem;margin:28px 0 12px}.cs-meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px;padding:0}.cs-meta span{background:var(--soft);border-radius:999px;padding:5px 11px;font-size:.88rem}.cs-gal{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.cs-gal img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:var(--r,10px);display:block}.cs-gal img:first-child{grid-column:1/-1}.cs-specs{display:grid;grid-template-columns:auto 1fr;border:1px solid var(--line);border-radius:10px;overflow:hidden;margin:0}.cs-specs dt,.cs-specs dd{margin:0;padding:9px 13px;border-top:1px solid var(--line)}.cs-specs dt{color:var(--muted)}.cs-specs dd{font-weight:600}.cs-specs dt:first-of-type,.cs-specs dd:first-of-type{border-top:0}.cs-feats{columns:2;padding-left:18px}.cs-side{position:sticky;top:90px;border:1px solid var(--line);border-radius:14px;padding:18px;display:grid;gap:10px;background:var(--bg)}.cs-px{font-size:1.8rem;font-weight:800;font-family:var(--display)}.cs-ref,.cs-small{color:var(--muted);font-size:.85rem}.cs-form{display:grid;gap:6px}.cs-form input,.cs-form textarea{font:inherit;padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink)}.cs-form label{font-size:.82rem;color:var(--muted)}.cs-en{display:flex;align-items:center;gap:10px;margin:6px 0}.cs-l{display:inline-grid;place-items:center;width:38px;height:30px;border-radius:6px;color:#fff;font-weight:800}.cs-A{background:#009C6D}.cs-B{background:#52B153}.cs-C{background:#A5CC74}.cs-D{background:#F4E70F;color:#222}.cs-E{background:#F2A541}.cs-F{background:#EB6B2C}.cs-G{background:#D7221F}@media (max-width:860px){.cs-grid{grid-template-columns:1fr}.cs-side{position:static}.cs-feats{columns:1}}`;
  doc.head.appendChild(st);
  const live = doc.createElement('script'); live.src = SITE + '/assets/cs-edit.js?v=27'; live.setAttribute('data-site', slug); live.setAttribute('data-page', 'item'); live.defer = true; doc.body.appendChild(live); { const dj = doc.createElement('script'); dj.src = SITE + '/assets/cs-date.js?v=4'; dj.defer = true; doc.body.appendChild(dj); }
  return dom.serialize();
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
