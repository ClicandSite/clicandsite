# Paris region — English edition (11/11/2026). Same facts as the French edition.

REGION = {
    "slug": "paris", "path": "paris", "nom": "Paris",
    "timbre": "Île-de-France",
    "photo": "paris",
    "photo_alt": "The Eiffel Tower and the rooftops of Paris",
    "description": "Eiffel Tower, Louvre, Notre-Dame, Sainte-Chapelle, Montmartre, Orsay, Versailles: practical guides to Paris, what to book and when to go.",
    "accroche": "Paris works all year round, and winter is the best season for museums. You just need to know what to book, which day each place is closed and when to turn up.",
    "intro": [
        "Paris is the most visited city in the world, and it shows: most major sights now ask you to book a time slot, even when entry is free. The good news is that almost everything is less than half an hour apart by metro, and the great monuments line the Seine.",
        "Remember three closing days: the Louvre is closed on Tuesdays, Orsay and Versailles on Mondays. From November to March the queues are shorter, several monuments are free on the first Sunday of the month and late museum openings let you end the day indoors. Each guide below tells you what to book, how to get there and when to go.",
    ],
    "h1": "Visiting Paris", "de": "Paris", "autres": "More places in Paris", "couleur": "encre",
    "locality": "Paris", "address_region": "Île-de-France",
    "departements": ["75", "77", "78"],
}

GROUPES = [
    ("monuments", "Monuments and views"),
    ("musees", "Museums and palaces"),
    ("quartiers", "Neighbourhoods and walks"),
    ('sorties', 'Days out and seasonal'),
]

VEDETTES = ["tour-eiffel", "louvre", "notre-dame", "montmartre", "musee-d-orsay", "versailles"]

def _d(**k):
    k.setdefault("region", "paris")
    k.setdefault("dept", "75")
    k.setdefault("cachet", "Paris")
    return k

DESTINATIONS = [
    _d(slug="tour-eiffel", path="eiffel-tower", groupe="monuments", nom="Eiffel Tower", couleur="encre", h1="Visiting the Eiffel Tower",
       in_="at the Eiffel Tower", to="to the Eiffel Tower", tips_for="visiting the Eiffel Tower",
       description="Visiting the Eiffel Tower: booking tickets, stairs or lift, getting to the top, the best viewpoints and how to get there.",
       accroche="Three levels, over 300 metres and the most famous view in Paris. Plan ahead: official tickets, the right time slot and, if your legs are up to it, the stairs.",
       intro=[
           "Built by Gustave Eiffel for the 1889 World's Fair, the tower was meant to be taken down twenty years later. It has three levels: the 1st floor with its glass floor, the 2nd floor, where the view is easiest to read, and the top, reached by lift only.",
           "You can walk up to the 2nd floor — 674 steps — then take the lift to the top. Either way, buy your tickets on the official website: fake ticketing sites imitate the tower and sell tickets that cannot be used.",
       ],
       a_voir=[
           ("The 1st floor and its glass floor", "The largest level, with a glass floor 57 metres above the ground and panels on how the tower was built. It is also the least crowded."),
           ("The 2nd floor", "For many, the best view: high enough to take in all of Paris, low enough to pick out every monument from Montmartre to Les Invalides."),
           ("The top", "Reached only by lift from the 2nd floor. You can see Gustave Eiffel's reconstructed office and, on a clear day, for dozens of kilometres."),
           ("The evening sparkle", "Every hour after dark, the tower sparkles for five minutes. It is best watched from the ground."),
           ("Trocadéro and the Champ de Mars", "The two esplanades on either side give the classic photos: Trocadéro facing the tower, the Champ de Mars to see its full height."),
       ],
       y_aller=[
           ("By metro and RER", "Bir-Hakeim (line 6) and Trocadéro (lines 6 and 9), or Champ de Mars - Tour Eiffel on RER C. Arriving via Trocadéro gives you the best first view."),
           ("By boat", "Seine boats and the Batobus stop at the foot of the tower, so you can combine your visit with a cruise."),
           ("By taxi or with a driver", "Traffic and drop-offs right by the tower are difficult; ask to be dropped on Quai Branly or at Trocadéro."),
       ],
       fiche=[("Time needed", "2 to 3 hours"), ("Best time", "At opening, or at sunset"), ("Booking", "Yes, on the official website"), ("Good for", "Everyone; stairs for keen walkers")],
       conseils=[
           "Book as early as you can: summit slots sell out fast during school holidays.",
           "On an overcast day, skip the top: the 2nd floor is enough and the view is better below the clouds.",
           "Security checks take time; bring a small bag and arrive a little before your slot.",
       ],
       activites=[
           ("Eiffel Tower tickets and tours", "Summit access, guided climbs, skip-the-line tours.", "Eiffel Tower"),
           ("Eiffel Tower and Seine cruise", "Combined tickets with a boat at the foot of the tower.", "Eiffel Tower Seine cruise"),
       ],
       faq=[
           ("Do I need to book the Eiffel Tower?", "It is strongly recommended, and climbing the stairs now has to be booked too. Buy only on the official website or from a recognised reseller."),
           ("Can you walk to the top of the Eiffel Tower?", "No. The stairs go to the 2nd floor (674 steps); the top is reached by lift from there."),
           ("When does the Eiffel Tower sparkle?", "Every hour after dark, for five minutes, until closing time."),
       ]),

    _d(slug="louvre", path="louvre", groupe="musees", nom="Louvre", couleur="ocre", h1="Visiting the Louvre",
       in_="at the Louvre", to="to the Louvre", tips_for="visiting the Louvre",
       description="Visiting the Louvre: compulsory booking, closing day, late openings, entrances and a route to see the Mona Lisa and the masterpieces without wearing yourself out.",
       accroche="You cannot see the world's largest museum in one go: you plan it. Book your time slot, pick three or four sections and avoid Tuesday, when it is closed.",
       intro=[
           "Once the palace of the kings of France, the Louvre holds collections from Antiquity to the 19th century across three wings: Denon, Sully and Richelieu. The Mona Lisa, the Venus de Milo and the Winged Victory of Samothrace are the stars, but they are a tiny part of what there is to see.",
           "Booking a time slot is compulsory, including for visitors who get in free. The museum is closed on Tuesdays and stays open late on Wednesday and Friday evenings, which are often quieter.",
       ],
       a_voir=[
           ("The Mona Lisa", "In the Salle des États, Denon wing. The queue forms in front of the painting: go there first at opening time, or at the end of a late opening."),
           ("The Winged Victory of Samothrace", "At the top of the Daru staircase, one of the most dramatic displays in the museum."),
           ("The Venus de Milo", "In the Greek galleries of the Sully wing, on the ground floor."),
           ("The great French paintings", "The Raft of the Medusa, Liberty Leading the People, the Coronation of Napoleon: the large-format gallery in the Denon wing, right next to the Mona Lisa."),
           ("Napoleon III's apartments", "Gilding, chandeliers and state rooms in the Richelieu wing, usually less crowded."),
           ("The Pyramid and Cour Napoléon", "I. M. Pei's glass pyramid, worth seeing from outside by day and by night."),
       ],
       y_aller=[
           ("By metro", "Palais-Royal - Musée du Louvre (lines 1 and 7). Louvre - Rivoli on line 1 is a little further."),
           ("Which entrance?", "The main entrance is under the Pyramid. The Carrousel entrance, at 99 Rue de Rivoli, is indoors and handy when it rains. Follow the instructions on your ticket."),
           ("On foot", "The museum is a few minutes from the Pont des Arts, the Tuileries and the Île de la Cité."),
       ],
       fiche=[("Time needed", "3 hours to a full day"), ("Closed", "Tuesdays"), ("Late openings", "Wednesday and Friday"), ("Booking", "Yes, compulsory")],
       conseils=[
           "Plan your route before you go in: three well-prepared hours beat a day of wandering.",
           "Save the Mona Lisa for opening time or the end of a late opening; the rest of the museum is far calmer.",
           "There are cafés and restaurants inside: take a proper break to keep going.",
       ],
       activites=[
           ("Louvre guided tours", "Small-group masterpiece tours with entry included.", "Louvre guided tour"),
           ("Louvre entry tickets", "Timed tickets and combined offers.", "Louvre Museum ticket"),
       ],
       faq=[
           ("What day is the Louvre closed?", "Tuesdays, plus a few public holidays. It stays open late on Wednesday and Friday."),
           ("Do I need to book the Louvre?", "Yes, a time slot is compulsory for every visitor, even those who get in free."),
           ("How long do you need at the Louvre?", "Allow three hours for the main masterpieces. A whole day is not enough to see everything: better to come back."),
       ]),

    _d(slug="notre-dame", path="notre-dame", groupe="monuments", nom="Notre-Dame", couleur="azur", h1="Visiting Notre-Dame de Paris",
       in_="at Notre-Dame", to="to Notre-Dame", tips_for="visiting Notre-Dame",
       description="Visiting Notre-Dame de Paris since it reopened: free entry, recommended booking, towers and crypt, late opening and how to get there.",
       accroche="Reopened in December 2024 after the fire, the cathedral has its pale stone and its light back. Entry is free; booking a slot saves a lot of time.",
       intro=[
           "Restored in five years after the April 2019 fire, Notre-Dame reopened in December 2024. The nave, cleaned of centuries of dust, is brighter than anyone alive remembers, and Viollet-le-Duc's spire has been rebuilt exactly as it was.",
           "Entry to the cathedral is free. A free booking system, opening two to three days ahead, lets you skip the queue; it is most useful from April to October. The towers and the archaeological crypt are paid for separately.",
       ],
       a_voir=[
           ("The nave and choir", "The new liturgical furniture, the rose windows and the restored side chapels. Take time to look up at the vaults."),
           ("The rose windows", "The three great medieval rose windows survived the fire. The south rose is brightest in late morning."),
           ("The towers", "After several hundred steps, the gallery of chimeras and a view over the Île de la Cité. Separate ticket and booking."),
           ("The archaeological crypt", "Under the square, the remains of ancient Lutetia and medieval Paris."),
           ("Square Jean-XXIII", "Behind the cathedral, the best view of the apse and the flying buttresses."),
       ],
       y_aller=[
           ("By metro and RER", "Cité (line 4) or Saint-Michel - Notre-Dame (RER B and C). The cathedral is a few minutes' walk away."),
           ("On foot", "From the Latin Quarter, the Marais or the Louvre, the bridges take you to the Île de la Cité in a quarter of an hour."),
       ],
       fiche=[("Time needed", "1 hour, 2 with the towers"), ("Entry", "Free"), ("Booking", "Recommended, free"), ("Open", "Daily, late on Thursdays")],
       conseils=[
           "Book your free slot as soon as it opens, two to three days ahead: they go fast.",
           "Combine it with the Sainte-Chapelle, five minutes' walk away on the same island.",
           "Dress modestly; services go on during visiting hours, so keep your voice down.",
       ],
       activites=[
           ("Notre-Dame and Île de la Cité guided tours", "The story of the cathedral, the fire and the restoration.", "Notre-Dame guided tour"),
           ("Notre-Dame, Sainte-Chapelle and Conciergerie", "Combined tours of the Île de la Cité in half a day.", "Notre-Dame Sainte-Chapelle"),
       ],
       faq=[
           ("Is Notre-Dame free to visit?", "Yes, entry to the cathedral is free. Only the towers and the archaeological crypt charge admission."),
           ("Do I need to book Notre-Dame?", "It is not compulsory, but booking a free slot avoids a long wait, especially from April to October."),
           ("Can you climb Notre-Dame's towers?", "Yes, with a paid ticket and a booking. There are several hundred steps and no lift."),
       ]),

    _d(slug="sainte-chapelle", path="sainte-chapelle", groupe="monuments", nom="Sainte-Chapelle", couleur="pin", h1="Visiting the Sainte-Chapelle",
       in_="at the Sainte-Chapelle", to="to the Sainte-Chapelle", tips_for="visiting the Sainte-Chapelle",
       description="Visiting the Sainte-Chapelle in Paris: compulsory time slot, security check, the best time for the stained glass, combined ticket with the Conciergerie.",
       accroche="Fifteen windows, over a thousand stained-glass scenes and hardly any wall. On a sunny day, the upper chapel is one of the most beautiful interiors in the world.",
       intro=[
           "Saint Louis built the Sainte-Chapelle in the 13th century to house the Crown of Thorns. Today it stands in the middle of the Palais de Justice on the Île de la Cité, which is why there is an airport-style security check at the entrance.",
           "Booking a time slot is compulsory, even for visitors who get in free. Your slot is valid for half an hour. A combined ticket also covers the neighbouring Conciergerie, the former palace that became Marie-Antoinette's prison.",
       ],
       a_voir=[
           ("The upper chapel", "The heart of the visit: fifteen huge windows telling the Bible from Genesis to the Passion. The later west rose shows the Apocalypse."),
           ("The lower chapel", "Once used by the palace staff, with its blue vault scattered with fleurs-de-lis."),
           ("The Conciergerie", "Next door, the great Gothic Hall of the Men-at-Arms and Marie-Antoinette's reconstructed cell."),
       ],
       y_aller=[
           ("By metro and RER", "Cité (line 4), two minutes away, or Saint-Michel - Notre-Dame (RER B and C), across the bridge."),
           ("Which entrance?", "Visitors go in on Boulevard du Palais, through the Palais de Justice security check. Large suitcases are refused."),
       ],
       fiche=[("Time needed", "45 minutes to 1 hour"), ("Best time", "A sunny day, late morning"), ("Booking", "Yes, compulsory"), ("Good for", "Everyone; lift on request")],
       conseils=[
           "Pick a sunny day if you can: the windows change completely with the light.",
           "Arrive about twenty minutes before your slot to get through security without stress.",
           "Classical concerts are held in the upper chapel in the evening: another way to see it.",
       ],
       activites=[
           ("Sainte-Chapelle and Conciergerie tickets", "Timed entry and combined tickets.", "Sainte-Chapelle ticket"),
           ("Concerts at the Sainte-Chapelle", "Classical music under the stained glass, in the evening.", "Sainte-Chapelle concert"),
       ],
       faq=[
           ("Do I need to book the Sainte-Chapelle?", "Yes, a time slot is compulsory for everyone, including free entry and Paris Museum Pass holders."),
           ("How long does the visit take?", "Allow 45 minutes to an hour, plus the security check, and an extra hour with the Conciergerie."),
           ("Is the Sainte-Chapelle free on the first Sunday of the month?", "Yes, from November to March, but you still have to book a slot."),
       ]),

    _d(slug="montmartre", path="montmartre", groupe="quartiers", nom="Montmartre", couleur="ocre", h1="Visiting Montmartre and the Sacré-Cœur",
       in_="in Montmartre", to="to Montmartre", tips_for="visiting Montmartre",
       description="Visiting Montmartre: the Sacré-Cœur and its dome, Place du Tertre, the vineyard, the Montmartre Museum. How to get up the hill and avoid the scams.",
       accroche="A village on a hill above Paris: steps, vines, painters' studios and, at the top, the white basilica of the Sacré-Cœur.",
       intro=[
           "Montmartre is the highest point in Paris. Once a village of windmills and vineyards, it drew Renoir, Picasso, Toulouse-Lautrec and Van Gogh at the end of the 19th century. Place du Tertre has become very touristy, but the streets on the far side of the hill are still quiet.",
           "Entry to the Sacré-Cœur basilica is free. The dome costs extra: about 300 steps, no lift, for one of the best views of the city. The funicular saves you the steps from Square Louise-Michel for the price of a metro ticket.",
       ],
       a_voir=[
           ("The Sacré-Cœur basilica", "Free entry, with one of the largest mosaics in France above the choir. The forecourt looks out over the whole city."),
           ("The dome", "About 300 spiral steps, then an open-air gallery around the cupola: the highest view in Paris after the Eiffel Tower."),
           ("Place du Tertre", "Painters and portrait artists at work. Very busy in the afternoon; nicer early in the morning."),
           ("The Montmartre Museum", "In the oldest house on the hill, with Suzanne Valadon's studio and the Renoir gardens."),
           ("The vineyard and Rue de l'Abreuvoir", "The Clos Montmartre, La Maison Rose and the cobbled streets on the north side, much quieter."),
           ("The Wall of Love", "In Square Jehan-Rictus, Place des Abbesses: \"I love you\" written in hundreds of languages."),
       ],
       y_aller=[
           ("By metro", "Anvers (line 2) for the funicular and the Sacré-Cœur, or Abbesses (line 12) to walk up through the village."),
           ("By funicular", "It links the bottom of the hill to the Sacré-Cœur forecourt with an ordinary metro ticket."),
           ("On foot", "From Abbesses, allow a quarter of an hour uphill via Rue des Abbesses and Rue Lepic."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Early morning, or sunset"), ("Sacré-Cœur entry", "Free"), ("Good for", "Keen walkers; funicular for the rest")],
       conseils=[
           "Walk up from Abbesses and come down the Sacré-Cœur steps: the climb is gentler and prettier.",
           "At the foot of the steps, ignore anyone trying to tie a bracelet on your wrist, and watch your pockets in the crowd.",
           "Sunset from the forecourt is magical, but everyone has the same idea: arrive early.",
       ],
       activites=[
           ("Montmartre guided tours", "Small-group walks in the painters' footsteps.", "Montmartre walking tour"),
           ("Montmartre food tours", "Tastings: cheese, wine and the hill's bakeries.", "Montmartre food tour"),
       ],
       faq=[
           ("Is the Sacré-Cœur free?", "Yes. Only the climb to the dome is paid."),
           ("Is there a lift to the Sacré-Cœur dome?", "No, you climb about 300 spiral steps."),
           ("How do you get to the Sacré-Cœur without the steps?", "Take the funicular from Anvers metro station: it works with a metro ticket."),
       ]),

    _d(slug="musee-d-orsay", path="musee-d-orsay", groupe="musees", nom="Musée d'Orsay", couleur="azur", h1="Visiting the Musée d'Orsay",
       in_="at the Musée d'Orsay", to="to the Musée d'Orsay", tips_for="visiting the Musée d'Orsay",
       description="Visiting the Musée d'Orsay: the Impressionists, the clock, closing day, Thursday late opening, booking and how to get there.",
       accroche="Monet, Renoir, Van Gogh, Degas: the world's largest Impressionist collection, in a former railway station. Thursday's late opening is the best time to go.",
       intro=[
           "Housed in the Gare d'Orsay, built for the 1900 World's Fair, the museum covers art from 1848 to 1914. The great glass-roofed nave holds the sculpture; the Impressionists are on the 5th floor, under the roof.",
           "The museum is closed on Mondays and stays open late on Thursday evenings. Booking a slot online is strongly recommended. The entrance areas are being renovated until 2028, without closing the collections.",
       ],
       a_voir=[
           ("The Impressionist gallery", "On the 5th floor: Monet, Renoir, Pissarro, Sisley, Degas, Caillebotte. The heart of the museum."),
           ("Van Gogh and Gauguin", "The Post-Impressionist rooms, with Starry Night Over the Rhône and Van Gogh's self-portrait."),
           ("The clocks", "The two great station clocks: from inside, you see Paris and the Sacré-Cœur through the clock face."),
           ("The nave", "The view down the glass-roofed hall, with sculpture by Carpeaux and Rodin."),
           ("The restaurant", "The former dining room of the station hotel, all gilding and chandeliers."),
       ],
       y_aller=[
           ("By RER and metro", "Musée d'Orsay station (RER C), right outside, or Solférino (line 12), five minutes away."),
           ("On foot", "From the Louvre, cross the Léopold-Sédar-Senghor footbridge: ten minutes."),
       ],
       fiche=[("Time needed", "2 to 3 hours"), ("Closed", "Mondays"), ("Late opening", "Thursday evening"), ("Booking", "Strongly recommended")],
       conseils=[
           "Go on Thursday evening: fewer people and a reduced price later in the day.",
           "Start on the 5th floor before the Impressionist rooms fill up.",
           "Carry on to the Musée de l'Orangerie and Monet's Water Lilies across the Seine: a joint ticket is available.",
       ],
       activites=[
           ("Musée d'Orsay tickets and tours", "Timed tickets and guided Impressionist tours.", "Musee d'Orsay"),
           ("Orsay and Orangerie", "Combined offers for both Impressionist museums.", "Orsay Orangerie"),
       ],
       faq=[
           ("What day is the Musée d'Orsay closed?", "Mondays, plus 1 May and 25 December."),
           ("How late is Orsay open on Thursdays?", "On Thursdays the museum stays open into the evening, with last entry about 45 minutes before closing."),
           ("Do I need to book the Musée d'Orsay?", "It is not compulsory but strongly recommended: tickets bought on the spot do not guarantee entry on busy days."),
       ]),

    _d(slug="arc-de-triomphe", path="arc-de-triomphe", groupe="monuments", nom="Arc de Triomphe", couleur="encre", h1="Visiting the Arc de Triomphe",
       in_="at the Arc de Triomphe", to="to the Arc de Triomphe", tips_for="visiting the Arc de Triomphe",
       description="Visiting the Arc de Triomphe: the rooftop and its 284 steps, the Tomb of the Unknown Soldier, the flame ceremony, how to get there and the Champs-Élysées.",
       accroche="At the top of the Champs-Élysées, 284 steps lead to a rooftop where twelve avenues fan out like a star. It is one of the most striking views in Paris.",
       intro=[
           "Napoleon commissioned the Arc de Triomphe in 1806 to honour the Grande Armée. The Unknown Soldier has lain beneath the arch since 1921, and the flame of remembrance is rekindled every evening in a short ceremony.",
           "The base of the monument and the tomb are free to visit. The rooftop, 50 metres up, is reached by 284 steps; the lift is for visitors with reduced mobility. Use the underground passage to get there: never cross the roundabout.",
       ],
       a_voir=[
           ("The rooftop", "The view over the twelve avenues of Place de l'Étoile, the historic axis to the Louvre and, the other way, La Défense."),
           ("The Tomb of the Unknown Soldier", "Under the arch, with the flame rekindled every evening at 6:30pm."),
           ("The sculptures", "François Rude's Departure of the Volunteers of 1792, known as La Marseillaise, on the Champs-Élysées side."),
           ("The Champs-Élysées", "Two kilometres down to Concorde. In December, the Christmas lights make it one of the city's most popular walks."),
       ],
       y_aller=[
           ("By metro and RER", "Charles de Gaulle - Étoile (lines 1, 2, 6 and RER A). Follow signs for the Arc de Triomphe exit to come out at the underground passage."),
           ("On foot", "Walk up the Champs-Élysées from Concorde: about half an hour."),
       ],
       fiche=[("Time needed", "1 hour"), ("Best time", "Late afternoon, then the flame"), ("Rooftop", "284 steps"), ("Free", "First Sunday of the month, November to March")],
       conseils=[
           "Go up an hour before sunset and come down for the flame ceremony.",
           "Buy your ticket online: the only wait is then the security check.",
           "On 11 November, 8 May and 14 July, access is restricted during ceremonies: check before you go.",
       ],
       activites=[
           ("Arc de Triomphe rooftop tickets", "Entry to the panoramic rooftop.", "Arc de Triomphe"),
           ("Champs-Élysées and Arc de Triomphe tours", "Guided walks and open-top bus tours.", "Champs-Elysees tour"),
       ],
       faq=[
           ("How many steps to the top of the Arc de Triomphe?", "284 steps. The lift is reserved for visitors with reduced mobility."),
           ("How do you get to the Arc de Triomphe?", "Through the underground passage from the top of the Champs-Élysées or Avenue de la Grande-Armée. Do not cross the roundabout: it is dangerous and forbidden."),
           ("What time is the flame rekindled?", "Every evening at 6:30pm, under the arch. The ceremony is public and free."),
       ]),

    _d(slug="opera-garnier", path="palais-garnier", groupe="monuments", nom="Palais Garnier", couleur="ocre", h1="Visiting the Palais Garnier opera house",
       in_="at the Palais Garnier", to="to the Palais Garnier", tips_for="visiting the Palais Garnier",
       description="Visiting the Palais Garnier opera house: the grand staircase, the grand foyer, the Chagall ceiling, timed tickets, opening times and tips.",
       accroche="Marble, gilding and a Chagall ceiling: the Palais Garnier is the most lavish interior in Paris, and you can explore it on your own during the day.",
       intro=[
           "Opened in 1875, the Palais Garnier is the masterpiece of the Second Empire. People come for the grand staircase, the grand foyer, a rival to the Hall of Mirrors, and, when there is no rehearsal, for the auditorium and its ceiling painted by Marc Chagall.",
           "Self-guided visits use a timed ticket, every day during the daytime, except for occasional closures for performances. Suitcases and large bags are not allowed.",
       ],
       a_voir=[
           ("The grand staircase", "A double flight of white marble with onyx banisters and chandeliers: the heart of the building."),
           ("The grand foyer", "A gilded gallery nearly 50 metres long, with mirrors and painted ceilings."),
           ("The auditorium and the Chagall ceiling", "Visible from a box when no rehearsal is on; the chandelier weighs several tonnes."),
           ("The library-museum", "Set models, costumes and memorabilia from the history of the Paris Opera."),
           ("The Galeries Lafayette rooftop", "Two minutes away, a free rooftop terrace looking over the opera house and all of Paris."),
       ],
       y_aller=[
           ("By metro", "Opéra (lines 3, 7 and 8), right outside; RER A at Auber, two minutes away."),
           ("On foot", "From the Louvre, walk up Avenue de l'Opéra: a quarter of an hour."),
       ],
       fiche=[("Time needed", "1.5 hours"), ("Open", "Daily, daytime"), ("Booking", "Recommended, timed ticket"), ("Good for", "Everyone")],
       conseils=[
           "Come early in the morning: the grand staircase is far more photogenic without the crowds.",
           "Check the calendar before you go: on some days the auditorium cannot be seen because of rehearsals.",
           "The best way to see the auditorium is still to attend a ballet: restricted-view seats are affordable.",
       ],
       activites=[
           ("Palais Garnier tickets and guided tours", "Timed self-guided entry or a guided tour.", "Palais Garnier"),
           ("Opera and department store district tours", "Guided walks between the Opera and Boulevard Haussmann.", "Palais Garnier guided tour"),
       ],
       faq=[
           ("Can you visit the Palais Garnier without seeing a show?", "Yes, self-guided visits are open every day during the daytime, except for occasional closures."),
           ("Can you see the Chagall ceiling on the tour?", "Yes, from a box, unless a rehearsal or performance is using the auditorium."),
           ("How long does a Palais Garnier visit take?", "Allow an hour and a half for the public areas and the current exhibition."),
       ]),

    _d(slug="croisiere-sur-la-seine", path="seine-cruise", groupe="quartiers", nom="Seine cruise", couleur="azur", h1="Taking a Seine river cruise",
       in_="on the Seine", to="to the boarding points", tips_for="your Seine cruise",
       description="Seine river cruises in Paris: which company to choose, where to board, daytime, sunset and dinner cruises, the Batobus and tips.",
       accroche="An hour on the water and Paris glides by: Notre-Dame, the Louvre, Orsay, the Eiffel Tower. It is the best way to get your bearings on day one.",
       intro=[
           "Most of the monuments of Paris line the Seine between the Île Saint-Louis and the Eiffel Tower. A sightseeing cruise of about an hour shows you all of them from your seat, with commentary in several languages.",
           "Several companies sail from the centre: Bateaux-Mouches from Pont de l'Alma, Bateaux Parisiens and Vedettes de Paris from the foot of the Eiffel Tower, Vedettes du Pont-Neuf from the Île de la Cité. The Batobus works like a bus on the water, with a day ticket.",
       ],
       a_voir=[
           ("The sightseeing cruise", "About an hour, a loop between the Eiffel Tower and the islands. No need to book far ahead outside the high season."),
           ("The sunset cruise", "Golden light on the façades, then the monuments lighting up: the best time slot."),
           ("The dinner cruise", "For a special evening, with a menu on board. Book ahead, especially at weekends."),
           ("The Batobus", "About ten stops, hop on and off as you like: handy for getting between museums without the metro."),
       ],
       y_aller=[
           ("Pont de l'Alma", "Alma - Marceau metro (line 9) or Pont de l'Alma on RER C for the Bateaux-Mouches."),
           ("Eiffel Tower", "Bir-Hakeim metro (line 6) or Champ de Mars - Tour Eiffel on RER C for the piers at Port de la Bourdonnais."),
           ("Pont-Neuf", "Pont-Neuf metro (line 7) or Cité (line 4) for Square du Vert-Galant."),
       ],
       fiche=[("Duration", "About 1 hour"), ("Best time", "Sunset"), ("Booking", "Recommended in summer and for dinners"), ("Good for", "Everyone, great for families")],
       conseils=[
           "Do it on your first day: you will spot the monuments to visit afterwards.",
           "Sit outside on the top deck and bring a jacket: it is always cooler on the water.",
           "In winter, when the Seine floods, boats can be suspended: check the day before.",
       ],
       activites=[
           ("Seine sightseeing cruises", "One hour from the Eiffel Tower or Pont de l'Alma.", "Seine river cruise Paris"),
           ("Seine dinner cruises", "Meals on board, from simple menus to fine dining.", "Seine dinner cruise"),
       ],
       faq=[
           ("Which Seine cruise company should I choose?", "The big companies offer very similar routes. Choose the boarding point that suits you best: Eiffel Tower, Pont de l'Alma or Pont-Neuf."),
           ("How long is a Seine cruise?", "About an hour for a sightseeing cruise, around two and a half hours for a dinner cruise."),
           ("Do the boats run in winter?", "Yes, all year round, except when the Seine floods. The boats are heated and glazed."),
       ]),

    _d(slug="le-marais", path="le-marais", groupe="quartiers", nom="Le Marais", couleur="pin", h1="Visiting Le Marais",
       in_="in the Marais", to="to the Marais", tips_for="visiting the Marais",
       description="Visiting Le Marais in Paris: Place des Vosges, Victor Hugo's House, the Musée Carnavalet, the Picasso Museum, Rue des Rosiers and Sunday shopping.",
       accroche="17th-century mansions, free museums, falafel and shops open on Sundays: the Marais is the most pleasant neighbourhood in Paris to explore on foot.",
       intro=[
           "Once the aristocrats' quarter, the Marais has kept its narrow streets and grand town houses, many of which are now museums. It stretches between the Hôtel de Ville, Place des Vosges and the Temple district.",
           "It is also one of the few areas of Paris where most shops open on Sundays. Two major museums are free for their permanent collections: the Musée Carnavalet, on the history of Paris, and Victor Hugo's House.",
       ],
       a_voir=[
           ("Place des Vosges", "The oldest royal square in Paris, ringed by arcades. The garden in the middle is perfect for a break."),
           ("Victor Hugo's House", "The writer's apartment on Place des Vosges. Permanent collections free."),
           ("The Musée Carnavalet", "The history of Paris from the beginning to the present, in two mansions. Free for the permanent collections, closed on Mondays."),
           ("The Picasso Museum", "The largest public collection of Picasso's work, in the Hôtel Salé."),
           ("Rue des Rosiers", "The heart of the historic Jewish quarter, famous for its falafel."),
           ("The Hôtel de Ville", "The neo-Renaissance city hall and, in winter, a temporary ice rink on the square."),
       ],
       y_aller=[
           ("By metro", "Saint-Paul (line 1), Chemin Vert (line 8) for Place des Vosges, or Hôtel de Ville (lines 1 and 11)."),
           ("On foot", "From Notre-Dame, cross the Île Saint-Louis: a quarter of an hour to Rue des Rosiers."),
       ],
       fiche=[("Time needed", "Half a day"), ("Best time", "Sunday, or a weekday morning"), ("Free museums", "Carnavalet, Victor Hugo's House"), ("Good for", "Everyone, on foot")],
       conseils=[
           "On Sundays the area is lively and the shops are open; Rue des Rosiers is quieter on Saturday, the Sabbath.",
           "The Musée Carnavalet is closed on Mondays; check before planning your walk around it.",
           "Head to the Marché des Enfants-Rouges, the oldest covered market in Paris, for lunch.",
       ],
       activites=[
           ("Marais guided tours", "History walks and tours of the Jewish quarter.", "Marais walking tour"),
           ("Marais food tours", "Tastings in bakeries, cheese shops and markets.", "Marais food tour"),
       ],
       faq=[
           ("Are the Marais shops open on Sundays?", "Yes, most shops in the area open on Sundays, which makes it an ideal Sunday outing."),
           ("Which free museums are in the Marais?", "The Musée Carnavalet and Victor Hugo's House, free for their permanent collections."),
           ("How do I get to the Marais?", "By metro to Saint-Paul (line 1) or Chemin Vert (line 8), or on foot from Notre-Dame."),
       ]),

    _d(slug="quartier-latin", path="latin-quarter", groupe="quartiers", nom="Latin Quarter and Luxembourg", couleur="pin", h1="Visiting the Latin Quarter and the Luxembourg Gardens",
       in_="in the Latin Quarter", to="to the Latin Quarter", tips_for="visiting the Latin Quarter",
       description="Visiting the Latin Quarter and the Luxembourg Gardens: the Panthéon, the Sorbonne, Rue Mouffetard, Shakespeare and Company, how to get there.",
       accroche="The Paris of students and bookshops, from the Panthéon to the Luxembourg Gardens. A neighbourhood to explore on foot, between two cafés.",
       intro=[
           "On the Left Bank, opposite the Île de la Cité, the Latin Quarter is named after the Latin spoken at the Sorbonne in the Middle Ages. Bookshops, art-house cinemas and cafés sit alongside the Panthéon, where Voltaire, Victor Hugo and Marie Curie are buried.",
           "Next door, the Luxembourg Gardens are the Parisians' favourite park: chestnut-lined paths, the Medici Fountain, toy sailboats on the pond and green chairs free for everyone. Entry is free.",
       ],
       a_voir=[
           ("The Luxembourg Gardens", "The Senate palace, the great pond, the Medici Fountain and over a hundred statues."),
           ("The Panthéon", "The resting place of great men and women, with Foucault's pendulum under the dome."),
           ("The Sorbonne", "The chapel and the fountain on Place de la Sorbonne, lined with cafés."),
           ("Rue Mouffetard", "A sloping street of food shops, with a market in the mornings from Tuesday to Sunday."),
           ("Shakespeare and Company", "The famous English-language bookshop facing Notre-Dame. There is often a queue to get in."),
           ("The Musée de Cluny", "The museum of the Middle Ages, with the Lady and the Unicorn tapestries and Gallo-Roman baths."),
       ],
       y_aller=[
           ("By RER and metro", "Luxembourg (RER B) for the gardens, Cluny - La Sorbonne (line 10) or Saint-Michel (line 4, RER B and C) for the quarter."),
           ("On foot", "From Notre-Dame, cross the Petit-Pont: five minutes to Rue Saint-Jacques."),
       ],
       fiche=[("Time needed", "Half a day"), ("Luxembourg Gardens", "Free, open daily"), ("Best time", "Morning, for the Rue Mouffetard market"), ("Good for", "Everyone, great for families")],
       conseils=[
           "Start with Rue Mouffetard in the morning, walk up to the Panthéon, then finish in the Luxembourg Gardens.",
           "With children: sailboats on the pond, the puppet theatre and the playground in the Luxembourg.",
           "The gardens' hours follow the sun: they close earlier in winter.",
       ],
       activites=[
           ("Latin Quarter guided tours", "Walks between the Sorbonne, the Panthéon and Saint-Germain.", "Latin Quarter walking tour"),
           ("Panthéon tickets", "Entry to the monument and, in season, the colonnade.", "Pantheon Paris"),
       ],
       faq=[
           ("Are the Luxembourg Gardens free?", "Yes, entry is free every day. Opening hours vary with the season."),
           ("Who is buried in the Panthéon?", "Voltaire, Rousseau, Victor Hugo, Émile Zola, Marie Curie and Josephine Baker, among others."),
           ("How do I get to the Luxembourg Gardens?", "Take RER B to Luxembourg station, right by the main entrance."),
       ]),

    _d(slug="versailles", locality="Versailles", path="versailles", groupe="musees", nom="Versailles", dept="78", cachet="Yvelines", couleur="ocre", h1="Visiting the Palace of Versailles",
       in_="at Versailles", to="to Versailles", tips_for="visiting Versailles",
       description="Visiting the Palace of Versailles from Paris: compulsory booking, closing day, the Passport ticket, the gardens, Trianon and how to get there by RER.",
       accroche="The Hall of Mirrors, the King's apartments, Le Nôtre's gardens and Marie-Antoinette's estate: a full day out, forty minutes from Paris.",
       intro=[
           "Louis XIV turned his father's hunting lodge into a royal residence and the seat of power. Today the estate covers the palace, the formal gardens, the Grand and Petit Trianon and the Queen's Hamlet, over hundreds of hectares.",
           "The palace is closed on Mondays. Booking a time slot is compulsory for everyone, even free entry. The Passport ticket covers the palace and the Trianon estate; the gardens are free except on Musical Fountains days in the warmer months.",
       ],
       a_voir=[
           ("The Hall of Mirrors", "357 mirrors and ceilings painted by Le Brun. Go first thing or late in the day to see it without the crowds."),
           ("The State Apartments", "The King's and Queen's apartments, with Louis XIV's bedchamber at the centre of the palace."),
           ("The gardens", "The Grand Canal, the fountains and Le Nôtre's groves. You can hire a rowing boat or a bike in the warmer months."),
           ("The Grand and Petit Trianon", "The royal family's more private residences, half an hour's walk from the palace. They open at noon."),
           ("The Queen's Hamlet", "Marie-Antoinette's country village, with a farm, a mill and a pond."),
           ("The Gallery of Coaches", "In the Great Stables opposite the palace: the coronation coaches, free to visit."),
       ],
       y_aller=[
           ("By RER C", "To Versailles Château Rive Gauche, the closest station, ten minutes' walk away. Allow about 40 minutes from central Paris."),
           ("By Transilien train", "Line L from Saint-Lazare to Versailles Rive Droite, or line N from Montparnasse to Versailles Chantiers. About twenty minutes' walk from there."),
           ("By car or with a driver", "Paid parking on Place d'Armes. A driver saves you connections, especially with children."),
       ],
       fiche=[("Time needed", "A full day"), ("Closed", "Mondays"), ("Booking", "Yes, compulsory"), ("Best days", "Wednesday, Thursday or Friday")],
       conseils=[
           "Avoid Tuesday and Sunday: they are the busiest days, since the palace is closed on Monday.",
           "Start with the gardens and Trianon if your palace slot is in the early afternoon.",
           "In winter the palace is free on the first Sunday of the month, but you still have to book a slot.",
       ],
       activites=[
           ("Versailles tickets and guided tours", "Passport tickets, guided tours and transport from Paris.", "Palace of Versailles"),
           ("Versailles by bike or in a small group", "Guided days covering the palace, gardens and Trianon.", "Versailles bike tour"),
       ],
       faq=[
           ("What day is Versailles closed?", "Mondays, plus 1 January, 1 May and 25 December."),
           ("Do I need to book Versailles?", "Yes, a time slot is compulsory for every visitor, including those who get in free."),
           ("How do I get to Versailles from Paris?", "The easiest way is RER C to Versailles Château Rive Gauche, ten minutes' walk from the palace."),
       ]),

    _d(slug="disneyland-paris", path="disneyland-paris", groupe="sorties", nom="Disneyland Paris", dept="77", cachet="Seine-et-Marne", couleur="azur", locality="Marne-la-Vallée",
       h1="Disneyland Paris: visiting both parks", **{"in": "at Disneyland Paris", "to": "to Disneyland Paris", "tips_for": "Disneyland Paris"},
       description="Visiting Disneyland Paris: Disneyland Park, Disney Adventure World and World of Frozen, dated tickets, getting there on RER A, and tips.",
       accroche="Two parks, a dining village and, since March 2026, World of Frozen. Disneyland Paris is a direct RER ride from central Paris.",
       intro=[
           "Disneyland Paris has two parks in Marne-la-Vallée, east of Paris: Disneyland Park, with its castle and the great classics, and Disney Adventure World, the former Walt Disney Studios Park, renamed and transformed on 29 March 2026. Disney Village, with restaurants and shops, lies between them.",
           "The big new arrival is World of Frozen, with the village of Arendelle on a large lake, next to Avengers Campus and the Pixar lands. Tickets are dated: buy them in advance, especially during school holidays.",
       ],
       a_voir=[
           ("Disneyland Park", "Sleeping Beauty Castle, Main Street, Pirates of the Caribbean, Big Thunder Mountain and the afternoon parade."),
           ("Disney Adventure World", "The second park, completely redesigned around a lake, with Disney, Pixar and Marvel lands and a night-time show."),
           ("World of Frozen", "The village of Arendelle, a boat ride through the film's story and character meetings. It is the busiest area: go early."),
           ("Avengers Campus", "The Marvel land, with thrill rides for older children and adults."),
           ("Disney Village", "Restaurants, shops and a cinema, free to enter, between the station and the parks."),
       ],
       y_aller=[
           ("By RER A", "To the Marne-la-Vallée - Chessy terminus, right outside the park entrance. Allow about 40 minutes from central Paris."),
           ("By TGV", "Marne-la-Vallée - Chessy TGV station, in the same place, has direct trains from many French cities."),
           ("By car or with a driver", "Via the A4 motorway. Park parking is paid; a private transfer saves changes with children."),
       ],
       fiche=[("Time needed", "1 to 2 days"), ("Booking", "Dated tickets, in advance"), ("Access", "RER A, Marne-la-Vallée - Chessy"), ("Good for", "Families, Disney and Marvel fans")],
       conseils=[
           "Arrive before opening and head first for the busiest rides, such as the Frozen attraction.",
           "Download the official app: it shows live waiting times.",
           "On weekdays outside school holidays, queues are much shorter than at weekends.",
       ],
       activites=[
           ("Disneyland Paris tickets", "Dated tickets for one or both parks.", "Disneyland Paris ticket"),
           ("Disneyland Paris with transport", "Ticket plus shuttle from central Paris.", "Disneyland Paris transfer"),
       ],
       faq=[
           ("How do you get to Disneyland Paris from Paris?", "Take RER A to the Marne-la-Vallée - Chessy terminus, right outside the parks, in about 40 minutes from the centre."),
           ("What is Disney Adventure World?", "It is the new name of the former Walt Disney Studios Park since 29 March 2026, now home to World of Frozen."),
           ("Should I book Disneyland tickets in advance?", "Yes, tickets are dated and some days sell out during the holidays, so buy them before you go."),
       ]),

    _d(slug="catacombes", path="catacombs", groupe="monuments", nom="Catacombs", couleur="encre", h1="Visiting the Paris Catacombs",
       **{"in": "in the Catacombs", "to": "to the Catacombs", "tips_for": "visiting the Catacombs"},
       description="Visiting the renovated Paris Catacombs: compulsory booking, closing day, 131 steps, how long it takes, getting to Denfert-Rochereau and tips.",
       accroche="Twenty metres below Paris, the bones of millions of Parisians line the galleries. Renovated in 2026, the Catacombs can only be visited with a booking.",
       intro=[
           "At the end of the 18th century, Paris emptied its overflowing cemeteries and moved the bones into old underground quarries. The ossuary, open to the public since the early 19th century, has become one of the most striking visits in the city.",
           "After several months of renovation, the Catacombs reopened on 8 April 2026 with new lighting and an updated visit. Booking a time slot online is compulsory: you cannot get in without a reserved ticket.",
       ],
       a_voir=[
           ("The ossuary", "Kilometres of skulls and bones stacked with care, sometimes in patterns, along galleries marked with inscriptions."),
           ("The old quarries", "Before the ossuary, the route passes through the limestone quarries that supplied some of the stone of Paris."),
           ("The renovated route", "New lighting, models and an audio guide that explain the history of the city's underground."),
       ],
       y_aller=[
           ("By metro and RER", "Denfert-Rochereau station (lines 4 and 6, RER B), right by the entrance on Avenue du Colonel-Henri-Rol-Tanguy."),
           ("The exit", "You come out elsewhere, on Rue Rémy-Dumoncel, a few minutes' walk away: bear it in mind if you are meeting someone."),
       ],
       fiche=[("Visit length", "About 1 hour"), ("Closed", "Mondays"), ("Booking", "Yes, compulsory"), ("Good to know", "131 steps down, 112 up")],
       conseils=[
           "Bring a jacket: it is about 14 °C underground all year round.",
           "Wear closed shoes; the ground is uneven and sometimes damp.",
           "The visit is not recommended for claustrophobic visitors or people with reduced mobility, and is not ideal for young children.",
       ],
       activites=[
           ("Catacombs tickets and guided tours", "Reserved entry and guided visits.", "Paris Catacombs"),
           ("Hidden and underground Paris", "Guided tours of secret Paris and its curiosities.", "Paris underground tour"),
       ],
       faq=[
           ("Do I need to book the Paris Catacombs?", "Yes, booking a time slot online is compulsory, and slots go fast, especially at weekends and during holidays."),
           ("What day are the Catacombs closed?", "Mondays, plus 1 January, 1 May and 25 December."),
           ("How many steps are there in the Catacombs?", "131 steps down at the start and 112 back up at the exit, with no lift."),
       ]),

    _d(slug="noel-a-paris", path="christmas-in-paris", groupe="sorties", nom="Christmas in Paris", couleur="ocre", h1="Christmas in Paris: lights, markets and ice rinks",
       **{"in": "at Christmas in Paris", "to": "to the Christmas sights", "tips_for": "Christmas in Paris"},
       description="Christmas 2026 in Paris: Champs-Élysées lights switch-on date, the return of its Christmas market, the Grand Palais ice rink, department store windows and cruises.",
       accroche="The Champs-Élysées lights go on on 22 November 2026, and its Christmas market returns after ten years. Here is where to find the magic of Christmas in Paris.",
       intro=[
           "From late November to early January, Paris dresses up for the holidays: illuminated avenues, animated department store windows, chalet markets and ice rinks. It is a great time to visit, as long as you wrap up warm.",
           "In 2026, the Champs-Élysées lights are switched on on Sunday 22 November and shine every evening until early January. The same day, the Champs-Élysées Christmas market makes its comeback, running until 4 January 2027.",
       ],
       a_voir=[
           ("The Champs-Élysées lights", "Hundreds of illuminated trees from Concorde to the Arc de Triomphe. The best view is from the top of the Arc de Triomphe."),
           ("The Champs-Élysées Christmas market", "Back after ten years, its chalets line the avenue between Place de la Concorde and the Rond-Point, from 22 November 2026 to 4 January 2027."),
           ("Department store windows", "On Boulevard Haussmann, the animated windows of Galeries Lafayette and Printemps, and the giant tree under the Galeries Lafayette dome."),
           ("The Grand Palais ice rink", "In December, a huge ice rink fills the glass-roofed nave of the Grand Palais. Book your slot ahead."),
           ("La Défense Christmas market", "One of the largest in the region, open from 12 November to 31 December 2026."),
           ("A Seine cruise", "To see the monuments lit up while staying warm in a glazed boat."),
       ],
       y_aller=[
           ("Champs-Élysées", "Metro Concorde (lines 1, 8, 12), Champs-Élysées - Clemenceau (lines 1 and 13) or Charles de Gaulle - Étoile."),
           ("Department stores", "Metro Chaussée d'Antin - La Fayette (lines 7 and 9) or Havre - Caumartin, RER A at Auber."),
       ],
       fiche=[("Lights", "From 22 November 2026"), ("Champs-Élysées market", "22 Nov 2026 - 4 Jan 2027"), ("Best time", "Weekdays, at nightfall"), ("Good for", "Everyone, great for families")],
       conseils=[
           "Go on a weekday rather than at the weekend: markets and windows are packed on Saturdays.",
           "Night falls around 5pm in December: visit museums in the afternoon and the lights afterwards.",
           "Book ice rinks, dinner cruises and New Year's Eve restaurants in advance.",
       ],
       activites=[
           ("Christmas lights tour", "Bus, walking or boat tours to see Paris lit up.", "Paris Christmas lights tour"),
           ("Christmas dinner cruise on the Seine", "Festive menus on board, with views of the illuminated monuments.", "Paris Christmas cruise"),
       ],
       faq=[
           ("When are the Champs-Élysées Christmas lights switched on in 2026?", "On Sunday 22 November 2026, in the early evening. They stay on every evening until early January."),
           ("Is there a Christmas market on the Champs-Élysées in 2026?", "Yes, it returns after ten years, from 22 November 2026 to 4 January 2027, between Concorde and the Rond-Point."),
           ("Where can you ice skate in Paris at Christmas?", "Under the glass roof of the Grand Palais in December, as well as on several rinks around the city and at La Défense."),
       ]),

]
for _x in DESTINATIONS:
    if "in_" in _x:
        _x["in"] = _x.pop("in_")

ITINERAIRE = {
    "slug": "3-days",
    "titre": "Paris in 3 days",
    "description": "A 3-day Paris itinerary by metro and on foot: Notre-Dame, the Sainte-Chapelle, the Louvre, Montmartre, Orsay, the Eiffel Tower and a Seine cruise.",
    "accroche": "Three days for the essentials of Paris, without rushing. Stops are grouped by neighbourhood, and each day takes the museums' closing days into account.",
    "jours": [
        ("Day 1: Île de la Cité and the Marais", [
            ("notre-dame", "In the morning, Notre-Dame with a booked slot, then Square Jean-XXIII for the view of the apse."),
            ("sainte-chapelle", "Five minutes' walk to the Sainte-Chapelle, ideally when the sun is high."),
            ("le-marais", "In the afternoon, cross the Île Saint-Louis to the Marais: Place des Vosges, the Musée Carnavalet and Rue des Rosiers."),
        ]),
        ("Day 2: the Louvre, the Opera and Montmartre", [
            ("louvre", "The Louvre at opening time (not on a Tuesday), with a planned route."),
            ("opera-garnier", "Walk up Avenue de l'Opéra to the Palais Garnier, then the Galeries Lafayette rooftop."),
            ("montmartre", "Metro to Abbesses, walk up through the village and watch the sunset from the Sacré-Cœur."),
        ]),
        ("Day 3: Orsay, the Eiffel Tower and the Seine", [
            ("musee-d-orsay", "The Musée d'Orsay in the morning (not on a Monday), starting on the 5th floor."),
            ("tour-eiffel", "Walk along the river to the Eiffel Tower, with a booked slot in mid-afternoon."),
            ("croisiere-sur-la-seine", "A sunset cruise from the foot of the tower, to watch Paris light up."),
        ]),
    ],
    "variante": "With a fourth day, spend it at Versailles (not on a Monday). For a quieter afternoon, swap the Eiffel Tower for the Arc de Triomphe and its rooftop, or for the Latin Quarter and the Luxembourg Gardens.",
    "variante_liens": ["versailles", "arc-de-triomphe", "quartier-latin"],
    "conseils": [
        "Stay near a metro line 1 or line 4 station: between them they serve most of the stops on this itinerary.",
        "Book the Louvre, the Sainte-Chapelle and the Eiffel Tower now: slots are compulsory or in high demand.",
        "Remember the closing days: the Louvre on Tuesdays, Orsay and Versailles on Mondays.",
    ],
}

TITRES = {
    "tour-eiffel": "Eiffel Tower: Tickets, the Top and Practical Tips",
    "louvre": "Visiting the Louvre: Booking, Entrances, Tips",
    "notre-dame": "Visiting Notre-Dame de Paris: Entry and Towers",
    "sainte-chapelle": "Sainte-Chapelle Paris: Booking and Tips",
    "montmartre": "Things to Do in Montmartre and the Sacré-Cœur",
    "musee-d-orsay": "Musée d'Orsay: Late Opening and Visiting Tips",
    "arc-de-triomphe": "Arc de Triomphe: Rooftop, Flame and Tips",
    "opera-garnier": "Palais Garnier Opera House: Visiting Tips",
    "croisiere-sur-la-seine": "Seine River Cruise: Where to Board and Tips",
    "le-marais": "Things to Do in the Marais, Paris",
    "quartier-latin": "Latin Quarter and Luxembourg Gardens Guide",
    "versailles": "Visiting Versailles from Paris: Booking, Tips",
    'disneyland-paris': 'Disneyland Paris: Tickets, Getting There, Tips',
    'catacombes': 'Paris Catacombs: Booking and Visiting Tips',
    'noel-a-paris': 'Christmas in Paris 2026: Lights, Markets, Rinks',
}
TITRE_REGION = "Paris Travel Guide: The Best Places to Visit"
TITRE_ITI = "Paris in 3 Days: An Itinerary by Metro"

ALIAS = {
    "tour-eiffel": ["Eiffel Tower"], "louvre": ["Louvre"], "notre-dame": ["Notre-Dame"], "sainte-chapelle": ["Sainte-Chapelle"],
    "montmartre": ["Montmartre", "Sacré-Cœur"], "musee-d-orsay": ["Musée d'Orsay", "Orsay"], "arc-de-triomphe": ["Arc de Triomphe"],
    "opera-garnier": ["Palais Garnier"], "croisiere-sur-la-seine": ["cruise"], "le-marais": ["Marais"],
    "quartier-latin": ["Latin Quarter", "Luxembourg Gardens"], "versailles": ["Versailles"],
    'disneyland-paris': ['Disneyland Paris', 'Disneyland'],
    'catacombes': ['Catacombs'],
    'noel-a-paris': ['Christmas in Paris'],
}
