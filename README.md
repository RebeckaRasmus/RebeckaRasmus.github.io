# 💒 Bröllopswebb — Rebecka & Rasmus 2026

## Filer
- `index.html` — hela webbplatsen (en sida)
- `manifest.json` — PWA-manifest för "lägg till på hemskärmen"
- `sw.js` — service worker (offline-stöd)
- `server.py` — enkel Flask-server

## Kom igång

```bash
pip install flask
python server.py
# → http://localhost:5000
```

## Att fylla i
Sök efter dessa platshållare i `index.html` och byt ut dem:

- `Rebecka` & `Rasmus` → era riktiga namn
- `[DATUM]` → OSA-datum
- `[LÄNK TILL ÖNSKELISTA]` → länk till er önskelista
- `[E-POST]` → er e-postadress
- Foton i galleriet och "Vår historia"-sektionen
- "Vår historia"-texten

## PWA — Lägg till på hemskärmen
Ikoner (`icon-192.png`, `icon-512.png`) behöver skapas och läggas i samma mapp.
Rekommenderad storlek: 192×192 och 512×512 px, gärna med ett monogram eller logotyp.

Bandern "Lägg till på hemskärmen" visas automatiskt i Android/Chrome.
På iPhone: Dela → "Lägg till på hemskärmen".

## Driftsättning
Webbplatsen är en statisk HTML-fil och kan hostas var som helst:
- **Gratis**: GitHub Pages, Netlify, Vercel
- **Med Python**: Kör `server.py` på valfri VPS
