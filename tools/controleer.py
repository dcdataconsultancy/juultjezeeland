"""Controleert de hele website in site/ op fouten die je niet in de browser ziet.

Gebruik, vanuit de hoofdmap van de repository (na tools/vertaal.py):

    python3 tools/controleer.py

Controleert in elke HTML pagina (NL, DE, EN):
- interne links en bestanden (href, src, srcset) die niet bestaan
- koppeltekens en gedachtestreepjes in de lopende tekst (eigennamen zoals Noord-Beveland mogen)
- lengte van <title> (max 65 tekens) en meta omschrijving (110 tot 165 tekens), als waarschuwing

Stopt met foutcode 1 bij kapotte links of streepjes; lengtes geven alleen een waarschuwing.
"""
import html, os, re, sys

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
EIGENNAMEN = re.compile(r'\b(?:Noord|Zuid|Nord|Süd|Schouwen|Zeeuws|Goeree|Sint|Oud|Nieuw)-\w+'
                        r"|'s-\w+"
                        r'|\w+-(?:Beveland|Duiveland|Vlaanderen|Overflakkee|Holland|Brabant)')
STREEP = re.compile(r'[‑–—]|\w-\w')


def bestaat(pagina, link):
    link = link.split('#')[0].split('?')[0]
    if not link or link.startswith(('http:', 'https:', '//', 'data:', 'mailto:', 'tel:')):
        return True
    basis = SITE if link.startswith('/') else os.path.dirname(pagina)
    doel = os.path.normpath(os.path.join(basis, link.lstrip('/')))
    return os.path.isfile(doel) or os.path.isfile(os.path.join(doel, 'index.html'))


fouten, waarschuwingen = [], []
for map_, _, bestanden in os.walk(SITE):
    for naam in sorted(bestanden):
        if not naam.endswith('.html'):
            continue
        pad = os.path.join(map_, naam)
        rel = os.path.relpath(pad, SITE)
        h = open(pad, encoding='utf-8').read()
        links = re.findall(r'\b(?:href|src)="([^"]*)"', h)
        links += [d.strip().split(' ')[0] for s in re.findall(r'\bsrcset="([^"]*)"', h) for d in s.split(',')]
        for link in links:
            if not bestaat(pad, link):
                fouten.append(f'{rel}: link bestaat niet: {link}')
        main = re.search(r'<main\b[^>]*>(.*?)</main>', h, re.S)
        if main:
            tekst = html.unescape(re.sub(r'<[^>]+>', ' ', main.group(1)))
            for woord in sorted({w for w in tekst.split() if STREEP.search(EIGENNAMEN.sub('X', w))}):
                fouten.append(f'{rel}: streepje in tekst: {woord}')
        if naam == '404.html':
            continue
        titel = re.search(r'<title>(.*?)</title>', h, re.S)
        oms = re.search(r'<meta name="description" content="([^"]*)"', h)
        if not titel or len(html.unescape(titel.group(1))) > 65:
            waarschuwingen.append(f'{rel}: titel ontbreekt of is langer dan 65 tekens')
        if not oms or not 110 <= len(html.unescape(oms.group(1))) <= 165:
            waarschuwingen.append(f'{rel}: omschrijving ontbreekt of is niet 110 tot 165 tekens')

for w in waarschuwingen:
    print('waarschuwing:', w)
print('\n'.join(fouten) or 'Geen fouten.')
sys.exit(1 if fouten else 0)
