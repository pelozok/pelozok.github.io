# pelozok.github.io

Personal portfolio and CV — **Kevin Daniel Pelozo Retamar**, Software Engineer & AI Engineer based in Costa Rica.

Live site: [pelozok.github.io](https://pelozok.github.io)

---

## About

A bilingual (ES / EN) single-page portfolio that brings together:

- A short personal introduction and stack overview.
- **Professional work** — selected client projects built at deLaGuayaba S.A. (Finwaise, küikmatch, Cámara de Bancos CR, ABC Dust, Voces Vitales Costa Rica, Grupo TLA, Neutral Logistix, ALPROSA).
- **Personal projects** — independent and community work (Iglesia Central AD, Clear Books).
- Experience timeline, education, languages, and contact info.
- A downloadable PDF version of the CV.

The current positioning leads with **AI-assisted development** (Claude Code, MCP, n8n, AWS Textract, LLM APIs) while still showing WordPress and infrastructure depth in the background.

## Tech stack

This site is intentionally lightweight — no framework, no build step, no dependencies.

- **HTML5** — semantic markup, ARIA-friendly.
- **CSS3** — custom properties, CSS grid, dark theme with a lime accent.
- **Vanilla JavaScript** — language toggle (ES / EN) with a `data-i18n` dictionary, persisted via `localStorage`.
- **Google Fonts** — Inter (UI) and JetBrains Mono (accents).
- **GitHub Pages** for hosting.

## Project structure

```
pelozok.github.io/
├── index.html                # Page markup + content
├── assets/
│   ├── css/
│   │   └── styles.css        # All styles (no preprocessor)
│   ├── js/
│   │   └── main.js           # i18n dictionary + language toggle
│   └── files/
│       └── Kevin-Pelozo-Retamar-CV-2026.pdf
└── README.md
```

## Running locally

```bash
# any static server will do
python3 -m http.server 4173
# then open http://localhost:4173
```

## Bilingual content

Every translatable string lives in `assets/js/main.js` inside the `i18n.es` / `i18n.en` dictionaries. Each translatable DOM node carries a `data-i18n="key"` attribute; the toggle in the header swaps the values, updates `<html lang>`, and saves the choice to `localStorage` so visitors keep their preference on return.

## Deploying

The repository is named `pelozok.github.io`, so GitHub Pages serves `main` from the repository root automatically. Pushing to `main` is all that's needed:

```bash
git add .
git commit -m "your change"
git push
```

## Contact

- Email — kevindp2008@gmail.com
- Phone — +506 7007-3757
- LinkedIn — [/in/kevin-pelozo](https://www.linkedin.com/in/kevin-pelozo/)
- GitHub — [@pelozok](https://github.com/pelozok)

---

© Kevin Daniel Pelozo Retamar
