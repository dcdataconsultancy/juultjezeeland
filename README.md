# Juultje Zeeland

Website voor Juultje Zeeland: vakantiehuisje en appartement in Wissenkerke, Noord-Beveland.

## Mappen

```
site/                    de website: alleen deze map komt online
  *.html                 Nederlandse pagina's
  de/  en/               Duitse en Engelse pagina's (gemaakt door tools/vertaal.py, niet met de hand aanpassen)
  assets/css/            opmaak (stijl.css)
  assets/fonts/          lettertypen DM Sans en Instrument Serif (licentie OFL), zodat bezoekers niets bij Google ophalen
  assets/fotos/          foto's (WebP 800 en 1600 px plus JPG als terugval, zonder EXIF)
  404.html, CNAME, robots.txt, sitemap.xml, llms.txt
tools/
  vertaal.py             maakt DE en EN pagina's, het SEO blok en sitemap.xml
  controleer.py          controleert links, streepjes en titellengtes
  smoobu-kalender.css    opmaak om in Smoobu te plakken (komt niet online)
.github/workflows/       publiceren en de branch controle
docs/seo/                lokale werkmap met audits, plannen en feitenbestanden (staat in .gitignore)
fotos-origineel/         lokale originele foto's (staat in .gitignore)
```

- Statische site zonder bouwstap. De url's zijn gelijk aan de paden binnen `site/`, bijvoorbeeld `site/de/boeken.html` wordt juultjezeeland.nl/de/boeken.html.
- Boekingen via de Smoobu Booking Engine (iframe in de sectie `#boeken`). Smoobu kiest de taal zelf op basis van de browser van de gast.

## Publiceren
Bij elke push naar `main` zet `.github/workflows/publiceer.yml` de map `site/` online via GitHub Pages (instelling Pages: Source = GitHub Actions). Bij elke pull request naar `dev` of `main` draait eerst `tools/controleer.py`; een kapotte link of een streepje in de tekst houdt de controle tegen.

## Werkwijze met branches
- `main` is de live website. Hier wordt nooit direct op gewerkt.
- `dev` is de ontwikkelbranch.
- Elke wijziging begint in een eigen branch vanaf `dev`, bijvoorbeeld `git checkout -b nieuwe-tekst dev`.
- Die branch gaat via een pull request naar `dev`.
- Pas daarna gaat `dev` via een pull request naar `main`.
- GitHub dwingt dit af: op `main` en `dev` kan niet direct gepusht worden, en een pull request naar `main` wordt alleen geaccepteerd als die van `dev` komt (controle in `.github/workflows/alleen-dev-naar-main.yml`).

## Teksten wijzigen
Pas alleen de Nederlandse pagina's in `site/` aan en maak daarna de Duitse en Engelse versie opnieuw, gevolgd door de controle:

```
python3 tools/vertaal.py
python3 tools/controleer.py
```

Nieuwe of gewijzigde Nederlandse teksten voeg je eerst toe aan de woordenlijsten `DE` en `EN` in `tools/vertaal.py`. Het script stopt met "ONVERTAALD" als er nog een tekst zonder vertaling is. Een nieuwe pagina voeg je toe aan `PAGINAS` onderaan het script.

## SEO en vindbaarheid
- `tools/vertaal.py` maakt in elke pagina (NL, DE, EN) het blok tussen `<!-- seo -->` en `<!-- /seo -->`: canonical, hreflang, Open Graph en op de homepage structured data (JSON-LD, `LodgingBusiness` met beide verblijven). Pas dit blok niet met de hand aan; feiten zoals telefoon, inchecktijd of oppervlakte staan in de functie `json_ld` in het script.
- Het script maakt ook `sitemap.xml`. `robots.txt` laat alle zoekmachines en AI zoekdiensten toe.
- `llms.txt` is een korte samenvatting voor AI diensten. Houd prijzen en voorwaarden daarin gelijk aan de website.
- Het deelbeeld voor sociale media en zoekresultaten is `site/assets/fotos/deelbeeld-1200.jpg` (1200 x 630).

## Boekingsmodule (Smoobu)
- Boven de boekingsmodule kiest de bezoeker in een keuzelijst "Beide verblijven", "Vakantiehuisje" (Smoobu ID 3563861) of "Appartement" (Smoobu ID 3563866). De knoppen "Prijs en beschikbaarheid" bij de verblijven kiezen het juiste verblijf vooraf.
- De opmaak binnen de boekingsmodule (zoals rood gearceerde data die niet meer kunnen, personalia pas na het zoeken op data, en op desktop eerst foto en prijs met de personalia eronder) kan niet vanaf deze website. Plak daarvoor `tools/smoobu-kalender.css` in Smoobu bij Custom CSS (Instellingen boekingssysteem, tabblad Custom style).

## Domein
De site draait op GitHub Pages met het eigen domein juultjezeeland.nl (bestand `site/CNAME` en de instelling bij Pages). Het domein staat bij Strato. DNS instellingen bij Strato:
- A records voor juultjezeeland.nl: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- AAAA records (optioneel): 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153
- CNAME voor www: dcdataconsultancy.github.io
