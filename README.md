# ToolsRhino website

Static, multi-page website for **ToolsRhino**, the specialist sister company of Connectlyx
(AI Automation · SaaS Product Creation · Management Systems).

## Pages
`index.html` · `services.html` · `management-systems.html` · `ai-automation.html` · `saas-development.html` · `industries.html` · `about.html` · `contact.html` · `404.html`
Plus `sitemap.xml`, `robots.txt` and `assets/` (css, js, images).

## Deploy
Upload the whole folder to the repo root (replacing the old `index.html`). It is plain HTML/CSS/JS, so it works on GitHub Pages, Netlify, Vercel or any static host. No build step is needed to publish.

## Editing content
Header, footer and all page copy are generated from `build/*.py` so the navigation stays identical everywhere.
1. Edit the text in `build/home.py`, `build/services.py`, `build/rest.py` (or nav/footer in `build/lib.py`).
2. Run `python3 build/build.py` to regenerate every `.html` file.
Colours and fonts live at the top of `assets/css/style.css` (`:root`).

## Things to know
- Contact form uses the same Web3Forms key as the previous site (`assets/js/main.js`).
- Contact details: info@connectlyx.com · support@connectlyx.com · +1 214 814 4539 · WhatsApp wa.me/12148144539.
- Palette: #0047AB, #FFFFFF, #AFDBF5, #1A2C5B.
- The animated "ink" background is WebGL with a CSS gradient fallback, and pauses off-screen / for reduced-motion users.
- Canonical URLs and the sitemap assume `https://www.toolsrhino.com/`.
