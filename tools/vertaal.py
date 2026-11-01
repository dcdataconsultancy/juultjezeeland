"""Maakt de/index.html en en/index.html uit de Nederlandse index.html.

Gebruik, vanuit de hoofdmap van de repository:

    python3 tools/vertaal.py

Werkwijze bij een wijziging:
1. Pas alleen de Nederlandse index.html aan.
2. Voeg nieuwe of gewijzigde Nederlandse teksten toe aan de woordenlijsten DE en EN hieronder
   (de Nederlandse tekst exact als sleutel, de vertaling als waarde).
3. Draai het script. Het stopt met "ONVERTAALD" en een lijst als er nog een Nederlandse tekst
   zonder vertaling is; vul die aan en draai opnieuw.

Gebruik geen koppeltekens of gedachtestreepjes in de vertalingen.
"""
import sys, re, os

DE = {
 'Juultje Zeeland | Vakantiehuisje en appartement in Wissenkerke': 'Juultje Zeeland | Ferienhaus und Ferienwohnung in Wissenkerke',
 'Twee sfeervolle verblijven voor twee personen in Wissenkerke op Noord-Beveland. Honden welkom. Boek rechtstreeks bij Marc en Angelia.': 'Zwei gemütliche Unterkünfte für zwei Personen in Wissenkerke auf Noord-Beveland. Hunde willkommen. Buchen Sie direkt bei Marc und Angelia.',
 'Juultje Zeeland, naar boven': 'Juultje Zeeland, nach oben',
 'Menu': 'Menü',
 'Hoofdmenu': 'Hauptmenü',
 'Verblijven': 'Unterkünfte',
 'Omgeving': 'Umgebung',
 'Praktisch': 'Praktisches',
 'Over ons': 'Über uns',
 'Contact': 'Kontakt',
 'Boek direct': 'Direkt buchen',
 'Rust en ruimte in het hart van Zeeland': 'Ruhe und Weite im Herzen von Zeeland',
 'Twee sfeervolle verblijven voor twee personen, aan weerszijden van ons huis in het dorp Wissenkerke. Polders, dijken en water liggen om de hoek. Je hond is van harte welkom.': 'Zwei gemütliche Unterkünfte für zwei Personen, zu beiden Seiten unseres Hauses im Dorf Wissenkerke. Polder, Deiche und Wasser liegen gleich um die Ecke. Ihr Hund ist herzlich willkommen.',
 'Bekijk beschikbaarheid': 'Verfügbarkeit prüfen',
 'Bekijk de verblijven': 'Unterkünfte ansehen',
 'Buitenkant van het huis': 'Außenansicht des Hauses',
 'Foto: buitenkant van het huis met hek en vlaggenmast': 'Foto: Außenansicht des Hauses mit Zaun und Fahnenmast',
 'Waarom Juultje Zeeland': 'Warum Juultje Zeeland',
 'Direct bij ons boeken': 'Direkt bei uns buchen',
 'Rechtstreeks contact, zonder tussenpartij': 'Direkter Kontakt, ohne Vermittler',
 'Honden welkom': 'Hunde willkommen',
 '€ 15 per nacht': '15 € pro Nacht',
 'Wij wonen naast de deur': 'Wir wohnen nebenan',
 'Voor tips en een persoonlijk welkom': 'Für Tipps und einen persönlichen Empfang',
 'Elektrische fiets huren': 'Elektrofahrrad mieten',
 'Beschikbaarheid en tarief op aanvraag': 'Verfügbarkeit und Preis auf Anfrage',
 'Twee verblijven, één adres': 'Zwei Unterkünfte, eine Adresse',
 'Allebei voor twee personen met één slaapkamer, aan verschillende kanten van ons huis. Beddengoed, handdoeken, wifi en airconditioning zijn overal inbegrepen.': 'Beide für zwei Personen mit einem Schlafzimmer, auf verschiedenen Seiten unseres Hauses. Bettwäsche, Handtücher, WLAN und Klimaanlage sind überall inklusive.',
 'Woonkamer van het vakantiehuisje met leren bank, eettafel en open keuken': 'Wohnzimmer des Ferienhauses mit Ledersofa, Esstisch und offener Küche',
 'Keuken van het vakantiehuisje met spoelbak, koffiezetapparaat en planken met glazen': 'Küche des Ferienhauses mit Spüle, Kaffeemaschine und Regalen mit Gläsern',
 'Zithoek met leren bank, salontafel en een grote plant bij het raam': 'Sitzecke mit Ledersofa, Couchtisch und einer großen Pflanze am Fenster',
 'Slaapkamer met tweepersoonsbed en nachtkastje': 'Schlafzimmer mit Doppelbett und Nachttisch',
 'Houten overkapping in de tuin met twee loungestoelen en een tafel': 'Überdachte Holzterrasse im Garten mit zwei Loungesesseln und einem Tisch',
 'Leren bank met kussens en een salontafel met verse bloemen': 'Ledersofa mit Kissen und ein Couchtisch mit frischen Blumen',
 'Slaapkamer met tweepersoonsbed en een televisie aan de muur': 'Schlafzimmer mit Doppelbett und einem Fernseher an der Wand',
 'Badkamer met inloopdouche en wastafelmeubel': 'Badezimmer mit ebenerdiger Dusche und Waschtisch',
 'Inloopdouche met regendouche': 'Ebenerdige Dusche mit Regenbrause',
 'Toilet met wastafel en een vrolijke poster': 'Toilette mit Waschbecken und einem fröhlichen Poster',
 'Doorkijk vanuit de woonkamer naar de badkamer en de slaapkamer': 'Blick vom Wohnzimmer ins Badezimmer und ins Schlafzimmer',
 'Zijpad met poort naar het vakantiehuisje': 'Seitenweg mit Tor zum Ferienhaus',
 'Oprit met eigen parkeerplaats voor het vakantiehuisje': 'Einfahrt mit eigenem Parkplatz für das Ferienhaus',
 'Vakantiehuisje Juultje': 'Ferienhaus Juultje',
 'Het ruimste verblijf': 'Die geräumigere Unterkunft',
 '2 personen': '2 Personen',
 '1 slaapkamer': '1 Schlafzimmer',
 'circa 35 m²': 'ca. 35 m²',
 'Eigen parkeerplaats op de oprit': 'Eigener Parkplatz in der Einfahrt',
 'Voor wie in alle rust wil genieten van Zeeland, met de kust, de natuur en gezellige dorpjes op korte afstand. Het huisje ligt aan de andere kant van onze woning en biedt net wat meer ruimte.': 'Für alle, die Zeeland in aller Ruhe genießen möchten, mit Küste, Natur und gemütlichen Dörfern ganz in der Nähe. Das Häuschen liegt auf der anderen Seite unseres Hauses und bietet etwas mehr Platz.',
 'Prijs en beschikbaarheid': 'Preis und Verfügbarkeit',
 'Slaapkamer van het appartement met tweepersoonsbed onder een schuin dak': 'Schlafzimmer der Ferienwohnung mit Doppelbett unter der Dachschräge',
 'Zithoek met grijze bank, bed en dakraam': 'Sitzecke mit grauem Sofa, Bett und Dachfenster',
 'Eettafel voor twee met een bos bloemen en een staande lamp': 'Esstisch für zwei mit einem Blumenstrauß und einer Stehlampe',
 'Keuken met koelkast, oven en kookplaat': 'Küche mit Kühlschrank, Backofen und Kochfeld',
 'Badkamer met wastafel en een rek met handdoeken': 'Badezimmer mit Waschbecken und einem Regal mit Handtüchern',
 'Eigen terras met tafel en twee stoelen in de zon': 'Eigene Terrasse mit Tisch und zwei Stühlen in der Sonne',
 'Tweepersoonsbed met sprei en een bijzettafel met plantje': 'Doppelbett mit Tagesdecke und einem Beistelltisch mit Pflanze',
 'Douche met douchegordijn en handgreep': 'Dusche mit Duschvorhang und Haltegriff',
 'Hal met kapstok en een spiegel aan de deur': 'Flur mit Garderobe und einem Spiegel an der Tür',
 'Appartement Juultje': 'Ferienwohnung Juultje',
 'Compact en comfortabel': 'Kompakt und komfortabel',
 'circa 26 m²': 'ca. 26 m²',
 'Airconditioning': 'Klimaanlage',
 'Een fijne uitvalsbasis voor een ontspannen verblijf. Vanuit Wissenkerke ontdek je de omgeving makkelijk te voet of op de fiets, en geniet je volop van de Zeeuwse natuur.': 'Ein schöner Ausgangspunkt für einen entspannten Aufenthalt. Von Wissenkerke aus erkunden Sie die Umgebung ganz einfach zu Fuß oder mit dem Fahrrad und genießen die Natur von Zeeland in vollen Zügen.',
 'Toegankelijkheid.': 'Barrierefreiheit.',
 'Beide verblijven hebben een lage instap, maar zijn niet volledig rolstoeltoegankelijk: sommige doorgangen en de ruimte bij de douche zijn beperkt. Heb je specifieke wensen? Neem dan vooraf even contact met ons op.': 'Beide Unterkünfte haben einen niedrigen Einstieg, sind aber nicht vollständig rollstuhlgerecht: Einige Durchgänge und der Platz an der Dusche sind begrenzt. Haben Sie besondere Wünsche? Dann nehmen Sie bitte vorher kurz Kontakt mit uns auf.',
 'Ontdek Noord-Beveland': 'Entdecken Sie Noord-Beveland',
 'Ideaal voor wie houdt van rust, natuur, wandelen en fietsen. Wij geven je graag onze persoonlijke tips.': 'Ideal für alle, die Ruhe, Natur, Wandern und Radfahren lieben. Wir geben Ihnen gern unsere persönlichen Tipps.',
 'Witte hond in het gras van de polder bij zonsondergang': 'Weißer Hund im Gras des Polders bei Sonnenuntergang',
 'Wandelen': 'Wandern',
 'Door de polders, langs dijken, natuurgebieden en het water. Ook heerlijk met de hond.': 'Durch die Polder, entlang der Deiche, durch Naturgebiete und am Wasser. Auch mit dem Hund herrlich.',
 'Twee elektrische fietsen op het gras in de tuin': 'Zwei Elektrofahrräder auf dem Rasen im Garten',
 'Fietsen': 'Radfahren',
 'Langs polders, Zeeuwse dorpen en de Noordzeekust. Vraag naar onze elektrische fietsen.': 'Vorbei an Poldern, zeeländischen Dörfern und der Nordseeküste. Fragen Sie nach unseren Elektrofahrrädern.',
 'Houten steiger in stil water bij zonsopkomst met een zeilboot in de verte': 'Holzsteg im stillen Wasser bei Sonnenaufgang mit einem Segelboot in der Ferne',
 'Oosterschelde en Veerse Meer': 'Oosterschelde und Veerse Meer',
 'Nationaal Park Oosterschelde en het Veerse Meer liggen dichtbij.': 'Der Nationalpark Oosterschelde und das Veerse Meer liegen ganz in der Nähe.',
 'Leeg zandstrand met zee en windmolens aan de horizon': 'Leerer Sandstrand mit Meer und Windrädern am Horizont',
 'Stranden': 'Strände',
 'Op korte rijafstand. Let op de plaatselijke regels voor honden.': 'Nur eine kurze Autofahrt entfernt. Bitte beachten Sie die örtlichen Regeln für Hunde.',
 'Dijk met fietspad langs het water en windmolens in de verte': 'Deich mit Radweg am Wasser und Windrädern in der Ferne',
 'Steiger en rotsen aan het water bij zonsopkomst': 'Steg und Felsen am Wasser bei Sonnenaufgang',
 'Oever met stenen en een rij boeien in het stille water': 'Ufer mit Steinen und einer Reihe Bojen im stillen Wasser',
 'Wat gasten zeggen': 'Das sagen unsere Gäste',
 'van 10 op Booking.com, 54 beoordelingen': 'von 10 auf Booking.com, 54 Bewertungen',
 'van 5 op Airbnb, 24 recensies': 'von 5 auf Airbnb, 24 Bewertungen',
 '“Prachtig huisje, alle comfort, leuke overkapping met tuintje voor de hond. Wij hebben genoten!”': '„Das Bett ist der Hammer! Selten habe ich woanders so gut geschlafen.“',
 'David uit België, vakantiehuisje via Booking.com': 'Alexandra aus Deutschland, Ferienhaus über Booking.com',
 '“Het ligt in een heel rustige buurt. Het was heel schoon en opgeruimd. De communicatie ging heel soepel.”': '„Genau wie auf den Bildern und super sauber. Wir haben uns rundum wohl gefühlt.“',
 'Liliane, appartement via Airbnb': 'Heike aus Deutschland, Ferienhaus über Booking.com',
 '“Dit is 1 van de beste vakantiehuisjes waar ik ben geweest. Ga er zeker nog een keer terug.”': '„Sehr gemütlich, gut ausgestattet, eingezäunter kleiner Garten mit überdachter Terrasse, perfekt für uns und den Hund.“',
 'Saida uit Nederland, vakantiehuisje via Booking.com': 'Anja aus Deutschland, Ferienhaus über Booking.com',
 'Goed om te weten': 'Gut zu wissen',
 'Aankomst en vertrek': 'Anreise und Abreise',
 'Aankomst vanaf 15.00 uur': 'Anreise ab 15:00 Uhr',
 'Vertrek uiterlijk 10.00 uur': 'Abreise bis spätestens 10:00 Uhr',
 'Zelf inchecken via een sleutelkluisje': 'Selbstständige Anreise mit Schlüsseltresor',
 'Eerder aankomen of later vertrekken alleen in overleg': 'Frühere Anreise oder spätere Abreise nur nach Absprache',
 'Huisregels': 'Hausregeln',
 'Niet roken binnen, geen feesten': 'Rauchen im Haus und Partys nicht erlaubt',
 'Rust tussen 21.00 en 07.00 uur': 'Ruhezeit zwischen 21:00 und 07:00 Uhr',
 'Extra gasten alleen na overleg': 'Zusätzliche Gäste nur nach Absprache',
 'Bij vertrek bezemschoon, afwas gedaan en koelkast leeg': 'Bei Abreise besenrein, Geschirr gespült und Kühlschrank leer',
 'Annuleren': 'Stornierung',
 'Tot 30 dagen voor aankomst gratis': 'Bis 30 Tage vor Anreise kostenlos',
 '30 tot 14 dagen voor aankomst: 50% van de boekingsprijs': '30 bis 14 Tage vor Anreise: 50 % des Buchungspreises',
 'Minder dan 14 dagen of niet verschenen: 100%': 'Weniger als 14 Tage oder Nichterscheinen: 100 %',
 'Boeken': 'Buchen',
 'Boek rechtstreeks bij ons': 'Buchen Sie direkt bei uns',
 'Altijd de actuele prijs en beschikbaarheid. Na je reservering ontvang je direct een bevestiging, en voor aankomst sturen we je alle praktische informatie.': 'Immer aktuelle Preise und Verfügbarkeit. Nach Ihrer Reservierung erhalten Sie sofort eine Bestätigung, und vor der Anreise senden wir Ihnen alle praktischen Informationen.',
 'Betalen kan met iDEAL, creditcard, Bancontact of via een overschrijving op factuur.': 'Bezahlen können Sie mit iDEAL, Kreditkarte, Bancontact oder per Überweisung auf Rechnung.',
 'Marc en Angelia': 'Marc und Angelia',
 'Foto: Marc en Angelia': 'Foto: Marc und Angelia',
 'Welkom bij Marc en Angelia': 'Willkommen bei Marc und Angelia',
 'Wij verwelkomen onze gasten graag in het rustige dorp Wissenkerke. We wonen zelf op hetzelfde adres, dus je bent nooit ver van een vriendelijk gezicht.': 'Wir begrüßen unsere Gäste gern im ruhigen Dorf Wissenkerke. Wir wohnen selbst an derselben Adresse, ein freundliches Gesicht ist also nie weit.',
 'Gastvrijheid en persoonlijk contact vinden we belangrijk. We helpen je graag met tips over de omgeving, leuke activiteiten en mooie plekken om te bezoeken.': 'Gastfreundschaft und persönlicher Kontakt sind uns wichtig. Wir helfen Ihnen gern mit Tipps zur Umgebung, schönen Aktivitäten und besonderen Orten.',
 'Vragen? Neem gerust contact op': 'Fragen? Melden Sie sich gern',
 'Bel of app Marc:': 'Marc per Anruf oder WhatsApp:',
 'Bel of app Angelia:': 'Angelia per Anruf oder WhatsApp:',
 '06 1366 4239': '+31 6 1366 4239',
 '06 8119 9425': '+31 6 8119 9425',
 'Mail: [nog aan te leveren]': 'Email: [folgt noch]',
 'Naam': 'Name',
 'Mailadres': 'Emailadresse',
 'Bericht': 'Nachricht',
 'Verstuur bericht': 'Nachricht senden',
 'Vakantiehuisje en appartement in Wissenkerke': 'Ferienhaus und Ferienwohnung in Wissenkerke',
 'Informatie': 'Informationen',
 'Algemene voorwaarden': 'Allgemeine Geschäftsbedingungen',
 'Annuleringsvoorwaarden': 'Stornierungsbedingungen',
 'Privacyverklaring': 'Datenschutzerklärung',
 'Taal': 'Sprache',
 'Fotogalerij': 'Fotogalerie',
 'Foto {n} van {t}': 'Foto {n} von {t}',
 'Sluiten': 'Schließen',
 'Vorige foto': 'Vorheriges Foto',
 'Volgende foto': 'Nächstes Foto',
}
DE_RE = [
 (r"^Bekijk alle (\d+) foto's van het vakantiehuisje$", r"Alle \1 Fotos vom Ferienhaus ansehen"),
 (r"^Bekijk alle (\d+) foto's van het appartement$", r"Alle \1 Fotos der Ferienwohnung ansehen"),
 (r"^(\d+) foto's$", r"\1 Fotos"),
 (r"^Vergroot foto (\d+) van (\d+)$", r"Foto \1 von \2 vergrößern"),
]

EN = {
 'Juultje Zeeland | Vakantiehuisje en appartement in Wissenkerke': 'Juultje Zeeland | Holiday cottage and apartment in Wissenkerke',
 'Twee sfeervolle verblijven voor twee personen in Wissenkerke op Noord-Beveland. Honden welkom. Boek rechtstreeks bij Marc en Angelia.': 'Two charming stays for two people in Wissenkerke on Noord-Beveland. Dogs welcome. Book directly with Marc and Angelia.',
 'Juultje Zeeland, naar boven': 'Juultje Zeeland, back to top',
 'Menu': 'Menu',
 'Hoofdmenu': 'Main menu',
 'Verblijven': 'Stays',
 'Omgeving': 'Area',
 'Praktisch': 'Practical',
 'Over ons': 'About us',
 'Contact': 'Contact',
 'Boek direct': 'Book now',
 'Rust en ruimte in het hart van Zeeland': 'Peace and space in the heart of Zeeland',
 'Twee sfeervolle verblijven voor twee personen, aan weerszijden van ons huis in het dorp Wissenkerke. Polders, dijken en water liggen om de hoek. Je hond is van harte welkom.': 'Two charming stays for two people, on either side of our home in the village of Wissenkerke. Polders, dykes and water are just around the corner. Your dog is very welcome.',
 'Bekijk beschikbaarheid': 'Check availability',
 'Bekijk de verblijven': 'View the stays',
 'Buitenkant van het huis': 'Outside of the house',
 'Foto: buitenkant van het huis met hek en vlaggenmast': 'Photo: outside of the house with gate and flagpole',
 'Waarom Juultje Zeeland': 'Why Juultje Zeeland',
 'Direct bij ons boeken': 'Book directly with us',
 'Rechtstreeks contact, zonder tussenpartij': 'Direct contact, no middleman',
 'Honden welkom': 'Dogs welcome',
 '€ 15 per nacht': '€15 per night',
 'Wij wonen naast de deur': 'We live next door',
 'Voor tips en een persoonlijk welkom': 'For tips and a personal welcome',
 'Elektrische fiets huren': 'Rent an electric bike',
 'Beschikbaarheid en tarief op aanvraag': 'Availability and rates on request',
 'Twee verblijven, één adres': 'Two stays, one address',
 'Allebei voor twee personen met één slaapkamer, aan verschillende kanten van ons huis. Beddengoed, handdoeken, wifi en airconditioning zijn overal inbegrepen.': 'Both sleep two people in one bedroom, on different sides of our home. Bed linen, towels, wifi and air conditioning are included everywhere.',
 'Woonkamer van het vakantiehuisje met leren bank, eettafel en open keuken': 'Living room of the holiday cottage with leather sofa, dining table and open kitchen',
 'Keuken van het vakantiehuisje met spoelbak, koffiezetapparaat en planken met glazen': 'Kitchen of the holiday cottage with sink, coffee machine and shelves with glasses',
 'Zithoek met leren bank, salontafel en een grote plant bij het raam': 'Seating area with leather sofa, coffee table and a large plant by the window',
 'Slaapkamer met tweepersoonsbed en nachtkastje': 'Bedroom with double bed and bedside table',
 'Houten overkapping in de tuin met twee loungestoelen en een tafel': 'Covered wooden patio in the garden with two lounge chairs and a table',
 'Leren bank met kussens en een salontafel met verse bloemen': 'Leather sofa with cushions and a coffee table with fresh flowers',
 'Slaapkamer met tweepersoonsbed en een televisie aan de muur': 'Bedroom with double bed and a television on the wall',
 'Badkamer met inloopdouche en wastafelmeubel': 'Bathroom with walk in shower and vanity unit',
 'Inloopdouche met regendouche': 'Walk in shower with rain shower head',
 'Toilet met wastafel en een vrolijke poster': 'Toilet with washbasin and a cheerful poster',
 'Doorkijk vanuit de woonkamer naar de badkamer en de slaapkamer': 'View from the living room into the bathroom and bedroom',
 'Zijpad met poort naar het vakantiehuisje': 'Side path with gate to the holiday cottage',
 'Oprit met eigen parkeerplaats voor het vakantiehuisje': 'Driveway with private parking for the holiday cottage',
 'Vakantiehuisje Juultje': 'Holiday cottage Juultje',
 'Het ruimste verblijf': 'The more spacious stay',
 '2 personen': '2 guests',
 '1 slaapkamer': '1 bedroom',
 'circa 35 m²': 'about 35 m²',
 'Eigen parkeerplaats op de oprit': 'Private parking on the driveway',
 'Voor wie in alle rust wil genieten van Zeeland, met de kust, de natuur en gezellige dorpjes op korte afstand. Het huisje ligt aan de andere kant van onze woning en biedt net wat meer ruimte.': 'For anyone who wants to enjoy Zeeland in peace and quiet, with the coast, nature and charming villages close by. The cottage is on the other side of our home and offers a little more space.',
 'Prijs en beschikbaarheid': 'Price and availability',
 'Slaapkamer van het appartement met tweepersoonsbed onder een schuin dak': 'Bedroom of the apartment with double bed under a sloping ceiling',
 'Zithoek met grijze bank, bed en dakraam': 'Seating area with grey sofa, bed and skylight',
 'Eettafel voor twee met een bos bloemen en een staande lamp': 'Dining table for two with a bunch of flowers and a floor lamp',
 'Keuken met koelkast, oven en kookplaat': 'Kitchen with fridge, oven and hob',
 'Badkamer met wastafel en een rek met handdoeken': 'Bathroom with washbasin and a towel rack',
 'Eigen terras met tafel en twee stoelen in de zon': 'Private patio with table and two chairs in the sun',
 'Tweepersoonsbed met sprei en een bijzettafel met plantje': 'Double bed with bedspread and a side table with a plant',
 'Douche met douchegordijn en handgreep': 'Shower with shower curtain and grab rail',
 'Hal met kapstok en een spiegel aan de deur': 'Hallway with coat rack and a mirror on the door',
 'Appartement Juultje': 'Apartment Juultje',
 'Compact en comfortabel': 'Compact and comfortable',
 'circa 26 m²': 'about 26 m²',
 'Airconditioning': 'Air conditioning',
 'Een fijne uitvalsbasis voor een ontspannen verblijf. Vanuit Wissenkerke ontdek je de omgeving makkelijk te voet of op de fiets, en geniet je volop van de Zeeuwse natuur.': "A lovely base for a relaxing stay. From Wissenkerke you can easily explore the area on foot or by bike and make the most of Zeeland's nature.",
 'Toegankelijkheid.': 'Accessibility.',
 'Beide verblijven hebben een lage instap, maar zijn niet volledig rolstoeltoegankelijk: sommige doorgangen en de ruimte bij de douche zijn beperkt. Heb je specifieke wensen? Neem dan vooraf even contact met ons op.': 'Both stays have a low entrance step but are not fully wheelchair accessible: some doorways and the space around the shower are limited. Do you have specific needs? Please get in touch with us beforehand.',
 'Ontdek Noord-Beveland': 'Discover Noord-Beveland',
 'Ideaal voor wie houdt van rust, natuur, wandelen en fietsen. Wij geven je graag onze persoonlijke tips.': 'Ideal for anyone who loves peace and quiet, nature, walking and cycling. We are happy to share our personal tips.',
 'Witte hond in het gras van de polder bij zonsondergang': 'White dog in the grass of the polder at sunset',
 'Wandelen': 'Walking',
 'Door de polders, langs dijken, natuurgebieden en het water. Ook heerlijk met de hond.': 'Through the polders, along dykes, nature reserves and the water. Lovely with your dog too.',
 'Twee elektrische fietsen op het gras in de tuin': 'Two electric bikes on the grass in the garden',
 'Fietsen': 'Cycling',
 'Langs polders, Zeeuwse dorpen en de Noordzeekust. Vraag naar onze elektrische fietsen.': 'Past polders, Zeeland villages and the North Sea coast. Ask about our electric bikes.',
 'Houten steiger in stil water bij zonsopkomst met een zeilboot in de verte': 'Wooden jetty on still water at sunrise with a sailing boat in the distance',
 'Oosterschelde en Veerse Meer': 'Oosterschelde and Veerse Meer',
 'Nationaal Park Oosterschelde en het Veerse Meer liggen dichtbij.': 'Oosterschelde National Park and the Veerse Meer lake are close by.',
 'Leeg zandstrand met zee en windmolens aan de horizon': 'Empty sandy beach with sea and wind turbines on the horizon',
 'Stranden': 'Beaches',
 'Op korte rijafstand. Let op de plaatselijke regels voor honden.': 'A short drive away. Please check the local rules for dogs.',
 'Dijk met fietspad langs het water en windmolens in de verte': 'Dyke with cycle path along the water and wind turbines in the distance',
 'Steiger en rotsen aan het water bij zonsopkomst': 'Jetty and rocks by the water at sunrise',
 'Oever met stenen en een rij boeien in het stille water': 'Shore with stones and a row of buoys in the still water',
 'Wat gasten zeggen': 'What guests say',
 '9,1': '9.1',
 '4,92': '4.92',
 'van 10 op Booking.com, 54 beoordelingen': 'out of 10 on Booking.com, 54 reviews',
 'van 5 op Airbnb, 24 recensies': 'out of 5 on Airbnb, 24 reviews',
 '“Prachtig huisje, alle comfort, leuke overkapping met tuintje voor de hond. Wij hebben genoten!”': '“We had a wonderful stay! The hosts were exceptionally friendly and always helpful, so we felt welcome from the very first minute.”',
 'David uit België, vakantiehuisje via Booking.com': 'Simon from Switzerland, holiday cottage via Booking.com (translated from German)',
 '“Het ligt in een heel rustige buurt. Het was heel schoon en opgeruimd. De communicatie ging heel soepel.”': '“It is in a very quiet neighbourhood. It was very clean and tidy. Communication was very smooth.”',
 'Liliane, appartement via Airbnb': 'Liliane, apartment via Airbnb (translated from Dutch)',
 '“Dit is 1 van de beste vakantiehuisjes waar ik ben geweest. Ga er zeker nog een keer terug.”': '“This is one of the best holiday homes I have ever stayed in. I will definitely go back.”',
 'Saida uit Nederland, vakantiehuisje via Booking.com': 'Saida from the Netherlands, holiday cottage via Booking.com (translated from Dutch)',
 'Goed om te weten': 'Good to know',
 'Aankomst en vertrek': 'Arrival and departure',
 'Aankomst vanaf 15.00 uur': 'Arrival from 3 pm',
 'Vertrek uiterlijk 10.00 uur': 'Departure by 10 am',
 'Zelf inchecken via een sleutelkluisje': 'Check in yourself using a key safe',
 'Eerder aankomen of later vertrekken alleen in overleg': 'Early arrival or late departure only by arrangement',
 'Huisregels': 'House rules',
 'Niet roken binnen, geen feesten': 'No smoking indoors, no parties',
 'Rust tussen 21.00 en 07.00 uur': 'Quiet hours from 9 pm to 7 am',
 'Extra gasten alleen na overleg': 'Extra guests only by arrangement',
 'Bij vertrek bezemschoon, afwas gedaan en koelkast leeg': 'On departure: swept clean, dishes done and fridge empty',
 'Annuleren': 'Cancellation',
 'Tot 30 dagen voor aankomst gratis': 'Free up to 30 days before arrival',
 '30 tot 14 dagen voor aankomst: 50% van de boekingsprijs': '30 to 14 days before arrival: 50% of the booking price',
 'Minder dan 14 dagen of niet verschenen: 100%': 'Less than 14 days or no show: 100%',
 'Boeken': 'Booking',
 'Boek rechtstreeks bij ons': 'Book directly with us',
 'Altijd de actuele prijs en beschikbaarheid. Na je reservering ontvang je direct een bevestiging, en voor aankomst sturen we je alle praktische informatie.': 'Always the latest prices and availability. You receive a confirmation straight after booking, and before your arrival we send you all the practical information.',
 'Betalen kan met iDEAL, creditcard, Bancontact of via een overschrijving op factuur.': 'You can pay by iDEAL, credit card, Bancontact or bank transfer on invoice.',
 'Marc en Angelia': 'Marc and Angelia',
 'Foto: Marc en Angelia': 'Photo: Marc and Angelia',
 'Welkom bij Marc en Angelia': 'Welcome from Marc and Angelia',
 'Wij verwelkomen onze gasten graag in het rustige dorp Wissenkerke. We wonen zelf op hetzelfde adres, dus je bent nooit ver van een vriendelijk gezicht.': 'We love welcoming our guests to the quiet village of Wissenkerke. We live at the same address ourselves, so a friendly face is never far away.',
 'Gastvrijheid en persoonlijk contact vinden we belangrijk. We helpen je graag met tips over de omgeving, leuke activiteiten en mooie plekken om te bezoeken.': 'Hospitality and personal contact matter to us. We are happy to help with tips about the area, fun activities and beautiful places to visit.',
 'Vragen? Neem gerust contact op': 'Questions? Feel free to get in touch',
 'Bel of app Marc:': 'Call or WhatsApp Marc:',
 'Bel of app Angelia:': 'Call or WhatsApp Angelia:',
 '06 1366 4239': '+31 6 1366 4239',
 '06 8119 9425': '+31 6 8119 9425',
 'Mail: [nog aan te leveren]': 'Email: [to follow]',
 'Naam': 'Name',
 'Mailadres': 'Email address',
 'Bericht': 'Message',
 'Verstuur bericht': 'Send message',
 'Vakantiehuisje en appartement in Wissenkerke': 'Holiday cottage and apartment in Wissenkerke',
 'Informatie': 'Information',
 'Algemene voorwaarden': 'Terms and conditions',
 'Annuleringsvoorwaarden': 'Cancellation policy',
 'Privacyverklaring': 'Privacy policy',
 'Taal': 'Language',
 'Fotogalerij': 'Photo gallery',
 'Foto {n} van {t}': 'Photo {n} of {t}',
 'Sluiten': 'Close',
 'Vorige foto': 'Previous photo',
 'Volgende foto': 'Next photo',
}
EN_RE = [
 (r"^Bekijk alle (\d+) foto's van het vakantiehuisje$", r"View all \1 photos of the holiday cottage"),
 (r"^Bekijk alle (\d+) foto's van het appartement$", r"View all \1 photos of the apartment"),
 (r"^(\d+) foto's$", r"\1 photos"),
 (r"^Vergroot foto (\d+) van (\d+)$", r"Enlarge photo \1 of \2"),
]

# strings die in alle talen gelijk blijven
GELIJK = {'Juultje Zeeland', 'NL', 'DE', 'EN', 'Wissenkerke, Noord-Beveland', '+7', '+3', '9,1', '4,92',
          'Instagram: Juultje Zeeland', 'Julianastraat 38, 4491 GB Wissenkerke', 'Nederlands', 'Deutsch', 'English', '©', '2026', '">'}

def vertaal(tekst, tabel, regels, missers):
    kern = tekst.strip()
    if not kern:
        return tekst
    if kern in tabel:
        nieuw = tabel[kern]
    else:
        for pat, rep in regels:
            if re.match(pat, kern):
                nieuw = re.sub(pat, rep, kern); break
        else:
            if kern not in GELIJK:
                missers.append(kern)
            return tekst
    i = tekst.index(kern)
    return tekst[:i] + nieuw + tekst[i + len(kern):]

def maak(bron, taal, tabel, regels):
    missers = []
    delen = re.split(r'(<[^>]+>)', bron)
    uit, in_code = [], False
    for d in delen:
        if d.startswith('<'):
            tag = d.lower()
            if tag.startswith(('<style', '<script')): in_code = True
            elif tag.startswith(('</style', '</script')): in_code = False
            def attr(m):
                return f'{m.group(1)}="{vertaal(m.group(2), tabel, regels, missers)}"'
            d = re.sub(r'\b(alt|aria-label|data-teller)="([^"]*)"', attr, d)
            if d.startswith('<meta name="description"'):
                d = re.sub(r'content="([^"]*)"', lambda m: f'content="{vertaal(m.group(1), tabel, regels, missers)}"', d)
            uit.append(d)
        else:
            uit.append(d if in_code else vertaal(d, tabel, regels, missers))
    h = ''.join(uit)
    andere = 'en' if taal == 'de' else 'de'
    struct = [
        ('<html lang="nl">', f'<html lang="{taal}">'),
        ('"assets/fotos/', '"../assets/fotos/'),
        (', assets/fotos/', ', ../assets/fotos/'),
        ('login.smoobu.com/nl/booking-tool', f'login.smoobu.com/{taal}/booking-tool'),
        ('<li class="talen"><strong>NL</strong><a href="de/" lang="de" hreflang="de">DE</a><a href="en/" lang="en" hreflang="en">EN</a></li>',
         '<li class="talen"><a href="../" lang="nl" hreflang="nl">NL</a>' +
         ('<strong>DE</strong><a href="../en/" lang="en" hreflang="en">EN</a>' if taal == 'de' else '<a href="../de/" lang="de" hreflang="de">DE</a><strong>EN</strong>') + '</li>'),
        ('<a href="./" lang="nl" hreflang="nl">Nederlands</a><a href="de/" lang="de" hreflang="de">Deutsch</a><a href="en/" lang="en" hreflang="en">English</a>',
         '<a href="../" lang="nl" hreflang="nl">Nederlands</a>' +
         ('<a href="./" lang="de" hreflang="de">Deutsch</a><a href="../en/" lang="en" hreflang="en">English</a>' if taal == 'de' else '<a href="../de/" lang="de" hreflang="de">Deutsch</a><a href="./" lang="en" hreflang="en">English</a>')),
    ]
    for o, n in struct:
        assert o in h, (taal, o)
        h = h.replace(o, n)
    return h, missers

pad = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
bron = open(pad).read()
root = os.path.dirname(os.path.abspath(pad))
fout = False
for taal, tabel, regels in (('de', DE, DE_RE), ('en', EN, EN_RE)):
    h, missers = maak(bron, taal, tabel, regels)
    if missers:
        fout = True
        print(taal, 'ONVERTAALD:', missers)
    os.makedirs(os.path.join(root, taal), exist_ok=True)
    open(os.path.join(root, taal, 'index.html'), 'w').write(h)
    print(taal, 'ok', len(h))
sys.exit(1 if fout else 0)
