# Content Brief: Immersion Cooling Mining — Pillar Page
**Slug:** `/en/immersion-cooling-mining`
**Cluster:** immersion-cooling-mining
**Brief type:** Hub / Pillar
**Created:** 2026-06-19
**Author assignment:** Senior engineer with immersion deployment experience [VERIFY: assign real author name]

---

## Page Goal

Commercial product/category page that converts operators evaluating immersion cooling. Positions BiXBiT as the only vendor offering both immersion cooling hardware and custom ASIC firmware (Antminer + Whatsminer) tuned for immersion thermal conditions — a differentiation no competitor (LiquidStack, GRC, Engineered Fluids) can claim.

---

## Search Intent

**Primary intent:** Commercial investigation — operator comparing cooling approaches and shortlisting vendors before a capital purchase.

**Secondary intent:** Informational — engineer/CTO validating technical fit before recommending to procurement.

**Do NOT optimize for:** Pure informational "what is immersion cooling" queries (those are served by the vs-air-cooling and single-phase spokes).

---

## Target Keywords

| Type | Keyword | Volume |
|---|---|---|
| Primary | `immersion cooling mining` | N/A (DataForSEO 401) |
| Secondary | `ASIC immersion cooling` | N/A |
| Secondary | `bitcoin miner immersion cooling` | N/A |
| Secondary | `immersion cooled bitcoin miner` | N/A |
| Secondary | `mining immersion cooling system` | N/A |
| Long-tail | `industrial immersion cooling for bitcoin mining` | N/A |

---

## H1

`Immersion Cooling for Bitcoin Mining: Industrial Systems for ASIC Fleets`

---

## Page Structure

### H2: Why Immersion Cooling Changes the Economics of ASIC Mining
- Core value proposition: thermal limit removal, sustained hash rate, reduced downtime
- 2–3 quantified claims: [VERIFY: PUE figures for immersion vs air cooling — BiXBiT internal data or published benchmarks. Typical published range: PUE 1.03–1.10 for immersion vs 1.4–1.6 for air. Verify before publishing.]
- [VERIFY: BiXBiT's own PUE and heat dissipation specs for their immersion system]
- Brief comparison hook → links to `/en/immersion-cooling-mining/vs-air-cooling`

### H2: How BiXBiT Immersion Cooling Works
- System overview: tank, dielectric fluid, heat exchanger, CDU
- Single-phase vs two-phase decision point → links to both spoke pages
- [VERIFY: exact system configuration BiXBiT ships — tank capacity (kW/tank), coolant flow rate, rack density supported]
- Schematic or diagram placeholder [VERIFY: engineering diagram available?]

### H2: Supported ASIC Hardware
- Antminer models (S19 series, S21 series, S21 Hydro) [VERIFY: full compatibility matrix from BiXBiT engineering team]
- Whatsminer models (M30S, M50 series, M60 series) [VERIFY: full compatibility matrix]
- Internal links: `/en/immersion-cooling-mining/antminer`, `/en/immersion-cooling-mining/whatsminer`

### H2: BiXBiT Firmware Integration — The Immersion Advantage
**This is the primary differentiation section — no competitor has this.**
- Custom firmware profiles tuned for immersion thermal envelope: higher clock targets, aggressive voltage scaling possible due to stable junction temperatures
- [VERIFY: specific overclock headroom unlocked by immersion vs air on S19/S21 — J/TH targets, TH/s increase. Do not publish without engineering verification.]
- [VERIFY: does BiXBiT firmware include immersion-specific operating profiles as a named feature?]
- Links: `/en/antminer-firmware/overclocking`, `/en/whatsminer-firmware/overclocking`

### H2: System Configurations — 100 to 100,000 ASIC
- Scale tiers: small farm (100–500 ASIC), mid-scale (500–5,000 ASIC), industrial (5,000+ ASIC)
- BiXBiT's addressable range and reference configurations [VERIFY: BiXBiT's standard system unit sizes — kW capacity per tank/rack]
- Key spec table: [VERIFY all]: tanks per MW, fluid volume per tank, electrical capacity per rack, coolant type

### H2: TCO Comparison: Immersion vs Air Cooling at Scale
- CapEx / OpEx framing
- Variables: electricity ($/kWh), ASIC count, air cooling baseline OpEx
- [VERIFY: BiXBiT published TCO model or reference numbers]
- Link to ROI spoke: `/en/immersion-cooling-mining/roi`

### H2: Implementation: From Site Survey to First Hash
- High-level deployment timeline (weeks, not days — realistic B2B framing)
- Site requirements: [VERIFY: floor load (kg/m²), electrical supply (3-phase requirements), fire suppression compatibility with dielectric fluids]
- Link to setup guide: `/en/immersion-cooling-mining/setup-guide`

### H2: Frequently Asked Questions
(See FAQ section below)

---

## Key Entities and Terms to Include

| Term | Context |
|---|---|
| Dielectric fluid | Coolant type; explain mineral oil vs engineered fluids briefly, link to spoke |
| Single-phase immersion cooling | Phase change distinction; link to spoke |
| Two-phase immersion cooling | Phase change distinction; link to spoke |
| PUE (Power Usage Effectiveness) | Efficiency metric; requires verified figures |
| TCO (Total Cost of Ownership) | Primary commercial framing metric |
| kW/rack | Rack density metric for scale comparison |
| Junction temperature (Tj) | ASIC thermal management metric |
| J/TH (joules per terahash) | Efficiency metric throughout |
| Antminer S19 / S21 / S21 Hydro | Specific ASIC models; cross-link to firmware pages |
| Whatsminer M50 / M60 | Specific ASIC models; cross-link to firmware pages |
| Heat exchanger / CDU (coolant distribution unit) | Hardware component terms |
| Thermal throttling | Problem that immersion eliminates |
| Dev fee | Mention in context of BiXBiT firmware transparency |

---

## FAQ (5–7 Questions)

1. What is immersion cooling for Bitcoin mining and how does it differ from air cooling?
2. Which ASIC miners are compatible with BiXBiT immersion cooling systems?
3. What efficiency gains (J/TH, PUE) can I expect from immersion cooling vs air cooling? [VERIFY: answer requires real data]
4. What facility requirements are needed to deploy an immersion cooling system?
5. Can I use custom firmware with immersion-cooled ASICs?
6. What is the typical ROI timeline for immersion cooling at 500–2,000 ASIC scale?
7. Does BiXBiT offer single-phase and two-phase immersion systems?

---

## E-E-A-T Signals

- Author byline: field engineer or CTO with immersion deployment credits [VERIFY: identify internal author]
- Include: deployment scale references (number of ASICs, MW deployed) [VERIFY: BiXBiT reference deployments]
- Cite specific component specs (kW/tank, fluid type, operating temperature range) [VERIFY all]
- Link to third-party fluid safety data sheets or manufacturer specs if applicable
- Reference specific ASIC model thermal envelopes (°C Tj limits) [VERIFY: Bitmain/MicroBT published specs]

---

## Internal Links

### Outbound (this page → cluster spokes)
| Target | Anchor Text | Placement |
|---|---|---|
| `/en/immersion-cooling-mining/vs-air-cooling` | "immersion vs air cooling comparison" | H2: Why Immersion Cooling section |
| `/en/immersion-cooling-mining/single-phase` | "single-phase immersion cooling" | H2: How It Works section |
| `/en/immersion-cooling-mining/two-phase` | "two-phase immersion cooling" | H2: How It Works section |
| `/en/immersion-cooling-mining/antminer` | "immersion cooling for Antminer" | H2: Supported ASIC Hardware |
| `/en/immersion-cooling-mining/whatsminer` | "immersion cooling for Whatsminer" | H2: Supported ASIC Hardware |
| `/en/immersion-cooling-mining/roi` | "immersion cooling ROI calculator" | H2: TCO Comparison section |
| `/en/immersion-cooling-mining/setup-guide` | "ASIC immersion cooling setup guide" | H2: Implementation section |
| `/en/immersion-cooling-mining/tank` | "immersion cooling tank specifications" | H2: System Configurations |
| `/en/immersion-cooling-mining/dielectric-fluid` | "dielectric fluid selection guide" | H2: How It Works section |

### Cross-cluster outbound (this page → firmware clusters)
| Target | Anchor Text | Placement |
|---|---|---|
| `/en/antminer-firmware/overclocking` | "immersion-optimized Antminer overclocking" | H2: Firmware Integration section |
| `/en/whatsminer-firmware/overclocking` | "immersion-optimized Whatsminer overclocking" | H2: Firmware Integration section |
| `/en/antminer-firmware` | "BiXBiT Antminer firmware" | H2: Firmware Integration section |
| `/en/whatsminer-firmware` | "BiXBiT Whatsminer firmware" | H2: Firmware Integration section |
| `/en/ams` | "AMS fleet monitoring for immersion deployments" | H2: System Configurations section |

### Inbound (firmware cluster pages already link here — see internal-linking.md)
- `/en/antminer-firmware/overclocking` → this page (existing in matrix)
- `/en/antminer-firmware/undervolting` → this page (existing in matrix)
- `/en/antminer-firmware/custom` → this page (existing in matrix)
- `/en/whatsminer-firmware/overclocking` → this page (existing in matrix)
- Homepage → this page [VERIFY: add to navigation once page is live]

---

## Schema Recommendation

```json
{
  "@type": ["Product", "FAQPage"],
  "name": "BiXBiT Immersion Cooling System for ASIC Mining",
  "description": "Industrial immersion cooling systems for Bitcoin ASIC mining farms. Compatible with Antminer and Whatsminer hardware.",
  "brand": {"@type": "Brand", "name": "BiXBiT"},
  "url": "https://bixbit.io/en/immersion-cooling-mining"
}
```
FAQPage schema: include all 7 FAQ pairs as `mainEntity` items.

---

## Word Count Target
3,000–3,500 words. Do not pad. Every section earns its word count with technical specificity.

---

## [VERIFY] Blockers — DO NOT PUBLISH WITHOUT RESOLVING

- [ ] BiXBiT immersion system model name(s) and SKU(s)
- [ ] Tank capacity in kW
- [ ] Supported ASIC model compatibility matrix (full list)
- [ ] PUE figures for BiXBiT immersion system (measured, not theoretical)
- [ ] J/TH improvement achievable with immersion + custom firmware vs air + stock firmware
- [ ] Deployment scale references (MW deployed, client counts)
- [ ] Fluid type used (mineral oil / PAO / engineered fluid — brand/spec)
- [ ] Floor load requirements (kg/m²)
- [ ] Electrical supply requirements
- [ ] Author name + credentials for byline
