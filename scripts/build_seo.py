#!/usr/bin/env python3
"""MyCreativeSite — pages SEO (métiers + Côte d'Azur), plan du site.
Lancer depuis la racine du dépôt : python3 scripts/build_seo.py
Chaque page a un contenu propre (pas de copie) : titre, textes, fonctionnalités et questions du métier."""
import json, os, html, datetime

SITE = "https://mycreativesite.fr"
TODAY = datetime.date.today().isoformat()
PRICES = [("Essentiel", 29, 190), ("Pro", 49, 290), ("Premium", 79, 490)]
PACK = ("Pack Auto, Moto & Immo", 99, 490)
BOUTIQUE = ("Boutique", 99, 490)
# 09/11/2026 (Anthony) : garages, concessions et agences → Pack seul ; boutiques → formule Boutique seule  # site + annonces illimitées sur Abracadeal + CRM + une page Google par annonce

PAGES = [
  dict(slug="site-internet-vtc", k="vtc", style="luxe",
    title="Création de site internet pour chauffeur VTC",
    meta="Site internet pour chauffeur VTC : réservation de course en ligne, tarifs fixes, bouton WhatsApp, version anglaise. En ligne en 48 h, dès 29 €/mois, sans engagement.",
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
  # 12/11/2026 (Anthony) : page dédiée aux taxis, la page VTC redevient 100 % VTC. Métier Taxi = modèle vtc.html?taxi=1.
  dict(slug="site-internet-taxi", k="taxi", style="moderne", label="Taxi", eyebrow_name="taxi",
    title="Création de site internet pour taxi",
    meta="Site internet pour chauffeur de taxi : réservation de course en ligne, transport conventionné, gares et aéroports, bouton d'appel. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    h1="Le site de votre taxi, pour que vos clients vous réservent en direct",
    lead="Habitués, patients, hôtels, voyageurs qui arrivent en gare ou à l'aéroport : avec votre propre site, ils vous trouvent sur Google et vous réservent sans passer par une centrale.",
    feats=[("Réservation de course","Départ, arrivée, date et heure : la demande arrive par mail et vous confirmez au client."),
           ("Transport conventionné","Mettez en avant votre conventionnement CPAM pour les patients assis : consultations, examens, hospitalisations."),
           ("Bouton d'appel toujours visible","Sur téléphone, le client vous appelle ou vous écrit sur WhatsApp en un geste."),
           ("Gares, aéroports, longues distances","Vos trajets réguliers et vos zones desservies affichés clairement, pour ressortir sur Google dans votre ville."),
           ("Votre véhicule et vos services","Places, bagages, siège enfant, accès personnes à mobilité réduite, paiement par carte à bord."),
           ("Site en anglais","Pratique pour la clientèle touristique et d'affaires (inclus en Premium).")],
    faq=[("Puis-je indiquer que je suis conventionné CPAM ?","Oui. Le transport de patients assis est mis en avant dans vos services, et les demandes arrivent directement chez vous."),
         ("Je dépends d'une centrale de réservation, le site est-il utile ?","Oui : il vous apporte vos propres clients, ceux qui vous cherchent sur Google ou qui veulent rappeler le même chauffeur."),
         ("Je peux modifier mes zones et mes services moi-même ?","Oui, depuis votre espace client, à tout moment, sans rien connaître à l'informatique.")]),
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
  dict(slug="site-internet-garage-mecanique", k="atelier", style="audacieux", label="Garage d'entretien et mécanique",
    title="Création de site internet pour garage mécanique et entretien automobile",
    meta="Site internet pour garage mécanique : rendez-vous atelier en ligne, vidange, pneus, freins, diagnostic, forfaits et tarifs. Dès 29 €/mois, sans engagement.",
    h1="Le site internet des garages d'entretien et de réparation",
    lead="Vidange, pneus, freins, distribution, diagnostic : vos clients voient vos forfaits, prennent rendez-vous en ligne et arrivent à l'atelier en sachant le prix.",
    why=("Pourquoi un site pour un garage mécanique ?", ["Quand un voyant s'allume ou qu'il faut changer les pneus, l'automobiliste cherche un garage près de chez lui sur son téléphone. Il choisit souvent celui qui affiche ses prix et permet de prendre rendez-vous tout de suite.", "Un site avec vos forfaits, vos tarifs et la prise de rendez-vous atelier en ligne vous apporte ces clients, sans passer par des plateformes qui prennent une commission sur chaque intervention."]),
    feats=[("Rendez-vous atelier","Prestation, date, immatriculation : la demande arrive dans votre agenda et par mail."),
           ("Forfaits affichés","Vidange, pneus, freins, climatisation, distribution : des prix clairs avant l'appel."),
           ("Toutes marques","Mettez en avant ce que vous faites : entretien, diagnostic, carrosserie, contrôle technique."),
           ("Véhicule de prêt","Indiquez vos services : prêt de véhicule, dépose matinale, paiement en plusieurs fois."),
           ("Avis Google","Vos avis mis en avant pour rassurer les nouveaux clients."),
           ("Modifiable depuis le téléphone","Tarifs, horaires et photos changés en quelques secondes.")],
    faq=[("Combien coûte un site internet pour un garage ?","Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement. La version atelier ne comprend pas de véhicules à vendre."),
         ("Je vends aussi des véhicules d'occasion","Choisissez alors le Pack Auto, Moto & Immo : stock de véhicules, une page Google par véhicule et annonces illimitées sur Abracadeal."),
         ("Je peux gérer mes créneaux d'atelier ?","Oui : horaires, jours fermés et nombre de véhicules pris en charge en même temps, depuis votre espace client."),
         ("Combien de temps pour être en ligne ?","En général 48 heures après réception de vos informations et photos.")]),
  dict(slug="site-internet-garage", k="garage", style="audacieux", pack=True,
    title="Création de site internet pour garage auto et moto",
    meta="Site internet pour garage auto et moto : rendez-vous atelier, forfaits, stock de véhicules d'occasion avec une page par véhicule sur Google, annonces illimitées sur Abracadeal. 99 €/mois, sans engagement.",
    h1="Le site internet des garages auto et moto qui remplit l'atelier et vend les occasions",
    lead="Rendez-vous atelier, forfaits affichés, véhicules d'occasion et reprise : un site qui travaille pour vous pendant que vous êtes sous le capot. Avec le Pack Auto, Moto & Immo, chaque véhicule a aussi sa page sur Google et part en annonce sur Abracadeal.",
    feats=[("Prise de rendez-vous","Prestation, date souhaitée, immatriculation : la demande arrive par mail et dans votre espace « Mes clients »."),
           ("Forfaits et tarifs","Vidange, pneus, freins, climatisation : des prix affichés qui donnent confiance avant même l'appel."),
           ("Stock de véhicules","Voitures et motos avec photos, fiche technique complète, prix et statut (en vente, réservé, vendu), filtrables par marque, énergie et budget."),
           ("Une page Google par véhicule","Pack Auto, Moto & Immo : chaque occasion a sa propre page (« Peugeot 308 2021 – 18 990 € – votre ville »), lisible par Google et partageable sur WhatsApp."),
           ("Annonces illimitées sur Abracadeal","Pack Auto, Moto & Immo : vos véhicules sont publiés et mis à jour automatiquement sur Abracadeal, sans passerelle à payer."),
           ("Estimation de reprise","Le client envoie son immatriculation et son kilométrage pour une estimation : un contact de plus à chaque visite.")],
    faq=[("Je peux ajouter mes véhicules moi-même ?","Oui : dans votre espace client, l'onglet « Mes véhicules » vous fait remplir une vraie fiche (marque, modèle, année, kilométrage, énergie, boîte, puissance, équipements, jusqu'à 30 photos). Le site et Abracadeal se mettent à jour tout seuls."),
         ("Je vends aussi des motos, c'est prévu ?","Oui : la fiche accepte voitures, motos et scooters, et Google les reconnaît comme tels."),
         ("Je n'ai pas d'atelier, je fais uniquement de la vente","Choisissez la version concession : plus d'atelier ni de rendez-vous, tout le site est tourné vers vos véhicules à vendre."),
         ("Quelle formule pour un garage ?","Si vous faites l'entretien et la réparation sans vendre de véhicules, la version atelier est disponible dès 29 € par mois (formules Essentiel, Pro, Premium). Si vous vendez aussi des véhicules, le Pack Auto, Moto & Immo, à 99 € par mois et 490 € de mise en ligne, ajoute les annonces illimitées sur Abracadeal, le CRM et une page Google par véhicule."),
         ("Combien de temps pour être en ligne ?","En général 48 heures après réception de vos informations et photos.")]),
  dict(slug="site-internet-agence-immobiliere", k="immobilier", style="riviera", pack=True,
    title="Création de site internet pour agence immobilière",
    meta="Site internet pour agence immobilière indépendante : biens à vendre et à louer avec DPE et GES, une page Google par bien, demande d'estimation en ligne, annonces illimitées sur Abracadeal. 99 €/mois, sans engagement.",
    h1="Un site d'agence immobilière qui génère des mandats et des visites",
    lead="Vos biens bien présentés, une demande d'estimation en ligne qui capte les vendeurs, une page Google par bien et vos annonces diffusées sur Abracadeal sans passerelle payante.",
    feats=[("Recherche de biens","Achat ou location, ville, budget, nombre de pièces : filtres en direct."),
           ("Fiches complètes et conformes","Surface, pièces, chambres, étage, DPE et GES avec leurs valeurs, dépenses d'énergie, copropriété et honoraires : les mentions obligatoires s'écrivent toutes seules."),
           ("Une page Google par bien","Pack Auto, Moto & Immo : chaque bien a sa propre page (« Appartement 3 pièces 78 m² – Fréjus – 450 000 € »), lisible par Google et partageable."),
           ("Annonces illimitées sur Abracadeal","Pack Auto, Moto & Immo : vos biens sont publiés et mis à jour automatiquement, retirés dès qu'ils sont vendus ou loués."),
           ("Estimation gratuite","Un formulaire dédié pour recevoir des demandes de vendeurs, suivies dans votre CRM."),
           ("Présentation de l'agent","Votre parcours, vos langues, votre secteur : la confiance avant le premier appel.")],
    faq=[("Je peux ajouter mes biens moi-même ?","Oui : l'onglet « Mes biens » de votre espace client vous fait remplir une fiche complète (vente ou location, surface, DPE et GES, charges, honoraires, jusqu'à 30 photos). Le site et Abracadeal suivent automatiquement."),
         ("Les mentions obligatoires sont-elles gérées ?","Oui : DPE et GES avec leurs étiquettes, dépenses d'énergie estimées, copropriété, honoraires, et en location le loyer charges comprises et le dépôt de garantie."),
         ("Le site est-il adapté à un agent indépendant ou mandataire ?","Oui : il met en avant votre nom, votre secteur et votre accompagnement personnel."),
         ("Faut-il payer une passerelle de diffusion ?","Non : avec le Pack Auto, Moto & Immo, la diffusion sur Abracadeal est incluse et illimitée.")]),
  dict(slug="site-internet-concession-automobile", k="concession", style="luxe", pack=True,
    title="Création de site internet pour concession automobile",
    meta="Site internet pour concession automobile : stock de voitures d'occasion, une page Google par véhicule, reprise, financement, annonces illimitées sur Abracadeal. 99 €/mois, sans engagement.",
    h1="Le site internet des concessions automobiles qui vend vos voitures",
    lead="100 % vente : pas d'atelier, pas de rendez-vous, tout le site est tourné vers votre stock. Chaque véhicule a sa propre page sur Google et part automatiquement en annonce sur Abracadeal.",
    feats=[("Votre stock en vitrine","Voitures filtrables par marque, énergie et budget, avec photos, prix et statut (en vente, réservé, vendu)."),
           ("Une page Google par véhicule","« BMW Série 3 2020 – 24 900 € – votre ville » : une vraie page par véhicule, avec fiche technique, équipements et photos, que Google peut afficher dans ses résultats."),
           ("Annonces illimitées sur Abracadeal","Votre stock est publié et mis à jour tout seul sur Abracadeal. Un véhicule vendu disparaît partout en même temps."),
           ("Fiche véhicule complète","Marque, modèle, version, année, kilométrage, énergie, boîte, puissance, couleur, Crit'Air, garantie, jusqu'à 30 photos : vous remplissez une fois, tout suit."),
           ("Reprise et financement","Demande de reprise en ligne (immatriculation et kilométrage), que vous recevez par mail et dans votre espace, et vos solutions de financement mises en avant."),
           ("Demandes suivies dans un CRM","« Je suis intéressé », demandes d'essai et de reprise arrivent dans votre espace, avec l'historique de chaque client.")],
    faq=[("Quelle différence avec un site de garage ?","La version concession retire l'atelier, les forfaits et la prise de rendez-vous : les boutons mènent à vos véhicules et le site parle d'achat, de reprise et de financement."),
         ("Je vends aussi des motos, ça marche ?","Oui : chaque fiche peut être une voiture, une moto ou un scooter. Si vous vendez surtout des motos, choisissez plutôt notre modèle concession moto."),
         ("Combien coûte le Pack Auto, Moto & Immo ?","99 € par mois et 490 € de mise en ligne, une fois. Annonces illimitées sur Abracadeal, CRM et page Google par véhicule compris, sans engagement."),
         ("Faut-il une passerelle ou un logiciel de diffusion ?","Non : la diffusion sur Abracadeal est incluse. Vous mettez à jour votre stock une seule fois, dans votre espace client."),
         ("Mes véhicules apparaîtront-ils sur Google ?","Chaque véhicule a sa propre page avec un titre, une description et des données structurées (marque, modèle, kilométrage, prix) que Google sait lire. Le délai d'apparition dépend de Google, en général quelques jours à quelques semaines.")]),
  dict(slug="site-internet-concession-moto", label="Concession moto", k="moto", style="luxe", pack=True,
    title="Création de site internet pour concession moto",
    meta="Site internet pour concession moto et scooter : motos d'occasion avec une page Google par modèle, reprise, financement, atelier en option, annonces illimitées sur Abracadeal. 99 €/mois, sans engagement.",
    h1="Un site pour vendre vos motos et scooters, même pendant que la boutique est fermée",
    lead="Roadsters, trails, sportives, scooters : vos motos d'occasion en vitrine, chacune avec sa page sur Google, et diffusées sur Abracadeal sans rien ressaisir.",
    feats=[("Vos motos en vitrine","Photos, cylindrée, kilométrage, année et prix, filtrables par marque et budget."),
           ("Une page par moto","« Yamaha MT-07 2020 – 6 490 € – votre ville » : chaque moto a sa page, reconnue par Google comme une moto."),
           ("Atelier en option","Entretien, pneus, préparation au contrôle : gardez la prise de rendez-vous si vous avez un atelier, retirez-la sinon."),
           ("Reprise et financement","Le motard laisse l'immatriculation et le kilométrage de sa moto actuelle, vous le rappelez avec votre estimation. Vos solutions de financement sont mises en avant."),
           ("Annonces illimitées sur Abracadeal","Avec le Pack Auto, Moto & Immo, vos motos sont publiées et retirées automatiquement."),
           ("Mis à jour depuis votre téléphone","Une moto vendue ? Vous la passez en « Vendu » en deux clics, le site et Abracadeal suivent.")],
    faq=[("Je vends aussi des scooters et des quads, c'est possible ?","Oui : la fiche propose moto, scooter et autres types de véhicules."),
         ("J'ai aussi un atelier, je garde la prise de rendez-vous ?","Oui : la version garage garde l'atelier et les rendez-vous. La version concession les retire pour ne parler que de vente."),
         ("Combien ça coûte ?","Le Pack Auto, Moto & Immo : 99 € par mois et 490 € de mise en ligne, une fois. Annonces illimitées sur Abracadeal, CRM et une page Google par moto compris, sans engagement.")]),
  dict(slug="site-internet-artisan-batiment", k="batiment", style="moderne",
    title="Création de site internet pour artisan du bâtiment et BTP",
    meta="Site internet pour artisan du bâtiment, entreprise de maçonnerie, de rénovation ou du BTP : demande de devis, réalisations avant/après, tarifs au m², zone d'intervention, décennale. Dès 29 €/mois.",
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
  dict(slug="site-internet-veterinaire", k="veterinaire", why=('Pourquoi un site pour une clinique vétérinaire ?', ["Les propriétaires d'animaux cherchent d'abord sur leur téléphone : un numéro d'urgence, des horaires, un créneau pour le rappel de vaccin. Sans site clair, ces appels arrivent tous à l'accueil, souvent au mauvais moment.", 'Un site qui affiche la garde, les actes courants et la prise de rendez-vous en ligne libère le téléphone et rassure avant la première visite. Il reste sobre et informatif, comme le veut la déontologie vétérinaire.']), style="riviera",
    title="Création de site internet pour vétérinaire et clinique vétérinaire",
    meta="Site internet pour vétérinaire et clinique vétérinaire : prise de rendez-vous en ligne, actes courants, tarifs indicatifs, urgences et horaires. Dès 29 €/mois, sans commission.",
    h1="Le site internet des vétérinaires et cliniques vétérinaires",
    lead="Cabinet ou clinique vétérinaire, chiens, chats ou NAC : les propriétaires prennent rendez-vous en ligne, trouvent vos horaires et votre numéro d'urgence, et découvrent votre équipe.",
    feats=[("Prise de rendez-vous","Motif, vétérinaire, jour et heure : le créneau est réservé dans votre agenda, sans commission."),
           ("Urgences et garde","Votre numéro d'urgence et vos horaires de garde, visibles en un coup d'œil sur téléphone."),
           ("Actes courants","Vaccins, bilans, stérilisation, dentaire, imagerie : des fiches claires, filtrables par animal."),
           ("Tarifs indicatifs","Consultation, vaccins, identification : des prix informatifs, modifiables à tout moment."),
           ("L'équipe et la clinique","Vétérinaires, auxiliaires, équipement et accès, pour rassurer avant la première visite."),
           ("Une communication sobre","Des textes factuels, sans promesse ni comparaison, dans le respect des règles de la profession.")],
    faq=[("Le site respecte-t-il les règles de communication des vétérinaires ?","Oui : les textes restent informatifs, sans publicité comparative ni promesse de résultat. Vous validez chaque texte avant la mise en ligne."),
         ("Je peux gérer mes créneaux moi-même ?","Oui, depuis votre espace client : horaires, jours fermés, vétérinaires disponibles et créneaux bloqués."),
         ("Je paie une commission sur les rendez-vous ?","Non : un abonnement fixe dès 29 € par mois, quel que soit le nombre de rendez-vous."),
         ('Combien coûte un site internet pour une clinique vétérinaire ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement. La prise de rendez-vous en ligne est incluse dès la formule Pro.')]),
  dict(slug="site-internet-auto-ecole", k="autoecole", why=('Pourquoi un site pour une auto-école ?', ["Les élèves et leurs parents comparent les auto-écoles en ligne avant de s'inscrire : prix des forfaits, financement, planning, agence la plus proche. Une auto-école sans site perd ces élèves au profit des plateformes nationales.", 'Avec un site à votre nom, vos formules et vos tarifs sont visibles, les élèves réservent leurs leçons sans appeler et vous gardez la relation directe, sans commission sur chaque heure de conduite.']), style="pop",
    title="Création de site internet pour auto-école",
    meta="Site internet pour auto-école : inscription et réservation des leçons en ligne, formules permis B et conduite accompagnée, tarifs et agences. Dès 29 €/mois.",
    h1="Le site internet des auto-écoles",
    lead="Permis B, conduite accompagnée, boîte automatique ou code seul : vos futurs élèves comparent vos formules, réservent leurs leçons et vous contactent depuis leur téléphone.",
    feats=[("Réservation des leçons","Formation, agence, jour et heure : la demande arrive dans votre agenda, sans commission."),
           ("Les formules","Permis B, AAC, boîte auto, heures à l'unité : des fiches claires, filtrables par type."),
           ("Tarifs affichés","Forfaits et prestations à l'unité, comme l'exige la réglementation, modifiables à tout moment."),
           ("Financements","CPF et permis à 1 € par jour mis en avant pour rassurer les familles."),
           ("Agences et moniteurs","Adresses, horaires et présentation de l'équipe."),
           ("Agrément visible","Votre numéro d'agrément préfectoral affiché en pied de page.")],
    faq=[("Les élèves peuvent-ils réserver leurs leçons en ligne ?","Oui : ils choisissent un créneau libre, vous gérez vos disponibilités depuis votre espace client."),
         ("Je peux afficher mon taux de réussite ?","Oui : affichez le taux officiel publié pour votre établissement, avec sa source."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois, quel que soit le nombre d'élèves."),
         ('Combien coûte un site internet pour une auto-école ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement et sans commission sur les heures de conduite.'),
         ('Le site convient-il à une auto-école avec plusieurs agences ?', "Oui : chaque agence a son adresse et ses horaires, et l'élève choisit son agence au moment de réserver.")]),
  dict(slug="site-internet-coach-sportif", k="coach", why=('Pourquoi un site pour un coach sportif ?', ["Un client qui cherche un coach ou une petite salle veut savoir si c'est pour lui, combien ça coûte et quand il peut commencer. Les réseaux sociaux montrent votre énergie, mais pas vos formules ni votre planning.", 'Un site avec une séance découverte réservable en ligne, vos carnets et vos cours en petit groupe transforme les curieux en clients, même quand vous êtes en séance.']), style="neon",
    title="Création de site internet pour coach sportif et salle de sport",
    meta="Site internet pour coach sportif, préparateur physique et petite salle de sport : réservation de séances, formules, carnets et planning. Dès 29 €/mois, sans commission.",
    h1="Le site internet des coachs sportifs et des petites salles",
    lead="Coaching individuel, petits groupes, cours à domicile ou en extérieur : vos clients découvrent vos formules et réservent leur séance en ligne.",
    feats=[("Réservation de séances","Séance, coach, jour et heure : réservé dans votre agenda, sans commission."),
           ("Formules et carnets","Séance découverte, carnets de 10, programmes : tout est clair avant de réserver."),
           ("Petits groupes","Le nombre de places par créneau est géré automatiquement."),
           ("Le studio","Photos, matériel, vestiaires, accès et parking."),
           ("Votre parcours","Diplômes et spécialités, pour donner confiance."),
           ("À domicile","Votre zone de déplacement à la place de l'adresse du studio.")],
    faq=[("Je peux limiter le nombre de places par cours ?","Oui : vous fixez le nombre de places par créneau, le site arrête les réservations quand c'est complet."),
         ("Le site convient-il à un coach sans salle ?","Oui : vous indiquez votre zone d'intervention, à domicile ou en extérieur."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un coach sportif ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Le site convient-il à une petite salle de sport ?', 'Oui : planning des cours, nombre de places par créneau, formules et carnets, présentation des coachs et du lieu.')]),
  dict(slug="site-internet-photographe", k="photographe", why=('Pourquoi un site pour un photographe ?', ['Les futurs mariés et les entreprises comparent les photographes sur Google avant de demander un devis. Un portfolio sur les réseaux sociaux ne dit ni vos prestations, ni vos prix de départ, ni vos disponibilités.', "Votre site met vos images en grand, présente clairement vos séances et reçoit les demandes de date avec toutes les informations utiles : moins d'allers-retours, plus de réservations."]), style="graphite",
    title="Création de site internet pour photographe",
    meta="Site internet pour photographe : galerie, prestations mariage, portrait et entreprise, demande de date en ligne, tarifs. Dès 29 €/mois, modifiable depuis votre téléphone.",
    h1="Le site internet des photographes",
    lead="Mariage, portrait, famille ou entreprise : vos photos en grand, vos prestations claires et une demande de date en deux clics.",
    feats=[("Vos images en grand","Des pages pensées pour mettre vos photos en valeur, sur ordinateur comme sur téléphone."),
           ("Demande de date","Prestation, lieu et date : la demande arrive dans votre agenda."),
           ("Prestations","Mariage, portrait, entreprise : des fiches claires avec ce qui est inclus."),
           ("Tarifs","Prix de départ et devis pour les mariages et les entreprises."),
           ("Le studio","Adresse, accès et zone de déplacement."),
           ("Vous","Votre parcours et votre façon de travailler.")],
    faq=[("Je peux changer mes photos moi-même ?","Oui, depuis votre espace client, en quelques secondes."),
         ("Le site convient-il à un photographe sans studio ?","Oui : vous indiquez votre zone d'intervention."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un photographe ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Mes photos restent-elles en bonne qualité ?', "Oui : elles sont optimisées pour s'afficher vite sur téléphone tout en restant nettes en grand sur ordinateur.")]),
  dict(slug="site-internet-toiletteur", k="toiletteur", why=('Pourquoi un site pour un salon de toilettage ?', ['Les propriétaires cherchent un toiletteur près de chez eux et veulent savoir si vous prenez leur animal, à quel prix et quand. Ces questions occupent le téléphone pendant que vous travaillez.', "Un site avec vos prestations par taille d'animal, vos tarifs et la prise de rendez-vous en ligne répond à leur place et remplit votre agenda."]), style="soleil",
    title="Création de site internet pour toiletteur et salon de toilettage",
    meta="Site internet pour salon de toilettage canin et félin : prise de rendez-vous en ligne, prestations par taille d'animal, tarifs et horaires. Dès 29 €/mois.",
    h1="Le site internet des toiletteurs",
    lead="Salon de toilettage ou toiletteur à domicile : les propriétaires choisissent la prestation selon leur animal et prennent rendez-vous en ligne.",
    feats=[("Prise de rendez-vous","Prestation, taille de l'animal, créneau : directement dans votre agenda."),
           ("Prestations","Petit chien, grand chien, chat : des fiches claires et filtrables."),
           ("Tarifs","Prix de départ selon la taille et le pelage."),
           ("Le salon","Photos, matériel, accès et parking."),
           ("Vous","Votre expérience et votre façon de travailler, pour rassurer."),
           ("À domicile","Votre zone de déplacement si vous vous déplacez en camion.")],
    faq=[("Je peux bloquer des créneaux ?","Oui, depuis votre espace client : congés, jours fermés, créneaux réservés."),
         ("Le site convient-il à un toiletteur mobile ?","Oui : la zone de déplacement remplace l'adresse du salon."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un toiletteur ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ("Je fais aussi du toilettage à domicile, c'est possible ?", 'Oui : indiquez votre zone de déplacement, les clients choisissent salon ou domicile au moment de réserver.')]),
  dict(slug="site-internet-fleuriste", k="fleuriste", why=('Pourquoi un site pour un fleuriste ?', ['Une grande partie des commandes de fleurs se décide vite, souvent la veille. Sans site, ces clients passent par des plateformes qui prennent une commission sur chaque bouquet.', 'Avec votre propre site, vos créations de saison sont visibles, la commande se fait en deux minutes en retrait ou en livraison, et la marge reste chez vous.']), style="provence",
    title="Création de site internet pour fleuriste",
    meta="Site internet pour fleuriste : commande de bouquets en retrait ou livraison, créations de saison, mariages et deuil, horaires. Dès 29 €/mois, sans commission.",
    h1="Le site internet des fleuristes",
    lead="Bouquets, compositions, mariages et deuil : vos clients commandent en ligne, en retrait à la boutique ou en livraison, sans passer par une plateforme à commission.",
    feats=[("Commande en ligne","Création, retrait ou livraison, date et heure : la commande arrive chez vous."),
           ("Créations de saison","Bouquets, événements, plantes : vous changez la vitrine chaque semaine."),
           ("Mariages et deuil","Des pages claires pour les demandes sur devis."),
           ("Livraison","Zone, créneaux et frais affichés."),
           ("La boutique","Adresse, horaires et arrivages."),
           ("Sans commission","Contrairement aux plateformes de transmission florale.")],
    faq=[("Je peux mettre à jour la vitrine chaque semaine ?","Oui, depuis votre téléphone : photo, nom, prix."),
         ("Les clients peuvent-ils payer en ligne ?","Avec la formule Boutique, oui ; sinon ils paient au retrait ou à la livraison."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un fleuriste ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement ni commission sur les commandes.'),
         ('Puis-je recevoir des commandes pour le deuil et les mariages ?', 'Oui : des pages dédiées reçoivent les demandes sur devis, avec la date, le lieu et le message à inscrire.')]),
  dict(slug="site-internet-traiteur", k="traiteur", why=('Pourquoi un site pour un traiteur ?', ["Un client qui organise un mariage ou un cocktail d'entreprise compare plusieurs traiteurs en ligne. Il veut voir vos plats, se faire une idée du prix par personne et savoir si vous êtes libre à sa date.", "Un site avec votre carte en photos et un formulaire de devis complet vous apporte des demandes déjà qualifiées : type d'événement, nombre d'invités, date et lieu."]), style="nuit",
    title="Création de site internet pour traiteur",
    meta="Site internet pour traiteur : demande de devis par événement et nombre d'invités, carte cocktail, buffet et desserts, tarifs indicatifs. Dès 29 €/mois.",
    h1="Le site internet des traiteurs",
    lead="Mariages, cocktails d'entreprise, plateaux repas : vos clients découvrent votre carte et vous envoient une demande de devis complète.",
    feats=[("Demande de devis","Type d'événement, nombre d'invités, date : tout ce qu'il faut pour chiffrer."),
           ("La carte","Cocktail, buffet, desserts : des fiches avec photos et composition."),
           ("Tarifs indicatifs","Prix par personne pour aider le client à se projeter."),
           ("Allergènes","Indiqués sur chaque fiche."),
           ("Le laboratoire","Votre équipe, votre savoir-faire et votre zone de livraison."),
           ("Avis clients","Vos avis Google mis en avant.")],
    faq=[("Je reçois les demandes comment ?","Par mail et dans votre espace client, avec toutes les informations de l'événement."),
         ("Je peux afficher les allergènes ?","Oui, sur chaque fiche produit."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un traiteur ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Puis-je montrer des menus différents selon les événements ?', 'Oui : cocktails, buffets, repas et desserts ont chacun leurs fiches, filtrables par le client.')]),
  dict(slug="site-internet-location-bateau", k="nautisme", why=('Pourquoi un site pour un loueur de bateaux ?', ['La clientèle est souvent touristique et réserve depuis son téléphone, parfois la veille au soir. Sans site, elle passe par des plateformes qui prennent une commission sur chaque location.', 'Votre site présente votre flotte, vos tarifs et les règles (permis, caution, carburant) et prend les réservations directement, avec une version en anglais en option.']), style="marine",
    title="Création de site internet pour location de bateaux et jet-ski",
    meta="Site internet pour loueur de bateaux et jet-ski : réservation en ligne, flotte avec ou sans permis, sorties avec skipper, tarifs et saison. Dès 29 €/mois.",
    h1="Le site internet des loueurs de bateaux et de jet-ski",
    lead="Bateaux sans permis, semi-rigides, jet-ski ou sorties avec skipper : vos clients choisissent, réservent la date et arrivent au ponton en sachant tout.",
    feats=[("Réservation en ligne","Bateau, durée et date : réservé dans votre agenda, sans commission."),
           ("La flotte","Sans permis, avec permis, jet-ski, sorties : fiches avec équipements."),
           ("Tarifs","Demi-journée, journée, carburant et caution clairement indiqués."),
           ("Le ponton","Plan d'accès, parking et horaires selon la saison."),
           ("Sécurité","Permis, gilets et briefing expliqués avant la réservation."),
           ("En plusieurs langues","Option bilingue pour la clientèle touristique.")],
    faq=[("Je peux gérer plusieurs bateaux en même temps ?","Oui : vous indiquez le nombre de bateaux disponibles par créneau."),
         ("Le site peut-il être en anglais ?","Oui, avec l'option bilingue."),
         ("Je paie une commission ?","Non : un abonnement fixe dès 29 € par mois, contrairement aux plateformes de location."),
         ('Combien coûte un site internet pour un loueur de bateaux ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement ni commission sur les locations.'),
         ("Je loue aussi des jet-skis et des paddles, c'est possible ?", 'Oui : chaque bateau, jet-ski ou sortie a sa fiche, avec ses équipements, sa capacité et ses tarifs.')]),
  dict(slug="site-internet-kinesitherapeute", k="kine", why=('Pourquoi un site pour un cabinet de kinésithérapie ?', ['Un patient qui sort de chez son médecin avec une ordonnance cherche un cabinet proche et disponible. Il veut savoir quoi apporter, si vous pratiquez le tiers payant et comment venir.', 'Un site sobre, avec la prise de rendez-vous en ligne et les informations pratiques, allège le secrétariat. Les textes restent informatifs, sans avis ni promesse de résultat, dans le respect du code de déontologie.']), style="foret",
    title="Création de site internet pour kinésithérapeute",
    meta="Site internet pour masseur-kinésithérapeute et cabinet de kinésithérapie : prise de rendez-vous, informations pratiques, honoraires, dans le respect de la déontologie. Dès 29 €/mois.",
    h1="Le site internet des masseurs-kinésithérapeutes",
    lead="Cabinet seul ou à plusieurs, au cabinet ou à domicile : vos patients prennent rendez-vous en ligne et trouvent les informations pratiques, avec une présentation sobre et informative.",
    feats=[("Prise de rendez-vous","Motif, praticien, créneau : directement dans l'agenda du cabinet."),
           ("Informations pratiques","Documents à apporter, annulation, accès, tenue."),
           ("Honoraires","Conventionnement et tiers payant indiqués clairement."),
           ("Le cabinet","Salles, équipement et accessibilité."),
           ("Les praticiens","Noms, qualifications et inscription à l'Ordre."),
           ("Une présentation sobre","Des textes informatifs, sans avis ni promesse de résultat.")],
    faq=[("Le site respecte-t-il les règles de communication des kinésithérapeutes ?","Oui : les textes restent informatifs, sans procédé publicitaire, témoignage ni promesse de résultat. Vous validez chaque texte avant la mise en ligne."),
         ("Je peux gérer les créneaux de plusieurs praticiens ?","Oui, depuis votre espace client."),
         ("Je paie une commission sur les rendez-vous ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un kinésithérapeute ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Le site convient-il à un cabinet de groupe ?', 'Oui : chaque praticien a son nom, ses qualifications et ses créneaux ; le patient choisit au moment de réserver.')]),
  dict(slug="site-internet-dentiste", k="dentiste", why=('Pourquoi un site pour un cabinet dentaire ?', ["Les patients cherchent un cabinet qui prend de nouveaux patients, un créneau rapide et la conduite à tenir en cas d'urgence. Ces questions saturent souvent le standard.", "Un site sobre, avec la prise de rendez-vous en ligne, les honoraires, l'information sur les devis et les urgences, répond à ces questions. Les textes restent informatifs, sans avis ni photos avant-après, dans le respect du code de déontologie."]), style="ocean",
    title="Création de site internet pour chirurgien-dentiste",
    meta="Site internet pour chirurgien-dentiste et cabinet dentaire : prise de rendez-vous, actes, honoraires, urgences et informations pratiques, dans le respect de la déontologie. Dès 29 €/mois.",
    h1="Le site internet des chirurgiens-dentistes",
    lead="Vos patients prennent rendez-vous en ligne, trouvent vos horaires, les informations sur les urgences et les honoraires, avec une présentation sobre et informative.",
    feats=[("Prise de rendez-vous","Motif, praticien, créneau : directement dans l'agenda du cabinet."),
           ("Urgences","La conduite à tenir le soir, le week-end et les jours fériés."),
           ("Les actes","Expliqués simplement, avec la mention du devis avant toute prothèse."),
           ("Honoraires","Conventionnement, tiers payant et devis."),
           ("Le cabinet","Équipement, hygiène et accessibilité."),
           ("Une présentation sobre","Des textes informatifs, sans avis ni photos avant-après.")],
    faq=[("Le site respecte-t-il les règles de communication des chirurgiens-dentistes ?","Oui : les textes restent informatifs, sans procédé publicitaire, témoignage ni promesse de résultat. Vous validez chaque texte avant la mise en ligne."),
         ("Je peux gérer les créneaux de plusieurs praticiens ?","Oui, depuis votre espace client."),
         ("Je paie une commission sur les rendez-vous ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour un chirurgien-dentiste ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Le site peut-il afficher les informations sur les urgences ?', "Oui : vos créneaux d'urgence en semaine et la conduite à tenir le dimanche et les jours fériés (le 15 oriente vers le chirurgien-dentiste de garde).")]),
  dict(slug="site-internet-bijouterie", k="bijouterie", why=('Pourquoi un site pour une bijouterie-horlogerie ?', ["Avant d'acheter des alliances ou de confier une montre, les clients cherchent sur leur téléphone : une boutique de confiance près de chez eux, un atelier sur place, un ordre de prix. Sans site, ils partent vers les grandes enseignes et les sites marchands.", "Votre site présente votre sélection, votre savoir-faire sur mesure et les tarifs de l'atelier, et prend les rendez-vous pour un conseil, un dépôt ou une estimation. Vous gardez le contact direct, sans commission."]), style="minimal",
    title="Création de site internet pour bijouterie et horlogerie",
    meta="Site internet pour bijouterie, joaillerie et horlogerie : sélection de bijoux et de montres, création sur mesure, atelier de réparation, rendez-vous en ligne. Dès 29 €/mois.",
    h1="Le site internet des bijouteries et horlogeries",
    lead="Bijoutier, joaillier ou horloger : vos clients découvrent votre sélection, vos créations sur mesure et votre atelier, puis prennent rendez-vous en ligne.",
    feats=[("Prise de rendez-vous","Conseil, alliances, sur mesure, réparation ou estimation : directement dans votre agenda."),
           ("La sélection","Bijoux et montres en photos, filtrables par rayon, avec un prix ou « dès »."),
           ("L'atelier","Piles, révisions, mises à taille et gravures, avec les tarifs de base."),
           ("Le sur mesure","Alliances, bagues de fiançailles et transformation de bijoux de famille."),
           ("Rachat d'or","Les conditions affichées clairement : pièce d'identité, cours du jour, paiement."),
           ("La boutique","Adresse, horaires, accès sur sonnette et moyens de paiement.")],
    faq=[("Je peux montrer mes bijoux sans les vendre en ligne ?","Oui : le modèle présente votre sélection et prend des rendez-vous. Si vous voulez vendre en ligne, la formule Boutique est faite pour ça."),
         ("Je peux afficher « dès » plutôt qu'un prix exact ?","Oui, chaque pièce accepte un prix exact, un prix de départ ou « sur demande », modifiable depuis votre espace client."),
         ("Je paie une commission sur les ventes ou les rendez-vous ?","Non : un abonnement fixe dès 29 € par mois."),
         ('Combien coûte un site internet pour une bijouterie ?', 'Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ("Le site convient-il à un horloger seul, sans boutique de bijoux ?","Oui : vous gardez uniquement le rayon atelier et vos prestations de réparation.")]),
  dict(slug='site-internet-profession-liberale', k='liberal', why=('Pourquoi un site pour une profession libérale ?', ["Avant de choisir un avocat, un expert-comptable ou un consultant, un client se renseigne en ligne : vos domaines d'intervention, votre façon de travailler, comment prendre rendez-vous. Sans site, il ne trouve que des annuaires.", 'Un site sobre, qui présente vos missions, vos honoraires selon les règles de votre profession et la prise de rendez-vous, rassure avant le premier contact et vous évite les appels inutiles.']), style='corporate',
    title='Création de site internet pour profession libérale',
    meta='Site internet pour avocat, expert-comptable, consultant, courtier, architecte ou formateur : missions, honoraires, prise de rendez-vous, dans le respect de votre déontologie. Dès 29 €/mois.',
    h1='Le site internet des professions libérales',
    lead="Avocats, experts-comptables, consultants, courtiers, formateurs, traducteurs, architectes et bureaux d'études : vos clients comprennent ce que vous faites et prennent rendez-vous en ligne.",
    feats=[
           ('Prise de rendez-vous','Au cabinet, en visio ou par téléphone, dans votre agenda.'),
           ('Vos missions','Expliquées simplement, filtrables par domaine.'),
           ('Honoraires','Présentés selon les règles de votre profession.'),
           ('Informations pratiques','Documents à apporter, confidentialité, délais.'),
           ('Le cabinet',"Équipe, inscription à l'Ordre, accès."),
           ('Une présentation sobre',"Pas d'avis clients ni de promesse de résultat.")],
    faq=[
         ('Le site respecte-t-il les règles de ma profession ?','Oui : les textes restent informatifs et vous validez chaque texte avant la mise en ligne. Les mentions obligatoires de votre profession sont ajoutées.'),
         ('Je peux recevoir des demandes en visio ?','Oui, le client choisit au cabinet, en visio ou par téléphone.'),
         ('Combien coûte un site pour une profession libérale ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Le modèle convient-il à un avocat ?','Oui : le modèle est sans avis clients et présente les honoraires sous forme de convention, comme le prévoient les règles de la profession.')]),
  dict(slug='site-internet-services-a-domicile', k='services', why=('Pourquoi un site pour une entreprise de services à domicile ?', ["Les familles comparent plusieurs entreprises avant de confier leurs clés : services proposés, zone d'intervention, prix, crédit d'impôt. Elles veulent un devis rapidement.", 'Un site clair, avec vos formules, vos tarifs et une demande de devis en ligne, vous apporte des clients réguliers sans passer par des plateformes qui prennent une commission.']), style='zen',
    title='Création de site internet pour services à domicile',
    meta="Site internet pour entreprise de ménage, repassage, aide à domicile, garde d'enfants ou nettoyage : formules, tarifs, zone d'intervention, devis en ligne. Dès 29 €/mois.",
    h1='Le site internet des services à domicile',
    lead="Ménage, repassage, aide aux personnes âgées, garde d'enfants, nettoyage de bureaux : vos clients voient vos formules et demandent un devis en ligne.",
    feats=[
           ('Demande de devis','Service, fréquence et créneau souhaité.'),
           ('Vos formules','Ménage, linge, aide, filtrables.'),
           ('Tarifs',"À l'heure ou au forfait, avec la mention du crédit d'impôt."),
           ("Zone d'intervention",'Les communes que vous couvrez.'),
           ('Vos intervenants','Formés, assurés, toujours les mêmes.'),
           ('Avis clients','Remplacés par vos avis Google.')],
    faq=[
         ("Le site peut-il parler du crédit d'impôt ?","Oui, si votre entreprise est déclarée services à la personne : la mention et l'avance immédiate sont expliquées simplement."),
         ('Je peux gérer plusieurs intervenants ?','Oui, depuis votre espace client.'),
         ('Combien coûte un site pour une entreprise de ménage ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Je paie une commission sur les clients ?','Non : un abonnement fixe, sans commission.')]),
  dict(slug='site-internet-evenementiel', k='evenementiel', why=("Pourquoi un site pour un professionnel de l'événementiel ?", ['Les futurs mariés et les entreprises comparent les organisateurs, décorateurs et DJ sur Google et sur les réseaux. Ils veulent voir vos réalisations et une idée de prix avant de demander un devis.', "Un site avec vos prestations en photos, vos formules et un formulaire de devis complet vous apporte des demandes déjà qualifiées : type d'événement, date, nombre d'invités."]), style='luxe',
    title='Création de site internet pour wedding planner, DJ et événementiel',
    meta="Site internet pour wedding planner, décorateur, DJ, organisateur d'événements ou d'activités : prestations en photos, tarifs indicatifs, demande de devis. Dès 29 €/mois.",
    h1="Le site internet des professionnels de l'événementiel",
    lead="Wedding planners, décorateurs, DJ, organisateurs d'événements et d'activités de loisirs : montrez vos réalisations et recevez des demandes de devis complètes.",
    feats=[
           ('Demande de devis',"Type d'événement, date et nombre d'invités."),
           ('Vos prestations','En photos, filtrables : mariage, fête, entreprise.'),
           ('Tarifs indicatifs','Pour filtrer les demandes dès le départ.'),
           ('Votre équipe','Qui vous êtes et comment vous travaillez.'),
           ('Location','Votre décoration et votre matériel à louer.'),
           ('Avis clients','Remplacés par vos avis Google.')],
    faq=[
         ('Je peux montrer mes réalisations ?','Oui, vous ajoutez vos photos depuis votre téléphone.'),
         ('Le site convient-il à un DJ ?','Oui : vos formules, votre matériel et vos dates disponibles.'),
         ('Combien coûte un site pour un wedding planner ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Je paie une commission sur les événements ?','Non : un abonnement fixe, sans commission.')]),
  dict(slug='site-internet-chambres-d-hotes-gite', k='hebergement', why=("Pourquoi un site pour des chambres d'hôtes ou un gîte ?", ["Les plateformes de réservation prennent une commission sur chaque nuit. Beaucoup de voyageurs cherchent ensuite le site de l'établissement pour réserver en direct.", 'Votre propre site présente vos chambres, vos tarifs par saison et reçoit les demandes de réservation : vous fidélisez vos clients et gardez la marge.']), style='terracotta',
    title="Création de site internet pour chambres d'hôtes et gîte",
    meta="Site internet pour chambres d'hôtes, gîte ou maison d'hôtes : chambres en photos, tarifs par saison, table d'hôtes, demande de réservation en direct. Dès 29 €/mois.",
    h1="Le site internet des chambres d'hôtes et gîtes",
    lead="Chambres d'hôtes, gîtes et maisons d'hôtes : vos voyageurs découvrent vos chambres et réservent en direct, sans commission.",
    feats=[
           ('Réservation en direct','Logement, dates et nombre de personnes.'),
           ('Vos chambres','En photos, avec leurs équipements.'),
           ('Tarifs par saison','Basse et haute saison, semaine au gîte.'),
           ("Table d'hôtes",'Vos dîners et vos séjours.'),
           ('Infos pratiques','Arrivée, départ, animaux, accès.'),
           ('Avis clients','Remplacés par vos avis Google.')],
    faq=[
         ('Je garde mes annonces sur les plateformes ?','Oui, votre site vient en plus et vous apporte des réservations directes, sans commission.'),
         ('Le site gère-t-il les acomptes ?',"Vous confirmez chaque demande et indiquez vos conditions d'acompte."),
         ('Combien coûte un site pour un gîte ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Le site peut-il être en anglais ?','Oui, une version anglaise est disponible en option.')]),
  dict(slug='site-internet-tourisme-loisirs', k='tourisme', why=('Pourquoi un site pour un guide ou une activité de loisirs ?', ["Les touristes réservent leurs visites et activités depuis leur téléphone, souvent la veille. Sans site, ils passent par des plateformes qui prennent jusqu'à un quart du prix.", 'Votre site présente votre programme, vos tarifs et vos points de départ, et prend les réservations directement, avec une version en anglais en option.']), style='riviera',
    title='Création de site internet pour guide touristique et activités de loisirs',
    meta="Site internet pour guide, organisateur d'excursions, loueur de vélos, école de plongée ou activité de loisirs : programme, tarifs, réservation en ligne. Dès 29 €/mois.",
    h1='Le site internet du tourisme et des loisirs',
    lead="Guides, organisateurs d'excursions, loueurs de vélos, écoles de plongée et activités de loisirs : vos clients réservent en ligne, sans commission.",
    feats=[
           ('Réservation en ligne','Sortie, date et nombre de participants.'),
           ('Votre programme','Filtrable : visites, excursions, nature.'),
           ('Tarifs','Par personne, réduits pour les enfants.'),
           ('Points de départ',"Et prise en charge à l'hôtel."),
           ('Langues','Version anglaise en option.'),
           ('Avis clients','Remplacés par vos avis Google.')],
    faq=[
         ('Je garde mes annonces sur les plateformes ?','Oui, votre site vient en plus et vous apporte des réservations directes.'),
         ('Le site peut-il être en anglais ?','Oui, une version anglaise est disponible en option.'),
         ('Combien coûte un site pour un guide ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Je peux limiter le nombre de places ?','Oui, vous fixez le nombre de places par sortie dans votre agenda.')]),
  dict(slug='site-internet-location-demenagement', k='location', why=('Pourquoi un site pour un loueur de véhicules ou un déménageur ?', ["Un client qui cherche un utilitaire pour demain ou un déménageur compare les prix sur son téléphone. Il veut savoir quel volume choisir, combien ça coûte et si c'est disponible.", 'Un site avec votre flotte, vos tarifs clairs et la réservation en ligne vous apporte ces clients directement, face aux grandes enseignes.']), style='audacieux',
    title='Création de site internet pour location de véhicules et déménagement',
    meta="Site internet pour loueur de voitures et d'utilitaires ou entreprise de déménagement : flotte, tarifs, réservation en ligne, devis de déménagement. Dès 29 €/mois.",
    h1='Le site internet des loueurs de véhicules et déménageurs',
    lead="Location de voitures et d'utilitaires, déménagement et monte-meuble : vos clients choisissent le bon véhicule et réservent en ligne.",
    feats=[
           ('Réservation en ligne','Véhicule, durée et heure de départ.'),
           ('Votre flotte','Filtrable : utilitaires, voitures, déménagement.'),
           ('Tarifs clairs','Kilomètres inclus et options.'),
           ('Devis de déménagement','Volume, étages et date.'),
           ('Infos pratiques','Documents, caution, horaires de retour.'),
           ('Avis clients','Remplacés par vos avis Google.')],
    faq=[
         ('Je peux afficher mes disponibilités ?','Oui, vous fixez le nombre de véhicules par créneau dans votre agenda.'),
         ('Le site gère-t-il les devis de déménagement ?','Oui, le client indique son volume, les étages et la date.'),
         ('Combien coûte un site pour un loueur ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ('Je paie une commission sur les locations ?','Non : un abonnement fixe, sans commission.')]),
  dict(slug='site-internet-infirmier-liberal', k='infirmier', why=('Pourquoi un site pour un cabinet infirmier ?', ['Un patient qui sort de chez son médecin avec une ordonnance cherche un infirmier disponible près de chez lui, souvent pour le lendemain matin. Il veut savoir si vous vous déplacez, à quelles heures et comment vous joindre.', 'Un site sobre, avec la demande de passage en ligne, les heures de permanence et la zone de soins à domicile, répond à ces questions et soulage votre téléphone pendant les tournées. Les textes restent informatifs, sans avis ni publicité, comme le prévoit le code de déontologie infirmier.']), style='marine',
    title='Création de site internet pour infirmier libéral',
    meta='Site internet pour infirmier ou infirmière libéral et cabinet infirmier : soins à domicile, permanences, demande de passage en ligne, dans le respect de la déontologie. Dès 29 €/mois.',
    h1='Le site internet des infirmiers libéraux',
    lead='Infirmiers et infirmières libéraux, cabinets infirmiers : vos patients trouvent vos permanences, votre zone de soins à domicile et demandent un passage en ligne.',
    feats=[
           ('Demande de passage','Soin, lieu (domicile ou cabinet) et créneau souhaité.'),
           ('Permanences','Les heures de soins sans rendez-vous au cabinet.'),
           ('Zone de soins à domicile','Les communes où vous vous déplacez.'),
           ('Les soins','Présentés sobrement, sur prescription.'),
           ('Honoraires','Conventionnés, avec le tiers payant.'),
           ('Une présentation sobre','Sans avis ni publicité, dans le respect de la déontologie.')],
    faq=[
         ('Le site respecte-t-il le code de déontologie des infirmiers ?','Oui : les textes restent informatifs, sans publicité, avis ni promesse. Vous validez chaque texte avant la mise en ligne.'),
         ('Je peux gérer les demandes de plusieurs infirmiers ?','Oui, depuis votre espace client, avec un agenda commun au cabinet.'),
         ('Combien coûte un site pour un infirmier libéral ?','Dès 190 € de mise en ligne puis 29 € par mois avec la formule Essentiel, sans engagement.'),
         ("Le site rappelle-t-il quoi faire en cas d'urgence ?","Oui : un encadré rappelle d'appeler le 15 en cas d'urgence vitale.")]),
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
# 08/11/2026 : page Cannes retirée. 13/11/2026 (Anthony, « ok ») : remise en ligne, une seule page locale « basé à Cannes, partout en France » (impressions GSC sur « création site internet cannes / cagnes-sur-mer »). Pas d'autres pages par ville.
LOCAL = dict(slug="creation-site-internet-cannes", k=None, label="Création de site à Cannes",
    title="Création de site internet à Cannes et sur la Côte d'Azur",
    meta="Création de site internet pour les pros à Cannes, Nice, Antibes, Cagnes-sur-Mer, Grasse et partout en France. Basé à Cannes. En ligne en 48 h, dès 29 €/mois, sans engagement.",
    h1="Création de site internet à Cannes et sur la Côte d'Azur",
    lead="MyCreativeSite est basé à Cannes. Nous créons les sites des commerçants, artisans et indépendants de la Riviera, de Menton à Saint-Tropez, et de toute la France à distance : 31 métiers, en ligne en 48 heures.",
    feats=[("Basés à Cannes","Nous connaissons les métiers et la clientèle de la Côte d'Azur, locale comme internationale."),
           ("Référencement local","Votre site est pensé pour ressortir sur « votre métier + votre ville » dans Google."),
           ("Clientèle étrangère","Site en anglais en option, ou inclus en Premium, pour les touristes et la clientèle d'affaires."),
           ("Tout à distance","Pas de rendez-vous nécessaire : vous envoyez vos infos, on vous envoie votre site."),
           ("Vous restez autonome","Prix, horaires et photos modifiables depuis votre espace client."),
           ("Sans engagement","Un abonnement mensuel, résiliable à tout moment, nom de domaine à votre nom.")],
    faq=[("Intervenez-vous en dehors de Cannes ?","Oui : Nice, Antibes, Cagnes-sur-Mer, Grasse, Mougins, Mandelieu, Menton, Saint-Raphaël, Fréjus, Saint-Tropez, et toute la France à distance."),
         ("Faut-il se rencontrer ?","Ce n'est pas nécessaire : tout se fait en ligne. Si vous êtes près de Cannes, on peut aussi en parler de vive voix."),
         ("Quels métiers accompagnez-vous ?","31 métiers : chauffeurs VTC et taxis, restaurants, garages et concessions auto et moto, agences immobilières, artisans du bâtiment, coiffeurs et instituts, masseurs et ostéopathes, boulangeries, plombiers et électriciens, location de bateaux, chambres d'hôtes et bien d'autres."),
         ("Combien coûte un site internet à Cannes ?","Dès 29 € par mois et 190 € de mise en ligne, hébergement, nom de domaine et maintenance compris. Vous ne payez qu'après avoir vu et validé votre site.")],
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
INTENT_LOCAL = [LOCAL]
CITIES = []  # 07/11/2026 : retirées à la demande d'Anthony, MyCreativeSite vend dans toute la France
CITY_SLUG = {}

# Pages « intention » : ce que le pro tape dans Google (pas cher, rapide, clé en main, simple à modifier)
INTENT = [
  dict(slug="site-internet-diffusion-annonces-auto-immo", k="concession", style="luxe", pack=True, label="Site + annonces auto, moto, immo",
    title="Site internet et diffusion d'annonces auto, moto et immobilier",
    meta="Votre site professionnel et vos annonces de véhicules ou de biens diffusées en illimité sur Abracadeal, sans passerelle ni logiciel de multidiffusion à payer. 99 €/mois, sans engagement.",
    h1="Votre site et vos annonces au même endroit, mis à jour une seule fois",
    lead="Pour les garages, concessions auto et moto et agences immobilières : vous gérez votre stock dans votre espace, et votre site, vos pages Google et vos annonces sur Abracadeal suivent automatiquement.",
    feats=[("Une seule saisie","Vous remplissez la fiche d'un véhicule ou d'un bien une fois : site, page Google et annonce sont créés en même temps."),
           ("Annonces illimitées","Aucune limite de nombre d'annonces sur Abracadeal, aucun coût par annonce."),
           ("Retrait automatique","Vendu, loué, sous compromis : l'annonce disparaît d'Abracadeal dans les minutes qui suivent."),
           ("Une page Google par annonce","Titre, prix, photos et fiche technique sur une vraie page de votre site, avec les données structurées que Google sait lire."),
           ("Compte Abracadeal ouvert pour vous","Votre SIRET est demandé au paiement : votre espace professionnel Abracadeal est créé et relié à votre site, sans démarche."),
           ("CRM inclus","Toutes les demandes (site et annonces) sont suivies dans votre espace, client par client.")],
    faq=[("Que remplace cette offre ?","Un site vitrine et un logiciel ou une passerelle de multidiffusion : ici, les deux sont réunis dans un seul abonnement."),
         ("Mes annonces partent-elles sur d'autres sites que Abracadeal ?","Aujourd'hui la diffusion se fait sur Abracadeal. Votre site et vos pages Google restent par ailleurs visibles par tous."),
         ("Combien ça coûte ?","99 € par mois et 490 € de mise en ligne, une fois. Sans engagement : vous arrêtez quand vous voulez, vos annonces sont alors retirées."),
         ("Qui peut en profiter ?","Les garages et concessions auto et moto, et les agences immobilières. Pour les autres métiers, voyez nos formules Essentiel, Pro et Premium.")]),
  # 12/11/2026 (Anthony : « les gens cherchent avant d'ouvrir l'entreprise ») : pages pour les créateurs d'entreprise
  dict(slug="site-internet-creation-entreprise", k=None, label="Création d'entreprise",
    title="Site internet pour création d'entreprise",
    meta="Vous créez votre entreprise ? Votre site internet en ligne en 48 h, dès 29 €/mois, sans engagement : être trouvé sur Google dès le premier jour d'activité.",
    h1="Vous créez votre entreprise ? Ayez votre site dès le premier jour",
    lead="Les premiers clients vous cherchent sur Google avant même de vous appeler. Un site professionnel en ligne en 48 h, à votre nom, pour démarrer avec une vraie vitrine.",
    feats=[("Prêt pour l'ouverture","Commandez avant l'ouverture : votre site est prêt pour le jour où vous démarrez."),
           ("Petit budget de départ","Dès 29 € par mois et 190 € de mise en ligne, une seule fois. Pas d'investissement lourd au démarrage."),
           ("Sans engagement","Vous arrêtez quand vous voulez : rien ne vous bloque si votre projet évolue."),
           ("Votre nom de domaine","Votre adresse du type votre-entreprise.fr et votre adresse mail pro, à votre nom."),
           ("Mentions légales rédigées","Les informations obligatoires (SIREN, adresse, hébergeur) sont intégrées pour vous."),
           ("Vous le modifiez seul","Nouveaux tarifs, nouvelles photos, horaires : vous changez tout depuis votre téléphone.")],
    faq=[("Je n'ai pas encore mon SIRET, puis-je commander ?","Oui. On prépare le site avec vous, et vous ajoutez votre SIREN dans les mentions légales dès que vous l'avez reçu."),
         ("Combien coûte un site quand on démarre ?","Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois. Hébergement, nom de domaine et dépannages compris."),
         ("Un site est-il utile si je démarre petit ?","Oui : c'est souvent la première chose que regarde un client avant d'appeler. Un site à votre nom rassure et vous fait trouver sur Google.")]),
  dict(slug="site-internet-auto-entrepreneur", k=None, label="Auto-entrepreneur",
    title="Site internet pour auto-entrepreneur",
    meta="Site internet pour auto-entrepreneur et micro-entrepreneur : en ligne en 48 h, dès 29 €/mois sans engagement, mentions légales incluses, modifiable depuis votre téléphone.",
    h1="Le site internet de votre auto-entreprise, simple et pas cher",
    lead="Vous vous lancez en micro-entreprise ? Un vrai site professionnel à votre nom, en ligne en 48 h, pour le prix d'un abonnement de téléphone.",
    feats=[("Dès 29 € par mois","Un budget adapté à une auto-entreprise, sans devis à plusieurs milliers d'euros."),
           ("Mentions légales prêtes","Votre nom avec la mention « EI », votre SIREN, votre adresse, l'hébergeur : on les remplit avec vous."),
           ("Formulaire de contact et appel","Les demandes de vos clients arrivent par mail ; sur téléphone, un bouton pour vous appeler."),
           ("Devis en PDF","Créez vos devis à votre nom depuis l'espace client, et envoyez-les à vos clients."),
           ("Site pour votre métier","Coiffure à domicile, coach, photographe, artisan, VTC… un modèle déjà prévu pour votre activité."),
           ("Sans engagement","Vous résiliez quand vous voulez, votre nom de domaine reste à vous.")],
    faq=[("Un auto-entrepreneur est-il obligé d'avoir un site ?","Non, ce n'est pas obligatoire. Mais si vous en avez un, il doit afficher les mentions légales. Et c'est souvent ce qui fait la différence pour être trouvé et choisi."),
         ("Quelles mentions doivent figurer sur le site d'un micro-entrepreneur ?","Votre nom et prénom suivis de « EI », votre SIREN, votre adresse, un moyen de contact et l'hébergeur du site. Nous les intégrons pour vous."),
         ("Puis-je changer de formule si mon activité grandit ?","Oui, vous passez à la formule supérieure quand vous voulez, sans refaire le site.")]),
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
INTENT += INTENT_LOCAL

CSS = """.logo-mark{width:34px;height:34px;flex:none;display:block}
.logo .and,.logo i,.grad-t{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
:root{--grad:linear-gradient(90deg,#FF2D8E 0%,#8B3DFF 52%,#12A8FF 100%)}

:root{--bg:#FFFFFF;--paper:#FAF8FF;--ink:#12162B;--muted:#5C627A;--line:#E1E4EE;--brand:#7C3AED;--brand-ink:#FFFFFF;--soft:#E8EBFF}
/* 11/11/2026 (Anthony) : pages métier toujours en clair comme l'accueil, même si le téléphone est en mode sombre */
:root{color-scheme:light;--brand-soft:#F2EAFF;--pop:#FFB020;--device:#12162B}
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
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:10px;padding:11px 18px;font-size:.93rem;line-height:1.2;font-weight:700;text-decoration:none;background:var(--grad);color:#fff;border:0}
.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--line)}
.btn.sm{padding:8px 13px;font-size:.88rem}
.crumbs{font-size:.85rem;color:var(--muted);padding-block:18px 0}
.crumbs a{color:var(--muted)}
/* 11/11/2026 : entête et bannière alignées sur l'accueil (bouton compte + « Je veux mon site », modèle sur ordinateur et téléphone à droite) */
.nav{display:flex;align-items:center;gap:10px}
.nav .acc{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:.95rem;color:var(--ink);text-decoration:none;padding:8px 12px;border:1px solid var(--line);border-radius:10px}
.nav .acc:hover{border-color:var(--brand)}
.nav .acc svg{width:18px;height:18px}
.eyebrow{display:block;font-size:.75rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--brand)}
.hero{display:grid;grid-template-columns:1fr 1.1fr;gap:48px;align-items:center;padding-block:26px 48px}
.hero h1{font-size:clamp(1.75rem,3.6vw,2.7rem);font-weight:800;line-height:1.08;margin-top:12px}
.hero .lead{color:var(--muted);font-size:1rem;margin:16px 0 24px;max-width:50ch}
.ctas{display:flex;flex-wrap:wrap;gap:12px}
.args{display:grid;grid-template-columns:repeat(3,1fr);margin-top:28px;max-width:540px}
.args>div{display:grid;gap:4px;align-content:start;padding:0 14px;border-left:1px solid var(--line)}
.args>div:first-child{padding-left:0;border-left:0}
.args .ai{display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--brand-soft);color:var(--brand);margin-bottom:6px}
.args .ai svg{width:21px;height:21px}
.args b{font-size:.9rem;line-height:1.25}
.args span:not(.ai){font-size:.82rem;color:var(--muted);line-height:1.35}
.devices{position:relative;padding-bottom:28px;min-width:0}
.devices .laptop{width:80%}
.devices .base{margin:0 0 0 -3%;width:86%;height:12px;background:linear-gradient(#2A3050,#12162B);border-radius:0 0 12px 12px}
.laptop{background:var(--device);border-radius:14px 14px 4px 4px;padding:10px 10px 0;box-shadow:0 30px 60px -20px rgba(18,22,43,.35)}
.laptop .bar{display:flex;gap:5px;padding:0 2px 8px}
.laptop .bar i{width:7px;height:7px;border-radius:50%;background:#3A4060}
.screen{aspect-ratio:16/10;overflow:hidden;border-radius:4px 4px 0 0;background:#000}
.screen img,.pscreen img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.phone{position:absolute;right:0;bottom:0;width:24%;min-width:92px;background:var(--device);border-radius:22px;padding:7px;box-shadow:0 24px 40px -14px rgba(18,22,43,.45)}
.pscreen{aspect-ratio:9/19.5;overflow:hidden;border-radius:16px;background:#000}
.hs-cap{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:6px 0 0;font-weight:600;font-size:.95rem}
.hs-dot{width:9px;height:9px;border-radius:50%;background:var(--grad)}
.hs-cap a{margin-left:auto;font-weight:600;font-size:.88rem;color:var(--brand);text-decoration:none}
.hs-cap a:hover{text-decoration:underline}
@media (max-width:860px){.ctas .btn{flex:1 1 auto}.nav .acc span{display:none}.nav .acc{padding:8px}.nav .btn.sm{white-space:nowrap}.hero{gap:30px;padding-block:18px 36px}.hero .lead{font-size:.95rem;margin:12px 0 20px}}
@media (max-width:520px){.args>div{padding:0 10px}.args b{font-size:.84rem}.args span:not(.ai){font-size:.76rem}}
@media (max-width:480px){.nav .btn.sm{padding:8px 10px;font-size:.82rem}.nav{gap:6px}.logo span{font-size:1rem}.logo{gap:6px}.logo .logo-mark{width:28px;height:28px}}
.shot{border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 60px -30px rgba(18,22,43,.45);background:var(--paper)}
.shot img{display:block;width:100%;height:auto}
section{padding-block:48px}
.feats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:26px}
.feat{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:8px;align-content:start}
.feat p{color:var(--muted);font-size:.95rem}
.prices{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:24px}
.prices.one{grid-template-columns:minmax(0,420px)}
.prices.one .pc{align-content:start}
.pc.hi{border:2px solid var(--ink);box-shadow:0 10px 30px rgba(0,0,0,.08)}
.pc.hi em{font-style:normal;font-size:.8rem;font-weight:700;color:var(--ink)}
.pc{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:4px}
.pc b{font:800 2rem "Bricolage Grotesque",sans-serif}
.pc span{color:var(--muted);font-size:.9rem}
.note{color:var(--muted);font-size:.88rem;margin-top:12px}
.faq{display:grid;gap:10px;margin-top:22px;max-width:780px}
.faq details{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:14px 18px}
.faq summary{cursor:pointer;font-weight:700}
.faq details p{color:var(--muted);margin-top:8px}
.links{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.links a{border:1px solid var(--line);background:var(--paper);border-radius:8px;padding:5px 11px;text-decoration:none;font-size:.84rem;line-height:1.35;color:var(--muted)}.links a:hover{border-color:var(--brand);color:var(--ink)}
.cities{color:var(--muted);margin-top:14px;max-width:70ch}
.cta{background:var(--ink);color:var(--bg);border-radius:16px;padding:26px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:18px}
.cta p{opacity:.8;margin-top:6px}
.cta .btn{background:var(--bg);color:var(--ink)}
footer{border-top:1px solid var(--line);padding-block:26px;color:var(--muted);font-size:.9rem}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px}
footer nav{display:flex;flex-wrap:wrap;gap:16px}
@media (max-width:860px){.hero{grid-template-columns:1fr}.feats,.prices,.prices.one{grid-template-columns:1fr}}
"""
LOGO = '<img class="logo-mark" src="/img/logo-m.png" width="34" height="34" alt="">'
ICON_ACC = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><circle cx="10" cy="7" r="3.2" stroke="currentColor" stroke-width="1.7"/><path d="M3.8 16.6c1.1-2.9 3.4-4.3 6.2-4.3s5.1 1.4 6.2 4.3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
HEADER = (f'<div class="wrap"><a class="logo" href="/" aria-label="MyCreativeSite, accueil">{LOGO}<span>My<i>creativesite</i></span></a>'
          f'<nav class="nav"><a class="acc" href="/espace/" aria-label="Espace client : se connecter">{ICON_ACC}<span>Espace client</span></a>'
          '<a class="btn sm" href="/#commande">Je veux mon site</a></nav></div>')
ARGS = ('<div class="args">'
  '<div><span class="ai"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v6c0 4.2-3 7.6-7 9-4-1.4-7-4.8-7-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg></span><b>Sans engagement</b><span>Vous arrêtez quand vous voulez.</span></div>'
  '<div><span class="ai"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg></span><b>Domaine à votre nom</b><span>Hébergement et domaine inclus.</span></div>'
  '<div><span class="ai"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18h2"/></svg></span><b>Parfait sur mobile</b><span>Pensé d\'abord pour le téléphone.</span></div>'
  '</div>')
NAMES = {"vtc":"Chauffeur VTC","taxi":"Taxi","moto":"Concession moto","restaurant":"Restaurant","garage":"Garage auto et moto","concession":"Concession automobile","immobilier":"Agence immobilière","batiment":"Artisan du bâtiment","beaute":"Coiffeur et institut de beauté","bienetre":"Masseur et ostéopathe","veterinaire":"Vétérinaire","atelier":"Garage d'entretien","autoecole":"Auto-école","coach":"Coach sportif","photographe":"Photographe","toiletteur":"Toiletteur","fleuriste":"Fleuriste","traiteur":"Traiteur","nautisme":"Location de bateaux","kine":"Kinésithérapeute","dentiste":"Dentiste","bijouterie":"Bijouterie-horlogerie","liberal":"Professions libérales","services":"Services à domicile","evenementiel":"Événementiel","hebergement":"Chambres d'hôtes et gîtes","tourisme":"Tourisme et loisirs","location":"Location et déménagement","infirmier":"Infirmier libéral","boulangerie":"Boulangerie","depannage":"Plombier et électricien","boutique":"Boutique en ligne"}
e = html.escape

def trade_links(cur):
    out = [f'<a href="/{p["slug"]}/">{p.get("label") or NAMES[p["k"]]}</a>' for p in PAGES if p["slug"] != cur]
    out += [f'<a href="/{c["slug"]}/">Site internet à {c["city"]}</a>' for c in CITIES if c["slug"] != cur]
    out += [f'<a href="/{p["slug"]}/">{p["label"]}</a>' for p in INTENT if p["slug"] != cur]
    return "".join(out)

GUIDES = {"moto": "concession-auto-moto-vendre-plus-avec-son-site", "vtc": "site-internet-chauffeur-vtc-les-indispensables", "taxi": "site-internet-taxi-les-indispensables", "restaurant": "site-internet-restaurant-les-indispensables",
  "garage": "site-internet-garage-les-indispensables", "concession": "concession-auto-moto-vendre-plus-avec-son-site", "immobilier": "site-internet-agence-immobiliere-les-indispensables",
  "batiment": "site-internet-artisan-batiment-les-indispensables", "beaute": "site-internet-coiffeur-institut-beaute-les-indispensables",
  "bienetre": "site-internet-masseur-osteopathe-bien-etre-les-indispensables", "veterinaire": "site-internet-veterinaire-les-indispensables", "autoecole": "site-internet-auto-ecole-les-indispensables", "coach": "site-internet-coach-sportif-les-indispensables", "photographe": "site-internet-photographe-les-indispensables", "toiletteur": "site-internet-toiletteur-les-indispensables", "fleuriste": "site-internet-fleuriste-les-indispensables", "traiteur": "site-internet-traiteur-les-indispensables", "nautisme": "site-internet-location-bateau-les-indispensables", "kine": "site-internet-kinesitherapeute-les-indispensables", "dentiste": "site-internet-dentiste-les-indispensables", "bijouterie": "site-internet-bijouterie-horlogerie-les-indispensables", "liberal": "site-internet-profession-liberale-les-indispensables", "services": "site-internet-services-a-domicile-les-indispensables", "evenementiel": "site-internet-evenementiel-les-indispensables", "hebergement": "site-internet-chambres-d-hotes-gite-les-indispensables", "tourisme": "site-internet-tourisme-loisirs-les-indispensables", "location": "site-internet-location-demenagement-les-indispensables", "infirmier": "site-internet-infirmier-liberal-les-indispensables", "boulangerie": "site-internet-boulangerie-les-indispensables",
  "depannage": "site-internet-plombier-electricien-les-indispensables", "boutique": "creer-boutique-en-ligne-les-indispensables"}
def full_title(t):
    """12/11/2026 : Google coupe les titres vers 60 caractères ; le nom du site n'est ajouté que s'il tient."""
    return t if len(t) > 43 else t + " · MyCreativeSite"
AVANT = {"site-internet-vtc": "devenir-chauffeur-vtc-etapes", "site-internet-taxi": "devenir-chauffeur-de-taxi-etapes",
  "site-internet-restaurant": "ouvrir-un-restaurant-etapes", "site-internet-coiffeur-institut-beaute": "ouvrir-salon-de-coiffure-etapes",
  "site-internet-artisan-batiment": "s-installer-artisan-batiment-etapes", "site-internet-plombier-electricien": "s-installer-artisan-batiment-etapes",
  "site-internet-coach-sportif": "devenir-coach-sportif-independant", "site-internet-agence-immobiliere": "ouvrir-agence-immobiliere-etapes",
  "site-internet-chambres-d-hotes-gite": "ouvrir-chambre-d-hotes-etapes", "site-internet-garage-mecanique": "ouvrir-un-garage-automobile-etapes",
  "site-internet-garage": "ouvrir-un-garage-automobile-etapes", "site-internet-auto-ecole": "ouvrir-une-auto-ecole-etapes",
  "site-internet-boulangerie": "ouvrir-une-boulangerie-etapes", "site-internet-masseur-osteopathe-bien-etre": "devenir-praticien-massage-bien-etre",
  "site-internet-services-a-domicile": "creer-entreprise-services-a-la-personne", "site-internet-toiletteur": "ouvrir-salon-de-toilettage-etapes",
  "site-internet-fleuriste": "ouvrir-une-boutique-de-fleuriste", "site-internet-photographe": "devenir-photographe-independant",
  "site-internet-traiteur": "devenir-traiteur-etapes", "site-internet-creation-entreprise": "creer-son-entreprise-checklist",
  "site-internet-auto-entrepreneur": "auto-entrepreneur-site-internet"}
def guide(p):
    from articles import ARTICLES
    g = GUIDES.get(p.get("k"))
    g2 = AVANT.get(p.get("slug"))  # 12/11/2026 : guide « avant d'ouvrir » du métier
    parts = []
    if g:
        a = next(x for x in ARTICLES if x["slug"] == g)
        parts.append(f'À lire : <a href="/conseils/{g}/">{e(a["title"])}</a>')
    if g2:
        b = next((x for x in ARTICLES if x["slug"] == g2), None)
        if b: parts.append(f'{"Vous n\'avez pas encore ouvert ? " if g else "À lire : "}<a href="/conseils/{g2}/">{e(b["title"])}</a>')
    return f'<p style="margin-top:18px">{"<br>".join(parts)}</p>' if parts else ""

def why(p):
    w = p.get("why")
    if not w: return ""
    paras = "".join(f'<p style="margin:12px 0 0;color:var(--muted)">{e(x)}</p>' for x in w[1])
    return f'<section style="padding-bottom:0"><div class="wrap" style="max-width:860px"><h2>{e(w[0])}</h2>{paras}</div></section>\n'

PROSE_CSS = ".prose{padding-bottom:0}.prose .wrap{max-width:860px}.prose p{margin:12px 0 0;color:var(--muted)}.prose b{color:var(--ink)}"

def body(p):
    """Sections de texte enrichies (scripts/seo_contenu.py)."""
    out = ""
    for h, paras in p.get("body", []):
        out += f'<section class="prose"><div class="wrap"><h2>{e(h)}</h2>' + "".join(f"<p>{x}</p>" for x in paras) + '</div></section>\n'
    return out

def faq_html(p):
    if p.get("body"):  # pages enrichies : questions en H3, réponses visibles
        return "".join(f'<div class="feat"><h3>{e(q)}</h3><p>{e(a)}</p></div>' for q,a in p["faq"])
    return "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in p["faq"])

def devices(k, name, link):
    """Modèle affiché comme sur l'accueil : écran d'ordinateur + téléphone, légende et lien."""
    low = e(name.lower())
    return (f'<div><div class="devices" aria-label="Aperçu du modèle sur ordinateur et téléphone">'
            f'<div class="laptop"><div class="bar"><i></i><i></i><i></i></div><div class="screen"><img src="/img/modele-{k}-d.jpg?v=4" width="960" height="600" fetchpriority="high" alt="Modèle de site pour {low} sur ordinateur"></div></div>'
            f'<div class="base"></div>'
            f'<div class="phone"><div class="pscreen"><img src="/img/modele-{k}-m.jpg?v=4" alt="Modèle de site pour {low} sur téléphone"></div></div></div>'
            f'<p class="hs-cap"><span class="hs-dot"></span><span>{e(name)}</span>{link}</p></div>')

def page(p):
    from seo_contenu import SEO
    p = {**p, **SEO.get(p["slug"], {})}
    url = f'{SITE}/{p["slug"]}/'
    plans = [PACK] if p.get("pack") else [BOUTIQUE] if p.get("k") == "boutique" else PRICES
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    svc_ld = {"@context":"https://schema.org","@type":"Service","name":p["title"],"serviceType":"Création de site internet","url":url,
      "provider":{"@type":"ProfessionalService","name":"MyCreativeSite","url":SITE+"/","email":"contact@mycreativesite.fr"},
      "areaServed":({"@type":"City","name":p["city"]} if p.get("city") else "FR"),
      "offers":[{"@type":"Offer","name":n,"price":m,"priceCurrency":"EUR","description":f"{m} € par mois + {s} € de mise en ligne"} for n,m,s in plans]}
    crumbs_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":p["title"],"item":url}]}
    k = p["k"]
    if k:
        mk, dk = ("garage.html?concession=1", "garage&amp;concession=1") if k == "concession" else ("garage.html?atelier=1", "garage&amp;atelier=1") if k == "atelier" else ("vtc.html?taxi=1", "taxi") if k == "taxi" else ("garage.html?concession=1&amp;moto=1", "garage&amp;concession=1&amp;moto=1") if k == "moto" else (k + ".html", k)
        demo = f'<a class="btn ghost" href="/espace/?demo={dk}&amp;style={p["style"]}">Essayer l\'espace client</a>'
        visual = devices(k, p.get("label") or NAMES[k], f'<a href="/modeles/{mk}#{p["style"]}">Voir le modèle en vrai</a>')
    else:
        demo = '<a class="btn ghost" href="/espace/?demo=restaurant">Essayer l\'espace client</a>' if p["slug"] == "site-internet-facile-a-modifier" else '<a class="btn ghost" href="/#modeles">Voir les modèles</a>'
        visual = devices("vtc", "Chauffeur VTC, un des 31 métiers", '<a href="/#modeles">Voir tous les modèles</a>')
    eyebrow = "Pack Auto, Moto &amp; Immo · 99 €/mois" if p.get("pack") else (f'Modèle {e(p.get("eyebrow_name") or NAMES[k].lower())} · en ligne en 48 h' if k else "Sites pros clés en main · 31 métiers")
    feats = "".join(f'<div class="feat"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t,d in p["feats"])
    prices = "".join(f'<div class="pc"><span>{n}</span><b>{m} €</b><span>par mois · + {s} € de mise en ligne</span></div>' for n,m,s in plans)
    if p.get("pack"):
        prices = (f'<div class="pc hi"><em>La formule de votre métier</em><span>{PACK[0]}</span><b>{PACK[1]} €</b><span>par mois · + {PACK[2]} € de mise en ligne</span>'
                  '<span>Tout Pro, annonces illimitées sur Abracadeal, CRM, une page Google par véhicule ou par bien</span></div>')
    elif p.get("k") == "boutique":
        prices = (f'<div class="pc hi"><em>La formule de votre métier</em><span>{BOUTIQUE[0]}</span><b>{BOUTIQUE[1]} €</b><span>par mois · + {BOUTIQUE[2]} € de mise en ligne</span>'
                  '<span>Tout Premium, catalogue, panier et paiement par carte, retrait ou livraison</span></div>')
    faq = faq_html(p)
    def _cl(c):
        sl = CITY_SLUG.get(c)
        return f'<a href="/{sl}/">{e(c)}</a>' if sl and sl != p["slug"] else e(c)
    cities = f'<p class="cities">{"Communes desservies" if p.get("city") else "Villes"} : {", ".join(_cl(c) for c in p["cities"])}.</p>' if p.get("cities") else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="color-scheme" content="light">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title(p.get("seo_title") or p["title"]))}</title>
<meta name="description" content="{e(p["meta"])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p.get("seo_title") or p["title"])} · MyCreativeSite">
<meta property="og:description" content="{e(p["meta"])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{SITE + ("/img/modele-" + p["k"] + "-d.jpg" if p.get("k") else "/img/og.jpg")}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png"><link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96.png"><link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192.png"><link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png?v=2"><meta name="apple-mobile-web-app-title" content="MyCreativeSite">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
<script type="application/ld+json">{json.dumps(svc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs_ld, ensure_ascii=False)}</script>
<style>{CSS}{PROSE_CSS if p.get("body") else ""}</style>
</head>
<body>
<header class="top">{HEADER}</header>
<main>
<div class="wrap crumbs"><a href="/">Accueil</a> › {e(p["title"])}</div>
<div class="wrap hero">
  <div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{e(p["h1"])}</h1>
    <p class="lead">{e(p["lead"])}</p>
    <div class="ctas"><a class="btn" href="/#commande">Je veux mon site</a>{demo}</div>
    {ARGS}
  </div>
  {visual}
</div>
{why(p)}{body(p)}<section><div class="wrap">
  <h2>Ce que votre site fait pour vous</h2>
  <div class="feats">{feats}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2>Des prix clairs, sans engagement</h2>
  <div class="prices{' one' if len(plans) == 1 else ''}">{prices}</div>
  <p class="note">TVA non applicable, art. 293 B du CGI. Hébergement, nom de domaine, version mobile, espace client, maintenance et réparations à distance inclus. <a href="/#tarifs">Détail des formules</a>{' · <a href="/#auto-immo">Pack Auto, Moto &amp; Immo</a>' if p.get('pack') else ''} · <a href="/cgv.html">Conditions générales</a></p>
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
<footer><div class="wrap"><span style="display:inline-flex;align-items:center;gap:8px"><img src="/img/m-badge.webp" alt="" width="20" height="20" style="width:20px;height:20px">© 2026 MyCreativeSite</span><nav><a href="/">Accueil</a><a href="/conseils/">Conseils</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV</a><span style="user-select:all">contact@mycreativesite.fr</span></nav></div></footer>
<script src="/assets/cs-visits.js?v=4" defer></script>
</body>
</html>
'''

CTA_LINK = {"Voir le modèle garage d'entretien": "/site-internet-garage-mecanique/", "Voir le modèle auto-école": "/site-internet-auto-ecole/", "Voir le modèle boulangerie": "/site-internet-boulangerie/", "Voir le modèle bien-être": "/site-internet-masseur-osteopathe-bien-etre/", "Voir le modèle services à domicile": "/site-internet-services-a-domicile/", "Voir le modèle toiletteur": "/site-internet-toiletteur/", "Voir le modèle fleuriste": "/site-internet-fleuriste/", "Voir le modèle photographe": "/site-internet-photographe/", "Voir le modèle traiteur": "/site-internet-traiteur/", "Voir le modèle agence immobilière": "/site-internet-agence-immobiliere/", "Voir le modèle institut de beauté": "/site-internet-coiffeur-institut-beaute/", "Voir le modèle chambres d'hôtes": "/site-internet-chambres-d-hotes-gite/", "Voir le modèle coach sportif": "/site-internet-coach-sportif/", "Voir le modèle restaurant": "/site-internet-restaurant/", "Voir le modèle coiffure": "/site-internet-coiffeur-institut-beaute/", "Voir le modèle artisan du bâtiment": "/site-internet-artisan-batiment/", "Voir le modèle VTC": "/site-internet-vtc/", "Votre site pour votre création d'entreprise": "/site-internet-creation-entreprise/", "Le site de votre auto-entreprise": "/site-internet-auto-entrepreneur/", "Voir le modèle taxi": "/site-internet-taxi/", "Voir le modèle garage d'entretien": "/site-internet-garage-mecanique/", "Voir le modèle auto-école": "/site-internet-auto-ecole/", "Voir le modèle coach sportif": "/site-internet-coach-sportif/", "Voir le modèle photographe": "/site-internet-photographe/", "Voir le modèle toiletteur": "/site-internet-toiletteur/", "Voir le modèle fleuriste": "/site-internet-fleuriste/", "Voir le modèle traiteur": "/site-internet-traiteur/", "Voir le modèle location de bateaux": "/site-internet-location-bateau/", "Voir le modèle kinésithérapeute": "/site-internet-kinesitherapeute/", "Voir le modèle dentiste": "/site-internet-dentiste/", "Voir le modèle bijouterie-horlogerie": "/site-internet-bijouterie/", "Voir le modèle profession libérale": "/site-internet-profession-liberale/", "Voir le modèle services à domicile": "/site-internet-services-a-domicile/", "Voir le modèle événementiel": "/site-internet-evenementiel/", "Voir le modèle chambres d'hôtes": "/site-internet-chambres-d-hotes-gite/", "Voir le modèle tourisme et loisirs": "/site-internet-tourisme-loisirs/", "Voir le modèle location et déménagement": "/site-internet-location-demenagement/", "Voir le modèle infirmier libéral": "/site-internet-infirmier-liberal/", "Voir le modèle vétérinaire": "/site-internet-veterinaire/", "Voir le modèle restaurant": "/site-internet-restaurant/", "Voir le modèle VTC": "/site-internet-vtc/", "Voir le modèle garage": "/site-internet-garage/", "Voir le modèle concession": "/site-internet-concession-automobile/", "Voir le Pack Auto, Moto & Immo": "/site-internet-diffusion-annonces-auto-immo/", "Voir le modèle immobilier": "/site-internet-agence-immobiliere/", "Voir le modèle bâtiment": "/site-internet-artisan-batiment/", "Voir le modèle beauté": "/site-internet-coiffeur-institut-beaute/", "Voir le modèle bien-être": "/site-internet-masseur-osteopathe-bien-etre/", "Voir le modèle boulangerie": "/site-internet-boulangerie/", "Voir le modèle dépannage": "/site-internet-plombier-electricien/", "Voir la formule Boutique": "/site-internet-boutique-en-ligne/", "Découvrir les modèles par métier": "/#modeles", "Lancer mon site": "/#commande", "Un site pensé pour Google, en ligne en 48 h": "/site-internet-rapide/"}
ARTICLE_CSS = """
.art{max-width:740px;padding-block:10px 40px}
.art h1{margin:6px 0 14px}
.art .date{color:var(--muted);font-size:.9rem}
.art p{margin:14px 0;font-size:1.05rem}
.art h2{margin:34px 0 6px;font-size:1.45rem}
.art ul{margin:12px 0;padding-left:22px;font-size:1.03rem}
.art li{margin:8px 0}
/* 11/11/2026 (Anthony) : boutons et liens plus fins, plus pros */
.art .box .btn{padding:7px 14px;font-size:.85rem}
.art .box{margin:28px 0 8px;background:var(--paper);border:1px solid var(--line);border-left:3px solid var(--brand);border-radius:10px;padding:12px 14px 12px 16px;font-size:.95rem;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px}
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
<meta name="color-scheme" content="light">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title(title))}</title>
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
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap">
{lds}
<style>{CSS}{ARTICLE_CSS}</style>
</head>
<body>
<header class="top">{HEADER}</header>
<main>{body}</main>
<footer><div class="wrap"><span style="display:inline-flex;align-items:center;gap:8px"><img src="/img/m-badge.webp" alt="" width="20" height="20" style="width:20px;height:20px">© 2026 MyCreativeSite</span><nav><a href="/">Accueil</a><a href="/conseils/">Conseils</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV</a><span style="user-select:all">contact@mycreativesite.fr</span></nav></div></footer>
<script src="/assets/cs-visits.js?v=4" defer></script>
</body>
</html>
'''

def render_block(b):
    t, v = b
    if t == "p": return f"<p>{v}</p>"
    if t == "h2": return f"<h2>{e(v)}</h2>"
    if t == "ul": return "<ul>" + "".join(f"<li>{x}</li>" for x in v) + "</ul>"
    if t == "faq": return '<h2>Questions fréquentes</h2><div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(r)}</p></details>" for q, r in v) + "</div>"
    if t == "cta": return f'<div class="box"><b>{e(v)}</b><a class="btn" href="{CTA_LINK.get(v, "/#tarifs")}">Voir</a></div>'
    return ""

def build_blog():
    from articles import ARTICLES
    os.makedirs("conseils", exist_ok=True)
    for a in ARTICLES:
        url = f"{SITE}/conseils/{a['slug']}/"
        others = "".join(f'<a href="/conseils/{o["slug"]}/">{e(o["title"])}</a>' for o in ARTICLES if o is not a)
        body = f'''<div class="wrap crumbs"><a href="/">Accueil</a> › <a href="/conseils/">Conseils</a></div>
<article class="wrap art"><h1>{e(a["title"])}</h1><p class="date">Publié le {datetime.date.fromisoformat(a["date"]).strftime("%d/%m/%Y")}{(" · mis à jour le " + datetime.date.fromisoformat(a["updated"]).strftime("%d/%m/%Y")) if a.get("updated") else ""} · MyCreativeSite</p>
{"".join(render_block(b) for b in a["body"])}
<h2>À lire aussi</h2><div class="links">{others}</div></article>'''
        ld = [{"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["desc"],"datePublished":a["date"],"dateModified":a.get("updated",a["date"]),
               "inLanguage":"fr-FR","mainEntityOfPage":url,"image":SITE+"/img/og.jpg",
               "author":{"@type":"Organization","name":"MyCreativeSite","url":SITE+"/"},"publisher":{"@type":"Organization","name":"MyCreativeSite","url":SITE+"/"}},
              {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
               {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Conseils","item":SITE+"/conseils/"},
               {"@type":"ListItem","position":3,"name":a["title"],"item":url}]}]
        fq = [x for b in a["body"] if b[0] == "faq" for x in b[1]]
        if fq: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":r}} for q, r in fq]})
        os.makedirs(f"conseils/{a['slug']}", exist_ok=True)
        open(f"conseils/{a['slug']}/index.html","w").write(shell(a["title"], a["desc"], url, ld, body, "article"))
    cards = "".join(f'<a class="card" href="/conseils/{a["slug"]}/"><h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p></a>' for a in ARTICLES)
    body = f'<div class="wrap crumbs"><a href="/">Accueil</a> › Conseils</div><div class="wrap" style="padding-block:10px 50px"><h1>Conseils pour le site internet de votre entreprise</h1><p class="lead" style="color:var(--muted);margin-top:12px;max-width:60ch">Prix, visibilité sur Google, obligations légales, nom de domaine : des réponses claires pour les artisans, commerçants et indépendants.</p><div class="list">{cards}</div></div>'
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Conseils MyCreativeSite","url":SITE+"/conseils/","inLanguage":"fr-FR"}]
    open("conseils/index.html","w").write(shell("Conseils pour le site internet de votre entreprise","Guides pratiques pour les professionnels : prix d'un site internet, visibilité sur Google, mentions légales, nom de domaine.",SITE+"/conseils/",ld,body))
    return ["conseils/"] + [f"conseils/{a['slug']}/" for a in ARTICLES]

def build_help():
    """Page d'aide : relier un nom de domaine (chez OVH, IONOS, GoDaddy, Gandi…) à son site MyCreativeSite."""
    url = SITE + "/aide/nom-de-domaine/"
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td><code>{c}</code></td></tr>' for a,b,c in [
        ("A", "@ ou vide", "185.199.108.153"), ("A", "@ ou vide", "185.199.109.153"),
        ("A", "@ ou vide", "185.199.110.153"), ("A", "@ ou vide", "185.199.111.153"),
        ("CNAME", "www", "clicandsite.github.io.")])
    regs = [
        ("OVHcloud", "Web Cloud › Noms de domaine › votre domaine › onglet « Zone DNS » › « Ajouter une entrée ». Supprimez d'abord les anciennes entrées A de la racine et l'entrée www si elles existent."),
        ("IONOS", "Domaines &amp; SSL › votre domaine › « DNS » › « Ajouter un enregistrement ». Si IONOS propose de « relier à un produit IONOS », refusez : choisissez l'ajout manuel."),
        ("GoDaddy", "Mes produits › Domaines › « DNS » › « Ajouter un nouvel enregistrement ». Remplacez l'enregistrement A « Parked » s'il existe."),
        ("Gandi", "Noms de domaine › votre domaine › « Enregistrements DNS » › « Ajouter un enregistrement »."),
        ("Google / Squarespace Domains, Namecheap, Hostinger…", "Cherchez « DNS » ou « Gérer les enregistrements » dans la fiche de votre domaine : les valeurs à saisir sont toujours les mêmes.")]
    regs_html = "".join(f'<h3 style="margin-top:18px">{a}</h3><p>{b}</p>' for a,b in regs)
    body = f"""<div class="wrap crumbs"><a href="/">Accueil</a> › Aide › Relier votre nom de domaine</div>
<article class="wrap art">
<h1>Relier votre nom de domaine à votre site MyCreativeSite</h1>
<p>Vous avez déjà un nom de domaine (par exemple <b>votre-garage.fr</b>) acheté chez OVH, IONOS, GoDaddy ou ailleurs ? Vous le gardez, chez vous. Il suffit d'ajouter quelques lignes dans sa « zone DNS » pour qu'il affiche votre nouveau site. Comptez 5 minutes, puis jusqu'à 24 heures pour que tout soit pris en compte.</p>
<h2>Les lignes à ajouter</h2>
<p>Dans la zone DNS de votre domaine, ajoutez ces 5 enregistrements (et supprimez les anciens enregistrements A ou www qui pointent ailleurs) :</p>
<div style="overflow-x:auto"><table style="border-collapse:collapse;width:100%;margin:14px 0;font-size:.98rem" border="1" cellpadding="8"><thead><tr><th>Type</th><th>Nom / sous-domaine</th><th>Valeur / cible</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Vous préférez garder votre site actuel et mettre MyCreativeSite sur un sous-domaine (par exemple <b>annonces.votre-garage.fr</b>) ? Ajoutez seulement un enregistrement <b>CNAME</b> avec le nom <code>annonces</code> et la cible <code>clicandsite.github.io.</code></p>
<h2>Où cliquer chez votre fournisseur</h2>
{regs_html}
<h2>Et ensuite ?</h2>
<ul><li>Envoyez-nous un mail à <b>contact@mycreativesite.fr</b> quand c'est fait : nous vérifions et activons le cadenas HTTPS (gratuit, automatique).</li>
<li>Vos adresses e-mail sur ce domaine ne sont pas touchées : ne modifiez pas les lignes <b>MX</b>.</li>
<li>Vous ne trouvez pas ? Donnez-nous un accès « technique » à votre espace, ou appelez votre fournisseur : la demande « ajouter des enregistrements A et CNAME » est classique.</li></ul>
<div class="box"><div><b>Vous n'avez pas encore de nom de domaine ?</b><br>Nous le réservons pour vous, il est inclus dans toutes les formules.</div><a class="btn" href="/#commande">Je veux mon site</a></div>
</article>"""
    ld = [{"@context":"https://schema.org","@type":"HowTo","name":"Relier son nom de domaine à son site MyCreativeSite","inLanguage":"fr-FR",
           "step":[{"@type":"HowToStep","text":"Ouvrir la zone DNS du nom de domaine chez son fournisseur."},
                   {"@type":"HowToStep","text":"Ajouter quatre enregistrements A vers 185.199.108.153, 185.199.109.153, 185.199.110.153 et 185.199.111.153."},
                   {"@type":"HowToStep","text":"Ajouter un enregistrement CNAME www vers clicandsite.github.io."},
                   {"@type":"HowToStep","text":"Prévenir MyCreativeSite, qui active le HTTPS."}]}]
    os.makedirs("aide/nom-de-domaine", exist_ok=True)
    open("aide/nom-de-domaine/index.html", "w").write(shell("Relier votre nom de domaine à votre site", "Votre nom de domaine est chez OVH, IONOS, GoDaddy ou Gandi ? Les enregistrements DNS à ajouter pour le relier à votre site MyCreativeSite, pas à pas.", url, ld, body, "article"))
    return ["aide/nom-de-domaine/"]


# 13/11/2026 (Anthony) : offre « Landing Page » — 490 € HT, paiement unique (Stripe), même prix pour tous
LANDING_PAY = "https://buy.stripe.com/14AeVd9WLeD19eFfwIgfu0c"
def landing_pages():
    url = SITE + "/landing-page/"
    inc = [("Textes sur mesure", "Écrits pour votre offre et pour la personne qui clique sur votre pub : un message, une promesse, une action."),
           ("Design orienté conversion, mobile d'abord", "La plupart des clics de pub viennent du téléphone : la page est pensée pour lui, sans menu qui disperse."),
           ("Tracking complet", "Google Ads, Meta (Facebook, Instagram), clics sur « Appeler » et WhatsApp : vous savez ce que chaque euro de pub rapporte."),
           ("Formulaire ou prise de rendez-vous", "Le visiteur demande un devis ou réserve un créneau sans quitter la page. Les demandes arrivent chez vous tout de suite."),
           ("Optimisation de la vitesse", "Une page qui s'affiche en moins de 2 secondes : chaque seconde de plus fait partir des visiteurs que vous avez payés."),
           ("Suivi et ajustements pendant 30 jours", "On regarde les chiffres avec vous et on ajuste les textes, l'ordre ou le bouton si la page ne convertit pas assez."),
           ("Livraison en 5 jours", "Votre page est en ligne en 5 jours ouvrés après votre brief, prête à recevoir vos campagnes."),
           ("Hébergement inclus", "Sur votre nom de domaine, sans frais tant que la page est en ligne. Ou sur votre propre hébergement si vous préférez, au même prix.")]
    who = [("Vous lancez une publicité", "Google Ads, Facebook ou Instagram : envoyez vos clics vers une page faite pour ça, pas vers votre accueil."),
           ("Vous testez une nouvelle offre", "Un nouveau service, une promo, une saison : une page dédiée pour mesurer si l'offre prend avant d'investir plus."),
           ("Votre page actuelle ne convertit pas", "Des visites mais peu d'appels ou de demandes ? On repart de zéro avec une page construite pour l'action.")]
    steps = [("Vous réglez en ligne", "Paiement unique et sécurisé, facture envoyée par e-mail."),
             ("Vous remplissez un court brief", "Votre offre, votre publicité, ce que doit faire le visiteur. Cinq minutes."),
             ("On crée votre page en 5 jours", "Textes, design, formulaire et tracking installés, hébergée par nos soins sur votre domaine, ou sur votre propre hébergement."),
             ("On l'améliore pendant 30 jours", "Suivi des résultats et ajustements inclus.")]
    faq = [("Pourquoi ne pas envoyer ma pub sur ma page d'accueil ?", "Une page d'accueil parle de tout : vos services, votre histoire, vos horaires. Le visiteur qui arrive d'une pub cherche une seule chose. Une landing page lui répond directement et lui donne un seul bouton, ce qui fait en général beaucoup plus d'appels ou de demandes pour le même budget de pub."),
           ("Le prix est-il le même pour tout le monde ?", "Oui : 490 € HT, paiement unique, quel que soit votre métier. TVA non applicable (art. 293 B du CGI) : vous payez 490 €."),
           ("Faut-il avoir un site MyCreativeSite ?", "Non. La landing page fonctionne seule. Si vous avez déjà un site chez nous ou ailleurs, elle peut se mettre sur votre propre nom de domaine."),
           ("Qui gère mes publicités ?", "Vous, ou la personne qui s'en occupe. Nous créons la page et installons le suivi (Google Ads, Meta, clics appel et WhatsApp) pour que vos campagnes mesurent les bons résultats."),
           ("Y a-t-il un abonnement ?", "Non, c'est un paiement unique de 490 € HT. L'hébergement est inclus, sans frais, tant que la page est en ligne."),
           ("Où la page est-elle hébergée ?", "Par défaut, nous l'hébergeons pour vous, sans frais, sur votre nom de domaine (par exemple promo.votre-site.fr), avec le cadenas HTTPS. Vous préférez votre propre hébergement (OVH, IONOS, o2switch, WordPress…) ? Nous l'y installons avec vos accès, ou nous vous remettons les fichiers, au même prix. Les ajustements des 30 jours se font alors avec vos accès."),
           ("Que se passe-t-il après les 30 jours ?", "La page reste à vous et continue de fonctionner. Si vous voulez d'autres changements plus tard, on vous fait un devis simple.")]
    feat = lambda t: "".join(f'<div class="feat"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in t)
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{e(r)}</p></details>" for q, r in faq)
    body = f"""
<div class="wrap crumbs"><a href="/">Accueil</a> › Landing Page</div>
<div class="wrap" style="padding-block:20px 40px;max-width:900px">
  <span class="eyebrow">Service en plus · Landing Page</span>
  <h1 style="font-size:clamp(1.8rem,4vw,2.9rem);font-weight:800;line-height:1.08;margin-top:12px">Vous faites de la pub Google ou Facebook ? Ne l'envoyez pas sur votre page d'accueil.</h1>
  <p class="lead" style="color:var(--muted);font-size:1.05rem;margin:16px 0 24px;max-width:62ch">Une page faite pour une seule chose : transformer les clics que vous payez en appels, en demandes de devis et en rendez-vous. Textes, design, formulaire et suivi des résultats compris.</p>
  <div class="ctas"><a class="btn" href="{LANDING_PAY}" data-cs-landing>Commander ma landing page · 490 € HT</a><a class="btn ghost" href="#inclus">Ce qui est inclus</a></div>
  <p class="note">Paiement unique, même prix pour tous. TVA non applicable (art. 293 B du CGI) : vous payez 490 €. Livrée en 5 jours.</p>
</div>
<section id="inclus"><div class="wrap">
  <span class="eyebrow">Inclus</span><h2>Tout ce qu'il faut pour que votre pub rapporte</h2>
  <div class="feats">{feat(inc)}</div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Pour qui</span><h2>Pour les pros qui veulent des résultats de leur pub</h2>
  <div class="feats">{feat(who)}</div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Comment ça se passe</span><h2>De la commande à la mise en ligne</h2>
  <div class="feats" style="grid-template-columns:repeat(4,minmax(0,1fr))">{"".join(f'<div class="feat"><span class="eyebrow">Étape {i+1}</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i,(a,b) in enumerate(steps))}</div>
</div></section>
<section><div class="wrap">
  <div class="prices one"><div class="pc hi"><em>Landing Page</em><b>490 € HT</b><span>Paiement unique, même prix pour tous. TVA non applicable, art. 293 B du CGI : vous payez 490 €.</span>
    <a class="btn" href="{LANDING_PAY}" data-cs-landing style="margin-top:14px">Commander ma landing page</a></div></div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Questions fréquentes</span><h2>Vos questions sur la landing page</h2>
  <div class="faq">{faq_html}</div>
</div></section>
<section><div class="wrap">
  <div class="cta"><div><h2>Vos clics méritent mieux que votre page d'accueil</h2><p>490 € HT, livrée en 5 jours, suivie pendant 30 jours.</p></div><a class="btn" href="{LANDING_PAY}" data-cs-landing>Commander</a></div>
  <p class="note">Besoin d'un site complet plutôt qu'une page ? <a href="/#tarifs">Voir les formules MyCreativeSite</a>. <a href="/cgv.html">Conditions générales</a>.</p>
</div></section>
<style>@media (max-width:860px){{.feats[style]{{grid-template-columns:minmax(0,1fr)!important}}}}</style>
<script>document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('[data-cs-landing]');if(a&&window.csTrack)window.csTrack('landing-paiement');}},true);</script>
"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": "Landing Page pour publicité Google Ads et Facebook", "serviceType": "Création de landing page",
           "provider": {"@id": SITE + "/#org"}, "areaServed": "FR", "url": url,
           "offers": {"@type": "Offer", "price": "490", "priceCurrency": "EUR", "url": LANDING_PAY, "availability": "https://schema.org/InStock"}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in faq]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Landing Page", "item": url}]}]
    os.makedirs("landing-page/merci", exist_ok=True)
    open("landing-page/index.html", "w").write(shell("Landing page pour vos pubs Google et Facebook : 490 €", "Une landing page qui transforme vos clics de pub en appels et demandes : textes sur mesure, design mobile, tracking Google Ads et Meta, formulaire, suivi 30 jours. 490 € HT, livrée en 5 jours.", url, ld, body))
    merci = f"""
<div class="wrap" style="padding-block:28px 56px;max-width:720px">
  <span class="eyebrow">Paiement reçu</span>
  <h1 style="font-size:clamp(1.7rem,3.6vw,2.4rem);font-weight:800;line-height:1.1;margin-top:12px">Merci ! Parlez-nous de votre offre.</h1>
  <p class="lead" style="color:var(--muted);margin:14px 0 22px">Cinq minutes pour nous dire quoi mettre en avant. Votre page est en ligne 5 jours ouvrés après ce brief. Votre facture arrive par e-mail.</p>
  <form id="lb" class="feat" style="gap:14px" novalidate>
    <input type="text" name="hp" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
    <label>Nom de votre entreprise<input name="company" required autocomplete="organization"></label>
    <label>E-mail<input name="email" type="email" required autocomplete="email"></label>
    <label>Téléphone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>L'offre à mettre en avant<textarea name="offer" rows="3" required placeholder="Ex. : rénovation de salle de bain clé en main dès 6 900 €, à Nice et alentours"></textarea></label>
    <label>Votre publicité<select name="ads"><option>Google Ads</option><option>Facebook / Instagram</option><option>Google et Facebook</option><option>Pas encore lancée</option><option>Autre</option></select></label>
    <label>Ce que doit faire le visiteur<select name="goal"><option>Demander un devis</option><option>Prendre rendez-vous</option><option>Appeler</option><option>Écrire sur WhatsApp</option><option>Autre</option></select></label>
    <label>Votre site actuel (si vous en avez un)<input name="url" type="url" placeholder="https://"></label>
    <label>Précisions (facultatif)<textarea name="msg" rows="3" placeholder="Couleurs, logo, photos, zone d'intervention, ce que font vos concurrents…"></textarea></label>
    <button class="btn" type="submit">Envoyer mon brief</button>
    <p class="note" id="lbm" role="status"></p>
  </form>
  <p class="note">Une question ? <a href="mailto:contact@mycreativesite.fr">contact@mycreativesite.fr</a></p>
</div>
<style>#lb label{{display:grid;gap:6px;font-weight:600;font-size:.95rem}}#lb input,#lb textarea,#lb select{{font:inherit;font-weight:400;padding:11px 12px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);width:100%;box-sizing:border-box}}</style>
<script>
(function(){{var f=document.getElementById('lb'),m=document.getElementById('lbm'),s=new URLSearchParams(location.search).get('s')||'';
f.addEventListener('submit',function(e){{e.preventDefault();if(!f.reportValidity())return;var d=new FormData(f),b=f.querySelector('button');b.disabled=true;m.textContent='Envoi…';
fetch('https://avcynjwcyygygkjuxsdt.supabase.co/rest/v1/rpc/cs_landing_brief',{{method:'POST',headers:{{'Content-Type':'application/json',apikey:'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO'}},
body:JSON.stringify({{p_company:d.get('company'),p_email:d.get('email'),p_phone:d.get('phone'),p_url:d.get('url'),p_offer:d.get('offer'),p_ads:d.get('ads'),p_goal:d.get('goal'),p_message:d.get('msg'),p_session:s,p_hp:d.get('hp')}})}})
.then(function(r){{return r.json().then(function(j){{if(!r.ok)throw new Error(j.message||'Erreur');return j;}});}})
.then(function(){{f.innerHTML='<h2>Brief bien reçu, merci !</h2><p>On vous recontacte sous 24 h ouvrées pour lancer votre page.</p>';if(window.csTrack)window.csTrack('landing-brief');}})
.catch(function(x){{b.disabled=false;m.textContent=x.message||'Envoi impossible, réessayez ou écrivez-nous.';}});}});}})();
</script>
"""
    open("landing-page/merci/index.html", "w").write(shell("Merci : votre brief de landing page", "Brief de votre landing page MyCreativeSite.", url + "merci/", [], merci).replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1))

def main():
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for p in PAGES + CITIES + INTENT:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w").write(page(p))
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    blog = build_blog()
    aide = build_help()
    landing_pages()
    urls = [("", "1.0"), ("landing-page/", "0.8")] + [(p["slug"] + "/", "0.8") for p in PAGES + CITIES + INTENT] + [(u, "0.6") for u in blog] + [(u, "0.4") for u in aide] + [("cgv.html", "0.3")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    from articles import ARTICLES
    adate = {f"conseils/{a['slug']}/": a["date"] for a in ARTICLES}
    sm += [f'  <url><loc>{SITE}/{u}</loc><lastmod>{adate.get(u, TODAY)}</lastmod><priority>{pr}</priority></url>' for u, pr in urls]
    sm.append("</urlset>")
    open("sitemap.xml", "w").write("\n".join(sm) + "\n")
    links = "".join(f'<a class="card" href="/{p["slug"]}/"><h3>{p.get("label") or NAMES[p["k"]]}</h3></a>' for p in PAGES)
    body404 = f'<div class="wrap" style="padding-block:40px 60px"><h1>Page introuvable</h1><p class="lead" style="color:var(--muted);margin-top:12px">Cette page n\'existe pas ou a été déplacée. Voici nos modèles de site par métier :</p><div class="list">{links}</div><p style="margin-top:24px"><a class="btn" href="/">Retour à l\'accueil</a></p></div>'
    open("404.html", "w").write(shell("Page introuvable", "Cette page n'existe pas.", SITE + "/404.html", [], body404).replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1))
    print("pages :", len(PAGES) + len(CITIES) + len(INTENT), "· sitemap :", len(urls), "adresses")

if __name__ == "__main__":
    main()
