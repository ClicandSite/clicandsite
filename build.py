#!/usr/bin/env python3
"""Générateur du guide Clic&Site (clicandsite.fr) — pages HTML statiques pour GitHub Pages.
Les identifiants d'affiliation se règlent dans AFFILIATION ; vides = liens normaux, sans commission."""
import html, json, os, shutil, datetime
from urllib.parse import quote_plus
import content as _c

def _typo(x):
    if isinstance(x, str):
        return x.replace("'", "\u2019").replace(" :", "\u00a0:").replace(" ;", "\u202f;").replace(" ?", "\u202f?").replace(" !", "\u202f!")
    if isinstance(x, list):
        return [_typo(i) for i in x]
    if isinstance(x, tuple):
        return tuple(_typo(i) for i in x)
    if isinstance(x, dict):
        return {k: (v if k in ("slug", "region", "couleur") else _typo(v)) for k, v in x.items()}
    return x

REGIONS = _typo(_c.REGIONS)
PROCHAINES_REGIONS = _typo(_c.PROCHAINES_REGIONS)
DESTINATIONS = _typo(_c.DESTINATIONS)

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

def page(path, title, desc, body, crumbs=None, jsonld=None, depth=0):
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
    <p><a href="{root}mentions-legales/">Mentions légales</a><span class="foot__sep"></span>Site réalisé par <a href="https://mycreativesite.fr/" rel="noopener">MyCreativeSite</a></p>
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
  <ul class="cards">{''.join(card(d, '') for d in dests)}</ul>
</section>
"""
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Clic&Site", "url": SITE + "/", "inLanguage": "fr-FR"}]
    write("", page("", "Clic&Site : les plus beaux sites de France, guides pratiques", "Que voir, comment y aller, quoi réserver : des guides courts et pratiques pour visiter les plus beaux sites de France, à commencer par la Côte d'Azur.", body, jsonld=ld))

def build_region(r):
    dests = [d for d in DESTINATIONS if d["region"] == r["slug"]]
    intro = "".join(f"<p>{e(p)}</p>" for p in r["intro"])
    body = f"""
<section class="hero wrap">
  <h1 class="hero__title">Visiter la {e(r['nom'])}</h1>
  <p class="hero__lead">{e(r['accroche'])}</p>
</section>
<section class="wrap prose">{intro}</section>
<section class="wrap" aria-labelledby="g-t">
  <h2 id="g-t" class="sec-title">Nos guides</h2>
  <ul class="cards">{''.join(card(d, '../') for d in dests)}</ul>
</section>
"""
    ld = [{"@context": "https://schema.org", "@type": "TouristDestination", "name": r["nom"], "description": r["description"],
           "includesAttraction": [{"@type": "TouristAttraction", "name": d["nom"], "url": f"{SITE}/{r['slug']}/{d['slug']}/"} for d in dests]}]
    write(r["slug"], page(r["slug"] + "/", r["titre_seo"], r["description"], body,
                          crumbs=[("Accueil", ""), (r["nom"], r["slug"] + "/")], jsonld=ld, depth=1))

def build_dest(d):
    r = REGION_BY_SLUG[d["region"]]
    root = "../../"
    intro = "".join(f"<p>{e(p)}</p>" for p in d["intro"])
    voir = "".join(f"<h3>{e(t)}</h3><p>{e(x)}</p>" for t, x in d["a_voir"])
    aller = "".join(f"<h3>{e(t)}</h3><p>{e(x)}</p>" for t, x in d["y_aller"])
    conseils = "".join(f"<li>{e(c)}</li>" for c in d["conseils"])
    fiche = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in d["fiche"])
    acts = "".join(f"""<li class="act">
  <h3 class="act__t">{e(t)}</h3><p>{e(x)}</p>
  <p class="act__btns"><a class="btn" href="{e(gyg(q))}" rel="sponsored nofollow noopener" target="_blank">Voir sur GetYourGuide</a><a class="btn btn--ghost" href="{e(viator(q))}" rel="sponsored nofollow noopener" target="_blank">Voir sur Viator</a></p>
</li>""" for t, x, q in d["activites"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    autres = [x for x in DESTINATIONS if x["region"] == d["region"] and x["slug"] != d["slug"]]
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
    <h1 class="post__title">Visiter {e(d['nom'])}</h1>
    <p class="post__lead">{e(d['accroche'])}</p>
  </div>
</header>
<div class="wrap layout">
  <article class="prose">
    {intro}
    <h2>À voir</h2>{voir}
    <h2>Comment y aller</h2>{aller}
    <h2>Nos conseils</h2><ul>{conseils}</ul>
    <h2>Réserver une activité</h2>
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
         "containedInPlace": {"@type": "Place", "name": r["nom"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
    ]
    del ld[0]["isAccessibleForFree"]
    path = f"{r['slug']}/{d['slug']}/"
    write(path.rstrip("/"), page(path, d["titre_seo"], d["description"], body,
                                 crumbs=[("Accueil", ""), (r["nom"], r["slug"] + "/"), (d["nom"], path)], jsonld=ld, depth=2))

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
    urls = [""] + [r["slug"] + "/" for r in REGIONS] + [f"{d['region']}/{d['slug']}/" for d in DESTINATIONS] + ["mentions-legales/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write("clicandsite.fr\n")
    nf = page("404.html", "Page introuvable | Clic&Site", "Cette page n'existe pas.",
              '<section class="hero wrap"><h1 class="hero__title hero__title--sm">Cette page n’existe pas.</h1><p class="hero__lead"><a href="/">Revenir à l’accueil</a> pour choisir une région.</p></section>')
    nf = nf.replace('href="assets/', 'href="/assets/').replace('href="cote-d-azur/', 'href="/cote-d-azur/').replace('href="mentions-legales/', 'href="/mentions-legales/').replace('href="#regions"', 'href="/#regions"')
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
    build_legal()
    build_misc()
    print("OK", sum(len(f) for _, _, f in os.walk(OUT)), "fichiers")

if __name__ == "__main__":
    main()
