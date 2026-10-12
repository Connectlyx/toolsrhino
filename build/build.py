"""Generate the static ToolsRhino site.  Usage:  python3 build/build.py
Edit content in build/*.py, then re-run to regenerate every .html file with a consistent header and footer."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import home, services, rest
from lib import SITE

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pages = {
    "index.html": home.build(), "services.html": services.services(), "management-systems.html": services.management(),
    "ai-automation.html": services.ai(), "saas-development.html": services.saas(), "industries.html": rest.industries(),
    "about.html": rest.about(), "contact.html": rest.contact(), "404.html": rest.notfound(),
}
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)

urls = [n for n in pages if n != "404.html"]
pri = {"index.html": "1.0", "services.html": "0.9", "management-systems.html": "0.9", "ai-automation.html": "0.9", "saas-development.html": "0.8"}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE}/{"" if n=="index.html" else n}</loc><lastmod>2026-10-12</lastmod><priority>{pri.get(n,"0.7")}</priority></url>\n' for n in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(pages), "pages")
