#!/usr/bin/env python3
"""
Yandex Direct auto-sync for BiXBiT dashboard.
Fetches campaign data from Yandex Direct Reports API and writes
to Supabase (state.days[date].yandex and state.periods[key].yandex).

Run daily via GitHub Actions at 01:00 UTC (04:00 Moscow).

Required env vars:
  YANDEX_DIRECT_TOKEN  — OAuth token with direct:api scope
  YANDEX_DIRECT_LOGIN  — advertiser client login (if accessing a client account
                          from an agency/operator account; omit for direct access)
  SUPABASE_URL         — e.g. https://bjczjgybcdfpeukfsfwh.supabase.co
  SUPABASE_ANON_KEY    — Supabase anon/service-role key
"""

import json
import os
import sys
import time
import math
import hashlib
import requests
from datetime import datetime, timedelta, date, timezone

# ── Config ────────────────────────────────────────────────────────────────────
YANDEX_TOKEN = os.environ.get('YANDEX_DIRECT_TOKEN', '')
YANDEX_LOGIN = os.environ.get('YANDEX_DIRECT_LOGIN', '')  # blank = direct access
SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY = os.environ.get('SUPABASE_ANON_KEY', '')

DIRECT_API_URL = 'https://api.direct.yandex.com/json/v5/reports'
SUPABASE_TABLE = 'dashboard_state'
SUPABASE_ROW   = 'bixbit'

# Report fields to request
REPORT_FIELDS = [
    'CampaignId',
    'CampaignName',
    'Impressions',
    'Clicks',
    'Ctr',         # already as percentage, e.g. "2.35" → 2.35 %
    'Cost',        # rubles, 2 decimal places in TSV
    'Conversions',
]

# ── Yandex Direct API ─────────────────────────────────────────────────────────

def _direct_headers():
    h = {
        'Authorization': f'Bearer {YANDEX_TOKEN}',
        'Accept-Language': 'en',
        'Content-Type': 'application/json',
        'skipReportSummary': 'true',   # skip "Total" row in TSV
    }
    if YANDEX_LOGIN:
        h['Client-Login'] = YANDEX_LOGIN
    return h


def fetch_report(date_from: str, date_to: str) -> str | None:
    """
    Call Yandex Direct Reports API and return raw TSV string.
    Handles 201/202 polling (the API can queue large reports).
    Returns None on unrecoverable error.
    """
    body = {
        'params': {
            'SelectionCriteria': {
                'DateFrom': date_from,
                'DateTo':   date_to,
            },
            'FieldNames':   REPORT_FIELDS,
            # Report name must be unique per account; include dates to avoid clash.
            'ReportName':   f'bixbit_{date_from}_{date_to}',
            'ReportType':   'CAMPAIGN_PERFORMANCE_REPORT',
            'DateRangeType':'CUSTOM_DATE',
            'Format':       'TSV',
            'IncludeVAT':   'NO',
            'IncludeDiscount': 'NO',
        }
    }

    headers = _direct_headers()

    for attempt in range(12):
        try:
            resp = requests.post(DIRECT_API_URL, headers=headers, json=body, timeout=60)
        except requests.RequestException as e:
            print(f'  HTTP error (attempt {attempt+1}): {e}')
            time.sleep(15)
            continue

        if resp.status_code == 200:
            return resp.text

        if resp.status_code in (201, 202):
            retry_after = int(resp.headers.get('retryIn', 15))
            print(f'  Report queued (HTTP {resp.status_code}), retrying in {retry_after}s …')
            time.sleep(retry_after)
            continue

        # 400 can happen if the ReportName clashes with an in-flight job.
        # Wait and retry once.
        if resp.status_code == 400:
            err = resp.text[:300]
            if 'already exists' in err.lower() or 'ALREADY_EXISTING' in err:
                print(f'  Report name collision, waiting 30s …')
                time.sleep(30)
                continue

        print(f'  API error {resp.status_code}: {resp.text[:400]}')
        return None

    print('  Exceeded max retries for Yandex Direct report')
    return None


def parse_tsv(raw: str) -> list[dict]:
    """Parse TSV report into list-of-dicts. Skips blank and Total lines."""
    if not raw:
        return []
    lines = raw.strip().split('\n')
    if len(lines) < 2:
        return []
    headers = lines[0].split('\t')
    rows = []
    for line in lines[1:]:
        line = line.strip()
        if not line or line.lower().startswith('total'):
            continue
        cols = line.split('\t')
        rows.append(dict(zip(headers, cols)))
    return rows


# ── Number helpers ────────────────────────────────────────────────────────────

def _f(val, fallback=0.0) -> float:
    try:
        return float(val)
    except (ValueError, TypeError):
        return fallback


def _i(val, fallback=0) -> int:
    try:
        v = int(float(val))
        return v
    except (ValueError, TypeError):
        return fallback


def _round4(x: float) -> float:
    """Round to 4 decimal places (enough for sub-cent CPC values)."""
    return math.floor(x * 10_000 + 0.5) / 10_000


def campaign_id(campaign_name: str) -> str:
    """Stable short ID derived from campaign name (deterministic across runs)."""
    return 'y_' + hashlib.md5(campaign_name.encode()).hexdigest()[:8]


# ── Supabase helpers ──────────────────────────────────────────────────────────

def _sb_headers():
    return {
        'apikey':        SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type':  'application/json',
    }


def load_state() -> dict:
    url = f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?key=eq.{SUPABASE_ROW}&select=payload'
    resp = requests.get(url, headers=_sb_headers(), timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if data:
        return data[0]['payload'] or {}
    return {}


def save_state(state: dict):
    url = f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?key=eq.{SUPABASE_ROW}'
    headers = {**_sb_headers(), 'Prefer': 'return=minimal'}
    resp = requests.patch(url, headers=headers, json={'payload': state}, timeout=30)
    resp.raise_for_status()


# ── Quarter helpers ───────────────────────────────────────────────────────────

def quarter_range(d: date) -> tuple[str, str]:
    """Return (quarter_start, quarter_end) as YYYY-MM-DD strings for the date d."""
    q = (d.month - 1) // 3          # 0-based quarter index
    start_month = q * 3 + 1
    end_month = start_month + 2
    # Last day of end_month
    if end_month == 12:
        end_day = 31
    else:
        end_day = (date(d.year, end_month + 1, 1) - timedelta(days=1)).day
    return (
        date(d.year, start_month, 1).isoformat(),
        date(d.year, end_month, end_day).isoformat(),
    )


def period_key(from_date: str, to_date: str) -> str:
    return f'{from_date}|{to_date}'


# ── Data processing ───────────────────────────────────────────────────────────

def rows_to_daily_snapshot(rows: list[dict]) -> dict:
    """
    Convert raw TSV rows for a single day into the state.days[date].yandex format:
    { budget, clicks, impressions, campaigns: [{id, name, budget, clicks, impressions, conversions}] }
    """
    campaigns = []
    for row in rows:
        name       = row.get('CampaignName', '').strip()
        impressions = _i(row.get('Impressions', 0))
        clicks      = _i(row.get('Clicks', 0))
        cost        = _f(row.get('Cost', 0))          # RUB
        conversions = _i(row.get('Conversions', 0))
        if not name or (impressions == 0 and clicks == 0 and cost == 0):
            continue
        campaigns.append({
            'id':          campaign_id(name),
            'name':        name,
            'budget':      round(cost, 2),
            'impressions': impressions,
            'clicks':      clicks,
            'conversions': conversions,
            'status':      'active',
        })

    total_budget      = round(sum(c['budget'] for c in campaigns), 2)
    total_impressions = sum(c['impressions'] for c in campaigns)
    total_clicks      = sum(c['clicks'] for c in campaigns)

    return {
        'budget':      total_budget,
        'impressions': total_impressions,
        'clicks':      total_clicks,
        'campaigns':   campaigns,
        'updated':     datetime.now(timezone.utc).isoformat(),
    }


def aggregate_from_days(state: dict, from_date: str, to_date: str) -> dict | None:
    """
    Aggregate state.days[*].yandex snapshots within [from_date, to_date].
    Returns aggregated dict in the same format as rows_to_daily_snapshot,
    plus ctr and cpc. Returns None if no data found.
    """
    days = state.get('days', {})
    camp_map: dict[str, dict] = {}
    total_budget      = 0.0
    total_impressions = 0
    total_clicks      = 0
    has_data = False

    d = datetime.strptime(from_date, '%Y-%m-%d').date()
    end = datetime.strptime(to_date, '%Y-%m-%d').date()
    while d <= end:
        key = d.isoformat()
        y = days.get(key, {}).get('yandex')
        if y:
            has_data = True
            total_budget      += y.get('budget', 0)
            total_impressions += y.get('impressions', 0)
            total_clicks      += y.get('clicks', 0)
            for c in y.get('campaigns', []):
                cid = c.get('id') or campaign_id(c.get('name', ''))
                if cid not in camp_map:
                    camp_map[cid] = {
                        'id':          cid,
                        'name':        c.get('name', ''),
                        'budget':      0.0,
                        'impressions': 0,
                        'clicks':      0,
                        'conversions': 0,
                        'status':      c.get('status', 'active'),
                    }
                camp_map[cid]['budget']      += c.get('budget', 0)
                camp_map[cid]['impressions'] += c.get('impressions', 0)
                camp_map[cid]['clicks']      += c.get('clicks', 0)
                camp_map[cid]['conversions'] += c.get('conversions', 0)
        d += timedelta(days=1)

    if not has_data:
        return None

    total_budget = round(total_budget, 2)
    campaigns = []
    for c in camp_map.values():
        campaigns.append({
            **c,
            'budget': round(c['budget'], 2),
        })

    ctr = round(total_clicks / total_impressions * 100, 2) if total_impressions > 0 else 0
    cpc = _round4(total_budget / total_clicks) if total_clicks > 0 else 0

    return {
        'budget':      total_budget,
        'impressions': total_impressions,
        'clicks':      total_clicks,
        'ctr':         ctr,
        'cpc':         cpc,
        'campaigns':   campaigns,
    }


def build_period_yandex(agg: dict, existing_period_yandex: dict) -> dict:
    """
    Merge aggregated daily data with the existing period's Yandex entry.
    Preserves manually-entered conversions, cpl, planfix_leads at the period
    and campaign level.
    """
    # Preserve manual campaign-level fields from the existing period
    existing_camps = {c.get('id', ''): c for c in existing_period_yandex.get('campaigns', [])}

    merged_campaigns = []
    for c in agg.get('campaigns', []):
        cid = c.get('id', '')
        existing = existing_camps.get(cid, {})
        merged_campaigns.append({
            **c,
            # Auto-computed
            'budget':      c['budget'],
            'impressions': c['impressions'],
            'clicks':      c['clicks'],
            # Preserve manually-entered values from existing period
            'conversions':   existing.get('conversions', c.get('conversions', 0)),
            'planfix_leads': existing.get('planfix_leads', 0),
            'status':        existing.get('status', c.get('status', 'active')),
        })

    total_budget      = agg['budget']
    total_impressions = agg['impressions']
    total_clicks      = agg['clicks']
    total_ctr         = agg['ctr']
    total_cpc         = agg['cpc']

    # Preserve period-level manual fields
    existing_conversions   = existing_period_yandex.get('conversions', 0)
    existing_cpl           = existing_period_yandex.get('cpl', 0)
    existing_planfix_leads = existing_period_yandex.get('planfix_leads', 0)

    return {
        'budget':        total_budget,
        'impressions':   total_impressions,
        'clicks':        total_clicks,
        'ctr':           total_ctr,
        'cpc':           total_cpc,
        'conversions':   existing_conversions,
        'cpl':           existing_cpl,
        'planfix_leads': existing_planfix_leads,
        'campaigns':     merged_campaigns,
        'updated':       datetime.now(timezone.utc).isoformat(),
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Validate config
    if not YANDEX_TOKEN:
        print('ERROR: YANDEX_DIRECT_TOKEN is not set'); sys.exit(1)
    if not SUPABASE_URL or not SUPABASE_KEY:
        print('ERROR: SUPABASE_URL or SUPABASE_ANON_KEY is not set'); sys.exit(1)

    today     = datetime.now(timezone.utc).date()
    yesterday = today - timedelta(days=1)
    y_str     = yesterday.isoformat()

    q_from, q_to = quarter_range(yesterday)
    pkey         = period_key(q_from, q_to)

    print(f'Yandex Direct sync — {y_str}')
    print(f'Quarter period: {q_from} → {q_to}  (key: {pkey})')

    # ── 1. Fetch yesterday's report ─────────────────────────────────────────
    print(f'\nFetching daily report ({y_str}) …')
    daily_tsv = fetch_report(y_str, y_str)
    if daily_tsv is None:
        print('Could not fetch daily report — aborting'); sys.exit(1)

    daily_rows = parse_tsv(daily_tsv)
    print(f'  Parsed {len(daily_rows)} campaign row(s)')

    if not daily_rows:
        print('No campaign data for yesterday — nothing to write'); sys.exit(0)

    daily_snapshot = rows_to_daily_snapshot(daily_rows)
    print(f'  Budget: {daily_snapshot["budget"]} RUB, '
          f'clicks: {daily_snapshot["clicks"]}, '
          f'impressions: {daily_snapshot["impressions"]}')

    # ── 2. Load current Supabase state ──────────────────────────────────────
    print('\nLoading Supabase state …')
    state = load_state()

    # ── 3. Write daily snapshot ─────────────────────────────────────────────
    state.setdefault('days', {})
    state['days'].setdefault(y_str, {})
    state['days'][y_str]['yandex'] = daily_snapshot
    print(f'  Wrote state.days[{y_str}].yandex')

    # ── 4. Aggregate quarter and write period ────────────────────────────────
    print(f'\nAggregating quarter ({q_from} → {q_to}) …')
    agg = aggregate_from_days(state, q_from, min(q_to, y_str))

    if agg:
        state.setdefault('periods', {})
        state['periods'].setdefault(pkey, {})
        existing_yandex = state['periods'][pkey].get('yandex', {})
        state['periods'][pkey]['yandex'] = build_period_yandex(agg, existing_yandex)
        print(f'  Budget: {agg["budget"]} RUB, '
              f'clicks: {agg["clicks"]}, '
              f'impressions: {agg["impressions"]}, '
              f'ctr: {agg["ctr"]}%, '
              f'cpc: {agg["cpc"]} RUB')
        print(f'  Wrote state.periods[{pkey}].yandex')
    else:
        print('  No aggregated data found (days may be empty)')

    # ── 5. Save state ────────────────────────────────────────────────────────
    print('\nSaving state to Supabase …')
    save_state(state)
    print('Done ✓')


if __name__ == '__main__':
    main()
