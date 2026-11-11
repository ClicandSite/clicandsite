# Données SEO (11/11/2026) : titres courts (< 62 caractères avec la marque), formes grammaticales des lieux,
# coordonnées GPS approximatives (centre du lieu) et mots repérés dans le texte pour les liens internes.
TITRES = {
    "monaco": "Visiter Monaco : que voir et comment y aller",
    "eze": "Visiter Èze : jardin, sentier Nietzsche, conseils",
    "iles-de-lerins": "Îles de Lérins : visite et bateau depuis Cannes",
    "saint-paul-de-vence": "Visiter Saint-Paul-de-Vence : que voir, conseils",
    "saint-tropez": "Visiter Saint-Tropez : que voir, comment y aller",
    "nice": "Visiter Nice : que voir, Vieux-Nice, musées",
    "cannes": "Visiter Cannes : Croisette, Suquet, îles",
    "antibes": "Visiter Antibes : vieille ville, Picasso, Cap",
    "villefranche-sur-mer": "Visiter Villefranche-sur-Mer : que voir",
    "saint-jean-cap-ferrat": "Visiter Saint-Jean-Cap-Ferrat : villa et sentier",
    "menton": "Visiter Menton : vieille ville, citron, jardins",
    "grasse": "Visiter Grasse : parfumeries et vieille ville",
    "gourdon": "Visiter Gourdon : village perché, gorges du Loup",
    "mougins": "Visiter Mougins : village perché et FAMM",
    "biot": "Visiter Biot : verrerie et musée Fernand Léger",
    "roquebrune-cap-martin": "Visiter Roquebrune-Cap-Martin : que voir",
    "massif-de-l-esterel": "Massif de l'Estérel : corniche d'Or, randonnées",
    "porquerolles": "Visiter Porquerolles : plages, vélo, bateau",
    "gorges-du-verdon": "Gorges du Verdon : visite depuis la Côte d'Azur",
}
TITRE_REGION = "Visiter la Côte d'Azur : les plus beaux sites"
TITRE_ITI = "La Côte d'Azur en 3 jours sans voiture"

# « Que voir … » / « Comment aller … »
LIEU_VOIR = {"iles-de-lerins": "aux îles de Lérins", "massif-de-l-esterel": "dans l'Estérel", "gorges-du-verdon": "dans les gorges du Verdon"}
LIEU_ALLER = {"iles-de-lerins": "aux îles de Lérins", "massif-de-l-esterel": "dans l'Estérel", "gorges-du-verdon": "aux gorges du Verdon"}

GEO = {
    "monaco": (43.7384, 7.4246), "eze": (43.7277, 7.3614), "iles-de-lerins": (43.5208, 7.0447),
    "saint-paul-de-vence": (43.6966, 7.1222), "saint-tropez": (43.2727, 6.6406), "nice": (43.7009, 7.2683),
    "cannes": (43.5513, 7.0128), "antibes": (43.5804, 7.1251), "villefranche-sur-mer": (43.7040, 7.3111),
    "saint-jean-cap-ferrat": (43.6839, 7.3315), "menton": (43.7747, 7.4975), "grasse": (43.6589, 6.9234),
    "gourdon": (43.7225, 6.9781), "mougins": (43.6000, 6.9953), "biot": (43.6283, 7.0960),
    "roquebrune-cap-martin": (43.7613, 7.4628), "massif-de-l-esterel": (43.4797, 6.9033),
    "porquerolles": (43.0006, 6.2032), "gorges-du-verdon": (43.7660, 6.3400),
}
PAYS = {"monaco": "MC"}

# Mots qui déclenchent un lien vers le guide correspondant (première occurrence seulement, jamais vers la page elle-même)
ALIAS = {
    "monaco": ["Monaco"], "eze": ["Èze"], "iles-de-lerins": ["îles de Lérins"], "saint-paul-de-vence": ["Saint-Paul-de-Vence", "Saint-Paul"],
    "saint-tropez": ["Saint-Tropez"], "nice": ["Nice"], "cannes": ["Cannes"], "antibes": ["Antibes"],
    "villefranche-sur-mer": ["Villefranche-sur-Mer", "Villefranche"], "saint-jean-cap-ferrat": ["Saint-Jean-Cap-Ferrat", "Cap-Ferrat"],
    "menton": ["Menton"], "grasse": ["Grasse"], "gourdon": ["Gourdon"], "mougins": ["Mougins"], "biot": ["Biot"],
    "roquebrune-cap-martin": ["Roquebrune-Cap-Martin", "Roquebrune"], "massif-de-l-esterel": ["Estérel"],
    "porquerolles": ["Porquerolles"], "gorges-du-verdon": ["gorges du Verdon", "Verdon"],
}

A_PROPOS = [
    "Clic&Site est un guide pratique des plus beaux sites de France. Chaque page répond aux trois questions qu'on se pose avant une sortie : qu'y a-t-il à voir, comment y aller, et à quel moment pour éviter la foule.",
    "Le guide est édité à Cannes, par une équipe qui travaille dans le transport de voyageurs sur toute la Côte d'Azur. Les conseils sur les accès, les embouteillages et les bons horaires viennent de là : de trajets faits toute l'année vers ces villages, ces ports et ces îles.",
    "Nous ne donnons ni prix ni horaires précis, parce qu'ils changent souvent : nous préférons vous renvoyer vers les sites officiels et les plateformes de réservation, qui les tiennent à jour.",
    "Clic&Site se finance par l'affiliation : quand vous réservez une activité après avoir cliqué sur un de nos liens, la plateforme nous verse une commission, sans surcoût pour vous. Cela ne change rien à nos recommandations.",
    "Nous commençons par la Côte d'Azur, que nous connaissons le mieux. Les autres régions arriveront une par une.",
]
