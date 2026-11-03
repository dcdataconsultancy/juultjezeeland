# Juultje Zeeland

Website voor Juultje Zeeland: vakantiehuisje en appartement in Wissenkerke, Noord-Beveland.

- Statische site, gehost op GitHub Pages: Nederlandse pagina's in de hoofdmap (`index.html`, `huisregels.html`), Duits in `de/`, Engels in `en/`
- Gedeelde opmaak in `assets/stijl.css`
- Boekingen via de Smoobu Booking Engine (iframe in de sectie `#boeken`). Smoobu kiest de taal zelf op basis van de browser van de gast.
- Foto's staan in `assets/fotos/` (WebP 800 en 1600 px plus JPG als terugval, zonder EXIF). Originelen horen in `fotos-origineel/`, die map staat in `.gitignore`.

## Teksten wijzigen
Pas alleen de Nederlandse pagina's aan en maak daarna de Duitse en Engelse versie opnieuw:

```
python3 tools/vertaal.py
```

Nieuwe of gewijzigde Nederlandse teksten voeg je eerst toe aan de woordenlijsten `DE` en `EN` in `tools/vertaal.py`. Het script stopt met "ONVERTAALD" als er nog een tekst zonder vertaling is. Een nieuwe pagina voeg je toe aan `PAGINAS` onderaan het script.

## Nog te doen
- Foto voor Over ons (Marc en Angelia)
- Mailadres invullen
- Pagina's voor algemene voorwaarden, annuleringsvoorwaarden en privacyverklaring
- Eigen domein juultjezeeland.nl koppelen (CNAME); daarna de `hreflang` links in `index.html` aanpassen
