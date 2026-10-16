# Content / Keyword Gap: BiXBiT vs ePIC Blockchain — 2026-09-25

**Scope:** Google US (2840) / en. bixbit.io (main locale /en) vs epicblockchain.io
**Author:** content-seo subagent
**Previous report:** `reports/competitor-gap-ePIC-2026-06-19.md` (June 2026, DataForSEO was down, WebFetch + self-test only)

---

## 0. Data sources and status

| Source | Endpoint / params | Status | Snapshot |
|---|---|---|---|
| DataForSEO Labs | `domain_rank_overview/live` epicblockchain.io | OK (20000) | `data/dfs-ranked-keywords-epicblockchain.io-2026-09-25.json` (`domain_rank_overview` block) |
| DataForSEO Labs | `ranked_keywords/live` epicblockchain.io, limit 1000 | OK, **total_count = 10** | same file |
| DataForSEO Labs | `ranked_keywords/live` bixbit.io | already pulled earlier (162 kw) | `data/dfs-ranked-keywords-bixbit.io-2026-09-25.json` |
| DataForSEO Labs | `domain_intersection/live` bixbit vs ePIC, `intersections=true` | OK, 1 shared keyword | `data/dfs-domain-intersection-bixbit.io-vs-epicblockchain.io-2026-09-25.json` |
| DataForSEO Labs | `domain_intersection/live` ePIC vs bixbit, `intersections=false` | OK, 9 keywords (all branded) | same file |
| DataForSEO Labs | `keyword_overview/live` (2 calls, 36 keywords) | OK; a number of keywords **came back with no data** (listed in §6) | inline, used in the tables below |
| DataForSEO SERP | `serp/google/organic/live/regular`, depth 30, 7 calls | 3 OK; **3 × `40101 Internal SE Server Error`** (`autotuning firmware antminer`, `antminer autotuning` retry, `mining firmware dev fee`); **1 × `40106 partial results`** (`firmware dev fee`, page 1 only) | `data/dfs-serp-firmware-probe-bixbit-vs-epic-2026-09-25.json` |
| GSC / GA4 | — | not checked this run (connectors were down in the 2026-09-16 baseline) | — |

Every response was small and came back inline, so no tool-results files were created. The snapshots in `data/` are compact transcripts of the fields that matter (kw, vol, pos, URL).
The 159 KB file `data/dfs-domain-intersection-epicblockchain.io-not-bixbit.io-2026-09-25.json` belongs to the offpage agent. It is a **backlinks** intersection, not a keyword intersection, and is not used here.

**Methodology caveat.** The Labs DB (ranked_keywords) misses ePIC's rankings on a number of commercial queries that a live SERP does show (see §1.2). For a thin domain like ePIC, Labs undercounts, so the gap was cross-checked with live SERPs on the core firmware queries. Most firmware volumes sit at the 10/mo floor bucket, so the tail was prioritized by intent and stage (TCO, comparison) rather than volume.

---

## 1. Where ePIC ranks and BiXBiT does not

### 1.1 Domain scale (Labs, US/en)

| Metric | bixbit.io | epicblockchain.io |
|---|---|---|
| Ranked keywords | 162 | **10** |
| ETV (est. traffic/mo) | 115 | **14.6** |
| pos 1 | 2 | 1 |
| pos 2–3 | 5 | 1 |
| pos 4–10 | 39 | 3 |
| pos 11–20 | — | 1 |
| Movement ePIC | — | new 6, up 1, down 1, lost 2 |

**Conclusion:** in classic US organic search, ePIC is a thin domain. In the Labs DB, **all** of its top-20 keywords are branded. The only non-branded ePIC keyword in Labs is `immersion cooling mining`, at position 30, and BiXBiT ranks higher on it (14).

### 1.2 Gap table (non-branded, relevant to the 4 priority clusters)

Sources: Labs ranked_keywords plus live SERP (marked "SERP"). "—" = not in top 30 (SERP) / not in DB (Labs). vol = DataForSEO US monthly volume, "n/d" = DataForSEO returned no volume.

| Keyword | Vol | ePIC pos | BiXBiT pos | Cluster | Priority | Comment |
|---|---|---|---|---|---|---|
| firmware dev fee | n/d | **4** (SERP, press release "reduces UMC OS development fee to 1.5%", 2026-01-26) | — | Firmware / TCO | **P0** | The only true gap in the firmware cluster. Decision-stage query (fee = TCO). Top 3 is Reddit, d-central.tech ("Zero Dev-Fee Bitcoin Mining"), bitcointalk. BiXBiT has no page. ePIC's 1.5% figure is `[VERIFY: current UMC OS dev fee, model range, conditions]` |
| mining firmware dev fee | n/d | n/d (SERP 40101) | n/d | Firmware / TCO | P0 (together with the one above) | no data, re-pull |
| antminer custom firmware | 10 | 7 (SERP, install guide "UMC OS … with RigRunner") | **5** (SERP, /en/firmwares/antminer) | Firmware | P1 (SXO) | Not a gap by position, but a page-type gap: ePIC ranks with an **install guide**, and d-central with a "complete guide". BiXBiT ranks with a product page. It needs an install/how-to spoke |
| immersion cooling mining | 20 | 30 (Labs; 2022 Medium repost) | 14 (Labs, fluids blog post) | Cooling | P1 (defend) | Shared. BiXBiT is ahead, but the landing page is a fluids post, not a commercial page. Intent mismatch (commercial) |
| antminer control board / s19 control board | 10 / 10 | — (ePIC's product category is UMC, but it doesn't rank) | — | Firmware (adjacent) | P3 | ePIC's hardware category. BiXBiT doesn't sell controllers `[VERIFY]`. Cover as a section inside the comparison, not as a separate page |
| antminer autotuning | n/d | n/d (SERP 40101) | n/d | Firmware | P1 | June: ePIC has a "Perpetual Tune" post `[VERIFY: name/mechanics]`. Rankings not confirmed (the post isn't in Labs). Re-pull the SERP |

**Topic-level finding (content ePIC has, with confirmed visibility):**
1. The dev-fee press release ranks in the top 5 for `firmware dev fee`.
2. The Antminer install guide (UMC OS + RigRunner) is in the top 10 for `antminer custom firmware`.
3. The immersion post (2022) is at position 30. Weak.

June's "custom firmware vs stock" and "what is Perpetual Tune" posts **don't appear in Labs US rankings**. They don't rank, or sit below the DB threshold.

### 1.3 ePIC branded demand (separate, no action on titles)

| Keyword | Vol | ePIC pos | URL | Note |
|---|---|---|---|---|
| blockminer | 210 | 23 | / | ePIC's rig brand. The SERP is ambiguous (other products share the name) |
| epic microsystems | 140 | 41 | / | most likely a different company (navigational), noise |
| epic miner | 90 | 2 | /product/ | |
| epic-miner | 90 | 4 | /product/ | |
| epic mining | 90 | 9 | / | ePIC is weak on its own brand (pos 9) |
| epic chip | 50 | 31 | /product/ | noise |
| epic block | 40 | 10 | /product/ | |
| epic blockchain | 30 | 1 | / | yearly trend −60% |
| epic chain crypto news | 30 | 18 | /blog/ | noise |
| epic umc | 20 | not in ePIC's ranked list | — | yearly +100%, quarterly −33% |
| epic firmware | 10 | — | — | |
| epic control board | 10 | — | — | |
| epic blockminer | 10 | — | — | |
| rigrunner | 260 | — | — | name of ePIC's installer, but also a PDU brand from another manufacturer. Ambiguous, **do not target** |

Total ePIC branded demand in the US is ≈ 400–500/mo (excluding noise and rigrunner). Brand interest is falling (epic blockchain −60% YoY). The one growing entity is `epic umc` (+100% YoY, low base). For BiXBiT this demand is only reachable through a factual comparison page ("ePIC UMC OS alternative"). ePIC's name must not appear in BiXBiT's own titles and meta.

---

## 2. Where BiXBiT beats ePIC

### 2.1 Shared keywords where BiXBiT ranks higher

| Keyword | Vol | BiXBiT pos | ePIC pos | BiXBiT URL | Source |
|---|---|---|---|---|---|
| immersion cooling mining | 20 | 14 | 30 | /en/blog/post/immersion-liquid-choosing-the-right-one-for-mining | Labs intersection |
| antminer custom firmware | 10 | 5 | 7 | /en/firmwares/antminer | SERP live |

### 2.2 BiXBiT keywords where ePIC is absent (selection from the 4 clusters)

Across the whole BiXBiT set: 74 keywords in the top 20. By cluster (top 20): firmware 4 kw / 170 vol, cooling 13 / 830, monitoring 1 / 70, infra (rack/container) 5 / 330. ePIC is absent from all of them.

| Keyword | Vol | BiXBiT pos | URL | Cluster |
|---|---|---|---|---|
| whatsminer firmware | 20 | 3 | /en/firmwares/whatsminer-series-m3x | Firmware |
| whatsminer custom firmware | 10 | 2 / 6 / 16 (SERP) | /en/firmwares, /whatsminer-series-m3x, /whatsminer-series-m6x | Firmware |
| whatsminer tools | 50 | 8 | /en/firmwares/whatsminer-series-m3x | Firmware |
| antminer firmware | 50 | 15 (Labs) / — (SERP top-25) | /en/firmwares/antminer | Firmware — **unstable**, see §3 |
| best asic firmware | n/d | 18 (SERP) | /en/firmwares | Firmware (comparison intent) |
| asic monitor | 70 | 7 | /en/ams | Monitoring |
| mineral oil for immersion cooling | 30 | 1 | /en/blog/post/immersion-liquid-… | Cooling |
| antminer in mineral oil / antminer mineral oil / mineral oil antminer | 50 each | 2 | /en/blog/post/immersion-liquid-… | Cooling |
| mineral oil immersion cooling | 20 | 5 | same | Cooling |
| what is novec liquid | 20 | 9 | /en/blog/post/novec-and-coolant-… | Cooling |
| how does immersion cooling work | 30 | 12 | /en/blog/post/how-does-immersion-cooling-work | Cooling |
| immersion computer cooling | 390 | 15 | same | Cooling |
| hydro rack | 40 | 16 | /en/products/rack-hydro | Cooling (hydro) |
| whatsminer hydro | 10 | 18 | /en/products/container-hydro | Cooling (hydro) |
| mining rack | 40 | 6 | /en/products/rack | Infra |
| crypto mining shipping container | 170 | 17 | /en/products/container | Infra |

**Whatsminer is uncontested territory against ePIC.** ePIC has no Whatsminer rankings in the US at all (neither Labs nor SERP). The live SERP for `whatsminer custom firmware` shows **bixbitusa.io at #9** (`/firmware/`). That is a second BiXBiT-brand domain competing on the same query. Flag for technical-seo / international-seo: cross-domain cannibalization or deliberate split, `[VERIFY: relationship between bixbitusa.io and bixbit.io]`.

---

## 3. Gap-closing plan (clusters, pages, intent)

Cluster files already exist: `content/clusters/antminer-firmware.md`, `whatsminer-firmware.md`, `immersion-cooling-mining.md`, `mining-fleet-monitoring.md`, `pdu-power-distribution.md`. The plan wires new spokes into them. No new hubs are needed.

| # | Priority | Page (target URL bixbit.io/en) | Type / intent | Hub | Target queries (DataForSEO) | What closes / why |
|---|---|---|---|---|---|---|
| 1 | **P0** | `/en/antminer-firmware/dev-fee` (new spoke; Whatsminer section inside) | Explainer + TCO calculator / commercial investigation | antminer-firmware (+ link from whatsminer-firmware) | firmware dev fee (ePIC 4, BiXBiT —), mining firmware dev fee | ePIC's only confirmed firmware gap. **Positioning risk:** BiXBiT's dev fee is 2.8% (2% on M2x) per the 2026-09-16 baseline `[VERIFY: current figures]`, and ePIC's published figure is 1.5% `[VERIFY]`. The page must **not** claim "lowest fee". Frame it honestly: how a fee is charged (hashrate share vs time share `[VERIFY: BiXBiT's mechanism]`), what the fee pays for, and a TCO formula where the operator plugs in their own J/TH, $/kWh and fee. Competitor fees in a table go in only with a source and date `[VERIFY each]`. Also fix the "no dev fee" claim in `content/briefs/antminer-firmware-pillar.md` and `whatsminer-firmware-pillar.md` (factually wrong) |
| 2 | **P0** | `/en/antminer-firmware/comparison` (brief exists: `content/briefs/antminer-firmware-comparison.md`) | Comparison / commercial investigation | antminer-firmware | best asic firmware (BiXBiT 18; hashrateindex "Top 5 Firmware 2026" #4, braiins #3) | Add an ePIC UMC OS column: dev fee, autotuning, supported models, **software-only vs control-board replacement** `[VERIFY all ePIC parameters]`. This is BiXBiT's core structural argument |
| 3 | P1 | `/en/antminer-firmware/install` (brief exists: `antminer-firmware-install.md`) | How-to / informational → transactional | antminer-firmware | antminer custom firmware (ePIC ranks here with its install guide) | Match the SERP page type: ePIC and d-central rank with guides. HowTo steps, fleet-level installation (batch via AMS) `[VERIFY: AMS batch-flash feature]`, rollback to stock |
| 4 | P1 | `/en/compare/bixbit-vs-epic-umc-os` (new) | Alternative/vs page / commercial | antminer-firmware (comparison) | epic umc (20, +100% YoY), epic firmware (10), epic control board (10) | Captures ePIC's branded comparative demand. Factual, with a "last verified" date. Every ePIC figure `[VERIFY]` with a link to the primary source. Low volume, but it's a bottom-funnel query and a GEO signal (LLMs pull vs pages for "ePIC alternatives") |
| 5 | P1 | `/en/antminer-firmware/autotuning` (brief exists: `antminer-autotuning.md`) | Explainer / informational-commercial | antminer-firmware | antminer autotuning (n/d, SERP 40101) | Counterpart to ePIC's "Perpetual Tune" `[VERIFY]`. Re-pull the SERP before publishing |
| 6 | P1 | `/en/immersion-cooling-mining` (pillar, brief exists: `immersion-cooling-mining-pillar.md`) | Commercial landing | immersion-cooling-mining | immersion cooling mining (BiXBiT 14, ePIC 30) | Move the commercial query off the fluids post and onto the commercial pillar; the fluids post links to the pillar with the exact-match anchor. ePIC has no cooling product, so this is a pure BiXBiT ecosystem advantage |
| 7 | P2 | `/en/firmwares/antminer` (on-page, `content/page-optimize/firmwares.md` exists) | Product/category / transactional | antminer-firmware | antminer firmware (50; Labs 15, live SERP not in top 25) | Unstable ranking. The SERP is dominated by forums/YouTube (how-to intent). Add an "install / update" block and FAQ, and link to spoke #3 |
| 8 | P2 | `/en/whatsminer-firmware` (pillar, brief exists) | Hub / commercial | whatsminer-firmware | whatsminer firmware (3), whatsminer custom firmware (2), whatsminer tools (8) | Defend the lead where ePIC has no rankings. Also resolve the bixbitusa.io vs bixbit.io question (#9 vs #2 on one query) |
| 9 | P3 | section inside #2/#4: "Custom firmware vs control-board replacement" | informational | antminer-firmware | antminer control board (10), s19 control board (10) | ePIC's hardware category. Cover it as an argument, not a standalone page |
| — | — | PDU, monitoring | — | pdu-power-distribution, mining-fleet-monitoring | — | **No gap against ePIC**: ePIC has zero rankings there. Priority follows the general plan, not this gap |

### Internal linking (additions to `content/internal-linking.md`)
- `/en/firmwares`, `/en/firmwares/antminer`, `/en/firmwares/whatsminer-series-*` → `/en/antminer-firmware/dev-fee` (anchor: "how the dev fee works").
- `/en/antminer-firmware/comparison` ↔ `/en/compare/bixbit-vs-epic-umc-os` ↔ `/en/antminer-firmware/dev-fee` (triangle).
- `/en/antminer-firmware/install` → `/en/ams` (fleet-scale install) `[VERIFY: feature]`.
- `/en/blog/post/immersion-liquid-choosing-the-right-one-for-mining` → `/en/immersion-cooling-mining` (anchor "immersion cooling for mining").

---

## 4. What changed since June 2026 / what got confirmed

| June claim (no DataForSEO) | Status 2026-09-25 | Data |
|---|---|---|
| ePIC is ahead on organic on-page signals | **Not confirmed for rankings.** ePIC has 10 US keywords / ETV 14.6 vs BiXBiT's 162 / 115 | Labs overview |
| ePIC "took" the "custom firmware vs stock" and Perpetual Tune topics on its blog | **Not confirmed.** Those posts are not in Labs US rankings | ranked_keywords |
| ePIC wins the dev-fee topic through PR (1.5%) | **Confirmed:** the press release is #4 for `firmware dev fee` (the 1.5% figure itself is still `[VERIFY]`) | SERP live |
| BiXBiT dev fee "3%" `[VERIFY]` | **Updated:** 2.8% / 2% M2x (baseline 2026-09-16) `[VERIFY: still current]`. ePIC's figure is lower, so the dev-fee page must argue TCO, not the lowest fee | memory / baseline |
| hashrateindex.com and d-central.tech are key third-party sources | **Confirmed:** hashrateindex "Top 5 Bitcoin Mining Firmware for 2026" is #4 for `best asic firmware`; d-central is #3 for `antminer custom firmware` and #2 for `firmware dev fee` | SERP live |
| BiXBiT's unique niches (cooling, AMS, PDU, Whatsminer) | **Confirmed:** zero ePIC rankings there; BiXBiT holds 13 cooling kw in the top 20 | Labs |
| AI visibility 0/10 vs 7/10 | Not rechecked here (geo-ai's area, see `data/geo-epic-2026-09-25/`) | — |

---

## 5. [VERIFY] list for a human

- ePIC UMC OS dev fee = 1.5% (source: ePIC press release dated 2026-01-26). Current? Conditions, models?
- ePIC model compatibility (Antminer S19/S21, Whatsminer M3x/M5x in the June report). Current?
- ePIC "Perpetual Tune": name, what it actually does.
- UMC is a hardware control-board replacement; the price per unit ($100–200 in June) is unconfirmed.
- BiXBiT dev fee 2.8% / 2% M2x: current? How it's charged (share of time vs hashrate)?
- Does BiXBiT have batch firmware installation through AMS?
- How bixbitusa.io relates to bixbit.io (same owner? partner?).
- Any J/TH or % improvement figures for comparison pages: only from BiXBiT's own tests, with methodology.

## 6. Keywords with no data in DataForSEO (keyword_overview returned nothing or null volume)
`epic antminer firmware`, `epic powerplay`, `epic firmware s19`, `epic firmware s21`, `epic firmware dev fee`, `epic vs braiins`, `universal mining controller`, `antminer autotuning`, `hydro cooling mining`, `zero dev fee firmware`, `antminer firmware install`, `umc os`, `perpetual tune`, `firmware dev fee`, `mining firmware dev fee`; null volume: `best antminer firmware`, `best asic firmware`, `bitcoin mining pdu`. Volumes were not invented.
