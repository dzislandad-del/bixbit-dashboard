# Content Brief: ASIC Immersion Cooling Setup Guide
**Slug:** `/en/immersion-cooling-mining/setup-guide`
**Cluster:** immersion-cooling-mining
**Brief type:** Spoke — how-to / transactional
**Created:** 2026-06-19
**Priority:** P1

---

## Page Goal

Capture bottom-of-funnel "how do I actually do this" intent. Operators who have decided on immersion cooling and are planning a deployment. High trust signal: a detailed, accurate setup guide demonstrates BiXBiT's operational credibility and reduces the perceived risk of buying from them.

Also captures organic traffic from operators who stumble on the guide and haven't yet chosen a vendor — the guide ends with a CTA to BiXBiT's system.

---

## Search Intent

**Primary:** Transactional / informational — operator planning an immersion deployment, needs step-by-step guidance.
**Secondary:** Commercial — using the guide to evaluate whether BiXBiT's system is turnkey or complex.

---

## Target Keywords

| Type | Keyword | Volume |
|---|---|---|
| Primary | `ASIC immersion cooling setup` | N/A |
| Secondary | `how to set up immersion cooling for mining` | N/A |
| Secondary | `immersion cooling mining installation` | N/A |
| Secondary | `bitcoin miner immersion tank setup` | N/A |
| Long-tail | `how to immersion cool an Antminer` | N/A |
| Long-tail | `immersion cooling ASIC step by step` | N/A |

---

## H1

`How to Set Up ASIC Immersion Cooling: Step-by-Step Guide for Mining Operations`

---

## Page Structure

### H2: Before You Start — Site Requirements Checklist
- Floor load capacity: [VERIFY: kg/m² requirement for BiXBiT immersion tanks fully loaded with fluid and ASICs]
- Electrical supply: [VERIFY: 3-phase voltage/amperage spec per tank and per row]
- Secondary cooling loop: [VERIFY: BTU rejection method — dry cooler, cooling tower, or chiller — and sizing guidance]
- Fire suppression compatibility: [VERIFY: is halon/FM-200 compatible with BiXBiT's fluid? Sprinkler interaction?]
- Network infrastructure: [VERIFY: does each ASIC still require ethernet in immersion? Management approach]
- Ventilation: [VERIFY: room ventilation requirements for fluid vapor management]

### H2: Step 1 — Hardware Preparation
- Fan removal from ASICs: standard requirement before immersion [VERIFY: specific procedure for S19, S21, M50, M60 — are there model-specific notes?]
- Fan connector sealing or fan blanks [VERIFY: does BiXBiT supply blanks or are they procured separately?]
- Connector inspection: identify any connectors needing waterproofing treatment [VERIFY: BiXBiT's recommended prep procedure]
- PCB inspection: [VERIFY: any coating or treatment required? Or is fluid compatible with bare PCBs?]
- Label / serial number documentation before submersion (for inventory management)

### H2: Step 2 — Tank Installation and Fluid Fill
- Tank positioning and leveling requirements [VERIFY: tolerance specs]
- Plumbing connections: primary loop connections, flow direction [VERIFY: BiXBiT connection specs]
- Fluid fill procedure: [VERIFY: fill order, fill rate, degassing procedure if applicable]
- Initial fill volume and headspace: [VERIFY: BiXBiT spec]
- Leak test procedure before powering on [VERIFY]

### H2: Step 3 — ASIC Submersion and First Power-On
- Submersion procedure: [VERIFY: any specific orientation requirements, spacing between units]
- Cable management in fluid: [VERIFY: how power cables route — is there a BiXBiT racking system?]
- Power-on sequence: [VERIFY: any required delays between fill and first power-on to allow air evacuation]
- Initial temperature monitoring: target inlet/outlet temperatures [VERIFY: BiXBiT commissioning targets]

### H2: Step 4 — Firmware Configuration for Immersion
**Key differentiator section — BiXBiT owns this angle.**
- Stock firmware vs BiXBiT custom firmware: in immersion, stock firmware may still throttle based on fan-less conditions [VERIFY: does stock Antminer/Whatsminer firmware tolerate fan removal without errors?]
- Installing BiXBiT firmware post-submersion vs pre-submersion [VERIFY: recommended sequence]
- Configuring immersion-optimized profiles: [VERIFY: specific steps in BiXBiT firmware UI for immersion mode]
- Per-chip autotuning in immersion context: let autotuning run for [VERIFY: recommended settling period] before evaluating performance
- Links: `/en/antminer-firmware/install`, `/en/whatsminer-firmware/install`

### H2: Step 5 — AMS Monitoring Configuration
- Connecting immersion-deployed ASICs to AMS dashboard
- Key metrics to monitor in immersion: Tj, hash rate, power draw, fluid inlet/outlet temperatures
- Alert thresholds: [VERIFY: BiXBiT recommended alert thresholds for immersion deployments]
- Link: `/en/ams`

### H2: Ongoing Maintenance Schedule
- Fluid level inspection: [VERIFY: interval]
- Fluid quality check: [VERIFY: interval and test method — conductivity test for mineral oil contamination]
- Heat exchanger inspection and cleaning: [VERIFY: interval]
- ASIC inspection (removal from fluid for maintenance): [VERIFY: how to safely remove and dry an ASIC from immersion for servicing]
- Fluid replacement: [VERIFY: lifespan of fluid — typically 3–5+ years for engineered fluids, shorter for mineral oil depending on contamination]

### H2: Frequently Asked Questions

---

## FAQ

1. Do I need to remove fans before placing an ASIC in an immersion cooling tank?
2. Can I install custom firmware before or after submersion?
3. How long does it take to set up an immersion cooling system from scratch?
4. What temperature should my immersion cooling fluid operate at?
5. How do I monitor ASIC performance inside an immersion tank?
6. What maintenance does an immersion cooling system require?
7. Can I mix different ASIC models in the same immersion tank?

---

## E-E-A-T Signals

- Numbered step-by-step structure signals operational expertise
- Specific temps, intervals, and specs throughout (all VERIFY tagged)
- Link to BiXBiT firmware install guides — practical cross-reference
- Author: field engineer who has commissioned BiXBiT immersion systems [VERIFY]
- Photography/video placeholder: commissioning photos or video walkthrough [VERIFY: BiXBiT media assets available?]

---

## Internal Links

### Outbound
| Target | Anchor Text | Placement |
|---|---|---|
| `/en/immersion-cooling-mining` | "BiXBiT immersion cooling system overview" | Intro |
| `/en/immersion-cooling-mining/dielectric-fluid` | "dielectric fluid selection guide" | Step 2 — fluid fill |
| `/en/immersion-cooling-mining/single-phase` | "single-phase immersion cooling" | Intro context note |
| `/en/antminer-firmware/install` | "BiXBiT Antminer firmware installation guide" | Step 4 |
| `/en/whatsminer-firmware/install` | "BiXBiT Whatsminer firmware installation guide" | Step 4 |
| `/en/antminer-firmware/autotuning` | "per-chip autotuning setup" | Step 4 |
| `/en/whatsminer-firmware/autotuning` | "Whatsminer autotuning configuration" | Step 4 |
| `/en/ams` | "AMS fleet monitoring" | Step 5 |

### Inbound
| Source | Anchor Text |
|---|---|
| `/en/immersion-cooling-mining` (pillar) | "ASIC immersion cooling setup guide" |
| `/en/immersion-cooling-mining/antminer` | "step-by-step Antminer immersion setup" |
| `/en/immersion-cooling-mining/whatsminer` | "step-by-step Whatsminer immersion setup" |
| `/en/antminer-firmware/install` | "installing firmware on immersion-deployed Antminers" |
| `/en/whatsminer-firmware/install` | "installing firmware on immersion-deployed Whatsminers" |

---

## Schema

`HowTo` (primary — Google rich result eligible) + `FAQPage`

HowTo steps map directly to H2 steps 1–5.

```json
{
  "@type": "HowTo",
  "name": "How to Set Up ASIC Immersion Cooling",
  "step": [
    {"@type": "HowToStep", "name": "Site Requirements Check", "url": "...#site-requirements"},
    {"@type": "HowToStep", "name": "Hardware Preparation", "url": "...#hardware-prep"},
    {"@type": "HowToStep", "name": "Tank Installation and Fluid Fill", "url": "...#fluid-fill"},
    {"@type": "HowToStep", "name": "ASIC Submersion and First Power-On", "url": "...#power-on"},
    {"@type": "HowToStep", "name": "Firmware Configuration for Immersion", "url": "...#firmware"},
    {"@type": "HowToStep", "name": "AMS Monitoring Setup", "url": "...#monitoring"}
  ]
}
```

---

## Word Count Target
2,200–2,800 words (procedural depth justifies higher word count)

---

## [VERIFY] Blockers

- [ ] Floor load spec (kg/m²) for BiXBiT immersion tank
- [ ] Electrical supply requirements (voltage, amperage per tank)
- [ ] Secondary cooling loop sizing guidance
- [ ] Fan removal procedure specifics per ASIC model (S19/S21/M50/M60)
- [ ] BiXBiT-specific fill procedure and fluid specs
- [ ] Power-on sequence and commissioning temperature targets
- [ ] BiXBiT firmware: does it have an explicit immersion mode or profile?
- [ ] AMS alert thresholds recommended for immersion deployments
- [ ] Maintenance schedule (fluid check, heat exchanger cleaning intervals)
- [ ] Stock firmware behavior without fans — does it fault? (Antminer and Whatsminer both)
