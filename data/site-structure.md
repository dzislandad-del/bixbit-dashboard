# data/site-structure.md — Реальная структура URL (источник правды)

> CRAWLED: 2026-09-16 (targeted re-verification pass, NOT a full 70-page re-crawl)
> Previous baseline: 2026-06-17 (70 pages). This pass confirmed ~28 URLs directly via raw HTTP
> fetch (status code + title + meta robots + canonical + JSON-LD) and cross-checked 5 sitemap
> files. Everything not re-touched this pass is carried over from 2026-06-17 and marked
> **"not re-verified this pass"** — do not treat those as current fact, just as last-known-state.
>
> **Headline change since June:** the June audit's assumption of "zero canonical / zero JSON-LD /
> zero meta description sitewide" is **NO LONGER TRUE**. Canonical tags, meta descriptions, and
> JSON-LD (WebSite + Organization, partially BreadcrumbList/FAQPage) are now deployed on every
> page checked. This was invisible to WebFetch (which cannot read `<head>`/`<script>` content) —
> confirmed only via raw `curl` fetch of page source in this pass. Treat any prior or future
> WebFetch-based claim of "no schema found" as unreliable; verify with raw HTML fetch.

> **UPDATE 2026-09-28** (raw HTML через `scripts/page-snapshot.py` + живые sitemap; снимок `data/page-snapshot-2026-09-28.json`):
> - **Локаль `/es/` существует** и полноценна: `/es`, `/es/ams`, `/es/firmwares`, `/es/firmwares/antminer` — 200, свои canonical,
>   переведённые title. **0 URL `/es/` в sitemap**, в hreflang не упомянута. `/pt`, `/zh`, `/kz`, `/fr` — 404.
> - **`docs.bixbit.io`** — отдельный сайт документации (200, без canonical, robots.txt 404), индексируется Bing.
> - Sitemap сейчас: en 137 URL, ru 763 (блог en 106 / ru 733 — не «~400 total»), es 0.
> - hreflang: только на `/en/products`, `/en/products/container`, `/en/calc`, `/en/blog` (ru + x-default); на остальных нет.
> - Подтверждено снова: canonical и meta description на всех 23 HTML; Organization.description = ad-copy охлаждения;
>   пустой FAQPage на `/en/firmwares`, `/en/documentation`, `/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1`, `/es/firmwares`;
>   `/en/faq` без FAQPage; sitemap-баги (сироты, дубль coolant, пробел в container-1k, lastmod 2024-09-04) не исправлены; `/llms.txt` 404.

---

## Sitemap index (https://bixbit.io/sitemap.xml) — confirmed 2026-09-16

| Sub-sitemap | en URLs | ru URLs | lastmod seen | Notes |
|---|---|---|---|---|
| sitemap-category.xml | 10 | 10 | 2024-09-04 (all, stale) | home, contacts, calc, sustainability, blog, products, firmwares, ams, faq, about |
| sitemap-product.xml | 7 | 7 | 2024-09-04 (all, stale) | container, rack, cell, coolant (**duplicate entry**), rack-hydro, server, container-hydro |
| sitemap-firmware.xml | 6 | 6 | 2025-10-31 / 2024-11-14 | antminer hub + 5 whatsminer series pages only — **7 legacy Antminer model pages removed since June** |
| sitemap-documentation.xml | 5 | 4 | 2023-06-12 to 2026-04-14 | individual articles only, hub page `/en/documentation` itself not listed |
| sitemap-blog.xml | ~400 total (en+ru) | — | 2018-10-15 to **2026-09-09** | grew from ~290 in June; actively publishing (newest post is 1 week old) |

**Confirmed NOT in any sitemap (live 200 pages, orphaned from sitemap discovery):**
- `/en/products/pdu` — live product page, zero sitemap presence
- `/en/asics-cooling`, `/en/asics-cooling/hydro-systems`, `/en/asics-cooling/immersion-systems` — still absent, same P1 gap as June, unresolved 3 months later
- `/en/documentation` (hub page) — only child articles are in the sitemap
- 7 legacy Antminer model pages (see Firmware section) — removed from sitemap-firmware.xml since June, consistent with their new noindex status

**Confirmed unresolved bugs (present in June, still present now):**
- `/en/products/coolant` still duplicated in sitemap-product.xml
- `/en/products/ container-1k` (literal space in URL) still malformed in sitemap-product.xml — confirmed the space-free URL `/en/products/container-1k` returns HTTP 200, so this is a sitemap-generation bug, not a dead page
- Category/product sitemap lastmod still frozen at 2024-09-04 sitewide

---

## robots.txt (https://bixbit.io/robots.txt) — confirmed 2026-09-16, UNCHANGED from June

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
Allow: /assets/*.js|css|png|jpg|jpeg|gif|svg|ttf|woff|webp|mp4
Clean-param: network&placement&adposition&none&gad_source&etext&gbraid&gtm_debug&show
Sitemap: https://bixbit.io/sitemap.xml
```

No explicit AI-crawler directives (GPTBot/ClaudeBot/PerplexityBot/Google-Extended not mentioned) →
still allowed by wildcard `*`. `/download/` still disallowed — unresolved [VERIFY] from June:
confirm firmware binaries don't live under `/download/`.

---

## Firmware (приоритет 1)

### Hub & series pages — re-confirmed 2026-09-16 via raw HTML fetch

- `/en/firmwares` — HTTP 200. Title: "BiXBiT Custom ASIC Mining Firmware". Meta description present
  (new since June). Canonical: self-referencing, present. JSON-LD: WebSite + Organization +
  BreadcrumbList + **FAQPage with empty `mainEntity: []`** (broken/placeholder schema — see report).
  In sitemap-category.xml.
- `/en/firmwares/antminer` — HTTP 200. Title: "Antminer Firmware by BiXBiT – Your Custom Firmware".
  Meta description present. Canonical present. JSON-LD: WebSite + Organization only (no
  Breadcrumb/Product/SoftwareApplication). In sitemap-firmware.xml, lastmod 2025-10-31.
- `/en/firmwares/whatsminer-series-m6x` — in sitemap-firmware.xml, lastmod 2025-10-31. **Not
  re-verified this pass** beyond sitemap presence.
- `/en/firmwares/whatsminer-series-m5x` — in sitemap-firmware.xml, lastmod 2025-10-31. **Not
  re-verified this pass.**
- `/en/firmwares/whatsminer-series-m3x` — in sitemap-firmware.xml, lastmod 2025-10-31. **Not
  re-verified this pass.**
- `/en/firmwares/whatsminer-series-m2x` — in sitemap-firmware.xml, lastmod 2025-10-31. **Not
  re-verified this pass.**
- `/en/firmwares/whatsminer-all-series` — in sitemap-firmware.xml, lastmod 2024-11-14. **Not
  re-verified this pass.**

### Legacy Antminer model pages — MAJOR CHANGE SINCE JUNE, confirmed 2026-09-16

All 7 pages below are still **live (HTTP 200)** but now carry `<meta name="robots"
content="noindex, follow">`, a **self-referencing canonical to their own URL** (not to the
antminer hub), and a **title + meta description byte-for-byte duplicated from
`/en/firmwares/antminer`** ("Antminer Firmware by BiXBiT – Your Custom Firmware"). All 7 have
been **removed from sitemap-firmware.xml** since the June crawl (which listed them as indexed,
titled pages). This is a consistent, uniform pattern across all 7 — looks like a deliberate
content-consolidation decision (merge thin per-model pages into the antminer hub, keep URLs alive
for backlink/UX continuity, noindex to stop them competing with the hub in search).

**[VERIFY with dev/content owner]: confirm this was an intentional consolidation and not a broken
template.** If intentional, it should be documented; if accidental, these pages likely lost
meaningful organic traffic (they had unique titles/content in June per the June crawl) and a
301 to the hub (instead of noindex,follow self-canonical) may be the better long-term pattern.

- `/en/firmwares/asic-s19` — HTTP 200, noindex,follow, duplicate title/meta, self-canonical, NOT in sitemap.
- `/en/firmwares/asic-S17-S17Pro` — same pattern.
- `/en/firmwares/asic-S17-plus` — same pattern.
- `/en/firmwares/asic-T17-plus` — same pattern.
- `/en/firmwares/asic-T17` — same pattern.
- `/en/firmwares/asic-T9-plus` — same pattern.
- `/en/firmwares/asic-s9-s9j-s9i` — same pattern.

---

## Cooling (приоритет 2)

- `/en/products` — "ASIC miner cooling systems | Bitcoin immersion cooling" — **not re-verified
  this pass** (June data carried over).
- `/en/asics-cooling` — HTTP 200, confirmed 2026-09-16. Title: "BiXBiT Crypto Mining Cooling
  Solutions for ASICs". Meta description present. Canonical present. JSON-LD: WebSite +
  Organization only. **Still absent from every sitemap** (unresolved P1 from June).
- `/en/asics-cooling/hydro-systems` — HTTP 200, confirmed live 2026-09-16 (status-only check,
  head/schema not re-extracted). Still absent from sitemap.
- `/en/asics-cooling/immersion-systems` — HTTP 200, confirmed live 2026-09-16 (status-only check).
  Still absent from sitemap.
- `/en/products/rack` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/rack-hydro` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/server` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/container` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/container-hydro` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/container-1k` — confirmed HTTP 200 live 2026-09-16 (the correct, space-free URL).
  Sitemap entry for this URL is malformed (contains a literal space) — see sitemap section.
- `/en/products/cell` — in sitemap-product.xml. **Not re-verified this pass.**
- `/en/products/coolant` — in sitemap-product.xml (duplicated entry). **Not re-verified this pass.**

---

## Monitoring / AMS (приоритет 3)

- `/en/ams` — HTTP 200, confirmed 2026-09-16. Title: "ASIC Monitoring Software – BiXBiT AMS".
  Meta description present. Canonical present. JSON-LD: WebSite + Organization + **FAQPage (real
  Q&A content, e.g. "What is BiXBiT AMS?", "Is the BiXBiT AMS system paid?")** + BreadcrumbList
  (Home → Monitoring system). This is the most complete schema implementation found on the site.
- `/en/ams/connect` — HTTP 200, confirmed live 2026-09-16 (status-only check). Still not in any
  sitemap. Title/content not re-extracted this pass — carried over from June as thin/onboarding
  page, `[VERIFY]` noindex candidate.

---

## Power Distribution / PDU (приоритет 4)

**CHANGED FROM "NOT FOUND" — confirmed live 2026-09-16.**

- `/en/products/pdu` — HTTP 200. Title: "Smart PDU for Mining Data Centers, Miners and Farms".
  Meta description present ("BiXBiT Smart PDU offers real-time power monitoring and load
  optimization..."). Canonical present. JSON-LD: WebSite + Organization only. Content covers
  6/12/16/20-pin configurations, real-time power monitoring, AMS integration, quote request form.
  **Not present in sitemap-product.xml, sitemap-category.xml, or any other sitemap discovered** —
  this page has zero sitemap discoverability despite being a fully built commercial page. Linked
  from `/en/firmwares` ("Order PDU" CTA) per prior page-optimize research.

---

## Blog (приоритет — content distribution)

**CHANGED FROM "NOT FOUND" — confirmed live and actively publishing 2026-09-16.**

- `/en/blog` — HTTP 200. Title: "BiXBiT Blog | Cryptocurrency articles and reviews". Meta
  description present (generic/thin: "The latest news on mining and cryptocurrency..."). Canonical
  present (appears twice in source — see report, possible duplicate tag bug). **Hreflang present**
  (en x-default + ru alternate — one of only 2 templates sitewide with hreflang deployed). JSON-LD:
  BreadcrumbList (with a malformed `Home` item id `https://bixbit.io/en/en` — double `/en/en`, bug)
  + WebSite + Organization.
- `sitemap-blog.xml` lists ~400 URLs total (en+ru) under `/en/blog/post/{slug}` and
  `/ru/blog/post/{slug}`, up from ~290 in June. Newest lastmod 2026-09-09 (6 days before this
  audit) confirms active publishing cadence. Oldest lastmod 2018-10-15 — old thin posts
  ("best-asics-for-mining-in-2018-2019...") still in the sitemap, same P2 content-freshness issue
  flagged in June, unresolved.
- Individual blog post URLs — **not re-verified this pass** beyond the sitemap sample; use
  `content-seo` agent's blog sitemap sample for cluster/gap analysis.

---

## Documentation / Knowledge Base (new section — was only vaguely referenced in June)

**CHANGED — June file only said "Knowledge Base" with no URLs. Confirmed structure 2026-09-16.**

- `/en/documentation` — HTTP 200 (hub page). Title: "Documentation | ASIC user guide from
  BiXBiT". Meta description present. Canonical present. JSON-LD: WebSite + Organization +
  **BreadcrumbList with a copy-paste bug** (position 2 item name is "Firmwares" pointing to
  `/en/firmwares` instead of "Documentation" / `/en/documentation`) + **FAQPage with empty
  `mainEntity: []`** (same broken-placeholder pattern as `/en/firmwares`). **Not present in any
  sitemap** — only its child articles are indexed via sitemap-documentation.xml.
- `/en/documentation/new-user-guide-for-whatsminer-asic` — in sitemap-documentation.xml,
  lastmod 2026-03-31. **Not re-verified this pass** beyond sitemap presence.
- `/en/documentation/user-guide-for-whatsminer-asic` — in sitemap-documentation.xml,
  lastmod 2026-01-28. **Not re-verified this pass.**
- `/en/documentation/error-codes-for-whatsminer-asic` — in sitemap-documentation.xml,
  lastmod 2026-04-14 (most recently updated URL found in entire site crawl). **Not re-verified
  this pass.**
- `/en/documentation/connecting-an-additional-variable-power-supply-unit` — in
  sitemap-documentation.xml, lastmod 2023-06-12. **Not re-verified this pass.**
- `/en/documentation/connecting-an-additional-power-supply-unit` — in sitemap-documentation.xml,
  lastmod 2023-06-12. **Not re-verified this pass.**

---

## Tools (new section)

- `/en/faq` — HTTP 200, confirmed 2026-09-16. Title: "FAQ frequently asked questions". **Meta
  description is a literal placeholder/template stub**: "FAQs start with a question and then
  provide a concise answer" — not real copy, needs urgent rewrite. Canonical present. JSON-LD:
  WebSite + Organization only — **no FAQPage schema despite this being the site's actual FAQ page
  with real Q&A content** (two sections confirmed via WebFetch: "BiXBiT Immersion Cooling Systems"
  and "Firmware and BiXBiT AMS", covering firmware dev-fee cost, warranty impact, flashing
  difficulty, leak risk, noise levels, etc.). In sitemap-category.xml.
- `/en/calc` — HTTP 200, confirmed 2026-09-16. Title: "Crypto Profit ASIC Calculator – Bitcoin &
  Hashrate Converter". Meta description present. Canonical present. **Hreflang present** (en
  x-default + ru — same as /en/blog, the only 2 templates with hreflang sitewide). JSON-LD:
  BreadcrumbList (same `/en/en` double-slug bug as blog) + WebSite + Organization. Interactive
  mining profitability calculator (GPU/ASIC, hashrate, power cost, multi-currency output);
  promotes immersion cooling (claims up to 40% performance increase — `[VERIFY]`, unsourced
  marketing claim on a live page, flag to content owner). In sitemap-category.xml.

---

## Homepage

- `/en` — HTTP 200, confirmed 2026-09-16. Title: "BiXBiT Bitcoin Mining Solutions – Tools for
  Crypto Miners" (unchanged since June). Meta description now present (new since June): "Bitcoin
  mining solutions by BiXBiT: firmwares, miners monitoring systems, PDU, immersion cooling for
  ASICs and server hardware, and hydro cooling systems." Canonical present, self-referencing.
  **No hreflang** (despite /ru homepage existing in sitemap). JSON-LD: WebSite + **Organization**
  (name "BiXBiT", logo `https://bixbit.io/site/images/logo_header.svg`, sameAs: Facebook,
  Instagram, YouTube — real social profiles). **Bug: Organization schema `description` field is
  cooling-product ad copy** ("BiXBiT immersion cooling systems for mining ✅ Safe construction...
  ➤ Worldwide shipping!") **reused verbatim as the sitewide Organization description on every
  single page** (confirmed identical on homepage, ams, firmwares, antminer, pdu, asics-cooling,
  faq, documentation, blog, calc) — this is not a company description, it's cooling-page ad copy,
  and it is factually wrong context for e.g. the firmware or PDU pages' Organization entity.

---

## About / Other

- `/en/about` — HTTP 200, confirmed live 2026-09-16 (status-only check, not re-extracted). Title
  was empty in June — **not re-verified for title/meta this pass.**
- `/en/sustainability` — HTTP 200, confirmed live 2026-09-16 (status-only check). Title from June:
  "Sustainability | How BiXBiT protects environment" — **not re-verified this pass.**
- `/en/contacts` — HTTP 200, confirmed live 2026-09-16 (status-only check). Title was empty in
  June — **not re-verified this pass.**

---

## Sitewide schema/meta patterns observed 2026-09-16 (applies across all pages checked)

1. **Canonical tags: deployed sitewide**, self-referencing, correct on every page checked (10/10).
2. **Meta descriptions: deployed sitewide** on every page checked, but quality is inconsistent —
   see `/en/faq` (placeholder stub) and `/en/firmwares/asic-*` (duplicated from hub) above.
3. **Hreflang: only on 2 of 10+ templates checked** (`/en/blog`, `/en/calc`) — homepage, firmware
   hub, antminer hub, ams, pdu, asics-cooling, faq, documentation all have **no hreflang** despite
   /ru counterparts existing in the sitemap.
4. **JSON-LD: deployed on every page checked**, minimum WebSite + Organization. Known bugs:
   - `WebSite` schema is emitted per-page with that page's own URL instead of one sitewide
     `WebSite` entity pointing at the homepage — non-standard, dilutes intent of the type.
   - `Organization.description` is cooling-page ad copy copy-pasted sitewide (see Homepage section).
   - `FAQPage` with `mainEntity: []` (empty) deployed on `/en/firmwares` and `/en/documentation` —
     broken/placeholder, likely to throw structured-data warnings in Search Console.
   - `/en/faq` — the actual FAQ page — has **no** FAQPage schema at all, while pages with FAQ
     widgets (`/en/ams`) do.
   - `BreadcrumbList` on `/en/documentation` shows wrong section name ("Firmwares" instead of
     "Documentation") — copy-paste bug.
   - `BreadcrumbList` on `/en/blog` and `/en/calc` has a malformed Home item id
     (`https://bixbit.io/en/en` — double `/en/en`).
   - `Product` / `SoftwareApplication` schema: **still absent everywhere**, including
     `/en/firmwares/antminer`, `/en/products/pdu`, `/en/asics-cooling` — same P0 gap as June.
