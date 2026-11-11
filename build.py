#!/usr/bin/env python3
"""Générateur du guide Clic&Site (clicandsite.fr) — pages HTML statiques pour GitHub Pages.
Les identifiants d'affiliation se règlent dans AFFILIATION ; vides = liens normaux, sans commission."""
import html, json, os, shutil, datetime
from urllib.parse import quote_plus
import content as _c
import content_more as _m
import seo as _seo
import og as _og
import re
for _d in _c.DESTINATIONS:
    _d["groupe"] = _m.GROUPES_INITIAUX[_d["slug"]]

def _typo(x):
    if isinstance(x, str):
        return x.replace("'", "\u2019").replace(" :", "\u00a0:").replace(" ;", "\u202f;").replace(" ?", "\u202f?").replace(" !", "\u202f!")
    if isinstance(x, list):
        return [_typo(i) for i in x]
    if isinstance(x, tuple):
        return tuple(_typo(i) for i in x)
    if isinstance(x, dict):
        return {k: (v if k in ("slug", "region", "couleur", "groupe", "variante_liens") else _typo(v)) for k, v in x.items()}
    return x

REGIONS = _typo(_c.REGIONS)
PROCHAINES_REGIONS = _typo(_c.PROCHAINES_REGIONS)
DESTINATIONS = _typo(_c.DESTINATIONS + _m.PLUS)
GROUPES = _typo(_m.GROUPES)
ITI = _typo(_m.ITINERAIRE)
SEO_T = _typo(_seo.TITRES)
LIEU_VOIR = _typo(_seo.LIEU_VOIR)
LIEU_ALLER = _typo(_seo.LIEU_ALLER)
A_PROPOS = _typo(_seo.A_PROPOS)
BRAND = " | Clic&Site"
VEDETTES = ["nice", "monaco", "eze", "cannes", "iles-de-lerins", "saint-tropez"]

SITE = "https://clicandsite.fr"
OUT = os.path.join(os.path.dirname(__file__), "site")
TODAY = datetime.date.today().isoformat()

AFFILIATION = {
    "getyourguide_partner_id": "",   # à renseigner après acceptation (partner.getyourguide.com)
    "viator_pid": "",                # à renseigner après acceptation (partnerresources.viator.com)
    "viator_mcid": "42383",
}
EPS_URL = "https://elite-prestige-services.fr/"
CONTACT = "contact@clicandsite.fr"

e = lambda s: html.escape(str(s), quote=True)

def gyg(q):
    u = "https://www.getyourguide.fr/s/?q=" + quote_plus(q)
    if AFFILIATION["getyourguide_partner_id"]:
        u += "&partner_id=" + AFFILIATION["getyourguide_partner_id"] + "&cmp=clicandsite"
    return u

def viator(q):
    u = "https://www.viator.com/fr-FR/searchResults/all?text=" + quote_plus(q)
    if AFFILIATION["viator_pid"]:
        u += f"&pid={AFFILIATION['viator_pid']}&mcid={AFFILIATION['viator_mcid']}&medium=link"
    return u

REGION_BY_SLUG = {r["slug"]: r for r in REGIONS}

def stamp(dept, cachet, small=False):
    return (f'<div class="stamp{" stamp--sm" if small else ""}" aria-hidden="true">'
            f'<span class="stamp__num">{e(dept)}</span></div>'
            f'<div class="postmark{" postmark--sm" if small else ""}" aria-hidden="true"><span>{e(cachet)}</span></div>')

def page(path, title, desc, body, crumbs=None, jsonld=None, depth=0, og_image="assets/og/accueil.jpg"):
    root = "../" * depth
    canonical = SITE + "/" + path
    ld = ""
    blocks = list(jsonld or [])
    if crumbs:
        blocks.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + p} for i, (n, p) in enumerate(crumbs)]})
    for b in blocks:
        ld += '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + "</script>\n"
    crumb_html = ""
    if crumbs and len(crumbs) > 1:
        items = []
        for i, (n, p) in enumerate(crumbs):
            items.append(f'<li><a href="{root}{p}">{e(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{e(n)}</li>')
        crumb_html = f'<nav class="crumbs wrap" aria-label="Fil d’Ariane"><ol>{"".join(items)}</ol></nav>'
    regions_nav = "".join(f'<a href="{root}{r["slug"]}/">{e(r["nom"])}</a>' for r in REGIONS)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(canonical)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Clic&amp;Site">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13324b">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/young-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/style.css">
{ld}</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="wrap top__in">
    <a class="brand" href="{root}">Clic<span class="brand__amp">&amp;</span>Site</a>
    <nav class="top__nav" aria-label="Régions">{regions_nav}<a href="{root}#regions">Toutes les régions</a></nav>
  </div>
</header>
{crumb_html}
<main id="contenu">
{body}
</main>
<footer class="foot">
  <div class="wrap foot__in">
    <p class="foot__brand">Clic<span class="brand__amp">&amp;</span>Site</p>
    <p>Des guides clairs pour visiter les plus beaux sites de France.</p>
    <p class="foot__aff">Certains liens de ce site sont affiliés : si vous réservez une activité après avoir cliqué, Clic&amp;Site perçoit une commission, sans aucun surcoût pour vous.</p>
    <p><a href="{root}a-propos/">À propos</a><span class="foot__sep"></span><a href="{root}mentions-legales/">Mentions légales</a><span class="foot__sep"></span>Site réalisé par <a class="mcs" href="https://mycreativesite.fr/" rel="noopener"><img src="{root}assets/mycreativesite-m.png" width="22" height="22" alt="">MyCreativeSite</a></p>
  </div>
</footer>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(OUT, path, "index.html") if not path.endswith(".xml") and not path.endswith(".txt") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def card(d, root):
    return f"""<li class="card card--{d['couleur']}">
  <a href="{root}{d['region']}/{d['slug']}/">
    <div class="card__face">{stamp(d['dept'], d['cachet'], small=True)}<span class="card__name">{e(d['nom'])}</span></div>
    <p class="card__txt">{e(d['accroche'])}</p>
  </a>
</li>"""

def build_home():
    r = REGIONS[0]
    dests = [d for d in DESTINATIONS if d["region"] == r["slug"]]
    by = {d["slug"]: d for d in dests}
    vedettes = [by[x] for x in VEDETTES]
    body = f"""
<section class="hero wrap">
  <h1 class="hero__title">Où aller, comment y aller, quoi réserver.</h1>
  <p class="hero__lead">Des guides courts et pratiques pour visiter les plus beaux sites de France sans perdre de temps. On commence par la Côte d’Azur.</p>
</section>
<section class="wrap" id="regions" aria-labelledby="regions-t">
  <h2 id="regions-t" class="sec-title">Les régions</h2>
  <a class="region-card" href="{r['slug']}/">
    <div class="region-card__face">
      {stamp(' '.join(r['departements']), 'Riviera')}
      <span class="region-card__name">{e(r['nom'])}</span>
      <span class="region-card__count">{len(dests)} guides</span>
    </div>
    <p class="region-card__txt">{e(r['accroche'])}</p>
  </a>
  <p class="next">Bientôt : {e(', '.join(PROCHAINES_REGIONS))}.</p>
</section>
<section class="wrap" aria-labelledby="inc-t">
  <h2 id="inc-t" class="sec-title">Les incontournables de la Côte d’Azur</h2>
  <ul class="cards">{''.join(card(d, '') for d in vedettes)}</ul>
  <p class="more"><a href="{r['slug']}/">Voir les {len(dests)} guides de la Côte d’Azur</a><span class="foot__sep foot__sep--dark"></span><a href="{r['slug']}/{ITI['slug']}/">{e(ITI['titre'])}</a></p>
</section>
"""
    _og.make(os.path.join(OUT, "assets", "og", "accueil.jpg"), "Les plus beaux sites de France", "Où aller, comment y aller, quoi réserver", "FR", "encre")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Clic&Site", "url": SITE + "/", "inLanguage": "fr-FR"},
          {"@context": "https://schema.org", "@type": "Organization", "name": "Clic&Site", "url": SITE + "/", "logo": SITE + "/assets/logo.png",
           "parentOrganization": {"@type": "Organization", "name": "iDream Lab"}}]
    write("", page("", "Clic&Site : les plus beaux sites de France, guides pratiques", "Que voir, comment y aller, quoi réserver : des guides courts et pratiques pour visiter les plus beaux sites de France, à commencer par la Côte d'Azur.", body, jsonld=ld))

def build_region(r):
    dests = [d for d in DESTINATIONS if d["region"] == r["slug"]]
    intro = "".join(f"<p>{e(p)}</p>" for p in r["intro"])
    groups = ""
    for gk, gn in GROUPES:
        gd = [d for d in dests if d["groupe"] == gk]
        if gd:
            groups += f'<section class="wrap" aria-labelledby="g-{gk}"><h2 id="g-{gk}" class="sec-title">{e(gn)}</h2><ul class="cards">{"".join(card(d, "../") for d in gd)}</ul></section>'
    body = f"""
<section class="hero wrap">
  <h1 class="hero__title">Visiter la {e(r['nom'])}</h1>
  <p class="hero__lead">{e(r['accroche'])}</p>
</section>
<section class="wrap prose">{intro}</section>
<section class="wrap">
  <a class="iti-link" href="{ITI['slug']}/"><span class="iti-link__t">{e(ITI['titre'])}</span><span class="iti-link__d">Un itinéraire complet, faisable sans voiture.</span></a>
</section>
{groups}
"""
    ld = [{"@context": "https://schema.org", "@type": "TouristDestination", "name": r["nom"], "description": r["description"],
           "includesAttraction": [{"@type": "TouristAttraction", "name": d["nom"], "url": f"{SITE}/{r['slug']}/{d['slug']}/"} for d in dests]}]
    _og.make(os.path.join(OUT, "assets", "og", r["slug"] + ".jpg"), "Visiter la " + r["nom"], f"{len(dests)} guides pratiques", " ".join(r["departements"]), "azur")
    write(r["slug"], page(r["slug"] + "/", _typo(_seo.TITRE_REGION) + BRAND, r["description"], body,
                          crumbs=[("Accueil", ""), (r["nom"], r["slug"] + "/")], jsonld=ld, depth=1, og_image=f"assets/og/{r['slug']}.jpg"))

ALIAS = []
for _slug, _names in _seo.ALIAS.items():
    for _n in _names:
        ALIAS.append((_typo(_n), _slug))
ALIAS.sort(key=lambda x: -len(x[0]))

def autolink(text_html, current, used, root, by):
    """Lie la première mention d'un autre guide (une seule fois par page)."""
    store = []
    for name, slug in ALIAS:
        if slug == current or slug in used:
            continue
        pat = re.compile(r"(?<![\w\-’])" + re.escape(e(name)) + r"(?![\w\-])")
        m = pat.search(text_html)
        if not m:
            continue
        d = by[slug]
        store.append(f'<a href="{root}{d["region"]}/{slug}/">{m.group(0)}</a>')
        text_html = text_html[:m.start()] + f"\x00{len(store)-1}\x00" + text_html[m.end():]
        used.add(slug)
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text_html)

def build_dest(d):
    r = REGION_BY_SLUG[d["region"]]
    root = "../../"
    by = {x["slug"]: x for x in DESTINATIONS}
    used = set()
    L = lambda t: autolink(e(t), d["slug"], used, root, by)
    intro = "".join(f"<p>{L(p)}</p>" for p in d["intro"])
    voir = "".join(f"<h3>{e(t)}</h3><p>{L(x)}</p>" for t, x in d["a_voir"])
    aller = "".join(f"<h3>{e(t)}</h3><p>{L(x)}</p>" for t, x in d["y_aller"])
    conseils = "".join(f"<li>{L(c)}</li>" for c in d["conseils"])
    lv = LIEU_VOIR.get(d["slug"], "à " + d["nom"])
    la = LIEU_ALLER.get(d["slug"], "à " + d["nom"])
    h1 = d.get("h1") or "Visiter " + d["nom"]
    pour = h1[0].lower() + h1[1:]
    fiche = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in d["fiche"])
    acts = "".join(f"""<li class="act">
  <h3 class="act__t">{e(t)}</h3><p>{e(x)}</p>
  <p class="act__btns"><a class="btn" href="{e(gyg(q))}" rel="sponsored nofollow noopener" target="_blank">Voir sur GetYourGuide</a><a class="btn btn--ghost" href="{e(viator(q))}" rel="sponsored nofollow noopener" target="_blank">Voir sur Viator</a></p>
</li>""" for t, x, q in d["activites"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    pool = [x for x in DESTINATIONS if x["region"] == d["region"] and x["slug"] != d["slug"]]
    autres = ([x for x in pool if x["groupe"] == d["groupe"]] + [x for x in pool if x["groupe"] != d["groupe"]])[:4]
    transfert = ""
    if d["region"] == "cote-d-azur":
        transfert = f"""<aside class="ride">
  <h2 class="ride__t">Y aller avec un chauffeur privé</h2>
  <p>Pour un aéroport, une famille avec bagages ou plusieurs sites dans la même journée, un chauffeur vous évite parkings et correspondances. Notre partenaire Elite Prestige Services, basé à Cannes, assure les transferts sur toute la Côte d’Azur.</p>
  <p><a class="btn btn--light" href="{EPS_URL}" rel="noopener" target="_blank">Réserver un transfert</a></p>
</aside>"""
    body = f"""
<header class="post post--{d['couleur']}">
  <div class="wrap post__in">
    {stamp(d['dept'], d['cachet'])}
    <h1 class="post__title">{e(h1)}</h1>
    <p class="post__lead">{e(d['accroche'])}</p>
  </div>
</header>
<div class="wrap layout">
  <article class="prose">
    {intro}
    <h2>Que voir {e(lv)}</h2>{voir}
    <h2>Comment aller {e(la)}</h2>{aller}
    <h2>Nos conseils pour {e(pour)}</h2><ul>{conseils}</ul>
    <h2>Activités à réserver {e(lv)}</h2>
    <ul class="acts">{acts}</ul>
    <p class="aff-note">Liens affiliés : si vous réservez, Clic&amp;Site touche une commission, sans surcoût pour vous. Les prix et disponibilités sont ceux de la plateforme.</p>
    <h2>Questions fréquentes</h2>
    <div class="faq">{faq}</div>
  </article>
  <aside class="fiche" aria-labelledby="fiche-t">
    <h2 id="fiche-t" class="fiche__t">En bref</h2>
    <dl>{fiche}</dl>
  </aside>
</div>
<div class="wrap">{transfert}</div>
<section class="wrap" aria-labelledby="autres-t">
  <h2 id="autres-t" class="sec-title">Autres sites de la {e(r['nom'])}</h2>
  <ul class="cards">{''.join(card(x, root) for x in autres)}</ul>
</section>
"""
    ld = [
        {"@context": "https://schema.org", "@type": "TouristAttraction", "name": d["nom"], "description": d["description"],
         "url": f"{SITE}/{r['slug']}/{d['slug']}/", "isAccessibleForFree": False,
         "image": f"{SITE}/assets/og/{d['slug']}.jpg",
         "geo": {"@type": "GeoCoordinates", "latitude": _seo.GEO[d["slug"]][0], "longitude": _seo.GEO[d["slug"]][1]},
         "address": {"@type": "PostalAddress", "addressLocality": d["nom"], "addressRegion": r["nom"], "addressCountry": _seo.PAYS.get(d["slug"], "FR")},
         "containedInPlace": {"@type": "Place", "name": r["nom"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
    ]
    del ld[0]["isAccessibleForFree"]
    path = f"{r['slug']}/{d['slug']}/"
    _og.make(os.path.join(OUT, "assets", "og", d["slug"] + ".jpg"), h1, "Guide pratique de la " + r["nom"], d["dept"], d["couleur"])
    write(path.rstrip("/"), page(path, SEO_T[d["slug"]] + BRAND, d["description"], body,
                                 crumbs=[("Accueil", ""), (r["nom"], r["slug"] + "/"), (d["nom"], path)], jsonld=ld, depth=2,
                                 og_image=f"assets/og/{d['slug']}.jpg"))

def build_iti(r):
    by = {d["slug"]: d for d in DESTINATIONS}
    root = "../../"
    jours = ""
    for titre, etapes in ITI["jours"]:
        items = "".join(f'<li><a href="{root}{r["slug"]}/{sl}/">{e(by[sl]["nom"])}</a> : {e(txt[0].lower() + txt[1:])}</li>' for sl, txt in etapes)
        jours += f'<li class="day"><h2>{e(titre)}</h2><ul>{items}</ul></li>'
    var_links = ", ".join(f'<a href="{root}{r["slug"]}/{sl}/">{e(by[sl]["nom"])}</a>' for sl in ITI["variante_liens"])
    body = f"""
<section class="hero wrap">
  <h1 class="hero__title">{e(ITI['titre'])}</h1>
  <p class="hero__lead">{e(ITI['accroche'])}</p>
</section>
<div class="wrap prose">
  <ol class="days">{jours}</ol>
  <h2>Variante en voiture</h2>
  <p>{e(ITI['variante'])}</p>
  <p>Les guides : {var_links}.</p>
  <h2>Conseils pour ces trois jours</h2>
  <ul>
    <li>Logez à Nice : la gare dessert Villefranche, Monaco, Antibes et Cannes en TER.</li>
    <li>Évitez la voiture en juillet-août, le train est plus rapide sur la côte.</li>
    <li>Gardez une tenue correcte pour la cathédrale de Monaco et le casino.</li>
  </ul>
</div>
<div class="wrap"><aside class="ride">
  <h2 class="ride__t">Un chauffeur pour la journée</h2>
  <p>Pour enchaîner Èze, Monaco et les villages perchés sans correspondances, Elite Prestige Services propose des mises à disposition avec chauffeur sur toute la Côte d’Azur.</p>
  <p><a class="btn btn--light" href="{EPS_URL}" rel="noopener" target="_blank">Réserver un chauffeur</a></p>
</aside></div>
"""
    path = f"{r['slug']}/{ITI['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": ITI["titre"], "description": ITI["description"], "inLanguage": "fr-FR",
           "author": {"@type": "Organization", "name": "Clic&Site"}, "dateModified": TODAY}]
    _og.make(os.path.join(OUT, "assets", "og", "3-jours.jpg"), ITI["titre"], "Itinéraire sans voiture", "3 j", "encre")
    write(path.rstrip("/"), page(path, _typo(_seo.TITRE_ITI) + BRAND, ITI["description"], body,
                                 crumbs=[("Accueil", ""), (r["nom"], r["slug"] + "/"), (ITI["titre"], path)], jsonld=ld, depth=2, og_image="assets/og/3-jours.jpg"))

def build_about():
    paras = "".join(f"<p>{e(p)}</p>" for p in A_PROPOS)
    body = f"""
<section class="hero wrap"><h1 class="hero__title hero__title--sm">À propos de Clic&amp;Site</h1></section>
<section class="wrap prose">{paras}<p>Une remarque, une erreur à signaler ? Écrivez-nous : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p></section>
"""
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "À propos de Clic&Site", "url": SITE + "/a-propos/"}]
    write("a-propos", page("a-propos/", "À propos" + BRAND, "Qui écrit Clic&Site, comment le guide est financé et pourquoi il ne donne ni prix ni horaires.", body,
                           crumbs=[("Accueil", ""), ("À propos", "a-propos/")], jsonld=ld, depth=1))

def build_legal():
    body = f"""
<section class="hero wrap"><h1 class="hero__title hero__title--sm">Mentions légales</h1></section>
<section class="wrap prose">
<h2>Éditeur</h2>
<p>Clic&amp;Site (clicandsite.fr) est édité par iDream Lab, société par actions simplifiée à associé unique (SASU) au capital de 50 euros, immatriculée sous le numéro 130 813 744 RCS Cannes, dont le siège social est situé au 34 rue Borniol, 06400 Cannes, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p>Directeur de la publication : Anthony Doche, président d’iDream Lab.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, États-Unis.</p>
<h2>Liens affiliés</h2>
<p>Clic&amp;Site est un guide éditorial. Certains liens vers des plateformes de réservation (GetYourGuide, Viator et d’autres) sont des liens affiliés : lorsqu’un visiteur réserve après avoir cliqué, la plateforme verse une commission à Clic&amp;Site. Le prix payé par le visiteur est le même. Clic&amp;Site ne vend aucune prestation touristique : les réservations, paiements et annulations relèvent exclusivement de la plateforme choisie et du prestataire.</p>
<p>Elite Prestige Services, présenté comme partenaire pour les transferts avec chauffeur sur la Côte d’Azur, est une entreprise liée à l’éditeur.</p>
<h2>Données personnelles et cookies</h2>
<p>Ce site ne dépose aucun cookie de mesure d’audience ni de publicité, et ne collecte aucune donnée personnelle. Les plateformes de réservation vers lesquelles pointent les liens appliquent leur propre politique de confidentialité.</p>
<h2>Exactitude des informations</h2>
<p>Les informations pratiques (accès, saisons, conseils) sont données à titre indicatif et peuvent évoluer. Vérifiez horaires et conditions auprès des sites et des transporteurs avant votre visite.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes et l’identité visuelle de Clic&amp;Site sont protégés. Toute reproduction sans autorisation est interdite.</p>
</section>
"""
    write("mentions-legales", page("mentions-legales/", "Mentions légales | Clic&Site", "Mentions légales du guide Clic&Site, édité par iDream Lab.", body,
                                   crumbs=[("Accueil", ""), ("Mentions légales", "mentions-legales/")], depth=1))

def build_misc():
    urls = [""] + [r["slug"] + "/" for r in REGIONS] + [f"{d['region']}/{d['slug']}/" for d in DESTINATIONS] + [f"{REGIONS[0]['slug']}/{ITI['slug']}/", "a-propos/", "mentions-legales/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("clicandsite.fr\n")
    nf = page("404.html", "Page introuvable | Clic&Site", "Cette page n'existe pas.",
              '<section class="hero wrap"><h1 class="hero__title hero__title--sm">Cette page n’existe pas.</h1><p class="hero__lead"><a href="/">Revenir à l’accueil</a> pour choisir une région.</p></section>')
    nf = nf.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('href="cote-d-azur/', 'href="/cote-d-azur/').replace('href="mentions-legales/', 'href="/mentions-legales/').replace('href="#regions"', 'href="/#regions"')
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(nf)
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(os.path.dirname(__file__), "assets"), os.path.join(OUT, "assets"))
    build_home()
    for r in REGIONS:
        build_region(r)
    for d in DESTINATIONS:
        build_dest(d)
    build_iti(REGIONS[0])
    build_about()
    build_legal()
    build_misc()
    print("OK", sum(len(f) for _, _, f in os.walk(OUT)), "fichiers")

if __name__ == "__main__":
    main()
