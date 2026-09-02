# Best Title Services

Website for **Best Title Services** — residential & commercial title insurance,
based in Hickory, NC, serving all of North & South Carolina.

Static site, no build tooling required to serve. Apple-inspired aesthetic:
floating glass cards, soft gradient washes, scroll-reveal motion, sticky glass navbar.

- **Brand:** `#0e2b6a` navy · `#fdc931` gold · `#f96223` orange
- **Contact:** orders@besttitlenc.com · (704) 467-3031
- **Underwriter:** WFG National Title Insurance Company

## Structure

```
index.html         Home — lake/mountain hero, floating cards, services, WFG band
services.html      Residential & Land · Closing · Commercial (+ FAQ accordion)
homeowners.html    Buyers, Sellers, and title insurance explained
contact.html       Contact cards + mailto form
build.py           Page generator — the single source of truth
assets/css/style.css   Design system
assets/js/main.js      Nav, scroll reveal, accordion, parallax, form
assets/img/            Imagery + logo lockups
sitemap.xml robots.txt
```

## Editing

The four HTML files are **generated**. Edit `build.py`, then:

```bash
python3 build.py
```

Nav, footer, CTA blocks and the "why choose us" grid are defined once in
`build.py` and injected into every page, so they can never drift apart.

## Cloning this for a sister agency

Everything that changes between sites lives in the `SITE` dict at the top of
`build.py` — name, email, phone, city, region, rate-calculator URL.

1. Copy this folder
2. Edit `SITE` in `build.py`
3. Drop the new logo in and regenerate `logo-dark.png` / `logo-light.png` / `favicon.png`
4. Swap any location-specific imagery in `assets/img/`
5. `python3 build.py` → commit → push

## Run locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000

## Deploy — Cloudflare Pages

Connect this repo in the Cloudflare dashboard:

| Setting | Value |
|---|---|
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `/` |
| Production branch | `main` |

Cloudflare serves the committed HTML directly — no build step runs. Every push
to `main` publishes. Add `besttitlenc.com` under **Custom domains** once it's live.
