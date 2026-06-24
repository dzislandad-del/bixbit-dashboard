# Content Brief: ASIC Fleet Dashboard — Enterprise Requirements
**Slug:** `/en/ams/mining-fleet-dashboard`
**Cluster:** mining-fleet-monitoring
**Type:** Spoke — Informational / Feature Education
**Priority:** P2
**Created:** 2026-06-19

---

## Target Keywords

| Keyword | Role | Vol. |
|---|---|---|
| ASIC monitoring dashboard | Primary | [VOL: N/A — DataForSEO 401] |
| mining fleet dashboard | Primary | [VOL: N/A] |
| bitcoin mining farm dashboard | Secondary | [VOL: N/A] |
| ASIC farm dashboard | Secondary | [VOL: N/A] |
| mining operations dashboard | Tertiary | [VOL: N/A] |

---

## Search Intent

**Informational.** Operators and technical directors evaluating what a mining fleet dashboard should show — often at the stage of writing internal RFPs or evaluating trial environments. They want to understand what "good" looks like before committing to a platform.

High AI-citability: "what should a mining monitoring dashboard show" is a natural ChatGPT/Perplexity query this page should answer.

---

## H1 and Structure

**H1:** ASIC Fleet Dashboard: What Enterprise Mining Operations Need From a Monitoring Interface

### H2 Structure

**H2: What a Mining Fleet Dashboard Must Show**
- Fleet health summary: online count, offline count, alert count, total hashrate
- Per-unit view: hashrate, temperature, fan speed, power draw, pool connection status
- Alert queue: active alerts sorted by severity
- Historical trends: 7-day / 30-day hashrate, temperature, uptime per unit

**H2: Fleet-Level vs Per-Unit View**
- Fleet level: aggregate health; catch systemic issues (network outage, power event)
- Per-unit: fault isolation; identify individual failing hardware
- How AMS surfaces both layers `[VERIFY: AMS view hierarchy — fleet → site → rack → unit]`

**H2: Dashboard Design for Operations at Scale**
- 100 units: table view is fine
- 1,000 units: need filter by status (online/offline/alert), sort by hashrate or temperature, group by location
- 10,000 units: need saved views, bulk selection, automated health scoring `[VERIFY: AMS bulk operations and view capabilities at scale]`

**H2: What Separates Enterprise Dashboards from Basic Monitoring**
- Per-chip data (requires firmware integration — BiXBiT firmware) vs per-unit data (stock firmware)
- Historical baselines per unit (detect gradual degradation)
- Multi-site grouping
- Role-based access (operator sees everything; client sees own units only)
- API export for BI tools `[VERIFY: AMS API for data export]`

**H2: FAQ**

---

## FAQ (4 Questions)

1. **What should a mining fleet dashboard display?**
   At minimum: per-unit hashrate, temperature, online/offline status, alert count, and pool connection. Enterprise dashboards also show per-chip data, historical trends, power draw, and multi-site grouping.

2. **How does the BiXBiT AMS dashboard differ from the built-in Antminer/Whatsminer web UI?**
   The built-in ASIC web UI is per-unit and requires direct IP access. AMS provides fleet-wide visibility across all units with alerting, remote actions, and historical data in a single interface. `[VERIFY: AMS dashboard specifics]`

3. **Can I customize the AMS dashboard view?**
   `[VERIFY: AMS dashboard customization — saved views, column configuration, grouping]`

4. **Does AMS support mobile access to the fleet dashboard?**
   `[VERIFY: AMS mobile / responsive interface]`

---

## Internal Links

### From This Page To:
- `/en/ams` (pillar) — "BiXBiT AMS"
- `/en/ams/asic-fleet-management` — "fleet management guide"
- `/en/ams/mining-farm-alerts-automation` — "alert configuration"
- `/en/ams/mining-hosting-monitoring` — "multi-client dashboard views"

### To This Page From:
- `/en/ams` (pillar) — "dashboard features"
- `/en/ams/asic-fleet-management` — "dashboard section"

---

## Schema

`TechArticle` + `FAQPage`

## Word Count Target

1,400–1,600 words. Feature-education format — scannable headers, concrete examples.

---

## [VERIFY] Blockers

- `[VERIFY: AMS dashboard view hierarchy — fleet → site → rack → unit or other]`
- `[VERIFY: AMS — filter/sort capabilities at large fleet sizes]`
- `[VERIFY: AMS — bulk selection and operations on dashboard]`
- `[VERIFY: AMS — API for BI/data export]`
- `[VERIFY: AMS — mobile/responsive dashboard]`
- `[VERIFY: AMS — dashboard customization options]`
