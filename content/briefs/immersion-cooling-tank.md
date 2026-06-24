# Content Brief: Mining Immersion Tank
**Slug:** `/en/immersion-cooling-mining/tank`
**Cluster:** immersion-cooling-mining
**Brief type:** Spoke — commercial investigation / buyer's guide
**Created:** 2026-06-19
**Priority:** P1

---

## Page Goal

Capture buyers researching immersion cooling tanks as the physical product. Operators who know they want immersion cooling and are now evaluating tank specifications, vendors, and what to look for. Positions BiXBiT's tank as the product while providing genuine buyer's guide value (trust builder). No competitor currently owns this SERP slot with ASIC-specific guidance.

---

## Search Intent

**Primary:** Commercial investigation — operator shortlisting immersion tanks and comparing specs.
**Secondary:** Informational — engineer specifying a tank for procurement.

---

## Target Keywords

| Type | Keyword | Volume |
|---|---|---|
| Primary | `mining immersion tank` | N/A |
| Secondary | `bitcoin miner immersion tank` | N/A |
| Secondary | `ASIC immersion cooling tank` | N/A |
| Secondary | `immersion cooling tank mining` | N/A |
| Long-tail | `immersion cooling tank specifications mining` | N/A |
| Long-tail | `how many miners in an immersion tank` | N/A |

---

## H1

`Mining Immersion Cooling Tanks: Specifications, Capacity, and Buyer's Guide`

---

## Page Structure

### H2: What Is an Immersion Cooling Tank?
- Physical description: sealed or open-top bath, constructed from [VERIFY: material — stainless steel / HDPE / other in BiXBiT's product]
- Key components: tank body, fluid containment, ASIC racking system within the tank, plumbing connections (primary fluid loop), lid/cover design
- Single-phase vs two-phase tank differences: [VERIFY: are they the same physical tank or different designs?]

### H2: Key Specifications to Evaluate When Buying an Immersion Tank
Buyer's guide framework — positions BiXBiT as knowledgeable vendor:
1. **Capacity (kW/tank):** [VERIFY: BiXBiT's tank capacity]
2. **ASIC count per tank:** [VERIFY: varies by ASIC form factor — S19/S21/M50]
3. **Fluid volume:** [VERIFY: liters per tank]
4. **Physical dimensions:** [VERIFY: L × W × H (mm or cm)]
5. **Weight (dry and fluid-filled):** [VERIFY: kg — drives structural/floor load decisions]
6. **Plumbing connections:** [VERIFY: connection type and size]
7. **Materials of construction:** [VERIFY: corrosion resistance, fluid compatibility]
8. **Racking system:** how ASICs are held and oriented [VERIFY: BiXBiT's racking approach]
9. **Access design:** lid removal, service access for individual ASIC removal [VERIFY]
10. **Safety features:** overflow protection, pressure relief, fluid containment berm [VERIFY]

### H2: BiXBiT Immersion Tank — Product Specifications
[Complete VERIFY dependency — do not write spec sheet without engineering input]
- Model name/SKU: [VERIFY]
- Capacity (kW): [VERIFY]
- ASIC count (S19/S21): [VERIFY]
- Fluid volume (L): [VERIFY]
- Dimensions (mm): [VERIFY]
- Weight dry / loaded: [VERIFY]
- Construction material: [VERIFY]
- Fluid type compatibility: [VERIFY]
- Connection type: [VERIFY]
- Certifications: [VERIFY: CE, UL, other relevant certifications]

### H2: How Many ASICs Fit in an Immersion Tank?
- Common question — answer it directly with a table [VERIFY all values]
- Variables: ASIC physical dimensions (footprint and depth), spacing requirements, racking density
- [VERIFY: S19 footprint vs S21 footprint vs M50 footprint — Bitmain/MicroBT published physical dimensions]
- Example table:

| ASIC Model | Units per BiXBiT Tank | Notes |
|---|---|---|
| Antminer S19 Pro | [VERIFY] | |
| Antminer S21 | [VERIFY] | |
| Whatsminer M50 | [VERIFY] | |
| Whatsminer M60 | [VERIFY] | |

### H2: Tank vs Rack — Density Comparison
- Air-cooled mining rack: [VERIFY: standard rack dimensions and ASIC count for S19/S21]
- Immersion tank: same floor footprint, higher ASIC density possible [VERIFY: density comparison]
- kW per floor area: [VERIFY: kW/m² for each approach]

### H2: Secondary Cooling Infrastructure for the Tank
- The tank alone doesn't reject heat — it transfers heat to a secondary loop
- Options: dry cooler (air-to-fluid), cooling tower (evaporative), chiller (refrigerative)
- Selection criteria: ambient climate, water availability, target fluid outlet temperature
- [VERIFY: BiXBiT's standard secondary cooling recommendations and compatible equipment]
- Sizing guidance: [VERIFY: BTU/kW factor for BiXBiT's system]

### H2: Ordering and Lead Times
- Single tank vs multi-tank order [VERIFY: BiXBiT MOQ]
- Lead time: [VERIFY: manufacturing and delivery time]
- Deployment support: does BiXBiT provide on-site commissioning? [VERIFY]
- Link to contact/sales CTA

### H2: Frequently Asked Questions

---

## FAQ

1. How many Bitcoin miners fit in an immersion cooling tank?
2. What fluid is used in mining immersion tanks?
3. How much does an immersion cooling tank for Bitcoin mining cost?
4. What size immersion tank do I need for 100 / 500 / 1000 ASICs?
5. How heavy is an immersion cooling tank when filled with fluid?
6. Does an immersion tank come with a racking system for ASICs?
7. What is the maintenance schedule for an immersion cooling tank?

---

## E-E-A-T Signals

- Specific product dimensions and weights (once VERIFY resolved)
- Density comparison table with named ASIC models
- Certifications listed [VERIFY]
- Author: product engineer or technical sales engineer [VERIFY]

---

## Internal Links

### Outbound
| Target | Anchor Text | Placement |
|---|---|---|
| `/en/immersion-cooling-mining` | "BiXBiT immersion cooling systems overview" | Intro + end CTA |
| `/en/immersion-cooling-mining/single-phase` | "single-phase immersion system design" | Tank specs H2 |
| `/en/immersion-cooling-mining/dielectric-fluid` | "immersion cooling fluid selection" | Fluid section |
| `/en/immersion-cooling-mining/setup-guide` | "installation guide for immersion tanks" | Ordering H2 |
| `/en/immersion-cooling-mining/roi` | "total cost of ownership" | Secondary cooling H2 |
| `/en/immersion-cooling-mining/antminer` | "Antminer compatibility" | ASIC count table |
| `/en/immersion-cooling-mining/whatsminer` | "Whatsminer compatibility" | ASIC count table |

### Inbound
| Source | Anchor Text |
|---|---|
| `/en/immersion-cooling-mining` (pillar) | "immersion cooling tank specifications" |
| `/en/immersion-cooling-mining/setup-guide` | "immersion tank specifications" |
| `/en/immersion-cooling-mining/roi` | "tank CapEx" |

---

## Schema

`Product` + `FAQPage`

```json
{
  "@type": "Product",
  "name": "BiXBiT Mining Immersion Cooling Tank",
  "description": "Industrial immersion cooling tank for Bitcoin ASIC mining. Compatible with Antminer and Whatsminer hardware.",
  "brand": {"@type": "Brand", "name": "BiXBiT"},
  "url": "https://bixbit.io/en/immersion-cooling-mining/tank"
}
```

---

## Word Count Target
1,800–2,200 words

---

## [VERIFY] Blockers

- [ ] BiXBiT tank model name and SKU
- [ ] Tank capacity (kW), fluid volume (L), dimensions (mm), dry/loaded weight (kg)
- [ ] ASIC count per tank for S19 Pro, S21, M50, M60
- [ ] Construction material and fluid compatibility
- [ ] Certifications (CE, UL, etc.)
- [ ] Secondary cooling options supported and sizing guidance
- [ ] MOQ and lead time
- [ ] On-site commissioning service availability
- [ ] Floor load (kg/m²) for a fully loaded tank
