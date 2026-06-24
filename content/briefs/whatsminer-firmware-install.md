# Content Brief: Whatsminer Firmware Installation Guide
**URL:** /en/whatsminer-firmware/install
**File:** content/briefs/whatsminer-firmware-install.md
**Last updated:** 2026-06-19
**Priority:** P1
**Assignee:** [Firmware engineer with hands-on Whatsminer installation experience]

---

## Page Goal

Provide the definitive step-by-step installation guide for BiXBiT firmware on Whatsminer hardware — covering all supported methods. This is a bottom-of-funnel page: the visitor has already decided to install BiXBiT firmware and needs accurate, complete instructions. Accuracy here is non-negotiable. MicroBT's own documentation is minimal and version-fragmented; no competitor has a comprehensive guide. This page can capture significant organic traffic and serve as a technical credibility signal.

---

## Search Intent

**Primary intent:** Informational / how-to — operator has made the decision and needs installation instructions.
**Secondary intent:** Commercial — operator evaluating ease of installation before committing.
**SERP type:** MicroBT support docs, mining forums, YouTube. No third-party firmware provider owns this SERP.

---

## Target Keywords

| Keyword | Role | Vol [NO DATA] | KD [NO DATA] |
|---|---|---|---|
| whatsminer firmware install | Primary | — | — |
| how to install whatsminer firmware | How-to | — | — |
| whatsminer firmware flash guide | Technical | — | — |
| whatsminer firmware sd card | Technical | — | — |
| whatsminer firmware recovery | Trust / troubleshooting | — | — |
| install custom firmware whatsminer | Commercial | — | — |
| whatsminer m30s firmware installation | Model-specific | — | — |

---

## Proposed URL

`https://bixbit.io/en/whatsminer-firmware/install`

---

## Meta

**Title tag (≤60 chars):** `How to Install Whatsminer Firmware — Complete Guide`
**Meta description (≤155 chars):** `Step-by-step guide to installing BiXBiT custom firmware on Whatsminer ASICs. Web UI, API, and fleet methods. Covers M30S, M50, and M60 series with troubleshooting.`

---

## H1

`How to Install Custom Firmware on Whatsminer: Complete Installation Guide`

---

## Page Structure

### H2: Before You Install — Checklist

All prerequisites must be satisfied before flashing:
1. Identify your Whatsminer model and hardware revision [VERIFY: how to confirm board revision — web UI, serial number, or sticker?]
2. Download the correct BiXBiT firmware package from [VERIFY: canonical download URL] — model and revision must match
3. Verify the SHA256 checksum of the downloaded file against BiXBiT's published reference [VERIFY: URL where checksums are published]
4. Confirm unit is on a stable power supply — do not flash on a circuit with known instability
5. Ensure the unit is accessible via web browser on your local network
6. Note your current pool configuration — [VERIFY: does the install process reset pool settings? Operator should record them manually to re-enter after install]
7. Accept that installing third-party firmware may affect MicroBT warranty [VERIFY: confirm warranty position]

### H2: Method 1 — Install via Whatsminer Web Interface (Recommended for Single Units)

Step-by-step:

**Step 1: Access the Whatsminer web interface**
Open a browser and navigate to the unit's IP address. Default login: [VERIFY: default Whatsminer web UI credentials — admin/admin or other? Do not publish incorrect credentials]

**Step 2: Navigate to the firmware update section**
[VERIFY: exact navigation path — e.g., System → Upgrade, or Configuration → Firmware, or similar. This must be accurate for the firmware version operators will encounter]

**Step 3: Upload the BiXBiT firmware package**
Select the downloaded .tar.gz firmware file and upload it. [VERIFY: confirm the expected file format/extension for BiXBiT Whatsminer firmware packages]

**Step 4: Verify the checksum (if displayed)**
[VERIFY: does the Whatsminer web UI display a checksum of the uploaded file before applying? If yes, describe where to find it and how to confirm]

**Step 5: Initiate the flash**
Click the flash/update button. [VERIFY: exact button label in Whatsminer web UI] Do not disconnect power, close the browser tab, or interrupt network connectivity during the flash.

**Step 6: Wait for reboot**
[VERIFY: expected duration of flash + reboot cycle for Whatsminer hardware — provide time in minutes]

**Step 7: Reconnect and verify**
After reboot, reconnect to the web UI. [VERIFY: where to find the firmware version string in BiXBiT's web interface — confirm it matches the expected BiXBiT version number]

**Step 8: Configure BiXBiT firmware settings**
- Re-enter pool configuration
- Select tuning mode (normal / efficiency / performance, or enable autotuning)
- Connect to AMS: → /en/ams

### H2: Method 2 — Install via Whatsminer API (Suitable for Multi-Unit Deployments)

For operators installing on multiple units:
[VERIFY: the exact Whatsminer API endpoint and parameters for pushing a firmware update. MicroBT's API structure is different from Bitmain's CGMiner-derived API — do not copy Antminer API commands]

Example API call:
```
[VERIFY: provide actual API command syntax — omit this code block entirely if the command cannot be verified before publication]
```

[VERIFY: Does the Whatsminer API support pointing units to a local firmware server (staged deployment)? This is a common enterprise requirement]

Notes:
- Authenticate with [VERIFY: API authentication method for Whatsminer]
- Deploy in batches — do not flash the entire fleet simultaneously [VERIFY: recommended batch size]
- Monitor progress: [VERIFY: how to confirm flash completion via API response or AMS]

### H2: Method 3 — Fleet Installation via AMS Dashboard

[VERIFY: confirm whether AMS supports fleet-wide Whatsminer firmware installation — if not confirmed, omit this section entirely rather than publish unverified capability]

If AMS supports fleet installation:
1. In AMS, select the target Whatsminer units
2. Navigate to: [VERIFY: AMS UI path for firmware management]
3. Upload or select the BiXBiT firmware package
4. Queue the deployment — AMS will manage the per-unit flash sequence
5. Monitor progress in the AMS fleet view

### H2: Post-Installation Configuration

After successful installation on any unit:

1. **Verify firmware version** in the web UI or AMS
2. **Configure pool settings** — re-enter your stratum pool address, worker name, and password
3. **Select tuning mode:**
   - Efficiency mode: lower power draw, slightly reduced or equal hashrate
   - Performance mode: higher hashrate, higher power draw
   - Autotuning: automated per-chip optimization (recommended default)
4. **Connect to AMS** — enter your AMS API credentials to enable remote monitoring [VERIFY: exact connection steps]
5. **Monitor for 24 hours** — confirm stable hashrate, expected power draw, and normal chip temperatures

### H2: Recovering from a Failed Installation

[VERIFY: this entire section requires hands-on Whatsminer recovery knowledge — do not publish without engineering review]

If a unit fails to boot after flashing:

#### H3: Recovery via Whatsminer Recovery Mode
[VERIFY: does Whatsminer hardware support a recovery mode? If yes: how to enter it (button combination, UART, or other); what firmware format is needed for recovery; can stock MicroBT firmware be restored through this method?]

#### H3: Recovery via UART / Serial Console
[VERIFY: is UART access available on Whatsminer hardware? Connector location and pinout — confirm before publishing]

#### H3: Contacting BiXBiT Support
If the above recovery steps fail: [VERIFY: support contact method — email, Telegram, ticket system?]

### H2: Frequently Asked Questions

**Q: Can I install BiXBiT firmware without voiding the MicroBT warranty?**
A: [VERIFY: warranty statement — see the custom firmware overview page]

**Q: What happens if I install firmware for the wrong hardware revision?**
A: [VERIFY: describe outcome — does the unit refuse to flash (safe failure), partially flash, or brick? This is safety-critical information]

**Q: Can I install BiXBiT firmware and then restore stock MicroBT firmware later?**
A: [VERIFY: rollback procedure — is it supported, and is it a clean restore?]

**Q: How long does installation take for a fleet of 500 units?**
A: [VERIFY: provide time estimate for batch API deployment vs AMS deployment for 500 units]

**Q: Which Whatsminer models and hardware revisions are supported?**
A: [VERIFY: link to compatibility table on the pillar page]

---

## Key Entities and Terms

- Firmware flash, firmware installation
- Whatsminer web interface, MicroBT API
- SHA256 checksum, firmware verification
- Hardware revision, board revision
- Recovery mode, UART, serial console
- Fleet deployment, batch update
- AMS integration
- Pool configuration, stratum

---

## E-E-A-T Signals

- Exact UI navigation paths and button labels (signals hands-on experience)
- Pre-installation checklist covering warranty, checksums, and revision confirmation
- Recovery section covering failure modes (signals completeness and operator trust)
- Hardware revision specificity (prevents bricking from wrong firmware)
- Author: firmware engineer with documented Whatsminer installation history

---

## Internal Links

### Links TO this page:
- /en/whatsminer-firmware (pillar) — "full Whatsminer firmware installation guide"
- /en/whatsminer-firmware/update — "complete installation guide for first-time setup"
- /en/whatsminer-firmware/whatsminer-m30s — "installation guide"
- /en/whatsminer-firmware/whatsminer-m50 — "firmware installation guide"

### Links FROM this page:
- /en/whatsminer-firmware — anchor: "BiXBiT Whatsminer firmware overview"
- /en/whatsminer-firmware/update — anchor: "updating existing BiXBiT installations"
- /en/whatsminer-firmware/autotuning — anchor: "configure autotuning after install"
- /en/whatsminer-firmware/security — anchor: "checksum verification and firmware security"
- /en/ams — anchor: "connect your Whatsminer fleet to AMS"
- /en/antminer-firmware/install — anchor: "Antminer firmware installation" (cross-cluster, mixed-fleet)

---

## Schema

Primary: HowTo
Secondary: FAQPage

HowTo schema: each numbered step in Method 1 should be a `HowToStep` with `name` and `text`. Include `supply` referencing the firmware package download.

---

## Word Count Target

1,800–2,400 words. More complex than an update guide because it covers three methods, post-install configuration, and recovery. Depth comes from technical specificity.

---

## Production Notes

- This is the highest-risk page in the cluster for technical accuracy. Incorrect installation steps can brick units.
- The recovery section is non-negotiable — operators will attempt recovery if installation fails and will return to this page. Omitting it leaves them stranded.
- Every command, UI path, and API call must be verified on actual Whatsminer hardware before publication.
- Hardware revision mismatch warning must appear in the pre-installation checklist AND in the FAQ. This is the most common operator mistake.
