# Technical Gap: BiXBiT (bixbit.io/en, /ru) vs PiTBiT (pitbitecosystem.com + pitbit.online), 2026-09-25

> Scope: only **noticeable** technical advantages PiTBiT has, plus where BiXBiT is ahead. Only items that are **new** compared with the ePIC and EMCD reports appear in the main table.
> I did not re-measure BiXBiT. Its numbers come from `reports/sub/competitor-gap-ePIC-tech-2026-09-25.md`, `reports/sub/competitor-gap-EMCD-tech-2026-09-25.md`, `data/dfs-lighthouse-instant-bixbit-vs-epic-2026-09-25.json` and `data/site-structure.md` (crawled 2026-09-16).
> PiTBiT snapshot: `data/dfs-lighthouse-instant-pitbit-2026-09-25.json`.

## Data sources (status)

| Source | Status |
|---|---|
| DataForSEO `lighthouse/live/json` (mobile, LH 13.4.0, simulated, **1 run per URL**, lab) | OK for 3 URLs: `/en/`, `/en/firmware/`, `pitbit.online/` |
| DataForSEO `instant_pages` + `raw_html` (JS off; one repeat run with a Googlebot UA) | OK: `/en/`, `/en/firmware/`, `/en/catalog/firmware/firmware-for-antminer-s21-pro/`, `/` (RU), `pitbit.online/`, `robots.txt`, `sitemap.xml` + 2 child sitemaps, `llms.txt` |
| DataForSEO SERP `site:pitbitecosystem.com/en/` (US/en) | OK, 1 query |
| curl / WebFetch | not used. I did not work around them |
| PageSpeed API / CrUX | **no access** (500 / 403). No field CWV |
| HTTP response headers (HSTS, brotli) for PiTBiT | **not retrieved**. Only `content_encoding: gzip` and `server: nginx` came through instant_pages |
| GSC | not applicable to a competitor |

## Measurements (mobile lab, 1 run)

| URL | Perf | BP | SEO | A11y | LCP | CLS | TBT | TTFB | Weight |
|---|---|---|---|---|---|---|---|---|---|
| bixbit.io/en | **0.87** | 0.77 | **0.85** | **0.93** | **2.75 s** | **0.001** | **365 ms** | **37 ms** | **16.9 MB** |
| pitbitecosystem.com/en/ | 0.44 | 0.73 | 0.58 | 0.88 | 10.4 s | 0.05 | 570 ms | 1048 ms | 29.9 MB |
| bixbit.io/en/firmwares/antminer | 0.56 | 0.73 | **0.92** | **0.90** | 42.1 s | **0.005** | 758 ms | **43 ms** | 23.8 MB |
| pitbitecosystem.com/en/firmware/ | **0.59** | 0.73 | 0.58 | 0.80 | **3.7 s** | 0.119 | **535 ms** | 253 ms | **6.5 MB** |
| pitbit.online/ (app login) | 0.97 | 0.96 | 0.92 | 0.89 | 2.3 s | n/a | n/a | 37 ms | 0.13 MB |

PiTBiT runs on 1C-Bitrix (nginx). Its third parties are Yandex Metrica, Yandex Cloud, Jivochat, the TradingView widget and JSDelivr. Interactive (TTI) on `/en/` is 95 s. On both EN pages the SEO score of 0.58 comes from the noindex problem described below.

## Main finding: PiTBiT's EN site is effectively closed to indexing

Every EN template I checked (home, firmware hub, product page) has **two conflicting robots meta tags** in `<head>`:
```html
<meta name="robots" content="noindex, nofollow">   <!-- right after <title> -->
...
<meta name="robots" content="index, follow" />     <!-- Bitrix default -->
```
The page is the same with a Googlebot UA. Google applies the most restrictive directive, so the result is **noindex, nofollow**. The EN pages also have **no canonical**, a placeholder description `"Описание сайта"`, keywords `"ключевые слова"`, empty `og:title`/`og:description`, `og:locale=ru-RU` and 0 JSON-LD. The sitemap contains **0 `/en/` URLs**.
SERP check `site:pitbitecosystem.com/en/` (US): 4 results, all of them junk: `/en/news/?PAGEN_2=22&SIZEN_2=3…` ×3 and `/en/auth/registration.php?register=yes&backurl=…`. Neither the homepage nor the firmware page is indexed. The robots.txt rule `Disallow: /*pagen` is lowercase, so it does not block `PAGEN_` (robots.txt matching is case-sensitive).

**Result: PiTBiT has no competitive technical presence in English organic search.** Their technical strength is only in the **RU** version.

## Comparison table (new compared with ePIC/EMCD only)

| # | Factor | BiXBiT | PiTBiT | Ahead | Prio | Fix |
|---|---|---|---|---|---|---|
| 1 | **Model-level firmware landing pages (RU)** | Hub `/en/firmwares/antminer` + 5 Whatsminer series pages. The 7 legacy Antminer model pages (`/en/firmwares/asic-s19`, `asic-S17*`, `T17*`, `T9-plus`, `s9…`) are **noindex** + a duplicated title/meta (09-16). There are no S19 XP / S21 / S21 Pro / S21 Hydro / L9 / T21 pages | `sitemap-iblock-2.xml`: **26 indexable RU pages**, one per model, `/catalog/firmware/proshivka_dlya_antminer_{model}/` (s21_pro, s21_xp_hydro, s19k_pro, l9, t21, ks/hs3, k7, d9…), each with its own lastmod | **PiTBiT** (RU long tail "прошивка для antminer s21 pro") | **P1** | Do not revive the thin legacy pages. Build a template `/en/firmwares/antminer/{model}` (+ `/ru/…`) only for models BiXBiT actually supports, each with a **unique** block: supported hashboards/control boards, available profiles, flashing method, a model-specific FAQ. Add SoftwareApplication + BreadcrumbList (m5x template) and a self-canonical, and include them in sitemap-firmware. The model list and every number are `[VERIFY]`. If a page has no unique content, leave the model as an anchor section in the hub (`#s21-pro`) instead of creating a URL |
| 2 | **Organization: legal/contact entity fields** | Organization has name, logo and sameAs (FB/IG…). Description is ad copy (ePIC #4). No `legalName`, `address`, `contactPoint`, `foundingDate` | RU `@graph`: Organization with `@id`, `legalName`, `foundingDate`, `PostalAddress`, `ContactPoint`, `sameAs` (VK/Telegram/YouTube) + WebSite with `SearchAction` | **PiTBiT** (RU home only) | P2 | Add these fields to the `@graph` from ePIC snippet B (snippet A below). All values are `[VERIFY]` (legal name, address, founding year, phone). Add sameAs for Telegram/YouTube/LinkedIn if the accounts exist |
| 3 | **Sitemap lastmod per URL** | category/product frozen at 2024-09-04, firmware at 2025-10-31 | Bitrix generates it automatically; product lastmod = today's edits | PiTBiT | (already P1 in ePIC #8) | Not new, but a third competitor confirms it. Priority stays the same |
| 4 | Social meta on the home page (RU) | og:image = favicon, 0 Twitter tags | Full OG + 5 Twitter tags, but og:image is also the favicon `android-chrome-512x512.png` | PiTBiT (Twitter tags only) | (already P1 in ePIC #3) | Not new |

Nothing else is ahead: **hreflang** is missing on both PiTBiT versions (RU and EN), so BiXBiT with 2 templates is formally ahead. Its P0 comes from EMCD, not PiTBiT. **llms.txt**: 404 on both sites (tie).

## Two domains: plus or minus for PiTBiT?

Structure: `pitbitecosystem.com` (Bitrix marketing site + shop, RU at `/`, EN at `/en/`), `pitbit.online` (monitoring app: login, `/openstat`, `/openstatpool`, `/firmware`) and a third domain, `pitbit.pro/calculating` (calculator, linked from the home page).

**Overall a minus for SEO**, with one small plus:
- Minus: `pitbit.online/` is a login page with 21 words, **no H1**, no canonical, an RU description on an `lang="en"` page, and **no link back** to pitbitecosystem.com (its only external link is Google OAuth). The brand's link equity and entity signals are split across 3 hosts, and Organization.sameAs does not connect them.
- Minus: the calculator on a separate domain (`pitbit.pro`) takes a classic linkable asset away from the main domain.
- Plus: application noise (auth, dashboards) stays off the marketing domain, and the app itself is light (Perf 0.97, 131 KB). The public `/openstat` / `/openstatpool` pages could become linkable stats pages. **Not measured** (I did not check their indexability or content).
- Takeaway for BiXBiT: keep marketing pages, the calculator (`/en/calc`) and docs on `bixbit.io`, which is already the case. Keep the AMS app on a separate host/subdomain with `noindex` on the login screen, and link from it to `/en/ams`. Where BiXBiT actually hosts the AMS app was **not checked** in this cycle (`[VERIFY]`).

## Where BiXBiT is clearly ahead

| Factor | BiXBiT | PiTBiT |
|---|---|---|
| **EN indexability** | Home/firmware/ams pages indexable, with self-canonicals | EN is noindex,nofollow (conflicting meta), no canonical, 0 EN URLs in the sitemap, junk pages in the index |
| EN meta | Specific titles/descriptions | `"Home page - PITBIT"`, `"Firmware"`, description `"Описание сайта"` |
| JSON-LD on EN | WebSite + Organization everywhere, SoftwareApplication on Whatsminer, FAQPage on /en/ams | 0 blocks on EN (only the RU home has @graph) |
| hreflang | 2 templates | 0 |
| TTFB | 37–43 ms | 253–1048 ms |
| Home page: Perf / LCP / weight | 0.87 / 2.75 s / 16.9 MB | 0.44 / 10.4 s / 29.9 MB |
| CLS | 0.001–0.005 | 0.05–0.119 (firmware page above the 0.1 threshold) |
| A11y / LH SEO | 0.90–0.93 / 0.85–0.92 | 0.80–0.88 / 0.58 |
| HTML | 2 errors (duplicate `<body>`) | 4–11 errors ("attribute has already been added", mismatched end tag) |
| Firmware landing page (weight/LCP) | **worse**: 23.8 MB / 42 s | 6.5 MB / 3.7 s. This is the one metric where PiTBiT is ahead, and it is already covered by ePIC P0 #1 |

## Ready-made snippet (real BiXBiT URLs)

**A. Organization additions to the `@graph` (on top of ePIC snippet B; `@id` = `https://bixbit.io/en#organization`)**
```json
{"@type": "Organization",
 "@id": "https://bixbit.io/en#organization",
 "name": "BiXBiT",
 "legalName": "[VERIFY: registered legal entity name]",
 "url": "https://bixbit.io/en",
 "logo": {"@type": "ImageObject", "url": "https://bixbit.io/site/images/logo_header.svg"},
 "foundingDate": "[VERIFY: year]",
 "contactPoint": {"@type": "ContactPoint", "contactType": "sales",
   "email": "[VERIFY]", "availableLanguage": ["English", "Russian"],
   "url": "https://bixbit.io/en/contacts"},
 "sameAs": ["https://www.facebook.com/bixbit.official",
            "https://www.instagram.com/bixbit.official/",
            "[VERIFY: LinkedIn / YouTube / Telegram]"]}
```
Only add `address` if the office is public and matches the NAP on `/en/contacts` (hand off to local-seo). Before merging: Rich Results Test + regression check against the 09-16 baseline. Deliver as a PR.

## Not measured (stated honestly)
- Field CWV (PSI 500, CrUX 403). Lab numbers are from a single run (±10–20%).
- PiTBiT HTTP headers (HSTS, brotli).
- Indexability and content of `pitbit.online/openstat`, `/openstatpool`, `/firmware`, and `pitbit.pro`.
- `site:` for the RU version (I only ran EN/US). The `site:` operator is approximate.
- Lighthouse per-audit details (the reasons for BP 0.73).

## [VERIFY] for a human
- Which Antminer/Whatsminer models BiXBiT really supports, before any per-model URL is created (#1).
- Legal name, founding year, contact email and the full list of official social profiles (#2).
- The AMS app host, and whether its login screen is closed to indexing.
