import re
from html import escape
from lib import *
from content_industries import INDUSTRIES, DEV_NOTE
from content_articles import ARTICLES

ART = {a["slug"]: a for a in ARTICLES}
IND = {i["slug"]: i for i in INDUSTRIES}
PUB = "2026-10-28"


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def post_card(a, delay=0):
    return (f'<a class="card post reveal" style="--d:{delay}s" href="insights/{a["slug"]}.html"><span class="tagline">{a["tag"]} · {a["read"]} min read</span>'
            f'<h3 class="h3">{a["h1"]}</h3><p>{a["desc"]}</p><span class="link-arrow">Read article {ARROW}</span></a>')


# ----------------------------------------------------------------------------- industry page
def industry_page(i):
    slug = f"industries/{i['slug']}.html"
    live = i["status"] == "live"
    pill = '<span class="pill live">Live &amp; available</span>' if live else ('<span class="pill dev">Early access planned</span>' if i.get("product") else '<span class="pill dev">In development</span>')
    hero = page_hero(strip_tags(i["name"]), i["h1"], i["lead"], trail=[("Industries", "industries.html")])
    prod = i.get("product")
    if prod:
        callout = (f'<div class="callout reveal"><strong>Early access planned.</strong> This sector is served by our product Gym Command Center, now in its final development and production-readiness phase. '
                   f'<p style="margin-top:16px"><a class="btn btn-blue btn-sm" href="{prod[0]}">{prod[1]} {ARROW}</a></p></div>')
    elif live:
        callout = '<div class="callout live reveal"><strong>Live and available.</strong> This system is running today.</div>'
    else:
        callout = f'<div class="callout reveal"><strong>In development.</strong> {DEV_NOTE}</div>'
    pains = '<ul class="ticks">' + "".join(f"<li>{p}</li>" for p in i["pains"]) + "</ul>"
    problem = f'''<section class="sec"><div class="wrap"><div class="split top">
  <div class="reveal"><span class="eyebrow">The challenge</span><h2 class="h2">Where the day-to-day usually leaks time and money.</h2>
    <p>{i["intro"][0]}</p><p>{i["intro"][1]}</p>{pill}</div>
  <div class="card reveal" style="--d:.1s;padding:36px"><h3 class="h3" style="margin-bottom:18px">Sound familiar?</h3>{pains}</div>
</div></div></section>'''
    mods = '<div class="grid g4">' + "".join(card(ic, t, d, delay=(n % 4) * .05) for n, (ic, t, d) in enumerate(i["modules"])) + "</div>"
    modules = f'<section class="sec light"><div class="wrap">{head("What it covers", f"Everything a {strip_tags(i["name"]).lower()} operation needs.", "Each module is configured around your own workflow, so the portal feels familiar from day one.")}{mods}{callout}</div></section>'
    how = f'''<section class="sec"><div class="wrap">{head("Getting started", "A clear path from first call to go-live.")}
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Talk and demo</h3><p>Tell us how you run today. We show you how the system would work and note what is different about your business.</p></div>
    <div class="step reveal" style="--d:.08s"><div class="n">02</div><h3>Configure</h3><p>We shape modules, fields, roles and reports around your process and import your existing records.</p></div>
    <div class="step reveal" style="--d:.16s"><div class="n">03</div><h3>Train</h3><p>Your team learns on their own data, with us alongside, in English or Urdu.</p></div>
    <div class="step reveal" style="--d:.24s"><div class="n">04</div><h3>Go live and grow</h3><p>We keep supporting, refining and adding automation as your needs change.</p></div>
  </div></div></section>'''
    art = ART[i["article"]]
    read = f'<section class="sec light" style="padding-block:80px"><div class="wrap">{head("Related reading", "A useful read before you decide.", center=True)}<div class="grid g2" style="max-width:860px;margin-inline:auto">{post_card(art)}{post_card(ART["ai-automation-examples-for-small-business"] if art["slug"] != "ai-automation-examples-for-small-business" else ART["what-is-a-management-system"], .06)}</div></div></section>'
    faq = f'<section class="sec"><div class="wrap">{head("FAQ", f"{strip_tags(i["name"])} software questions")}{faq_html(i["faq"])}</div></section>'
    others = [o for o in INDUSTRIES if o["slug"] != i["slug"]][:6]
    more = f'<section class="sec-tight"><div class="wrap"><div class="chips reveal" style="justify-content:center">' + "".join(
        f'<a href="industries/{o["slug"]}.html" style="padding:9px 18px;border-radius:999px;border:1px solid var(--line-strong);font-size:14.5px;background:rgba(255,255,255,.04)">{o["name"]}</a>' for o in others) + '</div></div></section>'
    body = hero + problem + modules + how + read + faq + more + cta_band(f"Ready to see it for your business?", "Book a short demo. We'll show you how the system would run your operation, using your own workflow as the starting point.")
    schemas = [faq_schema(i["faq"]), {"@context": "https://schema.org", "@type": "Service", "name": strip_tags(i["name"]) + " software",
               "serviceType": "Management software development", "provider": {"@type": "Organization", "name": "ToolsRhino", "url": SITE},
               "areaServed": "Worldwide", "description": i["desc"]}]
    return page(slug, i["title"], i["desc"], body, label=strip_tags(i["name"]), schemas=schemas, nav_cur=slug, trail=[("Industries", "industries.html")])


# ----------------------------------------------------------------------------- article page
def render_blocks(blocks):
    out = []
    for b in blocks:
        if isinstance(b, str):
            out.append(f"<p>{b}</p>")
        else:
            tag, items = b
            out.append(f"<{tag}>" + "".join(f"<li>{x}</li>" for x in items) + f"</{tag}>")
    return "".join(out)


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def article_page(a):
    slug = f"insights/{a['slug']}.html"
    hero = page_hero(a["title"].split(":")[0], a["h1"], a["intro"], ctas=False, trail=[("Insights", "insights.html")],
                     meta=f'ToolsRhino Team · <time datetime="{PUB}">October 28, 2026</time> · {a["read"]} min read')
    toc = '<nav class="toc" aria-label="In this article"><strong>In this article</strong><ol>' + "".join(
        f'<li><a href="#{slugify(h)}">{h}</a></li>' for h, _ in a["sections"]) + '<li><a href="#faq">Frequently asked questions</a></li></ol></nav>'
    secs = "".join(f'<h2 id="{slugify(h)}">{h}</h2>{render_blocks(b)}' for h, b in a["sections"])
    faqs = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(an)}</p></details>" for q, an in a["faq"])
    rel = "".join(post_card(ART[r], n * .06) for n, r in enumerate(a["related"]))
    body = hero + f'''<section class="sec" style="padding-top:20px"><div class="wrap"><div class="article-wrap">
  <article class="prose">{toc}{secs}
    <div class="callout reveal"><strong>Want this done for your business?</strong> <a href="contact.html">Tell us what you need</a> and we will reply within one business day, or take the next step below.
      <p style="margin-top:16px"><a class="btn btn-blue btn-sm" href="{a["link"][0]}">{a["link"][1]} {ARROW}</a></p></div>
    <h2 id="faq">Frequently asked questions</h2><div class="faq" style="margin:0">{faqs}</div>
  </article></div></div></section>
  <section class="sec light" style="padding-block:80px"><div class="wrap">{head("Keep reading", "More from ToolsRhino Insights.")}<div class="grid g2" style="max-width:860px;margin-inline:auto">{rel}</div></div></section>''' + cta_band()
    ld = [faq_schema(a["faq"]), {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": a["h1"], "description": a["desc"],
        "datePublished": PUB, "dateModified": PUB, "inLanguage": "en",
        "author": {"@type": "Organization", "name": "ToolsRhino", "url": SITE},
        "publisher": {"@type": "Organization", "name": "ToolsRhino", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo-navy.png"}},
        "mainEntityOfPage": f"{SITE}/{slug.replace('.html', '')}", "image": SITE + "/assets/img/og-image.png"}]
    return page(slug, a["title"] + " | ToolsRhino" if len(a["title"]) <= 44 else a["title"], a["desc"], body, label=a["title"].split(":")[0],
                schemas=ld, nav_cur=slug, trail=[("Insights", "insights.html")], og_type="article")


# ----------------------------------------------------------------------------- insights index
def insights_index():
    hero = page_hero("Insights", "Insights on management systems, AI automation and SaaS.",
                     "Practical, plain-spoken guides for business owners and founders, written by the team that builds these systems every day.", ctas=False)
    cards = "".join(post_card(a, (n % 3) * .06) for n, a in enumerate(ARTICLES))
    body = hero + f'<section class="sec" style="padding-top:20px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>' + cta_band()
    return page("insights.html", "Insights: Management Systems, AI & SaaS | ToolsRhino",
                "Practical guides on management systems, AI automation, WhatsApp workflows, rice mill software and SaaS MVP development from the ToolsRhino team.",
                body, label="Insights",
                schemas=[{"@context": "https://schema.org", "@type": "Blog", "name": "ToolsRhino Insights", "url": SITE + "/insights",
                          "blogPost": [{"@type": "BlogPosting", "headline": a["h1"], "url": f"{SITE}/insights/{a['slug']}"} for a in ARTICLES]}])
