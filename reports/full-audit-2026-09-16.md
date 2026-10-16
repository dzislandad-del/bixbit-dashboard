# Full SEO Audit — bixbit.io/en — 2026-09-16

**Scope:** https://bixbit.io/en (English locale), full site per RUNBOOK/CLAUDE.md.
**Prior baseline:** `reports/full-audit-2026-06-17.md` / `data/baseline-2026-06-17.json`.
**Sub-reports:** `reports/sub/technical-seo-2026-09-16.md`, `reports/sub/content-seo-2026-09-16.md`, `reports/sub/offpage-seo-2026-09-16.md`, `reports/sub/geo-ai-2026-09-16.md`, `reports/sub/local-seo-2026-09-16.md`.
**Site structure source of truth:** `data/site-structure.md` (re-verified 2026-09-16 — see note below on scope of re-verification).

---

## 1. Data Source Availability

| Source | Status | Notes |
|---|---|---|
| Google Search Console | **UNAVAILABLE** | No connector reachable this session (regression from June, where GSC was available) |
| GA4 | **UNAVAILABLE** | No connector reachable this session (regression from June) |
| PageSpeed Insights / CrUX | **UNAVAILABLE** | No connector reachable this session (regression from June) |
| DataForSEO | **UNAVAILABLE** | Not connected — third consecutive audit cycle without it |
| Moz | **UNAVAILABLE** | Not connected |
| Bing Webmaster | **UNAVAILABLE** | Not connected |
| `.env` (direct read) | **BLOCKED** | Denied by an auto-mode permission rule — cannot confirm which keys are actually configured |

**Honest framing:** every quantitative data source (traffic, positions, CTR, CWV, backlinks, keyword volume) is unavailable this cycle — this is worse than June, where GSC/GA4/PageSpeed were connected. Everything below is derived from direct page/sitemap/robots.txt inspection (raw `curl`, not WebFetch — see §2) and qualitative research (WebSearch). No traffic, ranking, or volume figures are cited anywhere in this report or its sub-reports; where a number appears, it is either a real on-page fact (e.g., dev fee %) or explicitly marked `[VERIFY]`/`[DATA UNAVAILABLE]`.

---

## 2. Methodology Correction (important — read before trusting any prior report)

Every `/page-optimize` pass run earlier today (homepage, `/en/ams`, `/en/firmwares`) and the June full-audit relied on **WebFetch**, which converts pages to markdown and **cannot see `<head>` or `<script>` content**. This was discovered mid-session and independently confirmed by today's technical-seo pass using raw `curl`. Consequence: **the "zero canonical / zero meta description / zero JSON-LD sitewide" finding from June, and the "absent" schema states assumed in today's three page-optimize artifacts, are wrong.** Canonical, meta descriptions, and JSON-LD (`WebSite` + `Organization`, partial `BreadcrumbList`/`FAQPage`) are actually deployed on every page checked.

**Action already taken:** `data/site-structure.md` has been rewritten with real per-page technical fingerprints captured via raw HTTP fetch. **Action still needed:** the JSON-LD snippets drafted in `content/page-optimize/homepage.md`, `ams.md`, and `firmwares.md` must be **diffed against what's actually live** before deploy — they should *add* `Product`/`SoftwareApplication` schema and *fix* the bugs below, not overwrite or duplicate the existing `WebSite`/`Organization` blocks. This is flagged as a P0 process note, not just a technical one.

---

## 3. Executive Summary — What Changed Since June

**Site structure:** The June crawl (70 pages) was three months stale. Four entire sections believed absent (`/en/products/pdu`, `/en/blog` — now ~400 URLs, `/en/documentation`, `/en/faq` + `/en/calc`) are live, real, and in most cases actively maintained. `data/site-structure.md` has been rewritten accordingly (see file header for exact re-verification scope: ~28 URLs directly re-checked via curl, sitemap network fully re-parsed, everything else explicitly labeled "not re-verified this pass").

**Technical health: MODERATE-TO-SERIOUS**, upgraded from June's CRITICAL — foundational elements (canonical, meta description, JSON-LD) now exist, but several are broken or half-deployed in ways that actively send bad signals to Google (empty `FAQPage`, wrong `Organization.description`, copy-pasted `BreadcrumbList`), which is arguably worse than the absence June found.

**Content:** Roughly zero net progress on the ~45 planned spoke pages across the four June content-brief clusters (firmware, cooling, monitoring, PDU) — the URL architecture in those briefs never matched the site's real IA. Two of the briefs' core claims ("no dev fee") are now confirmed **factually wrong** against the live site (real fee: 2.8%, 2% on Whatsminer M2x) and must be rewritten before any writer uses them.

**Off-page:** No change in data availability (still zero quantitative backlink data, third cycle running). BiXBiT remains absent from competitor-comparison content on d-central.tech/emcd.io despite the blog's growth — raw content volume hasn't converted into third-party citations.

**GEO/AI:** `llms.txt` is still not deployed (confirmed 404 live), and the repo's own draft has gone stale (wrong URLs). The sitewide `Organization.description` bug is independently significant here — it corrupts the one machine-readable "what is this company" signal AI systems read.

**Local:** No change — classical local SEO confirmed still not applicable (no real physical BiXBiT locations). One new minor NAP inconsistency found (mismatched Poland phone numbers between `/en/contacts` and `/en/about`).

---

## 4. Consolidated P0 — Fix This Week

| # | Finding | URL(s) | Source | Fix |
|---|---|---|---|---|
| 1 | `/en/faq` has real Q&A content but **no `FAQPage` schema** | `/en/faq` | technical-seo | Wrap existing content in `FAQPage` JSON-LD — highest-value, lowest-effort fix on the site |
| 2 | `Organization.description` is cooling-product ad copy, **identically copy-pasted on every page** (10/10 checked) | sitewide | technical-seo, escalated by geo-ai | Replace `description` field only (keep name/url/logo/sameAs); `[VERIFY]` real company description with content owner before shipping |
| 3 | `Product`/`SoftwareApplication` schema still 100% absent | `/en/firmwares/antminer`, `/en/products/pdu`, `/en/asics-cooling/*` | technical-seo (unchanged since June) | Deploy snippets already drafted (`content/page-optimize/firmwares-antminer.md` §schema, `homepage.md`, `ams.md`, `firmwares.md`) — **append to existing `WebSite`/`Organization` blocks, don't replace them** (see §2) |
| 4 | `/en/products/pdu` — live, fully built commercial page — **missing from every sitemap** | `/en/products/pdu` | technical-seo | Add to `sitemap-category.xml` or a new `sitemap-pdu.xml` |
| 5 | Hreflang missing on the highest-commercial-value templates (only deployed on `/en/blog`, `/en/calc`) | `/en`, `/en/ams`, `/en/firmwares`, `/en/firmwares/antminer`, `/en/products/pdu`, `/en/asics-cooling`, `/en/faq`, `/en/documentation` | technical-seo | Extend the already-working `/en/calc` pattern to remaining templates; `[VERIFY]` `/ru/*` counterpart parity first |
| 6 | `/en/faq` meta description is literal template placeholder text ("FAQs start with a question and then provide a concise answer") | `/en/faq` | technical-seo | Rewrite with real copy — draft in sub-report, `[VERIFY]` before shipping |
| 7 | Two June content briefs assert **"no dev fee"** — factually contradicted by the live site (2.8% / 2% on M2x) | `content/briefs/antminer-firmware-pillar.md`, `whatsminer-firmware-pillar.md` | content-seo | Rewrite differentiator claims and affected FAQ answers before any writer uses these briefs |
| 8 | `llms.txt` not deployed (404 live); repo draft also stale (wrong URLs: `/en/monitoring`, `/en/cooling/immersion`, `/en/pdu` vs. real `/en/ams`, `/en/asics-cooling/*`, `/en/products/pdu`) | `https://bixbit.io/llms.txt` | geo-ai | Rewrite draft against current `data/site-structure.md`, then deploy |
| 9 | CWV and GSC baselines are 3 months stale and unverified this cycle — do not cite June figures (CLS=0.888, 0 clicks) as current | `/en`, sitewide | technical-seo | Re-run PageSpeed/pull GSC the moment API access is restored |

---

## 5. P1 — Next 2 Weeks

- **7 legacy Antminer model pages** (`asic-s19`, `asic-S17-S17Pro`, `asic-S17-plus`, `asic-T17-plus`, `asic-T17`, `asic-T9-plus`, `asic-s9-s9j-s9i`) are now `noindex,follow`, self-canonical, duplicate-titled from the hub, and dropped from `sitemap-firmware.xml` — a uniform pattern suggesting deliberate consolidation, but unconfirmed. `[VERIFY]` intent with dev/content owner; if unintentional, evaluate 301s to `/en/firmwares/antminer` instead.
- **`/en/asics-cooling` + 2 sub-pages still absent from every sitemap** — same P1 flagged in June, unresolved 3 months later.
- **Empty `FAQPage` schema** (`mainEntity: []`) shipped on `/en/firmwares` and `/en/documentation` — populate or remove, don't ship the broken wrapper.
- **`BreadcrumbList` copy-paste bug** on `/en/documentation` (shows "Firmwares" instead of "Documentation").
- **Duplicate/malformed sitemap-product.xml entries** (`/en/products/coolant` duplicate, `/en/products/ container-1k` literal space) — unresolved 3 months after being flagged in June.
- **`content/internal-linking.md` (54KB, June)** is built against a URL architecture the site never adopted — needs a full rebuild, not edits.
- **AMS competitor-comparison briefs are fully written and unused** (`ams-vs-braiins-manager.md`, `ams-vs-luxor-commander.md`, `ams-vs-minerstat.md`) while zero live equivalents exist — lowest-effort content gap to close, given AMS's "supports Whatsminer, Braiins doesn't" differentiator is otherwise unused.
- **Blog content mix doesn't match stated priorities** — sampling shows the ~400-post blog is majority general crypto-news, with firmware (P1 priority per CLAUDE.md) barely represented in recent posts.
- **Documentation hub has a deeper tier than assumed** (error-code sub-pages, PSU guides) but is entirely orphaned from any sitemap except its individual child articles.

---

## 6. P2 — This Month

- `WebSite` schema emitted per-page instead of once, sitewide — non-standard usage, low priority.
- `BreadcrumbList` malformed `/en/en` double-slug Home ID on `/en/blog` and `/en/calc`.
- Duplicate `<link rel="canonical">` tag (same URL, harmless but a template code-smell) on `/en/blog`.
- Stale sitemap `lastmod` dates (2024-09-04) on `sitemap-category.xml`/`sitemap-product.xml` despite real content changes since then.
- Blog sitemap still includes 2018-era thin posts — content-pruning candidate.
- Zero named authorship anywhere sitewide (blog, documentation, firmware, `/en/about`) — E-E-A-T gap.
- AI-crawler explicit-allow directives for robots.txt (proposed in `content/dev-task-p0.md` §3.5) were never deployed — low urgency since wildcard `*` already implicitly allows them.

---

## 7. P3 — Backlog

- `/download/` still disallowed in robots.txt — unconfirmed whether firmware binaries live there (open since June).
- Off-page: unclaimed directory/profile listings found (SaaSHub, Crunchbase, an ISC High Performance 2025 exhibitor page) — human verification/claiming, not urgent.
- Small NAP inconsistency: mismatched Poland phone numbers between `/en/contacts` and `/en/about`.

---

## 8. Sub-Report Summaries

### Technical SEO → [sub/technical-seo-2026-09-16.md](sub/technical-seo-2026-09-16.md)
Full re-verification via raw HTTP fetch (not WebFetch) of ~28 URLs plus the entire sitemap network. Reverses June's "zero schema" finding; documents 6 distinct JSON-LD bugs plus the sitemap/hreflang/noindex findings above. `Product`/`SoftwareApplication` schema remains the one major gap unchanged since June.

### Content SEO → [sub/content-seo-2026-09-16.md](sub/content-seo-2026-09-16.md)
Confirms the "no dev fee" factual error in two pillar briefs, near-zero progress against the June content-cluster plan (wrong URL architecture throughout), and that blog volume growth hasn't shifted topic coverage toward stated priorities (firmware/cooling/monitoring/PDU). PDU and cooling pages are more built-out than the June briefs assumed (real spec tables, PUE data) but still lack FAQ/comparison content.

### Off-Page SEO → [sub/offpage-seo-2026-09-16.md](sub/offpage-seo-2026-09-16.md)
No quantitative backlink data available (third consecutive cycle). BiXBiT still absent from d-central.tech/emcd.io comparison content; the gap is relatively worse since those pages' scope has grown. Recommends promoting specific structured assets (calculator, changelog, error-code guides) rather than "the blog" generically for outreach.

### GEO / AI Visibility → [sub/geo-ai-2026-09-16.md](sub/geo-ai-2026-09-16.md)
`llms.txt` confirmed not deployed; repo draft stale. Escalates the `Organization.description` bug to P0 from a GEO angle (entity-consistency failure for AI/knowledge-graph extraction). Blog/documentation content is real but not shaped for AI passage-citability (specs sometimes embedded as images, no article-level FAQ).

### Local SEO → [sub/local-seo-2026-09-16.md](sub/local-seo-2026-09-16.md)
Confirms June's verdict unchanged: classical local SEO not applicable (no real physical locations; the only "USA office" is a third-party reseller). One new minor NAP inconsistency (phone number mismatch) flagged.

---

## 9. `[VERIFY]` Items Requiring Human Sign-Off

1. Intent behind the 7 legacy Antminer pages' noindex + sitemap removal — deliberate consolidation or broken deploy?
2. Real company description for `Organization.description` (do not ship AI-drafted copy without content-owner sign-off).
3. `/en/faq` meta description replacement copy.
4. Whether `/download/` (disallowed in robots.txt) hosts firmware binaries linked from firmware pages.
5. All `/ru/*` counterpart URLs actually exist/are live before wiring remaining hreflang pairs.
6. Actual current dev fee (2.8% / 2% M2x) — confirmed as a real on-page fact today, but flagged for periodic reconfirmation since commercial terms can change without a corresponding audit update.
7. GSC property configuration, `/en/ams/connect` noindex decision, `x-default` hreflang target — carried forward unresolved from June, not re-touched this pass.
8. Technical firmware specs (J/TH, °C, model compatibility beyond what's stated on-page) — none asserted as new fact anywhere in this audit cycle.

---

## 10. Baseline Snapshot

Saved to `data/baseline-2026-09-16.json` for the next `/weekly-drift` comparison.

---

## Next Steps

1. **This week:** action the 9 P0 items in §4 — the `/en/faq` FAQPage schema (item 1) and the `Organization.description` fix (item 2) are both real-content-exists-already, markup-only fixes with no dependency on unavailable data sources.
2. **Restore data connectors** (GSC, GA4, PageSpeed, DataForSEO, Moz, Bing) before the next `/full-audit` or `/weekly-drift` — this cycle ran with zero quantitative sources, which is a regression from June.
3. **Diff, don't duplicate:** before deploying any of today's `/page-optimize` JSON-LD drafts (homepage, ams, firmwares), reconcile them against the actual live schema documented in §2/§6 of the technical-seo sub-report.
4. **Rebuild `content/internal-linking.md`** and the four affected pillar briefs against the real URL architecture in the refreshed `data/site-structure.md`, correcting the "no dev fee" factual error first.
5. Schedule the next `/weekly-drift` once P0 fixes are deployed, to confirm they landed and didn't regress.
