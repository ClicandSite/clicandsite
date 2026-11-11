# Région Paris — édition française (11/11/2026).
# Faits vérifiés le 11/11/2026 sur les sites officiels et la presse. Règle : pas de prix, peu d'horaires.

REGION = {
    "slug": "paris",
    "nom": "Paris",
    "timbre": "Île-de-France",
    "photo": "paris",
    "photo_alt": "La tour Eiffel et les toits de Paris",
    "description": "Tour Eiffel, Louvre, Notre-Dame, Sainte-Chapelle, Montmartre, Orsay, Versailles : nos guides pour visiter Paris, ce qu'il faut réserver et quand y aller.",
    "accroche": "Paris se visite toute l'année, et l'hiver est même la meilleure saison pour les musées. Encore faut-il savoir ce qui se réserve, quel jour tout est fermé et à quelle heure passer.",
    "intro": [
        "Paris est la ville la plus visitée au monde, et cela se sent : la plupart des grands sites demandent aujourd'hui de réserver un créneau horaire, même quand l'entrée est gratuite. Bonne nouvelle, presque tout se rejoint en métro en moins d'une demi-heure, et les grands monuments sont regroupés le long de la Seine.",
        "Retenez trois jours de fermeture : le Louvre ferme le mardi, Orsay et Versailles le lundi. De novembre à mars, les files raccourcissent, plusieurs monuments sont gratuits le premier dimanche du mois et les nocturnes des musées permettent de finir la journée au chaud. Chaque guide ci-dessous vous dit quoi réserver, comment y aller et à quel moment.",
    ],
    "h1": "Visiter Paris", "de": "de Paris", "autres": "Autres sites à Paris", "couleur": "encre",
    "locality": "Paris", "address_region": "Île-de-France",
    "departements": ["75", "78"],
}

GROUPES = [
    ("monuments", "Monuments et panoramas"),
    ("musees", "Musées et châteaux"),
    ("quartiers", "Quartiers et balades"),
]

VEDETTES = ["tour-eiffel", "louvre", "notre-dame", "montmartre", "musee-d-orsay", "versailles"]

def _d(**k):
    k.setdefault("region", "paris")
    k.setdefault("dept", "75")
    k.setdefault("cachet", "Paris")
    return k

DESTINATIONS = [
    _d(slug="tour-eiffel", groupe="monuments", nom="Tour Eiffel", couleur="encre", h1="Visiter la tour Eiffel",
       description="Visiter la tour Eiffel : réserver ses billets, monter à pied ou en ascenseur, accéder au sommet, les meilleurs points de vue et comment y aller.",
       accroche="Trois étages, plus de 300 mètres et la vue la plus célèbre de Paris. La visite se prépare : billets officiels, bon créneau et, si vous avez les jambes, les escaliers.",
       intro=[
           "Construite par Gustave Eiffel pour l'Exposition universelle de 1889, la tour devait être démontée vingt ans plus tard. Elle se visite sur trois niveaux : le 1er étage et son plancher de verre, le 2e étage, d'où la vue est la plus lisible, et le sommet, réservé à l'ascenseur.",
           "On peut monter à pied jusqu'au 2e étage, soit 674 marches, puis prendre l'ascenseur pour le sommet. Dans tous les cas, achetez vos billets sur le site officiel : de faux sites de billetterie imitent la tour et vendent des billets inutilisables.",
       ],
       a_voir=[
           ("Le 1er étage et son plancher de verre", "Le niveau le plus vaste, avec un sol vitré à 57 mètres au-dessus du vide et des panneaux qui racontent la construction. C'est aussi l'étage le moins chargé."),
           ("Le 2e étage", "Pour beaucoup, la plus belle vue : assez haut pour embrasser Paris, assez bas pour reconnaître chaque monument, de Montmartre aux Invalides."),
           ("Le sommet", "Accessible uniquement en ascenseur depuis le 2e étage. On y voit le bureau reconstitué de Gustave Eiffel et, par temps clair, des dizaines de kilomètres à la ronde."),
           ("Le scintillement du soir", "Chaque heure après la tombée de la nuit, la tour scintille pendant cinq minutes. Le spectacle se regarde mieux d'en bas que d'en haut."),
           ("Le Trocadéro et le Champ-de-Mars", "Les deux esplanades qui encadrent la tour offrent les photos classiques : le Trocadéro face à la tour, le Champ-de-Mars pour la voir de toute sa hauteur."),
       ],
       y_aller=[
           ("En métro et en RER", "Stations Bir-Hakeim (ligne 6) et Trocadéro (lignes 6 et 9), ou gare Champ de Mars - Tour Eiffel sur le RER C. Le Trocadéro permet d'arriver par la plus belle vue."),
           ("En bateau", "Les bateaux de la Seine et le Batobus s'arrêtent au pied de la tour, ce qui permet de combiner la visite avec une croisière."),
           ("En taxi ou en chauffeur", "La circulation et l'arrêt sont difficiles aux abords immédiats ; demandez à être déposé quai Branly ou côté Trocadéro."),
       ],
       fiche=[("Durée conseillée", "2 à 3 heures"), ("Meilleur moment", "À l'ouverture, ou au coucher du soleil"), ("À réserver", "Oui, sur le site officiel"), ("Pour qui", "Tout le monde ; escaliers pour les bons marcheurs")],
       conseils=[
           "Réservez le plus tôt possible : les créneaux du sommet partent vite pendant les vacances scolaires.",
           "Par temps couvert, inutile de payer le sommet : le 2e étage suffit et la vue y est meilleure sous les nuages.",
           "Les contrôles de sécurité prennent du temps ; arrivez avec un sac léger et un peu d'avance sur votre créneau.",
       ],
       activites=[
           ("Billets et visites de la tour Eiffel", "Accès au sommet, montée guidée, visites avec coupe-file.", "Tour Eiffel"),
           ("Tour Eiffel et croisière sur la Seine", "Formules combinées avec un bateau au pied de la tour.", "Tour Eiffel croisière Seine"),
       ],
       faq=[
           ("Faut-il réserver pour monter à la tour Eiffel ?", "C'est fortement conseillé, et la montée par les escaliers se réserve désormais aussi. Achetez uniquement sur le site officiel ou chez un revendeur reconnu."),
           ("Peut-on monter au sommet à pied ?", "Non. Les escaliers mènent au 2e étage (674 marches) ; le sommet ne se rejoint qu'en ascenseur depuis le 2e."),
           ("À quelle heure la tour Eiffel scintille-t-elle ?", "Chaque heure après la tombée de la nuit, pendant cinq minutes, jusqu'à la fermeture."),
       ]),

    _d(slug="louvre", groupe="musees", nom="Louvre", couleur="ocre", h1="Visiter le musée du Louvre",
       description="Visiter le Louvre : réservation obligatoire, jour de fermeture, nocturnes, entrées, parcours pour voir la Joconde et les chefs-d'œuvre sans s'épuiser.",
       accroche="Le plus grand musée du monde ne se visite pas en entier : il se prépare. Réservez votre créneau, choisissez trois ou quatre ailes et évitez le mardi, jour de fermeture.",
       intro=[
           "Ancien palais des rois de France, le Louvre réunit des collections allant de l'Antiquité au XIXe siècle, réparties dans trois ailes : Denon, Sully et Richelieu. La Joconde, la Vénus de Milo et la Victoire de Samothrace en sont les vedettes, mais elles ne représentent qu'une infime partie de ce qu'on peut voir.",
           "La réservation d'un créneau horaire est obligatoire, y compris pour les visiteurs qui entrent gratuitement. Le musée est fermé le mardi et ouvre en nocturne le mercredi et le vendredi, deux soirées où il est souvent plus calme.",
       ],
       a_voir=[
           ("La Joconde", "Dans la salle des États, aile Denon. La file se forme devant le tableau : allez-y en premier à l'ouverture, ou en fin de nocturne."),
           ("La Victoire de Samothrace", "En haut de l'escalier Daru, l'une des mises en scène les plus spectaculaires du musée."),
           ("La Vénus de Milo", "Dans les salles grecques de l'aile Sully, au rez-de-chaussée."),
           ("Les grands formats français", "Le Radeau de la Méduse, La Liberté guidant le peuple, Le Sacre de Napoléon : la galerie des grands tableaux de l'aile Denon, juste à côté de la Joconde."),
           ("Les appartements Napoléon III", "Dorures, lustres et salons d'apparat dans l'aile Richelieu, souvent moins fréquentés."),
           ("La Pyramide et la cour Napoléon", "La pyramide de verre d'Ieoh Ming Pei, à admirer de l'extérieur, de jour comme de nuit."),
       ],
       y_aller=[
           ("En métro", "Station Palais-Royal - Musée du Louvre (lignes 1 et 7). La station Louvre - Rivoli, sur la ligne 1, est un peu plus loin."),
           ("Par quelle entrée ?", "L'entrée principale est sous la Pyramide. L'entrée du Carrousel, par le 99 rue de Rivoli, est couverte : pratique par temps de pluie. Suivez les indications de votre billet."),
           ("À pied", "Le musée est à quelques minutes du Pont des Arts, des Tuileries et de l'île de la Cité."),
       ],
       fiche=[("Durée conseillée", "3 heures à une journée"), ("Fermé", "Le mardi"), ("Nocturnes", "Mercredi et vendredi"), ("À réserver", "Oui, obligatoire")],
       conseils=[
           "Choisissez votre parcours avant d'entrer : trois heures bien préparées valent mieux qu'une journée à errer.",
           "Gardez la Joconde pour l'ouverture ou la fin de nocturne ; le reste du musée est bien plus calme.",
           "Cafés et restaurants se trouvent à l'intérieur du musée : prévoyez une vraie pause pour tenir la distance.",
       ],
       activites=[
           ("Visites guidées du Louvre", "Parcours chefs-d'œuvre en petit groupe, avec billet inclus.", "Louvre visite guidée"),
           ("Billets d'entrée au Louvre", "Billets à créneau horaire et formules combinées.", "Musée du Louvre billet"),
       ],
       faq=[
           ("Quel jour le Louvre est-il fermé ?", "Le mardi, ainsi que quelques jours fériés. Il ouvre en nocturne le mercredi et le vendredi."),
           ("Faut-il réserver pour le Louvre ?", "Oui, la réservation d'un créneau horaire est obligatoire pour tous les visiteurs, même ceux qui entrent gratuitement."),
           ("Combien de temps faut-il pour visiter le Louvre ?", "Comptez trois heures pour les grands chefs-d'œuvre. Une journée entière ne suffit pas à tout voir : mieux vaut revenir."),
       ]),

    _d(slug="notre-dame", groupe="monuments", nom="Notre-Dame", couleur="azur", h1="Visiter Notre-Dame de Paris",
       description="Visiter Notre-Dame de Paris depuis sa réouverture : entrée gratuite, réservation conseillée, tours et crypte, horaires de la nocturne, comment y aller.",
       accroche="Rouverte en décembre 2024 après l'incendie, la cathédrale a retrouvé sa pierre claire et sa lumière. L'entrée est gratuite ; réserver un créneau fait gagner beaucoup de temps.",
       intro=[
           "Restaurée en cinq ans après l'incendie d'avril 2019, Notre-Dame a rouvert ses portes en décembre 2024. La nef, nettoyée de plusieurs siècles de poussière, est plus lumineuse qu'elle ne l'a jamais été de mémoire de Parisien, et la flèche de Viollet-le-Duc a été reconstruite à l'identique.",
           "L'entrée dans la cathédrale est gratuite. Un système de réservation gratuite, ouvert deux à trois jours à l'avance, permet d'éviter la file d'attente ; il est surtout utile d'avril à octobre. La montée aux tours et la crypte archéologique se paient à part.",
       ],
       a_voir=[
           ("La nef et le chœur", "Le nouveau mobilier liturgique, les rosaces et les chapelles latérales restaurées. Prenez le temps de lever les yeux vers les voûtes."),
           ("Les rosaces", "Les trois grandes rosaces médiévales ont traversé l'incendie. La rosace sud est la plus lumineuse en fin de matinée."),
           ("Les tours", "Après plusieurs centaines de marches, la galerie des chimères et la vue sur l'île de la Cité. Billet et réservation à part."),
           ("La crypte archéologique", "Sous le parvis, les vestiges de la Lutèce antique et du Paris médiéval."),
           ("Le square Jean-XXIII", "Derrière la cathédrale, le meilleur point de vue sur le chevet et les arcs-boutants."),
       ],
       y_aller=[
           ("En métro et en RER", "Station Cité (ligne 4), ou gare Saint-Michel - Notre-Dame (RER B et C). La cathédrale est à quelques minutes à pied."),
           ("À pied", "Depuis le Quartier latin, le Marais ou le Louvre, on rejoint l'île de la Cité par les ponts en un quart d'heure."),
       ],
       fiche=[("Durée conseillée", "1 heure, 2 avec les tours"), ("Entrée", "Gratuite"), ("À réserver", "Conseillé, gratuit"), ("Ouvert", "Tous les jours, nocturne le jeudi")],
       conseils=[
           "Réservez votre créneau gratuit dès son ouverture, deux à trois jours avant : les places partent vite.",
           "Combinez avec la Sainte-Chapelle, à cinq minutes à pied sur la même île.",
           "Une tenue correcte est demandée ; les offices se déroulent pendant les visites, restez discret.",
       ],
       activites=[
           ("Visites guidées de Notre-Dame et de l'île de la Cité", "Histoire de la cathédrale, de l'incendie et de la restauration.", "Notre-Dame visite guidée"),
           ("Notre-Dame, Sainte-Chapelle et Conciergerie", "Formules combinées pour découvrir l'île de la Cité en une demi-journée.", "Notre-Dame Sainte-Chapelle"),
       ],
       faq=[
           ("L'entrée de Notre-Dame est-elle payante ?", "Non, l'entrée dans la cathédrale est gratuite. Seules les tours et la crypte archéologique sont payantes."),
           ("Faut-il réserver pour entrer dans Notre-Dame ?", "Ce n'est pas obligatoire, mais la réservation gratuite d'un créneau évite une longue attente, surtout d'avril à octobre."),
           ("Peut-on monter aux tours de Notre-Dame ?", "Oui, avec un billet payant et une réservation. Il faut gravir plusieurs centaines de marches, sans ascenseur."),
       ]),

    _d(slug="sainte-chapelle", groupe="monuments", nom="Sainte-Chapelle", couleur="pin", h1="Visiter la Sainte-Chapelle",
       description="Visiter la Sainte-Chapelle à Paris : réservation d'un créneau obligatoire, contrôle de sécurité, meilleur moment pour les vitraux, billet avec la Conciergerie.",
       accroche="Quinze verrières, plus de mille scènes de vitrail et presque pas de murs. Par un jour de soleil, la chapelle haute est l'un des plus beaux intérieurs du monde.",
       intro=[
           "Saint Louis fait construire la Sainte-Chapelle au XIIIe siècle pour abriter la couronne d'épines. Elle se trouve aujourd'hui au milieu du Palais de justice, sur l'île de la Cité, ce qui explique le contrôle de sécurité à l'entrée, comparable à celui d'un aéroport.",
           "La réservation d'un créneau horaire est obligatoire, même pour les visiteurs qui entrent gratuitement. Le créneau reste valable une demi-heure. Un billet combiné donne aussi accès à la Conciergerie voisine, l'ancien palais devenu prison de Marie-Antoinette.",
       ],
       a_voir=[
           ("La chapelle haute", "Le cœur de la visite : quinze immenses verrières qui racontent la Bible, de la Genèse à la Passion. La rose occidentale, plus tardive, représente l'Apocalypse."),
           ("La chapelle basse", "Réservée autrefois au personnel du palais, avec sa voûte bleue semée de fleurs de lys."),
           ("La Conciergerie", "Juste à côté, la grande salle gothique des gens d'armes et le cachot reconstitué de Marie-Antoinette."),
       ],
       y_aller=[
           ("En métro et en RER", "Station Cité (ligne 4), à deux minutes, ou gare Saint-Michel - Notre-Dame (RER B et C), de l'autre côté du pont."),
           ("Par quelle entrée ?", "L'entrée des visiteurs se fait boulevard du Palais, par le contrôle de sécurité du Palais de justice. Les grosses valises sont refusées."),
       ],
       fiche=[("Durée conseillée", "45 minutes à 1 heure"), ("Meilleur moment", "Un jour de soleil, en fin de matinée"), ("À réserver", "Oui, obligatoire"), ("Pour qui", "Tout le monde ; ascenseur sur demande")],
       conseils=[
           "Choisissez un jour ensoleillé si vous pouvez : les vitraux changent complètement avec la lumière.",
           "Arrivez une vingtaine de minutes avant votre créneau pour passer la sécurité sans stress.",
           "En soirée, des concerts de musique classique ont lieu dans la chapelle haute : une autre façon de la découvrir.",
       ],
       activites=[
           ("Billets Sainte-Chapelle et Conciergerie", "Entrée à créneau horaire et billet combiné.", "Sainte-Chapelle billet"),
           ("Concerts à la Sainte-Chapelle", "Musique classique sous les vitraux, le soir.", "Sainte-Chapelle concert"),
       ],
       faq=[
           ("Faut-il réserver la Sainte-Chapelle ?", "Oui, un créneau horaire est obligatoire pour tous, y compris pour l'entrée gratuite et le Paris Museum Pass."),
           ("Combien de temps dure la visite ?", "Comptez 45 minutes à une heure, plus le temps du contrôle de sécurité, et une heure de plus avec la Conciergerie."),
           ("La Sainte-Chapelle est-elle gratuite le premier dimanche du mois ?", "Oui, de novembre à mars, mais la réservation d'un créneau reste obligatoire."),
       ]),

    _d(slug="montmartre", groupe="quartiers", nom="Montmartre", couleur="ocre", h1="Visiter Montmartre et le Sacré-Cœur",
       description="Visiter Montmartre : le Sacré-Cœur et son dôme, la place du Tertre, les vignes, le musée de Montmartre. Comment monter sur la butte et éviter les pièges.",
       accroche="Une colline de village au-dessus de Paris : escaliers, vignes, ateliers de peintres et, tout en haut, la basilique blanche du Sacré-Cœur.",
       intro=[
           "Montmartre est le point le plus haut de Paris. Ancien village de moulins et de vignes, il a attiré à la fin du XIXe siècle Renoir, Picasso, Toulouse-Lautrec et Van Gogh. La place du Tertre est devenue très touristique, mais les rues de l'autre versant ont gardé leur calme.",
           "L'entrée de la basilique du Sacré-Cœur est gratuite. La montée au dôme est payante : environ 300 marches, sans ascenseur, pour l'un des plus beaux panoramas de la ville. Le funiculaire évite l'escalier du square Louise-Michel avec un simple ticket de métro.",
       ],
       a_voir=[
           ("La basilique du Sacré-Cœur", "Entrée libre, avec l'une des plus grandes mosaïques de France au-dessus du chœur. Le parvis offre une vue sur tout Paris."),
           ("Le dôme", "Environ 300 marches en colimaçon, puis une galerie à ciel ouvert autour de la coupole : la vue la plus haute de Paris après la tour Eiffel."),
           ("La place du Tertre", "Les peintres et portraitistes au travail. Très fréquentée l'après-midi ; plus agréable tôt le matin."),
           ("Le musée de Montmartre", "Dans la plus vieille maison de la butte, avec l'atelier de Suzanne Valadon et les jardins Renoir."),
           ("Les vignes et la rue de l'Abreuvoir", "Le Clos Montmartre, la Maison Rose et les rues pavées du versant nord, beaucoup plus calmes."),
           ("Le mur des Je t'aime", "Dans le square Jehan-Rictus, place des Abbesses : « je t'aime » écrit dans des centaines de langues."),
       ],
       y_aller=[
           ("En métro", "Station Anvers (ligne 2) pour le funiculaire et le Sacré-Cœur, ou Abbesses (ligne 12) pour monter par les rues du village."),
           ("En funiculaire", "Il relie le bas de la butte au parvis du Sacré-Cœur avec un ticket de métro ordinaire."),
           ("À pied", "Depuis Abbesses, comptez un quart d'heure de montée par la rue des Abbesses et la rue Lepic."),
       ],
       fiche=[("Durée conseillée", "Une demi-journée"), ("Meilleur moment", "Tôt le matin, ou au coucher du soleil"), ("Entrée du Sacré-Cœur", "Gratuite"), ("Pour qui", "Bons marcheurs ; funiculaire pour les autres")],
       conseils=[
           "Montez par Abbesses et redescendez par l'escalier du Sacré-Cœur : la montée est plus douce et plus jolie.",
           "Au pied des escaliers, ignorez les vendeurs qui vous nouent un bracelet au poignet, et surveillez vos poches dans la foule.",
           "Le coucher du soleil sur le parvis est un grand moment, mais tout le monde a la même idée : arrivez tôt.",
       ],
       activites=[
           ("Visites guidées de Montmartre", "Balades à pied sur les traces des peintres, en petit groupe.", "Montmartre visite guidée"),
           ("Montmartre gourmand", "Visites dégustation : fromages, vins et boulangeries de la butte.", "Montmartre food tour"),
       ],
       faq=[
           ("L'entrée du Sacré-Cœur est-elle gratuite ?", "Oui. Seule la montée au dôme est payante."),
           ("Y a-t-il un ascenseur pour le dôme du Sacré-Cœur ?", "Non, il faut monter environ 300 marches en colimaçon."),
           ("Comment monter au Sacré-Cœur sans escaliers ?", "Prenez le funiculaire depuis la station Anvers : il fonctionne avec un ticket de métro."),
       ]),

    _d(slug="musee-d-orsay", groupe="musees", nom="Musée d'Orsay", couleur="azur", h1="Visiter le musée d'Orsay",
       description="Visiter le musée d'Orsay : les impressionnistes, l'horloge, jour de fermeture, nocturne du jeudi, réservation conseillée et comment y aller.",
       accroche="Monet, Renoir, Van Gogh, Degas : la plus grande collection impressionniste du monde, dans une ancienne gare. La nocturne du jeudi est le meilleur moment pour y aller.",
       intro=[
           "Installé dans la gare d'Orsay, construite pour l'Exposition universelle de 1900, le musée couvre l'art de 1848 à 1914. La grande nef sous verrière accueille les sculptures ; les impressionnistes sont au 5e étage, sous les toits.",
           "Le musée est fermé le lundi et ouvre en nocturne le jeudi soir. La réservation d'un créneau en ligne est fortement conseillée. Des travaux de rénovation des espaces d'accueil sont en cours jusqu'en 2028, sans fermeture des collections.",
       ],
       a_voir=[
           ("La galerie impressionniste", "Au 5e étage : Monet, Renoir, Pissarro, Sisley, Degas, Caillebotte. Le cœur du musée."),
           ("Van Gogh et Gauguin", "Les salles postimpressionnistes, avec La Nuit étoilée sur le Rhône et l'autoportrait de Van Gogh."),
           ("Les horloges", "Les deux grandes horloges de l'ancienne gare : de l'intérieur, on voit Paris et le Sacré-Cœur à travers le cadran."),
           ("La nef", "La perspective sous la verrière, avec les sculptures de Carpeaux et de Rodin."),
           ("Le restaurant", "L'ancienne salle à manger de l'hôtel de la gare, avec ses dorures et ses lustres."),
       ],
       y_aller=[
           ("En RER et en métro", "Gare Musée d'Orsay (RER C), juste devant, ou station Solférino (ligne 12), à cinq minutes."),
           ("À pied", "Depuis le Louvre, traversez la passerelle Léopold-Sédar-Senghor : dix minutes de marche."),
       ],
       fiche=[("Durée conseillée", "2 à 3 heures"), ("Fermé", "Le lundi"), ("Nocturne", "Le jeudi soir"), ("À réserver", "Fortement conseillé")],
       conseils=[
           "Allez-y le jeudi soir : moins de monde et un tarif réduit en fin de journée.",
           "Commencez par le 5e étage, avant que les salles impressionnistes ne se remplissent.",
           "Prolongez avec le musée de l'Orangerie et les Nymphéas de Monet, de l'autre côté de la Seine : un billet jumelé existe.",
       ],
       activites=[
           ("Billets et visites du musée d'Orsay", "Billets à créneau horaire et visites guidées des impressionnistes.", "Musée d'Orsay"),
           ("Orsay et Orangerie", "Formules combinées pour les deux musées impressionnistes.", "Orsay Orangerie"),
       ],
       faq=[
           ("Quel jour le musée d'Orsay est-il fermé ?", "Le lundi, ainsi que le 1er mai et le 25 décembre."),
           ("Jusqu'à quelle heure ouvre la nocturne d'Orsay ?", "Le jeudi, le musée reste ouvert jusqu'en soirée, avec une dernière entrée environ 45 minutes avant la fermeture."),
           ("Faut-il réserver pour le musée d'Orsay ?", "Ce n'est pas obligatoire, mais c'est fortement conseillé : les billets achetés sur place ne garantissent pas l'entrée les jours d'affluence."),
       ]),

    _d(slug="arc-de-triomphe", groupe="monuments", nom="Arc de Triomphe", couleur="encre", h1="Visiter l'Arc de Triomphe",
       description="Visiter l'Arc de Triomphe : la terrasse et ses 284 marches, la tombe du Soldat inconnu, le ravivage de la flamme, comment y accéder et les Champs-Élysées.",
       accroche="Au sommet des Champs-Élysées, 284 marches mènent à une terrasse d'où partent douze avenues en étoile. C'est l'une des vues les plus graphiques de Paris.",
       intro=[
           "Napoléon commande l'Arc de Triomphe en 1806 pour célébrer la Grande Armée. Sous la voûte repose depuis 1921 le Soldat inconnu, et la flamme du souvenir y est ravivée chaque soir lors d'une courte cérémonie.",
           "Le pied du monument et la tombe sont en accès libre. La terrasse, à 50 mètres de hauteur, se rejoint par un escalier de 284 marches ; l'ascenseur est réservé aux personnes à mobilité réduite. On y accède uniquement par le passage souterrain : ne traversez jamais le rond-point.",
       ],
       a_voir=[
           ("La terrasse", "La vue sur les douze avenues de la place de l'Étoile, l'axe historique jusqu'au Louvre et, de l'autre côté, la Défense."),
           ("La tombe du Soldat inconnu", "Sous la voûte, avec la flamme ravivée chaque soir à 18 h 30."),
           ("Les sculptures", "Le Départ des volontaires de 1792, dit La Marseillaise, de François Rude, sur le pilier côté Champs-Élysées."),
           ("Les Champs-Élysées", "Deux kilomètres jusqu'à la Concorde. En décembre, les illuminations de Noël en font une des promenades les plus courues de Paris."),
       ],
       y_aller=[
           ("En métro et en RER", "Station Charles de Gaulle - Étoile (lignes 1, 2, 6 et RER A). Suivez la sortie Arc de Triomphe pour arriver directement au passage souterrain."),
           ("À pied", "Remontez les Champs-Élysées depuis la Concorde : une demi-heure de marche."),
       ],
       fiche=[("Durée conseillée", "1 heure"), ("Meilleur moment", "Fin d'après-midi, puis la flamme"), ("Terrasse", "284 marches"), ("Gratuit", "1er dimanche du mois, de novembre à mars")],
       conseils=[
           "Montez une heure avant le coucher du soleil et redescendez pour le ravivage de la flamme.",
           "Achetez votre billet en ligne : l'attente se résume alors au contrôle de sécurité.",
           "Le 11 novembre, le 8 mai et le 14 juillet, l'accès est restreint pendant les cérémonies : vérifiez avant de venir.",
       ],
       activites=[
           ("Billets pour la terrasse de l'Arc de Triomphe", "Entrée à la terrasse panoramique.", "Arc de Triomphe"),
           ("Champs-Élysées et Arc de Triomphe en visite guidée", "Balades commentées et bus panoramiques.", "Champs-Élysées visite"),
       ],
       faq=[
           ("Combien de marches pour monter en haut de l'Arc de Triomphe ?", "284 marches. L'ascenseur est réservé aux personnes à mobilité réduite."),
           ("Comment accéder à l'Arc de Triomphe ?", "Par le passage souterrain depuis le haut des Champs-Élysées ou l'avenue de la Grande-Armée. Ne traversez pas le rond-point, c'est dangereux et interdit."),
           ("À quelle heure est ravivée la flamme ?", "Chaque soir à 18 h 30, sous la voûte. La cérémonie est publique et gratuite."),
       ]),

    _d(slug="opera-garnier", groupe="monuments", nom="Opéra Garnier", couleur="ocre", h1="Visiter l'Opéra Garnier",
       description="Visiter l'Opéra Garnier : le grand escalier, le grand foyer, le plafond de Chagall, billets à créneau horaire, horaires et conseils de visite.",
       accroche="Marbre, dorures et plafond de Chagall : le Palais Garnier est le décor le plus fastueux de Paris, et il se visite librement en journée.",
       intro=[
           "Inauguré en 1875, le Palais Garnier est le chef-d'œuvre du Second Empire. On y vient pour le grand escalier, le grand foyer, digne de la galerie des Glaces, et, si aucune répétition n'a lieu, pour la salle et son plafond peint par Marc Chagall.",
           "La visite libre se fait avec un billet à créneau horaire, tous les jours en journée, sauf fermetures exceptionnelles liées aux spectacles. Les valises et grands sacs ne sont pas acceptés.",
       ],
       a_voir=[
           ("Le grand escalier", "Double volée de marbre blanc, rampes d'onyx et lustres : le cœur du palais."),
           ("Le grand foyer", "Une galerie dorée de près de 50 mètres, avec ses miroirs et ses plafonds peints."),
           ("La salle et le plafond de Chagall", "Visible depuis une loge quand aucune répétition n'a lieu ; le lustre pèse plusieurs tonnes."),
           ("La bibliothèque-musée", "Maquettes de décors, costumes et souvenirs de l'histoire de l'Opéra de Paris."),
           ("La terrasse des Galeries Lafayette", "À deux minutes, une terrasse gratuite avec vue sur le toit de l'Opéra et tout Paris."),
       ],
       y_aller=[
           ("En métro", "Station Opéra (lignes 3, 7 et 8), juste devant ; RER A à Auber, à deux minutes."),
           ("À pied", "Depuis le Louvre, remontez l'avenue de l'Opéra : un quart d'heure."),
       ],
       fiche=[("Durée conseillée", "1 h 30"), ("Ouvert", "Tous les jours, en journée"), ("À réserver", "Conseillé, billet à créneau"), ("Pour qui", "Tout le monde")],
       conseils=[
           "Venez en début de matinée : le grand escalier est bien plus photogénique sans la foule.",
           "Consultez le calendrier avant de venir : certains jours, la salle n'est pas visible à cause des répétitions.",
           "Le meilleur moyen de voir la salle reste d'assister à un ballet : les places à visibilité réduite sont abordables.",
       ],
       activites=[
           ("Billets et visites guidées du Palais Garnier", "Visite libre à créneau horaire ou visite guidée.", "Opéra Garnier"),
           ("Opéra Garnier et quartier des grands magasins", "Balades guidées entre l'Opéra et le boulevard Haussmann.", "Opéra Garnier visite guidée"),
       ],
       faq=[
           ("Peut-on visiter l'Opéra Garnier sans voir de spectacle ?", "Oui, la visite libre est ouverte tous les jours en journée, sauf fermetures exceptionnelles."),
           ("Voit-on le plafond de Chagall pendant la visite ?", "Oui, depuis une loge, sauf quand une répétition ou un spectacle occupe la salle."),
           ("Combien de temps dure la visite de l'Opéra Garnier ?", "Comptez une heure et demie pour les espaces publics et l'exposition en cours."),
       ]),

    _d(slug="croisiere-sur-la-seine", groupe="quartiers", nom="Croisière sur la Seine", couleur="azur", h1="Faire une croisière sur la Seine",
       description="Croisière sur la Seine à Paris : quelle compagnie choisir, d'où partir, croisière de jour, au coucher du soleil ou avec dîner, Batobus et conseils.",
       accroche="Une heure sur l'eau, et Paris défile : Notre-Dame, le Louvre, Orsay, la tour Eiffel. C'est la meilleure façon de comprendre la ville le premier jour.",
       intro=[
           "La plupart des monuments de Paris sont alignés le long de la Seine, entre l'île Saint-Louis et la tour Eiffel. Une croisière commentée d'une heure environ permet de tous les voir en restant assis, avec un audioguide en plusieurs langues.",
           "Plusieurs compagnies partent du centre : les Bateaux-Mouches depuis le pont de l'Alma, les Bateaux Parisiens et les Vedettes de Paris depuis le pied de la tour Eiffel, les Vedettes du Pont-Neuf depuis l'île de la Cité. Le Batobus, lui, fonctionne comme un bus sur l'eau, avec un billet à la journée.",
       ],
       a_voir=[
           ("La croisière commentée", "Environ une heure, aller-retour entre la tour Eiffel et les îles. Pas besoin de réserver longtemps à l'avance hors saison."),
           ("La croisière au coucher du soleil", "La lumière dorée sur les façades, puis les monuments qui s'illuminent : le meilleur créneau."),
           ("La croisière dîner", "Pour une soirée particulière, avec un menu à bord. Réservez, surtout le week-end."),
           ("Le Batobus", "Une dizaine d'escales, on monte et on descend à volonté : pratique pour relier les musées sans métro."),
       ],
       y_aller=[
           ("Pont de l'Alma", "Métro Alma - Marceau (ligne 9) ou RER C Pont de l'Alma pour les Bateaux-Mouches."),
           ("Tour Eiffel", "Métro Bir-Hakeim (ligne 6) ou RER C Champ de Mars - Tour Eiffel pour les embarcadères du port de la Bourdonnais."),
           ("Pont-Neuf", "Métro Pont-Neuf (ligne 7) ou Cité (ligne 4) pour le square du Vert-Galant."),
       ],
       fiche=[("Durée", "1 heure environ"), ("Meilleur moment", "Au coucher du soleil"), ("À réserver", "Conseillé en été et pour les dîners"), ("Pour qui", "Tout le monde, idéal en famille")],
       conseils=[
           "Faites-la le premier jour : vous repérerez les monuments à visiter ensuite.",
           "Asseyez-vous à l'extérieur, sur le pont supérieur, et prenez une veste : il fait toujours plus frais sur l'eau.",
           "En hiver, lors des crues de la Seine, les bateaux peuvent être suspendus : vérifiez la veille.",
       ],
       activites=[
           ("Croisières commentées sur la Seine", "Une heure au départ de la tour Eiffel ou du pont de l'Alma.", "Croisière Seine Paris"),
           ("Dîners croisière sur la Seine", "Menus à bord, de la formule simple au dîner gastronomique.", "Dîner croisière Seine"),
       ],
       faq=[
           ("Quelle compagnie choisir pour une croisière sur la Seine ?", "Les grandes compagnies proposent des parcours très proches. Choisissez selon le point de départ le plus pratique pour vous : tour Eiffel, pont de l'Alma ou Pont-Neuf."),
           ("Combien de temps dure une croisière sur la Seine ?", "Une heure environ pour une croisière commentée, deux heures et demie pour un dîner croisière."),
           ("Les bateaux circulent-ils en hiver ?", "Oui, toute l'année, sauf en cas de crue de la Seine. Les bateaux sont chauffés et vitrés."),
       ]),

    _d(slug="le-marais", groupe="quartiers", nom="Le Marais", couleur="pin", h1="Visiter le Marais",
       description="Visiter le Marais à Paris : la place des Vosges, la maison de Victor Hugo, le musée Carnavalet, le musée Picasso, la rue des Rosiers et les boutiques du dimanche.",
       accroche="Hôtels particuliers du XVIIe siècle, musées gratuits, falafels et boutiques ouvertes le dimanche : le Marais est le quartier le plus agréable à parcourir à pied.",
       intro=[
           "Ancien quartier aristocratique, le Marais a conservé ses rues étroites et ses hôtels particuliers, dont beaucoup abritent aujourd'hui des musées. Il s'étend entre l'Hôtel de Ville, la place des Vosges et le quartier du Temple.",
           "C'est aussi l'un des rares quartiers de Paris où la plupart des boutiques ouvrent le dimanche. Deux grands musées y sont gratuits pour les collections permanentes : le musée Carnavalet, consacré à l'histoire de Paris, et la maison de Victor Hugo.",
       ],
       a_voir=[
           ("La place des Vosges", "La plus ancienne place royale de Paris, entourée d'arcades. Le jardin central est parfait pour une pause."),
           ("La maison de Victor Hugo", "L'appartement de l'écrivain, place des Vosges. Collections permanentes gratuites."),
           ("Le musée Carnavalet", "L'histoire de Paris, des origines à nos jours, dans deux hôtels particuliers. Gratuit pour les collections permanentes, fermé le lundi."),
           ("Le musée Picasso", "La plus grande collection publique d'œuvres de Picasso, dans l'hôtel Salé."),
           ("La rue des Rosiers", "Le cœur du quartier juif historique, célèbre pour ses falafels."),
           ("L'Hôtel de Ville", "La façade néo-Renaissance et, en hiver, sa patinoire éphémère sur le parvis."),
       ],
       y_aller=[
           ("En métro", "Stations Saint-Paul (ligne 1), Chemin Vert (ligne 8) pour la place des Vosges, ou Hôtel de Ville (lignes 1 et 11)."),
           ("À pied", "Depuis Notre-Dame, traversez l'île Saint-Louis : un quart d'heure jusqu'à la rue des Rosiers."),
       ],
       fiche=[("Durée conseillée", "Une demi-journée"), ("Meilleur moment", "Le dimanche ou en semaine le matin"), ("Musées gratuits", "Carnavalet, maison de Victor Hugo"), ("Pour qui", "Tout le monde, à pied")],
       conseils=[
           "Le dimanche, le quartier est très animé et les boutiques sont ouvertes ; la rue des Rosiers est plus calme le samedi, jour de shabbat.",
           "Le musée Carnavalet est fermé le lundi ; vérifiez avant de bâtir votre parcours autour.",
           "Poussez jusqu'au marché des Enfants-Rouges, le plus vieux marché couvert de Paris, pour déjeuner.",
       ],
       activites=[
           ("Visites guidées du Marais", "Balades historiques et visites du quartier juif.", "Marais visite guidée"),
           ("Le Marais gourmand", "Visites dégustation dans les boulangeries, fromageries et marchés.", "Marais food tour"),
       ],
       faq=[
           ("Les boutiques du Marais sont-elles ouvertes le dimanche ?", "Oui, la plupart des boutiques du quartier ouvrent le dimanche, ce qui en fait une sortie idéale ce jour-là."),
           ("Quels musées gratuits voir dans le Marais ?", "Le musée Carnavalet et la maison de Victor Hugo, gratuits pour leurs collections permanentes."),
           ("Comment aller dans le Marais ?", "En métro jusqu'à Saint-Paul (ligne 1) ou Chemin Vert (ligne 8), ou à pied depuis Notre-Dame."),
       ]),

    _d(slug="quartier-latin", groupe="quartiers", nom="Quartier latin et Luxembourg", couleur="pin", h1="Visiter le Quartier latin et le jardin du Luxembourg",
       description="Visiter le Quartier latin et le jardin du Luxembourg : le Panthéon, la Sorbonne, la rue Mouffetard, Shakespeare and Company, comment y aller.",
       accroche="Le Paris des étudiants et des librairies, du Panthéon au jardin du Luxembourg. Un quartier à parcourir à pied, entre deux cafés.",
       intro=[
           "Sur la rive gauche, face à l'île de la Cité, le Quartier latin doit son nom au latin parlé à la Sorbonne au Moyen Âge. Librairies, cinémas d'art et d'essai et cafés y côtoient le Panthéon, où reposent Voltaire, Victor Hugo et Marie Curie.",
           "Le jardin du Luxembourg, juste à côté, est le jardin préféré des Parisiens : allées de marronniers, fontaine Médicis, voiliers à pousser sur le grand bassin et chaises vertes en libre accès. L'entrée est gratuite.",
       ],
       a_voir=[
           ("Le jardin du Luxembourg", "Le palais du Sénat, le grand bassin, la fontaine Médicis et plus d'une centaine de statues."),
           ("Le Panthéon", "La nécropole des grands hommes et des grandes femmes, avec le pendule de Foucault sous la coupole."),
           ("La Sorbonne et la place de la Sorbonne", "La chapelle et la fontaine de la place, entourée de cafés."),
           ("La rue Mouffetard", "Une rue en pente bordée de commerces de bouche, avec un marché le matin du mardi au dimanche."),
           ("Shakespeare and Company", "La célèbre librairie anglophone face à Notre-Dame. Il y a souvent une file pour entrer."),
           ("Le musée de Cluny", "Le musée du Moyen Âge, avec la tapisserie de la Dame à la licorne et des thermes gallo-romains."),
       ],
       y_aller=[
           ("En RER et en métro", "Gare Luxembourg (RER B) pour le jardin, station Cluny - La Sorbonne (ligne 10) ou Saint-Michel (ligne 4, RER B et C) pour le quartier."),
           ("À pied", "Depuis Notre-Dame, traversez le Petit-Pont : cinq minutes jusqu'à la rue Saint-Jacques."),
       ],
       fiche=[("Durée conseillée", "Une demi-journée"), ("Jardin du Luxembourg", "Gratuit, ouvert tous les jours"), ("Meilleur moment", "Le matin pour le marché de la rue Mouffetard"), ("Pour qui", "Tout le monde, idéal en famille")],
       conseils=[
           "Commencez par la rue Mouffetard le matin, remontez au Panthéon, puis finissez au Luxembourg.",
           "Avec des enfants : voiliers sur le grand bassin, marionnettes et aire de jeux au Luxembourg.",
           "Les horaires du jardin suivent le soleil : il ferme plus tôt en hiver.",
       ],
       activites=[
           ("Visites guidées du Quartier latin", "Balades à pied entre la Sorbonne, le Panthéon et Saint-Germain.", "Quartier latin visite guidée"),
           ("Billets pour le Panthéon", "Entrée au monument et, en saison, montée aux colonnades.", "Panthéon Paris"),
       ],
       faq=[
           ("Le jardin du Luxembourg est-il gratuit ?", "Oui, l'entrée est libre tous les jours. Ses horaires d'ouverture varient selon la saison."),
           ("Qui est enterré au Panthéon ?", "Voltaire, Rousseau, Victor Hugo, Émile Zola, Marie Curie, Joséphine Baker, entre autres."),
           ("Comment aller au jardin du Luxembourg ?", "Par le RER B, gare Luxembourg, juste devant l'entrée principale."),
       ]),

    _d(slug="versailles", locality="Versailles", groupe="musees", nom="Versailles", dept="78", cachet="Yvelines", couleur="ocre", h1="Visiter le château de Versailles",
       description="Visiter le château de Versailles depuis Paris : réservation obligatoire, jour de fermeture, billet Passeport, jardins, Trianon et comment y aller en RER.",
       accroche="La galerie des Glaces, les appartements du Roi, les jardins de Le Nôtre et le domaine de Marie-Antoinette : une journée entière, à quarante minutes de Paris.",
       intro=[
           "Louis XIV transforme le pavillon de chasse de son père en résidence royale et en siège du pouvoir. Le domaine compte aujourd'hui le château, les jardins à la française, le Grand et le Petit Trianon et le Hameau de la Reine, sur des centaines d'hectares.",
           "Le château est fermé le lundi. La réservation d'un créneau horaire est obligatoire pour tous, même pour les entrées gratuites. Le billet Passeport donne accès au château et au domaine de Trianon ; les jardins sont en accès libre, sauf les jours de Grandes Eaux musicales, à la belle saison.",
       ],
       a_voir=[
           ("La galerie des Glaces", "357 miroirs et les plafonds peints par Le Brun. Passez-y en tout début ou en fin de journée pour la voir sans foule."),
           ("Les Grands Appartements", "Les appartements du Roi et de la Reine, avec la chambre de Louis XIV au centre du château."),
           ("Les jardins", "Le Grand Canal, les bassins et les bosquets de Le Nôtre. On peut louer une barque ou un vélo à la belle saison."),
           ("Le Grand et le Petit Trianon", "Les résidences plus intimes de la famille royale, à une demi-heure de marche du château. Ils ouvrent à midi."),
           ("Le Hameau de la Reine", "Le village champêtre de Marie-Antoinette, avec ferme, moulin et étang."),
           ("La galerie des Carrosses", "Dans la Grande Écurie, face au château : les carrosses du sacre, en accès libre."),
       ],
       y_aller=[
           ("En RER C", "Direction Versailles Château Rive Gauche, la gare la plus proche, à dix minutes à pied. Comptez environ 40 minutes depuis le centre de Paris."),
           ("En train Transilien", "Ligne L depuis Saint-Lazare jusqu'à Versailles Rive Droite, ou ligne N depuis Montparnasse jusqu'à Versailles Chantiers. Une vingtaine de minutes à pied ensuite."),
           ("En voiture ou en chauffeur", "Parking payant place d'Armes. Un chauffeur évite les correspondances, surtout avec des enfants."),
       ],
       fiche=[("Durée conseillée", "Une journée"), ("Fermé", "Le lundi"), ("À réserver", "Oui, obligatoire"), ("Meilleur jour", "Mercredi, jeudi ou vendredi")],
       conseils=[
           "Évitez le mardi et le dimanche : ce sont les jours les plus chargés, le château étant fermé le lundi.",
           "Commencez par les jardins et Trianon si votre créneau au château est en début d'après-midi.",
           "En hiver, le château est gratuit le premier dimanche du mois, mais il faut quand même réserver un créneau.",
       ],
       activites=[
           ("Billets et visites guidées de Versailles", "Billet Passeport, visites guidées et transport depuis Paris.", "Château de Versailles"),
           ("Versailles à vélo ou en petit groupe", "Journées guidées avec le château, les jardins et Trianon.", "Versailles visite vélo"),
       ],
       faq=[
           ("Quel jour le château de Versailles est-il fermé ?", "Le lundi, ainsi que le 1er janvier, le 1er mai et le 25 décembre."),
           ("Faut-il réserver pour visiter Versailles ?", "Oui, la réservation d'un créneau horaire est obligatoire pour tous les visiteurs, y compris ceux qui entrent gratuitement."),
           ("Comment aller à Versailles depuis Paris ?", "Le plus simple est le RER C jusqu'à Versailles Château Rive Gauche, à dix minutes à pied du château."),
       ]),
]

ITINERAIRE = {
    "slug": "3-jours",
    "titre": "Paris en 3 jours",
    "description": "Un itinéraire de 3 jours à Paris, en métro et à pied : Notre-Dame, la Sainte-Chapelle, le Louvre, Montmartre, Orsay, la tour Eiffel et une croisière sur la Seine.",
    "accroche": "Trois jours pour l'essentiel de Paris, sans courir. Les étapes sont regroupées par quartier, et chaque journée tient compte des jours de fermeture des musées.",
    "jours": [
        ("Jour 1 : l'île de la Cité et le Marais", [
            ("notre-dame", "Le matin, Notre-Dame avec un créneau réservé, puis le square Jean-XXIII pour le chevet."),
            ("sainte-chapelle", "Cinq minutes à pied jusqu'à la Sainte-Chapelle, de préférence quand le soleil est haut."),
            ("le-marais", "L'après-midi, traversée de l'île Saint-Louis vers le Marais : place des Vosges, musée Carnavalet et rue des Rosiers."),
        ]),
        ("Jour 2 : le Louvre, l'Opéra et Montmartre", [
            ("louvre", "Le Louvre à l'ouverture (pas le mardi), avec un parcours préparé."),
            ("opera-garnier", "Remontée de l'avenue de l'Opéra pour le Palais Garnier, puis la terrasse des Galeries Lafayette."),
            ("montmartre", "Métro jusqu'à Abbesses, montée par les rues du village et coucher du soleil sur le parvis du Sacré-Cœur."),
        ]),
        ("Jour 3 : Orsay, la tour Eiffel et la Seine", [
            ("musee-d-orsay", "Le musée d'Orsay le matin (pas le lundi), en commençant par le 5e étage."),
            ("tour-eiffel", "Promenade le long des quais jusqu'à la tour Eiffel, avec un créneau réservé en milieu d'après-midi."),
            ("croisiere-sur-la-seine", "Croisière au coucher du soleil depuis le pied de la tour, pour voir Paris s'illuminer."),
        ]),
    ],
    "variante": "Avec un quatrième jour, consacrez-le à Versailles (pas le lundi). Pour un après-midi plus calme, remplacez la tour Eiffel par l'Arc de Triomphe et sa terrasse, ou par le Quartier latin et le jardin du Luxembourg.",
    "variante_liens": ["versailles", "arc-de-triomphe", "quartier-latin"],
    "conseils": [
        "Logez près d'une station de la ligne 1 ou de la ligne 4 : elles desservent la plupart des sites de cet itinéraire.",
        "Réservez dès maintenant le Louvre, la Sainte-Chapelle et la tour Eiffel : les créneaux sont obligatoires ou très demandés.",
        "Retenez les jours de fermeture : le Louvre le mardi, Orsay et Versailles le lundi.",
    ],
}

TITRES = {
    "tour-eiffel": "Visiter la tour Eiffel : billets, sommet, conseils",
    "louvre": "Visiter le Louvre : réservation, entrées, conseils",
    "notre-dame": "Visiter Notre-Dame de Paris : entrée, tours",
    "sainte-chapelle": "Visiter la Sainte-Chapelle : réservation, conseils",
    "montmartre": "Visiter Montmartre et le Sacré-Cœur",
    "musee-d-orsay": "Visiter le musée d'Orsay : nocturne, conseils",
    "arc-de-triomphe": "Visiter l'Arc de Triomphe : terrasse, flamme",
    "opera-garnier": "Visiter l'Opéra Garnier : visite libre, conseils",
    "croisiere-sur-la-seine": "Croisière sur la Seine : départs et conseils",
    "le-marais": "Visiter le Marais : place des Vosges, musées",
    "quartier-latin": "Quartier latin et jardin du Luxembourg",
    "versailles": "Visiter Versailles depuis Paris : réservation",
}
TITRE_REGION = "Visiter Paris : les plus beaux sites et conseils"
TITRE_ITI = "Paris en 3 jours : itinéraire en métro"

LIEU_VOIR = {"tour-eiffel": "à la tour Eiffel", "louvre": "au Louvre", "notre-dame": "à Notre-Dame", "sainte-chapelle": "à la Sainte-Chapelle",
             "montmartre": "à Montmartre", "musee-d-orsay": "au musée d'Orsay", "arc-de-triomphe": "à l'Arc de Triomphe", "opera-garnier": "à l'Opéra Garnier",
             "croisiere-sur-la-seine": "sur la Seine", "le-marais": "dans le Marais", "quartier-latin": "dans le Quartier latin", "versailles": "à Versailles"}
LIEU_ALLER = {"tour-eiffel": "à la tour Eiffel", "louvre": "au Louvre", "notre-dame": "à Notre-Dame", "sainte-chapelle": "à la Sainte-Chapelle",
              "montmartre": "à Montmartre", "musee-d-orsay": "au musée d'Orsay", "arc-de-triomphe": "à l'Arc de Triomphe", "opera-garnier": "à l'Opéra Garnier",
              "croisiere-sur-la-seine": "aux embarcadères", "le-marais": "dans le Marais", "quartier-latin": "dans le Quartier latin", "versailles": "à Versailles"}

GEO = {
    "tour-eiffel": (48.8584, 2.2945), "louvre": (48.8606, 2.3376), "notre-dame": (48.8530, 2.3499), "sainte-chapelle": (48.8554, 2.3450),
    "montmartre": (48.8867, 2.3431), "musee-d-orsay": (48.8600, 2.3266), "arc-de-triomphe": (48.8738, 2.2950), "opera-garnier": (48.8720, 2.3316),
    "croisiere-sur-la-seine": (48.8622, 2.3006), "le-marais": (48.8556, 2.3655), "quartier-latin": (48.8462, 2.3371), "versailles": (48.8049, 2.1204),
}

ALIAS = {
    "tour-eiffel": ["tour Eiffel"], "louvre": ["Louvre"], "notre-dame": ["Notre-Dame"], "sainte-chapelle": ["Sainte-Chapelle"],
    "montmartre": ["Montmartre", "Sacré-Cœur"], "musee-d-orsay": ["musée d'Orsay", "Orsay"], "arc-de-triomphe": ["Arc de Triomphe"],
    "opera-garnier": ["Palais Garnier", "Opéra Garnier"], "croisiere-sur-la-seine": ["croisière"], "le-marais": ["Marais"],
    "quartier-latin": ["Quartier latin", "jardin du Luxembourg", "Luxembourg"], "versailles": ["Versailles"],
}
