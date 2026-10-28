"""Generate the static ToolsRhino site.  Usage:  python3 build/build.py
Edit content in build/*.py, then re-run to regenerate every .html file with consistent header, footer and links."""
import os, sys, re, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import home, services, rest, seo_pages
from lib import SITE
from content_industries import INDUSTRIES
from content_articles import ARTICLES

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pages = {
    "index.html": home.build(), "services.html": services.services(), "management-systems.html": services.management(),
    "ai-automation.html": services.ai(), "saas-development.html": services.saas(), "industries.html": rest.industries(),
    "about.html": rest.about(), "contact.html": rest.contact(), "insights.html": seo_pages.insights_index(), "404.html": rest.notfound(),
}
for i in INDUSTRIES:
    pages[f"industries/{i['slug']}.html"] = seo_pages.industry_page(i)
for a in ARTICLES:
    pages[f"insights/{a['slug']}.html"] = seo_pages.article_page(a)

FOLDER_INDEX = {"industries.html": "industries/index.html", "insights.html": "insights/index.html"}  # avoids /x vs /x/ ambiguity
for name, html in pages.items():
    path = os.path.join(OUT, FOLDER_INDEX.get(name, name))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

today = "2026-10-28"
pri = {"index.html": "1.0", "services.html": "0.9", "management-systems.html": "0.9", "ai-automation.html": "0.9", "saas-development.html": "0.8",
       "industries.html": "0.8", "insights.html": "0.7"}
urls = [n for n in pages if n != "404.html"]
def loc(n):
    return SITE + "/" + ("" if n == "index.html" else n[:-5])
def prio(n):
    return pri.get(n, "0.8" if n.startswith("industries/") else "0.6" if n.startswith("insights/") else "0.5")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{loc(n)}</loc><lastmod>{today}</lastmod><priority>{prio(n)}</priority></url>\n' for n in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

llms = f"""# ToolsRhino
> ToolsRhino is the specialist sister company of Connectlyx. It builds AI automation, SaaS products and custom management systems for industries and businesses in the United States and worldwide.

## Services
- [Management Systems]({SITE}/management-systems): custom portals for orders, stock, staff, payroll, payments and reports
- [AI Automation]({SITE}/ai-automation): AI assistants, WhatsApp and email workflows, document processing, smart reporting
- [SaaS Product Creation]({SITE}/saas-development): from idea to MVP to scale

## Industries
""" + "".join(f"- [{re.sub('&amp;','&',i['name'])}]({SITE}/industries/{i['slug']}): {i['short']}\n" for i in INDUSTRIES) + f"""
## Insights
""" + "".join(f"- [{a['title']}]({SITE}/insights/{a['slug']}): {a['desc']}\n" for a in ARTICLES) + f"""
## Contact
- Email: info@connectlyx.com
- Support: support@connectlyx.com
- Phone / WhatsApp: +1 214 814 4539
- Parent company: https://www.connectlyx.com
"""
open(os.path.join(OUT, "llms.txt"), "w").write(llms)

import json
vercel = {
  "cleanUrls": True, "trailingSlash": False,
  "headers": [
    {"source": "/(.*)", "headers": [
      {"key": "X-Content-Type-Options", "value": "nosniff"},
      {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
      {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
      {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"},
      {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"}]},
    {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"}]},
  ]}
open(os.path.join(OUT, "vercel.json"), "w").write(json.dumps(vercel, indent=2) + "\n")
print("built", len(pages), "pages")
