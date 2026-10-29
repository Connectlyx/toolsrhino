"""Gym Command Center: product page, interface mock-ups (pure HTML/CSS/SVG) and featured sections."""
import urllib.parse
from lib import *

GCC_WA = WA + "?text=" + urllib.parse.quote("Hi, I'd like early access to Gym Command Center.")
GCC_FORM = "contact.html?topic=gym"


def smooth(pts):
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(1, len(pts)):
        x0, y0 = pts[i - 1]; x1, y1 = pts[i]; mx = (x0 + x1) / 2
        d += f" C{mx:.1f},{y0:.1f} {mx:.1f},{y1:.1f} {x1:.1f},{y1:.1f}"
    return d


def revenue_svg():
    vals = [3.1, 3.8, 3.4, 4.6, 4.2, 5.4, 5.0, 6.1, 5.7, 6.9, 6.5, 7.6]
    w, h = 320, 96
    pts = [(i * (w / (len(vals) - 1)), h - 8 - (v / 8.2) * (h - 16)) for i, v in enumerate(vals)]
    line = smooth(pts)
    area = line + f" L{w},{h} L0,{h} Z"
    grid = "".join(f'<line x1="0" x2="{w}" y1="{y}" y2="{y}" stroke="rgba(196,181,255,.10)" stroke-dasharray="3 5"/>' for y in (20, 48, 76))
    lx, ly = pts[-1]
    return (f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" class="gcc-chart" aria-hidden="true"><defs>'
            f'<linearGradient id="gA" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8B6CFF" stop-opacity=".45"/><stop offset="1" stop-color="#8B6CFF" stop-opacity="0"/></linearGradient>'
            f'<linearGradient id="gL" x1="0" x2="1"><stop offset="0" stop-color="#8B6CFF"/><stop offset="1" stop-color="#D9D0FF"/></linearGradient></defs>'
            f'{grid}<path d="{area}" fill="url(#gA)"/><path d="{line}" fill="none" stroke="url(#gL)" stroke-width="2.4" stroke-linecap="round"/>'
            f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4" fill="#fff" stroke="#8B6CFF" stroke-width="2.5"/></svg>')


def av(initials, i=0):
    hue = ["#8B6CFF", "#6C8BFF", "#B06CFF", "#6CB4FF", "#A28BFF"][i % 5]
    return f'<span class="av" style="background:linear-gradient(135deg,{hue},#2A2158)">{initials}</span>'


def dashboard_mock(compact=False, url="app.gymcommandcenter.com / dashboard"):
    nav_items = ["Command Center", "Members", "Memberships", "Invoices", "Payments", "Attendance", "Leads", "Trainers", "Reports", "Settings"]
    nav = "".join(f'<div class="{"on" if n == 0 else ""}">{t}</div>' for n, t in enumerate(nav_items))
    attn = [("amber", "18 memberships expire this week", "Review"),
            ("red", "14 invoices overdue · $3,210", "Remind"),
            ("violet", "23 members inactive for 14+ days", "Follow up"),
            ("blue", "6 leads waiting for a reply", "Open leads")]
    attn_html = "".join(f'<li><i class="dot {c}"></i><span>{t}</span><b>{b}</b></li>' for c, t, b in attn)
    kpis = [("Active members", "412", "▲ 27 new this month"), ("Revenue · this month", "$18,640", "▲ 9.4% vs last month"),
            ("Outstanding", "$3,210", "14 invoices"), ("Checked in today", "96", "Peak 6–8 pm")]
    k = "".join(f'<div class="gcc-kpi"><small>{a}</small><b>{b}</b><em>{c}</em></div>' for a, b, c in kpis)
    side = "" if compact else f'<aside class="gcc-side"><div class="gcc-brand"><i></i>Gym Command Center</div><nav class="gcc-nav">{nav}</nav></aside>'
    cls = " compact" if compact else ""
    return f'''<div class="mock gcc-frame{cls}"><div class="mock-in gcc">
  <div class="mock-bar"><i></i><i></i><i></i><span class="url">{url}</span></div>
  <div class="gcc-body">{side}
    <div class="gcc-main">
      <div class="gcc-top"><div><h4>Command Center</h4><small>Iron Works Fitness · Today</small></div><span class="gcc-chip">Sample data</span></div>
      <div class="gcc-kpis">{k}</div>
      <div class="gcc-row">
        <div class="gcc-card"><div class="gcc-card-h"><span>Revenue this month</span><small>Daily, $ thousands</small></div>{revenue_svg()}</div>
        <div class="gcc-card"><div class="gcc-card-h"><span>Attention required</span><small>4 items</small></div><ul class="attn">{attn_html}</ul></div>
      </div>
    </div></div></div></div>'''


def leads_mock():
    cols = [("New", [("Omar F.", "Instagram enquiry", "Today"), ("Lena P.", "Walk-in", "Today")]),
            ("Contacted", [("Marcus T.", "Asked about evening plans", "2d"), ("Hira Q.", "Wants a tour", "3d")]),
            ("Trial booked", [("Sana M.", "Thu · 6:30 pm", "Thu")]),
            ("Joined", [("Daniel O.", "Monthly Premium", "Mon")])]
    out = ""
    for t, cards in cols:
        cs = "".join(f'<div class="lead"><b>{n}</b><span>{d}</span><em>{w}</em></div>' for n, d, w in cards)
        out += f'<div class="kcol"><h5>{t} <small>{len(cards)}</small></h5>{cs}</div>'
    return f'''<div class="mock gcc-frame compact"><div class="mock-in gcc"><div class="mock-bar"><i></i><i></i><i></i><span class="url">app.gymcommandcenter.com / leads</span></div>
  <div class="gcc-main"><div class="gcc-top"><div><h4>Leads</h4><small>Follow up before they go cold</small></div><span class="gcc-chip">Sample data</span></div><div class="kanban">{out}</div></div></div></div>'''


def invoice_mock():
    return f'''<div class="mock gcc-frame compact"><div class="mock-in gcc"><div class="mock-bar"><i></i><i></i><i></i><span class="url">app.gymcommandcenter.com / invoices / 1042</span></div>
  <div class="gcc-main"><div class="gcc-top"><div><h4>Invoice #1042</h4><small>Monthly Premium · due 5 Nov</small></div><span class="status part">Partially paid</span></div>
   <div class="inv-who">{av("AK", 0)}<div><b>Ayesha K.</b><small>Member since March</small></div></div>
   <div class="inv-lines"><div><span>Monthly Premium</span><b>$60.00</b></div><div><span>Paid so far</span><b class="ok">− $30.00</b></div><div class="tot"><span>Balance due</span><b>$30.00</b></div></div>
   <div class="gcc-card"><div class="gcc-card-h"><span>Payment history</span></div><ul class="hist"><li><i class="dot violet"></i><span>Payment recorded by Reception</span><b>$30.00</b></li><li><i class="dot blue"></i><span>Invoice created</span><b>$60.00</b></li></ul></div>
  </div></div></div>'''


def stage(label, mock, note=""):
    return f'<figure class="shot reveal">{mock}<figcaption>{label}</figcaption></figure>'


def build_product():
    status = f'''<div class="callout status reveal"><strong>Where we are.</strong> Gym Command Center is in its final development and production-readiness phase. The core modules are built. We are now completing organisation onboarding, staff access, security checks and production verification. Early access will open to a small group of independent gyms first. There is no public launch date yet, and we will not announce one until it is verified.</div>'''
    hero = f'''<section class="page-hero" style="padding-bottom:40px">
  <canvas class="ink" aria-hidden="true"></canvas>
  <div class="wrap" style="max-width:1100px">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">Gym Command Center</span></nav>
    <span class="badge-new">Early access soon</span>
    <h1 class="h1">Gym Command Center. <span class="grad">Your gym. One command center.</span></h1>
    <p class="lead">A centralized gym management platform that brings members, memberships, billing, payments, attendance, leads and reporting into one dashboard, so you can see what needs attention before it costs you money.</p>
    <div class="cta-row"><a class="btn btn-primary" href="{GCC_FORM}">Join the early-access list {ARROW}</a><a class="btn btn-ghost" href="{GCC_WA}" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
  </div></section>'''

    showcase = f'''<section class="sec-tight" style="padding-top:0;margin-top:-10px"><div class="wrap"><div class="mock-stage reveal">{dashboard_mock()}</div>
  <p class="center" style="font-size:12.5px;color:var(--dim);margin-top:22px">Interface preview with sample data. The design is still being refined before launch.</p></div></section>'''

    problem = f'''<section class="sec"><div class="wrap"><div class="split top">
  <div class="reveal"><span class="eyebrow">The problem</span><h2 class="h2">Running a gym should not mean running a filing cabinet.</h2>
    <p>Most independent gyms start the same way: a register at the front desk, a spreadsheet for payments, a WhatsApp group for everything else. It works, until the member list passes a few hundred and nobody can say with confidence who has paid, who is about to lapse and who has quietly stopped coming.</p>
    <p>Gym Command Center is built for the owner who wants those answers in one place, and wants the team to be able to act on them without hunting through five tools.</p></div>
  <div class="card reveal" style="--d:.1s;padding:36px"><h3 class="h3" style="margin-bottom:18px">Questions it is designed to answer at a glance</h3>
    {ticks(["How much revenue have we recorded this month?", "Which invoices are overdue, and for how much?", "Which memberships expire this week?", "Who has not visited in two weeks?", "Which leads still need a reply?"])}</div>
</div></div></section>'''

    flow_steps = ["Attract leads", "Register members", "Manage memberships", "Collect payments", "Track attendance", "Follow up", "Analyse performance"]
    flow = f'''<section class="sec light"><div class="wrap">{head("One connected workflow", "From first enquiry to monthly report, in one system.", "Every step feeds the next, so staff move from one task to another without re-typing or switching tools.")}
  <ol class="flow reveal">{"".join(f"<li><span>{n+1}</span>{t}</li>" for n, t in enumerate(flow_steps))}</ol></div></section>'''

    mods = [("dash", "Command Center dashboard", "Active members, monthly revenue, outstanding balances, attendance, new members and expiring memberships at a glance."),
            ("users", "Members and profiles", "Member records with contact details and membership information, kept in one place."),
            ("layers", "Plans and memberships", "Create plans, then assign, renew, replace or cancel memberships."),
            ("file", "Invoices", "Create invoices, track status and download invoice PDFs."),
            ("wallet", "Payments", "Record payments against invoices and watch balances update."),
            ("chat", "Payment reminders", "Two configurable reminder dates, with logic that skips invoices that no longer qualify. Delivered by email at launch."),
            ("zap", "Attendance", "Record check-ins and review attendance history."),
            ("target", "Lead management", "Organise prospects in a Kanban-style board and follow up before they go cold."),
            ("hardhat", "Trainers and staff roles", "Trainer records, plus role-based access for owners, managers, receptionists, trainers and accountants."),
            ("chart", "Reports and exports", "Date-range reports on revenue, attendance, overdue payments and leads, with CSV export."),
            ("clock", "Notifications", "In-app notifications for payment events and other items that need a decision."),
            ("cog", "Currency and timezone", "Each gym sets its own currency and timezone, so the system fits its market.")]
    mgrid = '<div class="grid g4">' + "".join(card(i, t, d, delay=(n % 4) * .05) for n, (i, t, d) in enumerate(mods)) + "</div>"
    modules = f'<section class="sec"><div class="wrap">{head("What you can manage", "Everything a gym owner and their team touch every day.")}{mgrid}</div></section>'

    attention = f'''<section class="sec light"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">Attention required</span><h2 class="h2">A dashboard that tells you what to do next.</h2>
    <p>Most systems store information and wait for you to go looking. Gym Command Center brings expiring memberships, overdue payments, inactive members and leads that need a reply into a single list, so the first thing you see each morning is what matters most.</p>
    <p>It is the difference between a database and a command center.</p></div>
  <div class="reveal" style="--d:.1s">{invoice_mock()}</div>
</div></div></section>'''

    leads = f'''<section class="sec"><div class="wrap"><div class="split">
  <div class="reveal order-2">{leads_mock()}</div>
  <div class="reveal" style="--d:.1s"><span class="eyebrow">Leads to members</span><h2 class="h2">Do not let enquiries go cold.</h2>
    <p>Every enquiry, from Instagram messages to walk-ins, has a place on the board. Move it from first contact to trial to joined, and see which leads are waiting on your reply. When someone joins, their record is already there, ready to become a member.</p>
    {ticks(["Kanban-style lead board", "Lead and member records in the same system", "Reports on lead activity"])}</div>
</div></div></section>'''

    billing = f'''<section class="sec light"><div class="wrap">{head("Billing, without the arguments", "Invoices and payments that stay in sync.")}{timeline([
        ("Register the member", "Add the member and their contact details once."),
        ("Assign a plan", "Choose a membership plan and the dates that apply."),
        ("Create the invoice", "An invoice is generated for the plan, with a PDF you can share."),
        ("Record payments", "Staff record each payment against the invoice, including part-payments."),
        ("Watch the balance", "Invoice status and outstanding balances update as payments come in, and reminders go to eligible unpaid invoices.")])}</div></section>'''

    roles = [("Owner", "Overall control of the business."), ("Manager", "Day-to-day operations."), ("Receptionist", "Registration, attendance and front-desk tasks."),
             ("Trainer", "Trainer information and assigned tasks."), ("Accountant", "Billing, payments and financial records.")]
    roles_html = '<div class="grid g3 roles">' + "".join(
        f'<div class="card reveal" style="--d:{n*.05}s"><h3 class="h3">{r}</h3><p>{d}</p></div>' for n, (r, d) in enumerate(roles)) + "</div>"
    people = f'<section class="sec"><div class="wrap">{head("Built for owners and their teams", "The right access for every person on your team.", "Gym Command Center is business software for the people who run the gym, not a fitness app for members. Each role sees what their job needs.")}{roles_html}</div></section>'

    diffs = f'''<section class="sec light"><div class="wrap">{head("What makes it different", "Designed around how a gym is actually run.")}
  <div class="grid g3">
    {card("target", "A command center, not a database", "Records are only useful if they prompt action. The dashboard puts what needs attention first.")}
    {card("link", "One connected workflow", "Leads, members, memberships, invoices, payments and attendance share the same record, so nothing is typed twice.", delay=.05)}
    {card("lock", "Separate space for every gym", "Built as a multi-tenant platform, so each gym has its own organisation, staff access, settings and data.", delay=.1)}
    {card("globe", "Fits your market", "Set your own currency and timezone. Designed for gyms in Pakistan, the United States and beyond.", delay=.15)}
    {card("sparkle", "A premium, modern interface", "Fast navigation, clear tables and actionable alerts, in an interface that feels like professional business software.", delay=.2)}
    {card("zap", "A foundation for automation", "Reminders, notifications and alerts are built in, with more automation to come as the core proves itself.", delay=.25)}
  </div></div></section>'''

    road_items = [("done", "Built", "Core modules", "Members, memberships, invoices, payments, attendance, leads, trainers, reports and settings."),
                  ("now", "In progress", "Onboarding and staff access", "Owner sign-up, organisation setup, staff roles and invitations."),
                  ("now", "In progress", "Security and workflow verification", "Checking data separation between gyms, permissions, and billing and membership flows end to end."),
                  ("next", "Up next", "Production readiness", "Production configuration, email delivery and scheduled reminders."),
                  ("next", "Up next", "Early access", "A small group of independent gyms go first, and their feedback shapes the next release.")]
    road = '<ol class="road">' + "".join(f'<li class="{c}"><span class="rs">{s}</span><h3>{t}</h3><p>{d}</p></li>' for c, s, t, d in road_items) + "</ol>"
    roadmap = f'<section class="sec"><div class="wrap">{head("Honest status", "Where Gym Command Center stands today.", "We would rather be exact than exciting. Here is what is built, what we are finishing and what comes next.")}{road}{status}</div></section>'

    planned = [("chat", "WhatsApp reminders and follow-ups", "Payment and expiry reminders, plus lead follow-up, over the official WhatsApp Business Platform."),
               ("wallet", "Payment links, QR codes and gateways", "Online payment options, chosen by country, provider eligibility and customer demand."),
               ("bot", "AI business assistant", "Ask “which invoices are overdue?” in plain language and get answers from your own data."),
               ("chart", "Retention insights", "Spot declining attendance and members who may need a nudge."),
               ("building", "Multi-branch management", "Locations under one organisation with branch-level access and consolidated reporting."),
               ("plug", "Device integrations", "Biometric and door-access devices, once we know which ones early-access gyms use.")]
    pl = '<div class="grid g3">' + "".join(card(i, t, d, '<span class="pill custom">Planned, not yet available</span>', delay=(n % 3) * .05) for n, (i, t, d) in enumerate(planned)) + "</div>"
    planned_sec = f'<section class="sec light"><div class="wrap">{head("On the roadmap", "What we plan to add once the core is proven.", "These are directions, not promises of a date. We will describe each as available only when it has been built and tested.")}{pl}</div></section>'

    faqs = [
     ("Is Gym Command Center available now?", "Not yet. The core modules are built, and we are completing onboarding, staff access, security checks and production verification. Early access will open to a small group of independent gyms first. Join the list and we will tell you as soon as a date is confirmed."),
     ("How much will it cost?", "Pricing will be announced when early access opens. The model is a one-time setup fee plus a recurring subscription, and early-access gyms will hear the details first."),
     ("Does it send WhatsApp reminders?", "Not at launch. The first release focuses on configurable email payment reminders and in-dashboard alerts. WhatsApp reminders and follow-ups are planned once the core workflows are stable."),
     ("Can members pay online through the system?", "Staff record payments against invoices in the system. Online payment links, QR codes and gateway processing are planned, and we will choose providers based on country and customer demand."),
     ("Is it AI-powered?", "Not yet, and we would rather say so plainly. Today it is a gym management system with automation-oriented features such as reminders and alerts. An AI business assistant and retention insights are on the roadmap, and we will describe them as available only when they are."),
     ("Can I manage several branches?", "The platform is built around organisations that can have locations, but full multi-branch management is on the roadmap. Early access is aimed at single-location gyms."),
     ("Will it work in my country and currency?", "Each gym sets its own currency and timezone. We start with one currency per gym. Multi-currency accounting is not part of the first release."),
     ("Is my gym's data kept separate from other gyms?", "Gym Command Center is designed so that every gym is its own organisation with its own staff, settings and records, protected by role-based access. Verifying that separation end to end is part of our launch checklist, which is why we are not rushing the release."),
     ("Does it connect to biometric or door-access devices?", "Not currently. We will consider device integrations once we know which devices early-access gyms actually use."),
     ("Who is it for?", "Independent gyms and small fitness businesses with recurring memberships. It is built for owners and their teams, not as a member-facing fitness app or a personal-trainer tool."),
    ]
    faq = f'<section class="sec"><div class="wrap">{head("FAQ", "Gym Command Center questions")}{faq_html(faqs)}</div></section>'

    final = f'''<section class="sec" style="padding-top:40px"><div class="wrap"><div class="cta reveal"><canvas class="ink" aria-hidden="true"></canvas>
  <h2 class="h2">Be one of our first gyms.</h2><p class="lead">Early-access gyms get hands-on setup from the team building the product, and a real say in what we build next. Tell us about your gym and we will be in touch.</p>
  <div class="cta-row"><a class="btn btn-primary" href="{GCC_FORM}">Join the early-access list {ARROW}</a><a class="btn btn-ghost" href="{GCC_WA}" target="_blank" rel="noopener">Ask on WhatsApp</a></div></div></div></section>'''

    related = ""
    from seo_pages import post_card, ART
    related = f'<section class="sec light" style="padding-block:80px"><div class="wrap">{head("Related reading", "Useful before you choose gym software.")}<div class="grid g2" style="max-width:860px;margin-inline:auto">{post_card(ART["how-to-choose-gym-management-software"])}{post_card(ART["gym-membership-management-guide"], .06)}</div></div></section>'

    body = hero + showcase + problem + flow + modules + attention + leads + billing + people + diffs + roadmap + planned_sec + faq + related + final
    desc = "Gym Command Center is a centralized gym management platform for members, billing, payments, attendance, leads and reports. Early access soon."
    schemas = [faq_schema(faqs), {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Gym Command Center",
               "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "description": desc,
               "publisher": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "url": SITE + "/gym-command-center"}]
    return page("gym-command-center.html", "Gym Command Center | Gym Management Software | ToolsRhino", desc, body, label="Gym Command Center", schemas=schemas)


def featured_home():
    return f'''<section class="sec" style="padding-top:20px"><div class="wrap"><div class="feature-band">
  <div class="reveal"><span class="badge-new">New product · Early access soon</span><h2 class="h2" style="margin:16px 0 18px">Gym Command Center. <span class="grad">Your gym. One command center.</span></h2>
    <p class="lead" style="margin-bottom:22px">Our gym management platform brings members, memberships, billing, payments, attendance, leads and reports into one dashboard, so owners see what needs attention first.</p>
    {ticks(["Members, plans, invoices and payments in one place", "An attention list for expiring memberships and overdue payments", "Role-based access for your whole team"])}
    <div class="cta-row" style="justify-content:flex-start"><a class="btn btn-primary" href="gym-command-center.html">Explore Gym Command Center {ARROW}</a><a class="btn btn-ghost" href="{GCC_FORM}">Join early access</a></div>
    <p style="font-size:13px;color:var(--dim);margin-top:18px">In final development. Early access opens to a small group of gyms first.</p></div>
  <div class="reveal" style="--d:.1s">{dashboard_mock(compact=True)}</div>
</div></div></section>'''


def saas_example():
    return f'''<section class="sec light"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">What we build ourselves</span><h2 class="h2">We are building a SaaS product of our own.</h2>
    <p>Gym Command Center is a multi-tenant, subscription-based platform that we are taking from concept through launch right now. The same decisions we make for it, from data separation between customers to roles, billing and onboarding, are the ones we bring to your product.</p>
    <p style="margin-top:26px"><a class="link-arrow" href="gym-command-center.html">See Gym Command Center {ARROW}</a></p></div>
  <div class="reveal" style="--d:.1s">{leads_mock()}</div></div></div></section>'''
