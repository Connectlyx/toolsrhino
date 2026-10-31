"""Gym Command Center: product page and illustrative mock-up screens."""
from lib import *

STATUS = "Final development and production-readiness phase. Early access is planned once onboarding, security and core workflows are verified."
CMD_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 8 4 4-4 4M12 17h7"/></svg>'

NAV_ITEMS = [("dash", "Command Center"), ("users", "Members"), ("layers", "Memberships"), ("file", "Invoices"), ("wallet", "Payments"),
             ("zap", "Attendance"), ("target", "Leads"), ("dumbbell", "Trainers"), ("chart", "Reports"), ("cog", "Settings")]


def _sidebar(active):
    items = "".join(
        f'<div class="g-nav{" on" if n == active else ""}">{icon(i)}{n}' + ('<em>9</em>' if n == "Invoices" else '') + '</div>' for i, n in NAV_ITEMS)
    return f'''<aside class="g-side"><div class="g-brand"><i>{CMD_ICON}</i><div>Gym Command<br>Center<span>Management</span></div></div>{items}
<div class="org"><b>Northside Fitness</b>Owner · Main branch</div></aside>'''


def _frame(active, title, sub, body, btn="+ New member"):
    return f'''<div class="g-frame"><div class="g-app">{_sidebar(active)}
<div class="g-main"><div class="g-top"><div><h4>{title}</h4><small>{sub}</small></div>
<div class="g-tools"><div class="g-search">Search members, invoices…</div><div class="g-btn">{btn}</div><div class="g-avatar">NF</div></div></div>{body}</div></div></div>'''


def _spark(pts, color="#B9AEFF"):
    xs = [i * (64 / (len(pts) - 1)) for i in range(len(pts))]
    path = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f} {26 - p * 24:.1f}" for i, (x, p) in enumerate(zip(xs, pts)))
    return f'<svg class="spark" viewBox="0 0 64 26" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>'


def dashboard():
    bars = [("May", 52), ("Jun", 58), ("Jul", 55), ("Aug", 66), ("Sep", 72), ("Oct", 88)]
    b = "".join(f'<div class="{"cur" if m == "Oct" else ""}"><i style="height:{h}%;animation-delay:{n*.08:.2f}s"></i>{m}</div>' for n, (m, h) in enumerate(bars))
    att = [10, 18, 44, 60, 38, 22, 20, 30, 52, 86, 100, 74, 40, 16]
    a = "".join(f'<i class="{"hi" if v > 80 else ""}" style="height:{v}%"></i>' for v in att)
    body = f'''<div class="g-kpis">
  <div class="g-kpi"><small>Active members</small><b>412</b><em>▲ 18 this month</em>{_spark([.3,.4,.38,.55,.6,.8])}</div>
  <div class="g-kpi"><small>Revenue this month</small><b>$18,640</b><em>▲ 9% vs September</em>{_spark([.2,.35,.3,.5,.62,.85])}</div>
  <div class="g-kpi"><small>Outstanding</small><b>$3,215</b><em class="w">9 invoices overdue</em>{_spark([.7,.6,.65,.5,.55,.4], "#FFB85C")}</div>
  <div class="g-kpi"><small>Check-ins today</small><b>138</b><em>Peak 6–8 pm</em>{_spark([.2,.4,.3,.6,.5,.9], "#6FB4F5")}</div></div>
<div class="g-row">
  <div class="g-card"><h5>Revenue <span>Last 6 months</span></h5><div class="g-bars">{b}</div></div>
  <div class="g-card"><h5>Attention required <span>Needs action</span></h5>
    <div class="g-alert"><span class="d a"></span><div>Memberships expiring<span>Within the next 7 days</span></div><b>17</b></div>
    <div class="g-alert"><span class="d r"></span><div>Overdue invoices<span>$2,140 outstanding</span></div><b>9</b></div>
    <div class="g-alert"><span class="d v"></span><div>Inactive members<span>No visit in 14+ days</span></div><b>26</b></div>
    <div class="g-alert"><span class="d b"></span><div>Leads to follow up<span>Waiting for a reply</span></div><b>11</b></div></div></div>
<div class="g-card"><h5>Today’s attendance <span>By hour</span></h5><div class="g-att">{a}</div></div>'''
    return _frame("Command Center", "Command Center", "Thursday overview · Northside Fitness", body)


def members():
    rows = [("AK", "Ayesha Khan", "M-1042", "Premium · Monthly", "ok", "Active", "Nov 24", "$0"),
            ("DR", "Daniel Reyes", "M-1043", "Standard · Quarterly", "wn", "Expiring", "Nov 02", "$0"),
            ("SM", "Sara Malik", "M-1044", "Premium · Annual", "ok", "Active", "Aug 25", "$0"),
            ("TH", "Tom Harris", "M-1046", "Standard · Monthly", "bd", "Overdue", "Oct 30", "$45"),
            ("BZ", "Bilal Zafar", "M-1047", "Student · Monthly", "ok", "Active", "Nov 18", "$0"),
            ("LP", "Lina Park", "M-1049", "Premium · Monthly", "wn", "Expiring", "Nov 03", "$0"),
            ("OA", "Omar Aziz", "M-1051", "Standard · Monthly", "bd", "Overdue", "Oct 27", "$90")]
    r = "".join(f'<tr><td><div class="who"><div class="g-avatar">{i}</div><div><b>{n}</b><small>{m}</small></div></div></td><td>{p}</td><td><span class="g-st {c}">{s}</span></td><td class="hide-m">{e}</td><td class="hide-m">{bal}</td></tr>'
                for i, n, m, p, c, s, e, bal in rows)
    body = f'''<div class="g-chips"><span class="on">All members · 412</span><span>Active</span><span>Expiring soon · 17</span><span>Overdue · 9</span><span>Inactive · 26</span></div>
<div class="g-card" style="padding:14px 6px 6px"><table class="g-tbl"><thead><tr><th>Member</th><th>Plan</th><th>Status</th><th class="hide-m">Expires</th><th class="hide-m">Balance</th></tr></thead><tbody>{r}</tbody></table></div>'''
    return _frame("Members", "Members", "Profiles, memberships and balances in one list", body)


def billing():
    body = '''<div class="g-inv">
  <div class="g-card"><h5>Invoice INV-2041 <span class="g-st wn" style="font-size:11px">Partially paid</span></h5>
    <div class="g-line"><span>Member</span>Tom Harris · M-1046</div>
    <div class="g-line"><span>Standard plan · Monthly</span>$45.00</div>
    <div class="g-line"><span>Registration</span>$20.00</div>
    <div class="g-line"><span>Personal training pack</span>$30.00</div>
    <div class="g-line tot"><span style="color:#fff">Total</span>$95.00</div></div>
  <div class="g-card"><h5>Balance <span>Due Oct 30</span></h5>
    <div style="font-family:var(--font-display);font-size:30px;color:#fff;letter-spacing:-.03em;line-height:1">$35.00</div>
    <div class="g-prog"><i></i></div><div style="font-size:11.5px;color:var(--g-dim)">$60.00 of $95.00 received</div>
    <div class="g-btn" style="margin-top:14px;text-align:center">Record payment</div>
    <div class="g-tl" style="margin-top:18px">
      <div><i></i><div>Payment recorded<span>Cash · received by Reception</span></div><div>$40</div></div>
      <div><i></i><div>Payment recorded<span>Bank transfer · Oct 18</span></div><div>$20</div></div>
      <div><i class="o"></i><div>Reminder 1 scheduled<span>Email · 3 days before due date</span></div><div>Oct 27</div></div>
      <div><i class="o"></i><div>Reminder 2 scheduled<span>Email · on the due date</span></div><div>Oct 30</div></div></div></div></div>'''
    return _frame("Invoices", "Invoices & payments", "Balances update the moment a payment is recorded", body, "+ New invoice")


def leads():
    def L(n, s, note, tag):
        return f'<div class="g-lead"><b>{n}</b><span>{s}</span><span>{note}</span><em>{tag}</em></div>'
    body = f'''<div class="g-kan">
  <div class="g-col"><h6>New <span>3</span></h6>{L("Hamza Rauf","Instagram","Asked about evening plans","Call today")}{L("Chloe Bennett","Walk-in","Wants a tour on Saturday","Book tour")}{L("Imran Sheikh","Referral · Omar A.","Interested in a couples plan","Call today")}</div>
  <div class="g-col"><h6>Contacted <span>2</span></h6>{L("Nadia Hussain","Website form","Comparing two gyms nearby","Follow up Fri")}{L("Mark Ellison","Walk-in","Sent plan details","Follow up Mon")}</div>
  <div class="g-col"><h6>Trial booked <span>2</span></h6>{L("Zoya Ahmed","Instagram","Trial session Sat, 7 am","Trial Sat")}{L("Ryan Cole","Referral","Trial pass, 3 days","Trial Tue")}</div>
  <div class="g-col"><h6>Joined <span>1</span></h6>{L("Maria Lopez","Walk-in","Premium · Monthly","Member M-1052")}</div></div>
<div class="g-chips"><span class="on">This month · 8 new leads</span><span>Walk-in</span><span>Instagram</span><span>Referral</span><span>Website</span></div>'''
    return _frame("Leads", "Leads", "Every enquiry tracked until they join or decline", body, "+ New lead")


def tour():
    tabs = [("Dashboard", dashboard()), ("Members", members()), ("Billing", billing()), ("Leads", leads())]
    t = "".join(f'<button class="tab v" role="tab" id="gt{i}" aria-controls="gp{i}">{n}</button>' for i, (n, _) in enumerate(tabs))
    p = "".join(f'<div class="panel shot" role="tabpanel" id="gp{i}" aria-labelledby="gt{i}">{h}</div>' for i, (_, h) in enumerate(tabs))
    return f'<div data-tabs class="reveal"><div class="tabs" role="tablist" aria-label="Product tour">{t}</div>{p}</div><p class="g-note">Illustrative preview with sample data. The final interface may differ.</p>'


FAQ = [
 ("Is Gym Command Center available now?",
  "Not yet. It is in its final development and production-readiness phase. We plan to open early access once onboarding, security and the core workflows have been verified. Join the early-access list and we will contact you directly."),
 ("Who is it designed for?",
  "Independent gyms and small fitness businesses with one location, recurring memberships and regular payment collection. Fitness studios are a natural fit too. Multi-branch support is on our roadmap."),
 ("Can it send WhatsApp reminders?",
  "WhatsApp messaging is planned, but it is not part of the first release. At launch, payment reminders are designed to go out by email, with in-app alerts and the Attention Required view keeping staff informed."),
 ("Does it take online payments?",
  "Staff record payments against invoices inside the system. Online payment links, QR payments and gateway processing are on the roadmap and will be added based on customer demand and the markets we serve."),
 ("Is each gym’s data kept separate?",
  "Yes, that is how the product is designed. It uses a multi-tenant architecture in which each gym has its own organisation, staff access and settings. Ahead of launch we are verifying data isolation and permissions with dedicated security testing."),
 ("Which currencies and countries does it support?",
  "Each gym is configured with its own currency and timezone, so the product can be set up for markets such as Pakistan and the United States. Each client deployment uses a single configured currency."),
 ("Can it connect to biometric devices or door access?",
  "Not at the moment. If you rely on a specific device, tell us the model and we will consider it when planning integrations."),
 ("What will it cost?",
  "Pricing will be announced at launch. Early-access gyms will hear it from us first."),
]


def page_html():
    hero = f'''<section class="page-hero">
  <canvas class="ink" aria-hidden="true"></canvas>
  <div class="wrap" style="max-width:1100px">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="services.html">Services</a><span>/</span><span aria-current="page">Gym Command Center</span></nav>
    <span class="badge-early" style="margin-bottom:22px">Early access planned</span>
    <h1 class="h1"><span class="gcc-word">Gym Command Center:</span> gym management software for owners who want control.</h1>
    <p class="lead" style="max-width:70ch">Members, memberships, invoices, payments, attendance and leads in one dashboard that shows what needs your attention first. <strong style="color:#fff">Your Gym. One Command Center.</strong></p>
    <div class="cta-row"><a class="btn btn-primary" href="contact.html?interest=gym-command-center">Join the early-access list {ARROW}</a>
      <a class="btn btn-ghost" href="{WA_DEMO}" target="_blank" rel="noopener">Book a demo</a></div>
    <p style="margin-top:22px;font-size:14px;color:var(--dim);max-width:70ch"><strong style="color:var(--ice)">Status:</strong> {STATUS}</p>
  </div></section>'''

    tour_sec = f'''<section class="sec"><div class="wrap" style="max-width:1160px">
  {head("Product tour", "See how the command center is organised.", "A closer look at the screens your team will use every day.")}
  {tour()}</div></section>'''

    loop = f'''<section class="sec light"><div class="wrap">{head("One connected workflow", "From first enquiry to a clear monthly picture.", "Most gym software stores records. Gym Command Center connects the steps between them, so staff move from one task to the next without a separate system for each.")}
  <div class="loop reveal">
    <div class="st">Attract leads<small>Track every enquiry</small></div><div class="st">Register members<small>Profiles and contacts</small></div>
    <div class="st">Manage memberships<small>Assign, renew, cancel</small></div><div class="st">Collect payments<small>Invoices and balances</small></div>
    <div class="st">Track attendance<small>Check-ins and history</small></div><div class="st">Follow up<small>Reminders and alerts</small></div>
    <div class="st">Analyse<small>Reports and exports</small></div></div></div></section>'''

    mods = [("dash", "Command Center dashboard", "Active members, monthly revenue, outstanding balances, attendance, new joiners and expiring memberships at a glance."),
            ("users", "Members and memberships", "Member records, plans, renewals, replacements and cancellations managed in one place."),
            ("file", "Invoices and PDFs", "Create invoices, follow their status and generate PDF copies for members."),
            ("wallet", "Payment tracking", "Record payments against invoices and see balances update immediately."),
            ("chat", "Payment reminders", "Two configurable reminder dates per invoice, skipped automatically once an invoice is no longer eligible."),
            ("zap", "Attendance", "Record check-ins and review attendance history by member and by day."),
            ("target", "Lead management", "A Kanban-style pipeline that keeps every enquiry moving until they join or decline."),
            ("dumbbell", "Trainer records", "Keep trainer details and related information alongside the rest of your operation."),
            ("chart", "Reports and CSV export", "Date-range reports for revenue, attendance, overdue payments and leads."),
            ("sparkle", "Notifications", "In-app alerts for payment events and items that need attention."),
            ("lock", "Staff roles and access", "Owner, manager, receptionist, trainer and accountant roles, designed for the right people to see the right information."),
            ("globe", "Currency and timezone", "Configure each gym’s currency and timezone for the market it operates in.")]
    mg = '<div class="grid g3">' + "".join(card(i, t, d, delay=(n % 3) * .05) for n, (i, t, d) in enumerate(mods)) + "</div>"
    modules = f'<section class="sec"><div class="wrap">{head("What is inside", "Twelve capabilities, one dashboard.", "Everything a gym owner and the front-desk team need to run the business day to day.")}{mg}</div></section>'

    attn = f'''<section class="sec light"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">Attention required</span><h2 class="h2">Know what needs doing before you go looking for it.</h2>
    <p>Expiring memberships, overdue invoices, members who have stopped visiting and leads waiting for a reply usually live in four different places. Gym Command Center brings them into a single view, so the first five minutes of the day are spent acting, not searching.</p>
    <p>The goal is simple: fewer forgotten renewals, fewer unpaid balances and fewer enquiries that quietly go cold.</p></div>
  <div class="reveal" style="--d:.1s">{ticks(["Memberships expiring in the next seven days", "Overdue invoices and the amount outstanding", "Inactive members who have stopped visiting", "Leads that need a follow-up", "Payment events and in-app notifications"])}</div>
</div></div></section>'''

    roles = [("Owner", "Overall control of the business, settings and reports."), ("Manager", "Day-to-day operations and team oversight."),
             ("Receptionist", "Registration, check-ins and front-desk tasks."), ("Trainer", "Relevant trainer and assigned member information."),
             ("Accountant", "Invoices, payments and financial records.")]
    rl = '<div class="grid g4" style="grid-template-columns:repeat(5,1fr)">' + "".join(
        f'<div class="card reveal" style="padding:24px;--d:{n*.05}s"><h3 class="h3" style="font-size:1.1rem">{r}</h3><p style="font-size:14.5px;margin-top:8px">{d}</p></div>' for n, (r, d) in enumerate(roles)) + "</div>"
    roles_sec = f'<section class="sec"><div class="wrap">{head("Built for teams", "The right access for every role.", "Gym Command Center is designed around five staff roles, so your team sees what it needs to do its job.")}{rl}</div></section>'

    billing = f'''<section class="sec light"><div class="wrap">{head("Billing, simplified", "From registration to a settled invoice.")}{timeline([
        ("Register the member", "Create the profile and capture contact and membership details."),
        ("Assign a membership plan", "Choose the plan, and the system records the relevant billing information."),
        ("Create the invoice", "Generate the invoice and a PDF copy for the member."),
        ("Record payments", "Log each payment against the invoice, in part or in full."),
        ("Watch the balance", "Status and outstanding balance update automatically."),
        ("Remind, only when needed", "Configured reminders go out for eligible unpaid invoices and stop once they are settled.")])}</div></section>'''

    diff = f'''<section class="sec"><div class="wrap">{head("Why owners will like it", "A command center, not just a member database.")}
  <div class="grid g2">
    {card("dash", "Visibility over record-keeping", "Instead of storing information and leaving you to dig, it surfaces what needs attention across payments, memberships and leads.")}
    {card("link", "Connected modules", "Leads, members, invoices, payments and attendance share one record, so nobody re-types the same detail twice.", delay=.05)}
    {card("users", "Made for owners and managers", "It is a business tool for the people running the gym, not a consumer fitness app.", delay=.1)}
    {card("shield", "Separate, secure workspaces", "Each gym gets its own organisation, staff access and settings, designed so one gym’s information stays separate from another’s.", delay=.15)}
  </div></div></section>'''

    who = f'''<section class="sec light"><div class="wrap">{head("Who it is for", "Start with the gyms that need it most.")}
  <div class="grid g3">
    {card("dumbbell", "Independent gyms", "Single-location gyms with recurring memberships who want clean records, clear payments and fewer forgotten renewals. This is our focus for early access.")}
    {card("target", "Fitness studios", "Boutique and specialist studios with recurring memberships. We are validating the workflows with studios after the first launch.", delay=.05)}
    {card("building", "Multi-branch businesses", "Branch management is on the roadmap. We will open it up once branch-level access and reporting are fully tested.", delay=.1)}
  </div></div></section>'''

    now = ["Members, memberships and plans", "Invoices, PDFs and payment tracking", "Email payment reminders (two configurable dates)", "Attendance and lead pipeline", "Dashboard, reports and CSV export", "Staff roles and in-app notifications", "Currency and timezone settings"]
    nxt = ["WhatsApp reminders and follow-ups", "Online payment links, QR and gateway processing", "Improved payment-proof review workflow", "Membership-expiry and inactive-member campaigns", "AI business assistant and retention insights", "Branch management for multi-location gyms", "Device and door-access integrations on request"]
    road = f'''<section class="sec"><div class="wrap">{head("Honest roadmap", "What we are launching with, and what comes next.", "We would rather under-promise than oversell. Items on the right are planned, not yet available.")}
  <div class="rm">
    <div class="card reveal"><h3 class="h3">Planned for early access</h3><ul>{"".join(f"<li>{x}</li>" for x in now)}</ul></div>
    <div class="card reveal soon" style="--d:.08s"><h3 class="h3">Planned next</h3><ul>{"".join(f"<li>{x}</li>" for x in nxt)}</ul></div></div></div></section>'''

    faq = f'<section class="sec light"><div class="wrap">{head("FAQ", "Gym Command Center questions")}{faq_html(FAQ)}</div></section>'

    cta = f'''<section class="sec" style="padding-top:40px"><div class="wrap"><div class="cta reveal"><canvas class="ink" aria-hidden="true"></canvas>
  <span class="badge-early" style="margin-bottom:20px">Early access planned</span>
  <h2 class="h2">Be among the first gyms to run on Gym Command Center.</h2>
  <p class="lead">Join the early-access list for hands-on onboarding, a say in what we build next and first notice of launch pricing.</p>
  <div class="cta-row"><a class="btn btn-primary" href="contact.html?interest=gym-command-center">Join the early-access list {ARROW}</a><a class="btn btn-ghost" href="{WA_DEMO}" target="_blank" rel="noopener">Book a demo</a></div></div></div></section>'''

    body = hero + tour_sec + loop + modules + attn + roles_sec + billing + diff + who + road + faq + cta
    schemas = [faq_schema(FAQ), {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Gym Command Center",
               "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
               "description": "Gym management software for members, memberships, invoicing, payments, attendance, leads and reporting. Early access planned.",
               "publisher": {"@type": "Organization", "name": "ToolsRhino", "url": SITE}, "url": SITE + "/gym-command-center"}]
    return page("gym-command-center.html", "Gym Command Center | Gym Management Software | ToolsRhino",
                "Gym management software for members, billing, attendance and leads, with one dashboard showing what needs attention. Early access planned.",
                body, label="Gym Command Center", schemas=schemas, trail=[("Services", "services.html")])
