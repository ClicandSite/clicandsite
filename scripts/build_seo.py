#!/usr/bin/env python3
"""MyCreativeSite — pages SEO (métiers + Côte d'Azur), plan du site.
Lancer depuis la racine du dépôt : python3 scripts/build_seo.py
Chaque page a un contenu propre (pas de copie) : titre, textes, fonctionnalités et questions du métier."""
import json, os, html, datetime

SITE = "https://mycreativesite.fr"
TODAY = datetime.date.today().isoformat()
PRICES = [("Essentiel", 29, 190), ("Pro", 49, 290), ("Premium", 79, 490)]

PAGES = [
  dict(slug="site-internet-vtc", k="vtc", style="luxe",
    title="Création de site internet pour chauffeur VTC",
    meta="Site internet pour chauffeur VTC et taxi : réservation de course en ligne, tarifs fixes, bouton WhatsApp, version anglaise. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    h1="Libérez-vous des plateformes et trouvez vos clients pros avec votre site web",
    lead="Hôtels, entreprises, agences d'événements, conciergeries : avec votre propre site, vos clients réservent directement chez vous, sans commission. Transferts aéroport, mise à disposition, longues distances.",
    feats=[("Réservation dès l'accueil","Départ, arrivée, date et heure : la demande arrive par mail et vous rappelez le client."),
           ("Bouton WhatsApp et appel","Sur téléphone, un bouton toujours visible pour vous joindre en un geste."),
           ("Vos tarifs fixes","Aéroport → centre-ville, gares, événements : des prix clairs qui rassurent avant de réserver."),
           ("Votre véhicule mis en avant","Photos, nombre de places, bagages, équipements à bord, langues parlées."),
           ("Site en anglais","Indispensable pour la clientèle d'affaires et touristique (inclus en Premium)."),
           ("Paiement à la réservation","Forfait payé ou acompte par carte, l'argent arrive directement sur votre compte : fini les courses annulées (Pro).")],
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
  dict(slug="site-internet-masseur-osteopathe-bien-etre", k="bienetre", style="chaleureux",
    title="Création de site internet pour masseur, ostéopathe et bien-être",
    meta="Site internet pour masseur, ostéopathe, kiné, prof de yoga ou spa : réservation en ligne, carte des soins, tarifs, cartes cadeaux. Dès 29 €/mois, sans commission.",
    h1="Le site internet des masseurs, ostéopathes et professionnels du bien-être",
    lead="Masseur bien-être, ostéopathe, naturopathe, sophrologue, professeur de yoga ou petit spa : vos clients découvrent vos soins et réservent en ligne, sans commission.",
    feats=[("Réservation en ligne","Soin, praticien, jour et heure : la demande arrive directement chez vous."),
           ("Carte des soins","Massages, séances, cours : vos soins filtrables, avec durée et prix."),
           ("Cartes cadeaux","Un bouton « Offrir » sur chaque soin, idéal pour les fêtes."),
           ("Tarifs et forfaits","Séance, carte de 5 ou 10, abonnement : tout est clair avant de réserver."),
           ("Le lieu","Photos du cabinet ou du studio, ambiance, accès et parking."),
           ("Présentation du praticien","Votre parcours et vos diplômes, pour donner confiance.")],
    faq=[("Je paie une commission sur les réservations ?","Non : un abonnement fixe dès 29 € par mois, quel que soit le nombre de rendez-vous."),
         ("Le site convient-il à un praticien à domicile ?","Oui : la zone de déplacement remplace l'adresse du cabinet."),
         ("Je peux ajouter un nouveau soin moi-même ?","Oui, depuis votre espace client, avec photo, durée et prix.")]),
  dict(slug="site-internet-boulangerie", k="boulangerie", style="chaleureux",
    title="Création de site internet pour boulangerie et pâtisserie",
    meta="Site internet pour boulangerie, pâtisserie et commerce de bouche : commande à retirer, vitrine de la semaine, gâteaux sur commande, horaires. Dès 29 €/mois.",
    h1="Le site internet des boulangeries, pâtisseries et commerces de bouche",
    lead="Boulanger, pâtissier, chocolatier, traiteur, fromager ou épicerie fine : vos clients voient vos produits du moment et commandent à l'avance pour ne plus faire la queue.",
    feats=[("Commande à retirer","Produit, quantité et heure de retrait : vous recevez la commande la veille."),
           ("Vitrine de la semaine","Vos produits du moment, avec photo et prix, mis à jour en une minute."),
           ("Gâteaux sur commande","Anniversaires, mariages, plateaux pour entreprises : un formulaire dédié."),
           ("Horaires et fermetures","Jours fériés, vacances, horaires du dimanche : toujours à jour."),
           ("Avis Google","Votre note et vos meilleurs avis mis en avant (Pro et Premium)."),
           ("Livraison aux pros","Restaurants, hôtels, bureaux : une rubrique pour vos clients professionnels.")],
    faq=[("Je peux changer ma vitrine chaque jour ?","Oui, depuis votre téléphone, en quelques secondes."),
         ("Faut-il gérer un paiement en ligne ?","Non : le client paie au retrait. Le paiement en ligne à la commande est possible dès la formule Pro."),
         ("Le site convient-il à un traiteur ou un fromager ?","Oui, le modèle s'adapte à tous les commerces de bouche.")]),
  dict(slug="site-internet-boutique-en-ligne", k="boutique", style="moderne",
    title="Création de boutique en ligne pour commerçants et créateurs",
    meta="Boutique en ligne clé en main pour commerçants et créateurs : catalogue, panier, paiement par carte, retrait ou livraison. En ligne en 48 h, 99 €/mois, sans engagement.",
    h1="Votre boutique en ligne, avec paiement par carte, sans y passer vos soirées",
    lead="Vendez vos produits sur votre propre site, à votre nom. Vos clients remplissent leur panier, paient par carte, et choisissent le retrait en boutique ou la livraison.",
    feats=[("Paiement par carte","Le client paie en ligne, l'argent arrive directement sur votre compte via votre propre compte Stripe."),
           ("Catalogue facile à tenir","Ajoutez un produit, changez un prix ou une photo depuis votre téléphone, en une minute."),
           ("Retrait ou livraison","Retrait gratuit en boutique, livraison avec vos frais et votre seuil de livraison offerte."),
           ("Filtres par rayon et budget","Vos clients trouvent vite : déco, bougies, cadeaux, petits prix…"),
           ("Commandes rangées","Chaque commande arrive dans votre espace, avec le statut du paiement et l'historique du client."),
           ("Votre boutique, votre nom","Votre nom de domaine, sans commission de place de marché sur vos ventes.")],
    faq=[("Combien coûte la boutique ?","99 € par mois et 490 € de mise en ligne, sans engagement. Les frais bancaires de Stripe s'ajoutent à chaque paiement (environ 1,5 % + 0,25 € par carte européenne)."),
         ("Qui encaisse l'argent ?","Vous. Le paiement passe par votre propre compte Stripe et arrive sur votre compte bancaire. MyCreativeSite ne touche pas à vos ventes."),
         ("Combien de produits puis-je vendre ?","La formule est pensée pour les petites boutiques, jusqu'à 40 produits mis en avant. Pour un très grand catalogue, parlons-en avant."),
         ("Puis-je aussi vendre en boutique physique ?","Oui : le retrait en boutique permet à vos clients de commander en ligne et de passer chercher leur commande.")]),
  dict(slug="site-internet-plombier-electricien", k="depannage", style="audacieux",
    title="Création de site internet pour plombier, électricien et dépannage",
    meta="Site internet pour plombier, électricien, chauffagiste ou serrurier : demande de rappel urgent, interventions récentes, tarifs transparents, zone 7j/7. Dès 29 €/mois.",
    h1="Le site internet des plombiers, électriciens et dépanneurs",
    lead="Plombier, électricien, chauffagiste, serrurier ou vitrier : soyez trouvé au moment de l'urgence, et rassurez avec des prix clairs avant de vous déplacer.",
    feats=[("Demande de rappel urgent","Problème, code postal, délai : vous êtes prévenu immédiatement par SMS."),
           ("Interventions récentes","Le problème, la solution, le temps passé et le prix : la preuve de votre sérieux."),
           ("Tarifs transparents","Déplacement, débouchage, recherche de fuite : la confiance avant l'appel."),
           ("Zone d'intervention","Vos villes et vos délais, pour ressortir sur « plombier + ville »."),
           ("Bouton d'appel","Toujours visible sur téléphone, là où se font 9 recherches sur 10."),
           ("Garanties","Assurance, garantie de la main-d'œuvre, prix signé avant de commencer.")],
    faq=[("Mon site peut-il ressortir sur « plombier + ma ville » ?","Oui : il est pensé pour ça, avec vos zones d'intervention et vos services."),
         ("Je peux ajouter une intervention depuis le chantier ?","Oui, depuis votre téléphone, avec la photo et le prix."),
         ("Le site convient-il à un auto-entrepreneur ?","Oui, la formule Essentiel est faite pour démarrer, dès 29 € par mois.")]),
]
# 08/11/2026 : page Cannes retirée (pas de pages par ville, Cannes non affiché sur le site). Gardée ici pour mémoire, non générée.
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
         ("Quels métiers accompagnez-vous ?","Chauffeurs VTC, restaurants, garages et concessions, agences immobilières, artisans du bâtiment, coiffeurs et instituts de beauté, masseurs et ostéopathes, boulangeries, plombiers et électriciens, et d'autres commerces sur demande.")],
    cities=["Cannes","Le Cannet","Mougins","Antibes","Juan-les-Pins","Vallauris","Mandelieu-la-Napoule","Grasse","Nice","Cagnes-sur-Mer","Saint-Laurent-du-Var","Menton","Monaco","Saint-Raphaël","Fréjus","Sainte-Maxime","Saint-Tropez"])

# 07/11/2026 (Claude, demande d'Anthony) : pages locales par ville, chacune avec son propre contenu (pas de copie).
def _city(slug, city, title, meta, h1, lead, feats, faq, near, dist):
    return dict(slug=slug, k=None, city=city, title=title, meta=meta, h1=h1, lead=lead, feats=feats, faq=faq, cities=near, dist=dist)
CITIES = [
  _city("creation-site-internet-nice", "Nice", "Création de site internet à Nice pour les pros",
    "Création de site internet à Nice pour commerçants, artisans, restaurants et indépendants : site mobile, réservation, version anglaise. En ligne en 48 h, dès 29 €/mois.",
    "Création de site internet à Nice : un site qui parle aux Niçois et aux visiteurs",
    "Entre la clientèle du quartier et les millions de visiteurs qui arrivent par l'aéroport, un pro niçois doit être trouvé sur Google en français comme en anglais. On s'en occupe depuis Cannes, à une demi-heure.",
    [("Trouvé sur « métier + Nice »","Titres, textes et fiches pensés pour ressortir quand on cherche votre métier à Nice ou dans votre quartier : Vieux-Nice, Libération, Port, Cimiez."),
     ("Clientèle internationale","Une version anglaise (incluse en Premium) pour les touristes et la clientèle d'affaires de passage."),
     ("Réservation et rendez-vous","Table, rendez-vous, course ou devis : la demande arrive directement chez vous, avec les coordonnées du client."),
     ("Pensé pour le téléphone","La plupart de vos clients vous cherchent depuis leur mobile, souvent dans la rue : bouton d'appel et itinéraire en un geste."),
     ("Horaires de saison","Horaires d'été, fermeture annuelle, jours fériés : vous les changez vous-même en quelques secondes."),
     ("Avis Google affichés","Vos meilleurs avis mis en avant pour rassurer ceux qui ne vous connaissent pas encore (Pro et Premium).")],
    [("Vous déplacez-vous à Nice ?","Tout se fait à distance, sans rendez-vous. Si vous préférez en parler de vive voix, Cannes n'est qu'à une trentaine de kilomètres."),
     ("Mon commerce est dans une rue piétonne, ça compte pour Google ?","Oui : votre adresse exacte, votre plan d'accès et votre fiche Google doivent être cohérents. On veille à ce que le site donne les mêmes informations."),
     ("Pouvez-vous reprendre mon ancien site ?","Oui. On reprend vos textes et photos dans un modèle moderne et on garde votre nom de domaine.")],
    ["Nice","Saint-Laurent-du-Var","Cagnes-sur-Mer","Villefranche-sur-Mer","Beaulieu-sur-Mer","Èze","La Trinité","Carros"], "une trentaine de kilomètres"),
  _city("creation-site-internet-antibes", "Antibes", "Création de site internet à Antibes et Juan-les-Pins",
    "Création de site internet à Antibes, Juan-les-Pins et Sophia Antipolis pour commerçants, artisans et indépendants. Site mobile, version anglaise, en ligne en 48 h, dès 29 €/mois.",
    "Création de site internet à Antibes, Juan-les-Pins et Sophia Antipolis",
    "Port Vauban, Juan-les-Pins en saison, Sophia Antipolis toute l'année : à Antibes, vos clients sont aussi bien des habitants que des plaisanciers et des cadres en déplacement. Votre site doit leur parler à tous. Nous sommes à Cannes, à dix minutes.",
    [("Saison et hors saison","Mettez en avant vos offres d'été à Juan-les-Pins, puis vos services de l'année : vous changez les textes vous-même."),
     ("Clientèle anglophone","Plaisanciers, résidents étrangers, visiteurs : la version anglaise est incluse en Premium."),
     ("Clientèle d'affaires","Pour Sophia Antipolis : déjeuners d'équipe, transferts, services aux entreprises, avec demande de devis en ligne."),
     ("Réservation directe","Vos clients réservent chez vous, sans commission de plateforme sur les demandes qui arrivent par votre site."),
     ("Référencement local","Votre site est construit pour « votre métier + Antibes », « Juan-les-Pins » ou « Biot » selon votre zone."),
     ("Vous restez autonome","Prix, horaires et photos modifiables depuis votre téléphone, avec aperçu en direct.")],
    [("Travaillez-vous avec des entreprises de Sophia Antipolis ?","Oui : le site met en avant vos services aux professionnels et reçoit leurs demandes de devis."),
     ("Mon activité est saisonnière, le site l'est aussi ?","Non, le site reste en ligne toute l'année. Vous adaptez simplement textes et horaires selon la saison."),
     ("Faut-il se rencontrer ?","Ce n'est pas nécessaire, tout se fait en ligne. Nous sommes à Cannes, tout près si vous préférez en parler.")],
    ["Antibes","Juan-les-Pins","Biot","Valbonne","Sophia Antipolis","Vallauris","Golfe-Juan","Villeneuve-Loubet"], "une dizaine de kilomètres"),
  _city("creation-site-internet-grasse", "Grasse", "Création de site internet à Grasse et dans le pays grassois",
    "Création de site internet à Grasse, Mouans-Sartoux, Peymeinade et dans le pays grassois pour artisans, commerçants et indépendants. En ligne en 48 h, dès 29 €/mois.",
    "Création de site internet à Grasse et dans le pays grassois",
    "Artisans du parfum, commerces du centre historique, artisans du bâtiment des villages alentour : à Grasse, beaucoup de clients viennent de loin ou arrivent par la route. Votre site doit dire clairement ce que vous faites, où vous êtes et comment venir.",
    [("Plan d'accès clair","Adresse, stationnement, horaires : les infos que cherchent ceux qui montent à Grasse pour vous voir."),
     ("Visiteurs du monde entier","La ville attire une clientèle internationale : version anglaise incluse en Premium."),
     ("Zone d'intervention","Artisans : affichez les communes où vous intervenez, de Mouans-Sartoux à Saint-Vallier-de-Thiey."),
     ("Demandes de devis","Type de travaux, code postal, date souhaitée : la demande arrive chez vous avec les coordonnées du client."),
     ("Vos réalisations en photos","Ateliers, créations, chantiers terminés : une galerie que vous complétez vous-même."),
     ("Sans engagement","Un abonnement mensuel, résiliable à tout moment, nom de domaine à votre nom.")],
    [("Intervenez-vous dans les villages autour de Grasse ?","Oui, tout se fait à distance : Mouans-Sartoux, Peymeinade, Le Tignet, Cabris, Saint-Cézaire, Châteauneuf et au-delà."),
     ("Je vends des produits artisanaux, je peux les présenter ?","Oui, avec photos, descriptions et prix. Pour la vente en ligne avec paiement, parlez-nous de votre projet."),
     ("Combien de temps pour être en ligne ?","En général 48 heures après réception de vos informations et de vos photos.")],
    ["Grasse","Mouans-Sartoux","Peymeinade","Le Tignet","Cabris","Saint-Vallier-de-Thiey","Châteauneuf-Grasse","Opio"], "une quinzaine de kilomètres"),
  _city("creation-site-internet-saint-raphael-frejus", "Saint-Raphaël", "Création de site internet à Saint-Raphaël et Fréjus",
    "Création de site internet à Saint-Raphaël, Fréjus, Agay et dans l'Estérel pour commerçants, artisans et restaurants. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    "Création de site internet à Saint-Raphaël, Fréjus et dans l'Estérel",
    "Dans l'est du Var, l'été multiplie la population et les recherches sur Google. Être visible avant la saison, avec des horaires et des prix à jour, fait toute la différence pour un commerce, un restaurant ou un artisan.",
    [("Prêt avant la saison","En ligne en 48 heures : de quoi être visible dès les premières réservations de printemps."),
     ("Horaires et offres d'été","Vous mettez à jour vos horaires, menus et tarifs de saison vous-même, depuis votre téléphone."),
     ("Réservation en ligne","Table, rendez-vous ou intervention : les demandes arrivent directement chez vous, même quand vous êtes débordé."),
     ("Visiteurs étrangers","Version anglaise incluse en Premium pour la clientèle touristique."),
     ("Toute l'année aussi","Le site continue de travailler hors saison pour la clientèle locale de Fréjus, Puget-sur-Argens ou Roquebrune."),
     ("Avis Google","Vos meilleurs avis affichés sur le site (Pro et Premium).")],
    [("Vous intervenez dans le Var ?","Oui : Saint-Raphaël, Fréjus, Agay, Roquebrune-sur-Argens, Puget-sur-Argens, Sainte-Maxime et partout en France à distance."),
     ("Mon restaurant n'ouvre qu'en saison, je paie toute l'année ?","L'abonnement est sans engagement : vous pouvez l'arrêter à la fin du mois en cours. Mais un site en ligne toute l'année garde sa place sur Google."),
     ("Faut-il se rencontrer ?","Non, tout se fait en ligne. Nous sommes à Cannes, à une quarantaine de kilomètres.")],
    ["Saint-Raphaël","Fréjus","Agay","Boulouris","Roquebrune-sur-Argens","Puget-sur-Argens","Sainte-Maxime","Les Adrets-de-l'Estérel"], "une quarantaine de kilomètres"),
  _city("creation-site-internet-cagnes-sur-mer", "Cagnes-sur-Mer", "Création de site internet à Cagnes-sur-Mer",
    "Création de site internet à Cagnes-sur-Mer, Villeneuve-Loubet, Saint-Laurent-du-Var et Vence pour commerces de proximité, artisans et indépendants. Dès 29 €/mois.",
    "Création de site internet à Cagnes-sur-Mer et alentours",
    "Entre Nice et Antibes, Cagnes-sur-Mer vit beaucoup de sa clientèle de proximité. Quand quelqu'un cherche un artisan, un garage ou un restaurant « près de chez moi », votre site doit sortir, avec vos horaires et votre téléphone en un clic.",
    [("Recherches « près de chez moi »","Adresse, quartier et zone desservie clairement indiqués : Cros-de-Cagnes, Haut-de-Cagnes, centre-ville."),
     ("Appel en un geste","Sur téléphone, un bouton d'appel toujours visible pour vous joindre tout de suite."),
     ("Demandes de rappel","Pour les artisans et dépanneurs : le client laisse son problème et son numéro, vous rappelez."),
     ("Vos tarifs affichés","Des prix clairs qui rassurent avant d'appeler, modifiables par vous à tout moment."),
     ("Fiche Google cohérente","On aligne les informations du site sur votre fiche Google : mêmes horaires, même adresse, même téléphone."),
     ("Sans engagement","Abonnement mensuel, nom de domaine à votre nom.")],
    [("Vous travaillez aussi à Vence et Saint-Paul-de-Vence ?","Oui, et à Villeneuve-Loubet, Saint-Laurent-du-Var, La Colle-sur-Loup et partout en France à distance."),
     ("J'ai déjà une page Facebook, est-ce suffisant ?","Une page Facebook aide, mais Google met mieux en avant un vrai site. Lisez notre article à ce sujet dans les conseils."),
     ("Combien ça coûte ?","Dès 29 € par mois et 190 € de mise en ligne, hébergement et nom de domaine inclus.")],
    ["Cagnes-sur-Mer","Villeneuve-Loubet","Saint-Laurent-du-Var","La Colle-sur-Loup","Saint-Paul-de-Vence","Vence","Saint-Jeannet","La Gaude"], "une vingtaine de kilomètres"),
  _city("creation-site-internet-menton", "Menton", "Création de site internet à Menton et Roquebrune-Cap-Martin",
    "Création de site internet à Menton, Roquebrune-Cap-Martin et Beausoleil pour commerces, restaurants et artisans. Site mobile, version anglaise, en ligne en 48 h, dès 29 €/mois.",
    "Création de site internet à Menton et Roquebrune-Cap-Martin",
    "À deux pas de l'Italie et de Monaco, Menton reçoit des clients de partout, et pas seulement en février. Un site clair, rapide sur mobile et disponible en anglais aide les visiteurs à vous choisir.",
    [("Clientèle transfrontalière","Version anglaise incluse en Premium pour les visiteurs étrangers."),
     ("Réservation et commandes","Table, rendez-vous, commande à retirer : la demande arrive chez vous avec les coordonnées du client."),
     ("Horaires des événements","Pendant les grandes fêtes de la ville, prévenez de vos horaires spéciaux en quelques secondes."),
     ("Pensé pour le téléphone","Itinéraire, appel et horaires accessibles en un geste."),
     ("Galerie photos","Vos produits, votre salle ou vos réalisations mis en valeur, en grand."),
     ("Vous restez autonome","Vous modifiez prix, textes et photos vous-même, ou on le fait pour vous en Pro et Premium.")],
    [("Vous intervenez jusqu'à Menton ?","Oui, tout se fait à distance : Menton, Roquebrune-Cap-Martin, Beausoleil, Cap-d'Ail et au-delà."),
     ("Et pour un commerce à Monaco ?","C'est possible à distance. Les mentions légales et l'adresse s'adaptent à votre situation : parlez-nous-en avant de commander."),
     ("Mon site peut-il être en italien ?","Le site est prévu en français et en anglais. Pour une autre langue, écrivez-nous avant de commander.")],
    ["Menton","Roquebrune-Cap-Martin","Beausoleil","Cap-d'Ail","Sainte-Agnès","Gorbio","Castellar","Castillon"], "une soixantaine de kilomètres"),
]
CITIES = []  # 07/11/2026 : retirées à la demande d'Anthony, MyCreativeSite vend dans toute la France
CITY_SLUG = {}

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
NAMES = {"vtc":"Chauffeur VTC","restaurant":"Restaurant","garage":"Garage et concession","immobilier":"Agence immobilière","batiment":"Artisan du bâtiment","beaute":"Coiffeur et institut de beauté","bienetre":"Masseur et ostéopathe","boulangerie":"Boulangerie","depannage":"Plombier et électricien","boutique":"Boutique en ligne"}
e = html.escape

def trade_links(cur):
    out = [f'<a href="/{p["slug"]}/">{NAMES[p["k"]]}</a>' for p in PAGES if p["slug"] != cur]
    out += [f'<a href="/{c["slug"]}/">Site internet à {c["city"]}</a>' for c in CITIES if c["slug"] != cur]
    out += [f'<a href="/{p["slug"]}/">{p["label"]}</a>' for p in INTENT if p["slug"] != cur]
    return "".join(out)

GUIDES = {"vtc": "site-internet-chauffeur-vtc-les-indispensables", "restaurant": "site-internet-restaurant-les-indispensables"}
def guide(p):
    g = GUIDES.get(p.get("k"))
    if not g: return ""
    from articles import ARTICLES
    a = next(x for x in ARTICLES if x["slug"] == g)
    return f'<p style="margin-top:18px">À lire : <a href="/conseils/{g}/">{e(a["title"])}</a></p>'

def page(p):
    url = f'{SITE}/{p["slug"]}/'
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    svc_ld = {"@context":"https://schema.org","@type":"Service","name":p["title"],"serviceType":"Création de site internet","url":url,
      "provider":{"@type":"ProfessionalService","name":"MyCreativeSite","url":SITE+"/","email":"contact@mycreativesite.fr"},
      "areaServed":({"@type":"City","name":p["city"]} if p.get("city") else "FR"),
      "offers":[{"@type":"Offer","name":n,"price":m,"priceCurrency":"EUR","description":f"{m} € par mois + {s} € de mise en ligne"} for n,m,s in PRICES]}
    crumbs_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":p["title"],"item":url}]}
    k = p["k"]
    if k:
        visual = f'<div class="shot"><img src="/img/modele-{k}-d.jpg" width="960" height="600" alt="Exemple de site internet {NAMES[k].lower()} réalisé avec MyCreativeSite" fetchpriority="high"></div>'
        demo = f'<a class="btn ghost" href="/modeles/{k}.html#{p["style"]}">Voir le modèle en vrai</a><a class="btn ghost" href="/espace/?demo={k}&amp;style={p["style"]}">Essayer l\'espace client</a>'
    else:
        visual = '<div class="shot"><img src="/img/og.jpg" width="1200" height="630" alt="Exemples de sites internet réalisés par MyCreativeSite" fetchpriority="high"></div>'
        demo = '<a class="btn ghost" href="/espace/?demo=restaurant">Essayer l\'espace client</a>' if p["slug"] == "site-internet-facile-a-modifier" else '<a class="btn ghost" href="/#modeles">Voir les modèles</a>'
    feats = "".join(f'<div class="feat"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t,d in p["feats"])
    prices = "".join(f'<div class="pc"><span>{n}</span><b>{m} €</b><span>par mois · + {s} € de mise en ligne</span></div>' for n,m,s in PRICES)
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in p["faq"])
    def _cl(c):
        sl = CITY_SLUG.get(c)
        return f'<a href="/{sl}/">{e(c)}</a>' if sl and sl != p["slug"] else e(c)
    cities = f'<p class="cities">{"Communes desservies" if p.get("city") else "Villes"} : {", ".join(_cl(c) for c in p["cities"])}.</p>' if p.get("cities") else ""
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
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png"><link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96.png"><link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192.png"><link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png?v=2"><meta name="apple-mobile-web-app-title" content="MyCreativeSite">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
<script type="application/ld+json">{json.dumps(svc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs_ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}<span>My<i>creativesite</i></span></a><span style="display:flex;gap:10px;align-items:center"><a href="/espace/" style="font-weight:600;font-size:.92rem;text-decoration:none">Espace client</a><a class="btn sm" href="/#commande">Je veux mon site</a></span></div></header>
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
  <div class="faq">{faq}</div>{guide(p)}
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

CTA_LINK = {"Voir le modèle restaurant": "/site-internet-restaurant/", "Voir le modèle VTC": "/site-internet-vtc/", "Découvrir les modèles par métier": "/#modeles", "Lancer mon site": "/#commande", "Un site pensé pour Google, en ligne en 48 h": "/site-internet-rapide/"}
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
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png"><link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96.png"><link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192.png"><link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png?v=2"><meta name="apple-mobile-web-app-title" content="MyCreativeSite">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
{lds}
<style>{CSS}{ARTICLE_CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="logo" href="/">{LOGO}<span>My<i>creativesite</i></span></a><span style="display:flex;gap:10px;align-items:center"><a href="/espace/" style="font-weight:600;font-size:.92rem;text-decoration:none">Espace client</a><a class="btn sm" href="/#commande">Je veux mon site</a></span></div></header>
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
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for p in PAGES + CITIES + INTENT:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w").write(page(p))
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    blog = build_blog()
    urls = [("", "1.0")] + [(p["slug"] + "/", "0.8") for p in PAGES + CITIES + INTENT] + [(u, "0.6") for u in blog] + [("cgv.html", "0.3")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>' for u, pr in urls]
    sm.append("</urlset>")
    open("sitemap.xml", "w").write("\n".join(sm) + "\n")
    print("pages :", len(PAGES) + len(CITIES) + len(INTENT), "· sitemap :", len(urls), "adresses")

if __name__ == "__main__":
    main()
