# Région Alpes (sports d'hiver) — édition française (11/11/2026).
# Dates d'ouverture 2026-2027 annoncées par les stations (sous réserve d'enneigement). Pas de prix.

REGION = {
    "slug": "alpes",
    "nom": "Alpes",
    "h1": "Partir au ski dans les Alpes",
    "de": "des Alpes",
    "autres": "Autres stations des Alpes",
    "couleur": "azur",
    "timbre": "Savoie Mont-Blanc",
    "photo": "alpes",
    "photo_alt": "Des sommets enneigés au-dessus d'une station des Alpes",
    "address_region": "Auvergne-Rhône-Alpes",
    "description": "Chamonix, Val Thorens, Courchevel, Megève : nos guides des stations de ski des Alpes, dates d'ouverture de la saison, accès en train et activités sans ski.",
    "accroche": "Grands domaines reliés, villages de charme et sommets à plus de 3 000 mètres : la saison 2026-2027 commence dès le 21 novembre dans les stations les plus hautes.",
    "intro": [
        "Les Alpes françaises concentrent les plus grands domaines skiables du monde, entre la Savoie et la Haute-Savoie. Chaque station a sa personnalité : haute altitude et neige garantie à Val Thorens, luxe et pistes impeccables à Courchevel, ambiance de village à Megève, haute montagne et alpinisme à Chamonix.",
        "Beaucoup de stations se rejoignent sans voiture : en train jusqu'à Moûtiers, Sallanches ou Saint-Gervais, puis en car ou en navette. Chaque guide indique quand la station ouvre, comment y aller et quoi faire quand on ne skie pas. Les dates d'ouverture restent toujours soumises à l'enneigement.",
    ],
    "departements": ["73", "74"],
}

GROUPES = [
    ("stations", "Stations de ski"),
]

VEDETTES = ["chamonix", "val-thorens", "courchevel", "megeve"]

def _d(**k):
    k.setdefault("region", "alpes")
    return k

DESTINATIONS = [
    _d(slug="chamonix", groupe="stations", nom="Chamonix", dept="74", cachet="Haute-Savoie", couleur="encre", h1="Chamonix : ski et sorties au pied du mont Blanc",
       description="Visiter Chamonix en hiver : les domaines skiables, l'Aiguille du Midi, la Mer de Glace, la Vallée Blanche. Dates d'ouverture 2026-2027 et accès en train.",
       accroche="La capitale de l'alpinisme, face au mont Blanc. On y vient pour skier, mais aussi pour monter à près de 3 900 mètres sans être alpiniste.",
       intro=[
           "Chamonix n'est pas une station unique mais une vallée de plusieurs domaines indépendants : le Brévent et la Flégère face au mont Blanc, les Grands Montets au-dessus d'Argentière, Balme au fond de la vallée et Les Houches à l'entrée. Les navettes gratuites de la vallée les relient.",
           "Pour la saison 2026-2027, les premiers secteurs, les Grands Montets et la Flégère, doivent ouvrir fin novembre, les autres suivent en décembre. Le téléphérique de l'Aiguille du Midi et le train du Montenvers ferment chaque année quelques semaines en novembre pour maintenance avant de rouvrir pour l'hiver.",
       ],
       a_voir=[
           ("L'Aiguille du Midi", "Le téléphérique monte à 3 842 mètres en une vingtaine de minutes. Au sommet, terrasses face au mont Blanc et « Pas dans le vide », une cage de verre au-dessus de 1 000 mètres de vide. Montez le matin, par temps clair."),
           ("Le train du Montenvers et la Mer de Glace", "Un train à crémaillère rouge relie Chamonix au site du Montenvers, face au plus grand glacier de France. Une télécabine et des escaliers mènent à la grotte de glace creusée chaque année."),
           ("La Vallée Blanche", "Une descente hors-piste mythique d'une vingtaine de kilomètres depuis l'Aiguille du Midi. Elle se fait uniquement avec un guide de haute montagne."),
           ("Le Brévent et la Flégère", "Les deux domaines du versant ensoleillé, avec les plus belles vues sur le massif du Mont-Blanc. Idéal pour les skieurs intermédiaires."),
           ("Les Grands Montets", "Le domaine des bons skieurs, au-dessus d'Argentière : grandes pentes, neige d'altitude et vue sur les glaciers."),
           ("Le centre de Chamonix", "Rues piétonnes, façades Belle Époque, statue de Balmat et Saussure pointant le mont Blanc. L'après-ski se passe ici."),
       ],
       y_aller=[
           ("En train", "TGV ou TER jusqu'à Saint-Gervais-les-Bains - Le Fayet, puis le Mont-Blanc Express jusqu'à Chamonix, en une quarantaine de minutes."),
           ("Depuis l'aéroport de Genève", "Environ 1 h 15 par la route. Des navettes et des transferts privés font le trajet toute la saison."),
           ("Sur place", "Les navettes de la vallée desservent les domaines skiables. La carte d'hôte remise par les hébergeurs donne accès aux transports locaux."),
       ],
       fiche=[("Ouverture 2026-2027", "Fin novembre (premiers secteurs)"), ("Pour qui", "Bons skieurs, amateurs de haute montagne"), ("Sans skier", "Aiguille du Midi, Mer de Glace"), ("Accès", "Train jusqu'au Fayet puis Mont-Blanc Express")],
       conseils=[
           "Regardez la météo du sommet avant de monter à l'Aiguille du Midi : par temps couvert, on ne voit rien.",
           "Le hors-piste à Chamonix se pratique en haute montagne : ne partez jamais sans guide ni équipement de sécurité.",
           "En février, réservez votre hébergement tôt : la vallée est très demandée pendant les vacances scolaires.",
       ],
       activites=[
           ("Aiguille du Midi et Mer de Glace", "Billets et excursions guidées au départ de Chamonix ou de Genève.", "Chamonix Aiguille du Midi"),
           ("Cours de ski et sorties hors-piste", "Moniteurs et guides de haute montagne dans la vallée de Chamonix.", "Chamonix ski"),
       ],
       faq=[
           ("Quand ouvre la station de Chamonix en 2026 ?", "Les premiers secteurs, les Grands Montets et la Flégère, doivent ouvrir fin novembre 2026, le reste de la vallée en décembre, selon l'enneigement."),
           ("Peut-on monter à l'Aiguille du Midi en hiver ?", "Oui, le téléphérique fonctionne en hiver après sa fermeture annuelle de maintenance en novembre. Vérifiez la météo au sommet avant de partir."),
           ("Comment aller à Chamonix sans voiture ?", "En train jusqu'à Saint-Gervais-Le Fayet puis le Mont-Blanc Express, ou en navette depuis l'aéroport de Genève."),
       ]),

    _d(slug="val-thorens", groupe="stations", nom="Val Thorens", dept="73", cachet="Savoie", couleur="azur", h1="Val Thorens : la plus haute station d'Europe",
       description="Skier à Val Thorens : dates d'ouverture 2026-2027, les 3 Vallées, la Cime Caron, l'accès en train par Moûtiers et nos conseils.",
       accroche="À 2 300 mètres, Val Thorens est la plus haute station d'Europe. Elle ouvre la première et ferme la dernière : de fin novembre au début mai.",
       intro=[
           "Val Thorens se trouve tout au fond de la vallée des Belleville, au cœur des 3 Vallées, le plus grand domaine skiable relié du monde, avec Les Menuires, Méribel et Courchevel. Son altitude lui assure une neige fiable du début à la fin de la saison.",
           "Pour l'hiver 2026-2027, la station annonce une ouverture le 21 novembre 2026 et une fermeture début mai 2027, selon l'enneigement. La station est presque entièrement piétonne : on part skis aux pieds de la plupart des hébergements.",
       ],
       a_voir=[
           ("La Cime Caron", "Un téléphérique monte à 3 200 mètres pour l'un des plus grands panoramas des Alpes, du mont Blanc à la Vanoise. La descente est réservée aux bons skieurs."),
           ("Les 3 Vallées", "Avec le forfait 3 Vallées, on rejoint Les Menuires, Méribel et Courchevel à skis dans la journée."),
           ("Orelle", "Côté Maurienne, le secteur d'Orelle est relié à Val Thorens et offre des pistes ensoleillées et souvent moins fréquentées."),
           ("L'après-ski", "Val Thorens est réputée pour son ambiance festive, des terrasses d'altitude aux bars de la station."),
       ],
       y_aller=[
           ("En train", "Train jusqu'à la gare de Moûtiers - Salins - Brides-les-Bains, puis car régional jusqu'à la station, environ une heure de montée."),
           ("En avion", "Les aéroports les plus proches sont Chambéry, Lyon et Genève, avec des navettes et des transferts privés en saison."),
           ("En voiture", "Par la vallée de la Tarentaise puis la route des Belleville. Équipements spéciaux obligatoires en hiver ; la station est piétonne, prévoyez un parking."),
       ],
       fiche=[("Ouverture 2026-2027", "21 novembre 2026"), ("Fermeture", "Début mai 2027"), ("Altitude", "2 300 m"), ("Domaine", "Les 3 Vallées")],
       conseils=[
           "En début et fin de saison, c'est l'une des rares stations où l'on skie sur tout le domaine : idéal pour un séjour en novembre ou en avril.",
           "À 2 300 mètres, le froid et le vent peuvent être vifs : prévoyez masque, cagoule et crème solaire.",
           "Achetez votre forfait en ligne avant d'arriver pour éviter la file aux caisses le samedi.",
       ],
       activites=[
           ("Activités à Val Thorens", "Cours de ski, motoneige, parapente et sorties en raquettes.", "Val Thorens"),
           ("Excursions dans les 3 Vallées", "Sorties guidées et activités à Méribel et Courchevel.", "3 Vallées ski"),
       ],
       faq=[
           ("Quand ouvre Val Thorens en 2026 ?", "La station annonce une ouverture le samedi 21 novembre 2026, sous réserve d'enneigement, pour une saison jusqu'à début mai 2027."),
           ("Pourquoi Val Thorens est-elle la plus haute station d'Europe ?", "Son village est construit à 2 300 mètres d'altitude, et ses remontées montent jusqu'à 3 200 mètres à la Cime Caron."),
           ("Comment aller à Val Thorens sans voiture ?", "En train jusqu'à Moûtiers, puis en car régional jusqu'à la station."),
       ]),

    _d(slug="courchevel", groupe="stations", nom="Courchevel", dept="73", cachet="Savoie", couleur="encre", h1="Courchevel : ski et séjour dans les 3 Vallées",
       description="Skier à Courchevel : les villages 1850, 1650, 1550 et Le Praz, dates d'ouverture 2026-2027, accès en train par Moûtiers et activités sans ski.",
       accroche="Pistes damées au cordeau, altiport et grands hôtels : Courchevel est la station la plus prestigieuse des Alpes, mais aussi un excellent domaine pour tous les niveaux.",
       intro=[
           "Courchevel regroupe plusieurs villages étagés : Saint-Bon, Le Praz, Courchevel Village, Moriond et Courchevel 1850, le plus connu. Avec La Tania, ils forment le domaine de Courchevel, relié aux 3 Vallées par Méribel.",
           "La station annonce une saison du 4 décembre 2026 au 18 avril 2027, selon l'enneigement. Son domaine, réputé pour la qualité de son damage, convient aussi bien aux débutants qu'aux experts.",
       ],
       a_voir=[
           ("Courchevel 1850", "Le cœur de la station : boutiques de luxe, restaurants étoilés et l'altiport, où atterrissent les petits avions entre les pistes."),
           ("Le Grand Couloir", "Une des pistes noires les plus célèbres des Alpes, au départ de la Saulire. Réservée aux experts et conditionnée à l'enneigement."),
           ("Les tremplins du Praz", "Construits pour les Jeux olympiques d'Albertville en 1992, ils accueillent encore des compétitions de saut à skis."),
           ("Aquamotion", "Un grand centre aquatique et de bien-être à Courchevel Moriond, parfait pour une journée sans ski."),
           ("Moriond et La Tania", "Des villages plus familiaux et plus abordables, avec un accès direct au même domaine."),
       ],
       y_aller=[
           ("En train", "Train jusqu'à Moûtiers - Salins - Brides-les-Bains, puis car régional jusqu'aux différents villages de Courchevel."),
           ("En avion", "Aéroports de Chambéry, Lyon et Genève, avec navettes et transferts privés. L'altiport accueille aussi des vols privés."),
           ("Sur place", "Des navettes gratuites relient les villages de la station."),
       ],
       fiche=[("Ouverture 2026-2027", "4 décembre 2026"), ("Fermeture", "18 avril 2027"), ("Domaine", "Les 3 Vallées"), ("Pour qui", "Tous niveaux, séjours haut de gamme")],
       conseils=[
           "Pour un budget plus raisonnable, logez à Moriond, au Praz ou à La Tania : vous skierez sur le même domaine.",
           "Les pistes vers Méribel permettent de skier dans les 3 Vallées dans la journée : vérifiez que votre forfait l'inclut.",
           "Réservez vos restaurants d'altitude à l'avance pendant les vacances de Noël et de février.",
       ],
       activites=[
           ("Activités à Courchevel", "Cours de ski, raquettes, parapente et chiens de traîneau.", "Courchevel"),
           ("Excursions dans les 3 Vallées", "Sorties guidées à skis entre Courchevel, Méribel et Val Thorens.", "Courchevel 3 Vallées"),
       ],
       faq=[
           ("Quand ouvre Courchevel en 2026 ?", "La station annonce une ouverture le 4 décembre 2026 et une fermeture le 18 avril 2027, sous réserve d'enneigement."),
           ("Quel village choisir à Courchevel ?", "1850 pour le prestige et l'altitude, Moriond pour les familles, Le Praz et La Tania pour le charme et des prix plus doux."),
           ("Comment aller à Courchevel en train ?", "Jusqu'à la gare de Moûtiers, puis en car régional jusqu'à la station."),
       ]),

    _d(slug="megeve", groupe="stations", nom="Megève", dept="74", cachet="Haute-Savoie", couleur="ocre", h1="Megève : village de charme et ski face au mont Blanc",
       description="Skier à Megève : le village, le domaine Évasion Mont-Blanc, les dates d'ouverture 2026-2027, l'accès en train par Sallanches et les activités sans ski.",
       accroche="Un vrai village savoyard, des calèches dans les rues et des pistes boisées face au mont Blanc. Megève est la station chic et douce par excellence.",
       intro=[
           "Megève s'est construite autour de son village médiéval, avec son église et ses rues piétonnes. Son domaine fait partie d'Évasion Mont-Blanc, qui relie Megève, Saint-Gervais, Combloux et d'autres villages sur plus de 400 kilomètres de pistes.",
           "Pour 2026-2027, Megève prévoit une pré-ouverture partielle début décembre, puis une ouverture générale le 19 décembre 2026 jusqu'au début avril 2027, selon l'enneigement. Ses pistes de moyenne altitude, souvent bordées de sapins, en font une station agréable même par mauvais temps.",
       ],
       a_voir=[
           ("Le village", "Place de l'église, rues piétonnes, boutiques et calèches : c'est l'un des plus beaux villages de station des Alpes, surtout illuminé en décembre."),
           ("Le Mont d'Arbois", "Le secteur relié à Saint-Gervais, avec de longues pistes faciles et une vue imprenable sur le mont Blanc."),
           ("Rochebrune", "Le domaine juste au-dessus du village, accessible en téléphérique, pratique pour une demi-journée."),
           ("Le Jaillet et Combloux", "De l'autre côté de la vallée, des pistes ensoleillées face à la chaîne du Mont-Blanc."),
           ("Les activités sans ski", "Promenades en calèche, patinoire, randonnées en raquettes et chiens de traîneau."),
       ],
       y_aller=[
           ("En train", "Jusqu'à la gare de Sallanches - Combloux - Megève, puis une trentaine de minutes en car ou en taxi jusqu'au village."),
           ("Depuis l'aéroport de Genève", "Environ 1 h 15 par la route, avec navettes et transferts privés pendant la saison."),
           ("Sur place", "Des navettes gratuites desservent les différents départs de remontées."),
       ],
       fiche=[("Ouverture 2026-2027", "19 décembre 2026 (pré-ouverture début décembre)"), ("Fermeture", "Début avril 2027"), ("Domaine", "Évasion Mont-Blanc"), ("Pour qui", "Familles, skieurs tranquilles, amateurs de village")],
       conseils=[
           "Montez au Mont d'Arbois par beau temps : c'est là que la vue sur le mont Blanc est la plus spectaculaire.",
           "Profitez du village en fin de journée, quand les illuminations s'allument.",
           "Pendant les vacances de février, réservez les cours de ski pour enfants plusieurs semaines à l'avance.",
       ],
       activites=[
           ("Activités à Megève", "Cours de ski, chiens de traîneau, parapente et raquettes.", "Megève"),
           ("Excursions vers Chamonix et le mont Blanc", "Journées guidées au départ de Megève ou de Genève.", "Megève Chamonix excursion"),
       ],
       faq=[
           ("Quand ouvre Megève en 2026 ?", "Pré-ouverture partielle début décembre, puis ouverture générale le 19 décembre 2026, sous réserve d'enneigement."),
           ("Megève est-elle adaptée aux débutants ?", "Oui, le domaine compte beaucoup de pistes bleues et vertes, souvent abritées par la forêt."),
           ("Quelle est la gare la plus proche de Megève ?", "La gare de Sallanches - Combloux - Megève, à une trentaine de minutes du village en car ou en taxi."),
       ]),
]

TITRES = {
    "chamonix": "Chamonix en hiver : ski, Aiguille du Midi, accès",
    "val-thorens": "Val Thorens : ouverture 2026, accès, conseils",
    "courchevel": "Courchevel : ski, villages, ouverture 2026",
    "megeve": "Megève : ski, village, ouverture 2026-2027",
}
TITRE_REGION = "Ski dans les Alpes : stations et ouvertures 2026"

LIEU_VOIR = {"chamonix": "à Chamonix", "val-thorens": "à Val Thorens", "courchevel": "à Courchevel", "megeve": "à Megève"}
LIEU_ALLER = {"chamonix": "à Chamonix", "val-thorens": "à Val Thorens", "courchevel": "à Courchevel", "megeve": "à Megève"}

GEO = {"chamonix": (45.9237, 6.8694), "val-thorens": (45.2980, 6.5800), "courchevel": (45.4154, 6.6347), "megeve": (45.8567, 6.6175)}

ALIAS = {"chamonix": ["Chamonix"], "val-thorens": ["Val Thorens"], "courchevel": ["Courchevel"], "megeve": ["Megève"]}
