from lib import *

INDUSTRIES_MARQUEE = ["Rice mills", "Flour mills", "Textile units", "Poultry &amp; dairy farms", "Gyms &amp; fitness clubs", "Clinics", "Cafés &amp; restaurants",
                      "Pharmacies", "Schools &amp; academies", "Warehouses", "Retail &amp; distribution", "Logistics fleets"]

FAQ_HOME = [
    ("What does ToolsRhino actually do?",
     "ToolsRhino designs and builds three things: custom management systems for industries and businesses, AI automation that removes repetitive work, and SaaS products for founders and companies turning expertise into software. Everything is delivered as a secure portal your team can use from a phone or a desktop."),
    ("How is ToolsRhino related to Connectlyx?",
     "Connectlyx is our parent company, a full-service consulting, outsourcing, marketing and development partner. ToolsRhino is its specialist sister company, set up so that AI automation, SaaS and management systems get a dedicated team and a sharper focus."),
    ("Do I need any technical skills to use these systems?",
     "No. We build for business owners and shop-floor teams, not developers. If you can use WhatsApp, you can use our portals. We also train your staff as part of onboarding."),
    ("How long does setup take?",
     "It depends on the system and how much existing data has to be brought in. We agree a clear timeline with you before any work begins, and setup and team training are included."),
    ("Is my business data secure?",
     "Yes. Every client receives a separate, secure account with owner-level and staff-level access controls, so people only see what their role requires. We are happy to walk you through the details on a call."),
    ("Can the system be customised for my business?",
     "Always. Two businesses in the same industry rarely run the same way, so we shape workflows, fields, reports and approvals around yours during onboarding rather than forcing you into a template."),
    ("Which regions do you serve?",
     "We work with businesses across the United States and worldwide. Our team supports clients in English and Urdu, and our portals can be bilingual."),
]


def build():
    mock = f'''
<div class="mock-stage reveal"><div class="mock">
  <div class="float-chip a"><span class="dot"></span>Payroll run completed</div>
  <div class="float-chip b">{icon("chat")}&nbsp;WhatsApp reminder sent to 23 clients</div>
  <div class="mock-in">
    <div class="mock-bar"><i></i><i></i><i></i><span class="url">app.yourbusiness.com / dashboard</span></div>
    <div class="mock-body">
      <div class="mock-side"><div class="logo"><img src="assets/img/logo-light.png" alt="">Your Mill</div>
        <div class="it on">Overview</div><div class="it">Orders</div><div class="it">Stock</div><div class="it">Staff &amp; payroll</div><div class="it">Clients</div><div class="it">Deliveries</div><div class="it">Reports</div></div>
      <div class="mock-main">
        <div class="kpis">
          <div class="kpi"><small>Orders today</small><b>148</b><em>▲ 12% vs last week</em></div>
          <div class="kpi"><small>Stock in hand</small><b>42.6 t</b><em>3 warehouses</em></div>
          <div class="kpi"><small>Payments pending</small><b>$18.4k</b><em>9 reminders queued</em></div>
        </div>
        <div class="mock-row">
          <div class="chart"><small>Dispatches, last 12 days</small><div class="bars">{"".join(f'<i style="height:{h}%;animation-delay:{i*.06:.2f}s"></i>' for i,h in enumerate([42,55,38,64,58,72,50,80,68,90,76,96]))}</div></div>
          <div class="chat"><small>AI assistant</small><div class="bub me">How much Super Kernel do we have?</div><div class="bub">42.6 tonnes across 3 warehouses. Shall I draft a restock order?</div></div>
        </div>
      </div>
    </div>
  </div>
</div><p class="center" style="font-size:12.5px;color:var(--dim);margin-top:22px">Illustrative interface. Every portal is configured around your own workflow.</p></div>'''

    hero = f'''<section class="hero">
  <canvas class="ink" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="hero-inner">
      <div class="lineage reveal"><a class="parent" href="{PARENT}" target="_blank" rel="noopener">Connectlyx</a>{ARROW_LONG}<span class="child"><img src="assets/img/logo-navy.png" alt="">ToolsRhino</span></div>
      <div><a class="home-badge reveal" href="gym-command-center.html"><b>NEW</b> Gym Command Center: early access planned {ARROW}</a></div>
      <h1 class="h1 reveal" style="--d:.08s">Management systems and AI automation that work as hard as you do.</h1>
      <p class="lead reveal" style="--d:.16s">ToolsRhino is the specialist arm of Connectlyx for AI automation, SaaS product creation and custom management systems. We replace scattered spreadsheets, paper registers and endless WhatsApp threads with one secure portal your whole team can actually use.</p>
      <div class="cta-row reveal" style="--d:.24s"><a class="btn btn-primary" href="services.html">Explore our services {ARROW}</a><a class="btn btn-ghost" href="{WA_DEMO}" target="_blank" rel="noopener">Book a demo</a></div>
      <div class="hero-tags reveal" style="--d:.32s"><span>AI automation</span><span>SaaS product creation</span><span>Management systems</span><span>English &amp; Urdu</span></div>
    </div>
    {mock}
  </div>
</section>'''

    marquee = '<div class="marquee" aria-label="Industries we build for"><div class="marquee-track">' + "".join(f"<span>{m}</span>" for m in INDUSTRIES_MARQUEE * 2) + '</div></div>'

    lineage = f'''<section class="sec lineage-sec"><div class="wrap">
  {head("Our story in one line", "One family. One sharp focus.", "Connectlyx has always helped businesses connect, scale and grow. ToolsRhino is where we put our deepest engineering effort: building the software and automation that lets those businesses run with less friction.")}
  <div class="lin-grid">
    <div class="card lin-card parent reveal"><span class="tag">Parent company</span><h3>Connectlyx</h3>
      <p>A full-service partner for growing businesses. <em>Connect. Scale. Grow.</em></p>
      <ul><li>Business consultancy and sales development</li><li>HR consultancy, BPO and outsourcing</li><li>Digital marketing and graphic design</li><li>Development and AI services</li></ul>
      <p style="margin-top:26px"><a class="link-arrow" href="{PARENT}" target="_blank" rel="noopener">Visit connectlyx.com {ARROW}</a></p></div>
    <div class="lin-arrow reveal"><div>{ARROW}</div></div>
    <div class="card lin-card child reveal" style="--d:.1s"><span class="tag" style="color:var(--ice)">Specialist sister company</span>
      <h3><img src="assets/img/logo-light.png" alt="" style="display:inline;height:40px;vertical-align:middle;margin-right:12px">ToolsRhino</h3>
      <p style="color:#D2E4F7">Focused entirely on three things, done properly:</p>
      <ul><li><strong>AI automation</strong> that takes repetitive work off your team</li><li><strong>SaaS product creation</strong> from first sketch to paying customers</li><li><strong>Management systems</strong> for industries and everyday businesses</li></ul>
      <p style="margin-top:26px"><a class="link-arrow" href="about.html" style="color:#fff">How we work {ARROW}</a></p></div>
  </div></div></section>'''

    def panel(i, h, p, tk, link, label, chips):
        return f'''<div class="panel" role="tabpanel" id="p{i}" aria-labelledby="t{i}">
  <div><h3>{h}</h3><p>{p}</p>{ticks(tk)}<a class="link-arrow" href="{link}">{label} {ARROW}</a></div>
  <div class="vis"><div class="stack">{"".join(f'<div class="row-chip"><div><b>{a}</b><br><span>{b}</span></div><em class="{c}">{d}</em></div>' for a,b,c,d in chips)}</div></div></div>'''

    tabs = f'''<section class="sec"><div class="wrap">
  {head("What we build", "Three disciplines. One accountable team.", "Whether you need to run an existing operation better or launch a new software product, the work falls into one of these three.")}
  <div data-tabs class="reveal">
    <div class="tabs" role="tablist" aria-label="Services">
      <button class="tab" role="tab" id="t0" aria-controls="p0">Management Systems</button>
      <button class="tab" role="tab" id="t1" aria-controls="p1">AI Automation</button>
      <button class="tab" role="tab" id="t2" aria-controls="p2">SaaS Product Creation</button></div>
    {panel(0, "Management systems that mirror how your business really runs",
      "Orders, stock, staff, payroll, payments and deliveries: most businesses juggle them across five tools and three notebooks. We bring them into one secure portal, shaped around your workflow instead of a generic template.",
      ["Orders, sales and client ledgers in a single place", "Role-based access for owners, managers and staff", "Live reports you can read in thirty seconds", "Bilingual interface in English and Urdu"],
      "management-systems.html", "Explore management systems",
      [("Order #2041", "Dispatch scheduled for 9:30 am", "", "In transit"), ("Payroll · October", "38 staff · attendance verified", "", "Approved"), ("Stock · Super Kernel", "Reorder level reached", "b", "42.6 t")])}
    {panel(1, "Automation that takes the repetitive work off your team's desk",
      "We wire intelligence into the parts of the business that quietly eat hours: follow-ups, data entry, document handling and reporting. The result is fewer errors, faster replies and a team free to do the work that needs a human.",
      ["AI assistants that answer in your customers' language", "WhatsApp and email workflows that follow up on their own", "Invoice, receipt and document capture without retyping", "Automated reports delivered where you already read them"],
      "ai-automation.html", "Explore AI automation",
      [("Invoice scanned", "Ledger updated automatically", "", "Done"), ("Payment reminder", "Sent to 23 clients on WhatsApp", "b", "Sent"), ("Weekly report", "Delivered every Monday, 8 am", "", "Scheduled")])}
    {panel(2, "From idea to subscription product, built to scale",
      "If you are turning expertise into software, we handle the architecture, the build and the launch. Multi-tenant foundations, billing and admin tooling come as standard, so you can spend your energy on customers instead of plumbing.",
      ["Discovery, product scoping and a working MVP", "Multi-tenant architecture, subscriptions and onboarding", "Admin console, analytics and audit trails", "Roadmap support long after launch"],
      "saas-development.html", "Explore SaaS creation",
      [("Tenant · Acme Foods", "Workspace provisioned", "", "Active"), ("Plan · Growth", "Billed monthly, 14-day trial", "b", "Live"), ("Release 1.4", "Deployed to production", "", "Passing")])}
  </div></div></section>'''

    from gcc import dashboard
    feature = f'''<section class="sec feature-band"><div class="wrap" style="max-width:1160px">
  {head("Our first SaaS product", "Meet Gym Command Center.", "A gym management platform for owners who want one dashboard for members, billing, attendance and leads, with a clear view of what needs attention first.")}
  {dashboard()}
  <div class="cta-row reveal" style="margin-top:44px"><a class="btn btn-primary" href="gym-command-center.html">Explore Gym Command Center {ARROW}</a><a class="btn btn-ghost" href="contact.html?interest=gym-command-center">Join the early-access list</a></div>
  <p class="g-note">Illustrative preview with sample data. Early access is planned once onboarding, security and core workflows are verified.</p>
</div></section>'''

    stats = f'''<section class="sec-tight"><div class="wrap"><div class="stats reveal">
  <div class="stat"><b data-count="8" data-suffix="+">8+</b><span>Industry systems in development</span></div>
  <div class="stat"><b>24/7</b><span>AI assistant support built into every portal</span></div>
  <div class="stat"><b data-count="2">2</b><span>Languages supported, English and Urdu</span></div>
  <div class="stat"><b>Free</b><span>Setup and team training included with every project</span></div>
</div></div></section>'''

    SL = ["rice-mill-management-software", "flour-mill-management-software", "textile-mill-management-software", "poultry-dairy-farm-management-software",
          "GCC", "clinic-management-software", "restaurant-cafe-management-software"]
    def ind(ic, t, d, pill, kind, i):
        lk = f'<p style="margin-top:14px"><a class="link-arrow" href="{"gym-command-center" if SL[i] == "GCC" else "industries/" + SL[i]}.html">Learn more {ARROW}</a></p>' if i < len(SL) else ""
        return card(ic, t, d, f'<span class="pill {kind}">{pill}</span>' + lk, delay=i * .05)
    inds = f'''<section class="sec light"><div class="wrap">
  {head("Industries", "Built for the businesses that run on the ground.", "From mills and farms to clinics and cafés, the same intelligent foundation, adapted to how each industry actually works.")}
  <div class="grid g4">
    {ind("wheat", "Rice Mill Management", "Orders, staff and payroll, client tracking, deliveries, live reports and a bilingual AI assistant in one portal.", "In development", "dev", 0)}
    {ind("wheat", "Flour Mill Management", "Production tracking, inventory, orders and accounts built around flour mill operations.", "In development", "dev", 1)}
    {ind("shirt", "Textile Mill Management", "Production stages, staff and client order tracking for fabric and garment manufacturing.", "In development", "dev", 2)}
    {ind("barn", "Poultry, Cattle &amp; Dairy Farms", "Flock and herd records, feed tracking, health monitoring and sales management.", "In development", "dev", 3)}
    {ind("dumbbell", "Gym Command Center", "Members, memberships, invoices, payments, attendance and leads in one dashboard for gym owners.", "Early access planned", "dev", 4)}
    {ind("clinic", "Clinic Management", "Patient records, appointment booking, billing and automated follow-up reminders.", "In development", "dev", 5)}
    {ind("coffee", "Café &amp; Restaurant Management", "Orders, inventory, staff shifts and sales reporting for food businesses.", "In development", "dev", 6)}
    {ind("sparkle", "Your industry, built to order", "Pharmacies, schools, warehouses, retail, logistics and more. If it has a process, we can systemise it.", "Custom build", "custom", 7)}
  </div>
  <p class="center reveal" style="margin-top:44px"><a class="btn btn-blue" href="industries.html">See all industries {ARROW}</a></p>
</div></section>'''

    steps = f'''<section class="sec"><div class="wrap">
  {head("How it works", "From first conversation to fully live, in four steps.", "No lengthy IT project. No jargon. You stay in control of what gets built and when.")}
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Discover</h3><p>A short call or demo. We learn how your business runs today and where time and money quietly leak.</p></div>
    <div class="step reveal" style="--d:.08s"><div class="n">02</div><h3>Design</h3><p>We map your workflows into a clear blueprint: modules, roles, reports and the automations worth building first.</p></div>
    <div class="step reveal" style="--d:.16s"><div class="n">03</div><h3>Build &amp; configure</h3><p>We set up your portal, bring in your existing data and connect the tools you already use, such as WhatsApp.</p></div>
    <div class="step reveal" style="--d:.24s"><div class="n">04</div><h3>Launch &amp; grow</h3><p>We train your team, go live with you and keep improving the system as your business changes.</p></div>
  </div></div></section>'''

    why = f'''<section class="sec light"><div class="wrap">
  {head("Why ToolsRhino", "Software that feels like it was made for your team.", "Plenty of vendors sell software. We try to build the thing you would have built yourself, if you had the time and a team of engineers.")}
  <div class="grid g3">
    {card("target", "Built around your workflow", "We watch how work really happens, then build to match. Your team is never forced into someone else's template.", delay=0)}
    {card("sparkle", "AI woven in, not bolted on", "Intelligence sits inside the daily workflow, answering questions, drafting reminders and flagging problems early.", delay=.05)}
    {card("globe", "Speaks your team's language", "Bilingual portals in English and Urdu, so everyone from the owner to the floor supervisor is comfortable.", delay=.1)}
    {card("chat", "WhatsApp-first communication", "Your staff and clients already live on WhatsApp. Reminders, confirmations and quick queries meet them there.", delay=.15)}
    {card("shield", "Secure by design", "Every client gets a dedicated account with owner and staff-level permissions, so sensitive figures stay where they belong.", delay=.2)}
    {card("life", "Free setup and training", "We configure the portal, load your data and train your people. No technical background needed on your side.", delay=.25)}
  </div></div></section>'''

    est = f'''<section class="sec"><div class="wrap">
  {head("A quick reality check", "How many hours is manual work costing you?", "Move the sliders to describe your team. It takes ten seconds and the answer is usually a surprise.")}
  <div class="est reveal" data-estimator>
    <div class="est-in">
      <div class="field" style="margin-top:0"><label for="r1">Team members handling admin work <output>8</output></label><input id="r1" type="range" min="1" max="100" value="8"></div>
      <div class="field"><label for="r2">Hours each, per week, on repetitive tasks <output>6</output></label><input id="r2" type="range" min="1" max="30" value="6"></div>
      <div class="field"><label for="r3">Share of that work we could realistically automate <output>40%</output></label><input id="r3" type="range" min="10" max="80" value="40" data-fmt="pct"></div>
    </div>
    <div class="est-out"><small>Time you could win back each year</small>
      <div class="big"><span data-out-hours>0</span> hrs</div>
      <p>That is roughly <strong><span data-out-days>0</span> working days</strong> your team could spend on customers, quality and growth instead.</p>
      <p class="fine">Illustrative estimate based on 48 working weeks and an 8-hour day. A discovery call gives you a figure grounded in your real processes.</p>
      <p style="margin-top:22px;position:relative;z-index:1"><a class="btn btn-primary btn-sm" href="contact.html">Get my real number {ARROW}</a></p></div>
  </div></div></section>'''

    from seo_pages import post_card, ART
    teaser = f'''<section class="sec light"><div class="wrap">{head("From the Insights blog", "Practical reading for owners and founders.", "Plain-spoken guides on management systems, automation and building software products.")}
  <div class="grid g3">{"".join(post_card(ART[s], n * .06) for n, s in enumerate(["what-is-a-management-system", "ai-automation-examples-for-small-business", "excel-vs-custom-management-software"]))}</div>
  <p class="center reveal" style="margin-top:40px"><a class="btn btn-blue" href="insights.html">All insights {ARROW}</a></p></div></section>'''

    faq = f'''<section class="sec" style="padding-top:20px"><div class="wrap">
  {head("Questions, answered", "Things business owners ask us first.")}
  {faq_html(FAQ_HOME)}</div></section>'''

    body = hero + marquee + lineage + tabs + feature + stats + inds + steps + why + est + teaser + faq + cta_band()
    return page("index.html",
                "AI Automation & Custom Management Systems | ToolsRhino",
                "ToolsRhino, a Connectlyx company, builds AI automation, SaaS products and custom management systems for mills, clinics, gyms and growing businesses.",
                body, label="Home", schemas=[faq_schema(FAQ_HOME)])
