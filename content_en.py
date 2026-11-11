# English edition of Clic&Site (clicandsite.com) — 11/11/2026.
# Same facts as the French edition. Rule: no prices, no precise timetables.
# "slug" = internal key shared with the French site (photos, GPS, hreflang); "path" = English URL segment.

REGIONS = [
    {
        "slug": "cote-d-azur", "path": "french-riviera", "nom": "French Riviera",
        "description": "Nice, Monaco, Cannes, Èze, Saint-Tropez, the Lérins Islands, Porquerolles, the Esterel: practical guides to the French Riviera, how to get there and what to book.",
        "accroche": "Hilltop villages, islands fifteen minutes from the Croisette, legendary harbours: the Riviera is easy to explore without a car, as long as you know where to go and when.",
        "intro": [
            "The French Riviera — the Côte d'Azur — stretches from Saint-Tropez to Menton, between the Var and the Italian border. The coastal railway links most of the main towns, Nice and Cannes make good bases, and many places can be combined in a single day.",
            "The hard part is not finding things to see but avoiding the July-August traffic jams and the hours when the cruise-ship coaches arrive. Each guide below tells you how to get there and when to go. We have added the great day trips from the Riviera too, such as Porquerolles and the Verdon Gorge.",
        ],
        "departements": ["06", "83"],
    },
]

PROCHAINES_REGIONS = ["Provence", "the Alps", "Paris", "Brittany", "the Basque Country"]

GROUPES = [
    ("mer", "Towns and seaside"),
    ("villages", "Hilltop villages"),
    ("nature", "Islands and great outdoors"),
]

def _d(**k):
    k.setdefault("region", "cote-d-azur")
    return k

DESTINATIONS = [
    _d(slug="monaco", path="monaco", groupe="mer", nom="Monaco", dept="MC", cachet="Principality", couleur="azur",
       description="Visiting Monaco in a day: the Rock, the changing of the guard, the Oceanographic Museum, Monte-Carlo and the harbour. How to get there from Nice and Cannes.",
       accroche="Two square kilometres, a palace, a casino and one of Europe's finest sea museums. Monaco is easy to see on foot in a day.",
       intro=[
           "The Principality is best seen in two parts: the Rock, the old town on its clifftop with the Prince's Palace and the Oceanographic Museum, then Monte-Carlo with its casino and gardens. Port Hercule and its yachts lie in between.",
           "Monaco is a country in its own right, but there are no border checks coming from France and the currency is the euro. The town is steep: free public lifts link the different levels, so look for them before you tackle the stairs.",
       ],
       a_voir=[
           ("The Prince's Palace and the changing of the guard", "Every day at 11:55, the Prince's Carabiniers change the guard in front of the Palace. Arrive a quarter of an hour early for a front-row spot. The State Apartments are open for part of the year."),
           ("The Oceanographic Museum", "Founded by Prince Albert I and built into the cliff, it combines a remarkable aquarium with scientific collections. The rooftop terrace has one of the best views on the coast."),
           ("Monaco Cathedral", "A white-stone church on the Rock, where Princess Grace and Prince Rainier III are buried. Entry is free outside services."),
           ("The Saint-Martin Gardens", "A shady clifftop walk between the museum and the cathedral, ideal for a break from the heat."),
           ("Monte-Carlo and Casino Square", "The casino, the opera house and the Hôtel de Paris form the most photographed corner of the Principality. The casino atrium can be visited during the day; smart dress is expected."),
           ("Port Hercule", "The heart of the Formula 1 Grand Prix circuit, at the foot of the Rock. Walk along the quays to see the size of the yachts."),
       ],
       y_aller=[
           ("By train", "Monaco-Monte-Carlo station is served by regional TER trains on the coastal line: about twenty minutes from Nice, around an hour from Cannes. It is the easiest option."),
           ("By bus", "Regional buses run along the Lower Corniche from Nice. Slower than the train, but with sea views all the way."),
           ("By car or with a driver", "There are plenty of public car parks, all paying. During the Grand Prix and big events traffic is very difficult: take the train or a private transfer."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "April to June, September-October"), ("Avoid", "Grand Prix week, unless you are going for the race"), ("Good for", "Everyone, on foot")],
       conseils=[
           "Start with the Rock in the morning (changing of the guard, museum), go down to the harbour for lunch, then up to Monte-Carlo in the afternoon.",
           "On cruise-ship days the Rock is very busy between 10am and 3pm: the museum is the best place to be at those times.",
           "Dress modestly for the cathedral and the casino.",
       ],
       activites=[
           ("Monaco tickets and tours", "Oceanographic Museum, Prince's Palace, guided walks on the Rock.", "Monaco"),
           ("Monaco, Èze and Riviera day trips", "Small-group days from Nice or Cannes.", "Monaco Eze day trip"),
       ],
       faq=[
           ("Do you need a passport to go to Monaco?", "There are no border checks between France and Monaco, but carry an ID document as you would anywhere when travelling."),
           ("How long do you need to visit Monaco?", "One day is enough for the Rock, the harbour and Monte-Carlo. Allow an extra half-day to take your time at the Oceanographic Museum."),
           ("What is the best way to get from Nice to Monaco?", "The TER train: about twenty minutes, to a station in the heart of the Principality. Driving is not recommended on busy days."),
       ]),
    _d(slug="eze", path="eze", groupe="villages", nom="Èze", dept="06", cachet="Alpes-Maritimes", couleur="pin",
       to="to Èze", description="Things to do in Èze, the hilltop village between Nice and Monaco: the Jardin d'Èze, the Nietzsche path, the perfumeries. How to get there and when to go.",
       accroche="A medieval village clinging to its rock more than 400 metres above the sea. The view from the garden at the very top is worth the climb on its own.",
       intro=[
           "Èze is one of the most spectacular hilltop villages on the Riviera, between Nice and Monaco. Cobbled lanes, vaulted passages, stone houses: you enter on foot and cars stay below.",
           "At the top, on the ruins of the old castle, the Jardin d'Èze mixes succulents and sculptures, with a view over the Cap-Ferrat peninsula and, on very clear days, all the way to Corsica.",
       ],
       a_voir=[
           ("The Jardin d'Èze", "The highest point of the village, with a breathtaking view of the Mediterranean. It is the only paying part of the visit, and the one not to miss."),
           ("The village lanes", "No map needed: climb towards the garden and get lost in the passages on purpose. Art galleries and small shops at every corner."),
           ("Notre-Dame-de-l'Assomption church", "An ochre façade and a baroque interior in the heart of the village."),
           ("The Nietzsche path", "The trail linking the seafront (Èze-sur-Mer) to the village, once walked by the philosopher. Allow a good hour of steep climbing: if you are not a walker, do it downhill."),
           ("The perfumeries", "At the foot of the village, Grasse perfume houses have workshops and shops. Factory tours are free."),
       ],
       y_aller=[
           ("By bus from Nice", "Regional buses climb the Middle Corniche and stop at the foot of the village. It is the most practical option without a car."),
           ("By train, then on foot", "TER trains stop at Èze-sur-Mer, by the sea. From there the Nietzsche path climbs up to the village: a beautiful but demanding hike."),
           ("By car or with a driver", "Parking at the foot of the village is scarce in season. A private driver makes it easy to combine Èze and Monaco in the same day."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Early morning or late afternoon"), ("Avoid", "Midday in summer"), ("Good for", "Good walkers, no pushchairs")],
       conseils=[
           "Arrive before 10am: coach tours arrive later and the lanes get crowded.",
           "The streets are steep and cobbled: good shoes are essential.",
           "Èze combines very well with Monaco, a few minutes' drive away.",
       ],
       activites=[
           ("Èze and Monaco tours", "The classic Riviera pairing, as a half-day or full-day trip.", "Eze Monaco"),
           ("Perfume workshops and tours", "Create your own perfume, guided perfumery visits.", "Eze perfume"),
       ],
       faq=[
           ("Do you have to pay to visit Èze village?", "No, the village is free to enter. Only the Jardin d'Èze at the top charges admission."),
           ("Can you visit Èze with a pushchair or wheelchair?", "It is very difficult: the lanes are steep, cobbled and often stepped. A baby carrier is better."),
           ("How long does the Nietzsche path take?", "About an hour uphill from Èze-sur-Mer, a little less going down. The path is steep and has little shade: avoid the hottest hours."),
       ]),
    _d(slug="iles-de-lerins", path="lerins-islands", groupe="nature", nom="Lérins Islands", dept="06", cachet="Cannes", couleur="ocre",
       h1="Visiting the Lérins Islands", **{"in": "on the Lérins Islands", "to": "to the Lérins Islands", "tips_for": "visiting the Lérins Islands"},
       description="Visiting the Lérins Islands off Cannes: Sainte-Marguerite and the Man in the Iron Mask, Saint-Honorat and its monks. Ferries from Cannes, tips and activities.",
       accroche="Fifteen minutes by boat from the Croisette, two car-free islands: pine woods, coves, a fort where the Man in the Iron Mask was held, and an abbey where monks still live.",
       intro=[
           "The Lérins Islands are the best escape from Cannes. Sainte-Marguerite, the larger one, is covered in forest and fringed with coves. Saint-Honorat, smaller, belongs to a community of monks who grow vines there.",
           "There are no cars and no main roads: just paths, shade and very clear water. Plan the whole day and bring water and a picnic.",
       ],
       a_voir=[
           ("Fort Royal (Sainte-Marguerite)", "Visit the cell of the mysterious Man in the Iron Mask, imprisoned under Louis XIV. The fort also houses the Musée de la Mer, with finds from ancient shipwrecks."),
           ("Walking around Sainte-Marguerite", "A path follows the coast all the way round the island, with coves for swimming. The inland trail crosses a forest of pines and eucalyptus."),
           ("Lérins Abbey (Saint-Honorat)", "The Cistercian monks welcome visitors in silence. You can visit the abbey church and the fortified monastery by the water."),
           ("The monks' vineyards and wines", "Saint-Honorat is covered in vines. The monks make a renowned wine and liqueurs, sold on the island."),
       ],
       y_aller=[
           ("By boat from Cannes", "Shuttles leave from Quai Laubeuf in Cannes harbour all year round. About fifteen minutes to Sainte-Marguerite, a little more to Saint-Honorat. The two islands are served separately: check before you go if you want to visit both."),
           ("From other ports", "In season, boats also leave from Juan-les-Pins, Golfe-Juan and Nice, less frequently."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "May-June and September"), ("Avoid", "Sundays in August, very busy"), ("Good for", "Families, walkers, swimmers")],
       conseils=[
           "Take one of the first boats in the morning: you will have the coves to yourself.",
           "Bring water and lunch; places to eat are limited.",
           "On Saint-Honorat, calm is part of the experience: dress modestly and keep your voice down near the abbey.",
       ],
       activites=[
           ("Boats and trips to the islands", "Crossings, cruises around the islands, snorkelling trips.", "Lerins Islands"),
           ("Boat trips from Cannes", "Cruises, catamarans and boat rides around the bay.", "Cannes boat"),
       ],
       faq=[
           ("Can you visit both Lérins Islands in one day?", "Yes, but they are served separately from Cannes. Check the crossings on the day and start early."),
           ("Can you swim on the Lérins Islands?", "Yes, Sainte-Marguerite is fringed with coves of very clear water. There is no lifeguarded beach: take care with children."),
           ("Are there restaurants on the islands?", "There are a few, often packed in summer. A picnic is the simplest option."),
       ]),
    _d(slug="saint-paul-de-vence", path="saint-paul-de-vence", groupe="villages", nom="Saint-Paul-de-Vence", dept="06", cachet="Alpes-Maritimes", couleur="encre",
       description="Things to do in Saint-Paul-de-Vence: the ramparts, the galleries, the Fondation Maeght and Chagall's grave. How to get there from Nice and Cannes.",
       accroche="A walled village on its hill, art galleries at every door, and one of Europe's finest modern art museums a short walk away.",
       intro=[
           "Saint-Paul-de-Vence is the Riviera's artists' village. Its 16th-century ramparts still enclose a maze of cobbled lanes, fountains and galleries.",
           "Chagall lived here and is buried in the small village cemetery. Just below, the Fondation Maeght, opened in the 1960s, brings together Miró, Giacometti, Braque and Chagall in a building designed for them.",
       ],
       a_voir=[
           ("The ramparts walk", "A walkway runs all the way round the village, with views over the hills to the sea on one side and the foothills of the Alps on the other."),
           ("Rue Grande and the galleries", "The main street crosses the village from gate to gate. Painters, sculptors and ceramicists exhibit all year round."),
           ("The Fondation Maeght", "A few minutes' walk from the village, a museum in the middle of nature: the Giacometti courtyard, the Miró labyrinth and excellent temporary exhibitions."),
           ("Marc Chagall's grave", "In the cemetery at the southern end of the village. Visitors leave small pebbles, following tradition."),
           ("The pétanque square", "At the village entrance, under the plane trees, where people have always played pétanque. A simple, very Provençal moment."),
       ],
       y_aller=[
           ("By bus from Nice", "Regional buses link Nice and Saint-Paul-de-Vence, stopping at the foot of the village. Allow about an hour."),
           ("By car or with a driver", "The village is pedestrianised; paying car parks surround it and are often full in summer. Saint-Paul combines easily with Vence or Grasse."),
       ],
       fiche=[("Time needed", "Half a day, a full day with the Fondation"), ("Best time", "Spring and autumn"), ("Avoid", "Midday in July-August"), ("Good for", "Art lovers and old-stone enthusiasts")],
       conseils=[
           "Visit the Fondation Maeght in the morning and the village late in the day, when the light turns the ramparts golden and the groups have gone.",
           "The lanes are cobbled and steep: flat shoes recommended.",
           "Most galleries sell original works; you are welcome to go in and look without buying.",
       ],
       activites=[
           ("Saint-Paul-de-Vence tours", "Hilltop villages of the hinterland, often combined with Grasse or Èze.", "Saint-Paul-de-Vence"),
           ("Grasse and hilltop villages", "Days out between perfumeries and characterful villages.", "Grasse hilltop villages"),
       ],
       faq=[
           ("Is Saint-Paul-de-Vence wheelchair accessible?", "The village is steep and cobbled, so access is difficult. The Fondation Maeght is easier to get around."),
           ("Do you need to book the Fondation Maeght?", "Not usually, but it is advisable in high season and during major exhibitions."),
           ("Can you combine Saint-Paul-de-Vence and Èze in one day?", "Yes, by car or with a driver. Without a car it is harder: the two villages are on different bus lines from Nice."),
       ]),
    _d(slug="saint-tropez", path="saint-tropez", groupe="mer", nom="Saint-Tropez", dept="83", cachet="Var", couleur="azur",
       description="Things to do in Saint-Tropez: the harbour, the Citadel, the Place des Lices market, the Annonciade museum and Pampelonne. How to get there by boat and skip the traffic.",
       accroche="A former fishing village turned legend. Out of season Saint-Tropez is a little Provençal port again; in summer, arrive by sea.",
       intro=[
           "Saint-Tropez is first and foremost a harbour: colourful façades, terraces and yachts at the foot of the old town. Behind it, the lanes of La Ponche, the fishermen's quarter, lead down to a small beach.",
           "The peninsula is famous for its beaches, especially Pampelonne, in the neighbouring town of Ramatuelle. In July and August the access road is one of the most congested in France: the boat changes everything.",
       ],
       a_voir=[
           ("The Old Port", "Saint-Tropez's non-stop show. Go early in the morning to see it before the crowds, or at aperitif time for the atmosphere."),
           ("The Citadel", "The 17th-century fortress on the hill houses the maritime history museum. The view over the gulf and the town is the best in Saint-Tropez."),
           ("Place des Lices market", "Tuesday and Saturday mornings under the plane trees: Provençal produce, flowers, clothes. The locals' meeting place."),
           ("The Annonciade museum", "A former chapel on the harbour, housing paintings by the artists who loved Saint-Tropez, from Signac to Matisse."),
           ("La Ponche", "The old fishermen's quarter with its lanes and small beach, a stone's throw from the harbour."),
           ("Pampelonne beaches", "Several kilometres of sand in Ramatuelle, with public stretches and private beach clubs."),
       ],
       y_aller=[
           ("By boat", "The best option in season. Shuttles link Saint-Tropez with Sainte-Maxime all year round, and in summer with Saint-Raphaël, Cannes and Nice. You land right in the harbour."),
           ("By bus", "There is no train station in Saint-Tropez. Regional buses leave from Saint-Raphaël and Toulon, but get stuck in summer traffic."),
           ("By car or with a driver", "Out of season the drive is pleasant. In July-August expect hours of traffic at the entrance to the peninsula: leave very early or come back late."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "May-June and September"), ("Avoid", "Driving at weekends in July-August"), ("Good for", "Strollers, beach and market lovers")],
       conseils=[
           "Come on a Tuesday or Saturday to enjoy the Place des Lices market.",
           "In summer, take the boat from Sainte-Maxime or Cannes: faster and far more pleasant.",
           "Climb to the Citadel late in the afternoon for the light over the gulf.",
       ],
       activites=[
           ("Saint-Tropez day trips", "Days by boat or minibus from Cannes, Nice or Sainte-Maxime.", "Saint-Tropez"),
           ("Boats and cruises in the gulf", "Boat trips, celebrity-villa tours, full-day outings.", "Saint-Tropez boat"),
       ],
       faq=[
           ("How do you get to Saint-Tropez without a car?", "The easiest way is the boat, from Sainte-Maxime all year round or from Cannes, Nice and Saint-Raphaël in season. There is no train station."),
           ("What day is the Saint-Tropez market?", "The Place des Lices market is held on Tuesday and Saturday mornings."),
           ("Is Pampelonne beach in Saint-Tropez?", "It is in the neighbouring town of Ramatuelle, a few kilometres from the centre of Saint-Tropez."),
       ]),
    _d(slug="nice", path="nice", groupe="mer", nom="Nice", dept="06", cachet="Alpes-Maritimes", couleur="azur",
       description="Things to do in Nice: the Promenade des Anglais, the Old Town, Cours Saleya, Castle Hill and the Matisse and Chagall museums. Tips and getting around.",
       accroche="The capital of the Riviera: a huge bay, an old town of ochre façades and museums worthy of the greatest cities.",
       intro=[
           "Nice is the gateway to the French Riviera: an airport minutes from the centre, a station with trains to Monaco, Antibes and Cannes, and a tram that links it all.",
           "The city is best explored on foot, from the Promenade des Anglais to the lanes of the Old Town, then up to Castle Hill or the Cimiez district, where Matisse and Belle Époque high society lived.",
       ],
       a_voir=[
           ("The Promenade des Anglais", "Seven kilometres along the Baie des Anges, with its famous blue chairs. Walk, cycle or skate it, ideally at sunset."),
           ("Old Nice (Vieux-Nice)", "Narrow lanes, ochre and red façades, baroque churches and little grocery shops. This is where you try socca, Nice's chickpea pancake."),
           ("Cours Saleya", "The flower and local produce market is held here on Tuesday to Sunday mornings; on Mondays it makes way for an antiques market."),
           ("Castle Hill", "Nice's most famous viewpoint, with its waterfall and a view over the whole bay and harbour. Go up by the steps or the lift."),
           ("The Matisse Museum", "In a red Genoese villa in Cimiez surrounded by olive trees, a collection covering the painter's whole career; he lived in Nice."),
           ("The Marc Chagall National Museum", "Built to house the Biblical Message cycle, with stained glass and monumental canvases. One of the finest museums on the coast."),
           ("Port Lympia", "Colourful façades and traditional fishing boats called pointus. The starting point for the walk to Rauba-Capeù point."),
       ],
       y_aller=[
           ("From the airport", "Tram line 2 links Nice Côte d'Azur airport with the city centre and the harbour. It is the cheapest option."),
           ("By train", "Nice-Ville station is served by TER trains on the coastal line (Cannes, Antibes, Monaco, Menton) and by TGV high-speed trains from Paris."),
           ("Getting around Nice", "The centre is walkable; the tram and the Lignes d'Azur buses cover the rest. You do not need a car."),
       ],
       fiche=[("Time needed", "Two days"), ("Best time", "All year round"), ("Avoid", "The packed beaches on 15 August"), ("Good for", "Everyone")],
       conseils=[
           "Nice's beaches are pebbly: water shoes make swimming much more pleasant.",
           "Go up Castle Hill late in the afternoon for the light over the bay.",
           "Nice is the best base for visiting Monaco, Èze, Villefranche or Saint-Paul-de-Vence without a car.",
       ],
       activites=[
           ("Nice guided tours and food tours", "Old Town walks, Niçoise food tastings, bike or segway tours.", "Nice walking tour"),
           ("Day trips from Nice", "Monaco, Èze, Saint-Paul-de-Vence or the Verdon Gorge in a day.", "Nice day trip"),
       ],
       faq=[
           ("How many days do you need in Nice?", "Two days let you see the Old Town, Castle Hill, the Promenade and one or two museums. Add more if you use Nice as a base for the Riviera."),
           ("Are Nice's beaches sandy?", "No, they are pebbly. There are free public beaches and private beaches with sunbeds."),
           ("How do you get from Nice airport to the city centre?", "The easiest way is tram line 2, which links the airport with the centre and the harbour. A taxi or private driver is easier with luggage."),
       ]),
    _d(slug="cannes", path="cannes", groupe="mer", nom="Cannes", dept="06", cachet="Alpes-Maritimes", couleur="encre",
       description="Things to do in Cannes: La Croisette, the Palais des Festivals steps, Le Suquet, the Forville market and the Lérins Islands. What to see and how to plan your day.",
       accroche="Much more than a festival: a hilltop old town, a covered Provençal market and two wild islands fifteen minutes away by boat.",
       intro=[
           "Cannes lives to the rhythm of its big events, the Film Festival first among them, but it is worth visiting all year round. Between the Croisette and its palace hotels, the harbour and Le Suquet, everything is within walking distance.",
           "For the perfect day, keep time for the Lérins Islands: boats leave from the harbour, right below the old town.",
       ],
       a_voir=[
           ("La Croisette", "The Riviera's most famous boulevard, lined with palace hotels and private beaches. The walk continues to Pointe Croisette and its gardens."),
           ("The Palais des Festivals", "The interior is closed outside events, but everyone comes to be photographed on the steps. Next to it, the stars' handprints are set in the pavement."),
           ("Le Suquet", "The old town on its hill: cobbled lanes, restaurant terraces and, at the top, Notre-Dame-d'Espérance church with a view over the whole bay."),
           ("The Musée des Explorations du Monde", "At the top of Le Suquet, in the former castle of the Lérins monks: collections from five continents and a tower with the best panorama in Cannes."),
           ("Forville market", "Cannes's covered market at the foot of Le Suquet: fruit, vegetables, fish and cheese on Tuesday to Sunday mornings, a flea market on Mondays."),
           ("Rue d'Antibes", "The main shopping street, parallel to the Croisette, for shopping away from the seafront crowds."),
       ],
       y_aller=[
           ("By train", "Cannes station is right in the centre, a few minutes' walk from the Croisette. TER trains reach Nice in about half an hour and Antibes in about ten minutes."),
           ("From Nice airport", "Express buses link the airport with Cannes. With luggage or as a group, a private transfer is the simplest option."),
       ],
       fiche=[("Time needed", "One day, two with the islands"), ("Best time", "April to June, September-October"), ("Avoid", "Festival fortnight, unless you want the buzz"), ("Good for", "Everyone")],
       conseils=[
           "During the Cannes Film Festival and the big trade fairs, hotels are full and prices soar: book very early or come at another time.",
           "Do the Forville market in the morning, then climb Le Suquet before the heat.",
           "Keep a day for the Lérins Islands, the most enjoyable trip from Cannes.",
       ],
       activites=[
           ("Things to do in Cannes", "Guided tours, tastings, boat trips around the bay.", "Cannes"),
           ("Boat trips from Cannes", "Cruises, catamarans, trips to the Lérins Islands.", "Cannes boat"),
       ],
       faq=[
           ("Can you visit the Palais des Festivals?", "The interior is only open during events or on guided tours run by the tourist office. You can photograph the steps freely."),
           ("Are the beaches in Cannes public?", "There are free public beaches, especially at both ends of the Croisette and next to the Palais, and many private beaches."),
           ("When is the Cannes Film Festival?", "Every year in May, for about twelve days. Screenings are for industry professionals and guests."),
       ]),
    _d(slug="antibes", path="antibes", groupe="mer", nom="Antibes", dept="06", cachet="Alpes-Maritimes", couleur="ocre",
       description="Things to do in Antibes and Juan-les-Pins: ramparts, the Picasso Museum, the Provençal market, Port Vauban and the Cap d'Antibes coastal path.",
       accroche="Ramparts facing the sea, a Picasso museum in a château and one of the most beautiful coastal paths on the Riviera.",
       intro=[
           "Antibes has kept the soul of a small Provençal town, with its old quarter tucked behind the ramparts and its covered market. Port Vauban, one of Europe's largest marinas, welcomes some of the world's biggest yachts.",
           "To the south, Cap d'Antibes unfolds its villas, pines and coves, with Juan-les-Pins on the other side, its sandy beach and its July jazz festival.",
       ],
       a_voir=[
           ("The Picasso Museum", "Housed in the Château Grimaldi on the ramparts, where Picasso worked in 1946. The works from that period stayed here."),
           ("The Provençal market", "Under the covered hall of Cours Masséna in the old town: local produce, olives, flowers and specialities in the morning."),
           ("The ramparts and old town", "Walk along the sea-facing ramparts, then explore the lanes and the Safranier quarter, a village within the town."),
           ("Port Vauban and Fort Carré", "The harbour and its giant yachts, overlooked by Fort Carré, a star-shaped fortress you can visit."),
           ("The Cap d'Antibes coastal path", "A path carved into the rock by the sea, from Garoupe beach towards the tip of the cape. Wild scenery and turquoise water."),
           ("Juan-les-Pins", "Sandy beaches, pine woods and a seaside-resort feel. The Jazz à Juan festival has been held here every summer since the 1960s."),
       ],
       y_aller=[
           ("By train", "Antibes station is on the coastal TER line, about ten minutes from Cannes and twenty from Nice. Juan-les-Pins has its own station."),
           ("By bus", "Local buses link the old town, Cap d'Antibes and Juan-les-Pins. For the coastal path, get off near Garoupe beach."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "May-June and September"), ("Avoid", "The cape path in rough seas"), ("Good for", "Strollers, walkers, art lovers")],
       conseils=[
           "Start with the Provençal market in the morning, then the Picasso Museum, before heading to the cape in the afternoon.",
           "The Cap d'Antibes path is rugged: good shoes are essential, and it is closed in bad weather.",
           "Antibes is halfway between Nice and Cannes: a good base for exploring by train.",
       ],
       activites=[
           ("Things to do in Antibes and Juan-les-Pins", "Guided tours, boat trips, water sports.", "Antibes"),
           ("Boat trips around Cap d'Antibes", "Catamaran, glass-bottom boat, snorkelling trips.", "Cap d'Antibes boat"),
       ],
       faq=[
           ("How long is the Cap d'Antibes coastal path?", "Allow about an hour and a half there and back for the most spectacular section, from Garoupe beach. The ground is uneven and can be slippery."),
           ("Antibes or Juan-les-Pins: where to stay?", "Antibes for the charm of the old town and harbour; Juan-les-Pins for the sandy beach and summer evenings."),
           ("Is the Picasso Museum in Antibes worth it?", "Yes, especially for the setting: a château by the sea, with a sculpture terrace overlooking the Mediterranean."),
       ]),
    _d(slug="villefranche-sur-mer", path="villefranche-sur-mer", groupe="mer", nom="Villefranche-sur-Mer", dept="06", cachet="Alpes-Maritimes", couleur="azur",
       description="Things to do in Villefranche-sur-Mer: the bay, the Cocteau chapel, Rue Obscure, the citadel and the beach. Getting there from Nice.",
       accroche="One of the most beautiful bays in the Mediterranean, a village of ochre and pink façades, and a fishermen's chapel decorated entirely by Cocteau.",
       intro=[
           "A few minutes from Nice, Villefranche-sur-Mer rises above a deep natural harbour sheltered by Cap Ferrat. The colourful houses run down to the fishing port, where you can have a coffee by the water.",
           "The town is small and can be seen on foot in a few hours, which makes it an ideal stop to combine with Saint-Jean-Cap-Ferrat or Monaco.",
       ],
       a_voir=[
           ("The Saint-Pierre chapel", "A small fishermen's chapel on the harbour, decorated entirely by Jean Cocteau in the late 1950s: frescoes, colours and symbols."),
           ("Rue Obscure", "A street entirely covered by medieval vaults. Cool and mysterious, it runs through the old town."),
           ("The Saint-Elme citadel", "A 16th-century fortress now home to the town hall, gardens and several small museums."),
           ("The harbour and seafront", "Terraces and colourful boats at the foot of the old town, the most photographed spot in Villefranche."),
           ("Marinières beach", "A fine sandy beach, rare on this part of the coast, right below the station."),
       ],
       y_aller=[
           ("By train", "Villefranche-sur-Mer station is on the beach, about ten minutes from Nice by TER. By far the easiest option."),
           ("By bus", "Buses link Nice with Villefranche and continue to Saint-Jean-Cap-Ferrat."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Morning, on non-cruise days"), ("Avoid", "Parking in town in summer"), ("Good for", "Everyone")],
       conseils=[
           "Cruise ships anchor in the bay: on those days the town is busy around midday.",
           "Combine Villefranche in the morning with Saint-Jean-Cap-Ferrat in the afternoon.",
           "Take the train rather than the car: parking is scarce and expensive.",
       ],
       activites=[
           ("Things to do in Villefranche-sur-Mer", "Boat trips in the bay, kayaking, snorkelling.", "Villefranche-sur-Mer"),
           ("Riviera day trips", "Villefranche, Èze and Monaco in one day.", "Villefranche Eze Monaco"),
       ],
       faq=[
           ("How do you get from Nice to Villefranche-sur-Mer?", "The TER train takes about ten minutes and the station is on the beach. Buses run too."),
           ("Is there a sandy beach in Villefranche?", "Yes, Marinières beach, right below the station, has fine sand."),
           ("Can you visit the Cocteau chapel?", "Yes, it is open for much of the year for a small fee. Check opening days before you go."),
       ]),
    _d(slug="saint-jean-cap-ferrat", path="saint-jean-cap-ferrat", groupe="mer", nom="Saint-Jean-Cap-Ferrat", dept="06", cachet="Alpes-Maritimes", couleur="pin",
       to="to Cap Ferrat", **{"in": "in Cap Ferrat", "tips_for": "visiting Cap Ferrat"},
       description="Things to do in Saint-Jean-Cap-Ferrat: Villa Ephrussi de Rothschild and its gardens, the coastal path, Paloma beach. Getting there from Nice and Villefranche.",
       accroche="The billionaires' peninsula, but also one of France's most beautiful coastal paths and a pink villa surrounded by nine gardens.",
       intro=[
           "Between Villefranche and Beaulieu, Cap Ferrat juts into the sea, covered in pines and villas hidden behind their gates. The village of Saint-Jean, its small harbour and restaurants keep a relaxed feel.",
           "Most people come for two things: Villa Ephrussi de Rothschild and its gardens, and the path that circles the peninsula at the water's edge.",
       ],
       a_voir=[
           ("Villa Ephrussi de Rothschild", "A pink palace built for Baroness Béatrice de Rothschild in the early 20th century, with its art collections and nine themed gardens overlooking the sea on both sides."),
           ("The coastal path", "The path circles the peninsula and Pointe Saint-Hospice. Coves, clear water and views of Monaco and Italy."),
           ("Saint-Jean harbour", "A small fishing and pleasure harbour with waterside restaurants."),
           ("Paloma beach", "A small sheltered beach, partly public, facing the bay of Beaulieu and the mountains."),
           ("Villa Kérylos, in Beaulieu", "Next door in Beaulieu-sur-Mer, a recreation of an ancient Greek villa set on a rock by the water."),
       ],
       y_aller=[
           ("By train, then on foot", "Get off at Beaulieu-sur-Mer station: Villa Kérylos is close by, and Villa Ephrussi is about a twenty-minute uphill walk."),
           ("By bus", "Buses link Nice with Cap Ferrat via Villefranche."),
           ("By car or with a driver", "Parking is limited on the peninsula, especially in summer. A driver lets you combine the villas and Èze in one day."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "Spring, for the gardens in bloom"), ("Avoid", "The path in the midday heat in summer"), ("Good for", "Garden lovers and walkers")],
       conseils=[
           "Visit Villa Ephrussi in the morning, picnic on the peninsula and keep the afternoon for the path.",
           "The coastal path is closed in rough seas: check the weather before you set off.",
           "Bring a swimsuit: the coves along the path are made for swimming.",
       ],
       activites=[
           ("Villa Ephrussi and the Riviera", "Tickets, guided tours and day trips including Cap Ferrat.", "Villa Ephrussi Rothschild"),
           ("Boat trips around Cap Ferrat", "Sea trips along the villas and coves.", "Cap Ferrat boat"),
       ],
       faq=[
           ("How long does it take to visit Villa Ephrussi?", "Allow about two hours for the villa and gardens, a little more if you linger in the tea room."),
           ("Is the Cap Ferrat coastal path difficult?", "It is easy but long: allow several hours for the full loop. You can do just part of it, for example around Pointe Saint-Hospice."),
           ("Can you swim at Cap Ferrat?", "Yes, at Paloma beach, Passable beach and many coves reached from the path."),
       ]),
    _d(slug="menton", path="menton", groupe="mer", nom="Menton", dept="06", cachet="Alpes-Maritimes", couleur="ocre",
       description="Things to do in Menton: the colourful old town, the Saint-Michel basilica, the Jean Cocteau Museum, the gardens and the Lemon Festival. Getting there from Nice.",
       accroche="The pearl of France, right next to Italy: the mildest town on the coast, with colourful façades, lemons and gardens.",
       intro=[
           "Menton is the last French town before Italy. Its climate, the mildest on the Riviera, lets lemon trees and exotic plants thrive, and draws visitors from the end of winter.",
           "The old town climbs in steps up to the basilica, above the harbour and beaches. Italy is minutes away: Ventimiglia and its market are easy to reach by train.",
       ],
       a_voir=[
           ("The old town", "Yellow, orange and pink houses packed on the hill, stepped lanes and vaulted passages. The view from the harbour is the image of Menton."),
           ("The Saint-Michel-Archange basilica", "A baroque church at the top of a grand staircase, with a pebble-mosaic forecourt. Chamber music concerts are held here in summer."),
           ("The Jean Cocteau Museum", "A contemporary building on the seafront devoted to Cocteau, who loved Menton. The small Bastion museum on the harbour is dedicated to him too."),
           ("The gardens", "Menton is a town of gardens: Serre de la Madone, Val Rahmeh, Fontana Rosa… Plants from all over the world enjoy the climate."),
           ("The covered market", "Menton's market hall, near the old town, for local specialities and the famous lemons."),
       ],
       y_aller=[
           ("By train", "Menton is on the coastal TER line, about forty minutes from Nice via Monaco. Menton-Garavan station is closest to the old town."),
           ("By bus", "Regional buses link Nice and Menton along the Lower Corniche, stopping in Monaco."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "February for the Lemon Festival, then spring"), ("Avoid", "July-August if you dislike the heat"), ("Good for", "Strollers and garden lovers")],
       conseils=[
           "Come in February for the Fête du Citron: giant sculptures made of citrus fruit fill the town. Book accommodation early.",
           "Climb to the basilica through the old town's steps, then go back down to the harbour on the other side.",
           "Combine Menton with Roquebrune-Cap-Martin or a hop over to Italy.",
       ],
       activites=[
           ("Things to do in Menton", "Guided tours, tastings, trips to Italy.", "Menton"),
           ("French-Italian Riviera trips", "Day trips between Menton, Ventimiglia and Sanremo.", "Menton Italy day trip"),
       ],
       faq=[
           ("When is the Menton Lemon Festival?", "Every February for about two weeks, with parades and citrus sculptures in the Biovès gardens."),
           ("Can you go to Italy from Menton?", "Yes, by train: Ventimiglia is minutes away, and the line continues to Sanremo."),
           ("Does Menton have beaches?", "Yes, several pebble and mixed sand-and-pebble beaches on either side of the old town."),
       ]),
    _d(slug="grasse", path="grasse", groupe="villages", nom="Grasse", dept="06", cachet="Alpes-Maritimes", couleur="pin",
       description="Things to do in Grasse, the perfume capital: Fragonard, Molinard and Galimard perfumeries, the International Perfume Museum and the old town. Getting there from Cannes.",
       accroche="The world capital of perfume. Tour the factories, create your own fragrance, and see why jasmine and rose fields are worth their weight in gold.",
       intro=[
           "Perched above Cannes, Grasse has specialised in perfume for centuries. The perfume-making skills of the Pays de Grasse are on UNESCO's list of intangible cultural heritage.",
           "The old town, with its lanes and squares, has stayed authentic. People come to understand how a perfume is born, from the flowers to the bottle.",
       ],
       a_voir=[
           ("The International Perfume Museum", "The history of perfume around the world, from antiquity to today, with bottles, stills and gardens of perfume plants a few kilometres away."),
           ("Fragonard, Molinard and Galimard", "The big houses open their workshops: factory tours, often free, and shops."),
           ("Create your own perfume", "Several houses run one- to two-hour workshops where you compose your fragrance with a perfumer. A unique souvenir."),
           ("The old town and cathedral", "Steep lanes, arcaded squares and a cathedral with paintings by Rubens and by Fragonard, a native of the town."),
           ("Flower festivals", "In May, Expo Rose celebrates the May rose; in August, the Jasmine Festival fills the town."),
       ],
       y_aller=[
           ("By train from Cannes", "A TER line links Cannes and Grasse in about thirty minutes. The station is at the bottom of the town: allow for a climb or take a bus to the centre."),
           ("By bus", "Buses link Grasse with Cannes and Nice."),
           ("By car or with a driver", "Grasse combines easily with Gourdon, Mougins or Saint-Paul-de-Vence."),
       ],
       fiche=[("Time needed", "Half a day to a day"), ("Best time", "May for roses, August for jasmine"), ("Avoid", "Mondays for some museums"), ("Good for", "The curious, families, perfume lovers")],
       conseils=[
           "Book ahead if you want a perfume-making workshop, especially in season.",
           "Factory tours are short: you can easily do two in a row.",
           "Combine Grasse with the hilltop villages of Gourdon or Mougins.",
       ],
       activites=[
           ("Perfume-making workshops", "Compose your own perfume with a Grasse perfumer.", "Grasse perfume workshop"),
           ("Grasse and hilltop village tours", "Grasse, Gourdon and Saint-Paul-de-Vence in a day.", "Grasse day trip"),
       ],
       faq=[
           ("Are the perfumery tours in Grasse free?", "Guided factory tours at the big houses are generally free. Perfume-making workshops are paid."),
           ("How do you get to Grasse from Cannes?", "By TER train, about half an hour, or by bus. By car, allow half an hour without traffic."),
           ("How long is a perfume-making workshop?", "Usually one to two hours, and you leave with your own bottle."),
       ]),
    _d(slug="gourdon", path="gourdon", groupe="villages", nom="Gourdon", dept="06", cachet="Alpes-Maritimes", couleur="encre",
       description="Visiting Gourdon, one of the Most Beautiful Villages in France, perched above the Gorges du Loup with a view over the whole coast. Access, tips and nearby sights.",
       accroche="An eagle's nest on the edge of a cliff above the Gorges du Loup. From its square, the view runs to the sea, from the Esterel to Cap d'Antibes.",
       intro=[
           "Gourdon is listed among the Most Beautiful Villages in France. Clinging to a cliff, it overlooks the Gorges du Loup and offers one of the most impressive panoramas in the hinterland.",
           "The village is tiny: a few lanes, craftspeople, sweet shops and a viewpoint square. You can see it in an hour, then carry on to the gorges and neighbouring villages.",
       ],
       a_voir=[
           ("Place Victoria", "The village viewpoint, on the edge of the cliff. On clear days the view takes in the whole coast."),
           ("The lanes and craftspeople", "Soap makers, perfumers, confectioners and glassblowers occupy the stone houses."),
           ("Gourdon castle", "A medieval fortress above the village, surrounded by terraced gardens."),
           ("The Gorges du Loup", "Below, the road runs through spectacular gorges, with the Courmes waterfall and the Saut du Loup."),
           ("Tourrettes-sur-Loup", "The neighbouring hilltop village, famous for its violets and artists' studios."),
       ],
       y_aller=[
           ("By car or with a driver", "The only real option: Gourdon is about half an hour from Grasse on a mountain road. The car park is at the village entrance."),
           ("By bus", "There is a service from Grasse, but it is infrequent: check times before you go."),
       ],
       fiche=[("Time needed", "One to two hours, a day with the gorges"), ("Best time", "Spring and autumn"), ("Avoid", "Hazy days, when the view disappears"), ("Good for", "Lovers of views and mountain roads")],
       conseils=[
           "Pick a clear day: the view is the main reason to come.",
           "Do a loop: Grasse, Gourdon, Gorges du Loup, Tourrettes-sur-Loup, then back via Vence or Saint-Paul.",
           "The road is winding: take care if you suffer from car sickness.",
       ],
       activites=[
           ("Hilltop villages of the hinterland", "Tours to Grasse, Gourdon and Saint-Paul-de-Vence.", "Gourdon Grasse tour"),
           ("Hiking and canyoning in the Gorges du Loup", "Guided outings in the hinterland.", "Gorges du Loup"),
       ],
       faq=[
           ("Can you get to Gourdon without a car?", "It is difficult: buses are rare. An organised tour or a private driver is more practical."),
           ("How long does it take to visit Gourdon?", "An hour is enough for the village. Allow half a day with the Gorges du Loup and Tourrettes-sur-Loup."),
           ("Is Gourdon one of the Most Beautiful Villages in France?", "Yes, Gourdon is a member of the Plus Beaux Villages de France association."),
       ]),
    _d(slug="mougins", path="mougins", groupe="villages", nom="Mougins", dept="06", cachet="Alpes-Maritimes", couleur="azur",
       description="Visiting Mougins, the hilltop village above Cannes: flowery lanes, galleries, the FAMM museum of women artists and a long gastronomic tradition.",
       accroche="A spiral-shaped village above Cannes, where Picasso spent his last years and where people come as much for the art as for the food.",
       intro=[
           "Mougins winds around its hill a few kilometres from Cannes. Its flowery lanes are lined with galleries and restaurants: the village has been known for its cuisine for decades.",
           "Picasso lived in Mougins from 1961 until his death in 1973. Today the village is home to FAMM, Europe's first private museum devoted to women artists.",
       ],
       a_voir=[
           ("The village lanes", "A circular layout, stone houses covered in flowers and art galleries at every step."),
           ("FAMM", "Opened in 2024 in the former classical art museum, it shows works by women artists from the 19th century to today."),
           ("The wash house and town hall square", "The heart of the village, with shady terraces."),
           ("Mougins' restaurants", "The village has a long gastronomic tradition: plenty of restaurants, from the simplest to the most renowned."),
           ("Notre-Dame-de-Vie chapel", "Away from the village at the end of a cypress avenue, with a view over the countryside. Picasso lived in the farmhouse next door."),
       ],
       y_aller=[
           ("By bus from Cannes", "Buses link Cannes with Mougins village."),
           ("By car or with a driver", "The village is pedestrianised, with car parks at the entrance. Mougins combines well with Grasse or Valbonne."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Evening for dinner, spring for the flowers"), ("Avoid", "The hottest hours in summer"), ("Good for", "Food and art lovers")],
       conseils=[
           "Come in the late afternoon, browse the galleries, then stay for dinner.",
           "Book restaurants ahead in season and during events in Cannes.",
           "Combine Mougins with Grasse, about twenty minutes away.",
       ],
       activites=[
           ("Things to do in Mougins", "Tours, cooking classes, tastings.", "Mougins"),
           ("Cannes and hinterland tours", "Hilltop villages, Grasse and perfume.", "Mougins Grasse tour"),
       ],
       faq=[
           ("How do you get to Mougins from Cannes?", "By bus or by car: the village is about twenty minutes from central Cannes."),
           ("What is FAMM?", "The Femmes Artistes du Musée de Mougins, opened in 2024 and devoted to works by women artists."),
           ("Did Picasso live in Mougins?", "Yes, from 1961 until his death in 1973, in a farmhouse near Notre-Dame-de-Vie chapel."),
       ]),
    _d(slug="biot", path="biot", groupe="villages", nom="Biot", dept="06", cachet="Alpes-Maritimes", couleur="ocre",
       description="Visiting Biot: the glassworks and its bubble glass, the Fernand Léger National Museum, Place des Arcades and craft workshops. Getting there from Antibes.",
       accroche="The glassblowers' village. Watch bubble glass being blown, wander between workshops and discover Fernand Léger's colours.",
       intro=[
           "Biot is a hilltop village between Antibes and Valbonne, known worldwide for its bubble glass, born here in the mid-20th century. Glassblowers' and potters' workshops made its name.",
           "At the foot of the village, the Fernand Léger National Museum, its façade covered by a huge colourful mosaic, is one of the most unusual museums on the coast.",
       ],
       a_voir=[
           ("The Biot glassworks", "Watch the glassblowers at work and learn the bubble-glass technique. Shop and gallery on site."),
           ("The Fernand Léger National Museum", "A museum devoted entirely to the painter, with its great mosaic façade and gardens."),
           ("Place des Arcades", "The heart of the village, with medieval arcades and terraces."),
           ("Craft workshops", "Glassmakers, potters, goldsmiths: Biot's lanes are full of workshops open to the public."),
       ],
       y_aller=[
           ("By train, then bus", "Biot station is by the sea; buses then climb up to the village."),
           ("By car or with a driver", "Biot is about fifteen minutes from Antibes. Car parks at the village entrance."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "All year round"), ("Avoid", "The steep lanes with a pushchair"), ("Good for", "Families, craft and art lovers")],
       conseils=[
           "Start with the glassworks below the village to see the glassblowers at work.",
           "The Fernand Léger museum combines easily with a visit to the village.",
           "Biot pairs well with Antibes or Saint-Paul-de-Vence on the same day.",
       ],
       activites=[
           ("Things to do in Biot and Antibes", "Tours, workshops and outings around Antibes.", "Biot"),
           ("French Riviera hilltop villages", "Tours between Biot, Saint-Paul and Èze.", "French Riviera hilltop villages"),
       ],
       faq=[
           ("What is Biot bubble glass?", "Glass with air bubbles deliberately trapped inside, which became the signature of Biot's glassworks."),
           ("Can you watch glassblowers in Biot?", "Yes, the glassworks lets you watch the glassmakers at work in the workshop."),
           ("How do you get to Biot without a car?", "By train to Biot station, then by bus up to the village."),
       ]),
    _d(slug="roquebrune-cap-martin", path="roquebrune-cap-martin", groupe="villages", nom="Roquebrune-Cap-Martin", dept="06", cachet="Alpes-Maritimes", couleur="pin",
       description="Visiting Roquebrune-Cap-Martin: the medieval castle, the hilltop village, the Le Corbusier coastal path and Cap Martin. Getting there from Monaco and Menton.",
       accroche="A medieval village perched above Monaco and a pine-covered cape where Le Corbusier spent his summers in a cabin.",
       intro=[
           "Roquebrune-Cap-Martin is split between a hilltop village built around a medieval castle and Cap Martin, a wooded peninsula between Monaco and Menton.",
           "It is one of the best-preserved spots on the Riviera, ideal for a quieter day than Monaco, just minutes away.",
       ],
       a_voir=[
           ("Roquebrune castle", "A medieval keep at the top of the village, with a plunging view over Monaco and the sea."),
           ("The hilltop village", "Vaulted lanes and steps cut into the rock, such as Rue Moncollet."),
           ("The thousand-year-old olive tree", "One of the oldest olive trees in the region, on the way to Menton below the village."),
           ("Promenade Le Corbusier", "The Cap Martin coastal path runs along the sea among the pines. Le Corbusier had his cabin here, a UNESCO World Heritage site; it can be visited on booked guided tours."),
       ],
       y_aller=[
           ("By train", "Roquebrune-Cap-Martin and Carnolès stations are served by TER trains between Nice and Menton."),
           ("On foot from Monaco", "The village is a good walk from Monaco, uphill. You can also reach Cap Martin along the seafront."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Spring and autumn"), ("Avoid", "Climbing to the village in the full heat"), ("Good for", "Walkers and architecture lovers")],
       conseils=[
           "Walk the coastal path in the morning, when it is in the shade and quiet.",
           "Book the Cap Moderne tour ahead if you want to see Le Corbusier's cabin.",
           "Combine Roquebrune with Monaco or Menton on the same day.",
       ],
       activites=[
           ("Things to do between Monaco and Menton", "Guided tours, hikes, boat trips.", "Roquebrune-Cap-Martin"),
           ("Monaco and eastern Riviera tours", "Monaco, Roquebrune, Menton and Italy.", "Monaco Menton day trip"),
       ],
       faq=[
           ("Can you visit Le Corbusier's cabin?", "Yes, only on a booked guided tour with the Cap Moderne site."),
           ("How long is the Promenade Le Corbusier?", "Allow one to two hours depending on the section, on an easy seaside path."),
           ("How do you get to Roquebrune from Monaco?", "By train to Roquebrune-Cap-Martin station or on foot along the seafront."),
       ]),
    _d(slug="massif-de-l-esterel", path="esterel-massif", groupe="nature", nom="Esterel Massif", dept="83", cachet="Var", couleur="ocre",
       h1="Discovering the Esterel Massif", **{"in": "in the Esterel", "to": "to the Esterel", "tips_for": "visiting the Esterel"},
       description="Discover the Esterel Massif: the Corniche d'Or, red rocks, Pic de l'Ours, Cap Roux and the coves. Hikes, access and summer fire-risk rules.",
       accroche="Red rocks plunging into a turquoise sea: between Cannes and Saint-Raphaël, the wildest landscape on the French Riviera.",
       intro=[
           "The Esterel is a volcanic massif whose rock, rhyolite, gives it its striking red colour. It stretches between Mandelieu and Saint-Raphaël, across the Var and the Alpes-Maritimes.",
           "Discover it by car along the Corniche d'Or, on foot along its trails, or from the sea, where the red coves are most spectacular.",
       ],
       a_voir=[
           ("The Corniche d'Or", "The coast road between Mandelieu-la-Napoule and Saint-Raphaël, cut into the red rock above the sea. One of the most beautiful roads in France."),
           ("Pic de l'Ours", "One of the massif's summits, with a view over the whole coast to Cannes and the Alps."),
           ("Cap Roux", "One of the most spectacular headlands, reached by a hike from the Corniche."),
           ("The coves of Anthéor and Le Trayas", "Small coves between the red rocks, with very clear water."),
           ("Agay beaches", "A sheltered bay at the foot of the red Rastel d'Agay rock."),
       ],
       y_aller=[
           ("By car or with a driver", "The Corniche d'Or is best driven, with plenty of places to stop. Allow an hour from Cannes with stops."),
           ("By train", "TER trains between Cannes and Saint-Raphaël stop at a few small stations in the massif, such as Agay and Le Trayas, starting points for hikes."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "Spring and autumn"), ("Avoid", "High fire-risk days in summer"), ("Good for", "Hikers and nature lovers")],
       conseils=[
           "In summer, access to the massif depends on the fire risk and can be banned on some days: check the map published every evening by the Var prefecture before you go.",
           "The massif is closed at night all year round. Set off early, with water and sun protection.",
           "To see the coves at their best, take a boat trip from Cannes or Saint-Raphaël.",
       ],
       activites=[
           ("Hikes and outings in the Esterel", "Guided hikes, mountain biking, kayaking along the red rocks.", "Esterel"),
           ("Boat trips along the Esterel", "Sea trips to see the coves from the water.", "Esterel boat"),
       ],
       faq=[
           ("Is the Esterel Massif open in summer?", "From 21 June to 30 September, access depends on the day's fire risk and can be banned in strong wind or heat. Check the prefecture's map the day before."),
           ("Why are the Esterel rocks red?", "The massif is volcanic: its main rock, rhyolite, has that distinctive red colour."),
           ("Can you visit the Esterel without a car?", "Yes, by train to Agay or Le Trayas, where trails start. The Corniche viewpoints are easier by car."),
       ]),
    _d(slug="porquerolles", path="porquerolles", groupe="nature", nom="Porquerolles", dept="83", cachet="Var", couleur="azur",
       to="to Porquerolles", **{"in": "on Porquerolles"},
       description="Visiting Porquerolles island: Notre-Dame and Argent beaches, cycling, Fort Sainte-Agathe, Villa Carmignac. Ferry from La Tour Fondue and summer booking.",
       accroche="A car-free island with white-sand beaches and Caribbean-clear water, in the heart of a national park.",
       intro=[
           "Porquerolles is the largest of the Îles d'Hyères, off the Giens peninsula. It is part of Port-Cros National Park: no cars, cycle paths, forests and some of the most beautiful beaches in France.",
           "Explore the island by bike or on foot from the village and its harbour. To protect it, visitor numbers are capped on the busiest summer days.",
       ],
       a_voir=[
           ("Notre-Dame beach", "A long fine-sand beach lined with pines, often listed among the best in Europe. Just under an hour on foot or a quarter of an hour by bike from the village."),
           ("Argent beach", "Closer to the village, with pale sand and transparent water."),
           ("Fort Sainte-Agathe", "The fort above the harbour, with a view over the whole island and the mainland."),
           ("Villa Carmignac", "A contemporary art foundation in a villa among the vines. You visit barefoot; booking is recommended."),
           ("The cycle paths", "A network of forest tracks links beaches, the lighthouse and coves. Bike hire in the village."),
       ],
       y_aller=[
           ("By boat from La Tour Fondue", "Shuttles leave from La Tour Fondue harbour at the tip of the Giens peninsula all year round. The crossing takes about twenty minutes."),
           ("Book in summer", "In July-August visitor numbers are capped at around 6,000 a day: book your crossing in advance."),
           ("From other ports", "In season, boats also leave from Hyères, Toulon and Le Lavandou."),
       ],
       fiche=[("Time needed", "One day"), ("Best time", "May-June and September"), ("Avoid", "August days without a booking"), ("Good for", "Families, cyclists, swimmers")],
       conseils=[
           "Hire a bike as soon as you arrive and head for Notre-Dame beach before the crowds.",
           "Bring plenty of water: the tracks get very hot in summer.",
           "Paths may be closed when the fire risk is high.",
       ],
       activites=[
           ("Porquerolles trips", "Crossings, days on the island, bike hire.", "Porquerolles"),
           ("Boat trips around the Îles d'Hyères", "Porquerolles, Port-Cros and snorkelling trips.", "Hyeres islands boat"),
       ],
       faq=[
           ("Do you need to book the ferry to Porquerolles?", "In July and August it is strongly recommended: visitor numbers are capped at around 6,000 a day."),
           ("Can you take a car to Porquerolles?", "No, visitors' cars are not allowed on the island. Leave yours at La Tour Fondue car park."),
           ("How long is the crossing to Porquerolles?", "About twenty minutes from La Tour Fondue on the Giens peninsula."),
       ]),
    _d(slug="gorges-du-verdon", path="verdon-gorge", groupe="nature", nom="Verdon Gorge", dept="04", cachet="Verdon", couleur="pin",
       h1="Visiting the Verdon Gorge", **{"in": "in the Verdon Gorge", "to": "to the Verdon Gorge", "tips_for": "visiting the Verdon Gorge"},
       description="Day trip to the Verdon Gorge from the French Riviera: the canyon, Lake Sainte-Croix, Moustiers-Sainte-Marie and the Route des Crêtes. Tips and activities.",
       accroche="Europe's largest canyon, emerald-green water and dizzying cliffs, two hours from the Riviera.",
       intro=[
           "The Verdon Gorge is the essential nature trip from the French Riviera. Over some twenty kilometres the river has carved a canyon with cliffs several hundred metres high.",
           "Where the gorge ends, Lake Sainte-Croix and its turquoise water are perfect for swimming and pedal boats. Nearby, Moustiers-Sainte-Marie is one of the most beautiful villages in Provence.",
       ],
       a_voir=[
           ("The Route des Crêtes", "A loop from La Palud-sur-Verdon with viewpoints on the edge of the drop. The most impressive views of the canyon."),
           ("Lake Sainte-Croix", "A huge reservoir with turquoise water, beaches, pedal boats and canoes."),
           ("Pont du Galetas", "At the mouth of the gorge, where the canyon opens onto the lake. Starting point for electric boat and canoe trips into the gorge."),
           ("Moustiers-Sainte-Marie", "A village at the foot of a cliff, famous for its faience and the star hanging above it."),
           ("The Blanc-Martel trail", "The great hike along the bottom of the gorge, for experienced walkers: a full day, with tunnel sections."),
       ],
       y_aller=[
           ("By car or with a driver", "Allow about two to two and a half hours from Nice or Cannes. You need a full day."),
           ("On an organised tour", "Without a car it is the simplest option: many tours leave from Nice and Cannes."),
       ],
       fiche=[("Time needed", "A long day"), ("Best time", "June and September"), ("Avoid", "Pont du Galetas on an August Sunday"), ("Good for", "Nature lovers, families, active types")],
       conseils=[
           "Leave very early to enjoy the viewpoints before the crowds and find a space at Pont du Galetas.",
           "Pedal boat and canoe hire is in high demand in summer: arrive when they open.",
           "Swimming in the Verdon can be dangerous because of water releases from the dams: follow the signs.",
       ],
       activites=[
           ("Verdon Gorge day trips", "Days from Nice or Cannes, including Moustiers.", "Verdon Gorge"),
           ("Canoeing, rafting and canyoning in the Verdon", "Guided activities in the gorge.", "Verdon canoe rafting"),
       ],
       faq=[
           ("Can you do the Verdon Gorge as a day trip from Nice?", "Yes, but it is a long day: about two hours' drive each way. An organised tour saves you the driving."),
           ("Can you swim in the Verdon Gorge?", "Yes, especially in Lake Sainte-Croix. In the gorge, watch out for dam water releases that suddenly raise the water level."),
           ("When is the best time to visit the Verdon?", "June and September: good weather, warm water and fewer people than in July-August."),
       ]),
]

ITINERAIRE = {
    "slug": "3-days",
    "titre": "The French Riviera in 3 days",
    "description": "A 3-day French Riviera itinerary you can do without a car: Nice, Villefranche, Èze, Monaco, Cannes and the Lérins Islands. Tips and a driving alternative.",
    "accroche": "Three days, a coastal train and the best of the Riviera. This itinerary works entirely without a car, with Nice as your base.",
    "jours": [
        ("Day 1: Nice and Villefranche-sur-Mer", [
            ("nice", "In the morning, the Cours Saleya market and the lanes of Old Nice, then up Castle Hill for the view over the bay."),
            ("villefranche-sur-mer", "In the afternoon, ten minutes by train to Villefranche: the Cocteau chapel, Rue Obscure and a swim at Marinières beach."),
        ]),
        ("Day 2: Èze and Monaco", [
            ("eze", "Leave early for Èze, before the coaches arrive: the village lanes and the garden at the top."),
            ("monaco", "Head down to Monaco for the changing of the guard at 11:55, then the Oceanographic Museum, Port Hercule and Casino Square at the end of the day."),
        ]),
        ("Day 3: Cannes and the Lérins Islands", [
            ("cannes", "Train to Cannes, the Forville market and a climb up Le Suquet in the morning."),
            ("iles-de-lerins", "Boat from Quai Laubeuf to Sainte-Marguerite: Fort Royal, the coastal path and a swim in the coves. Back for the Croisette at sunset."),
        ]),
    ],
    "variante": "With a car or a driver, swap day 3 for the hinterland: Grasse and its perfumeries in the morning, Gourdon and its views at lunchtime, then Saint-Paul-de-Vence in the late afternoon.",
    "variante_liens": ["grasse", "gourdon", "saint-paul-de-vence"],
}

TITRES = {
    "monaco": "Things to Do in Monaco: A Practical Day Guide",
    "eze": "Things to Do in Èze: Garden, Nietzsche Path, Tips",
    "iles-de-lerins": "Lérins Islands: Visiting and Ferries from Cannes",
    "saint-paul-de-vence": "Saint-Paul-de-Vence: What to See and Tips",
    "saint-tropez": "Things to Do in Saint-Tropez and How to Get There",
    "nice": "Things to Do in Nice: Old Town, Castle Hill",
    "cannes": "Things to Do in Cannes: Croisette, Suquet, Islands",
    "antibes": "Things to Do in Antibes: Old Town, Picasso, Cape",
    "villefranche-sur-mer": "Things to Do in Villefranche-sur-Mer",
    "saint-jean-cap-ferrat": "Cap Ferrat: Villa Ephrussi and the Coastal Path",
    "menton": "Things to Do in Menton: Old Town, Lemons, Gardens",
    "grasse": "Things to Do in Grasse: Perfumeries and Old Town",
    "gourdon": "Gourdon: Hilltop Village above the Gorges du Loup",
    "mougins": "Things to Do in Mougins: Hilltop Village and FAMM",
    "biot": "Things to Do in Biot: Glassworks and Léger Museum",
    "roquebrune-cap-martin": "Roquebrune-Cap-Martin: What to See and Do",
    "massif-de-l-esterel": "Esterel Massif: Corniche d'Or, Red Rocks, Hikes",
    "porquerolles": "Porquerolles Island: Beaches, Bikes and Ferries",
    "gorges-du-verdon": "Verdon Gorge Day Trip from the French Riviera",
}
TITRE_REGION = "French Riviera Travel Guide: The Best Places"
TITRE_ITI = "French Riviera in 3 Days Without a Car"

ALIAS = {
    "monaco": ["Monaco"], "eze": ["Èze"], "iles-de-lerins": ["Lérins Islands"], "saint-paul-de-vence": ["Saint-Paul-de-Vence", "Saint-Paul"],
    "saint-tropez": ["Saint-Tropez"], "nice": ["Nice"], "cannes": ["Cannes"], "antibes": ["Antibes"],
    "villefranche-sur-mer": ["Villefranche-sur-Mer", "Villefranche"], "saint-jean-cap-ferrat": ["Saint-Jean-Cap-Ferrat", "Cap Ferrat"],
    "menton": ["Menton"], "grasse": ["Grasse"], "gourdon": ["Gourdon"], "mougins": ["Mougins"], "biot": ["Biot"],
    "roquebrune-cap-martin": ["Roquebrune-Cap-Martin", "Roquebrune"], "massif-de-l-esterel": ["Esterel"],
    "porquerolles": ["Porquerolles"], "gorges-du-verdon": ["Verdon Gorge", "Verdon"],
}

ABOUT = [
    "Clic&Site is a practical guide to the most beautiful places in France. Each page answers the three questions you ask before a day out: what is there to see, how do you get there, and when should you go to avoid the crowds.",
    "The guide is published in Cannes by a team that works in passenger transport across the French Riviera. Our advice on access, traffic and the best times comes from there: from year-round trips to these villages, harbours and islands.",
    "We give no prices or exact timetables, because they change often: we would rather point you to the official sites and booking platforms that keep them up to date.",
    "Clic&Site is funded by affiliate links: when you book an activity after clicking one of our links, the platform pays us a commission at no extra cost to you. It does not change what we recommend.",
    "We are starting with the French Riviera, which we know best. Other regions will follow one by one.",
]
