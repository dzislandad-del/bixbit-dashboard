# Technical Gap: BiXBiT (bixbit.io/en) vs EMCD (emcd.io), 2026-09-25

> Scope: only the **noticeable** technical advantages EMCD has, plus where BiXBiT is ahead.
> I did not re-measure BiXBiT. Its numbers come from `reports/sub/competitor-gap-ePIC-tech-2026-09-25.md` and `data/dfs-lighthouse-instant-bixbit-vs-epic-2026-09-25.json`.
> EMCD snapshot: `data/dfs-lighthouse-instant-emcd-2026-09-25.json`.
> BiXBiT URL structure: `data/site-structure.md` (real, crawled 2026-09-16).

## Data sources (status)

| Source | Status |
|---|---|
| DataForSEO `lighthouse/live/json` (mobile, LH 13.4.0, simulated, **1 run per URL**, lab) | OK for 2 URLs: `/` and `/fw/`. I did not run Lighthouse on the article |
| DataForSEO `instant_pages` (JS on) | OK: `/`, `/fw/`, `robots.txt`, `sitemap.xml` (status and size only), `llms.txt` |
| DataForSEO `task_post` crawl (40 pages, JS off, Googlebot UA) + `raw_html` | OK. hreflang, canonical and JSON-LD came from the raw HTML for `/`, `/fw/` and `/articles/mining/hidden-mining-how-to-detect-and-remove/` |
| curl | **no access** (denied). I did not work around it |
| HTTP response headers (HSTS etc.) for EMCD | **no access** through DataForSEO. Not compared |
| Sitemap contents (URL count, lastmod, image:) for EMCD | **not retrieved**. I only know it returns 200 and is 233 KB |
| PageSpeed API / CrUX | **no access** (500 / 403). No field CWV |
| GSC | not applicable to a competitor |

## Measurements (mobile lab, 1 run)

| URL | Perf | BP | SEO | A11y | LCP | CLS | TBT | TTFB | Weight |
|---|---|---|---|---|---|---|---|---|---|
| bixbit.io/en | **0.87** | 0.77 | 0.85 | **0.93** | **2.75 s** | **0.001** | **365 ms** | **37 ms** | 16.9 MB |
| emcd.io/ | 0.31 | 0.77 | 0.85 | 0.83 | 16.3 s | 0.096 | 4987 ms | 301 ms | 10.9 MB |
| bixbit.io/en/firmwares/antminer | **0.56** | 0.73 | 0.92 | 0.90 | 42.1 s | 0.005 | **758 ms** | **43 ms** | 23.8 MB |
| emcd.io/fw/ | 0.34 | 0.77 | 0.92 | 0.85 | **13.2 s** | 0.005 | 8504 ms | 406 ms | **6.9 MB** |

EMCD runs on Nuxt behind Cloudflare. JS main-thread work is 17–18 s, and its third-party load (FullStory, Segment, Intercom, AppsFlyer, Yandex, GTM) blocks rendering. BiXBiT's weak spot is media weight. EMCD's weak spot is JavaScript.

## Comparison table

| # | Factor | BiXBiT | EMCD | Ahead | Prio | Fix |
|---|---|---|---|---|---|---|
| 1 | **hreflang coverage** (NEW vs ePIC) | Only 2 of 10+ templates have hreflang (`/en/blog`, `/en/calc`). The homepage, firmware hub, antminer, ams, pdu, cooling, faq and docs have none, even though `/ru` counterparts exist (09-16) | Hreflang on **every page checked** (home, `/fw/`, article) with a full reciprocal set and `x-default` | **EMCD** | **P0** (already P0 since 09-16; EMCD confirms it is standard in the niche) | Add hreflang from the layout for every template with a `/ru` counterpart. Snippet A. Only list pairs whose translation actually exists (build the map from the CMS, not by pattern) |
| 2 | **Localized slugs + article-to-article mapping** (NEW) | Blog hreflang points en↔ru, but the RU blog also has transliterated slugs under /en/ (see the ePIC [VERIFY] item) | Each translation has its own localized slug (`/ru/articles/majning/chto-takoie-skrytyi-mainier/`, `/pt/articles/minerao/...`) and hreflang links the exact article counterparts | **EMCD** | P1 | Keep an explicit `translation_of` relation in the CMS. Generate hreflang from that relation, not from slug matching. Pull RU-language posts out of `/en/` (noindex or remove them from the en sitemap) |
| 3 | **Language scale** (NEW) | 2 locales (en, ru) | 5 locales in the hreflang cluster: en, ru, pt-BR, es-ES, zh-CN. Also `/de/ /fr/ /id/` (see "EMCD mistakes") | EMCD | P2 (strategy; hand off to international-seo) | PT-BR and ES map directly onto the priority LatAm/Paraguay markets in CLAUDE.md. Start with `/es/firmwares/antminer` and `/pt/...` for the firmware hub only, and only with human translation. Tech facts in translations are `[VERIFY]` |
| 4 | **Language region codes** | `en` / `ru` | Pairs `en` + `en-US`, `ru` + `ru-RU`, etc. | none | P3 | Not needed. A language code alone is enough when there is one version per language. EMCD's duplicated pairs and doubled `x-default` add no value |
| 5 | **og:locale / og:locale:alternate** | Missing (ePIC P1) | `og:locale=en_US` + `og:locale:alternate=ru_RU` on home and `/fw/` | EMCD | P2 | Already in snippet A of the ePIC report (`og:locale`, `og:locale:alternate`) |
| 6 | **Social meta on the homepage** | `og:image` is the favicon, 0 Twitter tags | Home: `og-en.png` 1024×512, 5 Twitter tags, `summary_large_image` | EMCD (home only) | P1 (already open in the ePIC report) | Same fix as ePIC #3 |
| 7 | **Article author** (NEW nuance) | Person "BiXBiT content team", url points to Instagram | Person with a real name ("Mikael Abgaryan"), no url | EMCD (slightly) | P2 | A real author plus an `/en/author/{slug}` page with a `url`/`sameAs` (LinkedIn). That beats both ePIC and EMCD |
| 8 | **Weight of the firmware landing page** | 23.8 MB, LCP 42 s | 6.9 MB, LCP 13.2 s | EMCD (on weight/LCP; worse on TBT/Perf score) | **P0** (already open) | ePIC #1: re-encode the 8 PNGs to AVIF/WebP, add `srcset`, preload the hero |
| 9 | **Clean HTML** | Duplicate `<body>` + 1 parse error | 0 errors (instant_pages), 1 `<body>` | EMCD | P1 (already open) | ePIC #2 |

### EMCD mistakes (do not copy these)
- **Article schema is invalid in its details.** `datePublished: "9/2/2026"` is not ISO 8601, and `article:published_time` has the same problem. There is no `dateModified`. `publisher.logo.url` = `/logo.svg` and `mainEntityOfPage.@id` are relative URLs. Google can drop the date from rich results.
- **Home and `/fw/` have no JSON-LD at all**, only microdata `Organization` in the footer. `/fw/` has no SoftwareApplication, Product or Breadcrumb.
- `/fw/`: `og:image=""`, `twitter:image=""`, and a malformed `twitter:card` (`content='summary_large_image'` inside the value). `og:site_name` is the page title.
- `/de/articles/`, `/fr/articles/`, `/id/articles/` serve **English content** with a self-canonical and are not in the hreflang cluster. That is locale duplication.
- `/security/` (EN URL) has a **Spanish** title: "EMCD: tus activos, nuestra fortaleza." That is a locale leak.
- `page_not_found_status_code: 301`: some nonexistent URLs redirect instead of returning 404 (soft-404 risk). But `/llms.txt` does return 404, so the behavior is inconsistent.
- llms.txt 404 (tie with BiXBiT and ePIC).

### Where BiXBiT is clearly ahead

| Factor | BiXBiT | EMCD |
|---|---|---|
| TTFB | 37–43 ms | 301–406 ms |
| Perf / TBT, homepage | 0.87 / 365 ms, LCP 2.75 s | 0.31 / 4987 ms, LCP 16.3 s |
| TBT, firmware page | 758 ms | 8504 ms (JS-heavy Nuxt + 15 third parties) |
| CLS, homepage | 0.001 | 0.096 (close to the 0.1 threshold) |
| A11y | 0.90–0.93 | 0.83–0.85 |
| JSON-LD on commercial pages | WebSite + Organization everywhere, SoftwareApplication + Breadcrumb on Whatsminer m5x | none (microdata Organization only) |
| Date format in Article | — (not re-checked today; confirm it is ISO) | invalid `9/2/2026` |
| Firmware landing page meta | title/OG populated | empty og:image, broken twitter:card |

BP/SEO scores are a **tie** (0.77 / 0.85–0.92 on both sites).

## Ready-made snippets (real BiXBiT URLs)

**A. hreflang for the layout (example `/en/firmwares/antminer`)**
```html
<link rel="canonical" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer">
```
The `/ru/firmwares/antminer` counterpart is an assumption based on the pattern. **Check that it exists and returns 200** before merging. The `/ru` page must carry the same set in reverse (reciprocity). For templates without a translation, output only `en` + `x-default`, or nothing.

**B. Article (blog). Fields that fix both BiXBiT's gaps and EMCD's mistakes**
```json
{"@type": "Article",
 "@id": "https://bixbit.io/en/blog/post/{slug}#article",
 "headline": "{title}",
 "datePublished": "2026-09-09T00:00:00+00:00",
 "dateModified": "{CMS updated_at, ISO 8601}",
 "inLanguage": "en",
 "author": {"@type": "Person", "name": "[VERIFY: real author]",
            "url": "https://bixbit.io/en/author/{author-slug}"},
 "publisher": {"@id": "https://bixbit.io/en#organization"},
 "mainEntityOfPage": {"@id": "https://bixbit.io/en/blog/post/{slug}#webpage"}}
```
Use absolute URLs and ISO dates only. The `/en/author/` path does not exist yet; that is a proposal. Before merging: Rich Results Test + regression check against the 09-16 baseline. Deliver it as a PR.

## Not measured (stated honestly)
- EMCD response headers (HSTS, brotli): not available through the DataForSEO endpoints I used. curl was denied.
- EMCD sitemap contents (URL count, lastmod, image:). Because of that, **content scale (number of articles) was not compared**.
- Lighthouse on the EMCD article, and field CWV for either site.
- One Lighthouse run per URL (±10–20%).

## [VERIFY] for a human
- Whether `/ru/*` counterparts exist for each en template before hreflang goes live.
- The real blog author(s) and author pages.
- Whether ES/PT versions of the firmware hub are needed (business decision). Translate all tech facts (J/TH, models, dev fee) only after checking.
