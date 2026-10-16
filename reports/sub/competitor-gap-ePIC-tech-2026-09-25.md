# Technical Gap: BiXBiT (bixbit.io/en) vs ePIC Blockchain (epicblockchain.io) — 2026-09-25

> Scope: only **noticeable** technical advantages of the competitor + where BiXBiT is ahead.
> Snapshot of measurements: `data/dfs-lighthouse-instant-bixbit-vs-epic-2026-09-25.json`.
> The URL structure comes from `data/site-structure.md` (real, crawled 2026-09-16), not guessed.

## Data sources (status)

| Source | Status | Used for |
|---|---|---|
| Google PageSpeed Insights API | **no access** (HTTP 500) | — |
| CrUX API | **no access** (HTTP 403). **No field CWV for either site** | — |
| DataForSEO `on_page/lighthouse/live` | OK: 4 runs, mobile, Lighthouse 13.4.0, simulated throttling, **1 run per URL (lab data, variance ±10–20%)**. `noAiMode` returned an empty result, so **per-audit details (why Best Practices/SEO lose points) were not retrieved** | Scores, LCP/CLS/TBT/TTFB, weight |
| DataForSEO `on_page/instant_pages` | OK: 4 URLs, JS on | Meta, OG/Twitter, HTML errors, encoding |
| Raw HTML (python urllib; curl/WebFetch denied in this session) | OK | JSON-LD types/contents, canonical, hreflang, robots, sitemaps, llms.txt, headers |
| GSC | not used (not in scope; historically no access) | — |

Pages compared: `https://bixbit.io/en` vs `https://epicblockchain.io/`; `https://bixbit.io/en/firmwares/antminer` vs `https://epicblockchain.io/product/umc-os/` (both are the main Antminer firmware landing pages). Blog template: `/en/blog/post/immersion-cooling-or-how-to-stop-wasting-money-on-air` vs `/custom-firmware-vs-stock-firmware-antminer/`. Plus `/en/firmwares/whatsminer-series-m5x` and `/support/firmware-download/`.

## Measurements (mobile lab, 1 run)

| URL | Perf | BP | SEO | A11y | LCP | CLS | TBT | TTFB | Weight |
|---|---|---|---|---|---|---|---|---|---|
| bixbit.io/en | **0.87** | 0.77 | 0.85 | 0.93 | **2.75 s** | 0.001 | 365 ms | **37 ms** | 16.9 MB |
| epicblockchain.io/ | 0.47 | 0.92 | 0.92 | 0.86 | 51.5 s | n/a | 390 ms | 2263 ms | 32.7 MB |
| bixbit.io/en/firmwares/antminer | 0.56 | 0.73 | 0.92 | 0.90 | **42.1 s** | 0.005 | 758 ms | 43 ms | 23.8 MB |
| epicblockchain.io/product/umc-os/ | 0.55 | **1.00** | **1.00** | 0.93 | 9.0 s | 0.009 | 314 ms | 2340 ms | 2.0 MB |

Note: the June baseline CLS of 0.888 on /en **did not reproduce**. Lab CLS today is 0.001. That is lab, not field data, so confirm in CrUX once access is back.

## Comparison table

| # | Factor | BiXBiT | ePIC | Ahead | Prio | Fix |
|---|---|---|---|---|---|---|
| 1 | **Weight / LCP on the main firmware landing page** | `/en/firmwares/antminer`: 23.8 MB, LCP 42 s, TBT 758 ms. 8 raster images of 0.8–3.3 MB each (19 MB of media in total): `problematic-chips.png` 3.27 MB, `network-protection.png` 3.24, `profile-switcher.png` 3.17, `hero-laptop.webp` 2.56 (the likely LCP element), `hash-board-failure.png` 2.5, `profile-generation.png` 2.0 | UMC OS page: 2.0 MB, LCP 9.0 s | **ePIC** (on the page that matters most commercially) | **P0** | Re-encode the 8 PNGs to AVIF/WebP at ≤1600 px wide, target ≤150 KB each. Serve responsive `srcset` (640/1024/1600). Hero: `fetchpriority="high"` + `<link rel="preload" as="image" imagesrcset=…>`, no `loading="lazy"`. Everything below the fold gets `loading="lazy" decoding="async"` (only 2 of 58 `<img>` tags have lazy loading today) |
| 2 | **Clean HTML** | instant_pages reports 2 parse errors on both templates: "tag closed unexpectedly" (L45) and "**`<body>` tag placed twice**" (L46). Probably a shared layout partial | 0 errors | **ePIC** | **P1** | Find the duplicate `<body>` in the shared layout (around line 45–46 of the rendered HTML, likely where the GTM `<noscript>` iframe is inserted). A duplicate body can move `<head>` elements into the body when the parser recovers |
| 3 | **Social/share meta** | 5 OG tags. **`og:image` = favicon `android-chrome-512x512.png` on every page checked**. No `og:site_name`/`og:locale`. **0 Twitter tags** | 10 OG + 4–7 Twitter tags (`summary_large_image`, page-specific `og:image` with width/height, `article:modified_time`) | **ePIC** | **P1** | Page-specific `og:image` at 1200×630, plus `og:site_name`, `og:locale`, `twitter:card`. See snippet A |
| 4 | **JSON-LD entity graph** | Separate blocks with no `@id` links. `WebSite.url` = **the current page URL** (on m5x `WebSite.url` = `/en/firmwares/whatsminer-series-m5x`, which is a bug). `Organization.description` is cooling ad copy with an emoji (known from 09-16). No `WebPage` node, no `dateModified` on commercial pages | Yoast `@graph`: WebPage→WebSite→Organization linked by `@id`, `SearchAction`, `ImageObject` logo, `datePublished`/`dateModified` on every page | **ePIC** | **P1** | Switch to a single `@graph` with `@id` (snippet B). `WebSite.url` is always `https://bixbit.io/en`. Fix the Organization description |
| 5 | **Schema on the blog** | Article + Person ("BiXBiT content team", url → Instagram) + BreadcrumbList | Article + Person (author page URL) + **FAQPage** + WebPage with dates | **ePIC** (slightly) | P2 | Author must be a real Person with an `/en/author/...` page (E-E-A-T). Add FAQPage on posts that have a visible Q&A block |
| 6 | **Firmware schema: Antminer** | `/en/firmwares/antminer`: WebSite + Organization only (no SoftwareApplication, no Breadcrumb). **Correction to the 09-16 baseline:** `/en/firmwares/whatsminer-series-m5x` **does** have `SoftwareApplication` (softwareVersion "1.8.1" `[VERIFY]`) + BreadcrumbList | No SoftwareApplication/Product anywhere (UMC OS page included) | **BiXBiT** on Whatsminer; nobody on Antminer | **P1** | Bring the m5x template over to `/en/firmwares/antminer` (snippet C). Fill every fact field only after `[VERIFY]` |
| 7 | **Image sitemap** | 0 `image:` entries | 132 `image:image` entries in page-sitemap.xml (Yoast) | **ePIC** | P2 | Add `<image:image>` to sitemap-firmware/product/category. Images of firmware UIs and cooling systems can pull Google Images traffic |
| 8 | **Sitemap freshness/completeness** | category/product lastmod frozen at 2024-09-04; `/en/products/pdu`, `/en/asics-cooling*`, `/en/documentation` missing; duplicate + URL with a space (all from 09-16, still open) | Yoast: lastmod auto-updated (page-sitemap 2026-09-22), all pages included. Minus: `/404-2/` listed in the sitemap | **ePIC** | **P1** | Generate lastmod from the real `updated_at`. Add the 5 missing URLs. Fix the duplicate/space (details in `reports/sub/technical-seo-2026-09-16.md`) |
| 9 | **HSTS / Best Practices** | No `Strict-Transport-Security` header. Lighthouse BP 0.73–0.77 (reasons unknown: audit details not retrieved). Third-party: GTM, GA, Clarity, ContentSquare, LinkedIn Ads, Yandex Metrica | HSTS present. BP 0.92–1.00 | **ePIC** | P2 | nginx: `add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;`. Re-run LH with full audits. Most likely BP losses are console errors, deprecated APIs or third-party cookies (hypothesis, not a finding). Audit whether both Clarity **and** ContentSquare are needed |
| 10 | **HTML compression** | gzip | brotli | ePIC (marginal) | P3 | `brotli on; brotli_types text/html text/css application/javascript application/json image/svg+xml;` (needs the ngx_brotli module) |
| 11 | **Lighthouse SEO score** | /en 0.85, antminer 0.92 | 0.92 / 1.00 | ePIC | P2 | Audits not retrieved. Candidates to check: empty `alt=""` (instant_pages flags `no_image_alt` on both sites), link text, tap targets. Re-run with full output |
| 12 | Passage/Q&A structure of the firmware landing page (tech-GEO) | H2s are feature headings ("Stock vs BiXBiT", "Transparent Pricing") | 10 H2s phrased as questions ("What is ePIC UMC OS?", "What Antminer Models Does UMC OS Support?", "…vs. Other Custom Antminer Firmware") | **ePIC** | P2 (hand off to content/geo-ai) | Add a visible Q&A block + FAQPage to `/en/firmwares/antminer`. Content is the geo-ai/content-seo agents' area |

### Where BiXBiT is clearly ahead

| Factor | BiXBiT | ePIC |
|---|---|---|
| **TTFB** | 37–43 ms | 2263–2340 ms (WordPress without a page cache; Lighthouse flags it itself) |
| **Homepage LCP / Perf** | 2.75 s / 0.87 | 51.5 s / 0.47, 32.7 MB |
| **CLS** | 0.001–0.005 (lab) | 0.009 (UMC page) |
| SoftwareApplication schema | on Whatsminer pages | none |
| Multilingual (en/ru) | yes (hreflang only on /en/blog and /en/calc, P0 from 09-16) | monolingual en-US |
| Content volume in the sitemap | 106 en blog posts, newest 2026-09-09 | 34 posts |
| Thematic sitemaps | firmware/product/blog/documentation | WP default (post/page/tag/author) |
| Hygiene | — | `/support/firmware-download/` **has no H1**; `/404-2/` in the sitemap |
| llms.txt | 404 | 404 (tie; nobody has one) |

## Ready-made snippets (real URLs)

**A. OG/Twitter (template `/en/firmwares/antminer`; the image needs to be created)**
```html
<meta property="og:site_name" content="BiXBiT">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ru_RU">
<meta property="og:image" content="https://bixbit.io/site/og/firmware-antminer-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Antminer Firmware by BiXBiT – Your Custom Firmware">
<meta name="twitter:image" content="https://bixbit.io/site/og/firmware-antminer-1200x630.png">
```

**B. Base `@graph` (every page; `WebPage` changes per page)**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": "https://bixbit.io/en#organization",
     "name": "BiXBiT", "url": "https://bixbit.io/en",
     "logo": {"@type": "ImageObject", "url": "https://bixbit.io/site/images/logo_header.svg"},
     "description": "[VERIFY: neutral company description – firmware, AMS monitoring, PDU, immersion/hydro cooling for industrial Bitcoin mining]",
     "sameAs": ["https://www.facebook.com/bixbit.official", "https://www.instagram.com/bixbit.official/"]},
    {"@type": "WebSite", "@id": "https://bixbit.io/en#website", "url": "https://bixbit.io/en",
     "name": "BiXBiT", "inLanguage": "en", "publisher": {"@id": "https://bixbit.io/en#organization"}},
    {"@type": "WebPage", "@id": "https://bixbit.io/en/firmwares/antminer#webpage",
     "url": "https://bixbit.io/en/firmwares/antminer",
     "name": "Antminer Firmware by BiXBiT – Your Custom Firmware",
     "isPartOf": {"@id": "https://bixbit.io/en#website"},
     "about": {"@id": "https://bixbit.io/en/firmwares/antminer#software"},
     "breadcrumb": {"@id": "https://bixbit.io/en/firmwares/antminer#breadcrumb"},
     "inLanguage": "en", "dateModified": "[CMS updated_at]"}
  ]
}
```
(Keep the existing `sameAs` array in full. Only the first 2 items were visible in this check.)

**C. SoftwareApplication + Breadcrumb for `/en/firmwares/antminer` (add to the @graph from B)**
```json
{"@type": "SoftwareApplication", "@id": "https://bixbit.io/en/firmwares/antminer#software",
 "name": "BiXBiT firmware for Antminer", "applicationCategory": "Firmware",
 "operatingSystem": "Linux", "softwareVersion": "[VERIFY]",
 "publisher": {"@id": "https://bixbit.io/en#organization"},
 "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD",
            "description": "[VERIFY: dev fee 2.8% – confirmed on-page 2026-09-16, re-check]"}},
{"@type": "BreadcrumbList", "@id": "https://bixbit.io/en/firmwares/antminer#breadcrumb",
 "itemListElement": [
  {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://bixbit.io/en"},
  {"@type": "ListItem", "position": 2, "name": "Firmwares", "item": "https://bixbit.io/en/firmwares"},
  {"@type": "ListItem", "position": 3, "name": "Antminer", "item": "https://bixbit.io/en/firmwares/antminer"}]}
```
Do not add supported models or J/TH to the schema without `[VERIFY]`. Before merging: run the regression check (Rich Results Test + diff against the 09-16 baseline). Deliver it as a PR, never straight to prod.

## Not measured (stated honestly)
- Field CWV (CrUX) for both sites: no access.
- Individual Lighthouse audits (why BP/SEO lose points): the full response came back empty.
- Indexing coverage/crawl stats (GSC): not requested and not available.
- One Lighthouse run per URL. ePIC's 51 s LCP could be a slow-server outlier. The gap direction is consistent with TTFB (2.3 s), though.
- hreflang on ePIC: not applicable (monolingual).

## [VERIFY] for a human
- `softwareVersion: "1.8.1"` in the m5x schema: is it current?
- Dev fee for the `offers` in snippet C (2.8% / 2% M2x, from 09-16).
- The neutral Organization description in snippet B.
- The /en/ blog post with a Russian transliterated slug `/en/blog/post/kak-maynit-kriptovalyutu-i-pri-etom-vygodno-ispolzovat-teplo-1` (2022): check whether the content is actually English. If not, noindex it or pull it from the en sitemap.
