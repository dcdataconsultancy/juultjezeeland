# Juultje Zeeland

Website voor Juultje Zeeland: vakantiehuisje en appartement in Wissenkerke, Noord-Beveland.

- Statische site, gehost op GitHub Pages: Nederlandse pagina's in de hoofdmap (`index.html`, `huisregels.html`, `algemene-voorwaarden.html`, `annuleringsvoorwaarden.html`, `privacyverklaring.html`), Duits in `de/`, Engels in `en/`
- Gedeelde opmaak in `assets/stijl.css`. De lettertypen (DM Sans en Instrument Serif, licentie OFL) staan in `assets/fonts/`, zodat bezoekers niets bij Google ophalen.
- Boekingen via de Smoobu Booking Engine (iframe in de sectie `#boeken`). Smoobu kiest de taal zelf op basis van de browser van de gast.
- Foto's staan in `assets/fotos/` (WebP 800 en 1600 px plus JPG als terugval, zonder EXIF). Originelen horen in `fotos-origineel/`, die map staat in `.gitignore`.

## Werkwijze met branches
- `main` is de live website. Hier wordt nooit direct op gewerkt.
- `dev` is de ontwikkelbranch.
- Elke wijziging begint in een eigen branch vanaf `dev`, bijvoorbeeld `git checkout -b nieuwe-tekst dev`.
- Die branch gaat via een pull request naar `dev`.
- Pas daarna gaat `dev` via een pull request naar `main`.
- GitHub dwingt dit af: op `main` en `dev` kan niet direct gepusht worden, en een pull request naar `main` wordt alleen geaccepteerd als die van `dev` komt (controle in `.github/workflows/alleen-dev-naar-main.yml`).

## Teksten wijzigen
Pas alleen de Nederlandse pagina's aan en maak daarna de Duitse en Engelse versie opnieuw:

```
python3 tools/vertaal.py
```

Nieuwe of gewijzigde Nederlandse teksten voeg je eerst toe aan de woordenlijsten `DE` en `EN` in `tools/vertaal.py`. Het script stopt met "ONVERTAALD" als er nog een tekst zonder vertaling is. Een nieuwe pagina voeg je toe aan `PAGINAS` onderaan het script.

## Boekingsmodule (Smoobu)
- Boven de boekingsmodule kiest de bezoeker in een keuzelijst "Beide verblijven", "Vakantiehuisje" (Smoobu ID 3563861) of "Appartement" (Smoobu ID 3563866). De knoppen "Prijs en beschikbaarheid" bij de verblijven kiezen het juiste verblijf vooraf.
- De opmaak binnen de boekingsmodule (zoals rood gearceerde data die niet meer kunnen, personalia pas na het zoeken op data, en op desktop eerst foto en prijs met de personalia eronder) kan niet vanaf deze website. Plak daarvoor `tools/smoobu-kalender.css` in Smoobu bij Custom CSS (Instellingen boekingssysteem, tabblad Custom style).

## Domein
De site draait op GitHub Pages met het eigen domein juultjezeeland.nl (bestand `CNAME`). Het domein staat bij Strato. DNS instellingen bij Strato:
- A records voor juultjezeeland.nl: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- AAAA records (optioneel): 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153
- CNAME voor www: dcdataconsultancy.github.io
