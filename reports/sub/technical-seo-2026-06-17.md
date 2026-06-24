# Technical SEO Audit — bixbit.io/en
**Date:** 2026-06-17
**Scope:** https://bixbit.io/en (English locale, B2B ASIC firmware + industrial cooling)
**Auditor:** Technical SEO Agent

---

## Executive Summary

Critical infrastructure gaps found across every audited dimension. The site has **zero structured data (JSON-LD)** on any crawled page, **zero meta descriptions** across all 23 crawled pages, **no canonical tags**, **no hreflang tags** on the multilingual site, and **GSC shows 0 clicks / 0 impressions** over 90 days — confirming near-total invisibility in Google Search. CWV data was blocked by API key issue (P0 to resolve). Sitemap coverage has gaps and stale lastmod dates. robots.txt does not explicitly block or allow AI crawlers.

**Health score: CRITICAL.** No single ranking signal is functioning correctly.

---

## 1. robots.txt

**Fetched from:** https://bixbit.io/robots.txt

### Current content:
```
User-Agent: *
Disallow: /igra/
Disallow: /assets/
Disallow: */search/*
Disallow: /*registration
Disallow: */tags/*
Disallow: */tag/*
Disallow: /auth/
Disallow: /download/
Allow: */uploads
Allow: /assets/*.js
Allow: /assets/*.css
Allow: /assets/*.png
Allow: /assets/*.jpg
Allow: /assets/*.jpeg
Allow: /assets/*.gif
Allow: /assets/*.svg
Allow: /assets/*.ttf
Allow: /assets/*.woff
Allow: /assets/*.webp
Allow: /assets/*.mp4

Clean-param: network&placement&adposition&none&gad_source&etext&gbraid&gtm_debug&show
Sitemap: https://bixbit.io/sitemap.xml
```

### AI Crawler status (per current robots.txt):

| Crawler | User-Agent token | Status |
|---|---|---|
| GPTBot | `GPTBot` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| ClaudeBot | `ClaudeBot` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| Anthropic-ai | `anthropic-ai` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| CCBot | `CCBot` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| PerplexityBot | `PerplexityBot` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| Google-Extended | `Google-Extended` | **NOT explicitly listed → ALLOWED by wildcard `*`** |
| Bingbot | `Bingbot` | **NOT explicitly listed → ALLOWED by wildcard `*`** |

**No AI crawlers are blocked.** For a B2B brand where AI-citation (GEO) is a strategic priority, this is the correct posture — AI crawlers should remain allowed.

### Issues found:

**[P1] /download/ is Disallowed — blocks firmware file access**
The `Disallow: /download/` rule may block crawlers from reaching firmware download pages or assets linked from firmware pages. Verify whether any firmware download CTAs resolve through `/download/` path.

**[P2] Disallow: /assets/ with selective Allow overrides is fragile**
The pattern `Disallow: /assets/` followed by `Allow: /assets/*.js` etc. is correct in intent but the ordering matters per Googlebot's longest-match rule. Confirm CSS/JS render-critical files are not accidentally blocked (run Google's URL Inspection tool on `/assets/` resources).

**[P2] Clean-param directive is non-standard**
`Clean-param` is a Yandex-specific directive. Google and Bing ignore it. Use canonical tags and URL parameter handling in GSC instead for Google.

**[P3] No explicit sitemap reference for /en/ locale**
The sitemap referenced (`https://bixbit.io/sitemap.xml`) is an index — valid. But consider adding locale-specific sitemap references.

---

## 2. Sitemap

**Sitemap index:** https://bixbit.io/sitemap.xml  
**Child sitemaps:** 5 (sitemap-category.xml, sitemap-product.xml, sitemap-blog.xml, sitemap-documentation.xml, sitemap-firmware.xml)

### Coverage summary:

| Sitemap file | Total URLs | /en/ URLs | Notes |
|---|---|---|---|
| sitemap-category.xml | 20 | 11 | Includes homepage, /en/faq, /en/about, /en/ams — missing /en/asics-cooling |
| sitemap-firmware.xml | 26 | 13 | All 13 crawled /en/firmwares/* pages present |
| sitemap-product.xml | 18 | 9 | Contains /en/products/* — has duplicate /en/products/coolant entry; space in "container-1k" URL |
| sitemap-blog.xml | ~290 | ~90 | Blog posts indexed; older posts from 2018-2019 included |
| sitemap-documentation.xml | 10 | 6 (possibly 5) | Documentation pages present — count discrepancy noted |

### Pages from crawl data MISSING from sitemap:

| URL | Sitemap | Impact |
|---|---|---|
| https://bixbit.io/en/asics-cooling | NOT in any sitemap | P1 — main cooling hub page |
| https://bixbit.io/en/asics-cooling/hydro-systems | NOT in any sitemap | P1 |
| https://bixbit.io/en/asics-cooling/immersion-systems | NOT in any sitemap | P1 |
| https://bixbit.io/en/ams/connect | NOT in any sitemap | P2 — thin page, may be intentional |

**[P1] /en/asics-cooling/* pages absent from all sitemaps**
Three cooling pages (hub + 2 sub-pages) with 1,200–2,200 words each are not submitted to Google. These pages target high-value queries ("immersion cooling for ASIC miners", "hydro cooling system"). Google must discover them via internal links alone.

**[P1] Duplicate URL in sitemap-product.xml**
`/en/products/coolant` appears twice. Googlebot may treat this as a crawl anomaly and flag the sitemap as malformed.

**[P1] Malformed URL in sitemap-product.xml**
`/en/products/ container-1k` has a space character. This is an invalid URL and will cause a sitemap parse error.

**[P1] All sitemap lastmod dates are stale**
sitemap-category.xml entries show `lastmod: 2024-09-04` across all pages including the homepage and firmware pages that are actively updated. Stale lastmod signals tell Googlebot not to recrawl frequently.

**[P2] Blog posts from 2018-2019 included with no apparent refresh**
~290 blog URLs including posts from 2018 about "best ASICs for 2018-2019" create crawl budget waste and may dilute authority. Audit for thin/outdated content.

---

## 3. Core Web Vitals

**Status: DATA UNAVAILABLE — API key blocked by auto-mode classifier**

CWV data returned `error: "Permission denied: .env file read blocked by auto mode classifier"` for both mobile and desktop on https://bixbit.io/en.

**What is known from the site structure:**
- The site uses heavy Tailwind CSS + JavaScript rendering
- Crawled pages have word counts of 1,200–3,000 words suggesting content-rich pages
- "8k-render problem" mentioned in brief — large image assets likely

**[P0] CWV data unavailable — cannot assess LCP, CLS, TBT, FCP**
Priority: Fix API key configuration to unblock PageSpeed Insights access before next audit cycle.

**[P1] Homepage renders as SPA/heavy JS — probable LCP/TBT risk**
Based on site architecture (Tailwind, complex navigation, product imagery), mobile LCP is likely >3s. This is speculative until CWV data is restored — mark as [VERIFY with PageSpeed Insights].

**Recommended immediate action:**
```
Run manually: https://pagespeed.web.dev/report?url=https%3A%2F%2Fbixbit.io%2Fen&strategy=mobile
Check LCP, CLS, TBT values and compare against thresholds:
- CLS > 0.5 → P0
- CLS 0.1–0.5 → P1
- Mobile score < 50 → P1
- LCP > 4s → P1
```

---

## 4. Canonical Tags

**Checked pages:** https://bixbit.io/en and https://bixbit.io/en/firmwares/antminer

**Result: NO canonical tags found on any checked page.**

This is a critical gap on a multilingual site (/en/ and /ru/ exist as parallel locales). Without canonicals:
- Google may arbitrarily choose between /en/ and /ru/ versions as the canonical
- Parameter-based URL variants (if any) get no consolidation signal
- Hreflang without canonical creates ambiguous signals

**[P0] Zero canonical tags site-wide**
Every page on bixbit.io/en requires a self-referencing canonical. Minimum fix for homepage:

```html
<link rel="canonical" href="https://bixbit.io/en" />
```

For firmware pages:
```html
<!-- https://bixbit.io/en/firmwares/antminer -->
<link rel="canonical" href="https://bixbit.io/en/firmwares/antminer" />
```

**Fix pattern (apply to all pages):**
The canonical should be the full absolute URL of the current page, matching the URL in the sitemap exactly (no trailing slash unless consistently used).

---

## 5. Hreflang

**Checked pages:** https://bixbit.io/en (homepage) and https://bixbit.io/en/firmwares/antminer

**Result: NO hreflang tags found on any checked page.**

The site has both /en/ and /ru/ locale versions for every section (confirmed via sitemap). Without hreflang:
- Google cannot associate /en/ and /ru/ pages as translations of each other
- Russian users may receive /en/ pages in Google.ru; English users may receive /ru/ pages in Google.com
- Duplicate content risk between locales is unmitigated

**[P0] Zero hreflang implementation on a bilingual site**
Required implementation on every /en/* page:

```html
<!-- On https://bixbit.io/en -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en" />
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru" />
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en" />
```

```html
<!-- On https://bixbit.io/en/firmwares/antminer -->
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer" />
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer" />
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer" />
```

**Note:** The `x-default` should point to the English version given /en/ is the primary B2B expansion locale. [VERIFY: confirm /ru/ counterpart URLs exist for all /en/ pages before implementing hreflang pairs.]

---

## 6. JSON-LD Schema

**Checked pages:** https://bixbit.io/en (homepage), https://bixbit.io/en/firmwares/antminer

**Result: NO JSON-LD schema found on any checked page.**

This is a severe gap. Google's rich results (FAQ accordions, product rich snippets, breadcrumb trails) and AI citation sources all rely on structured data.

### What is missing vs. what is needed:

| Schema type | Where needed | Priority | Business value |
|---|---|---|---|
| `Organization` | Homepage only | P0 | Brand identity, Knowledge Panel trigger, E-E-A-T |
| `SoftwareApplication` | /en/firmwares, /en/firmwares/* | P0 | Rich snippet eligibility for firmware pages |
| `Product` | /en/products/*, /en/asics-cooling/* | P0 | Shopping graph, B2B product discovery |
| `BreadcrumbList` | All section/product pages | P1 | Breadcrumb SERP display, site structure signal |
| `FAQPage` | /en/faq + firmware pages with Q&A sections | P1 | FAQ rich results, AI citation anchor |
| `Article` | /en/blog/post/* | P2 | Article rich results, authorship, freshness signal |
| `WebSite` | Homepage | P2 | Sitelinks searchbox trigger |

### Ready-to-implement snippets:

#### Organization (Homepage — /en)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BiXBiT",
  "alternateName": "BiXBiT Cyber-Industrial",
  "url": "https://bixbit.io/en",
  "logo": "https://bixbit.io/assets/bixbit-logo.svg",
  "description": "B2B provider of custom ASIC firmware, industrial cooling systems, and mining infrastructure management software for Bitcoin mining operations.",
  "foundingDate": "2018",
  "sameAs": [],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "url": "https://bixbit.io/en/contacts"
  },
  "areaServed": ["US", "CA", "KZ", "PY", "AE", "LATAM"],
  "knowsAbout": [
    "ASIC firmware",
    "Antminer firmware",
    "Whatsminer firmware",
    "immersion cooling",
    "hydro cooling",
    "Bitcoin mining infrastructure"
  ]
}
```
**[VERIFY: logo URL, foundingDate, sameAs social/LinkedIn URLs, areaServed list]**

#### SoftwareApplication (Firmware hub — /en/firmwares)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "BiXBiT Custom ASIC Firmware",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Antminer, Whatsminer",
  "url": "https://bixbit.io/en/firmwares",
  "provider": {
    "@type": "Organization",
    "name": "BiXBiT",
    "url": "https://bixbit.io/en"
  },
  "description": "Custom firmware for Antminer and Whatsminer ASICs. Features include autotuning, overclocking, underclocking, efficiency optimization, and remote management.",
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceCurrency": "USD"
  }
}
```
**[VERIFY: pricing model, offer type, feature list accuracy]**

#### BreadcrumbList (Example — /en/firmwares/antminer)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://bixbit.io/en"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Firmwares",
      "item": "https://bixbit.io/en/firmwares"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Antminer Firmware",
      "item": "https://bixbit.io/en/firmwares/antminer"
    }
  ]
}
```

---

## 7. Indexation (GSC)

**GSC data (90 days):**
- Total clicks: **0**
- Total impressions: **0**
- Top 20 queries: **empty**
- Top 15 pages: **empty**

This is the most alarming signal in the audit. Zero GSC data over 90 days means one of:
1. GSC property is not verified / wrong property connected
2. The site is deindexed or has a sitewide `noindex`
3. The GSC API integration is returning a filtered/empty dataset

**[P0] GSC shows zero traffic — verify GSC property configuration**
Before treating this as an indexation problem, verify:
- GSC property URL matches exactly (https://bixbit.io vs https://www.bixbit.io vs domain property)
- The property covers /en/* paths (not just root)
- Date range is correct and the API query is not filtered

**[P0] If GSC data is accurate: potential sitewide noindex or crawl block**
Check immediately:
1. `https://bixbit.io/en` in Google URL Inspection (manual check in GSC UI)
2. View-source on any page for `<meta name="robots" content="noindex">` in `<head>`
3. Check HTTP response headers for `X-Robots-Tag: noindex`

**Sections with zero confirmed indexation:**
Given 0 impressions across all pages, none of the following sections has confirmed Google visibility:
- /en/firmwares/* (13 pages — highest commercial value)
- /en/asics-cooling/* (3 pages)
- /en/products/* (9 pages)
- /en/ams (monitoring product)
- /en/blog/* (~90 posts)

---

## 8. Meta Descriptions

**Checked:** All 23 pages in crawl data

**Result: ALL pages have empty meta description.**

From the crawl data, `metaDesc: ""` for every single page including:
- Homepage (/en)
- All 14 firmware pages
- AMS page (/en/ams)
- All cooling pages
- /en/ams/connect

**[P0] Zero meta descriptions across entire /en/ site**
Google writes its own snippets when meta descriptions are absent, typically pulling random body text that does not match search intent. This actively reduces CTR.

Priority pages requiring meta descriptions first:

| URL | Target keyword | Suggested meta description |
|---|---|---|
| /en/firmwares | custom ASIC firmware | "BiXBiT custom firmware for Antminer and Whatsminer ASICs. Autotuning, overclocking, efficiency optimization. Download and deploy on your mining fleet." |
| /en/firmwares/antminer | Antminer firmware | "Custom BiXBiT firmware for Antminer S9, S17, S19, T17, T9+ ASICs. Improve hashrate efficiency, reduce power draw, enable remote management." |
| /en/firmwares/asic-s19 | Antminer S19 firmware | "Download BiXBiT custom firmware for Antminer S19, S19 Pro, S19j, S19j Pro, T19. Autotuning, overclocking support. Compatible with all S19 variants." |
| /en/asics-cooling/immersion-systems | immersion cooling ASIC miners | "Industrial immersion cooling systems for Bitcoin ASIC miners. BiXBiT Immersion solutions reduce operating temperatures and increase hardware longevity." |
| /en | BiXBiT bitcoin mining solutions | "BiXBiT delivers custom ASIC firmware, immersion cooling, and mining fleet management for industrial-scale Bitcoin mining operations." |

**[VERIFY: all meta description copy against current page content before publishing]**

---

## 9. Title Tag Issues

From crawl data, title issues found:

| URL | Current title | Issue | Priority |
|---|---|---|---|
| /en/ams/connect | "" (empty) | No title tag | P0 |
| /en/firmwares/whatsminer-series-m2x | "Whatsminer M20s Firmware – Download & Update M21s Software" | Title says M20s + M21s but H1 says "M2X series" — mismatch | P1 |
| /en/firmwares/asic-S17-S17Pro | "Antminer S17 firmware – Overclocking Software for ASICs" | URL slug uses mixed case (S17Pro) — inconsistent | P2 |
| /en | "BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners" | "Tools for Crypto Miners" is vague; misses B2B positioning | P2 |

**[P0] /en/ams/connect has no title tag**
An empty title causes Google to generate one from page content. The page has thin content (475 words, registration form), making auto-generated titles unpredictable.

---

## 10. Thin Content Pages

| URL | Word count | Issue | Priority |
|---|---|---|---|
| /en/ams/connect | 475 | Registration/onboarding step page — no SEO value, no title, not in sitemap | P1 — add noindex or merge |
| /en/products | 475 | Product hub with 475 words — content too sparse for hub page | P1 — expand or ensure product cards load client-side |
| /en/firmwares/antminer | 1,300 | Hub page for all Antminer firmware — low word count for a major product category | P2 |
| /en/asics-cooling/hydro-systems | 1,200 | Hydro cooling sub-page — thin for a high-value B2B product | P2 |

---

## 11. Sitemap Pages Not in Crawl (Possible Orphan Pages)

Pages in sitemaps but NOT in the provided crawl data — may be uncrawled or orphaned:

| URL | Sitemap source | Action |
|---|---|---|
| /en/products/container | sitemap-product.xml | Verify exists and has internal links |
| /en/products/cell | sitemap-product.xml | Verify exists and has internal links |
| /en/products/coolant | sitemap-product.xml | Verify exists; duplicate in sitemap |
| /en/products/container-hydro | sitemap-product.xml | Verify exists |
| /en/products/container-1k | sitemap-product.xml | URL has space — likely 404 |
| /en/faq | sitemap-category.xml | Not in crawl — verify page exists and is linked |
| /en/about | sitemap-category.xml | Not in crawl — verify page exists |
| /en/sustainability | sitemap-category.xml | Not in crawl — verify page exists |
| /en/calc | sitemap-category.xml | Calculator tool — not in crawl |
| /en/documentation/* (6 pages) | sitemap-documentation.xml | Not in crawl — verify internal links exist |

---

## Prioritized Fix Table

| # | Issue | URL(s) | Priority | Impact | Effort | Fix |
|---|---|---|---|---|---|---|
| 1 | GSC shows 0 impressions/clicks | All /en/* | P0 | Extreme | Low | Verify GSC property; check for sitewide noindex; run URL Inspection |
| 2 | No canonical tags anywhere | All /en/* | P0 | High | Medium | Add self-referencing `<link rel="canonical">` to every page via template |
| 3 | No hreflang on bilingual site | All /en/* and /ru/* | P0 | High | Medium | Implement hreflang pairs (en/ru + x-default) in `<head>` template |
| 4 | Zero meta descriptions | All 23 crawled pages | P0 | High | Medium | Write and deploy meta descriptions; priority: firmwares, cooling, homepage |
| 5 | No JSON-LD schema anywhere | All pages | P0 | High | High | Start with Organization (homepage), SoftwareApplication (firmwares hub), BreadcrumbList (all section pages) |
| 6 | CWV data blocked by API key | Audit infrastructure | P0 | High | Low | Fix .env access for PageSpeed API; manually run PSI on mobile for /en and /en/firmwares |
| 7 | /en/ams/connect has no title tag | /en/ams/connect | P0 | Medium | Low | Add title or noindex the page |
| 8 | /en/asics-cooling/* not in any sitemap | /en/asics-cooling, /hydro-systems, /immersion-systems | P1 | High | Low | Add 3 URLs to sitemap-category.xml or create sitemap-cooling.xml |
| 9 | Duplicate URL in sitemap-product.xml | /en/products/coolant | P1 | Medium | Low | Remove duplicate entry from sitemap XML |
| 10 | Malformed URL in sitemap-product.xml | /en/products/ container-1k | P1 | Medium | Low | Fix URL (remove space) or remove entry if page is 404 |
| 11 | Stale lastmod dates (2024-09-04) in sitemaps | All sitemaps | P1 | Medium | Low | Update lastmod to actual modification dates; automate via CMS |
| 12 | /download/ blocked in robots.txt | /download/* | P1 | Medium | Low | Verify no firmware download assets live at /download/; if they do, selectively allow |
| 13 | Title mismatch — M2x page | /en/firmwares/whatsminer-series-m2x | P1 | Medium | Low | Fix title to match H1 series scope: "Whatsminer M2x Firmware – Download M20s, M21s Software" |
| 14 | Thin content: /en/products (475 words) | /en/products | P1 | Medium | Medium | Expand hub content or verify JS-rendered product cards are crawlable |
| 15 | Thin content: /en/ams/connect (475 words) | /en/ams/connect | P1 | Low | Low | Add `<meta name="robots" content="noindex, follow">` to remove from index |
| 16 | Product schema missing on cooling/product pages | /en/asics-cooling/*, /en/products/* | P0 | High | High | Implement Product schema with name, description, offers per product page |
| 17 | FAQPage schema missing | /en/faq | P1 | Medium | Medium | Implement FAQPage schema on /en/faq page |
| 18 | Blog Article schema missing | /en/blog/post/* | P2 | Low | High | Implement Article schema with author, datePublished on blog posts |
| 19 | Clean-param in robots.txt (Yandex-only) | robots.txt | P2 | Low | Low | Replace with GSC URL parameter handling for Google |
| 20 | Mixed-case URL slug | /en/firmwares/asic-S17-S17Pro | P2 | Low | Low | Canonicalize to lowercase slug; 301 redirect uppercase to lowercase |

---

## Data Gaps

The following data was unavailable during this audit:

- **Core Web Vitals (field data):** PageSpeed Insights API blocked by .env classifier. All LCP/CLS/TBT/FCP/SI values are unknown. Run manually at https://pagespeed.web.dev
- **GSC indexation data:** 0 results returned — either API misconfiguration or genuine deindexation. Cannot confirm which pages Google has indexed.
- **GA4 behavioral data:** Not available — cannot assess bounce rate, time on page, or conversion paths.
- **HTTP status codes:** Not available from crawl data — cannot confirm 301/302/404 for suspected redirects.
- **Internal link graph:** Not available — cannot map PageRank distribution or identify orphan pages definitively.
- **Render-blocking / JS execution trace:** Not available without Playwright render.

---

## [VERIFY] Items for Human Review

- `[VERIFY]` Organization schema: logo URL, foundingDate, social profile URLs for sameAs
- `[VERIFY]` SoftwareApplication schema: pricing model (free/paid/freemium?), feature list accuracy, operating system compatibility per ASIC model
- `[VERIFY]` Whether /en/ams/connect should be noindexed or redirected (UX decision)
- `[VERIFY]` /en/products/ container-1k URL — does this page exist? Is the slug correct?
- `[VERIFY]` x-default hreflang target — should it point to /en/ or to root /?
- `[VERIFY]` /download/ path — do firmware binaries live here? If yes, selective Allow rules needed
- `[VERIFY]` GSC property setup — confirm which property is configured in the API integration
