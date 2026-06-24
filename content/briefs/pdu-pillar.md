# Brief: Managed PDU for ASIC Mining Farms — Pillar Page

URL: /en/pdu
Intent: commercial + informational (hybrid)
Primary keyword: PDU for mining
Secondary keywords: managed PDU mining farm, smart PDU ASIC, power distribution unit bitcoin mining, ASIC PDU, mining farm power distribution
Search volume: [NO DATA — DataForSEO 401]
Priority: P0
Schema: `Product` + `FAQPage`

---

## H1

Managed PDU for ASIC Mining Farms: Per-Outlet Control, Remote Switching, and AMS Integration

---

## Meta description (≤160 chars)

BiXBiT managed PDUs for Bitcoin mining: per-outlet switching, real-time energy metering, and direct AMS integration. Built for ASIC farm operators at any scale.

---

## Content structure

### H2: What a Mining PDU Does That a Standard PDU Cannot
Frame the core problem: standard rack PDUs distribute power passively — no per-outlet metering,
no remote reboot, no overload isolation per outlet. For an ASIC farm where a single stuck miner
can trip a circuit, this is operationally unacceptable at scale.

Key tезисы:
- Standard PDU: power strip with a breaker. No visibility, no control.
- Managed PDU: per-outlet switching, per-outlet watt/amp/kWh metering, remote access.
- BiXBiT PDU adds: API/AMS integration so telemetry flows into fleet dashboard automatically.

### H2: BiXBiT Managed PDU — Core Specifications
[VERIFY: all specific technical specifications from product team before publishing]

Placeholder structure:
- Form factor: [VERIFY: 1U/2U rack-mount, inlet connector type, outlet count, outlet type]
- Input: [VERIFY: single-phase / three-phase, voltage range, max amperage]
- Outlets: [VERIFY: number of controlled outlets, outlet format, per-outlet current rating]
- Metering: per-outlet real-time: watts, amps, kWh, power factor — [VERIFY]
- Switching: per-outlet remote on/off/reboot — [VERIFY: via web UI / API / AMS]
- Overload protection: per-outlet or per-group circuit breaker — [VERIFY]
- Connectivity: [VERIFY: Ethernet, IP-based management, SNMP/API support]
- Environmental: [VERIFY: operating temperature range, IP rating for immersion-adjacent deployments]
- Certifications: [VERIFY: UL, CE, RoHS, other relevant marks]

#### H3: Per-Outlet Energy Metering
Explain why watt-level visibility per ASIC matters: identify underperforming units pulling
full power but hashing below rated TH/s. Power efficiency = J/TH. If you can see watts per
outlet, you can calculate J/TH per device without touching the miner.

Link to: `/en/pdu/per-outlet-metering`

#### H3: Remote Per-Outlet Switching
Hard reboot a single stuck miner in 3 seconds from a browser or API call — no physical access
required. Critical for remote sites (Kazahstan, Paraguay, UAE deployments). 

Link to: `/en/pdu/remote-switching`

#### H3: Overload Protection
Per-outlet or per-group circuit isolation prevents a single ASIC failure event from cascading
to an entire rack. Explain difference between PDU-level protection and upstream breaker panels.

Link to: `/en/pdu/overload-protection`

### H2: AMS Integration — PDU Telemetry in Your Fleet Dashboard
BiXBiT PDU feeds per-outlet power data directly into AMS. Operators see power consumption
per device alongside hashrate, temperature, and fan speed in a single dashboard view.

Use cases:
- Automated alert when a device's power draw drops (hardware fault) or spikes (overclock anomaly)
- Per-client billing for hosting operators (kWh per outlet per billing period)
- PUE calculation inputs for colocation reporting

CTA: link to `/en/pdu/ams-integration` for full integration guide.
Cross-link: `/en/ams` and `/en/ams/mining-farm-power-monitoring`

### H2: Who Uses BiXBiT PDUs

#### H3: Large-Scale Farm Operators (100–100,000+ ASICs)
At this scale, even 1% downtime on power management = thousands of lost TH/s-hours.
Per-outlet remote reboot alone justifies managed PDU vs. unmanaged.

#### H3: Mining Hosting Providers
Per-outlet kWh metering enables accurate client billing. Know exactly what each client's
rack draws, generate billing reports, dispute-proof metering.

#### H3: Institutional Mining Operations
Compliance, auditing, and PUE reporting requirements. PDU metering data feeds into
energy efficiency reports for institutional LPs.

#### H3: Data Center Operators Running ASIC Workloads
High-density ASIC deployments (high kW/rack) require managed PDUs rated for the load.
Link to `/en/pdu/data-center-mining`.

### H2: Managed PDU vs. Direct Wiring vs. Unmanaged PDU
Three-way comparison in a table. Decision framework:
- Direct wiring: lowest cost, zero control, acceptable only for smallest installations
- Unmanaged PDU: adds metering, no per-outlet switching or remote access
- BiXBiT managed PDU: full per-outlet control, AMS integration, remote management

Link to: `/en/pdu/vs-direct-wiring` and `/en/pdu/vs-unmanaged-pdu`

### H2: PDU Sizing for ASIC Farms
Brief overview — link to detailed guide.
Rule of thumb framing (with [VERIFY] on any specific numbers):
- Calculate total load: ASIC rated wattage × unit count × [VERIFY: derating factor, typically 0.8]
- Choose PDU amperage and outlet count accordingly
- [VERIFY: NEC 80% rule on continuous loads reference]

Link to: `/en/pdu/sizing-asic-farm`

### H2: Immersion Cooling Deployments
Specific PDU considerations for immersion setups: fluid-resistant environments, IP-rated
enclosures, potential for higher power density per tank.

Link to: `/en/immersion-cooling-mining`

### H2: Frequently Asked Questions
(See FAQ block below)

### H2: Get Started
CTA block. Contact / demo request / datasheet download.

---

## Target entities / terms

Power distribution unit (PDU), managed PDU, smart PDU, per-outlet switching, per-outlet metering,
remote outlet control, ASIC miner, Bitcoin mining, Antminer, Whatsminer, AMS (Asset Management
System), kWh metering, power factor, J/TH, PUE (Power Usage Effectiveness), circuit breaker,
rack PDU, 1U rack, Ethernet management, SNMP, API, remote reboot, fleet monitoring, mining farm,
mining hosting, colocation, three-phase power, single-phase power, IEC connector, NEMA connector

---

## FAQ block

Q: What is a managed PDU and why does a mining farm need one?
A: A managed PDU (Power Distribution Unit) provides per-outlet remote switching and real-time
energy metering — unlike a standard PDU which is a passive power strip. In a mining farm,
managed PDUs allow operators to remotely reboot stuck ASICs, monitor per-device power
consumption in real time, isolate faults without physical access, and feed power data into
fleet monitoring software.

Q: Can BiXBiT PDUs integrate with third-party monitoring systems?
A: [VERIFY: API/SNMP support details. If BiXBiT PDU exposes an API or SNMP interface,
confirm here. Focus on confirmed AMS integration as the primary answer.]

Q: How many ASICs can one BiXBiT PDU support?
A: [VERIFY: outlet count per PDU model, typical ASIC wattage range, and resulting ASIC-per-PDU
count. Example: if PDU has 24 × 20A outlets and an Antminer S19 draws ~3,500W at 240V ~15A,
you could fit approximately N units per PDU — but exact numbers must come from product team.]

Q: What is the difference between managed and unmanaged PDUs for mining?
A: Unmanaged PDUs distribute power with basic metering but no per-outlet switching.
Managed PDUs add remote on/off/reboot per outlet, per-outlet kWh tracking, and API/software
integration. For farms with remote sites or hosting revenue models, managed PDUs are
operationally essential.

Q: Do BiXBiT PDUs work with immersion cooling setups?
A: [VERIFY: whether BiXBiT PDUs have IP rating suitable for immersion-adjacent environments,
and whether any specific model is rated for high-humidity or fluid-vapor environments.]

Q: How does PDU metering help reduce electricity costs?
A: Per-outlet watt metering lets operators identify ASICs pulling full power but hashing below
rated efficiency — early sign of hardware degradation. Combining PDU power data with AMS
hashrate telemetry gives a per-device J/TH figure, enabling targeted firmware tuning
(undervolting) or hardware replacement decisions.

---

## E-E-A-T signals

- Authored by: electrical engineer or infrastructure architect with ASIC deployment experience
- Include: real deployment scenario with PDU count calculation (1 MW farm example) — [VERIFY with product team]
- Include: photo/diagram of BiXBiT PDU in rack installation — [request from product team]
- Include: link to product datasheet PDF (PDF gets indexed; builds trust)
- Reference: NEC continuous load derating rules where applicable — [VERIFY: NEC article numbers]
- Avoid: marketing superlatives. Use specific feature names and measurable outcomes.

---

## Internal links

Inbound (from other pages to this pillar):
- Homepage → `/en/pdu` (product ecosystem nav + product card)
- `/en/ams` → `/en/pdu` ("PDU power distribution, integrated with AMS")
- `/en/antminer-firmware` → `/en/pdu` ("PDU power management for Antminer farms")
- `/en/whatsminer-firmware` → `/en/pdu` ("PDU power management for Whatsminer farms")
- `/en/immersion-cooling-mining` → `/en/pdu` ("managed PDU for immersion cooling deployments")

Outbound (from this pillar to spokes and cross-cluster):
- → `/en/pdu/per-outlet-metering` ("per-outlet energy metering")
- → `/en/pdu/remote-switching` ("per-outlet remote switching")
- → `/en/pdu/overload-protection` ("PDU overload protection")
- → `/en/pdu/ams-integration` ("AMS integration guide")
- → `/en/pdu/sizing-asic-farm` ("PDU sizing guide for ASIC farms")
- → `/en/pdu/vs-direct-wiring` ("PDU vs direct wiring comparison")
- → `/en/pdu/vs-unmanaged-pdu` ("managed vs unmanaged PDU")
- → `/en/pdu/data-center-mining` ("PDU for data center mining")
- → `/en/ams` ("AMS fleet monitoring dashboard")
- → `/en/ams/mining-farm-power-monitoring` ("per-unit power monitoring in AMS")
- → `/en/antminer-firmware` ("BiXBiT Antminer firmware")
- → `/en/whatsminer-firmware` ("BiXBiT Whatsminer firmware")
- → `/en/immersion-cooling-mining` ("immersion cooling deployments")

---

## Schema type

Primary: `Product`
```json
{
  "@type": "Product",
  "name": "BiXBiT Managed PDU for ASIC Mining",
  "description": "Managed power distribution unit with per-outlet switching, real-time energy metering, and AMS integration for ASIC mining farms.",
  "brand": { "@type": "Brand", "name": "BiXBiT" },
  "url": "https://bixbit.io/en/pdu"
}
```

Secondary: `FAQPage` — mark up all FAQ Q&A pairs with `@type: Question` / `acceptedAnswer`.

---

## VERIFY items

- [VERIFY: PDU form factor — 1U or 2U rack-mount]
- [VERIFY: inlet connector type and ratings (IEC 309, NEMA L6-30, etc.)]
- [VERIFY: outlet count per PDU model]
- [VERIFY: outlet type and per-outlet current rating]
- [VERIFY: max total amperage per PDU]
- [VERIFY: single-phase vs. three-phase models available]
- [VERIFY: per-outlet switching mechanism — relay, MOSFET, other]
- [VERIFY: management interface — web UI, API (REST?), SNMP?]
- [VERIFY: AMS integration protocol — is it native push, polling, or SNMP trap?]
- [VERIFY: operating temperature range]
- [VERIFY: IP rating, if any]
- [VERIFY: certifications — UL listed? CE marked? RoHS?]
- [VERIFY: NEC 80% continuous load rule reference — NEC 210.19(A)(1) or 210.20(A)]
- [VERIFY: PDU pricing / availability / lead times to include on product page or leave for sales contact]
