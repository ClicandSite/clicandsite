# -*- coding: utf-8 -*-
"""Contenus SEO enrichis, page par page (passes SEO automatiques, voir scripts/SEO_PLAN.md).
Chaque entrée remplace, pour la page du même slug dans build_seo.py : titre de l'onglet (seo_title),
meta description, H1, accroche, FAQ, et ajoute des sections de texte (body = [(H2, [paragraphes HTML])]).
Règles : uniquement les faits de scripts/BRIEF_CONTENU_SEO.md, prix identiques à ceux du site,
aucun texte recopié d'une page à l'autre, liens internes vers des pages qui existent."""

SEO = {

# ---------------------------------------------------------------- Pack Auto, Moto & Immo
"site-internet-diffusion-annonces-auto-immo": dict(
  seo_title="Site + diffusion d'annonces auto, moto et immo",
  meta="Site pro et diffusion d'annonces auto, moto ou immobilier en illimité sur Abracadeal, sans passerelle à payer. 99 €/mois, sans engagement.",
  h1="Site internet et diffusion d'annonces auto, moto et immobilier",
  lead="Garages qui vendent des véhicules, concessions auto et moto, agences immobilières : le Pack Auto, Moto & Immo réunit votre site professionnel et la diffusion illimitée de vos annonces sur Abracadeal. Vous saisissez un véhicule ou un bien une seule fois, le site, sa page Google et l'annonce suivent.",
  body=[
    ("Pourquoi réunir site et annonces dans un même outil ?", [
      "Quand un véhicule est vendu ou qu'un bien passe sous compromis, il faut d'habitude le retirer à plusieurs endroits : sur le site, sur les sites d'annonces, parfois dans un logiciel de diffusion payé à part. Chaque oubli fait sonner le téléphone pour rien et agace l'acheteur.",
      "Avec le Pack, votre stock vit dans votre espace client. Prix, photos, statut « vendu » : vous changez l'information à un seul endroit et votre site comme vos annonces Abracadeal sont synchronisés. Aucune passerelle ni logiciel de diffusion n'est à payer en plus.",
    ]),
    ("Ce que contient votre site", [
      "Votre site reprend le modèle de votre métier, au style que vous choisissez. Vos véhicules ou vos biens y sont présentés en vitrine, avec photos et fiches détaillées. Chaque annonce a sa propre page, avec un titre, un prix, des photos et une fiche technique, lisible par Google et facile à partager par message.",
      "Le Pack comprend tout ce que contient la formule Pro : espace client, devis en PDF, paiement en ligne (frais Stripe en plus), vos avis Google repris sur le site et les modifications faites par nous sur simple message. S'y ajoute le CRM : fichier clients, historique des demandes et relances, pour ne laisser filer aucun acheteur ni aucun vendeur.",
    ]),
    ("Deux versions, selon votre activité", [
      "<b>Concession auto et moto</b> : un site 100 % vente, avec le stock en vitrine, des fiches complètes, la reprise et le financement mis en avant. Pas d'atelier ni de prise de rendez-vous. Voyez le <a href=\"/site-internet-concession-automobile/\">modèle concession automobile</a> ou le <a href=\"/site-internet-concession-moto/\">modèle concession moto</a>.",
      "<b>Agence immobilière</b> : biens à vendre et à louer, DPE et GES affichés, demande d'estimation en ligne. Le <a href=\"/site-internet-agence-immobiliere/\">modèle agence immobilière</a> montre le rendu sur ordinateur et sur téléphone.",
      "Vous tenez un garage qui ne vend pas de véhicules et faites seulement l'entretien, les pneus ou les freins ? Le Pack n'est pas nécessaire : le <a href=\"/site-internet-garage-mecanique/\">site pour garage d'entretien</a> se fait dès la formule Essentiel.",
    ]),
    ("Comment ça marche", [
      "Vous choisissez la formule Pack Auto, Moto & Immo, votre métier, puis votre style parmi ceux proposés sur la page d'accueil. Vous envoyez vos informations et vos photos depuis votre téléphone, ou vous remplissez le site vous-même dans votre espace avec l'aperçu en direct.",
      "Votre SIRET est demandé au paiement : votre espace professionnel Abracadeal est alors ouvert et relié à votre site automatiquement, et votre page professionnelle Abracadeal est visible sur Google. Votre site est en ligne en 48 heures, et rien n'est facturé avant que vous l'ayez validé.",
    ]),
    ("Le prix du Pack", [
      "99 € par mois et 490 € de mise en ligne, une fois. Hébergement, nom de domaine à votre nom, version mobile et espace client sont inclus. TVA non applicable, art. 293 B du CGI : le prix affiché est le prix payé. Sans engagement : l'abonnement s'arrête à la fin du mois en cours. Le détail figure dans les <a href=\"/#tarifs\">tarifs</a> et les <a href=\"/cgv.html\">conditions générales</a>.",
    ]),
  ],
  faq=[
    ("Que remplace le Pack Auto, Moto & Immo ?", "Un site vitrine d'un côté, et une passerelle ou un logiciel de diffusion d'annonces de l'autre. Ici, les deux sont réunis dans un seul abonnement, sans coût par annonce."),
    ("Combien d'annonces puis-je publier ?", "Autant que vous voulez : les annonces sont illimitées sur Abracadeal et synchronisées avec votre site (prix, photos, vendus)."),
    ("Mes annonces sont-elles diffusées ailleurs que sur Abracadeal ?", "La diffusion se fait aujourd'hui sur Abracadeal. Votre site et la page Google de chaque véhicule ou de chaque bien restent par ailleurs visibles de tous."),
    ("Je fais seulement de l'entretien automobile, ai-je besoin du Pack ?", "Non. Un garage d'entretien (vidange, pneus, freins) peut choisir Essentiel, Pro ou Premium. Le Pack sert aux garages qui vendent des véhicules, aux concessions et aux agences immobilières."),
    ("Que se passe-t-il si j'arrête ?", "L'abonnement s'arrête à la fin du mois en cours et vos annonces sont retirées. Votre nom de domaine reste à vous, et on vous remet vos textes et vos photos."),
  ]),

# ---------------------------------------------------------------- Site pas cher
"site-internet-pas-cher": dict(
  seo_title="Site internet pas cher pour pros dès 29 €/mois",
  meta="Site internet pas cher pour artisans et commerçants : dès 29 €/mois + 190 € de mise en ligne, hébergement et domaine inclus, sans engagement.",
  h1="Création de site internet pas cher pour les professionnels",
  feats=[("Dès 29 € par mois","Hébergement, nom de domaine, version mobile, sécurité et espace client compris dans le prix."),
         ("190 € de mise en ligne, une fois","Personnalisation du modèle, textes rédigés, photos, installation : tout est compris."),
         ("Aucun engagement","Vous arrêtez quand vous voulez, l'abonnement s'arrête à la fin du mois en cours."),
         ("Pas de frais cachés","Le prix affiché est le prix payé (TVA non applicable). Les dépannages sont compris."),
         ("Le modèle de votre métier","Rubriques, textes et réservation déjà pensés pour votre activité : on l'adapte, on ne repart pas de zéro."),
         ("Moins de temps que le faire soi-même","Pas besoin d'apprendre un outil de création : on fait le site, vous le modifiez simplement.")],
  lead="Un site vitrine pas cher, mais un vrai site pensé pour votre métier : dès 29 € par mois et 190 € de mise en ligne, une seule fois. Hébergement, nom de domaine, version mobile et espace client sont compris, sans engagement de durée.",
  body=[
    ("Ce que vous payez, et rien d'autre", [
      "Un site internet se paie en deux temps chez MyCreativeSite : des frais de mise en ligne une seule fois, puis un abonnement mensuel. En Essentiel, c'est 190 € puis 29 € par mois. TVA non applicable, art. 293 B du CGI : le montant affiché est celui que vous réglez.",
      "Cet abonnement couvre ce qui, ailleurs, s'ajoute souvent sur la facture : l'hébergement sécurisé avec le cadenas HTTPS, le nom de domaine réservé à votre nom, la version mobile, les sauvegardes, les mises à jour, les pages de mentions légales et les dépannages à distance. Si vous n'avez pas de logo, on met votre nom en forme, offert.",
    ]),
    ("Pourquoi un site peu cher peut quand même être un bon site", [
      "Le prix bas ne vient pas d'un site au rabais : chaque métier a déjà son modèle, avec les rubriques, les textes et la réservation qui lui conviennent. Plutôt que de repartir de zéro, on adapte ce modèle à votre entreprise, à vos prix et à vos photos. C'est ce travail déjà fait qui permet le tarif.",
      "Le site est conçu d'abord pour le téléphone, là où la plupart de vos clients vous cherchent. Il présente clairement vos services, vos horaires et vos coordonnées, et l'agenda de réservation en ligne est inclus dès Essentiel : le client choisit un créneau libre, confirmé tout de suite.",
    ]),
    ("Trois formules, selon ce dont vous avez besoin", [
      "<b>Essentiel, 29 € par mois</b> (+ 190 € de mise en ligne) : pour être trouvé sur Google et recevoir des demandes. Devis en PDF à votre logo et QR code de votre site inclus.",
      "<b>Pro, 49 € par mois</b> (+ 290 €) : tout Essentiel, plus la réservation avec paiement en ligne (acompte ou totalité, frais Stripe en plus), vos avis Google affichés sur le site et les modifications faites par nous sur simple message.",
      "<b>Premium, 79 € par mois</b> (+ 490 €) : tout Pro, plus le CRM, le site en français et en anglais, le référencement local renforcé, la création de votre logo et de votre bannière et le style Signature. Pour vendre en ligne, la formule <a href=\"/site-internet-boutique-en-ligne/\">Boutique</a> est à 99 € par mois.",
    ]),
    ("Pas cher, et sans vous attacher", [
      "Aucun contrat sur 48 mois : vous restez parce que le site vous apporte des clients. Vous résiliez quand vous voulez et l'abonnement s'arrête à la fin du mois en cours. Votre nom de domaine est à votre nom : si vous partez, il vous est rendu gratuitement, avec vos textes et vos photos.",
      "Pour faire le point sur les budgets, notre guide <a href=\"/conseils/combien-coute-un-site-internet/\">combien coûte un site internet</a> détaille ce qu'il faut regarder avant de signer.",
    ]),
    ("Comment ça marche", [
      "Vous choisissez une formule, votre métier et votre style, puis vous envoyez votre nom, vos services, vos prix, vos horaires et quelques photos depuis votre téléphone. On rédige les textes et on installe tout. Vous voyez votre site sur une adresse provisoire, vous le validez, et il part en ligne. Rien n'est facturé avant votre validation. Ensuite, vous modifiez prix, horaires et photos vous-même : voyez notre page <a href=\"/site-internet-facile-a-modifier/\">site facile à modifier</a>.",
    ]),
  ],
  faq=[
    ("Combien coûte un site internet chez MyCreativeSite ?", "À partir de 29 € par mois et 190 € de mise en ligne, une fois, en formule Essentiel. Pro est à 49 € par mois (+ 290 €), Premium à 79 € par mois (+ 490 €)."),
    ("Qu'est-ce qui est compris dans l'abonnement ?", "L'hébergement sécurisé, le nom de domaine à votre nom, la version mobile, l'espace client, les sauvegardes, les mises à jour, les mentions légales et les dépannages à distance."),
    ("Y a-t-il des options payantes ?", "Elles sont facultatives : fiche Google optimisée (149 € une fois), logo et bannière (49 € une fois, offerts en Premium et Boutique), adresse mail pro (+ 5 € par mois) et site français / anglais (+ 10 € par mois, inclus en Premium et Boutique)."),
    ("Suis-je engagé sur une durée ?", "Non. Vous arrêtez quand vous voulez : l'abonnement s'arrête à la fin du mois en cours."),
    ("Quand est-ce que je paie ?", "Une fois votre site vu sur une adresse provisoire et validé. Rien n'est facturé avant."),
  ]),

# ---------------------------------------------------------------- Site clé en main
"site-internet-cle-en-main": dict(
  seo_title="Site internet clé en main pour artisans et TPE",
  meta="Site internet clé en main : nom de domaine, textes, hébergement, mentions légales et mise en ligne faits pour vous en 48 h. Dès 29 €/mois.",
  h1="Site internet clé en main : on s'occupe de tout pour vous",
  lead="Avec un site internet clé en main, vous n'avez rien de technique à faire : on réserve votre nom de domaine, on rédige vos textes, on installe et on héberge le site, et il est en ligne en 48 heures. Vous gardez ensuite la main sur vos prix, horaires et photos.",
  body=[
    ("Ce qui est fait pour vous", [
      "Le nom de domaine est réservé à votre nom, par exemple votre-entreprise.fr, et branché sur le site. Si vous en avez déjà un, on le récupère et vos clients gardent la même adresse. Le guide <a href=\"/aide/nom-de-domaine/\">relier votre nom de domaine</a> montre ce qu'il faut faire chez votre fournisseur.",
      "Les textes sont rédigés à partir des informations que vous nous donnez : vos services, vos prix, vos horaires, votre façon de travailler. Vous n'avez pas encore de logo ? Votre nom est mis en forme gratuitement. Les pages obligatoires, mentions légales et confidentialité, sont prêtes dès la mise en ligne.",
      "L'hébergement est rapide et sécurisé, avec le cadenas HTTPS. Sauvegardes, sécurité et mises à jour sont surveillées pour vous, et en cas de souci on répare à distance, sans frais.",
    ]),
    ("Ce que vous avez à faire", [
      "Choisir votre formule, votre métier et votre style : deux minutes. Puis remplir un formulaire simple depuis votre téléphone, avec votre nom, votre adresse, vos horaires, vos services, vos prix et vos photos : environ quinze minutes. Pas de rendez-vous, pas de visio : tout se fait en ligne et par mail, à votre rythme, même le soir.",
      "Vous préférez tout remplir vous-même ? C'est possible aussi : vous accédez tout de suite à votre espace, avec l'aperçu en direct de votre site.",
    ]),
    ("Un modèle déjà pensé pour votre métier", [
      "Clé en main ne veut pas dire générique. Chaque métier a son modèle : un <a href=\"/site-internet-restaurant/\">restaurant</a> affiche sa carte, un <a href=\"/site-internet-artisan-batiment/\">artisan du bâtiment</a> ses chantiers et sa demande de devis, un <a href=\"/site-internet-coiffeur-institut-beaute/\">salon de coiffure ou institut</a> sa prise de rendez-vous. Vous choisissez ensuite le style, couleurs et typographies, et vous pouvez en changer plus tard sans frais.",
      "Toutes les photos des modèles sont libres de droits : vous pouvez les garder ou les remplacer par les vôtres.",
    ]),
    ("Après la mise en ligne, vous restez autonome", [
      "Votre espace client vous permet de changer un prix, un horaire ou une photo depuis votre téléphone, en direct. En formules Pro et Premium, vous pouvez aussi nous envoyer vos changements par message et on s'en occupe.",
      "Vos réservations et demandes arrivent par mail et dans votre espace dès qu'un client réserve. L'agenda de réservation en ligne est inclus dès Essentiel.",
    ]),
    ("Le prix d'un site clé en main", [
      "Essentiel à 29 € par mois, Pro à 49 € par mois, Premium à 79 € par mois, avec des frais de mise en ligne une seule fois (190 €, 290 € ou 490 €). Sans engagement, et votre nom de domaine, vos textes et vos photos restent à vous si vous partez. Comparez les formules dans les <a href=\"/#tarifs\">tarifs</a>.",
    ]),
  ],
  faq=[
    ("Que veut dire « clé en main » chez MyCreativeSite ?", "Que vous n'avez rien de technique à faire : nom de domaine, textes, hébergement, sécurité, mentions légales et mise en ligne sont pris en charge."),
    ("Faut-il savoir se servir d'un ordinateur ?", "Pas besoin : quelques champs à remplir depuis votre téléphone suffisent, et toute la partie technique reste de notre côté."),
    ("Dois-je me déplacer ou prévoir une réunion ?", "Aucun déplacement ni appel vidéo : les échanges passent par le formulaire et par mail, quand ça vous arrange."),
    ("J'ai déjà un nom de domaine, je le garde ?", "Oui. On le récupère et on le branche sur votre nouveau site : vos clients gardent la même adresse."),
    ("Qui est propriétaire du site ?", "Vous. Le nom de domaine est enregistré à votre nom, et en cas de départ vos textes et vos photos vous sont remis."),
  ]),

# ---------------------------------------------------------------- Site rapide
"site-internet-rapide": dict(
  seo_title="Site internet rapide : en ligne en 48 heures",
  meta="Besoin d'un site internet rapidement ? Votre site pro en ligne en 48 h, sans rendez-vous, pensé pour le mobile. Dès 29 €/mois, sans engagement.",
  h1="Site internet rapide : votre site pro en ligne en 48 heures",
  lead="Ouverture, nouveau local, saison qui démarre : vous avez besoin d'un site maintenant. Une fois vos informations et vos photos reçues, votre site est en ligne en général sous 48 heures ouvrées, sans rendez-vous. Et c'est un site léger, pensé pour s'afficher vite sur téléphone.",
  body=[
    ("Pourquoi on peut aller aussi vite", [
      "Parce que le plus long est déjà fait. Chaque métier a un modèle conçu et testé, avec ses rubriques, sa réservation et ses textes de départ. Il ne reste qu'à y mettre votre nom, vos services, vos prix, vos horaires et vos photos.",
      "Et parce qu'il n'y a ni réunion ni allers-retours de maquettes. Tout passe par un formulaire simple, depuis votre téléphone. Vous pouvez aussi remplir le site vous-même dans votre espace client : vous y accédez tout de suite, avec l'aperçu en direct.",
    ]),
    ("Les étapes, du choix à la mise en ligne", [
      "<b>1. Vous choisissez</b> votre formule, votre métier et votre style : deux minutes. <b>2. Vous envoyez vos infos</b> : nom, adresse, horaires, services, prix et photos, environ quinze minutes. <b>3. On rédige les textes</b>, on installe tout et on branche votre nom de domaine.",
      "Vous voyez ensuite votre site sur une adresse provisoire, sur ordinateur et sur téléphone. Vous le validez et vous payez : votre nom de domaine est réservé et le site part en ligne. Rien n'est facturé avant votre validation.",
    ]),
    ("Rapide à faire, rapide à charger", [
      "Un site rapide, c'est aussi un site qui s'ouvre vite. Les pages sont légères, et le site est pensé d'abord pour le téléphone : c'est de là que la plupart de vos clients vous cherchent, souvent en 4G. La vitesse d'affichage sur mobile compte pour Google, et un visiteur qui attend trop longtemps repart.",
      "L'hébergement rapide et sécurisé, avec le cadenas HTTPS, est inclus dans toutes les formules, tout comme le nom de domaine et la version mobile.",
    ]),
    ("Rapide à modifier ensuite", [
      "Une fois en ligne, un prix, un horaire ou une photo se change en quelques secondes depuis votre espace client, et la modification est visible aussitôt. La page <a href=\"/site-internet-facile-a-modifier/\">site facile à modifier</a> montre comment, et vous pouvez essayer l'espace client sans inscription.",
    ]),
    ("Quel site pour aller vite ?", [
      "Les modèles existent déjà pour de nombreux métiers, par exemple <a href=\"/site-internet-plombier-electricien/\">plombier et électricien</a>, <a href=\"/site-internet-vtc/\">chauffeur VTC et taxi</a> ou <a href=\"/site-internet-boulangerie/\">boulangerie</a>. Côté prix : Essentiel à 29 € par mois (+ 190 € de mise en ligne), Pro à 49 € (+ 290 €), Premium à 79 € (+ 490 €), sans engagement. Pour un site sans rien à gérer, voyez aussi notre offre <a href=\"/site-internet-cle-en-main/\">site clé en main</a>.",
    ]),
  ],
  faq=[
    ("En combien de temps mon site est-il en ligne ?", "En général sous 48 heures ouvrées après réception de vos informations et de vos photos."),
    ("Que dois-je fournir ?", "Le nom de votre entreprise, votre adresse, vos services et prix, vos horaires, vos coordonnées et quelques photos. On rédige les textes à partir de ces informations."),
    ("Faut-il un rendez-vous ?", "Non. Pas de visio ni de réunion : un formulaire simple, depuis votre téléphone, suffit."),
    ("Est-ce que je vois le site avant de payer ?", "Oui. Vous le voyez sur une adresse provisoire, sur ordinateur et sur téléphone, et rien n'est facturé avant que vous l'ayez validé."),
    ("Un site rapide à charger, ça compte pour Google ?", "Oui : la vitesse sur mobile fait partie des critères pris en compte par Google, et un site lent fait partir les visiteurs."),
  ]),
}
