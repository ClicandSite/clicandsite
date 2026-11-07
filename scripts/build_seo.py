#!/usr/bin/env python3
"""MyCreativeSite — pages SEO (métiers + Côte d'Azur), plan du site.
Lancer depuis la racine du dépôt : python3 scripts/build_seo.py
Chaque page a un contenu propre (pas de copie) : titre, textes, fonctionnalités et questions du métier."""
import json, os, html, datetime

SITE = "https://mycreativesite.fr"
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
  dict(slug="site-internet-coiffeur-institut-beaute", k="beaute", style="luxe",
    title="Création de site internet pour coiffeur et institut de beauté",
    meta="Site internet pour salon de coiffure, barbier et institut de beauté : prise de rendez-vous en ligne, carte des tarifs, réalisations, horaires. Dès 29 €/mois, sans commission.",
    h1="Le site internet des coiffeurs, barbiers et instituts de beauté",
    lead="Salon de coiffure, barbier, esthéticienne, onglerie ou prothésiste ongulaire : vos clientes réservent en ligne, voient vos réalisations et vos tarifs, sans commission sur les rendez-vous.",
    feats=[("Prise de rendez-vous","Prestation, coiffeur ou esthéticienne, jour et heure : la demande arrive chez vous, sans commission."),
           ("Vos réalisations","Coupes, couleurs, ongles, cils : vos plus belles photos, filtrables par catégorie."),
           ("Carte des tarifs","Femme, homme, enfant, beauté : vos prix clairs, modifiables à tout moment."),
           ("Horaires et accès","Jours de fermeture, horaires du samedi, plan et parking : tout ce qu'on vous demande au téléphone."),
           ("Avis Google","Vos meilleurs avis mis en avant pour rassurer les nouvelles clientes."),
           ("Instagram","Votre compte mis en avant, pour transformer les abonnés en rendez-vous.")],
    faq=[("Je paie une commission sur les rendez-vous ?","Non. Contrairement aux plateformes de réservation, vous payez un abonnement fixe dès 29 € par mois, sans commission."),
         ("Je peux changer mes tarifs moi-même ?","Oui, depuis votre espace client sur téléphone : prix, prestations, horaires et photos."),
         ("Le site convient-il à une esthéticienne à domicile ?","Oui : la zone d'intervention remplace l'adresse du salon, et la prise de rendez-vous fonctionne pareil.")]),
]
LOCAL = dict(slug="creation-site-internet-cannes", k=None,
    title="Création de site internet à Cannes et sur la Côte d'Azur",
    meta="Création de site internet pour les professionnels à Cannes, Nice, Antibes, Grasse, Mougins et dans le Var. Agence basée à Cannes. En ligne en 48 h, dès 29 €/mois.",
    h1="Création de site internet à Cannes et sur la Côte d'Azur",
    lead="MyCreativeSite est basé à Cannes. Nous créons les sites des commerçants, artisans et indépendants de la Riviera, de Menton à Saint-Tropez, et partout en France à distance.",
    feats=[("Une agence locale","Basée à Cannes : nous connaissons les métiers et la clientèle de la Côte d'Azur, locale comme internationale."),
           ("Référencement local","Votre site est pensé pour ressortir sur « votre métier + votre ville » dans Google."),
           ("Clientèle étrangère","Site en anglais en option, ou inclus en Premium, pour les touristes et la clientèle d'affaires."),
           ("Tout à distance","Pas de rendez-vous nécessaire : vous envoyez vos infos, on vous envoie votre site."),
           ("Vous restez autonome","Prix, horaires et photos modifiables depuis votre espace client."),
           ("Sans engagement","Un abonnement mensuel, résiliable à tout moment, nom de domaine à votre nom.")],
    faq=[("Intervenez-vous en dehors de Cannes ?","Oui : Nice, Antibes, Cagnes-sur-Mer, Grasse, Mougins, Mandelieu, Menton, Saint-Raphaël, Fréjus, Saint-Tropez, et toute la France à distance."),
         ("Faut-il se rencontrer ?","Ce n'est pas nécessaire : tout se fait en ligne. Si vous êtes près de Cannes, on peut aussi en parler de vive voix."),
         ("Quels métiers accompagnez-vous ?","Chauffeurs VTC, restaurants, garages et concessions, agences immobilières, artisans du bâtiment, coiffeurs et instituts de beauté, et d'autres commerces sur demande.")],
    cities=["Cannes","Le Cannet","Mougins","Antibes","Juan-les-Pins","Vallauris","Mandelieu-la-Napoule","Grasse","Nice","Cagnes-sur-Mer","Saint-Laurent-du-Var","Menton","Monaco","Saint-Raphaël","Fréjus","Sainte-Maxime","Saint-Tropez"])

# Pages « intention » : ce que le pro tape dans Google (pas cher, rapide, clé en main, simple à modifier)
INTENT = [
  dict(slug="site-internet-pas-cher", k=None, label="Site pas cher",
    title="Création de site internet pas cher pour les pros",
    meta="Site internet professionnel pas cher : dès 29 €/mois et 190 € de mise en ligne, hébergement et nom de domaine inclus, sans engagement et sans frais cachés.",
    h1="Un site internet professionnel pas cher, sans mauvaise surprise",
    lead="Un vrai site sur mesure pour votre métier, pour le prix d'un abonnement de téléphone. Pas de devis à 3 000 €, pas de contrat de 48 mois, pas de frais cachés.",
    feats=[("Dès 29 € par mois","Hébergement, nom de domaine, version mobile, sécurité et espace client compris dans le prix."),
           ("190 € de mise en ligne, une fois","Personnalisation du modèle, textes rédigés, photos, installation : tout est compris."),
           ("Aucun engagement","Vous arrêtez quand vous voulez, l'abonnement s'arrête à la fin du mois en cours."),
           ("Pas de frais cachés","Le prix affiché est le prix payé (TVA non applicable). Les dépannages sont compris."),
           ("Moins cher qu'une agence","Une agence classique facture souvent de 1 500 à 5 000 € pour un site vitrine, plus la maintenance."),
           ("Moins de temps que le faire soi-même","Pas besoin d'apprendre Wix ou WordPress : on fait le site, vous le modifiez simplement.")],
    faq=[("Pourquoi c'est moins cher qu'une agence ?","Nos modèles sont déjà conçus pour votre métier : on les personnalise au lieu de tout recréer. Vous payez le résultat, pas des semaines de développement."),
         ("Qu'est-ce qui est inclus dans les 29 € ?","L'hébergement, le nom de domaine, la version mobile, le certificat de sécurité, le formulaire de contact, l'espace client et la maintenance."),
         ("Y a-t-il un engagement de durée ?","Non. Vous résiliez par simple e-mail, et votre nom de domaine reste à vous.")]),
  dict(slug="site-internet-rapide", k=None, label="Site en 48 h",
    title="Site internet rapide : en ligne en 48 heures",
    meta="Besoin d'un site internet rapidement ? Votre site professionnel en ligne en 48 h, sans rendez-vous, et un site rapide à charger sur mobile. Dès 29 €/mois.",
    h1="Votre site internet en ligne en 48 heures, et rapide à charger",
    lead="Ouverture d'entreprise, nouveau local, saison qui démarre : vous avez besoin d'être sur Google maintenant, pas dans deux mois.",
    feats=[("En ligne en 48 h","Après réception de vos infos et photos, votre site est en ligne en général sous 48 heures ouvrées."),
           ("Sans rendez-vous","Pas de réunion ni de visio : un formulaire simple depuis votre téléphone, c'est tout."),
           ("Modèles déjà prêts","Votre métier a déjà son modèle : on l'adapte à votre entreprise au lieu de partir de zéro."),
           ("Rapide à charger","Pages légères et optimisées : vos clients n'attendent pas, même en 4G."),
           ("Pensé pour le mobile","La majorité de vos clients vous cherchent depuis leur téléphone : le site est conçu pour eux d'abord."),
           ("Modifications instantanées","Un prix ou un horaire change ? Vous le modifiez et c'est en ligne aussitôt.")],
    faq=[("Comment pouvez-vous aller si vite ?","Chaque métier a un modèle déjà conçu et testé. Il reste à y mettre vos textes, vos photos et vos coordonnées."),
         ("Que dois-je fournir ?","Le nom de votre entreprise, vos services et prix, vos horaires, vos coordonnées et quelques photos. On rédige le reste avec vous."),
         ("Un site rapide, ça compte pour Google ?","Oui : la vitesse sur mobile fait partie des critères de Google. Un site lent fait partir les visiteurs et recule dans les résultats.")]),
  dict(slug="site-internet-cle-en-main", k=None, label="Site clé en main",
    title="Site internet clé en main pour artisans et commerçants",
    meta="Site internet clé en main : on s'occupe de tout, du nom de domaine à la mise en ligne. Hébergement, maintenance et espace client inclus. Dès 29 €/mois, sans engagement.",
    h1="Un site internet clé en main : on s'occupe de tout",
    lead="Vous gérez votre entreprise, on gère votre site. Nom de domaine, hébergement, textes, photos, sécurité et mises à jour : vous n'avez rien de technique à faire.",
    feats=[("Nom de domaine réservé","votre-entreprise.fr réservé à votre nom, et branché pour vous."),
           ("Textes rédigés","On écrit vos textes à partir de vos informations, pensés pour Google."),
           ("Hébergement et sécurité","Site sécurisé (https), sauvegardé et surveillé, sans rien à installer."),
           ("Mentions légales prêtes","Les pages obligatoires sont rédigées et mises en place."),
           ("Maintenance incluse","Mises à jour et dépannages compris dans l'abonnement."),
           ("Simple à faire évoluer","Un espace client facile pour changer prix, horaires et photos depuis votre téléphone.")],
    faq=[("Je ne suis pas à l'aise avec l'informatique, c'est un problème ?","Non, c'est justement fait pour ça : vous remplissez un formulaire, on fait le reste."),
         ("J'ai déjà un nom de domaine, je le garde ?","Oui, on le branche sur votre nouveau site."),
         ("Qui est propriétaire du site ?","Votre nom de domaine, vos textes et vos photos sont à vous. Si vous partez, vous les gardez.")]),
  dict(slug="site-internet-facile-a-modifier", k=None, label="Site facile à modifier",
    title="Site internet pratique et facile à modifier soi-même",
    meta="Un site internet pratique que vous modifiez vous-même depuis votre téléphone : prix, horaires, photos, carte. Aperçu en direct, sans compétence technique. Dès 29 €/mois.",
    h1="Un site pratique que vous modifiez vous-même, depuis votre téléphone",
    lead="Plus besoin d'attendre votre prestataire pour changer un prix ou un horaire. Votre espace client vous montre le résultat en direct avant d'enregistrer.",
    feats=[("Aperçu en direct","Vous voyez votre site changer pendant que vous tapez, sur ordinateur comme sur téléphone."),
           ("Prix et carte","Ajoutez, supprimez ou modifiez une ligne de tarif en quelques secondes."),
           ("Horaires","Fermeture exceptionnelle, horaires d'été : mis à jour en un instant."),
           ("Photos","Changez une photo depuis votre téléphone, elle est redimensionnée automatiquement."),
           ("Style du site","Changez les couleurs et la mise en page sans perdre vos textes."),
           ("Retour en arrière","Une erreur ? Annulez la dernière modification en un clic.")],
    faq=[("Faut-il des connaissances techniques ?","Non : ce sont des cases à remplir, comme un formulaire. Essayez la démo, sans inscription."),
         ("Et si je préfère que vous le fassiez ?","En formules Pro et Premium, vous nous envoyez vos changements par message et on s'en occupe."),
         ("Puis-je casser mon site ?","Non : la mise en page est protégée, et vous pouvez toujours annuler votre dernière modification.")]),
]

CSS = """.logo-mark{width:34px;height:34px;flex:none;display:block}
.logo .and,.logo i,.grad-t{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
:root{--grad:linear-gradient(90deg,#FF2D8E 0%,#8B3DFF 52%,#12A8FF 100%)}

:root{--bg:#FFFFFF;--paper:#FAF8FF;--ink:#12162B;--muted:#5C627A;--line:#E1E4EE;--brand:#7C3AED;--brand-ink:#FFFFFF;--soft:#E8EBFF}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0D1020;--paper:#151A30;--ink:#EEF0F8;--muted:#9AA1BC;--line:#262C47;--brand:#A98BFF;--brand-ink:#0D1020;--soft:#1E2550;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0D1020;--paper:#151A30;--ink:#EEF0F8;--muted:#9AA1BC;--line:#262C47;--brand:#A98BFF;--brand-ink:#0D1020;--soft:#1E2550;color-scheme:dark}
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
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:12px;padding:13px 20px;font-weight:700;text-decoration:none;background:var(--grad);color:#fff;border:0}
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
LOGO = '<img class="logo-mark" src="/img/logo-m.png" width="34" height="34" alt="">'
NAMES = {"vtc":"Chauffeur VTC","restaurant":"Restaurant","garage":"Garage et concession","immobilier":"Agence immobilière","batiment":"Artisan du bâtiment","beaute":"Coiffeur et institut de beauté"}
e = html.escape

def trade_links(cur):
    out = [f'<a href="/{p["slug"]}/">{NAMES[p["k"]]}</a>' for p in PAGES if p["slug"] != cur]
    if cur != LOCAL["slug"]: out.append(f'<a href="/{LOCAL["slug"]}/">Cannes et Côte d\'Azur</a>')
    out += [f'<a href="/{p["slug"]}/">{p["label"]}</a>' for p in INTENT if p["slug"] != cur]
    return "".join(out)

def page(p):
    url = f'{SITE}/{p["slug"]}/'
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    svc_ld = {"@context":"https://schema.org","@type":"Service","name":p["title"],"serviceType":"Création de site internet","url":url,
      "provider":{"@type":"ProfessionalService","name":"MyCreativeSite","url":SITE+"/","email":"contact@mycreativesite.fr",
                  "address":{"@type":"PostalAddress","streetAddress":"34 rue Borniol","postalCode":"06400","addressLocality":"Cannes","addressCountry":"FR"}},
      "areaServed":"FR",
      "offers":[{"@type":"Offer","name":n,"price":m,"priceCurrency":"EUR","description":f"{m} € par mois + {s} € de mise en ligne"} for n,m,s in PRICES]}
    crumbs_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":p["title"],"item":url}]}
    k = p["k"]
    if k:
        visual = f'<div class="shot"><img src="/img/modele-{k}-d.jpg" width="960" height="600" alt="Exemple de site internet {NAMES[k].lower()} réalisé avec MyCreativeSite" fetchpriority="high"></div>'
        demo = f'<a class="btn ghost" href="/modeles/{k}.html#{p["style"]}">Voir le modèle en vrai</a><a class="btn ghost" href="/espace/?demo={k}&amp;style={p["style"]}">Essayer l\'espace client</a>'
    else:
        visual = '<div class="shot"><img src="/img/og.jpg" width="1200" height="630" alt="Exemples de sites internet réalisés par MyCreativeSite à Cannes" fetchpriority="high"></div>'
        demo = '<a class="btn ghost" href="/espace/?demo=restaurant">Essayer l\'espace client</a>' if p["slug"] == "site-internet-facile-a-modifier" else '<a class="btn ghost" href="/#modeles">Voir les modèles</a>'
    feats = "".join(f'<div class="feat"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t,d in p["feats"])
    prices = "".join(f'<div class="pc"><span>{n}</span><b>{m} €</b><span>par mois · + {s} € de mise en ligne</span></div>' for n,m,s in PRICES)
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in p["faq"])
    cities = f'<p class="cities">Villes : {", ".join(p["cities"])}.</p>' if p.get("cities") else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])} · MyCreativeSite</title>
<meta name="description" content="{e(p["meta"])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p["title"])} · MyCreativeSite">
<meta property="og:description" content="{e(p["meta"])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/img/favicon-64.png"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
<script type="application/ld+json">{json.dumps(svc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs_ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}<span>My<i>creativesite</i></span></a><a class="btn sm" href="/#commande">Je veux mon site</a></div></header>
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
  <h2>À découvrir aussi</h2>
  <div class="links">{trade_links(p["slug"])}</div>
  {cities}
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="cta"><div><h2>Votre site en ligne en 48 heures</h2><p>Rien n'est facturé avant que vous ayez validé votre site.</p></div><a class="btn" href="/#commande">Je veux mon site</a></div>
</div></section>
</main>
<footer><div class="wrap"><span>© 2026 MyCreativeSite</span><nav><a href="/">Accueil</a><a href="/conseils/">Conseils</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV</a><span style="user-select:all">contact@mycreativesite.fr</span></nav></div></footer>
</body>
</html>
'''

CTA_LINK = {"Voir le modèle restaurant": "/site-internet-restaurant/", "Découvrir les modèles par métier": "/#modeles", "Lancer mon site": "/#commande", "Un site pensé pour Google, en ligne en 48 h": "/site-internet-rapide/"}
ARTICLE_CSS = """
.art{max-width:740px;padding-block:10px 40px}
.art h1{margin:6px 0 14px}
.art .date{color:var(--muted);font-size:.9rem}
.art p{margin:14px 0;font-size:1.05rem}
.art h2{margin:34px 0 6px;font-size:1.45rem}
.art ul{margin:12px 0;padding-left:22px;font-size:1.03rem}
.art li{margin:8px 0}
.art .box{margin:34px 0 8px;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px}
.list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:24px}
.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px;text-decoration:none;display:grid;gap:8px}
.card p{color:var(--muted);font-size:.95rem}
@media (max-width:760px){.list{grid-template-columns:1fr}}
"""

def shell(title, desc, url, ld, body, og_type="website"):
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)} · MyCreativeSite</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/img/favicon-64.png"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
{lds}
<style>{CSS}{ARTICLE_CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}<span>My<i>creativesite</i></span></a><a class="btn sm" href="/#commande">Je veux mon site</a></div></header>
<main>{body}</main>
<footer><div class="wrap"><span>© 2026 MyCreativeSite</span><nav><a href="/">Accueil</a><a href="/conseils/">Conseils</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV</a><span style="user-select:all">contact@mycreativesite.fr</span></nav></div></footer>
</body>
</html>
'''

def render_block(b):
    t, v = b
    if t == "p": return f"<p>{v}</p>"
    if t == "h2": return f"<h2>{e(v)}</h2>"
    if t == "ul": return "<ul>" + "".join(f"<li>{x}</li>" for x in v) + "</ul>"
    if t == "cta": return f'<div class="box"><b>{e(v)}</b><a class="btn" href="{CTA_LINK.get(v, "/#tarifs")}">Voir</a></div>'
    return ""

def build_blog():
    from articles import ARTICLES
    os.makedirs("conseils", exist_ok=True)
    for a in ARTICLES:
        url = f"{SITE}/conseils/{a['slug']}/"
        others = "".join(f'<a href="/conseils/{o["slug"]}/">{e(o["title"])}</a>' for o in ARTICLES if o is not a)
        body = f'''<div class="wrap crumbs"><a href="/">Accueil</a> › <a href="/conseils/">Conseils</a></div>
<article class="wrap art"><h1>{e(a["title"])}</h1><p class="date">Publié le {datetime.date.fromisoformat(a["date"]).strftime("%d/%m/%Y")} · MyCreativeSite</p>
{"".join(render_block(b) for b in a["body"])}
<h2>À lire aussi</h2><div class="links">{others}</div></article>'''
        ld = [{"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["desc"],"datePublished":a["date"],"dateModified":a["date"],
               "inLanguage":"fr-FR","mainEntityOfPage":url,"image":SITE+"/img/og.jpg",
               "author":{"@type":"Organization","name":"MyCreativeSite","url":SITE+"/"},"publisher":{"@type":"Organization","name":"MyCreativeSite","url":SITE+"/"}},
              {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
               {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Conseils","item":SITE+"/conseils/"},
               {"@type":"ListItem","position":3,"name":a["title"],"item":url}]}]
        os.makedirs(f"conseils/{a['slug']}", exist_ok=True)
        open(f"conseils/{a['slug']}/index.html","w").write(shell(a["title"], a["desc"], url, ld, body, "article"))
    cards = "".join(f'<a class="card" href="/conseils/{a["slug"]}/"><h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p></a>' for a in ARTICLES)
    body = f'<div class="wrap crumbs"><a href="/">Accueil</a> › Conseils</div><div class="wrap" style="padding-block:10px 50px"><h1>Conseils pour le site internet de votre entreprise</h1><p class="lead" style="color:var(--muted);margin-top:12px;max-width:60ch">Prix, visibilité sur Google, obligations légales, nom de domaine : des réponses claires pour les artisans, commerçants et indépendants.</p><div class="list">{cards}</div></div>'
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Conseils MyCreativeSite","url":SITE+"/conseils/","inLanguage":"fr-FR"}]
    open("conseils/index.html","w").write(shell("Conseils pour le site internet de votre entreprise","Guides pratiques pour les professionnels : prix d'un site internet, visibilité sur Google, mentions légales, nom de domaine.",SITE+"/conseils/",ld,body))
    return ["conseils/"] + [f"conseils/{a['slug']}/" for a in ARTICLES]

def main():
    for p in PAGES + [LOCAL] + INTENT:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w").write(page(p))
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    blog = build_blog()
    urls = [("", "1.0")] + [(p["slug"] + "/", "0.8") for p in PAGES + [LOCAL] + INTENT] + [(u, "0.6") for u in blog] + [("cgv.html", "0.3")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>' for u, pr in urls]
    sm.append("</urlset>")
    open("sitemap.xml", "w").write("\n".join(sm) + "\n")
    print("pages :", len(PAGES) + 1 + len(INTENT), "· sitemap :", len(urls), "adresses")

if __name__ == "__main__":
    main()
