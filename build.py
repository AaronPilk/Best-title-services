#!/usr/bin/env python3
"""
Best Title Services — static site builder.

Everything that changes between sister sites lives in SITE below.
To spin up the next agency: copy this folder, swap SITE + assets/img/logo-*.png,
run `python3 build.py`, commit, push. Cloudflare Pages serves the HTML directly.

Positioning note: this company serves North AND South Carolina broadly. Do not
reintroduce city-level positioning into copy, titles, meta or alt text.
"""

SITE = {
    "name":        "Best Title Services",
    "short":       "Best Title",
    "email":       "orders@besttitlenc.com",
    "domain":      "besttitlenc.com",
    "url":         "https://www.besttitlenc.com",
    "phone_disp":  "(704) 467-3031",
    "phone_plain": "704-467-3031",
    "phone_link":  "7044673031",
    "region":      "North &amp; South Carolina",
    "region_abbr": "NC &amp; SC",
    "serve_line":  "Serving North &amp; South Carolina",
    "counties":    "all 100 North Carolina counties and all 46 South Carolina counties",
    "rate_calc":   "https://rates.wfgnationaltitle.com/",
    "years":       "20+",
}

S = SITE
ORDER_SUBJECT = "New Title Request " + S["name"]
MAILTO = "mailto:{e}?subject={s}".format(e=S["email"], s=ORDER_SUBJECT.replace(" ", "%20"))
TEL = "tel:" + S["phone_link"]

# ---------------------------------------------------------------- icons
# Thin-line only. No filled glyphs, no clip-art metaphors.
I = {
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "mail" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "pin"  :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 8.6 8 10 4.6-1.4 8-5 8-10V5l-8-3z"/></svg>',
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
 "bolt" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
 "map"  :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m1 6 7-3 8 3 7-3v15l-7 3-8-3-7 3z"/><path d="M8 3v15M16 6v15"/></svg>',
 "chat" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8v.5z"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
 "trend":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M23 6 13.5 15.5l-5-5L1 18"/><path d="M17 6h6v6"/></svg>',
 "home" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-8 9 8"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/></svg>',
 "doc"  :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
 "bldg" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 9h.01M15 9h.01M9 13h.01M15 13h.01M9 17h.01M15 17h.01"/></svg>',
 "sold" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18M3 9l2-5h14l2 5M4 9v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9M9 20v-6h6v6"/></svg>',
 "ok"   :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4 12 14.01l-3-3"/></svg>',
 "plus" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
 "tick" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
 "x"    :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
 "calc" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h8M8 14h5"/></svg>',
}

NAVLINKS = [("index.html","Home"),("services.html","Services"),
            ("homeowners.html","Homeowners"),("contact.html","Contact")]

def head(title, desc, page):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="{url}/{page}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}/{page}" />
<meta property="og:image" content="{url}/assets/img/hero-lake.jpg" />
<meta name="theme-color" content="#0e2b6a" />
<link rel="icon" href="assets/img/favicon.png" />
<link rel="apple-touch-icon" href="assets/img/favicon.png" />
<link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
""".format(title=title, desc=desc, url=S["url"], page=("" if page=="index.html" else page))

def nav(active):
    links = "\n      ".join(
        '<a href="{h}"{c}>{t}</a>'.format(h=h, t=t, c=' class="active"' if h==active else '')
        for h,t in NAVLINKS)
    mob = "\n  ".join('<a href="{h}">{t}</a>'.format(h=h,t=t) for h,t in NAVLINKS)
    return """
<!-- NAV -->
<header class="nav">
  <div class="nav__inner">
    <a href="index.html" class="nav__logo" aria-label="{name} home">
      <img class="logo-dark" src="assets/img/logo-dark.png" alt="{name}" width="420" height="200" />
      <img class="logo-light" src="assets/img/logo-light.png" alt="{name}" width="420" height="200" />
    </a>
    <nav class="nav__links">
      {links}
    </nav>
    <div class="nav__cta">
      <a href="{tel}" class="nav__phone">{ph}{phone}</a>
      <a href="{mailto}" class="btn btn--primary btn--sm">Order Title {arrow}</a>
      <button class="nav__burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<div class="mobile-menu">
  {mob}
  <a href="{tel}">Call {phone}</a>
  <a href="{mailto}" class="btn btn--primary">Order Title</a>
</div>
""".format(name=S["name"], links=links, mob=mob, tel=TEL, mailto=MAILTO,
           phone=S["phone_plain"], ph=I["phone"], arrow=I["arrow"])

def cta(eyebrow, title, body):
    return """
<!-- CTA -->
<section class="section section--tight">
  <div class="wrap">
    <div class="cta-card" data-reveal>
      <span class="eyebrow eyebrow--light">{eyebrow}</span>
      <h2>{title}</h2>
      <p>{body}</p>
      <div class="cta-actions">
        <a href="{mailto}" class="btn btn--gold">Order Title {arrow}</a>
        <a href="{tel}" class="btn btn--outline-light">Call {phone}</a>
      </div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow, title=title, body=body, mailto=MAILTO, tel=TEL,
           phone=S["phone_plain"], arrow=I["arrow"])

def footer():
    links = "\n          ".join('<a href="{h}">{t}</a>'.format(h=h,t=t) for h,t in NAVLINKS)
    return """
<!-- FOOTER -->
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <div class="footer__logo"><img src="assets/img/logo-light.png" alt="{name}" width="420" height="200" /></div>
        <p>Title insurance, title searches, commitments, and closing coordination across {region}.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <div class="footer__links">
          {links}
          <a href="{rate}" target="_blank" rel="noopener">Rate Calculator</a>
        </div>
      </div>
      <div>
        <h4>Contact</h4>
        <div class="footer__contact">
          <a href="{tel}">{ph}{phone_disp}</a>
          <a href="mailto:{email}">{mail}{email}</a>
          <span>{pin}{serve}</span>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span id="year">2026</span> {name}. All rights reserved.</span>
      <span>Title insurance and closing services across {abbr}.</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
""".format(name=S["name"], region=S["region"], links=links, rate=S["rate_calc"],
           tel=TEL, ph=I["phone"], phone_disp=S["phone_disp"], mail=I["mail"],
           email=S["email"], pin=I["pin"], serve=S["serve_line"], abbr=S["region_abbr"])

# Six strong benefits — replaces the old eight-chip grid.
WHY = [("users", "Experienced Team",        "Two decades in title"),
       ("clock", "Fast Turnaround",         "Commitments without the wait"),
       ("chat",  "Responsive Communication", "You get a real answer"),
       ("doc",   "Thorough Title Review",   "Every detail checked"),
       ("map",   "NC &amp; SC Coverage",    "146 counties, both states"),
       ("shield","WFG Underwriting",        "National financial strength")]

def why_grid():
    return "\n      ".join(
        ('<div class="feature{d}" data-reveal><div class="feature__ico">{i}</div>'
         '<div><b>{t}</b><span>{s}</span></div></div>').format(
            d=(" d%d" % (n % 3) if n % 3 else ""), i=I[k], t=t, s=s)
        for n,(k,t,s) in enumerate(WHY))

SERVICE_CARDS = [
  ("home",  "Residential &amp; Land Title", "Thorough title work for homes, land, and property purchases across NC &amp; SC."),
  ("doc",   "Closing Coordination",         "Practical support to help connect the right parties and keep the file moving."),
  ("bldg",  "Commercial Title",             "Experienced title review and insurance for larger, more complex transactions."),
  ("trend", "Investors",                    "Dependable title support for single-property purchases, repeat transactions, and growing portfolios."),
]

def service_cards():
    return "\n      ".join(
      ('<a href="services.html" class="card{d}" data-reveal><div class="card__ico">{i}</div>'
       '<h3>{t}</h3><p>{p}</p></a>').format(
        d=(" d%d" % (n % 4) if n % 4 else ""), i=I[k], t=t, p=p)
      for n,(k,t,p) in enumerate(SERVICE_CARDS))

# ================================================================ HOME
def page_index():
    return (
    head("{n} — Title Insurance &amp; Title Services in NC &amp; SC".format(n=S["name"]),
         "Best Title Services provides dependable title insurance, title searches, commitments, and closing coordination for buyers, sellers, lenders, real estate professionals, and investors across North and South Carolina.",
         "index.html")
    + nav("index.html")
    + """
<!-- HERO -->
<section class="hero hero--home" id="top">
  <div class="hero__bg">
    <img src="assets/img/hero-lake.jpg" alt="Lake property at golden hour with foothills in the distance" fetchpriority="high" width="2400" height="1600" />
  </div>
  <div class="wrap">
    <div class="hero__content" data-reveal>
      <span class="hero__badge">Title Services &middot; North &amp; South Carolina</span>
      <h1>Title service <span class="text-grad">at its best.</span></h1>
      <p class="hero__sub">{name} provides dependable title insurance and title services for buyers, sellers, real estate professionals, and investors across {region}. Built on responsive service, fast turnaround, and experienced title work, we help keep transactions moving with confidence.</p>
      <div class="hero__actions">
        <a href="{mailto}" class="btn btn--gold">Order Title {arrow}</a>
        <a href="{rate}" target="_blank" rel="noopener" class="btn btn--ghost">Rate Calculator</a>
      </div>
      <div class="hero-badges">
        <span>{shield} WFG National Title underwriting</span>
        <span>{map} Serving NC &amp; SC</span>
      </div>
    </div>
  </div>

  <div class="hero__floats" aria-hidden="true">
    <div class="fc-wrap fc-a" data-parallax="16">
      <div class="float-card float-card--row anim-float">
        <div class="fc-ico">{bolt}</div>
        <div>
          <div class="fc-title">Fast, accurate title work</div>
          <div class="fc-sub">Reviewed carefully, delivered on time</div>
        </div>
      </div>
    </div>
    <div class="fc-wrap fc-b" data-parallax="24">
      <div class="float-card float-card--row anim-float delay">
        <div class="fc-ico">{chat}</div>
        <div>
          <div class="fc-title">Responsive service</div>
          <div class="fc-sub">Clear answers when you need them</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TRUST STATS -->
<section class="section section--tight stats-float">
  <div class="wrap">
    <div class="stats">
      <div class="stat-card" data-reveal><b class="text-grad-b">{years}</b><span>Years of title experience</span></div>
      <div class="stat-card d1" data-reveal><b class="text-grad-b">146</b><span>Counties across NC &amp; SC</span></div>
      <div class="stat-card d2" data-reveal><b class="text-grad-b">Fast</b><span>Turnaround on every file</span></div>
      <div class="stat-card d3" data-reveal><b class="text-grad-b">WFG</b><span>National Title underwriting</span></div>
    </div>
  </div>
</section>

<!-- WHO WE ARE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Who we are</span>
      <h2>A better title experience, from search to closing</h2>
      <p>{name} is built around responsive communication, experienced title work, and the kind of service that keeps transactions moving. We combine fast turnaround, careful review, and practical guidance to help buyers, sellers, lenders, real estate professionals, and investors close with confidence.</p>
    </div>
  </div>
</section>

<!-- WHAT WE DO -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What we do</span>
      <h2>The best path from title order to closing</h2>
      <p>From residential purchases and land transactions to closing coordination and commercial deals, {name} delivers experienced title work, responsive communication, and dependable title insurance across {region}.</p>
    </div>
    <div class="grid grid-4">
      {cards}
    </div>
    <div style="text-align:center;margin-top:48px;" data-reveal>
      <a href="services.html" class="btn btn--primary">Explore our services {arrow}</a>
    </div>
  </div>
</section>

<!-- LOCAL KNOWLEDGE / BROAD COVERAGE -->
<section class="section imgband">
  <div class="imgband__bg"><img src="assets/img/land.jpg" alt="Carolina foothills at golden hour" loading="lazy" width="1500" height="1125" /></div>
  <div class="wrap">
    <div style="max-width:620px;" data-reveal>
      <span class="eyebrow">Local knowledge. Broad Carolinas coverage.</span>
      <h2>Experienced title work wherever the property sits</h2>
      <p style="margin-top:20px;">Every property has a history. From mountain and lake properties to residential neighborhoods, land, and commercial transactions, our team understands how to review the details, identify potential issues, and help keep files moving across {region}.</p>
      <div style="margin-top:32px;">
        <a href="services.html" class="btn btn--gold">See how we work {arrow}</a>
      </div>
    </div>
  </div>
</section>

<!-- WHY BEST TITLE -->
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Why {short}</span>
      <h2>Why clients choose Best Title</h2>
      <p>Responsive communication, fast turnaround, experienced title work, and dependable service across {region}.</p>
    </div>
    <div class="grid grid-3">
      {why}
    </div>
  </div>
</section>

<!-- WFG PARTNER -->
<section class="section band">
  <div class="wrap">
    <div class="partner" data-reveal>
      <span class="eyebrow eyebrow--light">Our underwriting partner</span>
      <h2>Local service. National strength.</h2>
      <p style="max-width:600px;margin:20px auto 0;">{name} combines responsive, experienced title service with the financial strength and resources of WFG National Title Insurance Company.</p>
      <div class="partner__logo"><img src="assets/img/wfg.png" alt="WFG National Title Insurance Company" loading="lazy" /></div>
    </div>
  </div>
</section>
""".format(name=S["name"], short=S["short"], region=S["region"], years=S["years"],
           mailto=MAILTO, rate=S["rate_calc"], arrow=I["arrow"], shield=I["shield"],
           map=I["map"], bolt=I["bolt"], chat=I["chat"], why=why_grid(), cards=service_cards())
    + cta("Let&rsquo;s get started", "Ready for your best title experience?",
          "Send us the details and we&rsquo;ll get the file moving. Whether it is residential, land, commercial, or investment property, our team is ready to help with clear communication and dependable title service.")
    + footer())

# ================================================================ SERVICES
def page_services():
    return (
    head("Services — {n} | Residential, Land, Closing, Commercial &amp; Investor Title".format(n=S["name"]),
         "Residential and land title, closing coordination, investor support, and commercial title work across all 100 North Carolina counties and all 46 South Carolina counties.",
         "services.html")
    + nav("services.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Our services</span>
      <h1>Title services designed for the <span class="text-grad">best possible closing experience</span></h1>
      <p>Residential and land title, closing coordination, investor support, and commercial title work &mdash; handled with speed, accuracy, and responsive communication across {counties}.</p>
    </div>
  </div>
</section>

<!-- RESIDENTIAL & LAND -->
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/residential.jpg" alt="Residential property with a covered front porch" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Residential &amp; Land</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Residential &amp; Land Title</span>
        <h2>Thorough title work for homes and land</h2>
        <p>From residential purchases to land transactions, {name} provides careful title review, clear communication, and dependable title insurance to help protect ownership and keep files moving across {region}.</p>
        <ul class="checklist">
          <li>{ok}Title searches and commitments on residential purchases</li>
          <li>{ok}Land and acreage transactions, including complex parcels</li>
          <li>{ok}Owner&rsquo;s and lender&rsquo;s policies through WFG National Title</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- CLOSING COORDINATION -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media" data-reveal>
        <img src="assets/img/contract-review.jpg" alt="Reviewing closing documents with a client" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Closing Coordination</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Closing Coordination</span>
        <h2>Closing coordination that keeps things moving</h2>
        <p>We help coordinate the people and details needed to move the transaction forward, whether the closing is in person, remote, or somewhere in between.</p>
        <ul class="checklist">
          <li>{ok}Experienced closing attorneys and notaries</li>
          <li>{ok}Coordination across both Carolinas</li>
          <li>{ok}Remote and hybrid closings where they make sense</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- COMMERCIAL -->
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/commercial.jpg" alt="Modern commercial office building" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Commercial</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Commercial Title</span>
        <h2>Strong protection for higher-value transactions</h2>
        <p>Commercial real estate often involves larger investments, complex ownership structures, easements, leases, liens, and entity questions. {name} provides thorough title review and dependable title insurance designed to reduce risk and protect the investment.</p>
      </div>
    </div>
  </div>
</section>

<!-- INVESTORS -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media" data-reveal>
        <img src="assets/img/home-dusk.jpg" alt="Investment property at dusk" loading="lazy" width="2000" height="1125" />
        <span class="badge-pill">Investors</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Investor Title Support</span>
        <h2>Dependable title support for portfolios of any size</h2>
        <p>Whether it is a single-property purchase, a steady stream of repeat transactions, or a growing portfolio, investors need title work that is consistent, quick, and predictable.</p>
        <p>We handle recurring volume the same way we handle a first-time purchase: thorough review, clear communication, and a commitment you can plan around.</p>
      </div>
    </div>
  </div>
</section>

<!-- WHY GRID -->
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What you can expect</span>
      <h2>The same standard on every file</h2>
    </div>
    <div class="grid grid-3">
      {why}
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Common questions</span>
      <h2>Title insurance, answered</h2>
    </div>
    <div class="accordion">
      <div class="acc" data-reveal>
        <button class="acc__q">Which properties need title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Practically all of them. The stakes climb with commercial and investment deals, where prices are higher and purchase agreements are more complicated, so a defect costs considerably more to resolve after the fact.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Why is commercial title insurance important?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>It protects the investor when a problem surfaces on the title after closing. Those problems usually trace back to human error &mdash; a misfiled document, a clerical mistake, occasionally fraud.</p><p>Without a policy, the investor absorbs the loss. With one, the underwriter defends the claim.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Lender&rsquo;s policy or owner&rsquo;s policy &mdash; and who pays?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>There are two. The lender&rsquo;s policy protects the lender&rsquo;s stake and is required when there is financing. The owner&rsquo;s policy protects you. A buyer using a lender is typically responsible for both.</p><p>The owner&rsquo;s policy stays in force as long as you hold an interest in the property &mdash; no renewal, no expiration.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">How do I get started?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Send us the contract. We will open the file, order the search, and walk you through whatever comes back.</p></div></div>
      </div>
    </div>
  </div>
</section>
""".format(name=S["name"], region=S["region"], counties=S["counties"],
           why=why_grid(), ok=I["ok"], plus=I["plus"])
    + cta("Let&rsquo;s get started", "Ready to open a file?",
          "Send us the details and we&rsquo;ll get the title work underway. Residential, land, commercial, or investment &mdash; the same standard applies to every one.")
    + footer())

COVERS = ["Forged deeds and signatures",
 "Liens from contractors, tax offices or previous lenders",
 "Errors in the recorded deed",
 "Survey mistakes and boundary disputes",
 "Encroachments onto &mdash; or from &mdash; neighboring land",
 "Claims from an ex-spouse who never signed off on the sale",
 "Conflicting or contested wills",
 "Code violations left behind by a previous owner",
 "Documents that were recorded improperly"]
NOTCOVERS = ["Not paying a contractor who worked on your home",
 "Falling behind on your property taxes",
 "Eminent domain, when a government takes private land for public use"]

FAQ = [
 ("What is title insurance, exactly?",
  ["<p>&ldquo;Title&rdquo; means legal ownership. Title insurance covers third-party claims on a property &mdash; claims that did not surface in the original search and only appear after closing.</p>",
   "<p>A third party is anyone other than you: a contractor who was never paid by the previous owner, a county tax office, an heir nobody knew about.</p>",
   "<p>The premium is paid once, at closing. There is no renewal and no expiration.</p>"]),
 ("Why would a claim come up years after I buy?",
  ["<p>Someone may hold rights to the property that nobody flagged when you made your offer &mdash; and often the seller did not know either.</p>",
   "<p>In the case of an overlooked heir, that person may not learn they have a claim until a lawyer tells them. That is why coverage runs for as long as you hold an interest in the property.</p>"]),
 ("What does a title search actually look for?",
  ["<p>Before your loan closes, your lender orders a title search. A title company works the public record &mdash; deeds, mortgages, court judgments, divorce decrees, tax records, child support orders &mdash; looking for anything that would affect the lender&rsquo;s or the buyer&rsquo;s rights.</p>",
   "<p><strong>Liens.</strong> A contractor, tax authority, or lender who was not paid can attach a lien to the property. You do not want to inherit a previous owner&rsquo;s unpaid bills.</p>",
   "<p><strong>Easements.</strong> Someone else&rsquo;s right to use land you own &mdash; a utility corridor across the back of the lot, a neighbor&rsquo;s driveway. It can quietly limit what you are allowed to build.</p>",
   "<p><strong>Encumbrances.</strong> The broad category: liens and easements, plus zoning rules, HOA covenants, and any leasehold rights already running with the property.</p>"]),
 ("What happens if the search turns something up?",
  ["<p>We go to work clearing it. Sometimes that means your agent and the seller&rsquo;s agent getting the seller to resolve it before closing.</p>",
   "<p>Occasionally a problem is serious enough to end a deal &mdash; and it is far better to learn that now than after you have signed.</p>"]),
 ("What does it cost, and who pays?",
  ["<p>One premium, paid once at closing. The owner&rsquo;s policy is priced off the purchase price, the lender&rsquo;s off the loan amount. Together they typically run 0.5% to 1.0% of the purchase price, or roughly $1,500 to $3,000 on a $300,000 home, according to ALTA.</p>",
   "<p>The buyer covers the lender&rsquo;s policy as part of closing costs. The owner&rsquo;s policy can be paid by either side &mdash; local custom usually decides, and it is negotiable. Buying both at once lowers the cost of the owner&rsquo;s policy through a simultaneous issue rate.</p>",
   "<p>In both North and South Carolina, title insurance is filed at the same rate no matter which agency you use. What differs is who is running the search, and whether their underwriters can clear a problem when one appears.</p>"]),
 ("Why is the lender&rsquo;s policy on my closing statement?",
  ["<p>It protects the lender, not you, though you are the one paying for it. If you lose the home because it was sold to you fraudulently, the lender files a claim to recover the payments it was counting on.</p>",
   "<p>An owner&rsquo;s policy is what protects your equity, funds your defense if someone sues claiming rights to the property, and preserves your ability to sell later when the next buyer&rsquo;s search runs.</p>"]),
]

# ================================================================ HOMEOWNERS
def page_homeowners():
    yes = "\n          ".join("<li>{t}{c}</li>".format(t=I["tick"],c=c) for c in COVERS)
    no  = "\n          ".join("<li>{x}{c}</li>".format(x=I["x"],c=c) for c in NOTCOVERS)
    faq = "\n      ".join(
      ('<div class="acc" data-reveal><button class="acc__q">{q}<span class="ico">{p}</span></button>'
       '<div class="acc__a"><div class="acc__a-inner">{a}</div></div></div>').format(
        q=q, p=I["plus"], a="".join(a))
      for q,a in FAQ)
    return (
    head("Homeowners — {n} | Clear Answers on Title Insurance".format(n=S["name"]),
         "Clear answers for homeowners: what title insurance is, what it covers, what it leaves out, what it costs, and who pays. Title services across North and South Carolina.",
         "homeowners.html")
    + nav("homeowners.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">For homeowners</span>
      <h1>Clear answers for <span class="text-grad">homeowners</span></h1>
      <p>Buying or selling a home comes with enough moving parts. We explain title insurance clearly, help identify issues before closing, and provide dependable protection for one of the biggest investments most people make.</p>
    </div>
  </div>
</section>

<!-- BUYERS & SELLERS -->
<section class="section section--tight">
  <div class="wrap">
    <div class="grid grid-2">
      <div class="card" data-reveal>
        <div class="card__ico">{home}</div>
        <h3>Buying</h3>
        <p>Before you buy, someone needs to confirm the seller owns what they are selling &mdash; free and clear, with nothing attached that would follow the property to you.</p>
        <ul class="checklist checklist--tight">
          <li>{ok}A thorough search of the public record</li>
          <li>{ok}Issues identified before closing, not after</li>
          <li>{ok}One premium, paid once, with no expiration</li>
        </ul>
      </div>
      <div class="card d1" data-reveal>
        <div class="card__ico">{sold}</div>
        <h3>Selling</h3>
        <p>We coordinate the closing attorney, work through any outstanding liens, and keep the file moving so nothing stalls at the table.</p>
        <ul class="checklist checklist--tight">
          <li>{ok}Commitments issued on time and correct</li>
          <li>{ok}Liens identified and satisfied</li>
          <li>{ok}The same process whether or not you have an agent</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Title insurance, explained</span>
      <h2>The questions homeowners ask most</h2>
      <p>Short answers, in plain language. Open whichever one applies to you.</p>
    </div>
    <div class="accordion">
      {faq}
    </div>
  </div>
</section>

<!-- COVERAGE -->
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Coverage</span>
      <h2>What a policy reaches &mdash; and what it doesn&rsquo;t</h2>
      <p>A policy covers underlying problems with a property&rsquo;s title that were missed before you bought it.</p>
    </div>
    <div class="cover-2">
      <div class="cover-card cover-card--yes" data-reveal>
        <h3><span class="tag">{tickw}</span>What it covers</h3>
        <ul class="cover-list">
          {yes}
        </ul>
      </div>
      <div class="cover-card cover-card--no d1" data-reveal>
        <h3><span class="tag">{xw}</span>What it does not cover</h3>
        <p style="margin-bottom:18px;">A policy will not cover problems you create yourself after closing:</p>
        <ul class="cover-list">
          {no}
        </ul>
        <p style="margin-top:18px;">The line is timing. Title insurance addresses issues that already existed and would have changed your decision to buy had you known about them.</p>
      </div>
    </div>
  </div>
</section>

<!-- EXPANDED COVERAGE + RATE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="callout" data-reveal>
      <div class="callout__t">
        <h3>Standard or expanded coverage?</h3>
        <p>Expanded coverage reaches additional risks a standard policy leaves out. Which one fits depends on the property and the transaction &mdash; call and we will walk you through it, or estimate your cost with the WFG rate calculator.</p>
      </div>
      <a href="{rate}" target="_blank" rel="noopener" class="btn btn--primary">Rate Calculator {arrow}</a>
    </div>
  </div>
</section>
""".format(home=I["home"], sold=I["sold"], ok=I["ok"], tickw=I["tick"], xw=I["x"],
           yes=yes, no=no, faq=faq, rate=S["rate_calc"], arrow=I["arrow"])
    + cta("Questions before you sign?", "Ask us first",
          "We would rather spend fifteen minutes on the phone now than have you find out what a policy does and does not cover once something has already gone wrong.")
    + footer())

# ================================================================ CONTACT
def page_contact():
    return (
    head("Contact — {n} | Order Title in NC &amp; SC".format(n=S["name"]),
         "Order title, request a quote, or ask a question. Responsive title service across all 100 North Carolina counties and all 46 South Carolina counties. Call {p} or email {e}.".format(p=S["phone_disp"], e=S["email"]),
         "contact.html")
    + nav("contact.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Get in touch</span>
      <h1>Order title, or just <span class="text-grad">ask a question</span></h1>
      <p>Send us a file, request a quote, or ask something you would rather not guess at. Responsive title service across {counties}.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="contact-grid">

      <div class="contact-cards">
        <div class="contact-card" data-reveal>
          <div class="ci">{phone}</div>
          <div><h3>Call us</h3><a href="{tel}">{phone_disp}</a></div>
        </div>
        <div class="contact-card d1" data-reveal>
          <div class="ci">{mail}</div>
          <div><h3>Email &amp; orders</h3><a href="mailto:{email}">{email}</a></div>
        </div>
        <div class="contact-card d2" data-reveal>
          <div class="ci">{map}</div>
          <div><h3>Where we serve</h3><p>{serve}</p></div>
        </div>
        <div class="contact-card d3" data-reveal>
          <div class="ci">{chat}</div>
          <div><h3>Availability</h3><p>Responsive title service across {counties}</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="ci">{calc}</div>
          <div><h3>Estimate the cost</h3><a href="{rate}" target="_blank" rel="noopener">Open the WFG rate calculator &rarr;</a></div>
        </div>
      </div>

      <div class="order-panel" data-reveal>
        <span class="order-panel__label">Ready to order title?</span>
        <h2>Send us the details and we&rsquo;ll get the file moving</h2>
        <p>If something is missing, send what you have and we&rsquo;ll let you know what else is needed.</p>

        <ul class="order-panel__list">
          <li>{ok}Property address and county</li>
          <li>{ok}Buyer and seller names</li>
          <li>{ok}Purchase price and target closing date</li>
          <li>{ok}Lender contact, if there is one</li>
          <li>{ok}A copy of the contract, if you have it</li>
        </ul>

        <div class="order-panel__actions">
          <a href="{mailto}" class="btn btn--primary">Email {email} {arrow}</a>
          <a href="{tel}" class="btn btn--ghost">{phone} Call {phone_disp}</a>
        </div>
      </div>

    </div>
  </div>
</section>
""".format(phone=I["phone"], tel=TEL, phone_disp=S["phone_disp"], mail=I["mail"],
           email=S["email"], map=I["map"], serve=S["serve_line"], chat=I["chat"],
           counties=S["counties"], calc=I["calc"], rate=S["rate_calc"],
           arrow=I["arrow"], ok=I["ok"], mailto=MAILTO)
    + cta("No file too small", "We&rsquo;re ready when you are",
          "Send it over and we&rsquo;ll get moving &mdash; accurate title work, clear communication, and dependable service across {r}.".format(r=S["region"]))
    + footer())

# ================================================================ WRITE
PAGES = {
    "index.html":      page_index,
    "services.html":   page_services,
    "homeowners.html": page_homeowners,
    "contact.html":    page_contact,
}

if __name__ == "__main__":
    for fn, builder in PAGES.items():
        html = builder()
        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote %-16s %6d bytes" % (fn, len(html)))
    with open("sitemap.xml","w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for fn in ["", "services.html", "homeowners.html", "contact.html"]:
            f.write("  <url><loc>%s/%s</loc></url>\n" % (S["url"], fn))
        f.write("</urlset>\n")
    with open("robots.txt","w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % S["url"])
    print("wrote sitemap.xml, robots.txt")
