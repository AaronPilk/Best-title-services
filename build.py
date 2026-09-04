#!/usr/bin/env python3
"""
Best Title Services — static site builder.

Everything that changes between sister sites lives in SITE below.
To spin up the next agency: copy this folder, swap SITE + assets/img/logo-*.png,
run `python3 build.py`, commit, push. Cloudflare Pages serves the HTML directly.
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
    "city":        "Hickory, NC",
    "region":      "North &amp; South Carolina",
    "region_abbr": "NC &amp; SC",
    "locale_line": "Hickory, NC &middot; Serving all of North &amp; South Carolina",
    "rate_calc":   "https://rates.wfgnationaltitle.com/",
    "years":       "20+",
}

S = SITE
ORDER_SUBJECT = "New Title Request " + S["name"]
MAILTO = "mailto:{e}?subject={s}".format(e=S["email"], s=ORDER_SUBJECT.replace(" ", "%20"))
TEL = "tel:" + S["phone_link"]

# ---------------------------------------------------------------- icons
I = {
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "mail" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "pin"  :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 8.6 8 10 4.6-1.4 8-5 8-10V5l-8-3z"/></svg>',
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
 "bolt" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/></svg>',
 "search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
 "layers":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
 "home" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 9-8 9 8"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/></svg>',
 "doc"  :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
 "bldg" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 9h.01M15 9h.01M9 13h.01M15 13h.01M9 17h.01M15 17h.01"/></svg>',
 "sold" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h18M3 9l2-5h14l2 5M4 9v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9M9 20v-6h6v6"/></svg>',
 "ok"   :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4 12 14.01l-3-3"/></svg>',
 "plus" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
 "tick" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
 "x"    :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
 "calc" :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h8M8 14h5"/></svg>',
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
  <div class="blob blob--a" style="bottom:-50%;right:-5%;opacity:.20;"></div>
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <div class="footer__logo"><img src="assets/img/logo-light.png" alt="{name}" width="420" height="200" /></div>
        <p>Independent title agency in Hickory, North Carolina. Searches, commitments and closings across all 146 counties in the Carolinas.</p>
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
          <span>{pin}{locale}</span>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span id="year">2026</span> {name}. All rights reserved.</span>
      <span>Title insurance &amp; closing services &middot; Hickory, NC</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
""".format(name=S["name"], links=links, rate=S["rate_calc"],
           tel=TEL, ph=I["phone"], phone_disp=S["phone_disp"], mail=I["mail"],
           email=S["email"], pin=I["pin"], locale=S["locale_line"])

def feature(ico, title, sub, d=""):
    return ('<div class="feature{d}" data-reveal><div class="feature__ico">{i}</div>'
            '<div><b>{t}</b><span>{s}</span></div></div>').format(
            d=(" "+d if d else ""), i=I[ico], t=title, s=sub)

WHY = [("shield","Experience","Two decades of it"),
       ("check","Independent","No parent company"),
       ("bolt","Quick turnaround","Commitments that hold up"),
       ("clock","Reachable","You get a human"),
       ("clock","Nights &amp; weekends","Closings don&rsquo;t wait"),
       ("globe","Both Carolinas","100 NC &amp; 46 SC counties"),
       ("search","Prior policies","Deep search network"),
       ("layers","Messy files","Untangled, not punted")]

def why_grid():
    return "\n      ".join(feature(k,t,s,["","d1","d2","d3"][i%4]) for i,(k,t,s) in enumerate(WHY))

# ================================================================ HOME
def page_index():
    return (
    head("{n} — Title Insurance &amp; Closings in Hickory, NC".format(n=S["name"]),
         "Independent title agency in Hickory, North Carolina. We search, clear and insure title for buyers, sellers, lenders and investors across all 100 NC counties and all 46 in South Carolina. Nights and weekends included.",
         "index.html")
    + nav("index.html")
    + """
<!-- HERO -->
<section class="hero hero--home" id="top">
  <div class="hero__bg">
    <img src="assets/img/hero-lake.jpg" alt="A lake in the North Carolina foothills at sunset with the Blue Ridge beyond" fetchpriority="high" width="2400" height="1600" />
  </div>
  <div class="wrap">
    <div class="hero__content" data-reveal>
      <span class="hero__badge"><span class="dot"></span>Independent title agency &middot; Hickory, NC</span>
      <h1>Title service <span class="text-grad">at its best.</span></h1>
      <p class="hero__sub">{name} is an independent title agency in Hickory, North Carolina. We search, clear, and insure title for buyers, sellers, lenders, and investors across both Carolinas &mdash; and we answer the phone when you need us.</p>
      <div class="hero__actions">
        <a href="{mailto}" class="btn btn--gold">Order Title {arrow}</a>
        <a href="{rate}" target="_blank" rel="noopener" class="btn btn--ghost">Rate Calculator</a>
      </div>
      <div class="hero-badges">
        <span>{shield} WFG National Title underwriting</span>
        <span>{clock} We work nights and weekends</span>
      </div>
    </div>
  </div>

  <div class="hero__floats" aria-hidden="true">
    <div class="fc-wrap fc-a" data-parallax="16">
      <div class="float-card anim-float">
        <div class="fc-ico">{bolt}</div>
        <div class="fc-title">Commitment issued</div>
        <div class="fc-sub">Searched, cleared, on time</div>
      </div>
    </div>
    <div class="fc-wrap fc-b" data-parallax="26">
      <div class="float-card float-card--row anim-float delay">
        <div class="pulse"><i></i></div>
        <div>
          <div class="fc-title">Someone picks up</div>
          <div class="fc-sub">Early, late, weekends</div>
        </div>
      </div>
    </div>
    <div class="fc-wrap fc-c" data-parallax="12">
      <div class="float-card float-card--row anim-float delay2">
        <div class="fc-ico">{globe}</div>
        <div>
          <div class="fc-title">146 counties</div>
          <div class="fc-sub">All of NC and SC</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TRUST STATS -->
<section class="section section--tight stats-float">
  <div class="wrap">
    <div class="stats">
      <div class="stat-card" data-reveal><b class="text-grad-b">{years}</b><span>Years working Carolina title</span></div>
      <div class="stat-card d1" data-reveal><b class="text-grad-b">146</b><span>Counties across NC &amp; SC</span></div>
      <div class="stat-card d2" data-reveal><b class="text-grad-b">7-Day</b><span>We&rsquo;re reachable, including weekends</span></div>
      <div class="stat-card d3" data-reveal><b class="text-grad-b">WFG</b><span>National underwriting behind us</span></div>
    </div>
  </div>
</section>

<!-- INTRO / MISSION -->
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Who we are</span>
      <h2>Independent &mdash; and that&rsquo;s the point</h2>
      <p>No parent company setting our turnaround times. No call center between you and the person actually running your search. We answer to the file in front of us, and to whoever is waiting on it.</p>
    </div>
  </div>
</section>

<!-- SERVICES PREVIEW -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What we do</span>
      <h2>Three ways we get you to the table</h2>
      <p>Two decades of Carolina title work behind every commitment we issue &mdash; whether it&rsquo;s a starter home in Catawba County, a lake lot changing hands, or a commercial deal with a stack of easements attached.</p>
    </div>
    <div class="grid grid-3">
      <a href="services.html" class="card" data-reveal>
        <div class="card__ico">{home}</div>
        <h3>Residential &amp; Land Title</h3>
        <p>Fast, accurate commitments from people who know the county registers of deeds by name &mdash; and know which old parcels tend to hide problems.</p>
      </a>
      <a href="services.html" class="card d1" data-reveal>
        <div class="card__ico">{doc}</div>
        <h3>Closing Services</h3>
        <p>We&rsquo;ll match you with a closing attorney or notary who fits the deal &mdash; in person or remote, wherever you are in the Carolinas.</p>
      </a>
      <a href="services.html" class="card d2" data-reveal>
        <div class="card__ico">{bldg}</div>
        <h3>Commercial Title</h3>
        <p>Bigger numbers, longer negotiations, more moving parts. We insure commercial deals to the level the investment actually warrants.</p>
      </a>
    </div>
    <div style="text-align:center;margin-top:44px;" data-reveal>
      <a href="services.html" class="btn btn--primary">See what we handle {arrow}</a>
    </div>
  </div>
</section>

<!-- ROOTED LOCALLY -->
<section class="section imgband">
  <div class="imgband__bg"><img src="assets/img/land.jpg" alt="Rolling foothills at golden hour outside Hickory, North Carolina" loading="lazy" width="1500" height="1125" /></div>
  <div class="wrap">
    <div style="max-width:640px;" data-reveal>
      <span class="eyebrow">Rooted in the foothills</span>
      <h2>We know this ground &mdash; parcel by parcel.</h2>
      <p style="margin-top:18px;">From the lake to the ridgelines, land in the Carolina foothills carries its own history: old family deeds, boundaries that moved, easements written a century ago and never cleaned up. Reading that history is the job.</p>
      <p style="margin-top:14px;">Being local means we&rsquo;ve pulled chains of title on these parcels before. It also means we pick up the phone when something needs sorting out today, not next week.</p>
      <div style="margin-top:30px;">
        <a href="services.html" class="btn btn--gold">See how we work {arrow}</a>
      </div>
    </div>
  </div>
</section>

<!-- WHY CHOOSE -->
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Why {short}</span>
      <h2>Why agents and lenders keep calling us</h2>
      <p>Eight reasons files tend to move faster when they come through our office.</p>
    </div>
    <div class="grid grid-4">
      {why}
    </div>
  </div>
</section>

<!-- WFG PARTNER -->
<section class="section band">
  <div class="blob blob--a" style="top:-30%;left:-10%;opacity:.34;"></div>
  <div class="blob blob--b" style="bottom:-40%;right:-10%;opacity:.24;"></div>
  <div class="wrap">
    <div class="partner" data-reveal>
      <span class="eyebrow eyebrow--light">Our underwriting partner</span>
      <h2>A national underwriter standing<br>behind local work</h2>
      <p style="max-width:580px;margin:18px auto 0;">We write on WFG National Title Insurance Company paper. You get a neighbor who knows the county, plus the financial backing of one of the country&rsquo;s largest title underwriters.</p>
      <div class="partner__logo"><img src="assets/img/wfg.png" alt="WFG National Title Insurance Company" loading="lazy" /></div>
    </div>
  </div>
</section>
""".format(name=S["name"], short=S["short"], years=S["years"],
           mailto=MAILTO, rate=S["rate_calc"],
           arrow=I["arrow"], shield=I["shield"], clock=I["clock"], bolt=I["bolt"],
           globe=I["globe"], home=I["home"], doc=I["doc"], bldg=I["bldg"], why=why_grid())
    + cta("Nights and weekends included", "Send us the file",
          "Email the details and we&rsquo;ll get the search started today. Questions first? Call &mdash; early, late, or on a Saturday. Someone will pick up.")
    + footer())

# ================================================================ SERVICES
def page_services():
    return (
    head("Services — {n} | Residential, Land, Closing &amp; Commercial Title".format(n=S["name"]),
         "Residential and land title searches, closing coordination, and commercial title insurance across all 100 North Carolina counties and all 46 in South Carolina. Based in Hickory, NC.",
         "services.html")
    + nav("services.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Our services</span>
      <h1>What we handle, and <span class="text-grad">how we handle it</span></h1>
      <p>Residential and land title, closing coordination, and commercial work &mdash; searched carefully, cleared quickly, insured properly. All 100 North Carolina counties and all 46 in South Carolina.</p>
    </div>
  </div>
</section>

<!-- RESIDENTIAL -->
<section class="section section--tight">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/residential.jpg" alt="Craftsman home with a covered porch in a North Carolina foothills neighborhood" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Residential &amp; Land</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Residential &amp; Land Title</span>
        <h2>We know which parcels hide problems</h2>
        <p>{name} runs residential and land searches out of Hickory, in the Catawba Valley. Being from here isn&rsquo;t a slogan &mdash; it means we&rsquo;ve pulled chains of title on these parcels before, and we know which subdivisions, which old family tracts, and which lake lots tend to surprise people.</p>
        <p>Our underwriters work in-house. When something turns up on your file at seven in the evening, you&rsquo;re not waiting on a ticket queue in another time zone. You&rsquo;re talking to the person who can clear it.</p>
        <p>Time-sensitive is the only kind of file we get, so we treat every one that way &mdash; a starter home or a hundred-acre tract, same attention either way.</p>
      </div>
    </div>

    <div class="grid grid-4" style="margin-top:56px;">
      {why}
    </div>
  </div>
</section>

<!-- CLOSING SERVICES -->
<section class="section section--tight" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media" data-reveal>
        <img src="assets/img/closing.jpg" alt="Signing a real estate closing document" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Closing Services</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Closing Services</span>
        <h2>The right closing table, wherever you are</h2>
        <p>Finding an attorney or notary who can actually close on your timeline is half the battle &mdash; especially outside the metros.</p>
        <p>We&rsquo;ve built a bench of closing professionals across both Carolinas, so we can match the deal to someone who&rsquo;s available and knows the county it sits in.</p>
        <ul class="checklist">
          <li>{ok}Closing attorneys and notaries we&rsquo;ve worked with before</li>
          <li>{ok}Coverage well past the Charlotte and Raleigh metros</li>
          <li>{ok}Remote and hybrid closings when travel doesn&rsquo;t make sense</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- COMMERCIAL -->
<section class="section section--tight">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/commercial.jpg" alt="Modern commercial office building" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Commercial</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">Commercial Title</span>
        <h2>Bigger deals, more places to get hurt</h2>
        <p>A commercial purchase carries a price tag and a negotiation that a residential deal doesn&rsquo;t. It carries more title risk too &mdash; layered easements, old leases, mechanics&rsquo; liens, entity questions about who can actually sign.</p>
        <p>We insure to the level the investment warrants, and we tell you plainly what a policy does and doesn&rsquo;t reach.</p>
      </div>
    </div>

    <div class="accordion" style="margin-top:56px;">
      <div class="acc" data-reveal>
        <button class="acc__q">Which properties actually need title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Practically all of them. The stakes just climb with commercial deals &mdash; the prices are higher and the purchase agreements are more complicated, so a defect costs considerably more to fix after the fact.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Why bother with commercial title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>It protects the investor when something surfaces on the title after closing. Those problems usually trace back to plain human error &mdash; a misfiled document, a clerical mistake, occasionally outright fraud.</p><p>Without a policy, the investor absorbs the loss. With one, the underwriter defends the claim.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Lender&rsquo;s policy or owner&rsquo;s policy &mdash; and who pays?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>There are two. The lender&rsquo;s policy protects the lender&rsquo;s stake and is required when there&rsquo;s financing. The owner&rsquo;s policy protects you. A buyer using a lender is typically responsible for both.</p><p>The owner&rsquo;s policy stays in force as long as you hold an interest in the property &mdash; no renewal, no expiration.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">How do you get a policy?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Send us the contract. We&rsquo;ll open the file, order the search, and walk you through whatever comes back &mdash; with two decades of Carolina commercial and residential work behind the read.</p></div></div>
      </div>
    </div>
  </div>
</section>
""".format(name=S["name"], why=why_grid(), ok=I["ok"], plus=I["plus"])
    + cta("Got a contract in hand?", "Let&rsquo;s open the file",
          "Send it over and we&rsquo;ll get the search started today. Residential, land, or commercial &mdash; same attention, same turnaround.")
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
NOTCOVERS = ["Not paying the contractor who redid your roof",
 "Falling behind on your property taxes",
 "Eminent domain, when a government takes private land for public use"]

# ================================================================ HOMEOWNERS
def page_homeowners():
    yes = "\n          ".join("<li>{t}{c}</li>".format(t=I["tick"],c=c) for c in COVERS)
    no  = "\n          ".join("<li>{x}{c}</li>".format(x=I["x"],c=c) for c in NOTCOVERS)
    return (
    head("Homeowners — {n} | Title Insurance, Explained Plainly".format(n=S["name"]),
         "Plain answers for buyers and sellers: what title insurance is, what it covers, what it leaves out, what it costs, and who writes the check. From {n} in Hickory, NC.".format(n=S["name"]),
         "homeowners.html")
    + nav("homeowners.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">For homeowners</span>
      <h1>Buying or selling? <span class="text-grad">Here&rsquo;s what happens to your title.</span></h1>
      <p>Plain answers on what title insurance is, what it covers, what it costs, who pays for it, and why it matters on the biggest purchase most people ever make.</p>
    </div>
  </div>
</section>

<!-- BUYERS & SELLERS -->
<section class="section section--tight">
  <div class="wrap">
    <div class="grid grid-2">
      <div class="card" data-reveal>
        <div class="card__ico">{home}</div>
        <h3>Buyers</h3>
        <p>Before you buy, someone needs to confirm the seller actually owns what they&rsquo;re selling &mdash; free and clear, with nothing attached that would follow the property over to you.</p>
        <p><strong>Why it matters:</strong> a defect on the title can limit what you&rsquo;re allowed to do with your own property, or cost real money to resolve. We work the public record thoroughly so you know exactly what you&rsquo;re taking on before you sign.</p>
        <p>You pay for the policy once, at closing. No renewal, no expiration date. It covers you for as long as you &mdash; or your heirs &mdash; hold an interest in the property.</p>
      </div>
      <div class="card d1" data-reveal>
        <div class="card__ico">{sold}</div>
        <h3>Sellers</h3>
        <p>Selling? We&rsquo;ll line up a closing attorney, chase down and satisfy any outstanding liens, and keep the file moving so nothing stalls at the table.</p>
        <p>Listing it yourself or working with an agent &mdash; either way, <strong>we work the same</strong>.</p>
        <ul class="checklist checklist--tight">
          <li>{ok}Commitments issued on time and correct</li>
          <li>{ok}People who have seen your situation before</li>
          <li>{ok}Title problems untangled, not handed back to you</li>
        </ul>
        <p style="margin-top:16px;">Send us the contract and we&rsquo;ll take it from there.</p>
      </div>
    </div>
  </div>
</section>

<!-- WHAT IS TITLE INSURANCE -->
<section class="section section--tight" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/contract-review.jpg" alt="Going through a title insurance policy with a client" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Title Insurance 101</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">The basics</span>
        <h2>So what is title insurance, exactly?</h2>
        <p>When you finance a home, one line on your closing statement is title insurance. It&rsquo;s a single premium, paid once, and the required policy protects your lender.</p>
        <p>You can also buy an owner&rsquo;s policy to protect yourself. That one is optional &mdash; and it&rsquo;s the one worth understanding before you decide.</p>
      </div>
    </div>

    <div style="max-width:860px;margin:48px auto 0;" data-reveal>
      <p style="margin-bottom:16px;">Title insurance covers third-party claims on a property &mdash; claims that didn&rsquo;t surface in the original search and only turn up after closing. A third party is anyone other than you: a roofing contractor who never got paid by the previous owner, a county tax office, an heir nobody knew about. &ldquo;Title&rdquo; just means legal ownership.</p>
      <p style="margin-bottom:16px;">A claim can appear at any point, including years into quiet ownership. Someone may hold rights to the property that nobody flagged when you made your offer &mdash; and often the seller didn&rsquo;t know either. In the case of an overlooked heir, that person may not learn they have a claim until a lawyer tells them.</p>
      <p>Before your loan closes, your lender orders a title search. A title company works the public record looking for anything that would affect the lender&rsquo;s or the buyer&rsquo;s rights:</p>
    </div>

    <div class="grid grid-3" style="margin-top:32px;">
      <div class="card" data-reveal>
        <h3 style="font-size:1.2rem;">Liens</h3>
        <p>A contractor, tax authority, or lender who wasn&rsquo;t paid can attach a lien to the property. You do not want to inherit the last owner&rsquo;s unpaid bills.</p>
      </div>
      <div class="card d1" data-reveal>
        <h3 style="font-size:1.2rem;">Easements</h3>
        <p>Someone else&rsquo;s right to use land you own &mdash; a utility corridor across the back of the lot, a neighbor&rsquo;s driveway. It can quietly limit what you&rsquo;re allowed to build.</p>
      </div>
      <div class="card d2" data-reveal>
        <h3 style="font-size:1.2rem;">Encumbrances</h3>
        <p>The broad category: liens and easements, plus zoning rules, HOA covenants, and any leasehold rights already running with the property.</p>
      </div>
    </div>

    <div style="max-width:860px;margin:32px auto 0;" data-reveal>
      <p style="margin-bottom:16px;">The search pulls deeds, mortgages, court judgments, divorce decrees, tax records, and child support orders.</p>
      <p>If it turns up a problem &mdash; the industry calls them &ldquo;clouds&rdquo; &mdash; we go to work clearing it. Sometimes that means your agent and the seller&rsquo;s agent getting the seller to resolve it. Occasionally a problem is serious enough to end the deal, and it is far better to learn that now than after you have signed.</p>
    </div>
  </div>
</section>

<!-- COVERAGE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Coverage</span>
      <h2>What a policy reaches &mdash; and what it doesn&rsquo;t</h2>
      <p>A policy covers underlying problems with a property&rsquo;s title that were missed before you bought it. It earns its keep on the day a search turns out to have overlooked a lien or an ownership dispute.</p>
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
        <p style="margin-bottom:16px;">A policy doesn&rsquo;t shield you from every possible limit on your property rights &mdash; and it won&rsquo;t cover problems you create yourself after closing:</p>
        <ul class="cover-list">
          {no}
        </ul>
        <p style="margin-top:16px;">The line is timing. Title insurance addresses issues that already existed and would have changed your decision to buy had you known about them. It doesn&rsquo;t cover what happens next.</p>
      </div>
    </div>
  </div>
</section>

<!-- EXPANDED COVERAGE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="callout" data-reveal>
      <div class="callout__t">
        <h3>Standard or expanded coverage?</h3>
        <p>Expanded coverage reaches additional risks a standard policy leaves out. Which one fits depends on the property and the deal. Call and we&rsquo;ll tell you straight whether it&rsquo;s worth it for your purchase.</p>
      </div>
      <a href="{tel}" class="btn btn--primary">Call {phone} {arrow}</a>
    </div>
  </div>
</section>

<!-- COST / WHO PAYS -->
<section class="section section--tight" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media" data-reveal>
        <img src="assets/img/cost.jpg" alt="Title paperwork on a desk" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Cost &amp; Coverage</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">How it works</span>
        <h2>What it costs, and who writes the check</h2>
        <p>An owner&rsquo;s policy can pay off a lien that surfaced after closing, fund your defense when someone sues claiming rights to your property, or settle with you in cash if the deed you bought on turns out to be forged. It also protects your ability to sell later, when the next buyer&rsquo;s search runs and finds the same problem.</p>
        <p>The lender&rsquo;s policy doesn&rsquo;t protect you, though you&rsquo;re the one paying for it &mdash; so it&rsquo;s fair to ask what it&rsquo;s actually for. If you lose the home because it was sold to you fraudulently, the lender files a claim to recover the payments it was counting on. Normally a lender would foreclose to recoup its losses, but if someone else holds rights to the property, foreclosure isn&rsquo;t available to them either.</p>
      </div>
    </div>

    <div class="grid grid-2" style="margin-top:48px;align-items:start;">
      <div class="card" data-reveal>
        <h3 style="font-size:1.25rem;">What does it cost?</h3>
        <p>One premium, paid once at closing &mdash; not a recurring cost. The owner&rsquo;s policy is priced off the purchase price, the lender&rsquo;s off the loan amount. Together they typically run 0.5% to 1.0% of the purchase price, or roughly $1,500 to $3,000 on a $300,000 home, according to ALTA.</p>
        <p>In both North and South Carolina, title insurance is filed at the same rate no matter which agency you use. The price is the price. What differs is who&rsquo;s running the search, and whether their underwriters can clear a problem when one shows up. Run your numbers through the rate calculator.</p>
        <a href="{rate}" target="_blank" rel="noopener" class="btn btn--primary btn--sm" style="margin-top:8px;">Open Rate Calculator {arrow}</a>
      </div>
      <div class="card d1" data-reveal>
        <h3 style="font-size:1.25rem;">Who pays for it?</h3>
        <p>The buyer covers the lender&rsquo;s policy as part of closing costs. The owner&rsquo;s policy can be paid by either side &mdash; local custom usually decides, and it&rsquo;s negotiable.</p>
        <p>Buying both at the same time lowers the cost of the owner&rsquo;s policy, through what the industry calls a simultaneous issue rate.</p>
      </div>
    </div>
  </div>
</section>
""".format(home=I["home"], sold=I["sold"], ok=I["ok"],
           tickw=I["tick"], xw=I["x"], yes=yes, no=no, rate=S["rate_calc"],
           arrow=I["arrow"], tel=TEL, phone=S["phone_plain"])
    + cta("Still have questions?", "Ask before you sign, not after",
          "Call and ask. We&rsquo;d rather spend fifteen minutes on the phone now than have you find out what a policy does and doesn&rsquo;t cover once something has already gone wrong.")
    + footer())

# ================================================================ CONTACT
def page_contact():
    return (
    head("Contact — {n} | Hickory, NC".format(n=S["name"]),
         "Order title, request a quote, or ask a question. {n} is reachable early mornings, late evenings and weekends across North and South Carolina. Call {p} or email {e}.".format(n=S["name"], p=S["phone_disp"], e=S["email"]),
         "contact.html")
    + nav("contact.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Get in touch</span>
      <h1>Send us the file, or just <span class="text-grad">ask a question</span></h1>
      <p>Order title, get a quote, or ask something you&rsquo;d rather not guess at. Early mornings, late evenings, weekends &mdash; across all 100 North Carolina counties and all 46 in South Carolina.</p>
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
          <div class="ci">{pin}</div>
          <div><h3>Where we are</h3><p>{locale}</p></div>
        </div>
        <div class="contact-card d3" data-reveal>
          <div class="ci">{clock}</div>
          <div><h3>When we&rsquo;re around</h3><p>Nights and weekends included &middot; 146 counties across NC &amp; SC</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="ci">{calc}</div>
          <div><h3>Estimate the cost</h3><a href="{rate}" target="_blank" rel="noopener">Open the rate calculator &rarr;</a></div>
        </div>
      </div>

      <div class="order-panel" data-reveal>
        <span class="order-panel__label">Ready to order?</span>
        <h2>Send it to us and we&rsquo;ll open the file</h2>
        <p>Email the details and we&rsquo;ll get the search started the same day. Send what you have &mdash; we&rsquo;ll chase down the rest.</p>

        <ul class="order-panel__list">
          <li>{ok}Property address and county</li>
          <li>{ok}Buyer and seller names</li>
          <li>{ok}Purchase price and target closing date</li>
          <li>{ok}Lender contact, if there is one</li>
          <li>{ok}A copy of the contract, if you have it</li>
        </ul>

        <div class="order-panel__actions">
          <a href="{mailto}" class="btn btn--primary">Email {email} {arrow}</a>
          <a href="{tel}" class="btn btn--ghost">{phone_ico} Call {phone_disp}</a>
        </div>
        <p class="order-panel__note">Missing something on the list? Send it anyway &mdash; we&rsquo;ll tell you what else we need.</p>
      </div>

    </div>
  </div>
</section>
""".format(phone=I["phone"], phone_ico=I["phone"], tel=TEL, phone_disp=S["phone_disp"],
           mail=I["mail"], email=S["email"], pin=I["pin"], locale=S["locale_line"],
           clock=I["clock"], calc=I["calc"], rate=S["rate_calc"], arrow=I["arrow"],
           ok=I["ok"], mailto=MAILTO)
    + cta("No file too small", "We&rsquo;re ready when you are",
          "Send it over and we&rsquo;ll get moving &mdash; accurate title, straight answers, and a schedule that bends to yours instead of the other way around.")
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
