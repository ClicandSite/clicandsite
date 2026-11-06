#!/usr/bin/env python3
"""ClicandSite — pages SEO (métiers + Côte d'Azur), plan du site.
Lancer depuis la racine du dépôt : python3 scripts/build_seo.py
Chaque page a un contenu propre (pas de copie) : titre, textes, fonctionnalités et questions du métier."""
import json, os, html, datetime

SITE = "https://clicandsite.fr"
TODAY = datetime.date.today().isoformat()
PRICES = [("Essentiel", 29, 190), ("Pro", 59, 290), ("Premium", 89, 490)]

PAGES = [
  dict(slug="site-internet-vtc", k="vtc", style="luxe",
    title="Création de site internet pour chauffeur VTC",
    meta="Site internet pour chauffeur VTC et taxi : réservation de course en ligne, tarifs fixes, bouton WhatsApp, version anglaise. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    h1="Le site internet des chauffeurs VTC qui veulent leurs propres clients",
    lead="Arrêtez de dépendre uniquement des plateformes. Avec votre site, vos clients réservent directement chez vous : transferts aéroport, mise à disposition, longues distances.",
    feats=[("Réservation dès l'accueil","Départ, arrivée, date et heure : la demande arrive par mail et vous rappelez le client."),
           ("Bouton WhatsApp et appel","Sur téléphone, un bouton toujours visible pour vous joindre en un geste."),
           ("Vos tarifs fixes","Aéroport → centre-ville, gares, événements : des prix clairs qui rassurent avant de réserver."),
           ("Votre véhicule mis en avant","Photos, nombre de places, bagages, équipements à bord, langues parlées."),
           ("Site en anglais","Indispensable pour la clientèle d'affaires et touristique (inclus en Premium)."),
           ("Acompte en ligne","Le client paie un acompte par carte à la réservation : fini les courses annulées (Premium).")],
    faq=[("Mon site peut-il remplacer les plateformes de VTC ?","Il les complète : vos clients fidèles et les personnes qui vous trouvent sur Google réservent chez vous, sans commission sur la course."),
         ("Puis-je afficher mes tarifs aéroport ?","Oui. Vous modifiez vous-même vos forfaits depuis votre espace client, à tout moment."),
         ("Le site fonctionne-t-il pour une petite société de VTC avec plusieurs chauffeurs ?","Oui : vous présentez vos véhicules et les réservations arrivent sur l'adresse de votre choix.")]),
  dict(slug="site-internet-restaurant", k="restaurant", style="chaleureux",
    title="Création de site internet pour restaurant",
    meta="Site internet pour restaurant : réservation de table, carte et menu du jour modifiables, photos, horaires, plan d'accès. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    h1="Un site de restaurant qui donne faim et remplit vos tables",
    lead="Vos clients regardent votre carte et vos photos avant de venir. Donnez-leur un site à la hauteur de votre cuisine, avec la réservation en un clic.",
    feats=[("Réservation de table","Date, heure, nombre de couverts : la demande arrive directement par mail."),
           ("Carte par catégories","Entrées, plats, desserts, vins : vous changez un plat ou un prix vous-même en 30 secondes."),
           ("Menu du midi","Mettez en avant votre formule du jour, mise à jour depuis votre téléphone."),
           ("Photos qui donnent envie","Une galerie de vos plats et de votre salle, en grand sur ordinateur comme sur mobile."),
           ("Horaires et plan d'accès","Jours de fermeture, service du midi et du soir, adresse et accès clairement affichés."),
           ("Avis Google","Vos meilleurs avis affichés sur le site pour rassurer les nouveaux clients (Pro).")],
    faq=[("Je peux changer ma carte moi-même ?","Oui, depuis votre espace client : ajoutez un plat, changez un prix ou le menu du jour, le site est mis à jour aussitôt."),
         ("Le site remplace-t-il les plateformes de réservation ?","Il vous évite leurs commissions pour les clients qui vous trouvent directement. Vous pouvez aussi garder vos outils actuels."),
         ("Et si mon restaurant a déjà un site ?","On reprend vos textes et photos dans un modèle moderne, et on branche votre nom de domaine actuel.")]),
  dict(slug="site-internet-garage", k="garage", style="audacieux",
    title="Création de site internet pour garage et concession",
    meta="Site internet pour garage automobile et concession : prise de rendez-vous atelier, tarifs, stock de véhicules d'occasion, reprise. En ligne en 48 h, dès 29 €/mois.",
    h1="Le site internet des garages et des concessions indépendantes",
    lead="Rendez-vous atelier, véhicules d'occasion, reprise : un site qui travaille pour vous pendant que vous êtes sous le capot.",
    feats=[("Prise de rendez-vous","Prestation, date souhaitée, immatriculation : la demande arrive par mail."),
           ("Stock de véhicules","Fiches avec photos, kilométrage, énergie et prix, filtrables par marque et budget."),
           ("Estimation de reprise","Le client envoie son immatriculation et son kilométrage pour une estimation."),
           ("Forfaits et tarifs","Vidange, pneus, freins, climatisation : des prix affichés qui donnent confiance."),
           ("Présentation de l'atelier","Équipe, équipements, véhicule de prêt, moyens de paiement."),
           ("Annonces sur Abracadeal","En Premium, vos véhicules sont aussi diffusés sur Abracadeal.")],
    faq=[("Je peux ajouter mes véhicules moi-même ?","Oui : depuis votre espace client, vous ajoutez, modifiez ou retirez un véhicule avec ses photos et son prix."),
         ("Le site convient-il à un garage sans vente de véhicules ?","Oui, la partie stock peut être retirée : le site se concentre alors sur l'atelier et les rendez-vous."),
         ("Combien de temps pour être en ligne ?","En général 48 heures après réception de vos informations et photos.")]),
  dict(slug="site-internet-agence-immobiliere", k="immobilier", style="riviera",
    title="Création de site internet pour agence immobilière",
    meta="Site internet pour agence immobilière indépendante : biens à vendre et à louer filtrables, étiquette DPE, estimation gratuite, présentation de l'agent. Dès 29 €/mois.",
    h1="Un site d'agence immobilière qui génère des mandats",
    lead="Vos biens bien présentés, une estimation en ligne qui capte les vendeurs, et une image d'agence locale de confiance.",
    feats=[("Recherche de biens","Achat ou location, ville, budget, nombre de pièces : filtres en direct."),
           ("Fiches avec DPE","Photos, surface, pièces, prix et étiquette énergie conforme."),
           ("Estimation gratuite","Un formulaire dédié pour recevoir des demandes de vendeurs."),
           ("Présentation de l'agent","Votre parcours, vos langues, votre secteur : la confiance avant le premier appel."),
           ("Mentions obligatoires","Carte professionnelle, garantie financière et honoraires affichés."),
           ("Annonces sur Abracadeal","En Premium, vos biens sont aussi diffusés sur Abracadeal.")],
    faq=[("Je peux ajouter mes biens moi-même ?","Oui, depuis votre espace client, avec photos, prix et caractéristiques."),
         ("Le site est-il adapté à un agent indépendant ou mandataire ?","Oui : il met en avant votre nom, votre secteur et votre accompagnement personnel."),
         ("Puis-je afficher mes honoraires ?","Oui, c'est d'ailleurs obligatoire : une rubrique est prévue pour votre barème.")]),
  dict(slug="site-internet-artisan-batiment", k="batiment", style="moderne",
    title="Création de site internet pour artisan du bâtiment",
    meta="Site internet pour artisan du bâtiment et entreprise de rénovation : demande de devis, réalisations avant/après, tarifs au m², zone d'intervention, décennale. Dès 29 €/mois.",
    h1="Le site internet des artisans du bâtiment et de la rénovation",
    lead="Maçon, électricien, plombier, peintre, carreleur ou entreprise générale : montrez vos chantiers et recevez des demandes de devis qualifiées.",
    feats=[("Demande de devis","Type de travaux, code postal du chantier, date de début : vous recevez des demandes précises."),
           ("Vos réalisations","Photos de chantiers avec surface, durée et budget, filtrables par type de travaux."),
           ("Tarifs indicatifs","Peinture, carrelage, parquet au m² : vos clients savent à quoi s'attendre."),
           ("Zone d'intervention","Les villes où vous intervenez, sans frais de déplacement ou sur devis."),
           ("Garanties mises en avant","Assurance décennale, prix ferme, chantier propre : ce qui rassure avant de signer."),
           ("Présentation de l'artisan","Votre parcours et votre façon de travailler, avec votre photo.")],
    faq=[("Je peux ajouter mes chantiers moi-même ?","Oui : depuis votre téléphone, vous ajoutez les photos d'un chantier terminé et ses informations."),
         ("Le site convient-il à un auto-entrepreneur ?","Oui, la formule Essentiel est faite pour démarrer, avec un site complet dès 29 € par mois."),
         ("Puis-je indiquer mon assurance décennale ?","Oui, et c'est conseillé : elle est mise en avant sur le site et dans les mentions légales.")]),
]
LOCAL = dict(slug="creation-site-internet-cannes", k=None,
    title="Création de site internet à Cannes et sur la Côte d'Azur",
    meta="Création de site internet pour les professionnels à Cannes, Nice, Antibes, Grasse, Mougins et dans le Var. Agence basée à Cannes. En ligne en 48 h, dès 29 €/mois.",
    h1="Création de site internet à Cannes et sur la Côte d'Azur",
    lead="ClicandSite est basé à Cannes. Nous créons les sites des commerçants, artisans et indépendants de la Riviera, de Menton à Saint-Tropez, et partout en France à distance.",
    feats=[("Une agence locale","Basée à Cannes : nous connaissons les métiers et la clientèle de la Côte d'Azur, locale comme internationale."),
           ("Référencement local","Votre site est pensé pour ressortir sur « votre métier + votre ville » dans Google."),
           ("Clientèle étrangère","Site en anglais en option, ou inclus en Premium, pour les touristes et la clientèle d'affaires."),
           ("Tout à distance","Pas de rendez-vous nécessaire : vous envoyez vos infos, on vous envoie votre site."),
           ("Vous restez autonome","Prix, horaires et photos modifiables depuis votre espace client."),
           ("Sans engagement","Un abonnement mensuel, résiliable à tout moment, nom de domaine à votre nom.")],
    faq=[("Intervenez-vous en dehors de Cannes ?","Oui : Nice, Antibes, Cagnes-sur-Mer, Grasse, Mougins, Mandelieu, Menton, Saint-Raphaël, Fréjus, Saint-Tropez, et toute la France à distance."),
         ("Faut-il se rencontrer ?","Ce n'est pas nécessaire : tout se fait en ligne. Si vous êtes près de Cannes, on peut aussi en parler de vive voix."),
         ("Quels métiers accompagnez-vous ?","Chauffeurs VTC, restaurants, garages et concessions, agences immobilières, artisans du bâtiment, et d'autres commerces sur demande.")],
    cities=["Cannes","Le Cannet","Mougins","Antibes","Juan-les-Pins","Vallauris","Mandelieu-la-Napoule","Grasse","Nice","Cagnes-sur-Mer","Saint-Laurent-du-Var","Menton","Monaco","Saint-Raphaël","Fréjus","Sainte-Maxime","Saint-Tropez"])

CSS = """
:root{--bg:#F5F6FA;--paper:#FFFFFF;--ink:#12162B;--muted:#5C627A;--line:#E1E4EE;--brand:#2F45FF;--brand-ink:#FFFFFF;--soft:#E8EBFF}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0D1020;--paper:#151A30;--ink:#EEF0F8;--muted:#9AA1BC;--line:#262C47;--brand:#6A7BFF;--brand-ink:#0D1020;--soft:#1E2550;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0D1020;--paper:#151A30;--ink:#EEF0F8;--muted:#9AA1BC;--line:#262C47;--brand:#6A7BFF;--brand-ink:#0D1020;--soft:#1E2550;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Figtree",system-ui,-apple-system,"Segoe UI",sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1,h2,h3{font-family:"Bricolage Grotesque",system-ui,sans-serif;letter-spacing:-.02em;line-height:1.1;margin:0;text-wrap:balance}
h1{font-size:clamp(2rem,5vw,3.1rem)} h2{font-size:clamp(1.5rem,3vw,2.1rem)} h3{font-size:1.1rem}
p{margin:0} a{color:inherit}
.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-block:12px}
.logo{display:flex;align-items:center;gap:9px;font:800 1.2rem "Bricolage Grotesque",sans-serif;text-decoration:none}
.logo svg{width:26px;height:26px} .logo i{font-style:normal;color:var(--brand)}
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:12px;padding:13px 20px;font-weight:700;text-decoration:none;background:var(--brand);color:var(--brand-ink);border:0}
.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--line)}
.btn.sm{padding:9px 14px;font-size:.92rem}
.crumbs{font-size:.85rem;color:var(--muted);padding-block:18px 0}
.crumbs a{color:var(--muted)}
.hero{display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center;padding-block:28px 56px}
.hero .lead{color:var(--muted);font-size:1.12rem;margin:18px 0 26px;max-width:56ch}
.ctas{display:flex;flex-wrap:wrap;gap:12px}
.shot{border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 60px -30px rgba(18,22,43,.45);background:var(--paper)}
.shot img{display:block;width:100%;height:auto}
section{padding-block:48px}
.feats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:26px}
.feat{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:8px;align-content:start}
.feat p{color:var(--muted);font-size:.95rem}
.prices{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:24px}
.pc{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:4px}
.pc b{font:800 2rem "Bricolage Grotesque",sans-serif}
.pc span{color:var(--muted);font-size:.9rem}
.note{color:var(--muted);font-size:.88rem;margin-top:12px}
.faq{display:grid;gap:10px;margin-top:22px;max-width:780px}
.faq details{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:14px 18px}
.faq summary{cursor:pointer;font-weight:700}
.faq details p{color:var(--muted);margin-top:8px}
.links{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.links a{border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:7px 14px;text-decoration:none;font-size:.92rem}
.cities{color:var(--muted);margin-top:14px;max-width:70ch}
.cta{background:var(--ink);color:var(--bg);border-radius:20px;padding:34px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:18px}
.cta p{opacity:.8;margin-top:6px}
.cta .btn{background:var(--bg);color:var(--ink)}
footer{border-top:1px solid var(--line);padding-block:26px;color:var(--muted);font-size:.9rem}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}
footer nav{display:flex;flex-wrap:wrap;gap:16px}
@media (max-width:860px){.hero{grid-template-columns:1fr}.feats,.prices{grid-template-columns:1fr}}
"""
LOGO = '<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="1" y="1" width="24" height="24" rx="7" fill="var(--brand)"/><path d="M9 7.5l9 5.2-3.9 1 2.3 4.1-1.7 1-2.3-4.1-2.8 2.9z" fill="#fff"/></svg>'
NAMES = {"vtc":"Chauffeur VTC","restaurant":"Restaurant","garage":"Garage et concession","immobilier":"Agence immobilière","batiment":"Artisan du bâtiment"}
e = html.escape

def trade_links(cur):
    out = [f'<a href="/{p["slug"]}/">{NAMES[p["k"]]}</a>' for p in PAGES if p["slug"] != cur]
    if cur != LOCAL["slug"]: out.append(f'<a href="/{LOCAL["slug"]}/">Cannes et Côte d\'Azur</a>')
    return "".join(out)

def page(p):
    url = f'{SITE}/{p["slug"]}/'
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    svc_ld = {"@context":"https://schema.org","@type":"Service","name":p["title"],"serviceType":"Création de site internet","url":url,
      "provider":{"@type":"ProfessionalService","name":"ClicandSite","url":SITE+"/","email":"contact@clicandsite.fr",
                  "address":{"@type":"PostalAddress","streetAddress":"34 rue Borniol","postalCode":"06400","addressLocality":"Cannes","addressCountry":"FR"}},
      "areaServed":"FR",
      "offers":[{"@type":"Offer","name":n,"price":m,"priceCurrency":"EUR","description":f"{m} € par mois + {s} € de mise en ligne"} for n,m,s in PRICES]}
    crumbs_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":p["title"],"item":url}]}
    k = p["k"]
    if k:
        visual = f'<div class="shot"><img src="/img/modele-{k}-d.jpg" width="960" height="600" alt="Exemple de site internet {NAMES[k].lower()} réalisé avec ClicandSite" fetchpriority="high"></div>'
        demo = f'<a class="btn ghost" href="/modeles/{k}.html#{p["style"]}">Voir le modèle en vrai</a><a class="btn ghost" href="/espace/?demo={k}&amp;style={p["style"]}">Essayer l\'espace client</a>'
    else:
        visual = '<div class="shot"><img src="/img/og.jpg" width="1200" height="630" alt="Exemples de sites internet réalisés par ClicandSite à Cannes" fetchpriority="high"></div>'
        demo = '<a class="btn ghost" href="/#modeles">Voir les modèles</a>'
    feats = "".join(f'<div class="feat"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t,d in p["feats"])
    prices = "".join(f'<div class="pc"><span>{n}</span><b>{m} €</b><span>par mois · + {s} € de mise en ligne</span></div>' for n,m,s in PRICES)
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in p["faq"])
    cities = f'<p class="cities">Villes : {", ".join(p["cities"])}.</p>' if p.get("cities") else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])} · ClicandSite</title>
<meta name="description" content="{e(p["meta"])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p["title"])} · ClicandSite">
<meta property="og:description" content="{e(p["meta"])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 26'%3E%3Crect x='1' y='1' width='24' height='24' rx='7' fill='%232F45FF'/%3E%3Cpath d='M9 7.5l9 5.2-3.9 1 2.3 4.1-1.7 1-2.3-4.1-2.8 2.9z' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
<script type="application/ld+json">{json.dumps(svc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs_ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}<span>Clic<i>and</i>Site</span></a><a class="btn sm" href="/#commande">Je veux mon site</a></div></header>
<main>
<div class="wrap crumbs"><a href="/">Accueil</a> › {e(p["title"])}</div>
<div class="wrap hero">
  <div>
    <h1>{e(p["h1"])}</h1>
    <p class="lead">{e(p["lead"])}</p>
    <div class="ctas"><a class="btn" href="/#commande">Je veux mon site</a>{demo}</div>
  </div>
  {visual}
</div>
<section><div class="wrap">
  <h2>Ce que votre site fait pour vous</h2>
  <div class="feats">{feats}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2>Des prix clairs, sans engagement</h2>
  <div class="prices">{prices}</div>
  <p class="note">TVA non applicable, art. 293 B du CGI. Hébergement, nom de domaine, version mobile et espace client inclus. <a href="/#tarifs">Détail des formules</a> · <a href="/cgv.html">Conditions générales</a></p>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2>Questions fréquentes</h2>
  <div class="faq">{faq}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2>Nos autres sites métiers</h2>
  <div class="links">{trade_links(p["slug"])}</div>
  {cities}
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="cta"><div><h2>Votre site en ligne en 48 heures</h2><p>Rien n'est facturé avant que vous ayez validé votre site.</p></div><a class="btn" href="/#commande">Je veux mon site</a></div>
</div></section>
</main>
<footer><div class="wrap"><span>© 2026 ClicandSite · Cannes</span><nav><a href="/">Accueil</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV</a><span style="user-select:all">contact@clicandsite.fr</span></nav></div></footer>
</body>
</html>
'''

def main():
    for p in PAGES + [LOCAL]:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w").write(page(p))
    urls = [("", "1.0")] + [(p["slug"] + "/", "0.8") for p in PAGES + [LOCAL]] + [("cgv.html", "0.3")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>' for u, pr in urls]
    sm.append("</urlset>")
    open("sitemap.xml", "w").write("\n".join(sm) + "\n")
    print("pages :", len(PAGES) + 1, "· sitemap :", len(urls), "adresses")

if __name__ == "__main__":
    main()
