"""Shared layout, icons and helpers for the ToolsRhino static site generator."""
import json
from html import escape

SITE = "https://www.toolsrhino.com"
PHONE_DISPLAY = "+1 214 814 4539"
PHONE_TEL = "+12142148144539"[:0] + "+12148144539"
EMAIL_INFO = "info@connectlyx.com"
EMAIL_SUPPORT = "support@connectlyx.com"
WA = "https://wa.me/12148144539"
WA_DEMO = WA + "?text=Hi%2C%20I%27d%20like%20to%20book%20a%20demo."
PARENT = "https://www.connectlyx.com"

_I = {
 "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/><path d="m3 17.5 9 5 9-5" opacity=".5"/>',
 "bot": '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V5"/><circle cx="12" cy="3.8" r="1.2"/><circle cx="9" cy="14" r="1.2"/><circle cx="15" cy="14" r="1.2"/><path d="M2 14v2M22 14v2"/>',
 "rocket": '<path d="M12 15 9 12a22 22 0 0 1 2-4 12 12 0 0 1 10-5c0 3-1 8-5 10a22 22 0 0 1-4 2Z"/><circle cx="15.5" cy="8.5" r="1.3"/><path d="M9 12H5l2-3.5h3M12 15v4l3.5-2V14M5 15c-1.5 1.3-2 5-2 5s3.7-.5 5-2"/>',
 "factory": '<path d="M3 21V10l6 4V10l6 4V6h3v15Z"/><path d="M3 21h18"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.8 0 4.5 1.9 4.5 5"/>',
 "wallet": '<path d="M4 7a2 2 0 0 1 2-2h12v4"/><path d="M4 7v11a2 2 0 0 0 2 2h14V9H6a2 2 0 0 1-2-2Z"/><circle cx="16.5" cy="14.5" r="1.2"/>',
 "truck": '<path d="M2 6h11v10H2zM13 9h4l4 4v3h-8"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
 "chart": '<path d="M4 20V4M4 20h16"/><path d="m8 15 3-4 3 2 5-6"/>',
 "shield": '<path d="M12 3 4 6v6c0 4.5 3.2 7.8 8 9 4.8-1.2 8-4.5 8-9V6Z"/><path d="m9 12 2 2 4-4"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4Z"/><path d="M8 9.5h8M8 12.5h5"/>',
 "file": '<path d="M6 3h8l4 4v14H6Z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 "workflow": '<rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M6 9v3a3 3 0 0 0 3 3h6"/>',
 "plug": '<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0Z"/><path d="M12 17v4"/>',
 "database": '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "wheat": '<path d="M12 21V9"/><path d="M12 9c-2.5 0-4-1.6-4-4 2.5 0 4 1.6 4 4Zm0 0c2.5 0 4-1.6 4-4-2.5 0-4 1.6-4 4Zm0 5c-2.5 0-4-1.6-4-4 2.5 0 4 1.6 4 4Zm0 0c2.5 0 4-1.6 4-4-2.5 0-4 1.6-4 4Zm0 5c-2.5 0-4-1.6-4-4 2.5 0 4 1.6 4 4Zm0 0c2.5 0 4-1.6 4-4-2.5 0-4 1.6-4 4Z"/>',
 "shirt": '<path d="m8 3-5 4 3 3 2-1v12h8V9l2 1 3-3-5-4a4 4 0 0 1-8 0Z"/>',
 "barn": '<path d="M3 11 12 4l9 7v9H3Z"/><path d="M9 20v-6h6v6M3 11l9 5 9-5"/>',
 "dumbbell": '<path d="M6 7v10M18 7v10M3 10v4M21 10v4M6 12h12"/>',
 "clinic": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
 "coffee": '<path d="M4 8h13v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5Z"/><path d="M17 10h2a2 2 0 0 1 0 4h-2M8 3v2M12 3v2"/>',
 "pill": '<rect x="2.5" y="8.5" width="19" height="7" rx="3.5" transform="rotate(-40 12 12)"/><path d="m9.2 9.2 5.6 5.6"/>',
 "school": '<path d="m2 9 10-5 10 5-10 5Z"/><path d="M6 11.5V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.5M22 9v6"/>',
 "warehouse": '<path d="M3 9 12 4l9 5v11H3Z"/><path d="M8 20v-6h8v6M8 17h8"/>',
 "cart": '<path d="M3 4h2.5l2 11h10l2-8H7"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
 "building": '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10 21v-3h4v3"/>',
 "hardhat": '<path d="M3 18h18"/><path d="M5 18a7 7 0 0 1 14 0"/><path d="M12 7v4"/>',
 "scissors": '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="m8 8 12 10M8 16 20 6"/>',
 "route": '<circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H16a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h7.5"/>',
 "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8Z"/><path d="M19 16v4M17 18h4"/>',
 "code": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2Z"/>',
 "life": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="m5.6 5.6 3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "zap": '<path d="M13 2 4 14h7l-1 8 9-12h-7Z"/>',
 "dash": '<rect x="3" y="3" width="8" height="10" rx="1.5"/><rect x="13" y="3" width="8" height="6" rx="1.5"/><rect x="13" y="11" width="8" height="10" rx="1.5"/><rect x="3" y="15" width="8" height="6" rx="1.5"/>',
 "box": '<path d="m3 7 9-4 9 4v10l-9 4-9-4Z"/><path d="m3 7 9 4 9-4M12 11v10"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
 "cog": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
 "home": '<path d="m3 11 9-8 9 8v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1Z"/><path d="M9 21v-7h6v7"/>',
 "pin": '<path d="M12 21s7-6.2 7-11a7 7 0 0 0-14 0c0 4.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
}

def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>'

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_LONG = '<svg class="arr" viewBox="0 0 22 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 5h19M16 1l4 4-4 4"/></svg>'
EXT = '<svg width="11" height="11" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l6-6M4 3h5v5"/></svg>'
WA_SVG = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.7 6.4L3 29l6.8-1.8A13 13 0 1 0 16 3Zm0 23.7c-2 0-3.9-.5-5.6-1.5l-.4-.2-4 1 1.1-3.9-.3-.4A10.7 10.7 0 1 1 16 26.7Zm5.9-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3 2.9 1.2 2.9.8 3.4.7.5 0 1.9-.8 2.1-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4Z"/></svg>'

from content_industries import INDUSTRIES
from content_articles import ARTICLES

NAV = [
    ("index.html", "Home", None, None),
    ("services.html", "Services", [
        ("gym-command-center.html", "dumbbell", "Gym Command Center", "Our gym management SaaS, early access planned"),
        ("management-systems.html", "layers", "Management Systems", "Custom portals for industries and businesses"),
        ("ai-automation.html", "bot", "AI Automation", "Assistants, workflows and smart reporting"),
        ("saas-development.html", "rocket", "SaaS Product Creation", "From idea to a scalable subscription product"),
        ("services.html", "sparkle", "All services", "See everything we build and support"),
    ], "cols"),
    ("industries.html", "Industries",
        [(f"industries/{i['slug']}.html", i["icon"], i["name"].replace("&amp;", "&"), "") for i in INDUSTRIES]
        + [("industries.html", "sparkle", "All industries", "")], "cols compact"),
    ("insights.html", "Insights", None, None),
    ("about.html", "About", None, None),
    ("contact.html", "Contact", None, None),
]


def nav(cur):
    items = []
    for href, label, sub, kind in NAV:
        if sub:
            active = " active" if (cur == href or cur in [s[0] for s in sub]) else ""
            subs = "".join(
                f'<a href="{h}"><span class="ic">{icon(i)}</span><span><strong>{t}</strong>' + (f'<small>{d}</small>' if d else '') + '</span></a>'
                for h, i, t, d in sub)
            items.append(
                f'<li class="has-sub{active}"><a class="m" href="{href}">{label}'
                f'<svg class="caret" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="m2 3.5 3 3 3-3"/></svg></a>'
                f'<div class="sub {kind}">{subs}</div></li>')
        else:
            on = cur == href or (href == "insights.html" and cur.startswith("insights/"))
            cur_attr = ' aria-current="page"' if on else ""
            items.append(f'<li><a class="m" href="{href}"{cur_attr}>{label}</a></li>')
    mob = []
    for href, label, sub, kind in NAV:
        mob.append(f'<a href="{href}">{label}</a>')
        if label == "Services":
            mob += [f'<a class="child" href="{h}">{t}</a>' for h, i, t, d in sub[:3]]
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="strip"><div class="wrap"><span>ToolsRhino is the AI &amp; systems specialist of</span> <a href="{PARENT}" target="_blank" rel="noopener"><b>Connectlyx</b> {EXT}</a></div></div>
<div class="nav-shell"><nav class="nav" aria-label="Main">
  <a class="brand" href="index.html" aria-label="ToolsRhino home"><img src="assets/img/logo-light.png" alt="" width="55" height="34"><span><span class="brand-name">ToolsRhino</span><span class="brand-sub">by Connectlyx</span></span></a>
  <ul class="menu">{"".join(items)}</ul>
  <div class="nav-cta"><a class="btn btn-primary btn-sm" href="{WA_DEMO}" target="_blank" rel="noopener">Book a Demo {ARROW}</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile"><span></span></button></div>
</nav></div>
<div class="mobile" id="mobile">{"".join(mob)}<a class="btn btn-primary" href="{WA_DEMO}" target="_blank" rel="noopener">Book a Demo {ARROW}</a></div>
'''


def footer():
    ind = "".join(f'<li><a href="industries/{i["slug"]}.html">{i["name"]}</a></li>' for i in INDUSTRIES[:6])
    return f'''
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="assets/img/logo-light.png" alt="ToolsRhino" width="71" height="44">
        <p>AI automation, SaaS products and management systems for industries and businesses. Built with care, delivered worldwide.</p>
        <div class="foot-lineage"><a href="{PARENT}" target="_blank" rel="noopener">Connectlyx</a>{ARROW_LONG}<strong style="color:#fff">ToolsRhino</strong></div>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="management-systems.html">Management Systems</a></li>
        <li><a href="ai-automation.html">AI Automation</a></li>
        <li><a href="saas-development.html">SaaS Product Creation</a></li>
        <li><a href="gym-command-center.html">Gym Command Center</a></li>
        <li><a href="services.html">All Services</a></li></ul></div>
      <div><h4>Industries</h4><ul>{ind}<li><a href="industries.html">All industries</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="about.html">About ToolsRhino</a></li>
        <li><a href="insights.html">Insights</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="{PARENT}" target="_blank" rel="noopener">Connectlyx.com</a></li></ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a></li>
        <li><a href="mailto:{EMAIL_SUPPORT}">{EMAIL_SUPPORT}</a></li>
        <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp us</a></li></ul></div>
    </div>
    <div class="giant" aria-hidden="true">ToolsRhino</div>
    <div class="foot-bottom"><span>&copy; <span id="year">2026</span> ToolsRhino, a specialist company of Connectlyx. All rights reserved.</span><span>Serving businesses across the United States and worldwide.</span></div>
  </div>
</footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_SVG}</a>
<script src="assets/js/main.js" defer></script>
'''



def faq_html(items):
    out = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in items)
    return f'<div class="faq reveal">{out}</div>'


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumb_schema(slug, label, trail=()):
    items = [("Home", SITE + "/")]
    if slug != "index.html":
        items += [(n, SITE + "/" + h.replace(".html", "")) for n, h in trail]
        items.append((label, f"{SITE}/{slug.replace('.html', '')}"))
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "name": "ToolsRhino", "url": SITE + "/",
           "publisher": {"@type": "Organization", "name": "ToolsRhino"}}

ORG = {
    "@context": "https://schema.org", "@type": "Organization", "name": "ToolsRhino", "url": SITE + "/",
    "logo": SITE + "/assets/img/logo-navy.png",
    "description": "ToolsRhino builds AI automation, SaaS products and custom management systems for industries and businesses worldwide.",
    "parentOrganization": {"@type": "Organization", "name": "Connectlyx", "url": PARENT},
    "email": EMAIL_INFO, "telephone": "+1-214-814-4539",
    "areaServed": ["US", "Worldwide"],
    "contactPoint": [
        {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL_INFO, "telephone": "+1-214-814-4539", "availableLanguage": ["English", "Urdu"]},
        {"@type": "ContactPoint", "contactType": "technical support", "email": EMAIL_SUPPORT},
    ],
}


import re as _re

def clean(html):
    """Convert relative links to root-absolute clean URLs (Vercel cleanUrls)."""
    html = _re.sub(r'(href|src)="assets/', r'\1="/assets/', html)
    html = _re.sub(r'href="index\.html"', 'href="/"', html)
    html = _re.sub(r'href="([a-z0-9\-/]+)\.html"', r'href="/\1"', html)
    return html


def page(slug, title, desc, body, label=None, schemas=None, nav_cur=None, trail=(), og_type="website"):
    schemas = [ORG if slug == "index.html" else None, WEBSITE if slug == "index.html" else None,
               crumb_schema(slug, label or title, trail)] + (schemas or [])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n' for s in schemas if s)
    url = f"{SITE}/" if slug == "index.html" else f"{SITE}/{slug.replace('.html', '')}"
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#060D24">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" sizes="64x64" href="assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:site_name" content="ToolsRhino">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js')</script>
{ld}</head>
<body>
{nav(nav_cur or slug)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    return clean(html)


def page_hero(label, h1, lead, ctas=True, slug_label=None, h1_html=None, trail=(), meta=""):
    cta = ""
    if ctas:
        cta = (f'<div class="cta-row"><a class="btn btn-primary" href="{WA_DEMO}" target="_blank" rel="noopener">Book a Demo {ARROW}</a>'
               f'<a class="btn btn-ghost" href="contact.html">Talk to our team</a></div>')
    tr = "".join(f'<a href="{h}">{n}</a><span>/</span>' for n, h in trail)
    m = f'<p class="meta">{meta}</p>' if meta else ""
    return f'''<section class="page-hero">
  <canvas class="ink" aria-hidden="true"></canvas>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>{tr}<span aria-current="page">{label}</span></nav>
    <h1 class="h1">{h1_html or escape(h1)}</h1>
    {m}
    <p class="lead">{lead}</p>
    {cta}
  </div>
</section>'''


def cta_band(h="Let's put your operations on autopilot.", p="Tell us how your business runs today. We'll show you how it could run tomorrow."):
    return f'''<section class="sec" style="padding-top:40px"><div class="wrap"><div class="cta reveal">
  <canvas class="ink" aria-hidden="true"></canvas>
  <h2 class="h2">{h}</h2><p class="lead">{p}</p>
  <div class="cta-row"><a class="btn btn-primary" href="{WA_DEMO}" target="_blank" rel="noopener">Book a Demo {ARROW}</a><a class="btn btn-ghost" href="contact.html">Send us a message</a></div>
</div></div></section>'''


def head(eyebrow, h2, lead="", center=True, light=False):
    c = " center" if center else ""
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="sec-head{c} reveal"><span class="eyebrow">{eyebrow}</span><h2 class="h2">{h2}</h2>{l}</div>'


def card(ic, title, text, extra="", delay=0):
    return (f'<div class="card reveal" style="--d:{delay}s"><div class="ico">{icon(ic)}</div>'
            f'<h3 class="h3">{title}</h3><p>{text}</p>{extra}</div>')


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def timeline(steps):
    return '<div class="tl">' + "".join(
        f'<div class="tl-item reveal"><div class="n">{i+1}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, (t, d) in enumerate(steps)) + "</div>"
