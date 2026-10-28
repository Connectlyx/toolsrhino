# ToolsRhino website

Static multi-page website for **ToolsRhino** (AI Automation · SaaS Product Creation · Management Systems), a specialist sister company of Connectlyx. Hosted on Vercel.

## What is in here
- 23 pages: Home, Services (+ Management Systems, AI Automation, SaaS), Industries (+ 7 industry pages), Insights (+ 6 articles), About, Contact, 404
- `assets/` css, js, images · `sitemap.xml` · `robots.txt` · `llms.txt` · `vercel.json`
- `build/` the generator (optional, see below)

## Deploy (Vercel)
Commit everything to `main`. Vercel redeploys automatically. `vercel.json` turns on clean URLs (`/services` instead of `/services.html`), security headers and asset caching.

## Local preview
Links are root-absolute (`/assets/...`), so double-clicking `index.html` will not style correctly. Run a local server instead:
`python3 -m http.server 8000` from this folder, then open http://localhost:8000 (some clean URLs only work on Vercel; the home page and .html paths work locally).

## Editing content
Header, footer and all copy are generated from `build/*.py`:
- `build/content_articles.py` – Insights articles
- `build/content_industries.py` – industry pages
- `build/home.py`, `services.py`, `rest.py` – core pages · `lib.py` – nav, footer, SEO tags
Edit, then run `python3 build/build.py` to regenerate every page, the sitemap, llms.txt and vercel.json.
To add an article: copy an entry in `content_articles.py`, change slug/title/text, rebuild, commit.

## Contact form
Web3Forms (key in `assets/js/main.js`). Contact details: info@connectlyx.com · support@connectlyx.com · +1 214 814 4539 · wa.me/12148144539.
