# Brief: Per-Outlet Energy Metering for ASIC Mining PDUs

URL: /en/pdu/per-outlet-metering
Intent: technical informational
Primary keyword: PDU per-outlet metering mining
Secondary keywords: per-outlet energy metering ASIC, PDU power monitoring mining, ASIC power consumption per device, PDU watt meter mining farm
Search volume: [NO DATA — DataForSEO 401]
Priority: P1
Schema: `TechArticle` + `FAQPage`

---

## H1

Per-Outlet Energy Metering in Mining PDUs: Track Power Consumption Per ASIC in Real Time

---

## Meta description (≤160 chars)

BiXBiT managed PDUs measure watts, amps, and kWh at each individual outlet. Identify underperforming ASICs by power draw — without touching the hardware.

---

## Content structure

### H2: Why Per-Outlet Metering Matters in an ASIC Farm
The central insight: an ASIC that draws full rated wattage but delivers below-rated TH/s is
consuming electricity without producing proportionate hash. Without per-outlet metering, this
miner looks "operational" — it is powered on and responding — but it is silently inefficient.

Per-outlet metering enables:
1. **Device-level J/TH calculation** — watts (from PDU) ÷ TH/s (from AMS firmware telemetry)
   = J/TH per device. The industry efficiency benchmark, calculated automatically.
2. **Early fault detection** — abnormal power draw (spike or drop) often precedes a complete
   ASIC failure by hours. Detect before hashrate drops.
3. **Firmware tuning verification** — after undervolting or autotuning an ASIC, confirm actual
   wall-power reduction at the PDU level, not just relying on firmware-reported estimates.
4. **Hosting operator billing** — per-outlet kWh is the basis for electricity billing per client
   in a co-location or hosting model.

### H2: What Per-Outlet Metering Measures

#### H3: Watts (Real Power)
The actual power consumed by the ASIC at that outlet. This is what appears on the electricity
bill (after summing across all outlets). Reported in real time.

#### H3: Amps (Current)
Current draw per outlet. Useful for verifying the outlet stays within its current rating and
for identifying power factor issues.

#### H3: Volts (Voltage)
Per-outlet voltage monitoring detects supply voltage drops (voltage sag) under load —
important in high-density racks where long cable runs can cause volt-drop.

#### H3: Power Factor (PF)
ASIC power supplies typically have PF > 0.9. A low PF reading indicates a degraded or failing
PSU. [VERIFY: typical ASIC PSU power factor range]

#### H3: kWh (Energy Consumption)
Cumulative energy over time. The basis for electricity cost calculation and client billing.
BiXBiT PDU logs kWh per outlet — integrated into AMS for reporting.

### H2: Per-Outlet Metering vs. Total-Inlet Metering
Most basic "metered" PDUs only show total inlet power. Illustrate the difference:

| Feature | Total-inlet metered PDU | BiXBiT per-outlet metered PDU |
|---|---|---|
| Total farm power draw | Yes | Yes |
| Per-rack power draw | Yes (one reading) | Yes |
| Per-device power draw | No | Yes |
| Device J/TH calculation | Requires manual work | Automated via AMS |
| Fault isolation by power | No — circuit trip affects the whole PDU | Per-outlet level |
| Hosting billing granularity | Per-rack at best | Per-device (per-outlet) |

### H2: How AMS Uses Per-Outlet Metering Data
BiXBiT AMS pulls metering data from the PDU and correlates it with firmware telemetry
(TH/s per miner, temperature, fan speed). The result:

- Per-device efficiency score visible in the fleet dashboard
- Automated alerts when any device's watts spike beyond a threshold
- Historical power curves — track a device's efficiency degradation over weeks

Walk through the data flow: PDU → AMS → dashboard widget → alert trigger → operator action.

Link to: `/en/pdu/ams-integration` and `/en/ams/mining-farm-power-monitoring`

### H2: Using Metering Data to Verify Firmware Undervolting Results
Practical workflow:
1. Apply undervolting profile to a batch of ASICs via BiXBiT firmware / AMS
2. Monitor per-outlet watt readings on the PDU immediately after
3. Compare pre/post watts: expected reduction of [VERIFY: typical undervolt watt reduction %
   for S19 or M50 at a given frequency step]
4. Verify hashrate holds (via AMS TH/s telemetry)
5. Calculate new J/TH — confirm efficiency improvement at the wall

This closes the feedback loop between firmware tuning and actual power savings.
Link to: `/en/antminer-firmware/undervolting` and `/en/whatsminer-firmware/undervolting`

### H2: Technical Considerations for High-Density Mining Racks

#### H3: Measurement Accuracy
[VERIFY: BiXBiT PDU metering accuracy specification — e.g., ±1% or ±2% of reading.
This matters for billing applications where clients may dispute kWh figures.]

#### H3: Sampling Rate and Logging Interval
[VERIFY: how frequently the PDU samples per-outlet data, and what resolution AMS records
history at — e.g., 1-second samples, 1-minute averages stored in AMS]

#### H3: Connector and Cable Considerations
[VERIFY: outlet type on BiXBiT PDU — C13, C19, NEMA 5-20R, other — and matching PSU
connector on common ASICs (Antminer S19/S21 use C13/C19 depending on model)]

### H2: Frequently Asked Questions

---

## Target entities / terms

Per-outlet metering, energy metering, watts, amps, volts, power factor, kWh, real power,
apparent power, reactive power, PDU, managed PDU, ASIC, Antminer, Whatsminer, AMS,
J/TH, efficiency, undervolting, overclocking, firmware telemetry, fleet monitoring,
device-level analytics, hosting billing, colocation, PSU (power supply unit), C13 connector,
C19 connector, NEMA connector, voltage sag, circuit breaker, data logging, alert threshold

---

## FAQ block

Q: What is per-outlet metering on a PDU?
A: Per-outlet metering means the PDU measures and reports power consumption (watts, amps,
kWh, power factor) at each individual outlet receptacle, not just at the PDU's total inlet.
In a mining farm, this enables you to see exactly how much power each ASIC miner is drawing
at any moment.

Q: How does per-outlet metering help calculate ASIC efficiency (J/TH)?
A: J/TH = joules consumed per terahash produced. Joules = watts × seconds. If your PDU
reports that a specific outlet draws 3,400W and AMS reports that miner produces 105 TH/s,
the J/TH = 3,400 ÷ 105 ≈ 32.4 J/TH. Without per-outlet metering, this calculation requires
a handheld power meter at each device — impractical at scale.

Q: Can per-outlet metering detect failing ASICs before they stop working?
A: Often, yes. A degrading ASIC PSU or hashboard often shows an abnormal power draw
pattern before the device stops hashing entirely. A managed PDU with AMS integration can
alert when any outlet deviates from its baseline by a set threshold (e.g., ±10%), giving
operators early warning time to schedule maintenance.

Q: Is per-outlet kWh accurate enough for client billing?
A: [VERIFY: BiXBiT PDU measurement accuracy specification. For billing use cases, ±1%
accuracy is generally considered acceptable — confirm with product team whether the PDU
is suitable for revenue-grade metering or informational use only.]

Q: How does per-outlet metering differ from what ASIC firmware reports internally?
A: Firmware-reported power is an estimate based on the ASIC's internal power measurement
circuits, which may not account for PSU conversion losses or cable losses. PDU outlet metering
measures actual wall power delivered to the PSU — the true electrical load. For accurate
J/TH and billing purposes, PDU metering is more reliable than firmware estimates.

---

## E-E-A-T signals

- Author: electrical engineer or mining infrastructure specialist
- Include: diagram showing watts/amps/kWh reading flow from PDU outlet → AMS dashboard
- Include: worked example calculation — specific ASIC (model TBD with [VERIFY]), known TH/s,
  measured watts from PDU, resulting J/TH
- Reference: IEC 62053-21 or ANSI C12.20 for energy meter accuracy classes — [VERIFY: which
  standard BiXBiT PDU metering complies with]

---

## Internal links

Inbound:
- `/en/pdu` pillar → here ("per-outlet energy metering")
- `/en/pdu/what-is-pdu-mining` → here ("how per-outlet metering works in detail")
- `/en/ams/mining-farm-power-monitoring` → here ("PDU metering as the data source")
- `/en/antminer-firmware/undervolting` → here ("verify undervolting savings at the wall")
- `/en/whatsminer-firmware/undervolting` → here ("verify Whatsminer undervolting at the wall")

Outbound:
- → `/en/pdu` ("BiXBiT managed PDU overview")
- → `/en/pdu/ams-integration` ("how PDU metering integrates with AMS")
- → `/en/pdu/vs-unmanaged-pdu` ("why per-outlet metering beats total-inlet metering")
- → `/en/ams/mining-farm-power-monitoring` ("per-device power monitoring in AMS")
- → `/en/antminer-firmware/undervolting` ("reduce the watts your PDU will meter")
- → `/en/whatsminer-firmware/undervolting` ("Whatsminer undervolting: power savings")

---

## Schema type

```json
{
  "@type": "TechArticle",
  "headline": "Per-Outlet Energy Metering in Mining PDUs",
  "description": "Technical guide to per-outlet power metering in managed PDUs for ASIC mining farms — what it measures and how it integrates with fleet monitoring.",
  "author": { "@type": "Person", "name": "[VERIFY]" },
  "publisher": { "@type": "Organization", "name": "BiXBiT" }
}
```

Supplement with `FAQPage` schema.

---

## VERIFY items

- [VERIFY: BiXBiT PDU metering accuracy — ±X% of reading for watts/kWh]
- [VERIFY: metering parameters reported per outlet — confirm watts, amps, volts, PF, kWh all available]
- [VERIFY: data logging resolution and history depth in AMS]
- [VERIFY: applicable metering accuracy standard (IEC 62053, ANSI C12)]
- [VERIFY: typical ASIC PSU power factor range — e.g., >0.95 for modern Antminer/Whatsminer PSUs]
- [VERIFY: outlet connector type(s) on BiXBiT PDU]
- [VERIFY: example undervolting power reduction figures — get from firmware team, do not invent]
