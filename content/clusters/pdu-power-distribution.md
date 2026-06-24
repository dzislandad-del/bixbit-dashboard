# Topic Cluster: PDU Power Distribution for Mining
**Site:** https://bixbit.io/en
**Created:** 2026-06-19
**Cluster owner:** Content & Clusters agent
**Status:** Draft — briefs created, pages not yet live

---

## Strategic Rationale

The "PDU for mining" niche is almost entirely unoccupied by specialized content. General-purpose
PDU vendors (Raritan, Vertiv, APC/Schneider, Server Technology, Geist) have no mining-specific
content. Firmware competitors (Braiins, Vnish, LuxOS, ePIC) do not sell PDUs at all.

BiXBiT's managed PDU — with per-outlet remote switching, per-outlet energy metering, and direct
AMS integration — has a genuine product differentiator for mining operators. The SEO opportunity
is to own the "managed PDU + mining" semantic territory before any competitor moves in.

**User journey fit:** Operators who tune firmware (electricity cost focus) naturally need PDU-level
power visibility. The buyer journey runs:
`Firmware tuning → AMS monitoring → Immersion/Hydro cooling → PDU power distribution`

BiXBiT is the only vendor with assets across all four legs of that journey.

---

## Semantic Groups (by intent)

### Group A — Commercial (bottom-funnel)
- "PDU for mining", "mining PDU", "ASIC PDU"
- "managed PDU for Bitcoin mining"
- "smart PDU mining farm"
- "PDU remote switching ASIC"
- "BiXBiT PDU", "BiXBiT power distribution"
- "managed PDU for data center mining"

### Group B — Technical / Informational (mid-funnel)
- "PDU per-outlet metering mining"
- "PDU per-outlet switching ASIC farm"
- "PDU energy metering mining"
- "PDU remote reboot ASIC"
- "ASIC power management PDU"
- "PDU overload protection mining"
- "PDU circuit breaker ASIC rack"

### Group C — Comparison / Decision (mid-funnel)
- "PDU vs direct wiring mining"
- "managed PDU vs unmanaged PDU mining"
- "smart PDU vs basic PDU ASIC"
- "Raritan vs BiXBiT PDU mining"
- "APC PDU for Bitcoin mining"

### Group D — Educational / Awareness (top-funnel)
- "power distribution unit mining farm"
- "mining farm power distribution"
- "how to wire ASIC mining farm"
- "mining farm electrical design"
- "PDU sizing for ASIC mining"
- "kW per rack Bitcoin mining"

### Group E — Integration / Stack (mid-to-bottom funnel)
- "PDU AMS integration"
- "PDU monitoring software mining"
- "PDU ASIC power consumption tracking"
- "remote PDU management mining fleet"
- "PUE optimization mining data center"

---

## Hub-and-Spoke Structure

```
                    ┌─────────────────────────────────────────┐
                    │  PILLAR: /en/pdu                         │
                    │  "Managed PDU for ASIC Mining Farms"     │
                    │  Intent: commercial + informational       │
                    └──────────────────┬──────────────────────┘
                                       │
          ┌────────────────────────────┼─────────────────────────────┐
          │                            │                             │
          │           ┌────────────────┼────────────────┐            │
          │           │                │                │            │
          ▼           ▼                ▼                ▼            ▼
   /en/pdu/      /en/pdu/       /en/pdu/        /en/pdu/      /en/pdu/
   what-is       per-outlet     remote-         overload-     sizing
   (info)        -metering      switching       protection    (info)
                 (technical)    (technical)     (technical)

          ▼           ▼                ▼                ▼            ▼
   /en/pdu/      /en/pdu/       /en/pdu/        /en/pdu/      /en/pdu/
   vs-direct     vs-unmanaged   ams-            data-center   mining-
   -wiring       -pdu           integration     -mining       electrical-
   (comparison)  (comparison)   (integration)   (commercial)  -design
                                                              (top-funnel)
```

### Pages in cluster (11 total)

| # | URL slug | Type | Intent | Priority |
|---|---|---|---|---|
| 0 | `/en/pdu` | Pillar (hub) | commercial + informational | P0 |
| 1 | `/en/pdu/what-is-pdu-mining` | Spoke | informational | P1 |
| 2 | `/en/pdu/per-outlet-metering` | Spoke | technical informational | P1 |
| 3 | `/en/pdu/remote-switching` | Spoke | technical informational | P0 |
| 4 | `/en/pdu/overload-protection` | Spoke | technical informational | P1 |
| 5 | `/en/pdu/sizing-asic-farm` | Spoke | informational + commercial | P1 |
| 6 | `/en/pdu/vs-direct-wiring` | Spoke | comparison | P1 |
| 7 | `/en/pdu/vs-unmanaged-pdu` | Spoke | comparison | P0 |
| 8 | `/en/pdu/ams-integration` | Spoke | technical + commercial | P0 |
| 9 | `/en/pdu/data-center-mining` | Spoke | commercial | P1 |
| 10 | `/en/pdu/mining-electrical-design` | Spoke | informational | P2 |

---

## Cross-Cluster Connection Points

| PDU page | Connects to | Via topic |
|---|---|---|
| `/en/pdu` pillar | `/en/ams` | PDU sends per-outlet data to AMS dashboard |
| `/en/pdu` pillar | `/en/antminer-firmware` | Firmware controls ASIC power draw visible in PDU metering |
| `/en/pdu` pillar | `/en/whatsminer-firmware` | Same, Whatsminer platform |
| `/en/pdu` pillar | `/en/immersion-cooling-mining` | Immersion deployments have specific PDU requirements (IP rating, high-current) |
| `/en/pdu/ams-integration` | `/en/ams` | Deep integration spoke |
| `/en/pdu/ams-integration` | `/en/ams/mining-farm-power-monitoring` | Direct spoke-to-spoke linkage |
| `/en/pdu/per-outlet-metering` | `/en/ams/mining-farm-power-monitoring` | Both cover power visibility |
| `/en/pdu/remote-switching` | `/en/ams/mining-farm-alerts-automation` | Alert triggers → remote reboot via PDU |
| `/en/pdu/sizing-asic-farm` | `/en/antminer-firmware/undervolting` | Undervolting changes power draw → affects PDU sizing |
| `/en/pdu/data-center-mining` | `/en/immersion-cooling-mining/data-center` | Scale deployments need both |
| `/en/pdu/overload-protection` | `/en/antminer-firmware/overclocking` | Overclocking increases power draw → overload risk |

---

## Priority Publishing Order

1. `/en/pdu` — pillar page (P0, unblock all cross-links from other clusters)
2. `/en/pdu/ams-integration` (P0, enables AMS ↔ PDU cross-links immediately)
3. `/en/pdu/vs-unmanaged-pdu` (P0, highest commercial intent comparison)
4. `/en/pdu/remote-switching` (P0, core product differentiator)
5. `/en/pdu/per-outlet-metering` (P1)
6. `/en/pdu/sizing-asic-farm` (P1)
7. `/en/pdu/what-is-pdu-mining` (P1, top-of-funnel entry point)
8. `/en/pdu/overload-protection` (P1)
9. `/en/pdu/vs-direct-wiring` (P1)
10. `/en/pdu/data-center-mining` (P1)
11. `/en/pdu/mining-electrical-design` (P2)

---

## Schema Types by Page

| Page | Schema type |
|---|---|
| `/en/pdu` | `Product` + `FAQPage` |
| `/en/pdu/what-is-pdu-mining` | `TechArticle` + `FAQPage` |
| `/en/pdu/per-outlet-metering` | `TechArticle` + `FAQPage` |
| `/en/pdu/remote-switching` | `TechArticle` + `HowTo` |
| `/en/pdu/overload-protection` | `TechArticle` + `FAQPage` |
| `/en/pdu/sizing-asic-farm` | `TechArticle` + `HowTo` + `FAQPage` |
| `/en/pdu/vs-direct-wiring` | `TechArticle` + `FAQPage` |
| `/en/pdu/vs-unmanaged-pdu` | `TechArticle` + `FAQPage` (comparison) |
| `/en/pdu/ams-integration` | `TechArticle` + `HowTo` |
| `/en/pdu/data-center-mining` | `Product` + `FAQPage` |
| `/en/pdu/mining-electrical-design` | `TechArticle` + `FAQPage` |

---

## Content Gaps vs. Competitors

| Competitor | PDU content | BiXBiT opportunity |
|---|---|---|
| Braiins OS+ | None — no PDU product | Own entire "mining firmware + PDU" stack narrative |
| Vnish | None | Same |
| LuxOS / Luxor | None | Same |
| ePIC | None | Same |
| Raritan (Legrand) | Generic data center PDU content, no mining specifics | Target "mining PDU" long-tails Raritan does not pursue |
| Vertiv | Generic enterprise content | No mining content whatsoever |
| APC / Schneider | Generic data center PDU guides | No ASIC-specific content |
| Server Technology | Generic high-density PDU content | No mining content |

**Key content gaps to exploit:**
- "PDU for ASIC mining" — no specialized content exists from any vendor
- "managed PDU vs direct wiring for mining" — no comparison content exists
- "PDU sizing for Antminer / Whatsminer" — no model-specific content exists
- "PDU + AMS integration" — BiXBiT is the only vendor who can write this
- "PDU overload protection ASIC farm" — informational, uncontested

---

## E-E-A-T Signals to Build In

- Author: electrical engineer or data center infrastructure engineer (not marketing)
- Cite: NEC (National Electrical Code) references for wiring ampacity rules — `[VERIFY: specific NEC articles]`
- Cite: IEC 62368-1 or IEC 60309 for industrial power connector standards — `[VERIFY: applicable standards]`
- Cite: BiXBiT PDU product specifications (outlets, amperage, form factor) — `[VERIFY: actual specs from product team]`
- Include: real deployment scenario examples (1 MW farm, 10 MW colocation) with PDU count calculations — `[VERIFY: example numbers with product team]`
- Include: comparison table with Raritan, Server Technology, APC — factual spec comparison, no invented numbers — `[VERIFY: competitor specs from public datasheets]`
