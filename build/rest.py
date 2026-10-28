from lib import *
from content_industries import INDUSTRIES as _IND
_SLUG = {i['name'].replace('&amp;','&').split(' Management')[0].lower(): i['slug'] for i in _IND}

def industries():
    L = [
        ("wheat", "Rice Mill Management", "Orders, staff and payroll, client tracking, deliveries, live reports and a bilingual AI assistant in one portal.", "Live &amp; available", "live"),
        ("wheat", "Flour Mill Management", "Production tracking, inventory, orders and accounts built around flour mill operations.", "In development", "dev"),
        ("shirt", "Textile Mill Management", "Production stages, staff and client order tracking for fabric and garment manufacturing.", "In development", "dev"),
        ("barn", "Poultry, Cattle &amp; Dairy Farms", "Flock and herd records, feed tracking, health monitoring and sales management.", "In development", "dev"),
        ("dumbbell", "Gym Management", "Member sign-ups, attendance, membership renewals and payment reminders, fully automated.", "In development", "dev"),
        ("clinic", "Clinic Management", "Patient records, appointment booking, billing and automated follow-up reminders.", "In development", "dev"),
        ("coffee", "Café &amp; Restaurant Management", "Orders, inventory, staff shifts and sales reporting for cafés and restaurants.", "In development", "dev"),
        ("pill", "Pharmacy &amp; Medical Store", "Batch and expiry tracking, supplier orders, prescriptions and sales reporting.", "Custom build", "custom"),
        ("school", "School &amp; Academy Management", "Admissions, attendance, fee collection, timetables and parent communication.", "Custom build", "custom"),
        ("warehouse", "Warehouse &amp; Distribution", "Multi-location stock, inbound and outbound logistics, and route-linked deliveries.", "Custom build", "custom"),
        ("cart", "Retail &amp; POS", "Point of sale, product catalogues, stock sync and customer loyalty in one place.", "Custom build", "custom"),
        ("route", "Logistics &amp; Fleet", "Vehicle assignment, trip tracking, driver payments and maintenance schedules.", "Custom build", "custom"),
        ("building", "Real Estate &amp; Property", "Listings, tenants, rent collection, maintenance requests and owner statements.", "Custom build", "custom"),
        ("hardhat", "Construction &amp; Contracting", "Project budgets, site labour, materials, subcontractor payments and progress reports.", "Custom build", "custom"),
        ("scissors", "Salon &amp; Spa", "Bookings, stylist schedules, packages, inventory and reminders that cut no-shows.", "Custom build", "custom"),
    ]
    def _lk(t):
        key = t.replace('&amp;','&').split(' Management')[0].lower()
        for k, v in _SLUG.items():
            if key.startswith(k.split(',')[0]) or k.startswith(key.split(',')[0]):
                return f'<p style="margin-top:14px"><a class="link-arrow" href="industries/{v}.html">Learn more {ARROW}</a></p>'
        return ""
    cards = "".join(card(i, t, d, f'<span class="pill {k}">{p}</span>' + _lk(t), delay=(n % 3) * .06) for n, (i, t, d, p, k) in enumerate(L))
    hero = page_hero("Industries", "Systems shaped around your industry.",
        "Every sector has its own rhythm, vocabulary and bottlenecks. Our management systems and automations are built to respect that, from the first screen to the last report.")
    body = hero + f'''<section class="sec"><div class="wrap">
  {head("Industry solutions", "Live today, in development and built to order.", "Our rice mill management system is live. Others are in development, and anything else can be built to order, using the same secure foundation.")}
  <div class="grid g3">{cards}</div></div></section>
  <section class="sec light"><div class="wrap"><div class="split">
    <div class="reveal"><span class="eyebrow">Not listed?</span><h2 class="h2">If your business has a process, we can systemise it.</h2>
    <p>The industries above are where we have focused first, but the underlying approach is universal: understand the workflow, record every step once, automate what repeats and report on what matters.</p>
    <p style="margin-top:26px"><a class="btn btn-blue" href="contact.html">Describe your business {ARROW}</a></p></div>
    <div class="reveal" style="--d:.1s">{ticks(["Free demo built around your sector", "Fields, roles and reports tailored to you", "Data migration from spreadsheets and registers", "Bilingual English and Urdu interface", "Training for owners and staff"])}</div>
  </div></div></section>''' + cta_band()
    return page("industries.html", "Industry Management Software Solutions | ToolsRhino",
                "Management software built for your sector: rice mills, flour mills, textile units, farms, gyms, clinics, restaurants, pharmacies, schools and more.",
                body, label="Industries")


def about():
    hero = page_hero("About", "We build the systems behind businesses that mean business.",
        "ToolsRhino is a specialist sister company of Connectlyx, created to give AI automation, SaaS and management systems the dedicated focus they deserve.", ctas=False)
    body = hero + f'''
<section class="sec"><div class="wrap"><div class="split top">
  <div class="reveal"><span class="eyebrow">Our story</span><h2 class="h2">Born from a pattern we kept seeing.</h2>
    <p>Working with business owners through Connectlyx, one pattern kept repeating. Capable, hard-working people were running mills, clinics, shops and farms on a tangle of notebooks, spreadsheets and chat threads. Good businesses, held back by tools that never quite fit.</p>
    <p>Off-the-shelf software was either too generic or too heavy. Custom software felt out of reach. So we created ToolsRhino: a team devoted to building practical, affordable, intelligent systems that match the way real businesses operate.</p>
    <p>The name is deliberate. A rhino is tough, focused and difficult to stop once it is moving. That is the standard we hold our software to.</p></div>
  <div class="reveal" style="--d:.1s">
    <div class="lin-grid" style="grid-template-columns:1fr;gap:16px">
      <div class="card lin-card parent" style="padding:30px"><span class="tag">Parent</span><h3 style="font-size:1.6rem">Connectlyx</h3><p>Consulting, outsourcing, marketing and development under one roof.</p></div>
      <div class="lin-arrow" style="padding:6px 0"><div style="width:56px;height:56px;transform:rotate(90deg)">{ARROW}</div></div>
      <div class="card lin-card child" style="padding:30px"><span class="tag" style="color:var(--ice)">Specialist</span><h3 style="font-size:1.6rem">ToolsRhino</h3><p style="color:#D2E4F7">AI automation, SaaS products and management systems.</p></div>
    </div></div>
</div></div></section>

<section class="sec light"><div class="wrap">{head("How we think", "Four principles behind every build.")}
  <div class="grid g4">
    {card("target", "Start with the workflow", "We study how your people work before we propose anything. The software follows the business, never the reverse.")}
    {card("sparkle", "Make AI useful first", "We would rather automate one boring task perfectly than showcase ten features nobody asked for.", delay=.05)}
    {card("users", "Simple enough for the shop floor", "If a new team member cannot use it after a short walkthrough, we go back and simplify it.", delay=.1)}
    {card("life", "Stay after launch", "Go-live is the beginning of the relationship. We keep supporting, refining and extending.", delay=.15)}
  </div></div></section>

<section class="sec"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">Where we work</span><h2 class="h2">Serving businesses across the United States and worldwide.</h2>
    <p>Our systems are delivered online, so distance is rarely a barrier. We work with clients in English and Urdu, and we are comfortable adapting portals for local currencies, units, tax rules and ways of doing business.</p>
    <p style="margin-top:26px"><a class="btn btn-blue" href="contact.html">Start a conversation {ARROW}</a></p></div>
  <div class="reveal" style="--d:.1s"><div class="grid g2">
    {card("globe", "Worldwide delivery", "Remote onboarding, training and support across time zones.")}
    {card("chat", "Bilingual support", "English and Urdu, in the portal and on the phone.", delay=.05)}
    {card("phone", "Direct access", "Talk to the people building your system, by call, email or WhatsApp.", delay=.1)}
    {card("shield", "Secure by default", "Dedicated accounts and role-based access for every client.", delay=.15)}
  </div></div>
</div></div></section>''' + cta_band()
    return page("about.html", "About ToolsRhino | A Specialist Company of Connectlyx",
                "Learn how ToolsRhino, the specialist sister company of Connectlyx, builds AI automation, SaaS products and management systems for businesses worldwide.",
                body, label="About")


def contact():
    hero = page_hero("Contact", "Let's build something for your business.",
        "Tell us how you run today and what you would like to improve. We reply within one business day, usually sooner.", ctas=False)
    row = lambda ic, lab, val: f'<div class="c-row"><div class="ico">{icon(ic)}</div><div><small>{lab}</small>{val}</div></div>'
    body = hero + f'''<section class="sec" style="padding-top:20px"><div class="wrap"><div class="contact-grid">
  <div class="card contact-card reveal"><h2 class="h3" style="font-size:1.7rem;margin-bottom:8px">Reach us directly</h2><p>Serving businesses across the United States and worldwide.</p>
    <div style="margin-top:14px">
    {row("mail", "General inquiries", f'<a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a>')}
    {row("life", "Technical support", f'<a href="mailto:{EMAIL_SUPPORT}">{EMAIL_SUPPORT}</a>')}
    {row("phone", "Call", f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>')}
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px">
      <a class="btn wa" href="{WA}" target="_blank" rel="noopener">{WA_SVG.replace("<svg","<svg style='width:20px;height:20px'")} WhatsApp {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="{PARENT}" target="_blank" rel="noopener">Visit Connectlyx {EXT}</a></div></div>
  <form class="card contact-card form reveal" id="inquiryForm" style="--d:.1s">
    <h2 class="h3" style="font-size:1.7rem;margin-bottom:24px">Send us a message</h2>
    <div class="two"><div class="f"><label for="n">Your name</label><input id="n" name="name" type="text" placeholder="John Smith" required autocomplete="name"></div>
      <div class="f"><label for="e">Email address</label><input id="e" name="email" type="email" placeholder="you@company.com" required autocomplete="email"></div></div>
    <div class="f"><label for="s">What do you need?</label><select id="s" name="service"><option>Management system</option><option>AI automation</option><option>SaaS product creation</option><option>Not sure yet</option></select></div>
    <div class="f"><label for="m">Message</label><textarea id="m" name="message" placeholder="Tell us about your business and what you're looking for…" required></textarea></div>
    <input class="hp" type="text" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="btn btn-blue" type="submit">Send message {ARROW}</button>
    <div class="form-note" id="formStatus" role="status">We typically reply within 24 hours.</div>
  </form>
</div></div></section>''' + cta_band("Prefer to see it first?", "Book a live demo on WhatsApp and we'll walk you through a system built for your industry.")
    return page("contact.html", "Contact ToolsRhino | Book a Demo",
                "Contact ToolsRhino to book a demo. Email info@connectlyx.com, call +1 214 814 4539 or message us on WhatsApp. Serving businesses in the US and worldwide.",
                body, label="Contact")


def notfound():
    body = f'''<section class="page-hero" style="min-height:80vh;display:grid;align-items:center"><canvas class="ink" aria-hidden="true"></canvas><div class="wrap center" style="text-align:center">
  <span class="eyebrow">Error 404</span><h1 class="h1" style="margin:18px 0">This page wandered off.</h1>
  <p class="lead" style="margin:0 auto 32px">The link may be old or mistyped. Let's get you back on track.</p>
  <div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="index.html">Back to home {ARROW}</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div></div></section>'''
    return page("404.html", "Page not found | ToolsRhino", "The page you are looking for could not be found.", body, label="404")
