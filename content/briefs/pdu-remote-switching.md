# Brief: Remote Per-Outlet Switching for Mining PDUs

URL: /en/pdu/remote-switching
Intent: technical informational
Primary keyword: PDU remote switching ASIC
Secondary keywords: remote outlet control mining PDU, PDU remote reboot ASIC, per-outlet switching mining farm, remote power cycle ASIC miner
Search volume: [NO DATA — DataForSEO 401]
Priority: P0
Schema: `TechArticle` + `HowTo`

---

## H1

Remote Per-Outlet Switching: Reboot Any ASIC in Your Mining Farm Without Physical Access

---

## Meta description (≤160 chars)

BiXBiT managed PDUs let you power-cycle any ASIC outlet remotely in seconds via web UI or AMS. Cut downtime from stuck miners — no technician dispatch required.

---

## Content structure

### H2: The Stuck Miner Problem at Scale
Frame the operational reality: in a farm of 500+ ASICs, at any given time some percentage
of miners will hang — API becomes unresponsive, hashrate drops to zero but the miner
appears "on." The only recovery is a power cycle.

Without remote switching:
- Dispatch a technician to physically pull and re-plug the power cable
- At a remote site (Kazakhstan, Paraguay), this means hours of downtime per incident
- At a 5,000-ASIC farm, if even 0.5% of machines need a reboot per day, that is 25 manual
  reboot events — significant labor cost and lost hashrate

With per-outlet remote switching:
- Operator identifies the stuck miner in AMS (hashrate = 0, temperature nominal)
- Clicks "reboot outlet" in AMS or the PDU web interface
- Power cycle completes in [VERIFY: typical relay open/close cycle time — e.g., 5–10 seconds]
- Miner resumes hashing — total downtime under 3 minutes, no staff required on-site

### H2: How Per-Outlet Switching Works in BiXBiT PDUs

#### H3: Outlet Relay Mechanism
[VERIFY: how BiXBiT PDU switches outlets — relay, solid-state switch, or other mechanism.
Describe switching behavior: open → off → delay → close → on. Confirm whether switching
is "break before make" for safety.]

#### H3: Management Interfaces
BiXBiT PDU can be controlled via:
- **Web UI**: direct browser access to the PDU management interface
- **AMS integration**: outlet switching commands issued directly from AMS dashboard
  without logging into the PDU separately
- **API**: [VERIFY: REST API, SNMP set, or other interface for scripted/automated switching]

#### H3: Switching Commands
Three modes available: [VERIFY all three exist on BiXBiT PDU]
- **Off** — cut power to outlet (miner loses power)
- **On** — restore power to outlet
- **Reboot** (power cycle) — off for [VERIFY: configurable delay, typically 5–30 seconds] then on.
  Most common command for stuck miner recovery.

#### H3: Group Switching (Rack-Level)
[VERIFY: whether BiXBiT PDU supports switching multiple outlets simultaneously (group/bank switching)
for scenarios like: "reboot all outlets in rack 3" during a planned maintenance window]

### H2: Remote Switching in the AMS Workflow

Operator workflow step-by-step:
1. AMS detects miner with hashrate = 0 (alert fires: "Miner offline — 0 TH/s, powered on")
2. Operator opens the miner's detail view in AMS
3. Clicks "Reboot outlet" — AMS sends the switching command to the PDU
4. PDU cuts power to that outlet for the configured cycle delay
5. PDU restores power — miner boots
6. AMS detects miner reconnecting — clears the alert when TH/s returns to expected range

This entire flow happens from one dashboard — no PDU login, no VPN to the PDU separately,
no physical intervention.

Link to: `/en/pdu/ams-integration` and `/en/ams/mining-farm-alerts-automation`

### H2: Remote Switching for Planned Maintenance

Beyond emergency reboots, per-outlet switching supports planned operations:
- **Firmware update**: power-cycle ASICs post-flash to apply firmware via AMS in batches
- **Sequential load management**: stagger startup of large ASIC batches to avoid
  inrush current spikes on the distribution panel
- **Scheduled overnight maintenance windows**: power-cycle a rack's outlets in sequence
  without manual labor during off-peak hours

Link to: `/en/antminer-firmware/update` and `/en/whatsminer-firmware/update`

### H2: Safety Considerations for Remote Switching

#### H3: Switching High-Current Loads
ASIC PSUs are high-current loads. [VERIFY: whether BiXBiT PDU outlet relays are rated for
inductive load switching, not just resistive. Confirm relay current rating at rated voltage.]

#### H3: Access Control
[VERIFY: what authentication and authorization controls exist — user roles (admin vs. read-only),
whether switching commands require confirmation, audit log of who switched what outlet and when]

#### H3: Inrush Current Management
When an ASIC PSU powers on, it draws a brief inrush current spike (typically 2–5× rated
continuous current for <100ms). [VERIFY: whether BiXBiT PDU has sequenced startup delay between
outlets to prevent multiple simultaneous inrush events from tripping upstream breakers.
This is often called "sequential power-up" or "staggered startup."]

### H2: HowTo: Reboot a Stuck ASIC via BiXBiT PDU (Remote)

Step 1: Identify the stuck miner in AMS (hashrate 0, device shows as powered)
Step 2: Note the miner's PDU outlet assignment (visible in AMS device details)
Step 3: From AMS device panel, select "Reboot outlet" action
Step 4: Confirm the power cycle command
Step 5: Wait for the reboot cycle to complete ([VERIFY: typical duration])
Step 6: Verify the miner reconnects and hashrate returns to normal in AMS

Alternative: access the PDU's web UI directly → navigate to Outlets → select the outlet →
select "Cycle" or "Reboot" → confirm.

### H2: Frequently Asked Questions

---

## Target entities / terms

Per-outlet switching, remote outlet control, power cycle, ASIC reboot, relay, PDU, managed PDU,
BiXBiT PDU, AMS, fleet monitoring, stuck miner, hashrate, TH/s, downtime, remote site,
web UI, API, SNMP, inrush current, sequential startup, outlet bank, group switching,
maintenance window, firmware update, mining farm, remote management, power cycle delay

---

## FAQ block

Q: Can I reboot individual ASICs remotely without using managed PDUs?
A: You can attempt a soft reboot via the ASIC's API (if it is responsive) or via AMS.
However, if the miner's firmware is hung and the API is unresponsive, a software reboot
command will not work. Hard power-cycling the outlet via a managed PDU is the reliable
recovery method in this case — it works regardless of the miner's software state.

Q: How long does an outlet reboot cycle take?
A: [VERIFY: BiXBiT PDU power cycle duration — typically 5–30 seconds depending on
configurable delay. Add the ASIC boot time — typically 60–90 seconds to begin hashing.
Total time from "reboot command" to "hashing again" is typically under 3 minutes.]

Q: Can AMS trigger automatic reboots when a miner goes offline?
A: [VERIFY: whether AMS supports automated (rule-based) outlet switching — e.g., "if hashrate
= 0 for 10 minutes, automatically trigger outlet reboot." If supported, describe the
automation configuration. If manual only, state that clearly.]

Q: What happens to the ASIC's settings after a hard power cycle?
A: For ASICs running BiXBiT firmware, configuration (frequency profile, pool settings,
fan curve, etc.) is stored in flash memory and persists through power cycles. The miner
reboots and resumes operation with the same configuration.
[VERIFY: confirm this is accurate for BiXBiT firmware on both Antminer and Whatsminer]

Q: Is remote switching secure? Can unauthorized users reboot my miners?
A: [VERIFY: BiXBiT PDU access control model — user authentication, role-based permissions,
audit log. AMS-initiated switching inherits AMS user permissions.]

---

## E-E-A-T signals

- Author: data center operations engineer or mining infrastructure specialist
- Include: a real or realistic scenario — e.g., "a 2,000-ASIC farm in Kazakhstan with 4 staff
  on-site, averaging 8 manual reboots per day before deploying managed PDUs" — [VERIFY: whether
  BiXBiT can provide a real customer case study with permission]
- Include: diagram of the switching signal path: AMS → PDU management IP → outlet relay → ASIC PSU
- Reference: ANSI/TIA-942 or ASHRAE data center management best practices if applicable — [VERIFY]

---

## Internal links

Inbound:
- `/en/pdu` pillar → here ("per-outlet remote switching")
- `/en/pdu/ams-integration` → here ("outlet switching commands from AMS")
- `/en/ams/mining-farm-alerts-automation` → here ("trigger outlet reboot from an AMS alert")
- `/en/antminer-firmware/update` → here ("power cycle after firmware update via PDU")

Outbound:
- → `/en/pdu` ("BiXBiT managed PDU overview")
- → `/en/pdu/ams-integration` ("AMS integration — full guide")
- → `/en/pdu/overload-protection` ("outlet switching for fault isolation")
- → `/en/ams/mining-farm-alerts-automation` ("configure alerts that trigger outlet switching")
- → `/en/antminer-firmware/update` ("firmware update workflow including power cycles")
- → `/en/whatsminer-firmware/update` ("Whatsminer firmware update workflow")

---

## Schema type

Primary: `TechArticle`
Secondary: `HowTo` — mark up the "How to Reboot a Stuck ASIC" section steps

```json
{
  "@type": "HowTo",
  "name": "Reboot a Stuck ASIC via BiXBiT PDU Remote Switching",
  "step": [
    { "@type": "HowToStep", "text": "Identify the stuck miner in AMS..." },
    { "@type": "HowToStep", "text": "Note the miner's PDU outlet assignment..." },
    ...
  ]
}
```

Supplement with `FAQPage` schema.

---

## VERIFY items

- [VERIFY: outlet switching mechanism — relay type, current rating, voltage rating]
- [VERIFY: power cycle delay duration — default and configurable range]
- [VERIFY: whether inrush current / sequential startup is supported]
- [VERIFY: management interfaces available — web UI, REST API, SNMP, AMS native]
- [VERIFY: group/bank switching capability]
- [VERIFY: access control model — user roles, audit log, confirmation requirement]
- [VERIFY: whether AMS supports automated rule-based outlet switching]
- [VERIFY: ASIC boot time after power cycle for Antminer and Whatsminer models]
- [VERIFY: whether customer case study with downtime reduction data is available for publication]
