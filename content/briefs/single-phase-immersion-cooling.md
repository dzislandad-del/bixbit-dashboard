# Content Brief: Single-Phase Immersion Cooling for Mining
**Slug:** `/en/immersion-cooling-mining/single-phase`
**Cluster:** immersion-cooling-mining
**Brief type:** Spoke — informational/commercial
**Created:** 2026-06-19
**Priority:** P1

---

## Page Goal

Serve operators and engineers researching single-phase immersion cooling as a deployment option. Explain what it is, how it compares to two-phase, and position BiXBiT's single-phase offering. Mid-funnel page: reader understands immersion conceptually but is evaluating which phase-type is right for their operation.

---

## Search Intent

**Primary:** Informational — engineer/CTO understanding the technology before recommending a purchase.
**Secondary:** Commercial investigation — narrowing down single-phase vs two-phase decision.

---

## Target Keywords

| Type | Keyword | Volume |
|---|---|---|
| Primary | `single phase immersion cooling mining` | N/A |
| Secondary | `single phase immersion cooling ASIC` | N/A |
| Secondary | `mineral oil immersion cooling mining` | N/A |
| Secondary | `single phase vs two phase immersion cooling` | N/A |
| Long-tail | `single phase immersion cooling Bitcoin miner setup` | N/A |

---

## H1

`Single-Phase Immersion Cooling for ASIC Mining: How It Works and When to Use It`

---

## Page Structure

### H2: What Is Single-Phase Immersion Cooling?
- Definition: ASIC submerged in dielectric fluid (mineral oil or engineered fluid); fluid stays liquid, heat transferred to external heat exchanger
- Key components: tank/bath, dielectric fluid, CDU (coolant distribution unit), secondary cooling loop
- [VERIFY: BiXBiT's single-phase system configuration — mineral oil vs engineered fluid, CDU specs]

### H2: Single-Phase vs Two-Phase Immersion Cooling
- Phase change principle: two-phase fluid boils at chip surface; single-phase does not
- Practical differences: fluid cost, heat removal capacity per kW, system complexity
- Maintenance implications: fluid top-up, leak risk, decontamination procedures
- [VERIFY: specific operating temperatures for each phase type in BiXBiT's system]
- Link to: `/en/immersion-cooling-mining/two-phase`

### H2: Dielectric Fluid Selection in Single-Phase Systems
- Mineral oil: low cost, widely available, high viscosity challenges at low temperatures
- Synthetic PAO (polyalphaolefin): better low-temp performance, higher cost
- Engineered fluids (e.g., 3M Novec, Calorion): lower viscosity, cleaner handling
- [VERIFY: which fluid type BiXBiT uses or recommends in their single-phase system]
- Link to: `/en/immersion-cooling-mining/dielectric-fluid`

### H2: Technical Specifications — Single-Phase Immersion Systems
[All values in this section require VERIFY before publish]
- [VERIFY: kW/tank capacity for BiXBiT single-phase units]
- [VERIFY: operating fluid temperature range (inlet/outlet)]
- [VERIFY: fluid volume per tank]
- [VERIFY: ASIC capacity per tank (unit count)]
- [VERIFY: secondary cooling loop (dry cooler / chiller / cooling tower options)]
- Rack density achievable: [VERIFY vs air cooling baseline]

### H2: Compatible ASIC Hardware
- [VERIFY: full list of Antminer models compatible with BiXBiT single-phase system]
- [VERIFY: full list of Whatsminer models compatible with BiXBiT single-phase system]
- Fan removal requirement: most ASICs require fan removal before immersion — note safety step
- [VERIFY: does BiXBiT provide fan blanking plates or modified hardware?]
- Links: `/en/immersion-cooling-mining/antminer`, `/en/immersion-cooling-mining/whatsminer`

### H2: Firmware Considerations for Single-Phase Immersion
- Single-phase stable Tj enables aggressive clock targets vs air-cooled defaults
- [VERIFY: specific temperature delta between air-cooled and single-phase immersed Tj under load]
- Per-chip autotuning in BiXBiT firmware leverages stable thermal baseline
- [VERIFY: does BiXBiT firmware include a named single-phase operating profile?]
- Links: `/en/antminer-firmware/autotuning`, `/en/whatsminer-firmware/autotuning`

### H2: Installation and Facility Requirements
- Space: [VERIFY: footprint per tank (m²)]
- Electrical: [VERIFY: 3-phase requirements, amperage per tank]
- Secondary cooling infrastructure: [VERIFY: BTU rejection requirements, dry cooler sizing]
- Fire suppression compatibility: most dielectric fluids are non-flammable [VERIFY: flash point specs]
- Link to: `/en/immersion-cooling-mining/setup-guide`

### H2: Frequently Asked Questions

---

## FAQ

1. What fluid is used in single-phase immersion cooling for Bitcoin mining?
2. How does single-phase immersion cooling differ from two-phase?
3. What ASIC modifications are needed before submerging miners in single-phase immersion tanks?
4. Can I overclock ASICs more aggressively in a single-phase immersion system?
5. What are the maintenance requirements for a single-phase immersion tank?
6. Is single-phase or two-phase immersion cooling better for large-scale mining?

---

## E-E-A-T Signals

- Specific fluid chemistry references (viscosity, flash point, thermal conductivity) [VERIFY]
- Cite fluid manufacturer data sheets where available
- Component-level technical detail on CDU and heat exchanger sizing
- Author: engineer with immersion deployment background [VERIFY]

---

## Internal Links

### Outbound
| Target | Anchor Text | Placement |
|---|---|---|
| `/en/immersion-cooling-mining` | "BiXBiT immersion cooling systems overview" | Intro and CTA |
| `/en/immersion-cooling-mining/two-phase` | "two-phase immersion cooling comparison" | Single vs Two-Phase H2 |
| `/en/immersion-cooling-mining/dielectric-fluid` | "dielectric fluid selection guide" | Fluid Selection H2 |
| `/en/immersion-cooling-mining/antminer` | "Antminer immersion cooling compatibility" | Compatible Hardware H2 |
| `/en/immersion-cooling-mining/whatsminer` | "Whatsminer immersion cooling compatibility" | Compatible Hardware H2 |
| `/en/immersion-cooling-mining/setup-guide` | "ASIC immersion cooling setup guide" | Installation H2 |
| `/en/antminer-firmware/autotuning` | "per-chip autotuning with immersion thermal headroom" | Firmware section |
| `/en/whatsminer-firmware/autotuning` | "Whatsminer autotuning in immersion deployments" | Firmware section |

### Inbound
| Source | Anchor Text |
|---|---|
| `/en/immersion-cooling-mining` (pillar) | "single-phase immersion cooling" |
| `/en/immersion-cooling-mining/vs-air-cooling` | "single-phase immersion systems" |
| `/en/immersion-cooling-mining/two-phase` | "how single-phase differs from two-phase" |

---

## Schema

`Article` + `FAQPage`

---

## Word Count Target
1,600–2,000 words

---

## [VERIFY] Blockers

- [ ] BiXBiT single-phase system model name and specs (kW/tank, fluid volume, ASIC count)
- [ ] Fluid type used (mineral oil / PAO / engineered fluid — name and spec sheet)
- [ ] Operating temperature range (fluid inlet/outlet °C)
- [ ] Antminer and Whatsminer compatibility list for single-phase
- [ ] Fan removal requirements and process
- [ ] Secondary cooling options (dry cooler / chiller / cooling tower)
- [ ] Firmware: does BiXBiT firmware have named single-phase profiles?
