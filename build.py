#!/usr/bin/env python3
"""Générateur du guide Clic&Site — pages HTML statiques pour GitHub Pages, en deux langues.
  python3 build.py        -> site/     (français, clicandsite.fr)
  python3 build.py en     -> site_en/  (anglais, clicandsite.com)
Les identifiants d'affiliation se règlent dans AFFILIATION ; vides = liens normaux, sans commission."""
import html, json, os, shutil, datetime, sys, re
import hashlib as _hl
from urllib.parse import quote_plus
import content as _c
import content_more as _m
import content_en as _en
import seo as _seo
import photos as _ph
import og as _og
import content_paris_fr as _pf
import content_paris_en as _pe

LANG = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CS_LANG", "fr")).lower()
assert LANG in ("fr", "en")
HERE = os.path.dirname(os.path.abspath(__file__))

for _d in _c.DESTINATIONS:
    _d["groupe"] = _m.GROUPES_INITIAUX[_d["slug"]]

KEEP = ("slug", "region", "couleur", "groupe", "variante_liens", "path")

def _typo(x, lang=None):
    lang = lang or LANG
    if isinstance(x, str):
        x = x.replace("'", "’")
        if lang == "fr":
            x = x.replace(" :", " :").replace(" ;", " ;").replace(" ?", " ?").replace(" !", " !")
        return x
    if isinstance(x, list):
        return [_typo(i, lang) for i in x]
    if isinstance(x, tuple):
        return tuple(_typo(i, lang) for i in x)
    if isinstance(x, dict):
        return {k: (v if k in KEEP else _typo(v, lang)) for k, v in x.items()}
    return x

# ---------- Adresses des pages dans les deux langues (pour hreflang et le sélecteur de langue) ----------
SITES = {"fr": "https://clicandsite.fr", "en": "https://clicandsite.com"}
FR_DEST = _c.DESTINATIONS + _m.PLUS + _pf.DESTINATIONS
EN_DEST = _en.DESTINATIONS + _pe.DESTINATIONS
REGION_PATH = {"fr": {r["slug"]: r["slug"] for r in _c.REGIONS + [_pf.REGION]}, "en": {r["slug"]: r["path"] for r in _en.REGIONS + [_pe.REGION]}}
DEST_PATH = {"fr": {d["slug"]: d["slug"] for d in FR_DEST}, "en": {d["slug"]: d["path"] for d in EN_DEST}}
ITI_PATH = {"fr": {"cote-d-azur": _m.ITINERAIRE["slug"], "paris": _pf.ITINERAIRE["slug"]}, "en": {"cote-d-azur": _en.ITINERAIRE["slug"], "paris": _pe.ITINERAIRE["slug"]}}
STATIC = {"about": {"fr": "a-propos/", "en": "about/"}, "legal": {"fr": "mentions-legales/", "en": "legal-notice/"}}

def url_of(key, lang):
    kind, _, ident = key.partition(":")
    if kind == "home":
        return ""
    if kind == "region":
        return REGION_PATH[lang][ident] + "/"
    if kind == "dest":
        reg = next(d["region"] for d in FR_DEST if d["slug"] == ident)
        return f"{REGION_PATH[lang][reg]}/{DEST_PATH[lang][ident]}/"
    if kind == "iti":
        return f"{REGION_PATH[lang][ident]}/{ITI_PATH[lang][ident]}/"
    return STATIC[kind][lang]

# ---------- Contenu de la langue construite ----------
RIVIERA_EXTRA = {
    "fr": {"timbre": "Riviera", "photo": _ph.REGION_PHOTO, "photo_alt": "Le Cap-Ferrat et la côte vus du ciel", "h1": "Visiter la Côte d'Azur", "de": "de la Côte d'Azur", "autres": "Autres sites de la Côte d'Azur", "couleur": "azur"},
    "en": {"timbre": "Riviera", "photo": _ph.REGION_PHOTO, "photo_alt": "Aerial view of Cap Ferrat and the coast", "h1": "Visiting the French Riviera", "de": "French Riviera", "autres": "More places on the French Riviera", "couleur": "azur"},
}
PARIS_EXTRA = {
    "fr": {"h1": "Visiter Paris", "de": "de Paris", "autres": "Autres sites à Paris", "couleur": "encre"},
    "en": {"h1": "Visiting Paris", "de": "Paris", "autres": "More places in Paris", "couleur": "encre"},
}
if LANG == "fr":
    REGIONS = _typo([dict(_c.REGIONS[0], **RIVIERA_EXTRA["fr"]), dict(_pf.REGION, **PARIS_EXTRA["fr"])])
    PROCHAINES_REGIONS = _typo([x for x in _c.PROCHAINES_REGIONS if x != "Paris"])
    DESTINATIONS = _typo(_c.DESTINATIONS + _m.PLUS + _pf.DESTINATIONS)
    GROUPES = {"cote-d-azur": _typo(_m.GROUPES), "paris": _typo(_pf.GROUPES)}
    ITIS = {"cote-d-azur": _typo(dict(_m.ITINERAIRE, conseils=["Logez à Nice : la gare dessert Villefranche, Monaco, Antibes et Cannes en TER.", "Évitez la voiture en juillet-août, le train est plus rapide sur la côte.", "Gardez une tenue correcte pour la cathédrale de Monaco et le casino."])),
            "paris": _typo(_pf.ITINERAIRE)}
    SEO_T = _typo(dict(_seo.TITRES, **_pf.TITRES))
    TITRE_REGION = _typo({"cote-d-azur": _seo.TITRE_REGION, "paris": _pf.TITRE_REGION})
    TITRE_ITI = _typo({"cote-d-azur": _seo.TITRE_ITI, "paris": _pf.TITRE_ITI})
    A_PROPOS = _typo(_seo.A_PROPOS[:-1] + ["Nous avons commencé par la Côte d'Azur, que nous connaissons le mieux, puis Paris, qui se visite toute l'année. Les autres régions arriveront une par une."])
    ALIAS_SRC = dict(_seo.ALIAS, **_pf.ALIAS)
    VEDETTES = {"cote-d-azur": ["nice", "monaco", "eze", "cannes", "iles-de-lerins", "saint-tropez"], "paris": _pf.VEDETTES}
else:
    REGIONS = _typo([dict(_en.REGIONS[0], **RIVIERA_EXTRA["en"]), dict(_pe.REGION, **PARIS_EXTRA["en"])])
    PROCHAINES_REGIONS = _typo([x for x in _en.PROCHAINES_REGIONS if x != "Paris"])
    DESTINATIONS = _typo(_en.DESTINATIONS + _pe.DESTINATIONS)
    GROUPES = {"cote-d-azur": _typo(_en.GROUPES), "paris": _typo(_pe.GROUPES)}
    ITIS = {"cote-d-azur": _typo(dict(_en.ITINERAIRE, conseils=["Stay in Nice: the station has direct regional trains to Villefranche, Monaco, Antibes and Cannes.", "Avoid driving in July and August; the coastal train is faster.", "Dress modestly for Monaco Cathedral and the casino."])),
            "paris": _typo(_pe.ITINERAIRE)}
    SEO_T = _typo(dict(_en.TITRES, **_pe.TITRES))
    TITRE_REGION = _typo({"cote-d-azur": _en.TITRE_REGION, "paris": _pe.TITRE_REGION})
    TITRE_ITI = _typo({"cote-d-azur": _en.TITRE_ITI, "paris": _pe.TITRE_ITI})
    A_PROPOS = _typo(_en.ABOUT[:-1] + ["We started with the French Riviera, which we know best, then Paris, which is worth visiting all year round. Other regions will follow one by one."])
    ALIAS_SRC = dict(_en.ALIAS, **_pe.ALIAS)
    VEDETTES = {"cote-d-azur": ["nice", "monaco", "eze", "cannes", "iles-de-lerins", "saint-tropez"], "paris": _pe.VEDETTES}
for _d in DESTINATIONS:
    _d.setdefault("path", _d["slug"])
for _r in REGIONS:
    _r.setdefault("path", _r["slug"])
LIEU_VOIR = _typo(dict(_seo.LIEU_VOIR, **_pf.LIEU_VOIR))
LIEU_ALLER = _typo(dict(_seo.LIEU_ALLER, **_pf.LIEU_ALLER))
GEO = dict(_seo.GEO, **_pf.GEO)
HOME_ORDER = ["paris", "cote-d-azur"]
BRAND = " | Clic&Site"

SITE = SITES[LANG]
OTHER = "en" if LANG == "fr" else "fr"
OUT = os.path.join(HERE, "site" if LANG == "fr" else "site_en")
TODAY = datetime.date.today().isoformat()
CSS_V = _hl.md5(open(os.path.join(HERE, "assets", "style.css"), "rb").read()).hexdigest()[:8]

AFFILIATION = {
    "getyourguide_partner_id": "XMYSXGR",   # à renseigner après acceptation (partner.getyourguide.com)
    "viator_pid": "",                # à renseigner après acceptation (partnerresources.viator.com)
    "viator_mcid": "42383",
}
EPS_URL = "https://elite-prestige-services.fr/"
CONTACT = "contact@clicandsite.fr"

T = {
 "fr": dict(html_lang="fr", locale="fr_FR", skip="Aller au contenu", nav="Régions", all_regions="Toutes les régions",
            crumbs="Fil d’Ariane", home="Accueil", switch="English", switch_lang="en",
            tagline="Des guides clairs pour visiter les plus beaux sites de France.",
            aff_foot="Certains liens de ce site sont affiliés : si vous réservez une activité après avoir cliqué, Clic&amp;Site perçoit une commission, sans aucun surcoût pour vous.",
            about="À propos", legal="Mentions légales", made_by="Site réalisé par", photo="Photo : ",
            home_title="Où aller, comment y aller, quoi réserver.",
            home_lead="Des guides courts et pratiques pour visiter les plus beaux sites de France sans perdre de temps. On commence par Paris et la Côte d’Azur.",
            home_alt="Le pont Alexandre III à la tombée de la nuit, à Paris", regions="Les régions", guides="guides", soon="Bientôt : ",
            must_see="Les incontournables {de}", see_all="Voir les {n} guides {de}",
            home_seo="Clic&Site : les plus beaux sites de France, guides pratiques",
            home_desc="Que voir, comment y aller, quoi réserver : des guides courts et pratiques pour visiter les plus beaux sites de France, à commencer par Paris et la Côte d'Azur.",
            og_home=("Les plus beaux sites de France", "Où aller, comment y aller, quoi réserver"),
            region_h1="Visiter la {nom}", region_alt="Le Cap-Ferrat et la côte vus du ciel", iti_d="Un itinéraire complet, faisable sans voiture.",
            og_region="{n} guides pratiques", visit="Visiter ", view_of="Vue de ",
            see_h2="Que voir {lv}", go_h2="Comment aller {la}", tips_h2="Nos conseils pour {pour}", acts_h2="Activités à réserver {lv}",
            btn_gyg="Voir sur GetYourGuide", btn_viator="Voir sur Viator",
            aff_note="Liens affiliés : si vous réservez, Clic&amp;Site touche une commission, sans surcoût pour vous. Les prix et disponibilités sont ceux de la plateforme.",
            faq="Questions fréquentes", brief="En bref", others="Autres sites de la {nom}",
            ride_t="Y aller avec un chauffeur privé",
            ride_p="Pour un aéroport, une famille avec bagages ou plusieurs sites dans la même journée, un chauffeur vous évite parkings et correspondances. Notre partenaire Elite Prestige Services, basé à Cannes, assure les transferts sur toute la Côte d’Azur.",
            ride_btn="Réserver un transfert", og_dest="Guide pratique {de}",
            iti_variant="Variante en voiture", iti_more="Pour aller plus loin", iti_guides="Les guides : ", iti_tips="Conseils pour ces trois jours",
            iti_tips_list=["Logez à Nice : la gare dessert Villefranche, Monaco, Antibes et Cannes en TER.",
                           "Évitez la voiture en juillet-août, le train est plus rapide sur la côte.",
                           "Gardez une tenue correcte pour la cathédrale de Monaco et le casino."],
            day_t="Un chauffeur pour la journée",
            day_p="Pour enchaîner Èze, Monaco et les villages perchés sans correspondances, Elite Prestige Services propose des mises à disposition avec chauffeur sur toute la Côte d’Azur.",
            day_btn="Réserver un chauffeur", og_iti=("Itinéraire sans voiture", "3 j"),
            about_h1="À propos de Clic&amp;Site", about_mail="Une remarque, une erreur à signaler ? Écrivez-nous : ",
            about_seo="À propos", about_desc="Qui écrit Clic&Site, comment le guide est financé et pourquoi il ne donne ni prix ni horaires.",
            nf_title="Page introuvable", nf_h1="Cette page n’existe pas.", nf_p='<a href="/">Revenir à l’accueil</a> pour choisir une région.',
            accueil_credit="Pont Alexandre III, Paris (accueil)"),
 "en": dict(html_lang="en", locale="en_GB", skip="Skip to content", nav="Regions", all_regions="All regions",
            crumbs="Breadcrumb", home="Home", switch="Français", switch_lang="fr",
            tagline="Clear, practical guides to the most beautiful places in France.",
            aff_foot="Some links on this site are affiliate links: if you book an activity after clicking, Clic&amp;Site earns a commission at no extra cost to you.",
            about="About", legal="Legal notice", made_by="Website by", photo="Photo: ",
            home_title="Where to go, how to get there, what to book.",
            home_lead="Short, practical guides to the most beautiful places in France, so you spend your time there rather than planning. We start with Paris and the French Riviera.",
            home_alt="The Pont Alexandre III at dusk, Paris", regions="Regions", guides="guides", soon="Coming soon: ",
            must_see="{de} highlights", see_all="See all {n} {de} guides",
            home_seo="Clic&Site: practical guides to the best places in France",
            home_desc="What to see, how to get there and what to book: short, practical guides to the most beautiful places in France, starting with Paris and the French Riviera.",
            og_home=("The most beautiful places in France", "Where to go, how to get there, what to book"),
            region_h1="Visiting the {nom}", region_alt="Aerial view of Cap Ferrat and the coast", iti_d="A complete itinerary you can do without a car.",
            og_region="{n} practical guides", visit="Visit ", view_of="View of ",
            see_h2="Things to do {lv}", go_h2="How to get {la}", tips_h2="Tips for {pour}", acts_h2="Tours and activities {lv}",
            btn_gyg="See on GetYourGuide", btn_viator="See on Viator",
            aff_note="Affiliate links: if you book, Clic&amp;Site earns a commission at no extra cost to you. Prices and availability are set by the booking platform.",
            faq="Frequently asked questions", brief="At a glance", others="More places on the {nom}",
            ride_t="Go there with a private driver",
            ride_p="For an airport transfer, a family with luggage or several places in one day, a driver saves you parking and connections. Our partner Elite Prestige Services, based in Cannes, covers the whole French Riviera.",
            ride_btn="Book a transfer", og_dest="{nom} travel guide",
            iti_variant="With a car", iti_more="Going further", iti_guides="Guides: ", iti_tips="Tips for these three days",
            iti_tips_list=["Stay in Nice: the station has direct regional trains to Villefranche, Monaco, Antibes and Cannes.",
                           "Avoid driving in July and August; the coastal train is faster.",
                           "Dress modestly for Monaco Cathedral and the casino."],
            day_t="A driver for the day",
            day_p="To link Èze, Monaco and the hilltop villages without waiting for connections, Elite Prestige Services offers chauffeur hire by the hour across the French Riviera.",
            day_btn="Book a driver", og_iti=("Itinerary without a car", "3 d"),
            about_h1="About Clic&amp;Site", about_mail="Spotted a mistake or have a suggestion? Email us: ",
            about_seo="About", about_desc="Who writes Clic&Site, how the guide is funded and why it gives no prices or timetables.",
            nf_title="Page not found", nf_h1="This page does not exist.", nf_p='<a href="/">Go back to the home page</a> to choose a region.',
            accueil_credit="Pont Alexandre III, Paris (home page)"),
}[LANG]

e = lambda s: html.escape(str(s), quote=True)

def photo(slug, root):
    v = _ph.PHOTOS[slug]
    if v[0] == "unsplash":
        base = f"{root}assets/photos/{slug}"
        big, mid, small = base + ".jpg", base + "-960.jpg", base + "-640.jpg"
        absolute = f"{SITE}/assets/photos/{slug}.jpg"
        credit = f'{T["photo"]}<a href="{v[3]}" rel="noopener" target="_blank">{e(v[2])}</a> / Unsplash'
    else:
        path = v[1]; fname = path.split("/")[-1]
        th = lambda w: f"https://upload.wikimedia.org/wikipedia/commons/thumb/{path}/{w}px-{fname}"
        big, mid, small = th(1920), th(960), th(960)
        absolute = big
        lic = v[4]
        credit = f'{T["photo"]}<a href="{v[3]}" rel="noopener" target="_blank">{e(v[2])}</a>, <a href="{_ph.LICENCES[lic]}" rel="noopener license" target="_blank">{lic}</a>, Wikimedia Commons'
    return {"big": big, "mid": mid, "small": small, "abs": absolute, "credit": credit}

def hero_img(slug, root, alt):
    ph = photo(slug, root)
    return (f'<img class="post__img" src="{ph["big"]}" srcset="{ph["mid"]} 960w, {ph["big"]} 1920w" sizes="100vw" alt="{e(alt)}" fetchpriority="high">'
            f'<div class="post__shade" aria-hidden="true"></div>'), ph

def gyg(q):
    u = ("https://www.getyourguide.fr/s/?q=" if LANG == "fr" else "https://www.getyourguide.com/s/?q=") + quote_plus(q)
    if AFFILIATION["getyourguide_partner_id"]:
        u += "&partner_id=" + AFFILIATION["getyourguide_partner_id"] + "&cmp=clicandsite-" + LANG + "&utm_medium=online_publisher"
    return u

def viator(q):
    u = ("https://www.viator.com/fr-FR/searchResults/all?text=" if LANG == "fr" else "https://www.viator.com/searchResults/all?text=") + quote_plus(q)
    if AFFILIATION["viator_pid"]:
        u += f"&pid={AFFILIATION['viator_pid']}&mcid={AFFILIATION['viator_mcid']}&medium=link"
    return u

REGION_BY_SLUG = {r["slug"]: r for r in REGIONS}
RPATH = {r["slug"]: r["path"] for r in REGIONS}

def durl(d):
    return f"{RPATH[d['region']]}/{d['path']}/"

def stamp(dept, cachet, small=False):
    return (f'<div class="stamp{" stamp--sm" if small else ""}" aria-hidden="true">'
            f'<span class="stamp__num">{e(dept)}</span></div>'
            f'<div class="postmark{" postmark--sm" if small else ""}" aria-hidden="true"><span>{e(cachet)}</span></div>')

def page(key, title, desc, body, crumbs=None, jsonld=None, depth=0, og_image="assets/og/accueil.jpg"):
    path = url_of(key, LANG) if key != "404" else "404.html"
    root = "../" * depth
    canonical = SITE + "/" + path
    alt_links = ""
    switch = ""
    if key != "404":
        here, there = SITES[LANG] + "/" + url_of(key, LANG), SITES[OTHER] + "/" + url_of(key, OTHER)
        alt_links = (f'<link rel="alternate" hreflang="{LANG}" href="{e(here)}">\n'
                     f'<link rel="alternate" hreflang="{OTHER}" href="{e(there)}">\n'
                     f'<link rel="alternate" hreflang="x-default" href="{e(SITES["en"] + "/" + url_of(key, "en"))}">\n')
        switch = f'<a class="lang" href="{e(there)}" hreflang="{OTHER}" lang="{OTHER}">{T["switch"]}</a>'
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
        crumb_html = f'<nav class="crumbs wrap" aria-label="{T["crumbs"]}"><ol>{"".join(items)}</ol></nav>'
    hero = 'class="post' in body
    if hero and crumb_html:
        body = body.replace("</header>", "</header>\n" + crumb_html, 1); crumb_html = ""
    logo = "logo-clair.svg" if hero else "logo-fonce.svg"
    regions_nav = "".join(f'<a href="{root}{r["path"]}/">{e(r["nom"])}</a>' for r in REGIONS)
    return f"""<!doctype html>
<html lang="{T['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(canonical)}">
{alt_links}<meta property="og:type" content="website">
<meta property="og:site_name" content="Clic&amp;Site">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:locale" content="{T['locale']}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13324b">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/young-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/style.css?v={CSS_V}">
{ld}</head>
<body class="{"hero-page" if hero else "plain-page"}">
<a class="skip" href="#contenu">{T['skip']}</a>
<header class="top">
  <div class="wrap top__in">
    <a class="brand" href="{root}"><img class="brand__logo" src="{root}assets/{logo}" width="167" height="40" alt="Clic&amp;Site"></a>
    <nav class="top__nav" aria-label="{T['nav']}">{regions_nav}<a href="{root}#regions">{T['all_regions']}</a>{switch}</nav>
  </div>
</header>
{crumb_html}
<main id="contenu">
{body}
</main>
<footer class="foot">
  <div class="wrap foot__in">
    <p class="foot__brand">Clic<span class="brand__amp">&amp;</span>Site</p>
    <p>{T['tagline']}</p>
    <p class="foot__aff">{T['aff_foot']}</p>
    <p><a href="{root}{STATIC['about'][LANG]}">{T['about']}</a><span class="foot__sep"></span><a href="{root}{STATIC['legal'][LANG]}">{T['legal']}</a><span class="foot__sep"></span>{T['made_by']} <a class="mcs" href="https://mycreativesite.fr/" rel="noopener"><img src="{root}assets/mycreativesite-m.png" width="22" height="22" alt="">MyCreativeSite</a></p>
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
    ph = photo(d["slug"], root)
    return f"""<li class="card card--{d['couleur']}">
  <a href="{root}{durl(d)}">
    <div class="card__face"><img class="card__img" src="{ph['small']}" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div>{stamp(d['dept'], d['cachet'], small=True)}<span class="card__name">{e(d['nom'])}</span></div>
    <p class="card__txt">{e(d['accroche'])}</p>
  </a>
</li>"""

def region_card(r, root):
    n = len([d for d in DESTINATIONS if d["region"] == r["slug"]])
    return f"""<a class="region-card" href="{root}{r['path']}/">
    <div class="region-card__face">
      <img class="card__img" src="{photo(r['photo'], root)['mid']}" alt="" loading="lazy" decoding="async"><div class="card__shade" aria-hidden="true"></div>
      {stamp(' '.join(r['departements']), r['timbre'])}
      <span class="region-card__name">{e(r['nom'])}</span>
      <span class="region-card__count">{n} {T['guides']}</span>
    </div>
    <p class="region-card__txt">{e(r['accroche'])}</p>
  </a>"""

def build_home():
    order = [REGION_BY_SLUG[s] for s in HOME_ORDER]
    by = {d["slug"]: d for d in DESTINATIONS}
    musts = ""
    for r in order:
        n = len([d for d in DESTINATIONS if d["region"] == r["slug"]])
        it = ITIS[r["slug"]]
        musts += f"""<section class="wrap" aria-labelledby="inc-{r['slug']}">
  <h2 id="inc-{r['slug']}" class="sec-title">{e(T['must_see'].format(de=r['de']))}</h2>
  <ul class="cards">{''.join(card(by[x], '') for x in VEDETTES[r['slug']])}</ul>
  <p class="more"><a href="{r['path']}/">{e(T['see_all'].format(n=n, de=r['de']))}</a><span class="foot__sep foot__sep--dark"></span><a href="{r['path']}/{it['slug']}/">{e(it['titre'])}</a></p>
</section>
"""
    body = f"""
<header class="post post--home">
  {hero_img("accueil", "", T['home_alt'])[0]}
  <div class="wrap post__in">
    <h1 class="post__title post__title--home">{T['home_title']}</h1>
    <p class="post__lead">{T['home_lead']}</p>
  </div>
  <p class="credit">{photo("accueil", "")["credit"]}</p>
</header>
<section class="wrap" id="regions" aria-labelledby="regions-t">
  <h2 id="regions-t" class="sec-title">{T['regions']}</h2>
  <div class="regions">{''.join(region_card(r, '') for r in order)}</div>
  <p class="next">{T['soon']}{e(', '.join(PROCHAINES_REGIONS))}.</p>
</section>
{musts}"""
    _og.make(os.path.join(OUT, "assets", "og", "accueil.jpg"), T["og_home"][0], T["og_home"][1], "FR", "encre")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Clic&Site", "url": SITE + "/", "inLanguage": "fr-FR" if LANG == "fr" else "en"},
          {"@context": "https://schema.org", "@type": "Organization", "name": "Clic&Site", "url": SITE + "/", "logo": SITE + "/assets/logo.png",
           "parentOrganization": {"@type": "Organization", "name": "iDream Lab"}}]
    write("", page("home", T["home_seo"], T["home_desc"], body, jsonld=ld))

def build_region(r):
    dests = [d for d in DESTINATIONS if d["region"] == r["slug"]]
    intro = "".join(f"<p>{e(p)}</p>" for p in r["intro"])
    groups = ""
    ITI = ITIS[r["slug"]]
    for gk, gn in GROUPES[r["slug"]]:
        gd = [d for d in dests if d["groupe"] == gk]
        if gd:
            groups += f'<section class="wrap" aria-labelledby="g-{gk}"><h2 id="g-{gk}" class="sec-title">{e(gn)}</h2><ul class="cards">{"".join(card(d, "../") for d in gd)}</ul></section>'
    body = f"""
<header class="post">
  {hero_img(r['photo'], "../", r['photo_alt'])[0]}
  <div class="wrap post__in">
    <h1 class="post__title">{e(r['h1'])}</h1>
    <p class="post__lead">{e(r['accroche'])}</p>
  </div>
  <p class="credit">{photo(r['photo'], "../")["credit"]}</p>
</header>
<section class="wrap prose">{intro}</section>
<section class="wrap">
  <a class="iti-link" href="{ITI['slug']}/"><span class="iti-link__t">{e(ITI['titre'])}</span><span class="iti-link__d">{T['iti_d']}</span></a>
</section>
{groups}
"""
    ld = [{"@context": "https://schema.org", "@type": "TouristDestination", "name": r["nom"], "description": r["description"],
           "includesAttraction": [{"@type": "TouristAttraction", "name": d["nom"], "url": f"{SITE}/{durl(d)}"} for d in dests]}]
    _og.make(os.path.join(OUT, "assets", "og", r["path"] + ".jpg"), r["h1"], T["og_region"].format(n=len(dests)), " ".join(r["departements"]), r["couleur"])
    write(r["path"], page("region:" + r["slug"], TITRE_REGION[r["slug"]] + BRAND, r["description"], body,
                          crumbs=[(T["home"], ""), (r["nom"], r["path"] + "/")], jsonld=ld, depth=1, og_image=f"assets/og/{r['path']}.jpg"))

ALIAS = []
for _slug, _names in ALIAS_SRC.items():
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
        store.append(f'<a href="{root}{durl(d)}">{m.group(0)}</a>')
        text_html = text_html[:m.start()] + f"\x00{len(store)-1}\x00" + text_html[m.end():]
        used.add(slug)
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text_html)

def build_dest(d):
    r = REGION_BY_SLUG[d["region"]]
    root = "../../"
    by = {x["slug"]: x for x in DESTINATIONS}
    used = {x["slug"] for x in DESTINATIONS if x["region"] != d["region"]}
    L = lambda t: autolink(e(t), d["slug"], used, root, by)
    intro = "".join(f"<p>{L(p)}</p>" for p in d["intro"])
    voir = "".join(f"<h3>{e(t)}</h3><p>{L(x)}</p>" for t, x in d["a_voir"])
    aller = "".join(f"<h3>{e(t)}</h3><p>{L(x)}</p>" for t, x in d["y_aller"])
    conseils = "".join(f"<li>{L(c)}</li>" for c in d["conseils"])
    if LANG == "fr":
        lv = LIEU_VOIR.get(d["slug"], "à " + d["nom"])
        la = LIEU_ALLER.get(d["slug"], "à " + d["nom"])
        h1 = d.get("h1") or T["visit"] + d["nom"]
        pour = h1[0].lower() + h1[1:]
    else:
        lv = d.get("in", "in " + d["nom"])
        la = d.get("to", "to " + d["nom"])
        h1 = d.get("h1") or T["visit"] + d["nom"]
        pour = d.get("tips_for", "visiting " + d["nom"])
    hero = hero_img(d["slug"], root, T["view_of"] + d["nom"])
    fiche = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in d["fiche"])
    acts = "".join(f"""<li class="act">
  <h3 class="act__t">{e(t)}</h3><p>{e(x)}</p>
  <p class="act__btns"><a class="btn" href="{e(gyg(q))}" rel="sponsored nofollow noopener" target="_blank">{T['btn_gyg']}</a><a class="btn btn--ghost" href="{e(viator(q))}" rel="sponsored nofollow noopener" target="_blank">{T['btn_viator']}</a></p>
</li>""" for t, x, q in d["activites"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    pool = [x for x in DESTINATIONS if x["region"] == d["region"] and x["slug"] != d["slug"]]
    autres = ([x for x in pool if x["groupe"] == d["groupe"]] + [x for x in pool if x["groupe"] != d["groupe"]])[:4]
    transfert = ""
    if d["region"] == "cote-d-azur":
        transfert = f"""<aside class="ride">
  <h2 class="ride__t">{T['ride_t']}</h2>
  <p>{T['ride_p']}</p>
  <p><a class="btn btn--light" href="{EPS_URL}" rel="noopener" target="_blank">{T['ride_btn']}</a></p>
</aside>"""
    body = f"""
<header class="post post--{d['couleur']}">
  {hero[0]}
  <div class="wrap post__in">
    {stamp(d['dept'], d['cachet'])}
    <h1 class="post__title">{e(h1)}</h1>
    <p class="post__lead">{e(d['accroche'])}</p>
  </div>
  <p class="credit">{hero[1]["credit"]}</p>
</header>
<div class="wrap layout">
  <article class="prose">
    {intro}
    <h2>{e(T['see_h2'].format(lv=lv))}</h2>{voir}
    <h2>{e(T['go_h2'].format(la=la))}</h2>{aller}
    <h2>{e(T['tips_h2'].format(pour=pour))}</h2><ul>{conseils}</ul>
    <h2>{e(T['acts_h2'].format(lv=lv))}</h2>
    <ul class="acts">{acts}</ul>
    <p class="aff-note">{T['aff_note']}</p>
    <h2>{T['faq']}</h2>
    <div class="faq">{faq}</div>
  </article>
  <aside class="fiche" aria-labelledby="fiche-t">
    <h2 id="fiche-t" class="fiche__t">{T['brief']}</h2>
    <dl>{fiche}</dl>
  </aside>
</div>
<div class="wrap">{transfert}</div>
<section class="wrap" aria-labelledby="autres-t">
  <h2 id="autres-t" class="sec-title">{e(r['autres'])}</h2>
  <ul class="cards">{''.join(card(x, root) for x in autres)}</ul>
</section>
"""
    ld = [
        {"@context": "https://schema.org", "@type": "TouristAttraction", "name": d["nom"], "description": d["description"],
         "url": f"{SITE}/{durl(d)}",
         "image": [photo(d["slug"], "")["abs"], f"{SITE}/assets/og/{d['path']}.jpg"],
         "geo": {"@type": "GeoCoordinates", "latitude": GEO[d["slug"]][0], "longitude": GEO[d["slug"]][1]},
         "address": {"@type": "PostalAddress", "addressLocality": ("Paris" if d["region"] == "paris" and d["slug"] != "versailles" else d["nom"]), "addressRegion": ("Île-de-France" if d["region"] == "paris" else r["nom"]), "addressCountry": _seo.PAYS.get(d["slug"], "FR")},
         "containedInPlace": {"@type": "Place", "name": r["nom"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
    ]
    path = durl(d)
    _og.make(os.path.join(OUT, "assets", "og", d["path"] + ".jpg"), h1, T["og_dest"].format(nom=r["nom"], de=r["de"]), d["dept"], d["couleur"])
    write(path.rstrip("/"), page("dest:" + d["slug"], SEO_T[d["slug"]] + BRAND, d["description"], body,
                                 crumbs=[(T["home"], ""), (r["nom"], r["path"] + "/"), (d["nom"], path)], jsonld=ld, depth=2,
                                 og_image=f"assets/og/{d['path']}.jpg"))

def build_iti(r):
    ITI = ITIS[r["slug"]]
    by = {d["slug"]: d for d in DESTINATIONS}
    root = "../../"
    jours = ""
    for titre, etapes in ITI["jours"]:
        items = "".join(f'<li><a href="{root}{durl(by[sl])}">{e(by[sl]["nom"])}</a>: {e(txt[0].lower() + txt[1:])}</li>'.replace("</a>: ", "</a> : " if LANG == "fr" else "</a>: ") for sl, txt in etapes)
        jours += f'<li class="day"><h2>{e(titre)}</h2><ul>{items}</ul></li>'
    var_links = ", ".join(f'<a href="{root}{durl(by[sl])}">{e(by[sl]["nom"])}</a>' for sl in ITI["variante_liens"])
    tips = "".join(f"<li>{e(t)}</li>" for t in ITI["conseils"])
    ride = f"""<div class="wrap"><aside class="ride">
  <h2 class="ride__t">{T['day_t']}</h2>
  <p>{T['day_p']}</p>
  <p><a class="btn btn--light" href="{EPS_URL}" rel="noopener" target="_blank">{T['day_btn']}</a></p>
</aside></div>""" if r["slug"] == "cote-d-azur" else ""
    body = f"""
<section class="hero wrap">
  <h1 class="hero__title">{e(ITI['titre'])}</h1>
  <p class="hero__lead">{e(ITI['accroche'])}</p>
</section>
<div class="wrap prose">
  <ol class="days">{jours}</ol>
  <h2>{T['iti_variant'] if r['slug'] == 'cote-d-azur' else T['iti_more']}</h2>
  <p>{e(ITI['variante'])}</p>
  <p>{e(_typo(T['iti_guides']))}{var_links}.</p>
  <h2>{T['iti_tips']}</h2>
  <ul>
    {tips}
  </ul>
</div>
{ride}
"""
    path = f"{r['path']}/{ITI['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": ITI["titre"], "description": ITI["description"], "inLanguage": "fr-FR" if LANG == "fr" else "en",
           "author": {"@type": "Organization", "name": "Clic&Site"}, "dateModified": TODAY}]
    ogf = f"{r['path']}-{ITI['slug']}.jpg"
    og_sub = T["og_iti"][0] if r["slug"] == "cote-d-azur" else ITI["accroche"].split(".")[0]
    _og.make(os.path.join(OUT, "assets", "og", ogf), ITI["titre"], og_sub, T["og_iti"][1], "encre")
    write(path.rstrip("/"), page("iti:" + r["slug"], TITRE_ITI[r["slug"]] + BRAND, ITI["description"], body,
                                 crumbs=[(T["home"], ""), (r["nom"], r["path"] + "/"), (ITI["titre"], path)], jsonld=ld, depth=2, og_image=f"assets/og/{ogf}"))

def build_about():
    paras = "".join(f"<p>{e(p)}</p>" for p in A_PROPOS)
    path = STATIC["about"][LANG]
    body = f"""
<section class="hero wrap"><h1 class="hero__title hero__title--sm">{T['about_h1']}</h1></section>
<section class="wrap prose">{paras}<p>{e(_typo(T['about_mail']))}<a href="mailto:{CONTACT}">{CONTACT}</a>.</p></section>
"""
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "name": html.unescape(T["about_h1"]), "url": SITE + "/" + path}]
    write(path.rstrip("/"), page("about", T["about_seo"] + BRAND, T["about_desc"], body,
                                 crumbs=[(T["home"], ""), (T["about"], path)], jsonld=ld, depth=1))

def build_legal():
    by = {d["slug"]: d["nom"] for d in DESTINATIONS}
    by["accueil"] = T["accueil_credit"]
    sep = " : " if LANG == "fr" else ": "
    credits = "".join(f'<li>{e(by.get(k, k))}{sep}{photo(k, "../")["credit"].replace(T["photo"], "")}</li>' for k in _ph.PHOTOS)
    path = STATIC["legal"][LANG]
    if LANG == "fr":
        body = f"""
<section class="hero wrap"><h1 class="hero__title hero__title--sm">Mentions légales</h1></section>
<section class="wrap prose">
<h2>Éditeur</h2>
<p>Clic&amp;Site (clicandsite.fr et clicandsite.com) est édité par iDream Lab, société par actions simplifiée à associé unique (SASU) au capital de 50 euros, immatriculée sous le numéro 130 813 744 RCS Cannes, dont le siège social est situé au 34 rue Borniol, 06400 Cannes, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p>Directeur de la publication : Anthony Doche, président d’iDream Lab.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, États-Unis.</p>
<h2>Liens affiliés</h2>
<p>Clic&amp;Site est un guide éditorial. Certains liens vers des plateformes de réservation (GetYourGuide, Viator et d’autres) sont des liens affiliés : lorsqu’un visiteur réserve après avoir cliqué, la plateforme verse une commission à Clic&amp;Site. Le prix payé par le visiteur est le même. Clic&amp;Site ne vend aucune prestation touristique : les réservations, paiements et annulations relèvent exclusivement de la plateforme choisie et du prestataire.</p>
<p>Elite Prestige Services, présenté comme partenaire pour les transferts avec chauffeur sur la Côte d’Azur, est une entreprise liée à l’éditeur.</p>
<h2>Crédits photos</h2>
<p>Photos issues d’Unsplash (licence Unsplash) et de Wikimedia Commons (licences Creative Commons indiquées). Merci à leurs auteurs.</p>
<ul>{credits}</ul>
<h2>Données personnelles et cookies</h2>
<p>Ce site ne dépose aucun cookie de mesure d’audience ni de publicité, et ne collecte aucune donnée personnelle. Les plateformes de réservation vers lesquelles pointent les liens appliquent leur propre politique de confidentialité.</p>
<h2>Exactitude des informations</h2>
<p>Les informations pratiques (accès, saisons, conseils) sont données à titre indicatif et peuvent évoluer. Vérifiez horaires et conditions auprès des sites et des transporteurs avant votre visite.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes et l’identité visuelle de Clic&amp;Site sont protégés. Toute reproduction sans autorisation est interdite.</p>
</section>
"""
        title, desc = "Mentions légales | Clic&Site", "Mentions légales du guide Clic&Site, édité par iDream Lab."
    else:
        body = f"""
<section class="hero wrap"><h1 class="hero__title hero__title--sm">Legal notice</h1></section>
<section class="wrap prose">
<h2>Publisher</h2>
<p>Clic&amp;Site (clicandsite.com and clicandsite.fr) is published by iDream Lab, a French simplified joint-stock company (SASU) with a share capital of 50 euros, registered under number 130 813 744 RCS Cannes, whose registered office is at 34 rue Borniol, 06400 Cannes, France. Contact: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p>Publication director: Anthony Doche, president of iDream Lab.</p>
<h2>Hosting</h2>
<p>The site is hosted by GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, United States.</p>
<h2>Affiliate links</h2>
<p>Clic&amp;Site is an editorial guide. Some links to booking platforms (GetYourGuide, Viator and others) are affiliate links: when a visitor books after clicking, the platform pays Clic&amp;Site a commission. The price you pay is the same. Clic&amp;Site does not sell any travel services: bookings, payments and cancellations are handled solely by the chosen platform and the provider.</p>
<p>Elite Prestige Services, presented as a partner for chauffeur transfers on the French Riviera, is a company related to the publisher.</p>
<h2>Photo credits</h2>
<p>Photos from Unsplash (Unsplash licence) and Wikimedia Commons (Creative Commons licences as stated). Many thanks to their authors.</p>
<ul>{credits}</ul>
<h2>Personal data and cookies</h2>
<p>This site sets no analytics or advertising cookies and collects no personal data. The booking platforms we link to apply their own privacy policies.</p>
<h2>Accuracy</h2>
<p>Practical information (access, seasons, tips) is given as a guide and may change. Check opening times and conditions with the sites and transport operators before your visit.</p>
<h2>Intellectual property</h2>
<p>The texts and visual identity of Clic&amp;Site are protected. Reproduction without permission is prohibited.</p>
</section>
"""
        title, desc = "Legal notice | Clic&Site", "Legal notice for the Clic&Site travel guide, published by iDream Lab."
    write(path.rstrip("/"), page("legal", title, desc, body, crumbs=[(T["home"], ""), (T["legal"], path)], depth=1))

def build_misc():
    urls = [""] + [r["path"] + "/" for r in REGIONS] + [durl(d) for d in DESTINATIONS] + [f"{r['path']}/{ITIS[r['slug']]['slug']}/" for r in REGIONS] + [STATIC["about"][LANG], STATIC["legal"][LANG]]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write(SITE.split("//")[1] + "\n")
    nf = page("404", T["nf_title"] + BRAND, T["nf_title"] + ".",
              f'<section class="hero wrap"><h1 class="hero__title hero__title--sm">{T["nf_h1"]}</h1><p class="hero__lead">{T["nf_p"]}</p></section>')
    nf = re.sub(r'(href|src)="(?!https?:|/|#|mailto:)', r'\1="/', nf)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(nf)
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"))
    shutil.rmtree(os.path.join(OUT, "assets", "og"), ignore_errors=True)
    build_home()
    for r in REGIONS:
        build_region(r)
    for d in DESTINATIONS:
        build_dest(d)
    for r in REGIONS:
        build_iti(r)
    build_about()
    build_legal()
    build_misc()
    print("OK", LANG, sum(len(f) for _, _, f in os.walk(OUT)), "fichiers")

if __name__ == "__main__":
    main()
