# Contenu éditorial du guide Clic&Site.
# Règle : pas de prix, pas d'horaires précis de transports (ils changent) — seulement des repères stables.

REGIONS = [
    {
        "slug": "cote-d-azur",
        "nom": "Côte d'Azur",
        "titre_seo": "Visiter la Côte d'Azur : les plus beaux sites à voir | Clic&Site",
        "description": "Monaco, Èze, les îles de Lérins, Saint-Paul-de-Vence, Saint-Tropez : nos guides pour visiter la Côte d'Azur, comment y aller et quoi réserver.",
        "accroche": "Villages perchés, îles à quinze minutes de la Croisette, ports de légende : la Riviera se visite très bien sans voiture, à condition de savoir où aller et quand.",
        "intro": [
            "La Côte d'Azur s'étire de Saint-Tropez à Menton, entre le Var et la frontière italienne. Le train côtier relie la plupart des grandes villes, Nice et Cannes servent de camp de base, et beaucoup de sites se combinent dans la même journée.",
            "Le plus difficile n'est pas de trouver quoi voir, c'est d'éviter les embouteillages de juillet-août et les heures où les cars de croisière arrivent. Chaque guide ci-dessous vous dit comment y aller et à quel moment.",
        ],
        "departements": ["06", "83"],
    },
]

PROCHAINES_REGIONS = ["Provence", "Alpes", "Paris", "Bretagne", "Pays basque"]

DESTINATIONS = [
    {
        "slug": "monaco",
        "region": "cote-d-azur",
        "nom": "Monaco",
        "dept": "MC",
        "cachet": "Principauté",
        "couleur": "azur",
        "titre_seo": "Visiter Monaco : que voir, comment y aller, quoi réserver | Clic&Site",
        "description": "Visiter Monaco en une journée : le Rocher, la relève de la garde, le Musée océanographique, Monte-Carlo et le port. Comment y aller depuis Nice et Cannes.",
        "accroche": "Deux kilomètres carrés, un palais, un casino et l'un des plus beaux musées de la mer d'Europe. Monaco se visite à pied en une journée.",
        "intro": [
            "La Principauté se découvre en deux temps : le Rocher, vieille ville perchée où se trouvent le Palais princier et le Musée océanographique, puis Monte-Carlo, son casino et ses jardins. Entre les deux, le port Hercule et ses yachts.",
            "Monaco est un pays à part entière, mais on y entre sans contrôle depuis la France et on paie en euros. Le relief est raide : des ascenseurs publics gratuits relient les différents niveaux de la ville, pensez-y avant de gravir les escaliers.",
        ],
        "a_voir": [
            ("Le Palais princier et la relève de la garde", "Chaque jour à 11 h 55, les carabiniers du Prince relèvent la garde devant le Palais. Arrivez un quart d'heure avant pour avoir une place au premier rang. Les grands appartements se visitent une partie de l'année."),
            ("Le Musée océanographique", "Fondé par le prince Albert Ier et accroché à la falaise, il réunit un aquarium remarquable et des collections scientifiques. La terrasse sur le toit offre l'une des plus belles vues de la côte."),
            ("La cathédrale de Monaco", "Église en pierre blanche du Rocher, où reposent la princesse Grace et le prince Rainier III. L'entrée est libre en dehors des offices."),
            ("Les jardins Saint-Martin", "Une promenade ombragée au bord de la falaise, entre le musée et la cathédrale. Idéal pour une pause à l'abri de la chaleur."),
            ("Monte-Carlo et la place du Casino", "Le casino, l'opéra et l'Hôtel de Paris forment l'ensemble le plus photographié de la Principauté. L'atrium du casino se visite en journée ; une tenue correcte est demandée."),
            ("Le port Hercule", "Le cœur du circuit du Grand Prix de Formule 1, au pied du Rocher. Le long des quais, on mesure la taille des yachts amarrés."),
        ],
        "y_aller": [
            ("En train", "La gare de Monaco-Monte-Carlo est desservie par les TER de la ligne côtière : une vingtaine de minutes depuis Nice, environ une heure depuis Cannes. C'est la solution la plus simple."),
            ("En car", "Des cars régionaux longent la Basse Corniche depuis Nice. Plus lent que le train, mais avec la mer tout du long."),
            ("En voiture ou en chauffeur", "Les parkings publics sont nombreux mais payants. Pendant le Grand Prix et les grands événements, la circulation est très difficile : préférez le train ou un transfert avec chauffeur."),
        ],
        "fiche": [
            ("Durée conseillée", "Une journée"),
            ("Meilleur moment", "Avril à juin, septembre-octobre"),
            ("À éviter", "La semaine du Grand Prix, sauf pour la course"),
            ("Pour qui", "Tout le monde, à pied"),
        ],
        "conseils": [
            "Commencez par le Rocher le matin (relève de la garde, musée), descendez au port pour déjeuner, puis montez à Monte-Carlo l'après-midi.",
            "Les jours de croisière, le Rocher est très fréquenté entre 10 h et 15 h : le musée reste la meilleure activité à ces heures-là.",
            "Gardez une tenue correcte pour la cathédrale et le casino.",
        ],
        "activites": [
            ("Billets et visites à Monaco", "Musée océanographique, Palais princier, visites guidées du Rocher.", "Monaco"),
            ("Monaco, Èze et la Riviera en excursion", "Journées en petit groupe au départ de Nice ou de Cannes.", "Monaco Eze excursion"),
        ],
        "faq": [
            ("Faut-il un passeport pour aller à Monaco ?", "Il n'y a pas de contrôle à la frontière entre la France et Monaco, mais gardez une pièce d'identité sur vous, comme partout en voyage."),
            ("Combien de temps faut-il pour visiter Monaco ?", "Une journée suffit pour le Rocher, le port et Monte-Carlo. Comptez une demi-journée de plus si vous voulez prendre le temps au Musée océanographique."),
            ("Quel est le meilleur moyen d'aller à Monaco depuis Nice ?", "Le TER : une vingtaine de minutes, avec une gare au cœur de la Principauté. La voiture est déconseillée les jours d'affluence."),
        ],
    },
    {
        "slug": "eze",
        "region": "cote-d-azur",
        "nom": "Èze",
        "dept": "06",
        "cachet": "Alpes-Maritimes",
        "couleur": "pin",
        "titre_seo": "Visiter Èze village : jardin exotique, sentier Nietzsche, conseils | Clic&Site",
        "description": "Visiter Èze, le village perché entre Nice et Monaco : le jardin d'Èze, le sentier Nietzsche, les parfumeries. Comment y aller et à quelle heure.",
        "accroche": "Un village médiéval accroché à son rocher, à plus de 400 mètres au-dessus de la mer. La vue depuis le jardin, tout en haut, justifie à elle seule la montée.",
        "intro": [
            "Èze est l'un des villages perchés les plus spectaculaires de la Riviera, entre Nice et Monaco. Ruelles pavées, passages voûtés, maisons de pierre : on y entre à pied, les voitures restent en bas.",
            "Au sommet, sur les ruines de l'ancien château, le jardin d'Èze mêle plantes grasses et sculptures, avec une vue qui porte sur la presqu'île du Cap-Ferrat et, par temps très clair, jusqu'à la Corse.",
        ],
        "a_voir": [
            ("Le jardin d'Èze", "Le point culminant du village. Le panorama sur la Méditerranée y est saisissant ; c'est la seule partie payante de la visite, et celle qu'il ne faut pas manquer."),
            ("Les ruelles du village", "Pas de plan nécessaire : on monte vers le jardin en se perdant volontairement dans les passages. Galeries d'art et petites boutiques à chaque coin."),
            ("L'église Notre-Dame-de-l'Assomption", "Façade ocre et intérieur baroque, au cœur du village."),
            ("Le chemin de Nietzsche", "Le sentier qui relie le bord de mer (Èze-sur-Mer) au village, emprunté par le philosophe. Comptez une bonne heure de montée raide : à faire plutôt dans le sens de la descente si vous n'êtes pas marcheur."),
            ("Les parfumeries", "Au pied du village, les parfumeurs de Grasse ont installé usines et boutiques. Visites gratuites des ateliers."),
        ],
        "y_aller": [
            ("En car depuis Nice", "Des cars régionaux montent par la Moyenne Corniche et déposent au pied du village. C'est le moyen le plus pratique sans voiture."),
            ("En train puis à pied", "Le TER s'arrête à Èze-sur-Mer, au bord de l'eau. De là, le chemin de Nietzsche monte jusqu'au village : une belle randonnée, mais exigeante."),
            ("En voiture ou en chauffeur", "Les places de parking au pied du village sont rares en saison. Un transfert avec chauffeur permet de combiner Èze et Monaco dans la même journée."),
        ],
        "fiche": [
            ("Durée conseillée", "Une demi-journée"),
            ("Meilleur moment", "Tôt le matin ou en fin d'après-midi"),
            ("À éviter", "Le milieu de journée en été"),
            ("Pour qui", "Bons marcheurs, pas de poussette"),
        ],
        "conseils": [
            "Arrivez avant 10 h : les excursions en car arrivent ensuite et les ruelles deviennent étroites.",
            "Les rues sont en pente et pavées : de bonnes chaussures sont indispensables.",
            "Èze se combine très bien avec Monaco, à quelques minutes de route.",
        ],
        "activites": [
            ("Excursions Èze et Monaco", "Le duo classique de la Riviera, en demi-journée ou en journée.", "Eze Monaco"),
            ("Ateliers et visites autour du parfum", "Création de parfum, visites guidées des parfumeries.", "Eze parfum"),
        ],
        "faq": [
            ("Le village d'Èze est-il payant ?", "Non, le village est en accès libre. Seul le jardin d'Èze, au sommet, est payant."),
            ("Peut-on visiter Èze avec une poussette ou en fauteuil ?", "C'est très difficile : les ruelles sont en pente, pavées et souvent en escalier. Un porte-bébé est préférable."),
            ("Combien de temps dure le chemin de Nietzsche ?", "Comptez environ une heure de montée depuis Èze-sur-Mer, un peu moins à la descente. Le sentier est raide et peu ombragé : évitez les heures chaudes."),
        ],
    },
    {
        "slug": "iles-de-lerins",
        "region": "cote-d-azur",
        "nom": "Îles de Lérins",
        "dept": "06",
        "cachet": "Cannes",
        "couleur": "ocre",
        "titre_seo": "Îles de Lérins : Sainte-Marguerite, Saint-Honorat, bateau depuis Cannes | Clic&Site",
        "description": "Visiter les îles de Lérins au large de Cannes : Sainte-Marguerite et le Masque de fer, Saint-Honorat et ses moines. Bateaux, conseils et activités.",
        "accroche": "À un quart d'heure de bateau de la Croisette, deux îles sans voiture : des pins, des criques, un fort où fut enfermé le Masque de fer et une abbaye où vivent encore des moines.",
        "intro": [
            "Les îles de Lérins sont la meilleure échappée depuis Cannes. Sainte-Marguerite, la plus grande, est couverte de forêt et bordée de criques. Saint-Honorat, plus petite, appartient à une communauté de moines qui y cultive la vigne.",
            "On n'y trouve ni voiture ni grande route : seulement des sentiers, de l'ombre et de l'eau très claire. Prévoyez la journée, de l'eau et un pique-nique.",
        ],
        "a_voir": [
            ("Le Fort royal (Sainte-Marguerite)", "On y visite la cellule de l'énigmatique homme au masque de fer, prisonnier sous Louis XIV. Le fort abrite aussi le musée de la Mer et ses objets remontés d'épaves antiques."),
            ("Le tour de Sainte-Marguerite à pied", "Un sentier fait le tour de l'île en suivant la côte, avec des criques pour se baigner. Le chemin intérieur traverse une forêt de pins et d'eucalyptus."),
            ("L'abbaye de Lérins (Saint-Honorat)", "Les moines cisterciens accueillent les visiteurs dans le silence. L'église abbatiale se visite, ainsi que le monastère fortifié au bord de l'eau."),
            ("Les vignes et les vins des moines", "Saint-Honorat est couverte de vignes. Les moines produisent un vin réputé et des liqueurs, vendus sur place."),
        ],
        "y_aller": [
            ("En bateau depuis Cannes", "Les navettes partent du quai Laubeuf, au port de Cannes, toute l'année. Une quinzaine de minutes pour Sainte-Marguerite, un peu plus pour Saint-Honorat. Les deux îles sont desservies séparément : vérifiez avant de partir si vous voulez visiter les deux."),
            ("Depuis d'autres ports", "En saison, des bateaux partent aussi de Juan-les-Pins, Golfe-Juan ou Nice, avec des fréquences plus faibles."),
        ],
        "fiche": [
            ("Durée conseillée", "Une journée"),
            ("Meilleur moment", "Mai-juin et septembre"),
            ("À éviter", "Les dimanches d'août, très fréquentés"),
            ("Pour qui", "Familles, marcheurs, baigneurs"),
        ],
        "conseils": [
            "Prenez un des premiers bateaux du matin : vous aurez les criques pour vous.",
            "Emportez de l'eau et de quoi déjeuner, les possibilités de restauration sont limitées.",
            "Sur Saint-Honorat, le calme fait partie de l'expérience : tenue correcte et voix basse près de l'abbaye.",
        ],
        "activites": [
            ("Bateaux et excursions vers les îles", "Traversées, croisières autour des îles, sorties snorkeling.", "Iles de Lerins"),
            ("Sorties en mer au départ de Cannes", "Croisières, catamarans et balades en bateau dans la baie.", "Cannes bateau"),
        ],
        "faq": [
            ("Peut-on visiter les deux îles dans la même journée ?", "Oui, mais elles sont desservies séparément au départ de Cannes. Renseignez-vous sur les traversées le jour même et commencez tôt."),
            ("Peut-on se baigner aux îles de Lérins ?", "Oui, Sainte-Marguerite est bordée de criques à l'eau très claire. Il n'y a pas de plage surveillée : soyez prudents avec les enfants."),
            ("Y a-t-il des restaurants sur les îles ?", "Il y en a quelques-uns, souvent pris d'assaut en été. Un pique-nique reste la solution la plus simple."),
        ],
    },
    {
        "slug": "saint-paul-de-vence",
        "region": "cote-d-azur",
        "nom": "Saint-Paul-de-Vence",
        "dept": "06",
        "cachet": "Alpes-Maritimes",
        "couleur": "encre",
        "titre_seo": "Visiter Saint-Paul-de-Vence : village, Fondation Maeght, conseils | Clic&Site",
        "description": "Visiter Saint-Paul-de-Vence : les remparts, les galeries, la Fondation Maeght et la tombe de Chagall. Comment y aller depuis Nice et Cannes.",
        "accroche": "Un village fortifié sur sa colline, des galeries d'art à chaque porte, et à deux pas l'un des plus beaux musées d'art moderne d'Europe.",
        "intro": [
            "Saint-Paul-de-Vence est le village des artistes de la Côte d'Azur. Ses remparts, élevés au XVIe siècle, enserrent toujours un dédale de ruelles pavées, de fontaines et de galeries.",
            "Chagall y a vécu et repose dans le petit cimetière du village. Juste en dessous, la Fondation Maeght, ouverte dans les années 1960, réunit Miró, Giacometti, Braque ou Chagall dans un bâtiment pensé pour eux.",
        ],
        "a_voir": [
            ("Le tour des remparts", "Un chemin de ronde fait le tour du village, avec des vues sur les collines jusqu'à la mer d'un côté, et vers les Préalpes de l'autre."),
            ("La rue Grande et les galeries", "L'artère principale traverse le village de porte en porte. Peintres, sculpteurs et céramistes y exposent toute l'année."),
            ("La Fondation Maeght", "À quelques minutes de marche du village, un musée en pleine nature : la cour Giacometti, le labyrinthe Miró, des expositions temporaires de grande qualité."),
            ("La tombe de Marc Chagall", "Au cimetière, à l'extrémité sud du village. Les visiteurs y déposent des petits cailloux, selon la tradition."),
            ("La place du jeu de boules", "À l'entrée du village, sous les platanes : on y joue à la pétanque depuis toujours. Un moment simple et très provençal."),
        ],
        "y_aller": [
            ("En car depuis Nice", "Des cars régionaux relient Nice à Saint-Paul-de-Vence, avec un arrêt au pied du village. Comptez environ une heure."),
            ("En voiture ou en chauffeur", "Le village est piéton ; des parkings payants l'entourent, souvent pleins en été. Saint-Paul se combine facilement avec Vence ou Grasse."),
        ],
        "fiche": [
            ("Durée conseillée", "Une demi-journée, une journée avec la Fondation"),
            ("Meilleur moment", "Le printemps et l'automne"),
            ("À éviter", "Le milieu de journée en juillet-août"),
            ("Pour qui", "Amateurs d'art et de vieilles pierres"),
        ],
        "conseils": [
            "Visitez la Fondation Maeght le matin et le village en fin de journée, quand la lumière dore les remparts et que les groupes sont partis.",
            "Les ruelles sont pavées et pentues : chaussures plates conseillées.",
            "La plupart des galeries vendent des œuvres originales ; on peut entrer et regarder sans acheter.",
        ],
        "activites": [
            ("Excursions Saint-Paul-de-Vence", "Villages perchés de l'arrière-pays, souvent combinés avec Grasse ou Èze.", "Saint-Paul-de-Vence"),
            ("Grasse et les villages perchés", "Journées entre parfumeries et villages de caractère.", "Grasse villages perches"),
        ],
        "faq": [
            ("Saint-Paul-de-Vence est-il accessible en fauteuil ?", "Le village est en pente et pavé, l'accès est difficile. La Fondation Maeght est plus facile d'accès."),
            ("Faut-il réserver la Fondation Maeght ?", "Ce n'est pas obligatoire en général, mais c'est conseillé en haute saison et pendant les grandes expositions."),
            ("Peut-on combiner Saint-Paul-de-Vence et Èze dans la journée ?", "Oui, en voiture ou avec un chauffeur. Sans voiture, c'est plus compliqué : les deux villages sont desservis par des lignes différentes depuis Nice."),
        ],
    },
    {
        "slug": "saint-tropez",
        "region": "cote-d-azur",
        "nom": "Saint-Tropez",
        "dept": "83",
        "cachet": "Var",
        "couleur": "azur",
        "titre_seo": "Visiter Saint-Tropez : que voir, comment y aller sans bouchons | Clic&Site",
        "description": "Visiter Saint-Tropez : le port, la citadelle, le marché des Lices, le musée de l'Annonciade et Pampelonne. Comment y aller en bateau pour éviter les bouchons.",
        "accroche": "Un ancien village de pêcheurs devenu légende. Hors saison, Saint-Tropez redevient un petit port provençal ; en été, mieux vaut y arriver par la mer.",
        "intro": [
            "Saint-Tropez, c'est d'abord un port : façades colorées, terrasses et yachts au pied de la vieille ville. Derrière, les ruelles de la Ponche, quartier des pêcheurs, descendent jusqu'à une petite plage.",
            "La presqu'île est réputée pour ses plages, surtout Pampelonne, sur la commune voisine de Ramatuelle. En juillet et août, la route d'accès est l'une des plus encombrées de France : le bateau change tout.",
        ],
        "a_voir": [
            ("Le Vieux-Port", "Le spectacle permanent de Saint-Tropez. Allez-y tôt le matin pour voir le port avant la foule, ou à l'heure de l'apéritif pour l'ambiance."),
            ("La Citadelle", "Sur les hauteurs, la forteresse du XVIIe siècle abrite le musée d'histoire maritime. La vue sur le golfe et la ville est la plus belle de Saint-Tropez."),
            ("Le marché de la place des Lices", "Le mardi et le samedi matin, sous les platanes : produits provençaux, fleurs, vêtements. Le rendez-vous des Tropéziens."),
            ("Le musée de l'Annonciade", "Une ancienne chapelle au bord du port, qui abrite une collection de peintres qui ont aimé Saint-Tropez, de Signac à Matisse."),
            ("Le quartier de la Ponche", "L'ancien quartier des pêcheurs, ses ruelles et sa petite plage, à deux pas du port."),
            ("Les plages de Pampelonne", "Plusieurs kilomètres de sable sur la commune de Ramatuelle, entre plages publiques et établissements privés."),
        ],
        "y_aller": [
            ("En bateau", "La meilleure solution en saison. Des navettes relient Saint-Tropez à Sainte-Maxime toute l'année, et en été à Saint-Raphaël, Cannes ou Nice. On débarque directement au port."),
            ("En car", "Il n'y a pas de gare à Saint-Tropez. Des cars régionaux partent de Saint-Raphaël et de Toulon, mais ils sont pris dans les bouchons en été."),
            ("En voiture ou en chauffeur", "Hors saison, la route est agréable. En juillet-août, comptez parfois des heures de bouchons à l'entrée de la presqu'île : partez très tôt ou rentrez tard."),
        ],
        "fiche": [
            ("Durée conseillée", "Une journée"),
            ("Meilleur moment", "Mai-juin et septembre"),
            ("À éviter", "Les week-ends de juillet-août en voiture"),
            ("Pour qui", "Flâneurs, amateurs de plages et de marchés"),
        ],
        "conseils": [
            "Venez un mardi ou un samedi pour profiter du marché des Lices.",
            "En été, privilégiez le bateau depuis Sainte-Maxime ou Cannes : c'est plus rapide et bien plus agréable.",
            "Montez à la Citadelle en fin d'après-midi pour la lumière sur le golfe.",
        ],
        "activites": [
            ("Excursions à Saint-Tropez", "Journées en bateau ou en minibus au départ de Cannes, Nice ou Sainte-Maxime.", "Saint-Tropez"),
            ("Bateaux et croisières dans le golfe", "Balades en mer, tour des villas, sorties à la journée.", "Saint-Tropez bateau"),
        ],
        "faq": [
            ("Comment aller à Saint-Tropez sans voiture ?", "Le plus simple est le bateau, depuis Sainte-Maxime toute l'année ou depuis Cannes, Nice et Saint-Raphaël en saison. Il n'y a pas de gare."),
            ("Quel jour a lieu le marché de Saint-Tropez ?", "Le marché de la place des Lices se tient le mardi et le samedi matin."),
            ("La plage de Pampelonne est-elle à Saint-Tropez ?", "Elle est sur la commune voisine de Ramatuelle, à quelques kilomètres du centre de Saint-Tropez."),
        ],
    },
]
