from lib import *

def related(*slugs):
    from seo_pages import post_card, ART
    return f'<section class="sec light" style="padding-block:80px"><div class="wrap">{head("Related reading", "Go deeper before you decide.")}<div class="grid g2" style="max-width:860px;margin-inline:auto">' + ''.join(post_card(ART[x], n * .06) for n, x in enumerate(slugs)) + '</div></div></section>'


def vis(chips):
    return '<div class="stack" style="width:100%">' + "".join(
        f'<div class="row-chip"><div><b>{a}</b><br><span>{b}</span></div><em class="{c}">{d}</em></div>' for a, b, c, d in chips) + "</div>"

# --------------------------------------------------------------------- SERVICES
FAQ_SERVICES = [
    ("Which service should I start with?",
     "Most clients begin with a management system, because it puts the foundations in place: clean data, clear roles and one source of truth. AI automation then plugs into that foundation. If you are building a software product to sell, start with SaaS product creation instead."),
    ("Do you work with small businesses or only large companies?",
     "Both. Our portals are designed so that a single-site business can be running within days, while the same architecture scales to multi-branch operations."),
    ("Can you connect to the tools we already use?",
     "In most cases, yes. We integrate with WhatsApp Business, email and SMS providers, payment gateways, accounting tools and spreadsheets through their official APIs or structured imports."),
    ("What happens after the system goes live?",
     "We stay. Support, training for new staff and continuous improvements are part of the relationship, and you can always reach us at support@connectlyx.com."),
]

def services():
    big = lambda i, ic, h, p, tk, link, chips: f'''<div class="svc-big reveal"><div class="svc-txt"><span class="num-big">0{i} · {icon(ic).replace('<svg','<svg style="width:15px;height:15px;display:inline;vertical-align:-2px"')}</span>
  <h2>{h}</h2><p>{p}</p>{ticks(tk)}<a class="link-arrow" href="{link}">Learn more {ARROW}</a></div><div class="svc-vis">{vis(chips)}</div></div>'''

    hero = page_hero("Services", "AI automation, SaaS and management systems, engineered for real operations.",
        "ToolsRhino exists for one reason: to make businesses run with less friction. We design, build and support the software and automation that sit quietly behind an efficient company.")

    main = f'''<section class="sec"><div class="wrap">
  {big(1, "layers", "Custom management system development",
       "A management system is the backbone of an organised business. We build secure, role-based portals that bring orders, inventory, people, payments and deliveries into one place, with the reports an owner needs at a glance.",
       ["Operations, inventory and order management", "Staff, attendance and payroll", "Client, supplier and payment ledgers", "Dashboards and exportable reports"],
       "management-systems.html", [("Orders", "148 processed today", "", "Live"), ("Inventory", "3 items below reorder level", "b", "Alert"), ("Payroll", "October cycle ready", "", "Approved")])}
  {big(2, "bot", "AI automation services",
       "We apply AI where it earns its keep: answering routine questions, chasing payments, reading documents and compiling reports. Each automation is scoped to a measurable result, then monitored and refined after launch.",
       ["AI assistants and customer-facing chat", "WhatsApp, email and SMS workflow automation", "Document, invoice and receipt processing", "Smart alerts, summaries and scheduled reports"],
       "ai-automation.html", [("Support query", "Answered in Urdu, 4 seconds", "", "Resolved"), ("Invoice #8841", "Captured and posted to ledger", "b", "Auto"), ("Overdue payments", "Reminders sent on WhatsApp", "", "23 sent")])}
  {big(3, "rocket", "SaaS product creation",
       "For founders and companies turning a good idea into a subscription product. We take you from discovery and design through MVP, launch and scale, with multi-tenant architecture, billing and admin tooling built the right way from the start.",
       ["Product discovery, scoping and UX design", "MVP development and iterative releases", "Multi-tenant architecture and subscription billing", "Analytics, admin console and roadmap support"],
       "saas-development.html", [("Workspace", "Provisioned in 8 seconds", "", "Active"), ("Subscription", "Growth plan, renews monthly", "b", "Billing"), ("Release", "v1.4 deployed", "", "Passing")])}
</div></section>'''

    extras = f'''<section class="sec light"><div class="wrap">
  {head("Wrapped around every project", "The supporting work that makes software stick.", "Good systems fail when the surrounding details are ignored. These are included in how we work, not sold as afterthoughts.")}
  <div class="grid g3">
    {card("dash", "Web portals and dashboards", "Clean, fast interfaces for owners, managers, staff and clients, designed to work on a phone as comfortably as on a desktop.")}
    {card("plug", "Integrations and APIs", "WhatsApp Business, payment gateways, accounting packages, email and SMS. We connect the tools you already depend on.", delay=.05)}
    {card("database", "Data migration and clean-up", "We bring your spreadsheets and registers across, tidy duplicates and set things up so day one starts with accurate numbers.", delay=.1)}
    {card("chart", "Analytics and reporting", "Profit, stock movement, staff performance, receivables: reports shaped around the questions you actually ask.", delay=.15)}
    {card("lock", "Security and access control", "Owner, manager and staff permissions, activity trails and sensible backups, because trust is part of the product.", delay=.2)}
    {card("life", "Training and ongoing support", "Hands-on onboarding for your team and a responsive support channel after launch, in English and Urdu.", delay=.25)}
  </div></div></section>'''

    models = f'''<section class="sec"><div class="wrap">
  {head("Ways to work with us", "Pick the engagement that fits where you are.")}
  <div class="grid g3">
    {card("box", "Done-for-you system", "We scope, build, configure and launch your management system or automation end to end, and train your team to run it.")}
    {card("code", "Product build partnership", "A dedicated team takes your SaaS concept from design to launch, working in short cycles with you in the loop.", delay=.05)}
    {card("cog", "Continuous improvement", "Already have a system or a process? We refine, extend and automate it month by month as your needs evolve.", delay=.1)}
  </div></div></section>'''

    faq = f'<section class="sec" style="padding-top:20px"><div class="wrap">{head("FAQ", "About our services")}{faq_html(FAQ_SERVICES)}</div></section>'
    body = hero + main + extras + models + faq + cta_band()
    return page("services.html", "AI Automation & Management System Services | ToolsRhino",
                "Explore ToolsRhino's services: custom management system development, AI automation, workflow automation and SaaS product creation for businesses worldwide.",
                body, label="Services", schemas=[faq_schema(FAQ_SERVICES), {"@context": "https://schema.org", "@type": "Service", "name": "AI automation, SaaS and management system development", "provider": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "areaServed": "Worldwide"}])


# --------------------------------------------------------------------- MANAGEMENT SYSTEMS
FAQ_MS = [
    ("What is a management system, in plain terms?",
     "It is a single secure portal where the daily running of your business lives: orders, stock, staff, payments, deliveries and reports. Instead of five spreadsheets and a notebook, everyone works from the same live information."),
    ("How is this different from a large ERP package?",
     "Traditional ERP software is powerful but heavy, expensive to configure and built for big corporations. Our systems are lighter and tailored to your industry, so your team learns them in days and you pay only for what you actually use."),
    ("Can it replace our Excel sheets?",
     "Yes. We import your existing sheets, clean them and move the logic into the portal, including formulas, ledgers and reports. You keep the ability to export to Excel whenever you like."),
    ("Will it work on phones?",
     "Yes. The portals are responsive, so owners can check figures from a phone and floor staff can record entries without a computer."),
    ("Can you customise it for the way we work?",
     "That is the point. Fields, approvals, user roles and reports are shaped around your processes during onboarding, and we adjust them as the business changes."),
    ("How much does a management system cost?",
     "It depends on scope, the number of modules and how much needs integrating. After a short discovery call we give you a clear proposal, so there are no surprises."),
]

SLUGS = ['rice-mill-management-software', 'flour-mill-management-software', 'textile-mill-management-software', 'poultry-dairy-farm-management-software', 'gym-management-software', 'clinic-management-software', 'restaurant-cafe-management-software']

def management():
    hero = page_hero("Management Systems", "Management systems that finally match the way you work.",
        "Custom management system development for industries and businesses: one portal for operations, people, payments and reporting, designed around your workflow and ready within days.")
    what = f'''<section class="sec"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">What it is</span><h2 class="h2">One source of truth for the whole business.</h2>
    <p>Most growing businesses did not choose their tools; they inherited them. A spreadsheet for orders, a notebook for staff attendance, a WhatsApp group for deliveries, and an accountant who reconciles it all at month-end.</p>
    <p>A management system replaces that patchwork with a single, secure portal. Every order, payment and shift is recorded once, visible to the people who need it, and reflected instantly in your reports. It is business management software, but tailored to your sector and your habits rather than a one-size-fits-all package.</p>
    <p style="margin-top:26px"><a class="btn btn-blue" href="{WA_DEMO}" target="_blank" rel="noopener">See a live demo {ARROW}</a></p></div>
  <div class="reveal" style="--d:.1s"><div class="vis" style="aspect-ratio:1">{vis([("Order #2041", "Client: Al-Noor Traders", "", "Dispatched"), ("Payment received", "$4,250 · Bank transfer", "b", "Matched"), ("Attendance", "36 of 38 staff present", "", "Today"), ("Stock level", "Super Kernel · 42.6 t", "b", "Healthy")])}</div></div>
</div></div></section>'''

    compare = f'''<section class="sec light"><div class="wrap">
  {head("Before and after", "What changes when the system goes live.")}
  <div class="compare">
    <div class="card before reveal"><h3>Before</h3><ul>
      <li>Orders scattered across notebooks, chats and sheets</li><li>Stock counts that are only right on the day someone checks</li>
      <li>Payroll built by hand, every month, with errors</li><li>Payments chased manually and forgotten</li><li>Reports that arrive days after you needed them</li></ul></div>
    <div class="card after reveal" style="--d:.1s"><h3>After</h3><ul>
      <li>Every order logged once, tracked until delivery</li><li>Live stock levels with reorder alerts</li>
      <li>Attendance-linked payroll in a few clicks</li><li>Automatic payment reminders by WhatsApp</li><li>Dashboards that are current the moment you open them</li></ul></div>
  </div></div></section>'''

    mods = [("wallet", "Orders, sales and invoicing", "Quotations, orders, invoices and client ledgers, linked end to end."),
            ("box", "Inventory and stock", "Multi-location stock, batch tracking and reorder alerts that prevent shortages."),
            ("users", "Staff, attendance and payroll", "Shifts, leave, overtime and salary runs that calculate themselves."),
            ("link", "Clients and suppliers", "A complete history of every account, balance and conversation."),
            ("truck", "Delivery and dispatch", "Plan routes, assign vehicles and confirm drop-offs with proof."),
            ("chart", "Reports and analytics", "Profit, receivables, productivity and trends, filtered by date, branch or team."),
            ("lock", "Roles and permissions", "Owner, manager and staff views, so sensitive numbers stay private."),
            ("bot", "Built-in AI assistant", "Ask questions in plain English or Urdu and get answers from your own data."),
            ("chat", "WhatsApp and email alerts", "Automatic confirmations, reminders and summaries sent from the system.")]
    mgrid = '<div class="grid g3">' + "".join(
        f'<div class="card reveal" style="--d:{(i%3)*.06}s"><div class="mod"><div class="ico">{icon(ic)}</div><div><h3>{t}</h3><p>{d}</p></div></div></div>'
        for i, (ic, t, d) in enumerate(mods)) + "</div>"
    modules = f'<section class="sec"><div class="wrap">{head("Modules", "Everything your operation needs, nothing it doesn’t.", "We assemble the portal from proven modules, then shape each one to your workflow. Start small and add more as you grow.")}{mgrid}</div></section>'

    inds = ["Rice mills", "Flour mills", "Textile units", "Poultry, cattle &amp; dairy", "Gyms &amp; fitness", "Clinics", "Cafés &amp; restaurants", "Pharmacies", "Schools", "Warehouses", "Retail &amp; distribution", "Logistics"]
    ind = f'''<section class="sec light"><div class="wrap">{head("Industries", "Proven foundations, tailored to your sector.", "Our rice mill management system is live today, and further industry systems are on the way. If yours is not listed, we build it to order.")}
  <div class="chips reveal" style="justify-content:center">{"".join((f"<a href='industries/{SLUGS[n]}.html' style='padding:9px 18px;border-radius:999px;border:1px solid #CDE4F6;background:#fff;color:var(--navy);font-size:14.5px'>{i}</a>" if n < len(SLUGS) else f"<span style='background:#fff;border-color:#CDE4F6;color:var(--navy)'>{i}</span>") for n, i in enumerate(inds))}</div>
  <p class="center reveal" style="margin-top:40px"><a class="link-arrow" href="industries.html">Browse industry systems {ARROW}</a></p></div></section>'''

    proc = f'''<section class="sec"><div class="wrap">{head("Our process", "How we build your management system.")}{timeline([
        ("Discovery and demo", "We sit with you, understand how work flows through the business and show a live example from your sector."),
        ("Blueprint", "Modules, user roles, reports and integrations are agreed on paper before a line of code is written."),
        ("Build and data migration", "We configure the portal, import your existing records and connect WhatsApp, email and payment tools."),
        ("Training and go-live", "Your team learns on real data, with us beside them. Then you switch over, confidently."),
        ("Support and evolution", "New branches, new reports, new automations: we keep the system growing alongside the business.")])}</div></section>'''

    faq = f'<section class="sec light" style="padding-top:90px"><div class="wrap">{head("FAQ", "Management system questions")}<div class="faqwrap">{faq_html(FAQ_MS)}</div></div></section>'
    faq = faq.replace('class="sec light"', 'class="sec"')
    body = hero + what + compare + modules + ind + proc + faq + related('what-is-a-management-system', 'excel-vs-custom-management-software') + cta_band()
    return page("management-systems.html", "Custom Management System Development | ToolsRhino",
                "Custom management software for mills, farms, clinics, gyms and restaurants: orders, inventory, payroll and reports in one portal with a built-in AI assistant.",
                body, label="Management Systems", schemas=[faq_schema(FAQ_MS), {"@context": "https://schema.org", "@type": "Service", "name": "Custom management system development", "provider": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "areaServed": "Worldwide"}])


# --------------------------------------------------------------------- AI AUTOMATION
FAQ_AI = [
    ("What kinds of tasks can AI automation handle?",
     "Anything repetitive and rule-driven: answering common questions, sending reminders, reading invoices, updating records, compiling reports and routing approvals. If a person does the same task more than a few times a week, it is a candidate."),
    ("Will AI replace my staff?",
     "Our aim is the opposite. We automate the repetitive work so your people can spend time on judgement, relationships and growth. Sensitive decisions always stay with a human."),
    ("Is my data safe with AI?",
     "Your information stays inside your own secure account, with role-based access and activity logs. We design automations so the AI only sees what it needs for the task."),
    ("Can the assistant speak Urdu as well as English?",
     "Yes. Our assistants and portals support English and Urdu, and can respond in the language the person writes in."),
    ("How quickly will we see results?",
     "Most clients notice a difference within the first few weeks, because we start with one or two high-impact workflows rather than trying to automate everything at once."),
    ("Do we need a management system first?",
     "Not necessarily. We can automate on top of your existing tools. That said, clean, structured data makes automation far more reliable, which is why the two work so well together."),
]

def ai():
    hero = page_hero("AI Automation", "AI automation that gives your team their hours back.",
        "Business process automation with intelligence built in: AI assistants, WhatsApp workflows, document processing and smart reporting that remove busywork and reduce costly errors.")
    what = f'''<section class="sec"><div class="wrap">{head("What we automate", "Six places AI quietly earns its keep.", "We pick automations by the hours they save and the mistakes they prevent, not by how impressive they sound in a presentation.")}
  <div class="grid g3">
    {card("bot", "AI business assistants", "A chat assistant trained on your own data that answers customer and staff questions around the clock, in English or Urdu.")}
    {card("chat", "WhatsApp and email automation", "Order confirmations, payment reminders, appointment nudges and follow-ups sent at the right moment, without anyone typing them.", delay=.05)}
    {card("file", "Document and invoice processing", "Invoices, receipts and forms are read, checked and posted to the right record, so nobody retypes numbers again.", delay=.1)}
    {card("workflow", "Workflow and approval automation", "Requests move to the right person, escalate when stuck and leave a clear trail, from purchase approvals to leave applications.", delay=.15)}
    {card("chart", "Smart reports and alerts", "Daily summaries, unusual-spend warnings and low-stock alerts delivered to your phone before small issues become big ones.", delay=.2)}
    {card("zap", "Lead capture and follow-up", "Enquiries from your website or WhatsApp are logged, qualified and followed up automatically until a human should step in.", delay=.25)}
  </div></div></section>'''

    func = f'''<section class="sec light"><div class="wrap">{head("By department", "Automation that fits every corner of the business.")}
  <div class="grid g4">
    {card("cart", "Sales", "Instant replies to enquiries, quotation drafts, pipeline reminders and lapsed-client nudges.")}
    {card("factory", "Operations", "Job tracking, stock alerts, dispatch updates and supplier follow-ups handled automatically.", delay=.05)}
    {card("wallet", "Finance", "Invoice capture, payment matching, overdue reminders and month-end summaries without the scramble.", delay=.1)}
    {card("users", "HR", "Attendance checks, leave requests, payroll preparation and onboarding checklists on autopilot.", delay=.15)}
  </div></div></section>'''

    resp = f'''<section class="sec"><div class="wrap"><div class="split top">
  <div class="reveal"><span class="eyebrow">Our approach</span><h2 class="h2">Responsible AI, kept practical.</h2>
    <p>Artificial intelligence is useful when it is predictable. We design every automation so that you can see what it did, why it did it and how to change it.</p>
    <p>We start small, prove the value on one workflow, then expand. That keeps risk low, results visible and your team comfortable with the change.</p></div>
  <div class="grid reveal" style="--d:.1s">
    {card("user" if False else "users", "A human stays in the loop", "Sensitive actions such as large payments or customer disputes are routed to a person for approval.")}
    {card("lock", "Your data stays yours", "Information lives in your own secure account, with permissions that mirror your organisation.")}
    {card("file", "Everything is traceable", "Activity logs show what the automation did and when, making audits and corrections simple.")}
  </div></div></div></section>'''

    proc = f'''<section class="sec light"><div class="wrap">{head("How we deliver", "From first workflow to a connected automation stack.")}{timeline([
        ("Process audit", "We map where time goes and rank tasks by effort saved and risk involved."),
        ("Pilot automation", "One high-impact workflow is built, tested with your team and measured against a clear target."),
        ("Integrate and expand", "Successful automations connect to WhatsApp, email, accounting and your management system."),
        ("Monitor and refine", "We review results, handle edge cases and extend automation to the next process in line.")])}</div></section>'''

    faq = f'<section class="sec"><div class="wrap">{head("FAQ", "AI automation questions")}{faq_html(FAQ_AI)}</div></section>'
    body = hero + what + func + resp + proc + faq + related("ai-automation-examples-for-small-business", "automate-whatsapp-payment-reminders") + cta_band("Ready to hand the repetitive work to AI?", "Book a short call. We'll point out the three automations most likely to pay for themselves first.")
    return page("ai-automation.html", "AI Automation Services for Business | ToolsRhino",
                "Business process automation with AI: chat assistants, WhatsApp workflows, invoice processing and smart reporting that save hours. English and Urdu.",
                body, label="AI Automation", schemas=[faq_schema(FAQ_AI), {"@context": "https://schema.org", "@type": "Service", "name": "AI automation services", "provider": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "areaServed": "Worldwide"}])


# --------------------------------------------------------------------- SAAS
FAQ_SAAS = [
    ("How long does it take to build a SaaS MVP?",
     "It depends on scope, but a focused MVP is usually a matter of weeks rather than months. We agree the smallest version that can earn real feedback, ship it, then iterate."),
    ("Who owns the code and the product?",
     "You do. Ownership and intellectual property terms are agreed in writing before work begins."),
    ("Can you help if I only have an idea?",
     "Yes. Our discovery phase turns a rough idea into a clear scope, user journeys and a prototype you can test with real people before committing to a full build."),
    ("Will the product handle many customers?",
     "We build on multi-tenant foundations with scale in mind, so adding customers means adding subscriptions, not rebuilding the product."),
    ("Do you support the product after launch?",
     "Yes. Many clients keep us on for releases, fixes and new features as their customer base grows."),
]

def saas():
    hero = page_hero("SaaS Product Creation", "SaaS product development, from first sketch to paying customers.",
        "We design and build subscription software for founders, agencies and established businesses: multi-tenant architecture, billing, onboarding and the admin tools you need to run it.")
    who = f'''<section class="sec"><div class="wrap">{head("Who it is for", "Built for people turning expertise into software.")}
  <div class="grid g3">
    {card("rocket", "Founders with a validated idea", "You know the problem and have spoken to customers. We turn that insight into a product people can sign up for.")}
    {card("building", "Businesses productising internal tools", "The system that runs your own operation might be valuable to others in your industry. We help package and launch it.", delay=.05)}
    {card("users", "Agencies and consultants", "Convert repeatable expertise into a recurring-revenue software product, without hiring an engineering team.", delay=.1)}
  </div></div></section>'''

    incl = [("layers", "Multi-tenant architecture", "Isolated workspaces for each customer on one maintainable codebase."),
            ("wallet", "Subscription billing", "Plans, trials, upgrades and invoices handled properly from day one."),
            ("users", "Onboarding and user management", "Sign-up, invitations, roles and permissions that feel effortless."),
            ("dash", "Admin console", "See every account, plan and event, and support customers without touching code."),
            ("chart", "Product analytics", "Understand activation, usage and churn so the roadmap follows evidence."),
            ("plug", "APIs and integrations", "Open your product to other tools through clean, documented endpoints."),
            ("shield", "Security and compliance basics", "Encryption, access control, backups and audit trails built in."),
            ("sparkle", "AI features", "Add assistants, smart search or automation that make your product stand apart.")]
    g = '<div class="grid g4">' + "".join(card(i, t, d, delay=(n % 4) * .05) for n, (i, t, d) in enumerate(incl)) + "</div>"
    inc = f'<section class="sec light"><div class="wrap">{head("What is included", "The full stack of a modern SaaS product.", "Every product we build starts with the unglamorous foundations that make growth safe.")}{g}</div></section>'

    proc = f'''<section class="sec"><div class="wrap">{head("The journey", "Five stages from concept to scale.")}{timeline([
        ("Discovery and scoping", "We define the problem, the user, the smallest valuable feature set and what success looks like."),
        ("Prototype and design", "Clickable designs let you and your first users react before engineering effort is spent."),
        ("MVP build", "Short development cycles, regular demos and a working product in your hands early."),
        ("Launch and learn", "We help you release, onboard the first customers and measure what they actually do."),
        ("Scale and extend", "Performance, new features, integrations and AI capabilities as demand grows.")])}</div></section>'''
    faq = f'<section class="sec light"><div class="wrap">{head("FAQ", "SaaS development questions")}{faq_html(FAQ_SAAS)}</div></section>'
    faq = faq.replace('class="sec light"', 'class="sec"')
    body = hero + who + inc + proc + faq + related("saas-mvp-development-guide", "what-is-a-management-system") + cta_band("Have a product idea worth building?", "Share the idea. We'll help you shape the smallest version worth launching.")
    return page("saas-development.html", "SaaS Product Development & MVP Services | ToolsRhino",
                "ToolsRhino builds SaaS products from idea to launch: multi-tenant architecture, subscription billing, admin tools and AI features for founders and businesses.",
                body, label="SaaS Product Creation", schemas=[faq_schema(FAQ_SAAS), {"@context": "https://schema.org", "@type": "Service", "name": "SaaS product development", "provider": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "areaServed": "Worldwide"}])
