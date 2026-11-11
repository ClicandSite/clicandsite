# Alps region (winter sports) — English edition (11/11/2026). Same facts as the French edition.

REGION = {
    "slug": "alpes", "path": "french-alps", "nom": "French Alps",
    "h1": "Skiing in the French Alps",
    "de": "French Alps",
    "autres": "More resorts in the French Alps",
    "couleur": "azur",
    "timbre": "Savoie Mont-Blanc",
    "photo": "alpes",
    "photo_alt": "Snowy peaks above a ski resort in the French Alps",
    "address_region": "Auvergne-Rhône-Alpes",
    "description": "Chamonix, Val Thorens, Courchevel, Megève: guides to French Alps ski resorts, 2026-2027 opening dates, getting there by train and things to do off the slopes.",
    "accroche": "Huge linked ski areas, charming villages and peaks above 3,000 metres: the 2026-2027 season starts on 21 November in the highest resorts.",
    "intro": [
        "The French Alps hold some of the largest ski areas in the world, across Savoie and Haute-Savoie. Each resort has its own character: high altitude and reliable snow in Val Thorens, luxury and perfect pistes in Courchevel, village charm in Megève, high mountains and mountaineering in Chamonix.",
        "Many resorts can be reached without a car: by train to Moûtiers, Sallanches or Saint-Gervais, then by bus or shuttle. Each guide tells you when the resort opens, how to get there and what to do when you are not skiing. Opening dates always depend on snow.",
    ],
    "departements": ["73", "74"],
}

GROUPES = [
    ("stations", "Ski resorts"),
]

VEDETTES = ["chamonix", "val-thorens", "courchevel", "megeve"]

def _d(**k):
    k.setdefault("region", "alpes")
    return k

DESTINATIONS = [
    _d(slug="chamonix", path="chamonix", groupe="stations", nom="Chamonix", dept="74", cachet="Haute-Savoie", couleur="encre", h1="Chamonix: skiing and trips below Mont Blanc",
       **{"in": "in Chamonix", "to": "to Chamonix", "tips_for": "a winter trip to Chamonix"},
       description="Chamonix in winter: the ski areas, the Aiguille du Midi, the Mer de Glace and the Vallée Blanche. 2026-2027 opening dates and getting there by train.",
       accroche="The capital of mountaineering, facing Mont Blanc. People come to ski, but also to go up to almost 3,900 metres without being climbers.",
       intro=[
           "Chamonix is not a single resort but a valley of separate ski areas: Brévent and Flégère facing Mont Blanc, Grands Montets above Argentière, Balme at the head of the valley and Les Houches at its entrance. Free valley shuttles link them.",
           "For the 2026-2027 season, the first areas, Grands Montets and Flégère, are due to open at the end of November, with the others following in December. The Aiguille du Midi cable car and the Montenvers train close for a few weeks of maintenance every November before reopening for winter.",
       ],
       a_voir=[
           ("The Aiguille du Midi", "The cable car climbs to 3,842 metres in about twenty minutes. At the top: terraces facing Mont Blanc and the Step into the Void, a glass box above a 1,000-metre drop. Go in the morning, on a clear day."),
           ("The Montenvers train and the Mer de Glace", "A red rack railway runs from Chamonix to Montenvers, facing France's largest glacier. A gondola and steps lead down to the ice cave dug out every year."),
           ("The Vallée Blanche", "A legendary off-piste run of about twenty kilometres from the Aiguille du Midi. It must be done with a mountain guide."),
           ("Brévent and Flégère", "The two sunny-side ski areas, with the finest views of the Mont Blanc massif. Ideal for intermediate skiers."),
           ("Grands Montets", "The area for strong skiers, above Argentière: big slopes, high-altitude snow and glacier views."),
           ("Chamonix town centre", "Pedestrian streets, Belle Époque façades and the statue of Balmat and Saussure pointing at Mont Blanc. Après-ski happens here."),
       ],
       y_aller=[
           ("By train", "TGV or TER to Saint-Gervais-les-Bains - Le Fayet, then the Mont-Blanc Express to Chamonix in about forty minutes."),
           ("From Geneva airport", "About 1 hour 15 minutes by road. Shuttles and private transfers run all season."),
           ("Getting around", "Valley shuttles serve the ski areas. The guest card from your accommodation gives access to local transport."),
       ],
       fiche=[("2026-2027 opening", "Late November (first areas)"), ("Good for", "Strong skiers, high-mountain fans"), ("Without skiing", "Aiguille du Midi, Mer de Glace"), ("Access", "Train to Le Fayet, then Mont-Blanc Express")],
       conseils=[
           "Check the summit weather before going up the Aiguille du Midi: on a cloudy day you will see nothing.",
           "Off-piste skiing in Chamonix means high mountains: never go without a guide and safety equipment.",
           "For February, book your accommodation early: the valley is in high demand during school holidays.",
       ],
       activites=[
           ("Aiguille du Midi and Mer de Glace", "Tickets and guided trips from Chamonix or Geneva.", "Chamonix Aiguille du Midi"),
           ("Ski lessons and off-piste outings", "Instructors and mountain guides in the Chamonix valley.", "Chamonix ski"),
       ],
       faq=[
           ("When does Chamonix open in 2026?", "The first areas, Grands Montets and Flégère, are due to open at the end of November 2026, with the rest of the valley in December, depending on snow."),
           ("Can you go up the Aiguille du Midi in winter?", "Yes, the cable car runs in winter after its annual maintenance closure in November. Check the summit weather before you go."),
           ("How do you get to Chamonix without a car?", "By train to Saint-Gervais-Le Fayet then the Mont-Blanc Express, or by shuttle from Geneva airport."),
       ]),

    _d(slug="val-thorens", path="val-thorens", groupe="stations", nom="Val Thorens", dept="73", cachet="Savoie", couleur="azur", h1="Val Thorens: Europe's highest ski resort",
       **{"in": "in Val Thorens", "to": "to Val Thorens", "tips_for": "skiing in Val Thorens"},
       description="Skiing in Val Thorens: 2026-2027 opening dates, the 3 Valleys, Cime Caron, getting there by train via Moûtiers, and tips.",
       accroche="At 2,300 metres, Val Thorens is the highest ski resort in Europe. It opens first and closes last: from late November to early May.",
       intro=[
           "Val Thorens sits at the head of the Belleville valley, at the heart of the 3 Valleys, the world's largest linked ski area, together with Les Menuires, Méribel and Courchevel. Its altitude gives reliable snow from the start of the season to the end.",
           "For winter 2026-2027 the resort plans to open on 21 November 2026 and close in early May 2027, depending on snow. The resort is almost entirely car-free: you can ski from the door of most accommodation.",
       ],
       a_voir=[
           ("Cime Caron", "A cable car rises to 3,200 metres for one of the biggest panoramas in the Alps, from Mont Blanc to the Vanoise. The run down is for strong skiers."),
           ("The 3 Valleys", "With a 3 Valleys pass you can ski to Les Menuires, Méribel and Courchevel in a day."),
           ("Orelle", "On the Maurienne side, the Orelle sector is linked to Val Thorens, with sunny and often quieter slopes."),
           ("Après-ski", "Val Thorens is known for its party atmosphere, from mountain terraces to bars in the resort."),
       ],
       y_aller=[
           ("By train", "Train to Moûtiers - Salins - Brides-les-Bains station, then a regional bus to the resort, about an hour's drive up."),
           ("By plane", "The nearest airports are Chambéry, Lyon and Geneva, with shuttles and private transfers in season."),
           ("By car", "Through the Tarentaise valley then the Belleville road. Winter equipment is compulsory; the resort is car-free, so book parking."),
       ],
       fiche=[("2026-2027 opening", "21 November 2026"), ("Closing", "Early May 2027"), ("Altitude", "2,300 m"), ("Ski area", "The 3 Valleys")],
       conseils=[
           "Early and late in the season, it is one of the few resorts where the whole area is open: ideal for a trip in November or April.",
           "At 2,300 metres, cold and wind can be fierce: bring goggles, a balaclava and sunscreen.",
           "Buy your lift pass online before arriving to skip the Saturday queue at the ticket office.",
       ],
       activites=[
           ("Things to do in Val Thorens", "Ski lessons, snowmobiling, paragliding and snowshoe outings.", "Val Thorens"),
           ("3 Valleys outings", "Guided trips and activities in Méribel and Courchevel.", "3 Valleys ski"),
       ],
       faq=[
           ("When does Val Thorens open in 2026?", "The resort plans to open on Saturday 21 November 2026, depending on snow, for a season running until early May 2027."),
           ("Why is Val Thorens the highest resort in Europe?", "The village is built at 2,300 metres, and its lifts reach 3,200 metres at Cime Caron."),
           ("How do you get to Val Thorens without a car?", "By train to Moûtiers, then by regional bus to the resort."),
       ]),

    _d(slug="courchevel", path="courchevel", groupe="stations", nom="Courchevel", dept="73", cachet="Savoie", couleur="encre", h1="Courchevel: skiing and staying in the 3 Valleys",
       **{"in": "in Courchevel", "to": "to Courchevel", "tips_for": "skiing in Courchevel"},
       description="Skiing in Courchevel: the 1850, 1650, 1550 and Le Praz villages, 2026-2027 opening dates, getting there by train via Moûtiers and things to do off the slopes.",
       accroche="Perfectly groomed pistes, an altiport and grand hotels: Courchevel is the most prestigious resort in the Alps, and also an excellent ski area for every level.",
       intro=[
           "Courchevel is made up of several villages at different heights: Saint-Bon, Le Praz, Courchevel Village, Moriond and Courchevel 1850, the best known. With La Tania they form the Courchevel ski area, linked to the 3 Valleys via Méribel.",
           "The resort announces a season from 4 December 2026 to 18 April 2027, depending on snow. Its ski area, known for the quality of its grooming, suits beginners and experts alike.",
       ],
       a_voir=[
           ("Courchevel 1850", "The heart of the resort: luxury shops, Michelin-starred restaurants and the altiport, where small planes land between the slopes."),
           ("The Grand Couloir", "One of the most famous black runs in the Alps, from La Saulire. For experts only and dependent on snow."),
           ("The Le Praz ski jumps", "Built for the 1992 Albertville Olympics, they still host ski-jumping competitions."),
           ("Aquamotion", "A large aquatic and wellness centre in Courchevel Moriond, perfect for a day off skis."),
           ("Moriond and La Tania", "More family-friendly, more affordable villages with direct access to the same ski area."),
       ],
       y_aller=[
           ("By train", "Train to Moûtiers - Salins - Brides-les-Bains, then a regional bus to the different Courchevel villages."),
           ("By plane", "Chambéry, Lyon and Geneva airports, with shuttles and private transfers. The altiport also takes private flights."),
           ("Getting around", "Free shuttles link the villages of the resort."),
       ],
       fiche=[("2026-2027 opening", "4 December 2026"), ("Closing", "18 April 2027"), ("Ski area", "The 3 Valleys"), ("Good for", "All levels, upmarket stays")],
       conseils=[
           "For a more reasonable budget, stay in Moriond, Le Praz or La Tania: you will ski the same area.",
           "The runs to Méribel let you ski the 3 Valleys in a day: check that your pass covers it.",
           "Book mountain restaurants ahead during the Christmas and February holidays.",
       ],
       activites=[
           ("Things to do in Courchevel", "Ski lessons, snowshoeing, paragliding and dog sledding.", "Courchevel"),
           ("3 Valleys outings", "Guided ski days between Courchevel, Méribel and Val Thorens.", "Courchevel 3 Valleys"),
       ],
       faq=[
           ("When does Courchevel open in 2026?", "The resort announces an opening on 4 December 2026 and a closing on 18 April 2027, depending on snow."),
           ("Which Courchevel village should I choose?", "1850 for prestige and altitude, Moriond for families, Le Praz and La Tania for charm and gentler prices."),
           ("How do you get to Courchevel by train?", "To Moûtiers station, then by regional bus to the resort."),
       ]),

    _d(slug="megeve", path="megeve", groupe="stations", nom="Megève", dept="74", cachet="Haute-Savoie", couleur="ocre", h1="Megève: a charming village and skiing facing Mont Blanc",
       **{"in": "in Megève", "to": "to Megève", "tips_for": "a ski trip to Megève"},
       description="Skiing in Megève: the village, the Évasion Mont-Blanc ski area, 2026-2027 opening dates, getting there by train via Sallanches and things to do off the slopes.",
       accroche="A real Savoyard village, horse-drawn carriages in the streets and tree-lined slopes facing Mont Blanc. Megève is the classic chic, gentle ski resort.",
       intro=[
           "Megève grew up around its medieval village, with its church and pedestrian streets. Its ski area is part of Évasion Mont-Blanc, which links Megève, Saint-Gervais, Combloux and other villages across more than 400 kilometres of pistes.",
           "For 2026-2027, Megève plans a partial early opening in early December, then a full opening on 19 December 2026 until early April 2027, depending on snow. Its mid-altitude, often tree-lined runs make it pleasant even in bad weather.",
       ],
       a_voir=[
           ("The village", "Church square, pedestrian streets, shops and horse-drawn carriages: one of the prettiest resort villages in the Alps, especially when lit up in December."),
           ("Mont d'Arbois", "The sector linked to Saint-Gervais, with long easy runs and a superb view of Mont Blanc."),
           ("Rochebrune", "The area right above the village, reached by cable car, handy for half a day."),
           ("Le Jaillet and Combloux", "Across the valley, sunny slopes facing the Mont Blanc range."),
           ("Off the slopes", "Carriage rides, an ice rink, snowshoe walks and dog sledding."),
       ],
       y_aller=[
           ("By train", "To Sallanches - Combloux - Megève station, then about thirty minutes by bus or taxi to the village."),
           ("From Geneva airport", "About 1 hour 15 minutes by road, with shuttles and private transfers in season."),
           ("Getting around", "Free shuttles serve the different lift departures."),
       ],
       fiche=[("2026-2027 opening", "19 December 2026 (partial early December)"), ("Closing", "Early April 2027"), ("Ski area", "Évasion Mont-Blanc"), ("Good for", "Families, relaxed skiers, village lovers")],
       conseils=[
           "Go up Mont d'Arbois on a clear day: that is where the view of Mont Blanc is most spectacular.",
           "Enjoy the village at the end of the day, when the lights come on.",
           "During the February holidays, book children's ski lessons several weeks ahead.",
       ],
       activites=[
           ("Things to do in Megève", "Ski lessons, dog sledding, paragliding and snowshoeing.", "Megeve"),
           ("Trips to Chamonix and Mont Blanc", "Guided days from Megève or Geneva.", "Megeve Chamonix tour"),
       ],
       faq=[
           ("When does Megève open in 2026?", "A partial early opening in early December, then a full opening on 19 December 2026, depending on snow."),
           ("Is Megève good for beginners?", "Yes, the area has many blue and green runs, often sheltered by forest."),
           ("What is the nearest train station to Megève?", "Sallanches - Combloux - Megève station, about thirty minutes from the village by bus or taxi."),
       ]),
]

TITRES = {
    "chamonix": "Chamonix in Winter: Skiing, Aiguille du Midi, Access",
    "val-thorens": "Val Thorens: 2026 Opening, Getting There, Tips",
    "courchevel": "Courchevel: Skiing, Villages, 2026 Opening",
    "megeve": "Megève: Skiing, Village, 2026-2027 Opening",
}
TITRE_REGION = "French Alps Ski Resorts: Guides and 2026 Openings"

ALIAS = {"chamonix": ["Chamonix"], "val-thorens": ["Val Thorens"], "courchevel": ["Courchevel"], "megeve": ["Megève"]}
