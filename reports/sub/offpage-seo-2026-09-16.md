# Off-Page SEO Audit — BiXBiT (bixbit.io/en)
**Date:** 2026-09-16
**Analyst:** Off-page SEO Agent
**Scope:** Backlink profile (qualitative), brand mention landscape, competitor link-gap
(Braiins, Vnish, LuxOS, ePIC), outreach targets — update to `reports/sub/offpage-seo-2026-06-17.md`

---

## DATA GAP — Critical Disclosure (unchanged since June)

All quantitative backlink metrics remain **UNAVAILABLE**. Checked this session via `ToolSearch`
before starting — no `seo-backlinks` / `seo-dataforseo` skill invocation was possible because the
underlying credentials are not present, and direct `.env` access is blocked by a permission rule.

| Source | Status | Reason |
|---|---|---|
| DataForSEO Backlinks | UNAVAILABLE | No credentials; `.env` access blocked by permission rule this session |
| Moz API | UNAVAILABLE | No credentials configured |
| Bing Webmaster API | UNAVAILABLE | No credentials configured |
| Ahrefs / Semrush | No access | Not configured |

**No DR/DA, referring-domain counts, anchor-text ratios, spam scores, or link-velocity numbers
appear anywhere in this report.** Every place a quantitative backlink metric would normally go is
marked `[DATA UNAVAILABLE — requires Moz/DataForSEO/Bing Webmaster API key]`. This is the third
consecutive audit cycle (per MEMORY.md baseline) without programmatic backlink access — **escalate
to human: add DataForSEO credentials before the next `/full-audit` cycle**, or this report will
remain qualitative-only indefinitely.

All findings below come from live web search (`WebSearch`/`WebFetch`) run 2026-09-16, not from any
backlink index.

---

## 1. What Changed Since June 2026

1. **Blog now exists at scale (~400 URLs, actively publishing).** In June, "no blog content" was
   itself cited as an outreach constraint — there was nothing distinctive to pitch besides ANN
   threads. That constraint is gone. See Section 3 for what this does and does not unlock.
2. **New directory/aggregator footprint found:** SaaSHub comparison page
   (`saashub.com/compare-minetheasic-vs-bixbit-whatsminer-antminer-firmware`), a Crunchbase company
   profile, and an ISC High Performance 2025 exhibitor listing on `swapcard.com` — none of these
   appeared in the June search pass. Confidence: Medium (found via search snippet; link
   status/quality not independently fetchable for all three — see 2.1).
3. **The core competitive gap has NOT closed.** d-central.tech and emcd.io firmware-comparison
   content, re-checked by direct fetch this session, still exclude BiXBiT entirely — same as June.
   If anything the gap is more conspicuous: d-central.tech's comparison roster has grown to include
   **ePIC, AxeOS/Bitaxe, Nerd-firmware family, CGMiner/BFGMiner, and D-Central's own DCENT_OS**,
   while BiXBiT remains absent.
4. **Reddit presence: still zero.** Repeated site-scoped search returns nothing; brand-name
   collision with unrelated "Bix"/"Bixbite"/"BizX" entities continues to pollute generic SERPs (see
   Section 5, P3).

---

## 2. Brand Mention Landscape (2026-09-16 pass)

### 2.1 Confirmed / Likely Mentions (new or re-confirmed this pass)

| Source | URL | Type | Notes |
|---|---|---|---|
| BitcoinTalk.org | `topic=5566528.20` — "[ANN] BiXBiT Full Mining Ecosystem" | ANN thread | Re-confirmed live; per search snippet the ANN post itself is now dated Jan 2026 (thread bumped/reposted) |
| BitcoinTalk.org | `topic=5407702.0` — "Dev custom ASIC Whatsminer firmwares" | ANN thread | Re-confirmed live from June |
| BitcoinTalk.org | `topic=5437897.0` — "Bounty BiXBiT" | New thread found this pass | Bounty campaign thread — community-engagement signal, low authority |
| SaaSHub | `saashub.com/compare-minetheasic-vs-bixbit-whatsminer-antminer-firmware` | Software-comparison directory page | **New find.** WebFetch returned HTTP 403 (bot-blocked) — outbound link to bixbit.io and follow/nofollow status **[VERIFY manually in a browser]**. SaaSHub is a mid-tier software-directory aggregator; worth claiming/completing the listing regardless of current link status. |
| Crunchbase | `crunchbase.com/organization/bixbit` | Company data profile | **New find.** High-DA aggregator, standard practice to claim and complete (website field, description, funding/founding data). Typically nofollow but strong entity/NAP signal for Knowledge Graph and GEO. |
| Swapcard (ISC High Performance 2025) | exhibitor listing page | Trade-show exhibitor directory | **New find.** Confirms real-world event presence (ISC High Performance is an HPC/data-center trade show) — a legitimate, checkable industry signal and a class of directory (event exhibitor pages) not previously catalogued in the June audit. |
| LinkedIn / X / YouTube / Facebook | company/brand profiles | Owned social profiles | Not backlinks, but relevant for NAP consistency / entity graph (see local-seo and geo-ai agents) |
| bixbitusa.io + help.bixbitusa.io | US-entity site + help center | Cross-domain sibling brand | Still **not confirmed** whether it passes a follow link back to bixbit.io/en — same open item as June. `[VERIFY]` |

### 2.2 Explicitly checked and NOT found

- **Reddit:** zero relevant results across repeated queries (`site:reddit.com "BiXBiT"` and
  variants). Either no community presence or content is too sparse/old to surface in search.
- **Mining tool/profitability directories** (WhatToMine, Minerstat, NiceHash, AsicMinerValue): no
  BiXBiT presence found. These platforms mostly index pools/hardware/exchanges, not third-party
  firmware, so absence here is lower-priority than the firmware-comparison gap in Section 3.

### 2.3 A caution on AI-generated summaries during this research

WebSearch's own summarization repeatedly surfaced specific performance claims — "40% faster,"
"$60,000+ annual savings per MW," "70–80% higher hashrate," "10–20% lower power draw" — these are
**scraped directly from bixbit.io/bixbitusa.io's own marketing copy**, not third-party verification.
Per CLAUDE.md Section 4, none of these figures should be reused in outreach templates or reports
without being marked `[VERIFY]` and confirmed by a human against actual bench data. This report does
not treat them as established facts anywhere below.

---

## 3. Blog (~400 URLs) — What It Does and Doesn't Change for Off-Page

The blog's existence resolves the June-era objection "there is nothing to pitch." It does **not**
automatically make BiXBiT link-worthy. Distinguish:

**Content types found in search results that ARE plausible link magnets, if promoted directly
(not via the generic blog homepage):**
- `/en/blog/post/firmware-update-log-for-whatsminer` — a changelog page. Changelogs are exactly the
  kind of granular technical reference that forum posts and troubleshooting threads naturally cite.
- `/en/calc` (Crypto Profit ASIC Calculator) — classic link-magnet format; "mining profitability
  calculator" roundup articles and tool directories link to calculators far more readily than to
  blog posts. This was not flagged as an outreach asset in June because its existence wasn't yet
  confirmed as production-ready; per `data/site-structure.md` it is now live with hreflang deployed.
- `/en/documentation/*` (user guides, error-code references) — plausible "further reading" citation
  targets from third-party troubleshooting content and from pool/hosting provider support docs.

**What this does NOT do:** having 400 blog URLs is not itself an outreach pitch. d-central.tech and
emcd.io did not start linking to BiXBiT despite the blog growing from ~290 to ~400 posts between
June and September — volume alone isn't converting into editorial citations. The gap is about
**specific, structured, comparison-grade assets** (a BiXBiT vs. Braiins/Vnish/LuxOS spec table, a
sourced benchmark writeup, a calculator) that a third-party editor can point to or embed, not about
raw post count. Recommend coordinating with `content-seo` to identify (or commission) 2-3 flagship
posts/pages built specifically as outreach assets, rather than pitching the blog in general.

---

## 4. Competitor Gap — Re-Verified 2026-09-16 (Direct Fetch)

| Site | Braiins | Vnish | LuxOS | ePIC | Other firmware now listed | BiXBiT |
|---|---|---|---|---|---|---|
| d-central.tech (`bitcoin-mining-software-comparison`) | YES | YES | YES | YES (new since June) | AxeOS/Bitaxe, Nerd-firmware family, CGMiner, BFGMiner, DCENT_OS | **NO** — confirmed via direct fetch |
| emcd.io (`best-custom-asic-firmware-...`) | YES | YES | YES | not seen | — | **NO** — confirmed via direct fetch |
| hashrateindex.com ("Top 5 Bitcoin Mining Firmware 2026") | YES (BraiinsOS) | not seen in retrieved snippet | YES (leads the list) | not seen | — | **No evidence of inclusion** in retrieved snippets — full article not fetched in full; [VERIFY by human fetch of the complete article] |

**Interpretation, updated from June:** the exclusion is not just persistent, it is **relatively
worse** — d-central.tech has since added ePIC and a full open-source firmware section (AxeOS, Nerd
family, CGMiner/BFGMiner) plus its own DCENT_OS, meaning its comparison scope expanded and still did
not pick up BiXBiT. This strengthens the case for direct, proactive outreach rather than waiting to
be discovered.

`[DATA UNAVAILABLE — requires Moz/DataForSEO/Bing Webmaster API key]` for: referring-domain counts,
DR/DA of d-central.tech/emcd.io/hashrateindex.com, and any BiXBiT vs. competitor backlink-count
comparison. Any market-share figures attributed to competitors in third-party content (e.g. a
Cambridge Digital Mining Industry Report figure cited by d-central.tech for VNISH's hashrate share)
belong to that third-party source, not to BiXBiT, and are not verified here.

---

## 5. Prioritized Outreach Target List

### P0 — act within 2 weeks

| Target | Why | Action |
|---|---|---|
| d-central.tech | Highest-authority niche firmware comparison; gap is now wider (added ePIC + open-source section, still no BiXBiT) | Human outreach using Template A (updated below) — pitch calculator + changelog + spec sheet as concrete assets, not just "consider us" |
| emcd.io | Pool-operator editorial reach, comparison content confirmed to exclude BiXBiT | Human outreach using Template C |
| hashrateindex.com | Premier mining-data media; heavily cited by AI answer engines (GEO overlap) | Human to fetch full article and confirm inclusion/exclusion before outreach; if excluded, Template B |

### P1 — act within 30 days

| Target | Why | Action |
|---|---|---|
| SaaSHub listing | New directory find; link status unverified (403 on automated fetch) | Human to manually check the live page, claim/complete listing if unclaimed, confirm outbound link exists |
| Crunchbase profile | High-DA aggregator; standard B2B entity signal | Human to claim/verify profile completeness (website, description, founding data) |
| bixbitusa.io / help.bixbitusa.io cross-linking | Carried over unresolved from June — sibling-domain authority may be leaking | Audit cross-domain links; ensure follow link + correct anchor to bixbit.io/en |
| ISC High Performance exhibitor listing (swapcard.com) + any other trade-show exhibitor pages | New directory class identified this pass; event-exhibitor pages are a legitimate, checkable link source | Human to confirm the listing links out correctly; identify other past/future trade shows BiXBiT exhibited at and claim those listings too |

### P2 — next quarter

| Target | Why | Action |
|---|---|---|
| Software/tool directories in the "ASIC mining tools" and "firmware alternatives" space (AlternativeTo, G2, Capterra-style listings — pattern confirmed to exist for competitors, e.g. "Awesome Miner Alternatives" on alternativeto.net) | BiXBiT not found on any of these during this pass; competitors and adjacent tools are | Submit/claim listings; low effort, moderate authority |
| Promote `/en/calc` directly (not the blog) to "mining profitability calculator" roundups and tool-directory sites | Calculators attract links more readily than articles | Build a one-page outreach pitch specifically for the calculator, separate from firmware pitches |
| Leverage specific blog/documentation pages (changelog, error-code guides) as citation targets for troubleshooting forums | New content inventory (400 posts) makes this newly possible | Coordinate with `content-seo` to select 2-3 flagship technical pages for targeted promotion |

### P3 — monitoring only

| Target | Why | Action |
|---|---|---|
| Brand disambiguation ("Bix", "Bixbite", "BIX Malaysia", "BizX") | Reconfirmed this pass — these entities dominate generic-brand SERP/search snippets ahead of BiXBiT-specific results | Strengthen Organization schema / entity signals (coordinate with technical-seo); monitor branded search share |
| Reddit / community presence | Confirmed zero footprint again this pass | Not urgent — low ROI vs. P0/P1 targets; revisit if a genuine organic community forms |

---

## 6. Outreach Templates (Pass to Human Negotiator)

> Templates from the June report (Sections 5A–5C) remain valid and are not reproduced in full here.
> Two additions below reflect this pass's new findings. All outreach, negotiation, and follow-up
> must be handled by a human — this agent does not conduct outreach.

### Template D: SaaSHub / Crunchbase — Claim & Complete Listing

**To:** N/A (self-service claim flow on each platform)

Action for human: log into SaaSHub and Crunchbase, claim the BiXBiT listing/profile if unclaimed,
verify the website field points to `https://bixbit.io/en`, and confirm whether the SaaSHub
comparison page (`compare-minetheasic-vs-bixbit-whatsminer-antminer-firmware`) currently links out.
If the platform allows a company description edit, keep language consistent with brand voice rules
in CLAUDE.md Section 4 (no unverified performance claims).

### Template E: hashrateindex.com — Calculator/Changelog Pitch (supplements June Template B)

**To:** [verify contact at hashrateindex.com]
**Subject:** A concrete data asset for your mining-firmware coverage — BiXBiT calculator + changelog

Hi [Name],

Following up on whether BiXBiT firmware might fit your industry coverage — rather than a general
pitch, two specific assets that might be useful to cite or link directly:
- Our public mining profitability calculator: bixbit.io/en/calc
- Our public firmware changelog for Whatsminer: bixbit.io/en/blog/post/firmware-update-log-for-whatsminer

Happy to provide more structured data (spec sheet, benchmark methodology) if useful for a fuller
writeup.

[Human name]

---

## 7. Mention Monitoring — Updated Query List

Carry forward all June queries (Section 6 of the prior report) and add:

7. `site:saashub.com "bixbit"` — check listing status periodically
8. `site:crunchbase.com "bixbit"` — check profile completeness
9. `"bixbit" swapcard OR exhibitor OR "trade show"` — catch other event-listing mentions
10. `"bixbit" -bixbit.io -bixbitusa.io` (broad, no site restriction) — general unlinked-mention sweep, rerun quarterly

---

## 8. Methodology & Limitations

Sources used: `WebSearch` (9 queries) + `WebFetch` (2 successful fetches of d-central.tech and
emcd.io comparison pages; 1 blocked fetch — SaaSHub, HTTP 403). No backlink-index API was available
or used. All confidence levels are qualitative:

- d-central.tech / emcd.io exclusion: **High confidence** (direct page fetch, full content list
  reviewed, BiXBiT absent).
- hashrateindex.com exclusion: **Medium confidence** (search-snippet only, full article not
  fetched — flagged `[VERIFY]`).
- New directory finds (SaaSHub, Crunchbase, Swapcard): **Medium confidence** (found via search
  snippet; not all independently verified for link presence/status).
- Reddit absence: **Medium-high confidence** (repeated queries, consistent null result, but search
  tooling may under-index Reddit generally).

**Everything requiring a quantitative backlink metric remains
`[DATA UNAVAILABLE — requires Moz/DataForSEO/Bing Webmaster API key]`.** This is now three
consecutive audit cycles without programmatic backlink data (see MEMORY.md baseline from June).
Recommend this be escalated as a standing action item ahead of the next `/full-audit`.
