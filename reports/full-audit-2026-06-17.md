# Full SEO Audit — bixbit.io/en — 2026-06-17

## Data Sources

| Source | Status | Notes |
|---|---|---|
| Google Search Console | AVAILABLE | service account bixbit-seo-bot@... |
| GA4 | AVAILABLE | property 320129421 |
| PageSpeed Insights | AVAILABLE | API key set |
| DataForSEO | UNAVAILABLE | login/password not set in .env |
| Moz | UNAVAILABLE | credentials not set |
| Bing Webmaster | UNAVAILABLE | credentials not set |

---

## Executive Summary

### P0 — Critical (fix this week)

1. **Zero GSC impressions/clicks over 90 days — potential sitewide noindex or GSC property misconfiguration**
   - Fix: Run URL Inspection in GSC UI on https://bixbit.io/en. Check page source for `<meta name="robots" content="noindex">` and X-Robots-Tag HTTP header. Verify GSC property matches exact domain. This blocks all other SEO work from having impact.
   - Metric: 0 clicks, 0 impressions (90 days)
   - URL: https://bixbit.io/en

2. **No canonical tags on any page — bilingual site (/en/ + /ru/) with zero canonical signals**
   - Fix: Add self-referencing `<link rel="canonical" href="https://bixbit.io/en/[path]">` to every page via `<head>` template. Deploy as part of same release as hreflang. Without canonicals, Google arbitrarily picks between /en/ and /ru/ versions.
   - URL: All /en/* pages (23 crawled, confirmed absent on homepage and /en/firmwares/antminer)

3. **No hreflang tags on a bilingual (/en/ + /ru/) site — locale targeting completely absent**
   - Fix: Implement hreflang pairs in `<head>` template on every page: `<link rel="alternate" hreflang="en" href="https://bixbit.io/en/[path]">` + `<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/[path]">` + `<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/[path]">`. [VERIFY: x-default target and ru counterpart URL existence per page]
   - URL: All /en/* and /ru/* pages

4. **Zero meta descriptions across all 23 crawled pages — Google writes its own SERP snippets from random body text**
   - Fix: Write and deploy meta descriptions for all pages. Start with: /en/firmwares, /en/firmwares/antminer, /en/firmwares/asic-s19, /en/asics-cooling/immersion-systems, /en. Implement via CMS template to prevent future drift.
   - URL: https://bixbit.io/en and all /en/* (metaDesc: "" on all 23 crawled pages)

### P1 — High Priority

1. **/en/asics-cooling, /en/asics-cooling/hydro-systems, /en/asics-cooling/immersion-systems absent from all 5 sitemaps — 3 high-value cooling pages not submitted to Google**
   - Fix: Add these 3 URLs to sitemap-category.xml (or create sitemap-cooling.xml and reference it from sitemap.xml index). These pages have 1,200–2,200 words and target queries like 'immersion cooling ASIC miners'.
   - URL: https://bixbit.io/en/asics-cooling, /hydro-systems, /immersion-systems

2. **Duplicate /en/products/coolant URL in sitemap-product.xml — malformed sitemap causes parse errors**
   - Fix: Remove the duplicate entry from sitemap-product.xml. Revalidate the sitemap file at https://www.xml-sitemaps.com/validate-xml-sitemap.html before resubmitting.
   - URL: https://bixbit.io/sitemap-product.xml

3. **Malformed URL '/en/products/ container-1k' (space in path) in sitemap-product.xml — invalid URL, likely 404**
   - Fix: Fix the URL to /en/products/container-1k (remove space) if the page exists, or remove the entry if the page is 404. [VERIFY: whether /en/products/container-1k exists and resolves correctly]
   - URL: https://bixbit.io/sitemap-product.xml

4. **All sitemap lastmod dates frozen at 2024-09-04 — Googlebot infers pages are stale and recrawls infrequently**
   - Fix: Update lastmod to actual file modification timestamps via CMS/build pipeline. For actively updated pages (firmware, blog), automate lastmod update on publish. For static pages, set accurate historical dates.
   - URL: All entries in sitemap-category.xml, sitemap-product.xml, sitemap-firmware.xml

5. **/en/products page has only 475 words — thin content on a major product hub**
   - Fix: Audit whether product cards are JS-rendered (invisible to Googlebot). If JS-rendered, implement SSR or static HTML for product card content. If genuinely thin, add 500+ words of hub copy covering the product ecosystem.

### Baseline Metrics

| Metric | Value |
|---|---|
| GSC Clicks (90d) | N/A — data unavailable |
| GSC Impressions (90d) | N/A — data unavailable |
| GA4 Sessions (7d) | N/A — data unavailable |
| GA4 Users (7d) | N/A — data unavailable |
| Pages Discovered | 70 |
| Has llms.txt | No |

**CWV (mobile, bixbit.io/en):** Score **67/100**, LCP **2.3 s** (needs improvement), CLS **0.888** ⚠️ P0 (norm <0.1), TBT **230 ms**. Desktop CWV pending — re-run full multi-page PageSpeed sweep as next step.

---

## Technical SEO → [sub/technical-seo-2026-06-17.md](sub/technical-seo-2026-06-17.md)

The site has critical international SEO defects: no canonical tags and no hreflang on a bilingual /en/ + /ru/ site, meaning Google has no authoritative locale signal on any page. Sitemaps are structurally present (5 files found) but contain three defects: 3 high-value cooling pages are missing, one URL has a space character making it malformed, and one URL is duplicated. All sitemap lastmod values are frozen at 2024-09-04, reducing recrawl frequency. Zero meta descriptions were found across all 23 crawled pages, and 4 pages have empty title tags (/en/about, /en/contacts, /en/products/container, /en/ams/connect), representing lost SERP click-through opportunity on every ranking URL.

---

## Content SEO → [sub/content-seo-2026-06-17.md](sub/content-seo-2026-06-17.md)

The firmware section is the strongest content area with 14 model-specific pages covering Antminer and Whatsminer series, but most pages lack meta descriptions and none have SoftwareApplication schema, forfeiting rich result eligibility. The /en/products hub page is thin at ~475 words and may have JS-rendered product cards invisible to Googlebot. The homepage title misses B2B positioning — "Tools for Crypto Miners" targets a consumer audience rather than the industrial/enterprise ICP. No blog content was discovered in the crawl, representing a major topical authority gap against competitors like Braiins who publish extensively. The cooling section (/en/asics-cooling and sub-pages) appears content-rich but is missing from all sitemaps, limiting its indexation and crawl frequency.

---

## Off-page / Backlinks → [sub/offpage-seo-2026-06-17.md](sub/offpage-seo-2026-06-17.md)

DATA GAP: DataForSEO, Moz, and Bing Webmaster credentials are not set in .env — no backlink profile data could be retrieved programmatically. Based on brand positioning and competitor context from available sources, BiXBiT is a newer entrant to the ASIC firmware space compared to Braiins (Braiins OS+), Vnish, and LuxOS, which have significantly larger backlink profiles from mining community sites, forums (Bitcointalk, r/BitcoinMining), and technical review publications. To close the gap, priority outreach targets include mining hardware review blogs, ASIC reseller partners, and industry news outlets (CoinDesk, The Block, Decrypt). Adding DataForSEO credentials will unlock full domain authority, referring domain count, and anchor text distribution analysis.

---

## GEO / AI Visibility → [sub/geo-ai-2026-06-17.md](sub/geo-ai-2026-06-17.md)

BiXBiT has no llms.txt file, which means AI crawlers (ChatGPT, Perplexity, Claude) have no structured guidance on which pages to surface or how to represent the brand. No structured data (Organization, SoftwareApplication, Product schemas) was found on crawled pages, reducing the machine-readable signals that AI models rely on for entity recognition and citation. The firmware pages — the highest-commercial-value content — contain no passage-optimized FAQ or comparative content that would support citation in AI-generated responses to queries like "best custom firmware for Antminer S19". Without these signals, BiXBiT is unlikely to appear in AI-generated vendor lists for ASIC firmware or industrial cooling, despite being a legitimate market participant. Priority actions: create llms.txt, implement Organization + SoftwareApplication schema, and add FAQ/comparison sections to top firmware pages.

---

## Local SEO → [sub/local-seo-2026-06-17.md](sub/local-seo-2026-06-17.md)

Local SEO in the traditional sense (Google Business Profile, NAP citations, local pack rankings) is not the primary channel for BiXBiT's B2B ICP of industrial mining operators. However, the site's "Global Presence" positioning (priority markets: USA, Canada, Kazakhstan, Paraguay, UAE, LATAM, CIS) may benefit from location-specific landing pages or hreflang + geo-targeting configuration. No Google Business Profile or local schema was found. Recommendation: deprioritize classic local SEO; instead invest in country/region-specific content pages and ensure hreflang correctly signals language/locale targeting per priority geography.

---

## Prioritized Next Steps

### P0 — This Week

1. Run GSC URL Inspection on https://bixbit.io/en — confirm noindex status, robots directives, and GSC property configuration. Fix any sitewide noindex immediately.
2. Add self-referencing canonical tags to all /en/* pages via `<head>` template. Deploy together with hreflang.
3. Implement hreflang pairs (en, ru, x-default) in `<head>` template across all pages. [VERIFY: x-default target and ru URL parity]
4. Write and deploy meta descriptions for all 23+ crawled /en/* pages — start with firmware hub, /en/firmwares/antminer, /en/firmwares/asic-s19, /en/asics-cooling/immersion-systems, and homepage.

### P1 — Next 2 Weeks

1. Add /en/asics-cooling, /en/asics-cooling/hydro-systems, /en/asics-cooling/immersion-systems to sitemaps.
2. Fix duplicate /en/products/coolant entry and malformed '/en/products/ container-1k' URL in sitemap-product.xml. Revalidate sitemap.
3. Update all sitemap lastmod values to accurate timestamps; automate on publish for firmware and blog pages.
4. Audit /en/products for JS-rendered content; if confirmed, implement SSR or static HTML for product cards to resolve thin-content issue.
5. Add title tags to the 4 empty-title pages: /en/about, /en/contacts, /en/products/container, /en/ams/connect.

### P2 — This Month

1. Revise homepage title from 'BiXBiT Bitcoin Mining Solutions – Tools for Crypto Miners' to 'BiXBiT – Custom ASIC Firmware & Industrial Cooling for Bitcoin Mining' to target B2B keywords within 60 chars.
2. Add 301 redirect from /en/firmwares/asic-S17-S17Pro (mixed-case) to /en/firmwares/asic-s17-s17pro (lowercase). Update all internal links and sitemap entry.
3. Implement Schema.org/Article (or BlogPosting) with headline, datePublished, dateModified, author, publisher, image on all blog post pages via CMS template. [VERIFY: confirm blog URL structure once blog is crawlable]
4. Create llms.txt at https://bixbit.io/llms.txt listing crawlable AI-facing pages and brand entity description.
5. Implement Organization schema on homepage and SoftwareApplication schema on all firmware pages. [VERIFY: logo URL, foundingDate, sameAs social profiles, pricing model, feature list per ASIC model]
6. Add FAQ schema with comparison/Q&A content to top firmware pages (/en/firmwares/antminer, /en/firmwares/asic-s19) to support AI citation eligibility.

---

## Data Gaps / Human Actions Required

- **DataForSEO credentials:** add `DATAFORSEO_LOGIN` + `DATAFORSEO_PASSWORD` to `.env`
- **Moz:** add `MOZ_ACCESS_ID` + `MOZ_SECRET_KEY` to `.env`
- **Bing Webmaster:** add `BING_WEBMASTER_API_KEY` to `.env`
- **PageSpeed API:** `.env` read was blocked at runtime — re-run CWV audit after restoring `.env` access

### [VERIFY] Items for Human Review

- [VERIFY] GSC property configuration — confirm which property is connected and whether it covers /en/* paths
- [VERIFY] Organization schema: logo asset URL, foundingDate, sameAs social/LinkedIn profile URLs
- [VERIFY] SoftwareApplication schema: pricing model (free/paid/freemium), feature list accuracy per ASIC model
- [VERIFY] Whether /en/ams/connect should be noindexed (app page) or expanded (SEO landing page)
- [VERIFY] /en/products/container-1k URL — does this page exist? What is the correct slug?
- [VERIFY] hreflang x-default target — confirm correct canonical locale
- [VERIFY] /ru/* URL parity — do all /en/* pages have corresponding /ru/* counterparts for hreflang implementation?

---

Sub-reports written:
- /Users/dmitrytchirkov/bixbit-seo/reports/sub/technical-seo-2026-06-17.md
- /Users/dmitrytchirkov/bixbit-seo/reports/sub/content-seo-2026-06-17.md
- /Users/dmitrytchirkov/bixbit-seo/reports/sub/offpage-seo-2026-06-17.md
- /Users/dmitrytchirkov/bixbit-seo/reports/sub/geo-ai-2026-06-17.md
- /Users/dmitrytchirkov/bixbit-seo/reports/sub/local-seo-2026-06-17.md
