# Topic Cluster: Immersion Cooling Mining
**Site:** https://bixbit.io/en
**Cluster slug:** immersion-cooling-mining
**Created:** 2026-06-19
**DataForSEO status:** 401 — search volumes unavailable. Volumes marked N/A. No fabricated data.
**Priority:** P1 (CLAUDE.md §3 — second after ASIC firmware clusters)

---

## Cluster Purpose

Establish BiXBiT as a credible B2B vendor for industrial-scale immersion cooling infrastructure targeting operators running 100–100,000+ ASICs. Differentiate from pure hardware vendors (LiquidStack, GRC, Engineered Fluids) by leading with the firmware-cooling integration angle — BiXBiT is the only vendor in this SERP space that ships both immersion cooling hardware and custom firmware (Antminer + Whatsminer) designed to leverage immersion thermal headroom.

---

## Hub-and-Spoke Architecture

### Hub (Pillar Page)
| Attribute | Value |
|---|---|
| Slug | `/en/immersion-cooling-mining` |
| Primary keyword | `immersion cooling mining` |
| Secondary keywords | `ASIC immersion cooling`, `bitcoin miner immersion cooling`, `immersion cooled bitcoin miner`, `mining immersion cooling system` |
| Intent | Commercial investigation — operator evaluating whether to deploy immersion and which vendor/system to choose |
| Schema | `Product` + `FAQPage` |
| Word count target | 3,000–3,500 |
| Brief | `content/briefs/immersion-cooling-mining-pillar.md` |

### Spoke Pages

| # | Slug | Primary Keyword | Intent | Schema | Priority | Brief |
|---|---|---|---|---|---|---|
| 1 | `/en/immersion-cooling-mining/vs-air-cooling` | `immersion cooling vs air cooling mining` | Informational / comparison | `Article` + `FAQPage` | P1 | `immersion-cooling-vs-air-cooling.md` |
| 2 | `/en/immersion-cooling-mining/single-phase` | `single phase immersion cooling mining` | Informational / commercial | `Article` + `FAQPage` | P1 | `single-phase-immersion-cooling.md` |
| 3 | `/en/immersion-cooling-mining/two-phase` | `two phase immersion cooling mining` | Informational / commercial | `Article` + `FAQPage` | P1 | `two-phase-immersion-cooling.md` |
| 4 | `/en/immersion-cooling-mining/dielectric-fluid` | `immersion cooling dielectric fluid` | Informational | `Article` + `FAQPage` | P2 | `immersion-cooling-dielectric-fluid.md` |
| 5 | `/en/immersion-cooling-mining/setup-guide` | `ASIC immersion cooling setup` | Informational / transactional | `HowTo` + `FAQPage` | P1 | `immersion-cooling-asic-setup.md` |
| 6 | `/en/immersion-cooling-mining/roi` | `immersion cooling ROI mining` | Commercial investigation | `Article` + `FAQPage` | P1 | `immersion-cooling-roi.md` |
| 7 | `/en/immersion-cooling-mining/data-center` | `immersion cooling data center mining` | Commercial investigation | `Article` + `FAQPage` | P2 | `immersion-cooling-data-center.md` |
| 8 | `/en/immersion-cooling-mining/antminer` | `immersion cooling Antminer` | Commercial / transactional | `Product` + `FAQPage` | P0 | `immersion-cooling-antminer.md` |
| 9 | `/en/immersion-cooling-mining/whatsminer` | `immersion cooling Whatsminer` | Commercial / transactional | `Product` + `FAQPage` | P0 | `immersion-cooling-whatsminer.md` |
| 10 | `/en/immersion-cooling-mining/tank` | `mining immersion tank` | Commercial investigation | `Product` + `FAQPage` | P1 | `immersion-cooling-tank.md` |
| 11 | `/en/immersion-cooling-mining/pue` | `immersion cooling PUE data center` | Informational | `Article` | P2 | *(defer — low commercial value for BiXBiT's ICP at this stage)* |

**Total active briefs: 10** (PUE page deferred — low product tie-in for current BiXBiT product scope).

---

## Competitor Gap Analysis

### Who ranks in this SERP space
- **LiquidStack** — strong product pages, weak on ROI calculators and firmware integration content
- **Engineered Fluids** — deep technical content on dielectric fluids, weak on ASIC-specific setup and operator TCO
- **GRC (Green Revolution Cooling)** — strong on data center / enterprise angle, minimal Bitcoin mining specifics
- **DCX** — thin content overall, few guides
- **Braiins / Vnish / LuxOS** — firmware vendors with no immersion cooling content at all

### BiXBiT content gaps to exploit
1. **Firmware + immersion integration** — nobody covers "what firmware settings to use in immersion" as a dedicated page. BiXBiT is uniquely positioned here.
2. **Mid-scale ROI (100–5,000 ASIC)** — LiquidStack targets hyperscale (5,000+ ASIC); GRC targets enterprise IT. The 100–5,000 ASIC mining operator segment is underserved.
3. **Model-specific pages** (immersion cooling for Antminer S19/S21, Whatsminer M50/M60) — no competitor owns these SERP slots.
4. **Immersion tank buying guide** — informational with commercial intent; nobody does a thorough, brand-neutral guide that positions their own product.
5. **Single-phase vs two-phase decision guide** — existing content is generic; BiXBiT can anchor it to real mining operator decisions.

---

## Cross-Cluster Integration Points

### Immersion Cooling → Antminer Firmware Cluster
| Immersion Cooling Page | Target Firmware Page | Rationale |
|---|---|---|
| `/en/immersion-cooling-mining` (pillar) | `/en/antminer-firmware/overclocking` | Immersion unlocks sustained overclock |
| `/en/immersion-cooling-mining` (pillar) | `/en/antminer-firmware` | BiXBiT firmware optimized for immersion |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware` | Primary CTA — pair hardware with firmware |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/overclocking` | Immersion-specific overclock profiles |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/antminer-s19` | S19 immersion deployment |
| `/en/immersion-cooling-mining/antminer` | `/en/antminer-firmware/antminer-s21` | S21 / S21 Hydro deployment |
| `/en/immersion-cooling-mining/setup-guide` | `/en/antminer-firmware/install` | Firmware install is part of immersion setup |
| `/en/immersion-cooling-mining/roi` | `/en/antminer-firmware/undervolting` | Efficiency gains compound ROI |

### Immersion Cooling → Whatsminer Firmware Cluster
| Immersion Cooling Page | Target Firmware Page | Rationale |
|---|---|---|
| `/en/immersion-cooling-mining` (pillar) | `/en/whatsminer-firmware/overclocking` | Immersion unlocks sustained Whatsminer overclock |
| `/en/immersion-cooling-mining` (pillar) | `/en/whatsminer-firmware` | BiXBiT Whatsminer firmware for immersion |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware` | Primary CTA — pair hardware with firmware |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware/overclocking` | Immersion-specific overclock profiles |
| `/en/immersion-cooling-mining/whatsminer` | `/en/whatsminer-firmware/whatsminer-m50` | M50/M60 immersion deployment |
| `/en/immersion-cooling-mining/setup-guide` | `/en/whatsminer-firmware/install` | Firmware install is part of immersion setup |
| `/en/immersion-cooling-mining/roi` | `/en/whatsminer-firmware/undervolting` | Efficiency gains compound ROI |

### Firmware Clusters → Immersion Cooling (already partially in internal-linking.md, extended here)
| Source Firmware Page | Target Immersion Page | Anchor Text |
|---|---|---|
| `/en/antminer-firmware/overclocking` | `/en/immersion-cooling-mining` | "immersion cooling for sustained overclocking" |
| `/en/antminer-firmware/undervolting` | `/en/immersion-cooling-mining` | "immersion cooling extends undervolt headroom" |
| `/en/antminer-firmware/custom` | `/en/immersion-cooling-mining` | "custom firmware for immersion deployments" |
| `/en/antminer-firmware/antminer-s21` | `/en/immersion-cooling-mining/antminer` | "immersion cooling for Antminer S21" |
| `/en/whatsminer-firmware/overclocking` | `/en/immersion-cooling-mining` | "immersion cooling for sustained Whatsminer overclocking" |
| `/en/whatsminer-firmware/undervolting` | `/en/immersion-cooling-mining` | "immersion cooling extends Whatsminer undervolt headroom" |
| `/en/whatsminer-firmware/whatsminer-m50` | `/en/immersion-cooling-mining/whatsminer` | "immersion cooling for Whatsminer M60" |

---

## Content Production Priority

| Priority | Page | Rationale |
|---|---|---|
| P0 | Pillar: `/en/immersion-cooling-mining` | Hub required before spokes can rank; product-level commercial page |
| P0 | `/en/immersion-cooling-mining/antminer` | Highest commercial intent; cross-links to existing Antminer firmware cluster |
| P0 | `/en/immersion-cooling-mining/whatsminer` | Same rationale for Whatsminer cluster |
| P1 | `/en/immersion-cooling-mining/vs-air-cooling` | High informational volume; top-of-funnel entry point |
| P1 | `/en/immersion-cooling-mining/roi` | Bottom-funnel commercial; operator decision driver |
| P1 | `/en/immersion-cooling-mining/setup-guide` | Transactional intent; pairs with firmware install guides |
| P1 | `/en/immersion-cooling-mining/single-phase` | Comparison intent, mid-funnel |
| P1 | `/en/immersion-cooling-mining/tank` | Commercial investigation; buyer's guide format |
| P2 | `/en/immersion-cooling-mining/two-phase` | Narrower audience; high technical depth required |
| P2 | `/en/immersion-cooling-mining/dielectric-fluid` | Informational; supports E-E-A-T but lower conversion |
| P2 | `/en/immersion-cooling-mining/data-center` | Broader intent; relevant for DC operator ICP segment |
