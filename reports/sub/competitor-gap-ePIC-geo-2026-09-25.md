# GEO / AI-Citation Gap: BiXBiT vs ePIC Blockchain (UMC OS), 2026-09-25

**Scope:** AI-answer visibility of BiXBiT (bixbit.io) vs ePIC Blockchain (epicblockchain.io, UMC OS / PowerPlay) across B2B firmware, monitoring and cooling queries.
**Method: MEASURED.** Live DataForSEO AI Optimization API calls, not a self-test. This replaces the June Claude self-test.
**Compared against:** `reports/geo-check-epic-gap-2026-06-19.md` and `reports/competitor-gap-ePIC-2026-06-19.md` §3. In June the self-test scored ePIC 7/10 and BiXBiT 0/10.

---

## 0. Data sources and status

| Source | Endpoint | Status | Notes |
|---|---|---|---|
| ChatGPT | `/v3/ai_optimization/chat_gpt/llm_responses/live` | OK, 11/11 calls returned 20000 | `gpt-4.1-mini-2025-04-14`, web_search + force_web_search, US. $0.33 |
| Perplexity | `/v3/ai_optimization/perplexity/llm_responses/live` | OK, 11/11 | `sonar`, US. About $0.06 |
| Claude | `/v3/ai_optimization/claude/llm_responses/live` | OK, 11/11 | `claude-sonnet-4-6`, web_search, US. $1.03. The q5 answer was truncated at the token limit |
| Gemini | `/v3/ai_optimization/gemini/llm_responses/live` | OK, 11/11 | `gemini-3.5-flash`, web_search. **The endpoint has no location parameter.** $0.76 |
| Google AI Overview | `/v3/serp/google/organic/live/advanced` + `load_async_ai_overview` | OK, with 40101/40106 on q5, q6, q10, q11 (retried once) | US/en desktop, depth 20. q11 has partial results (organic page 1 only). $0.07 |
| LLM Mentions DB | `/v3/ai_optimization/llm_mentions/search/live` | OK | Historical sampled Q&A (Google AIO and ChatGPT US). A `filters` field returned `40501 Invalid Field: 'filters'`. Multi-keyword targets returned 0 results, so single-entity targets were used |
| WebFetch | 3 source pages | OK | Used to check whether top gap sources name BiXBiT |
| curl (Bash) | — | **Denied** by permissions | robots.txt and llms.txt were not re-checked live today. The status comes from the 2026-09-16 audit |

**Raw data:**
- Per-engine answers: `data/geo-epic-2026-09-25/` (`{chatgpt,perplexity,claude,gemini}-qN.json`, `aio-qN.raw.json`, `aio-qN.aio-text.md`, `aio-summary.json`)
- LLM Mentions dumps:
  - `data/dfs-llm-mentions-google-bixbit-sources-2026-09-25.json`
  - `data/dfs-llm-mentions-aio-braiins-answers-2026-09-25.json`
  - `data/dfs-llm-mentions-chatgpt-braiins-answers-2026-09-25.json`
  - `data/dfs-llm-mentions-aio-epicblockchain-answers-2026-09-25.json`

**Limits:**
- Each prompt was run once per engine, so every cell is a single sample. LLM answers vary between runs; treat 1-answer differences as noise.
- On Google, q10 returned **two different AIOs** in two runs.

---

## 1. Headline score (measured)

The 10 non-branded prompts (q1–q10) were run on 4 LLMs, giving 40 answers, plus 10 Google AIO keywords. q11 names ePIC in the prompt, so it is excluded from the score.

| Metric | ePIC | BiXBiT |
|---|---|---|
| Named in LLM answer text (of 40) | **7** (ChatGPT 3, Claude 2, Perplexity 1, Gemini 1) | **11** (Perplexity 4, Claude 3, Gemini 3, ChatGPT 1*) |
| Own domain cited in LLM answer (of 40) | 6 | 10 |
| Named in Google AIO text (of 10) | 0 | 2 (q2, q5) |
| Own domain in AIO references (of 10) | 0 | 3 (q2, q5, q9) |
| **Total named (of 50)** | **7 / 50** | **13 / 50** |
| Named in "lowest dev fee" answers (q6, 4 LLMs + AIO) | **4 / 5**, shown as the lowest or near-lowest at 1.5% | **0 / 5** |
| Named on ChatGPT for firmware prompts (q1–q6, q9, q10) | **3 / 8** | **0 / 8** |

\* ChatGPT q8 (immersion cooling) names "BiXBiT … Europe", backed only by a google.com/maps search link. bixbit.io is cited **0/11** on ChatGPT.

**Change since June:**
- The June "ePIC 7/10 vs BiXBiT 0/10" was a Claude self-test on prompts that were mostly ePIC-branded. It is **not supported** by today's measurement.
- Measured today, BiXBiT leads overall, 13 vs 7 named.
- ePIC still **owns two high-intent slots:**
  1. **The dev-fee question.** Every engine ranks ePIC UMC OS at 1.5% as lowest or near-lowest, and BiXBiT is never named.
  2. **ChatGPT.** ePIC appears in 3 firmware answers; BiXBiT appears in 0 firmware answers and 0 citations.

### LLM Mentions DB (historical sample, US)

| Platform | ePIC (epicblockchain.io) | BiXBiT |
|---|---|---|
| Google AIO, domain in sources | 2 queries ("epic miner" and "epic-miner", ambiguous with Epic Cash) | **49 queries**: S19/L7 profitability, "asic monitoring" → `/en/ams`, "container miner" → `/en/products/container`, immersion oil, ERC-20 wallets. **0 firmware queries** |
| ChatGPT, domain anywhere | 0 | 0 for bixbit.io; **3 answers cite `bixbit.tech`**, a mirror of the S19 profitability post |

This means the historical corpus cites BiXBiT for **informational blog content, not firmware**. `bixbit.tech` splits the entity: ChatGPT attributes the content to "bixbit.tech". `[VERIFY: is bixbit.tech an official mirror? If so, canonical to bixbit.io / 301]`

---

## 2. Query × engine matrix

Legend:
- **E** = ePIC named in text; **e** = epicblockchain.io cited
- **B** = BiXBiT named; **b** = bixbit.io cited
- `—` = neither

| # | Prompt (LLM) / keyword (AIO) | ChatGPT | Perplexity | Claude | Gemini | Google AIO | Key sources cited |
|---|---|---|---|---|---|---|---|
| q1 | Best custom firmware for Antminer 2026 / "best antminer firmware" | **E e** | B b, plus e cited but not used in text | B b | — | — (bixbit #13 organic) | d-central.tech, braiins.com, hashrateindex.com, hashrate.farm, emcd.io, spark.money, vnish.* |
| q2 | Custom firmware for Whatsminer M30/M50/M60 / "custom firmware whatsminer" | — | B b | B b | B b | **B b** (bixbit #1 organic) | bixbit.io (m3x/m5x/m6x), asicdip.com, vnish.farm, blockspace.media, einpresswire.com |
| q3 | Best autotuning (J/TH) / "antminer autotuning firmware" | — | — | — | — | — (epic #3 organic, "perpetual tune") | d-central.tech, vni.sh, braiins.com, hashrateindex.com, altairtech.io (AIO) |
| q4 | Alternatives to Braiins OS+ / "braiins os alternative" | **E** (cites spark.money) | — | — | B b | — | d-central.tech, emcd.io, spark.money, slashdot.org, sourceforge.net, gitnux.org |
| q5 | Compare ASIC firmware providers / "asic firmware comparison" | — | B b (offer only) | **E e** | — | **B b** (AIO table column "Bixbit Firmware") | d-central.tech, hashrateindex.com, spark.money, emcd.io, obm.io |
| q6 | Lowest dev fee / "antminer firmware dev fee" | **E e** | **E e** | **E** | **E e** | — | **d-central.tech, spark.money, prnewswire.com (ePIC 1.5% PR), vnish.group, github.com** |
| q7 | Fleet monitoring software / "mining farm monitoring software" | — | — | — | — | — | hashrateindex.com, awesomeminer.com, braiins.com, minersme.cloud, nonce.app, minerstat.com |
| q8 | Immersion cooling providers / "immersion cooling bitcoin mining" | B (Maps link only) | — | B b | B b | — | liquidstack.com, grcooling.com, kelvion.com, marketsandmarkets.com, bitdeer.com, engineeredfluids.com |
| q9 | Is custom firmware safe / no backdoors | — | B b | — | — | b (ref `/en/firmwares`, bixbit #9 organic) | d-central.tech, viabtc.com, theminingshop.co.uk, vni.sh, arxiv.org |
| q10 | Firmware for a 10k S19/S21 fleet to cut power | — | — | — | — | — (run A: bixbit ref, #2 organic; run B: none) | d-central.tech, awesomeminer.com, braiins.com, hashrateindex.com, vnish.pro, nonce.app |
| q11 | *(branded)* What is ePIC UMC OS | E e | E e | E e | E e | E e (epic #1, #2, #8 organic) | epicblockchain.io, prnewswire.com, einnews/einpresswire, altairtech.io, github.com. **BiXBiT is never offered as an alternative** |

### Verbatim anchors (quotes ≤ 20 words; full text in the data files)

**ePIC**
- ChatGPT q1: "ePIC offers the Universal Mining Controller Operating System (UMC OS), a custom firmware designed for Antminer S19x and S21"
- Perplexity q6: "ePIC UMC OS has the lowest published dev fee at 1.5%"
- Claude q6: "For a production-ready option with the lowest fee, ePIC UMC OS at 1.5%"

**BiXBiT**
- Perplexity q1: "BiXBiT — offers custom ASIC firmware for Antminer, but the search results here provide less comparative evidence"
- Gemini q2: "BiXBiT is one of the earliest and most consistent providers of custom firmware for WhatsMiner machines."
- AIO q2: "rare compared to Bitmain AntMiner, but options like BiXBiT and recent third-party releases by Luxor"

**Attribution risks**

The engines state ePIC facts that conflict with each other. All are `[VERIFY]` and none should be repeated in BiXBiT copy:
- **Dev fee:** 1.5%, reduced from 2.5% in January 2026 (ChatGPT q1). d-central calls 1.5% "firmware-only" and says the UMC board has no recurring fee.
- **Other names and fees:** Claude q5 mentions "AltairOS … 2.2% developer fee".
- **Headquarters:** Claude q5 says "Toronto, Canada".
- **Model support:** "S19j and newer" vs "S19x and S21".
- **Stratum V2:** ChatGPT q11 says UMC OS "does not support Stratum V2".
- **Maturity:** d-central lists UMC OS as "MATURITY: EXPERIMENTAL".

---

## 3. Source-domain gap: sources that name ePIC but not BiXBiT

Counts are the number of the 44 LLM answers plus 11 AIOs where the domain was cited in an answer that names or cites ePIC but does not name or cite BiXBiT. Whether each page names each brand was checked by WebFetch on 2026-09-25 where marked.

| # | Domain / URL | Gap count | ePIC on page | BiXBiT on page | Why it matters | Priority | Action (white-hat only) |
|---|---|---|---|---|---|---|---|
| 1 | **d-central.tech**: `/firmware-comparison/`, `/bitcoin-mining-software-comparison/`, `/braiins-os-vs-vnish-vs-luxos-…-2026/`, `/antminer-s19-firmware-guide-…/` | 8 | **Yes** (WebFetch: "ePIC UMC OS … 1.5% firmware-only dev fee"; "ePIC Firmware (ePIC Blockchain)") | **No** (WebFetch, both pages) | The most-cited third-party source on every engine: cited in 7 BiXBiT answers too, but it never names BiXBiT | **P0** | Editorial pitch: a Whatsminer-firmware angle (the gap in their tables) plus a factual data sheet (models, dev fee 2.8% / 2% M2x, rollback, autotune). Offer test units or a changelog. No paid placement disguised as editorial |
| 2 | **spark.money**: `/tools/bitcoin-mining-firmware-comparison` | 4 | **Yes**: "Among aftermarket options, ePIC UMC OS charges 1.5%." | **No** (WebFetch) | ChatGPT's main third-party source for ePIC (q4, q6, q11). It holds a structured dev-fee table | **P0** | Submit a correction or addition request with a public spec source (a BiXBiT dev-fee/spec page, see §4) |
| 3 | **prnewswire.com** / **einpresswire.com** / **einnews.com** | 4 + 2 | Yes (ePIC UMC OS 1.5% dev-fee press release; universal controller release) | BiXBiT has a 2024 prweb release (Cormint/ERCOT) that no engine cited today | The wire release is the primary evidence LLMs cite for "lowest dev fee" | **P1** | Issue a factual wire release on a real milestone (Whatsminer M6x support, fleet count, dev-fee terms). No revenue claims. `[VERIFY: milestone facts]` |
| 4 | **github.com** (ePIC repos; DCENT_OS) | 3 | Yes (ePIC org repos, per the June report) | No BiXBiT org found in June `[VERIFY today]` | Crawled and used as trust or open-source evidence for "safe / no backdoors" answers | **P1** | Publish a real repo: AMS API client or examples, a firmware changelog, a checksum/signature verification guide. Only if engineering signs off |
| 5 | **hashrateindex.com** (Luxor) | 2 (gap), 5 (in BiXBiT answers) | Cited in the June report for "Top 5 firmware" with ePIC `[VERIFY today]` | Not verified | High-authority data publisher; cited on q3, q5, q7, q10 | **P1** | Pitch data or contributor content (Whatsminer tuning, immersion). Owned by competitor Luxor, so expect limited uptake |
| 6 | **altairtech.io** | 2 | Yes (ePIC hardware reseller) | — | Reseller pages act as independent corroboration | **P2** | Get BiXBiT firmware listed on distributor or reseller pages (bixbitusa.io, HODL Ranch, container resellers), with consistent naming |
| 7 | **vnish.group / emcd.io / slashdot.org / sourceforge.net / gitnux.org / worldmetrics.org** | 1–2 each | Mixed | Not verified | Listicle and directory sources for "alternatives to Braiins" (q4) | **P2** | Claim or create listings on SourceForge/Slashdot (a legitimate vendor profile) and pitch emcd.io's firmware comparison. `[VERIFY: whether emcd.io names BiXBiT]` |
| 8 | **youtube.com** ("ePIC UMC improves hashrate with no Dev fee", VoskCoin reviews) | AIO q11 + LLM Mentions DB | Yes | A BiXBiT overclocking-guide video exists (June) | Video is cited in AIO | **P3** | Publish transcribed technical videos (Whatsminer flashing, autotune walkthrough) |
| — | epicblockchain.io (own site) | 9 | — | — | ePIC's own spec page `/product/umc-os/` is cited directly for the dev fee | **P0 (mirror it)** | BiXBiT needs an equivalent single citable spec/dev-fee page (see §4) |

**Not gaps: sources where BiXBiT is already cited (defend these):**
- bixbit.io Whatsminer pages (`/whatsminer-series-m3x`, `/m5x`, `/m6x`): Whatsminer is BiXBiT's clearest win, across 4/5 engines.
- `/en/firmwares` and `/en/firmwares/antminer`.
- `/en/asics-cooling/immersion-systems` and `/en/products/container-1k`.

---

## 4. Passage / citability recommendations (only what closes this gap)

Priorities:
1. The dev-fee slot.
2. ChatGPT absence.
3. Antminer-comparison presence.
4. The "safe / no backdoor" slot.

### P0-1: Create one citable fact block for "BiXBiT firmware dev fee and supported models"

**Why:** ePIC wins q6 on every engine because a single page states "1.5% dev fee" in plain text, and three third-party pages repeat it. BiXBiT's published fee (2.8%, 2% on M2x; confirmed in the 2026-09 baseline) does not surface in any of the 50 answers.

**Where:** `/en/firmwares`, near the top, plus an identical block on `/en/firmwares/antminer` and each `/whatsminer-series-*` page.

**Format:** a plain HTML table, not an image or JS widget.

| Field | Value |
|---|---|
| Dev fee (Antminer) | 2.8% `[VERIFY current]` |
| Dev fee (Whatsminer M2x) | 2% `[VERIFY current]` |
| Dev fee (Whatsminer M3x/M5x/M6x) | `[VERIFY]` |
| Supported Antminer models | `[VERIFY list]` |
| Supported Whatsminer models | `[VERIFY list]` |
| Autotuning | `[VERIFY: per-chip / per-board]` |
| Rollback to stock | `[VERIFY]` |
| Immersion / hydro mode | `[VERIFY]` |

**Rules:**
- Answer-first sentence: "BiXBiT firmware charges a 2.8% dev fee on Antminer and 2% on Whatsminer M2x `[VERIFY]`; it supports …"
- **Do not claim "lowest dev fee".** It would be false against ePIC's reported 1.5% and DCENT_OS's 0%.
- Differentiate on facts BiXBiT can prove, e.g., Whatsminer coverage, which ePIC and d-central's tables lack.

### P0-2: Whatsminer-first positioning in the opening passage of `/en/firmwares`

**Why:** Whatsminer is the only query where BiXBiT wins on every engine and in AIO (organic #1). On ePIC's branded query (q11), no engine offers BiXBiT as an alternative.

**Change:** the first 2 sentences should define the entity. Suggested wording: "BiXBiT is a custom firmware for Antminer and Whatsminer ASICs (M2x–M6x) with autotuning and fleet management via AMS." `[VERIFY wording with product owner]`
- Reuse the same canonical sentence in `llms.txt` and in Organization/SoftwareApplication schema. The 2026-09-16 audit found the sitewide schema description is cooling ad copy; fix it at the same time.

### P1-3: An ASIC firmware comparison page, `/en/firmwares/comparison` (new)

**Why:**
- q1, q4, q5 and q10 answers are built from comparison tables (d-central, spark.money, emcd.io).
- Perplexity q1 explicitly says BiXBiT has "less comparative evidence".
- The AIO for q5 already renders a "Bixbit Firmware" column, but it is sourced from a 2021 blog post.

**Content:**
- An objective table: Braiins OS+, VNish, LuxOS, ePIC UMC OS, BiXBiT.
- Columns: dev fee, Antminer models, Whatsminer models, autotune, rollback, open-source status, fleet software.
- Each competitor cell links to that vendor's own public page as the source.
- **Mark every competitor figure `[VERIFY]`** until checked against the vendor page on the publication date.
- Add "last verified" dates.

### P1-4: A security / "no backdoor" passage and FAQ

**Why:** q9 is split between Braiins (open-source) and generic advice. BiXBiT is cited there by Perplexity and AIO (`/en/firmwares`), but with no specific claim.

**Change:**
- Add a Q&A: "Is BiXBiT firmware safe? Does it contain backdoors?"
- Answer with verifiable facts only: signed builds, checksum publication, rollback, what the dev fee connects to (pool/stratum destination).
- Every fact is `[VERIFY with engineering]`; publish only what is provable.
- Mark it up as FAQPage. `/en/firmwares` currently ships an empty `FAQPage mainEntity: []` (2026-09-16 audit). Fix that.

### P1-5: Resolve the `bixbit.tech` duplicate

ChatGPT cites `bixbit.tech/en/blog/...` (3 answers in the LLM Mentions DB), not bixbit.io.
- Consolidate with a 301 or cross-domain canonical to bixbit.io so citations accrue to the main entity. `[VERIFY domain ownership / purpose]`

### P2-6: Monitoring (q7) and autotuning (q3)

Neither brand appears in these answers, so this is not an ePIC gap.
- `/en/ams`: add a spec passage (max devices, supported firmware/brands, alerting, API) as a table `[VERIFY]`.
- Get listed on hashrateindex.com / d-central's "ASIC management software" list; d-central's `/complete-list-of-bitcoin-asic-management-software/` is cited in AIO.

### Infrastructure: carried over, not re-verified today (curl denied)

- **`/llms.txt`:** 404 as of 2026-09-16. The draft is `content/geo/llms.txt`, which has 4 stale URLs.
  - Ship it after fixing the URLs, with a "Firmware facts" section that mirrors the P0-1 table.
  - ePIC also had no llms.txt in June, so this is a cheap differentiator.
- **robots.txt:** AI crawlers are implicitly allowed and nothing blocks them. An explicit allow for GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot and Google-Extended is P2 (proposal in `content/dev-task-p0.md` §3.5).

---

## 5. Plan

| Priority | Action | Owner | Effort | Closes |
|---|---|---|---|---|
| P0 | Dev-fee and model fact table on `/en/firmwares`, `/antminer` and Whatsminer pages (HTML, `[VERIFY]` values) | content + product | S | q6 on all engines, and ChatGPT absence |
| P0 | Canonical entity sentence (Antminer + Whatsminer) in the opener, schema and llms.txt; deploy the fixed llms.txt | content + dev | S | q1, q4, q11 alternatives |
| P0 | Outreach to d-central.tech (firmware-comparison + software-comparison) and spark.money (firmware comparison) with the public fact sheet | off-page | M | 8 + 4 gap citations |
| P1 | `/en/firmwares/comparison` page with sourced competitor cells | content | M | q1, q4, q5, q10 |
| P1 | Security/backdoor FAQ plus a working FAQPage schema | content + eng | S | q9 |
| P1 | Factual wire release (prnewswire/einpresswire) on a real product milestone | PR | S | The q6 evidence chain |
| P1 | bixbit.tech → bixbit.io consolidation | dev | S | ChatGPT attribution |
| P1 | Public GitHub (AMS API examples, checksum verification) if engineering agrees | eng | M | q9, trust signals |
| P2 | SourceForge/Slashdot vendor listings; reseller/distributor listings; `/en/ams` spec table | off-page + content | S–M | q4, q7 |
| P3 | Transcribed YouTube technical walkthroughs | marketing | M | AIO video slots |

**Re-measure:** re-run the same 11 prompts × 5 engines after the P0 items ship (about 4–6 weeks). The prompts are stored in the data JSONs. The cost of this run was about $2.25 in total.

**Guardrails:**
- No fabricated specs; every `[VERIFY]` value needs product sign-off.
- No "lowest fee" or other claims BiXBiT cannot prove.
- No profitability promises.
- No paid or disguised placements or mention spam.
