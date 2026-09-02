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
        <p>Providing residential and commercial title insurance across {region}. Trusted, independent, and available when you need us.</p>
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
      <span>Residential &amp; Commercial Title Insurance &middot; {abbr}</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
""".format(name=S["name"], region=S["region"], links=links, rate=S["rate_calc"],
           tel=TEL, ph=I["phone"], phone_disp=S["phone_disp"], mail=I["mail"],
           email=S["email"], pin=I["pin"], locale=S["locale_line"], abbr=S["region_abbr"])

def feature(ico, title, sub, d=""):
    return ('<div class="feature{d}" data-reveal><div class="feature__ico">{i}</div>'
            '<div><b>{t}</b><span>{s}</span></div></div>').format(
            d=(" "+d if d else ""), i=I[ico], t=title, s=sub)

WHY = [("shield","Experience",S["years"]+" years in title"),
       ("check","Trustworthy","Independent &amp; reliable"),
       ("bolt","Fast &amp; Accurate","Precise commitments"),
       ("clock","Responsive","Accessible when you need us"),
       ("clock","Nights &amp; Weekends","Available 7 days"),
       ("globe","NC &amp; SC Counties","Full state coverage"),
       ("search","Prior Policies","Extensive search network"),
       ("layers","Complex Issues","Resolved with confidence")]

def why_grid():
    return "\n      ".join(feature(k,t,s,["","d1","d2","d3"][i%4]) for i,(k,t,s) in enumerate(WHY))

# ================================================================ HOME
def page_index():
    return (
    head("{n} — Residential &amp; Commercial Title Insurance in Hickory, NC".format(n=S["name"]),
         "{n} is a trusted, independent title agency providing residential and commercial title insurance across North and South Carolina. Based in Hickory, NC. Fast, accurate, and available nights and weekends.".format(n=S["name"]),
         "index.html")
    + nav("index.html")
    + """
<!-- HERO -->
<section class="hero hero--home" id="top">
  <div class="hero__bg">
    <img src="assets/img/hero-lake.jpg" alt="Lake Hickory at sunset with the Blue Ridge foothills beyond" fetchpriority="high" width="2400" height="1600" />
  </div>
  <div class="wrap">
    <div class="hero__content" data-reveal>
      <span class="hero__badge"><span class="dot"></span>Independent title agency &middot; Hickory, NC</span>
      <h1>Residential &amp; commercial title insurance, <span class="text-grad">done right.</span></h1>
      <p class="hero__sub">{name} is a trusted, independent title agency specializing in title insurance across {region} &mdash; built on exceptional customer service, fast turnaround, and deep industry expertise.</p>
      <div class="hero__actions">
        <a href="{mailto}" class="btn btn--gold">Order Title {arrow}</a>
        <a href="{rate}" target="_blank" rel="noopener" class="btn btn--ghost">Rate Calculator</a>
      </div>
      <div class="hero-badges">
        <span>{shield} Backed by WFG Underwriters</span>
        <span>{clock} Available Nights &amp; Weekends</span>
      </div>
    </div>
  </div>

  <div class="hero__floats" aria-hidden="true">
    <div class="fc-wrap fc-a" data-parallax="16">
      <div class="float-card anim-float">
        <div class="fc-ico">{bolt}</div>
        <div class="fc-title">Title commitment</div>
        <div class="fc-sub">Fast, accurate, on your timeline</div>
      </div>
    </div>
    <div class="fc-wrap fc-b" data-parallax="26">
      <div class="float-card float-card--row anim-float delay">
        <div class="pulse"><i></i></div>
        <div>
          <div class="fc-title">We answer after hours</div>
          <div class="fc-sub">Early mornings &middot; Late evenings</div>
        </div>
      </div>
    </div>
    <div class="fc-wrap fc-c" data-parallax="12">
      <div class="float-card float-card--row anim-float delay2">
        <div class="fc-ico">{globe}</div>
        <div>
          <div class="fc-title">Every county, NC &amp; SC</div>
          <div class="fc-sub">Statewide search network</div>
        </div>
      </div>
    </div>
  </div>

</section>

<!-- TRUST STATS -->
<section class="section section--tight stats-float">
  <div class="wrap">
    <div class="stats">
      <div class="stat-card" data-reveal><b class="text-grad-b">{years}</b><span>Years in title &amp; real estate</span></div>
      <div class="stat-card d1" data-reveal><b class="text-grad-b">100%</b><span>NC &amp; SC county coverage</span></div>
      <div class="stat-card d2" data-reveal><b class="text-grad-b">7-Day</b><span>Nights &amp; weekend service</span></div>
      <div class="stat-card d3" data-reveal><b class="text-grad-b">WFG</b><span>Industry-leading underwriter</span></div>
    </div>
  </div>
</section>

<!-- INTRO / MISSION -->
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Who we are</span>
      <h2>A trusted, independent title agency for the Carolinas</h2>
      <p>We exist to exceed expectations and deliver unparalleled service to our valued clients &mdash; combining precision, speed, and genuine care on every file.</p>
    </div>
  </div>
</section>

<!-- SERVICES PREVIEW -->
<section class="section" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">What we do</span>
      <h2>A tailored range of title services</h2>
      <p>At {name}, we offer a tailored range of services backed by more than {yrs_words} of experience &mdash; from residential and land title insurance to closing coordination and complex commercial transactions.</p>
    </div>
    <div class="grid grid-3">
      <a href="services.html" class="card" data-reveal>
        <div class="card__ico">{home}</div>
        <h3>Residential &amp; Land Title</h3>
        <p>Exceptional customer service and unparalleled speed with utmost precision &mdash; from a locally rooted team that knows your area.</p>
      </a>
      <a href="services.html" class="card d1" data-reveal>
        <div class="card__ico">{doc}</div>
        <h3>Closing Services</h3>
        <p>We connect you with experienced closing attorneys and notaries &mdash; including remote closings for flexibility and convenience.</p>
      </a>
      <a href="services.html" class="card d2" data-reveal>
        <div class="card__ico">{bldg}</div>
        <h3>Commercial Title</h3>
        <p>Higher stakes and intricate negotiations demand full protection. We safeguard your investment commensurate with its value.</p>
      </a>
    </div>
    <div style="text-align:center;margin-top:44px;" data-reveal>
      <a href="services.html" class="btn btn--primary">Explore all services {arrow}</a>
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
      <p style="margin-top:18px;">From the lake to the ridgelines, land in the Carolina foothills carries its own history: old family deeds, shifting boundaries, easements written a century ago. We read that history for a living.</p>
      <p style="margin-top:14px;">Being local means we understand your particular location and circumstances &mdash; and it means we pick up the phone when something needs sorting out today, not next week.</p>
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
      <h2>Built for speed, accuracy &amp; trust</h2>
      <p>Every reason clients across the Carolinas keep coming back to us.</p>
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
      <h2>Proudly partnered with WFG&rsquo;s<br>industry-leading underwriters</h2>
      <p style="max-width:580px;margin:18px auto 0;">Backed by WFG National Title Insurance Company, we pair local expertise with the strength of a national underwriter.</p>
      <div class="partner__logo"><img src="assets/img/wfg.png" alt="WFG National Title Insurance Company" loading="lazy" /></div>
    </div>
  </div>
</section>
""".format(name=S["name"], short=S["short"], region=S["region"], years=S["years"],
           yrs_words="two decades", mailto=MAILTO, rate=S["rate_calc"],
           arrow=I["arrow"], shield=I["shield"], clock=I["clock"], bolt=I["bolt"],
           globe=I["globe"], home=I["home"], doc=I["doc"], bldg=I["bldg"], why=why_grid())
    + cta("Available nights &amp; weekends", "Ready to order your title?",
          "Send us your request and our team will get started right away. Questions? We&rsquo;re accessible early mornings and late evenings &mdash; whenever you need us.")
    + footer())

# ================================================================ SERVICES
def page_services():
    return (
    head("Services — {n} | Residential, Closing &amp; Commercial Title".format(n=S["name"]),
         "Residential and land title insurance, closing services, and commercial title insurance across North and South Carolina — backed by more than two decades of experience.",
         "services.html")
    + nav("services.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Our services</span>
      <h1>Title services, tailored to <span class="text-grad">every transaction</span></h1>
      <p>From residential and land title to closing coordination and complex commercial deals &mdash; delivered with speed, precision, and genuine care across the Carolinas.</p>
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
        <span class="eyebrow">Residential &amp; Land Title Insurance</span>
        <h2>Local expertise, unmatched precision</h2>
        <p>{name} is committed to delivering exceptional customer service and unparalleled speed with utmost precision.</p>
        <p>As a locally rooted North Carolina business based in {city}, we take pride in our deep understanding of your unique location and circumstances. With our team of in-house underwriters, we&rsquo;re accessible to address inquiries and tackle any problems that emerge during early mornings or late evenings.</p>
        <p>Your requests are our highest priority, and we remain steadfast in our commitment to meeting your time-sensitive needs, regardless of their scale.</p>
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
        <h2>The right closing, in person or remote</h2>
        <p>At {name} we understand that finding the right attorney or notary for your closing can be a crucial step in the real estate process.</p>
        <p>We&rsquo;ve established partnerships with a network of experienced professionals spanning various regions.</p>
        <ul class="checklist">
          <li>{ok}Experienced closing attorneys &amp; notaries</li>
          <li>{ok}A trusted network spanning multiple regions</li>
          <li>{ok}Remote closings for flexibility &amp; convenience</li>
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
        <span class="eyebrow">Commercial Title Insurance</span>
        <h2>Protection commensurate with value</h2>
        <p>Unlike residential properties, commercial ones usually carry a hefty price tag and involve intricate negotiation procedures.</p>
        <p>Safeguarding your investment to its fullest extent, commensurate with its value, is paramount.</p>
      </div>
    </div>

    <div class="accordion" style="margin-top:56px;">
      <div class="acc" data-reveal>
        <button class="acc__q">What property type requires title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Although title insurance is common across all real estate transactions, its significance escalates in commercial real estate dealings due to the typically elevated purchase prices and intricate purchase agreements involved.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Why do I need commercial title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Commercial title insurance safeguards the investor in case any complications arise concerning the property&rsquo;s title. These issues can stem from sources such as negligence, clerical errors, or even fraud.</p><p>In the absence of a title insurance policy, the property investor risks losing their investment.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">Types of policies and who pays<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>There are two types of title insurance: the lender&rsquo;s policy and the owner&rsquo;s policy. If the buyer is utilizing a lender, they are responsible for purchasing both policies.</p><p>The owner&rsquo;s policy provides coverage for as long as the individual owns the property.</p></div></div>
      </div>
      <div class="acc" data-reveal>
        <button class="acc__q">How do you acquire title insurance?<span class="ico">{plus}</span></button>
        <div class="acc__a"><div class="acc__a-inner"><p>Given the complexity of commercial real estate, selecting the appropriate agency is paramount. With over two decades of experience, we are here to serve your needs.</p></div></div>
      </div>
    </div>
  </div>
</section>
""".format(name=S["name"], city=S["city"], why=why_grid(), ok=I["ok"], plus=I["plus"])
    + cta("Let&rsquo;s go&hellip;", "Start your transaction today",
          "Whatever the property type, our team is ready to get your title moving &mdash; accurately and fast. Available nights and weekends.")
    + footer())

COVERS = ["Property survey errors","Boundary disputes","Errors on the property deed",
 "Building code violations by a previous owner","Conflicting wills",
 "Claims by an ex-spouse who didn&rsquo;t sign off on the sale","Forged documents",
 "Liens from contractors, taxing entities or previous lenders","Encroachments",
 "Improperly recorded documents"]
NOTCOVERS = ["Failing to pay the company that replaced your roof",
 "Failing to pay your property taxes",
 "Eminent domain &mdash; when a government seizes private property for a public purpose"]

# ================================================================ HOMEOWNERS
def page_homeowners():
    yes = "\n          ".join("<li>{t}{c}</li>".format(t=I["tick"],c=c) for c in COVERS)
    no  = "\n          ".join("<li>{x}{c}</li>".format(x=I["x"],c=c) for c in NOTCOVERS)
    return (
    head("Homeowners — {n} | Buyers, Sellers &amp; Title Insurance Explained".format(n=S["name"]),
         "For buyers and sellers: what title insurance is, what it covers and doesn't, how it works, who pays, and how much it costs — explained by {n}.".format(n=S["name"]),
         "homeowners.html")
    + nav("homeowners.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">For homeowners</span>
      <h1>Buying or selling? <span class="text-grad">We&rsquo;ve got your title covered.</span></h1>
      <p>Everything you need to know about title insurance &mdash; what it is, what it covers, how it works, and why it protects one of the biggest investments you&rsquo;ll ever make.</p>
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
        <p>When purchasing a home, it&rsquo;s essential to verify the seller&rsquo;s rightful ownership and ensure there are no unresolved issues that could impede the transfer of the title to you.</p>
        <p><strong>Why is this important?</strong> Problems with the title can impose limitations on property usage and potentially lead to financial losses. This is where title insurance becomes invaluable, and {name} is here to assist you. We conduct thorough title searches to confirm that your ownership is clear of any encumbrances.</p>
        <p>The cost of title insurance is paid only once, with no renewal premiums or expiration dates. This protection endures for as long as you, or your successors, hold an interest in the property &mdash; ensuring long-term security.</p>
      </div>
      <div class="card d1" data-reveal>
        <div class="card__ico">{sold}</div>
        <h3>Sellers</h3>
        <p>Selling your house? <strong>{name} can help!</strong> We will assist you in finding an experienced Closing Attorney and satisfy any liens. We promise a smooth closing, great communication, and amazing service.</p>
        <p>Whether you are listing your house for sale by owner or working with a real estate agent, we are here for you.</p>
        <ul class="checklist checklist--tight">
          <li>{ok}Timely and accurate title commitments</li>
          <li>{ok}Experienced and knowledgeable</li>
          <li>{ok}Ability to resolve complex issues</li>
        </ul>
        <p style="margin-top:16px;">{name} will make the closing easy. Contact us to get your transaction started.</p>
      </div>
    </div>
  </div>
</section>

<!-- WHAT IS TITLE INSURANCE -->
<section class="section section--tight" style="background:var(--bg-2);">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-reveal>
        <img src="assets/img/contract-review.jpg" alt="Reviewing a title insurance policy with a client" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Title Insurance 101</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">The basics</span>
        <h2>What is title insurance and why do I need it?</h2>
        <p>When you take out a mortgage, one part of your closing costs will be title insurance. The premium is a one-time charge, and the policy protects the lender. You also can purchase owner&rsquo;s title insurance to protect yourself, but it&rsquo;s not required.</p>
        <p>Here&rsquo;s what you need to know about title insurance: what it covers, how much it costs, and whether you should buy it.</p>
      </div>
    </div>

    <div style="max-width:860px;margin:48px auto 0;" data-reveal>
      <p style="margin-bottom:16px;">Title insurance is a policy that covers third-party claims on a property that don&rsquo;t show up in the initial title search and arise after a real estate closing. A third party is someone other than the property&rsquo;s owner, such as a construction company that didn&rsquo;t get paid for its work on the home under a previous owner. The term &ldquo;title&rdquo; refers to someone&rsquo;s legal ownership of the property.</p>
      <p style="margin-bottom:16px;">A title claim could arise at any time, even after you&rsquo;ve owned the property with no problems for many years. How could this happen? Someone else might have ownership rights that you don&rsquo;t know about when you make an offer to buy a property. Even the current owner might not be aware that someone else has a claim on the property. In the case of an overlooked heir, even the person who has those rights might not know they have them.</p>
      <p>Before your home loan closes, your mortgage lender will order a title search from a title company. The title company searches public records related to your home to try to find any title defects that could affect the lender&rsquo;s or buyer&rsquo;s property rights, such as:</p>
    </div>

    <div class="grid grid-3" style="margin-top:32px;">
      <div class="card" data-reveal>
        <h3 style="font-size:1.2rem;">Liens</h3>
        <p>Liens can get placed on the property by a contractor, tax authority or lender who hasn&rsquo;t been paid. You don&rsquo;t want to get stuck paying a previous owner&rsquo;s unpaid bills.</p>
      </div>
      <div class="card d1" data-reveal>
        <h3 style="font-size:1.2rem;">Easements</h3>
        <p>Easements are someone else&rsquo;s right to use your property even though you are the owner &mdash; for example, utility lines in your backyard. An easement could limit your ability to use your property however you want.</p>
      </div>
      <div class="card d2" data-reveal>
        <h3 style="font-size:1.2rem;">Encumbrances</h3>
        <p>Encumbrances include liens (&ldquo;financial encumbrances&rdquo;) and easements, but also zoning laws, restrictive covenants imposed by homeowners associations, and leaseholder rights.</p>
      </div>
    </div>

    <div style="max-width:860px;margin:32px auto 0;" data-reveal>
      <p style="margin-bottom:16px;">A title company searches public records including deeds, mortgages, divorce decrees, court judgments, tax records and child support orders.</p>
      <p>If the title search reveals any problems (also called &ldquo;clouds&rdquo;), the title company will try to resolve them. In some cases, your real estate agent will need to work with the seller&rsquo;s agent to get the seller to resolve the problem. In other cases, the problem may be significant enough to derail the sale.</p>
    </div>
  </div>
</section>

<!-- COVERAGE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Coverage</span>
      <h2>What title insurance covers &mdash; and what it doesn&rsquo;t</h2>
      <p>A title insurance policy covers underlying issues with a property&rsquo;s title that might have been missed before you bought the home. It comes in handy if the public record search failed to catch any liens or ownership disputes.</p>
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
        <p style="margin-bottom:16px;">Title insurance doesn&rsquo;t protect homeowners against all possible infringements on their property rights. For example, it doesn&rsquo;t protect you against title problems caused by your own actions, such as:</p>
        <ul class="cover-list">
          {no}
        </ul>
        <p style="margin-top:16px;">In short, it doesn&rsquo;t protect against issues newly created after you buy the property. It protects against issues that might have affected your decision to purchase the property had you known about them at the time.</p>
      </div>
    </div>
  </div>
</section>

<!-- EXPANDED COVERAGE -->
<section class="section section--tight">
  <div class="wrap">
    <div class="callout" data-reveal>
      <div class="callout__t">
        <h3>Standard vs. Expanded Coverage</h3>
        <p>Homeowners can choose between standard and expanded coverage, which broadens protection against certain additional risks. Not sure which fits your purchase? Call us and we&rsquo;ll walk you through the difference in plain English.</p>
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
        <img src="assets/img/cost.jpg" alt="Title insurance paperwork on a desk" loading="lazy" width="1500" height="1125" />
        <span class="badge-pill">Cost &amp; Coverage</span>
      </div>
      <div class="split__body d1" data-reveal>
        <span class="eyebrow">How it works</span>
        <h2>Who pays for title insurance, and how much does it cost?</h2>
        <p>An owner&rsquo;s title insurance policy can cover the costs of paying off a previously undiscovered lien or defending against a lawsuit filed against you by someone claiming a right to the property. It can also provide a cash settlement to a new owner who unwittingly purchases a property with a forged deed. It protects your ability to sell the home one day if a problem turns up during a later title search.</p>
        <p>You&rsquo;re probably less concerned about how a lender&rsquo;s policy works since it doesn&rsquo;t protect you &mdash; but you might still be curious, as you&rsquo;re being asked to pay for it. If you lose your home because the property was sold to you fraudulently, the lender will file a claim with its title insurance company to recoup the mortgage payments it was expecting from you. Under other circumstances the lender could foreclose to recoup its losses &mdash; but if someone else has a right to the home, foreclosure isn&rsquo;t an option.</p>
      </div>
    </div>

    <div class="grid grid-2" style="margin-top:48px;align-items:start;">
      <div class="card" data-reveal>
        <h3 style="font-size:1.25rem;">How much does it cost?</h3>
        <p>Title insurance is a one-time, up-front fee &mdash; not an ongoing expense. An owner&rsquo;s policy is based on the home&rsquo;s purchase price, while a lender&rsquo;s policy is based on the loan amount. Both policies together usually cost about 0.5% to 1.0% of the home&rsquo;s purchase price, or $1,500 to $3,000 on a $300,000 home, according to ALTA.</p>
        <p>In North and South Carolina, the price for title insurance is the same no matter which title insurance company you use. However, it&rsquo;s important to make sure you&rsquo;re using a reputable company with experienced underwriters. You can get an estimate of what title insurance costs in your area using the rate calculator.</p>
        <a href="{rate}" target="_blank" rel="noopener" class="btn btn--primary btn--sm" style="margin-top:8px;">Open Rate Calculator {arrow}</a>
      </div>
      <div class="card d1" data-reveal>
        <h3 style="font-size:1.25rem;">Who pays for title insurance?</h3>
        <p>The buyer pays for the lender&rsquo;s title insurance policy as part of their closing costs. Either the buyer or seller can pay for the owner&rsquo;s policy on behalf of the buyer. Local real estate custom often determines who pays.</p>
        <p>Buying an owner&rsquo;s policy at the same time as a lender&rsquo;s policy can reduce the cost of the owner&rsquo;s policy through what&rsquo;s called a &ldquo;simultaneous issue charge.&rdquo;</p>
      </div>
    </div>
  </div>
</section>
""".format(name=S["name"], home=I["home"], sold=I["sold"], ok=I["ok"],
           tickw=I["tick"], xw=I["x"], yes=yes, no=no, rate=S["rate_calc"],
           arrow=I["arrow"], tel=TEL, phone=S["phone_plain"])
    + cta("Let&rsquo;s go&hellip;", "Protect your investment",
          "Buying or selling in the Carolinas? We&rsquo;ll make your closing easy &mdash; with clear title, great communication, and service available nights and weekends.")
    + footer())

# ================================================================ CONTACT
def page_contact():
    return (
    head("Contact — {n} | Order Title in Hickory, NC".format(n=S["name"]),
         "Contact {n} to order title or ask a question. Available nights and weekends across North and South Carolina. Call {p} or email {e}.".format(n=S["name"], p=S["phone_disp"], e=S["email"]),
         "contact.html")
    + nav("contact.html")
    + """
<section class="subhero">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Get in touch</span>
      <h1>Let&rsquo;s get your <span class="text-grad">title started</span></h1>
      <p>Order title, request a quote, or ask a question. We&rsquo;re accessible early mornings, late evenings, and weekends &mdash; serving every county in North and South Carolina.</p>
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
          <div><h3>Hours</h3><p>Available nights &amp; weekends &middot; Serving all of NC &amp; SC</p></div>
        </div>
        <div class="contact-card" data-reveal>
          <div class="ci">{calc}</div>
          <div><h3>Rate calculator</h3><a href="{rate}" target="_blank" rel="noopener">Estimate your title costs &rarr;</a></div>
        </div>
      </div>

      <form class="form-card" id="contactForm" data-reveal novalidate>
        <div class="form-row">
          <div class="field">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" placeholder="Your full name" autocomplete="name" required />
          </div>
          <div class="field">
            <label for="phone">Phone</label>
            <input type="tel" id="phone" name="phone" placeholder="(704) 000-0000" autocomplete="tel" />
          </div>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" placeholder="you@email.com" autocomplete="email" required />
        </div>
        <div class="field">
          <label for="topic">How can we help?</label>
          <select id="topic" name="topic">
            <option>Order title</option>
            <option>Request a quote</option>
            <option>Residential / land title</option>
            <option>Commercial title</option>
            <option>Closing services</option>
            <option>General question</option>
          </select>
        </div>
        <div class="field">
          <label for="message">Details</label>
          <textarea id="message" name="message" placeholder="Property address, transaction details, timeline, or your question&hellip;"></textarea>
        </div>
        <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Send message {arrow}</button>
        <p id="formNote" style="font-size:.85rem;color:var(--muted);margin-top:14px;text-align:center;">This opens your email app pre-filled to {email}. Prefer to call? <a href="{tel}" style="color:var(--brand-2);font-weight:650;">{phone_disp}</a></p>
      </form>

    </div>
  </div>
</section>
""".format(phone=I["phone"], tel=TEL, phone_disp=S["phone_disp"], mail=I["mail"],
           email=S["email"], pin=I["pin"], locale=S["locale_line"], clock=I["clock"],
           calc=I["calc"], rate=S["rate_calc"], arrow=I["arrow"])
    + cta("Available nights &amp; weekends", "Ready when you are",
          "Send your request and our team will get started right away &mdash; accurate title, clear communication, and service on your schedule.")
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
    # sitemap + robots
    with open("sitemap.xml","w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for fn in ["", "services.html", "homeowners.html", "contact.html"]:
            f.write("  <url><loc>%s/%s</loc></url>\n" % (S["url"], fn))
        f.write("</urlset>\n")
    with open("robots.txt","w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % S["url"])
    print("wrote sitemap.xml, robots.txt")
