#!/usr/bin/env python3
"""Google Ads auto-sync for BiXBiT dashboard.

Ежедневно (без аргументов): снимок за вчера → state.days[вчера].google и
итоги квартала с начала квартала по вчера одним запросом к API → periods[квартал].google.
Пересчёт прошлого квартала: --quarter 2026-Q3 (или --from/--to).

Бюджет, показы, клики, конверсии и статусы — из Google Ads; Planfix-лиды
(ручной ввод) сохраняются по совпадению id или названия кампании.
Предыдущая версия блока google сохраняется в payload.backups.
"""
import argparse, json, os, sys, math, hashlib, requests
from datetime import datetime, timedelta, date, timezone

DEVELOPER_TOKEN   = os.environ.get('GOOGLE_ADS_DEVELOPER_TOKEN', '')
CLIENT_ID         = os.environ.get('GOOGLE_ADS_CLIENT_ID', '')
CLIENT_SECRET     = os.environ.get('GOOGLE_ADS_CLIENT_SECRET', '')
REFRESH_TOKEN     = os.environ.get('GOOGLE_ADS_REFRESH_TOKEN', '')
CUSTOMER_ID       = os.environ.get('GOOGLE_ADS_CUSTOMER_ID', '').replace('-', '')
LOGIN_CUSTOMER_ID = os.environ.get('GOOGLE_ADS_LOGIN_CUSTOMER_ID', '').replace('-', '')
SUPABASE_URL = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY = os.environ.get('SUPABASE_ANON_KEY', '')
SUPABASE_TABLE = 'dashboard_state'
SUPABASE_ROW   = 'bixbit'
API_VERSION    = 'v25'
GOOGLE_ADS_API = f'https://googleads.googleapis.com/{API_VERSION}'

GAQL_QUERY = """
SELECT campaign.id, campaign.name, campaign.status,
  metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.ctr, metrics.conversions, metrics.average_cpc
FROM campaign
WHERE segments.date = '{date}'
  AND campaign.status != 'REMOVED'
  AND metrics.impressions > 0
"""

GAQL_RANGE = """
SELECT campaign.id, campaign.name, campaign.status,
  metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM campaign
WHERE segments.date BETWEEN '{start}' AND '{end}'
  AND campaign.status != 'REMOVED'
  AND metrics.impressions > 0
"""

def get_access_token():
    resp = requests.post('https://oauth2.googleapis.com/token', data={
        'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN, 'grant_type': 'refresh_token',
    }, timeout=30)
    resp.raise_for_status()
    return resp.json()['access_token']

def ads_headers(token, use_mcc=True):
    h = {'Authorization': f'Bearer {token}', 'developer-token': DEVELOPER_TOKEN,
         'Content-Type': 'application/json'}
    if use_mcc and LOGIN_CUSTOMER_ID and LOGIN_CUSTOMER_ID != CUSTOMER_ID:
        h['login-customer-id'] = LOGIN_CUSTOMER_ID
    return h

def fetch_campaigns(target_date=None, query=None):
    try:
        token = get_access_token()
        print('  OAuth token obtained OK')
    except Exception as e:
        print(f'  OAuth error: {e}')
        return None
    url = f'{GOOGLE_ADS_API}/customers/{CUSTOMER_ID}/googleAds:searchStream'
    query = (query or GAQL_QUERY.format(date=target_date)).strip()
    attempts = [(True, 'with MCC'), (False, 'direct (no MCC)')] \
        if LOGIN_CUSTOMER_ID and LOGIN_CUSTOMER_ID != CUSTOMER_ID \
        else [(False, 'direct')]
    last_error = None
    for use_mcc, label in attempts:
        print(f'  Trying {label} …')
        try:
            resp = requests.post(url, headers=ads_headers(token, use_mcc),
                                 json={'query': query}, timeout=60)
        except requests.RequestException as e:
            print(f'  HTTP error: {e}')
            return None
        if resp.ok:
            rows = []
            for line in resp.text.strip().splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                    for r in chunk.get('results', []):
                        rows.append(r)
                except Exception:
                    pass
            print(f'  Success via {label}')
            return rows
        if resp.status_code == 403 and 'USER_PERMISSION_DENIED' in resp.text:
            print(f'  USER_PERMISSION_DENIED via {label} — trying next option')
            last_error = resp.text[:400]
            continue
        else:
            print(f'  API error {resp.status_code}: {resp.text[:600]}')
            return None
    print(f'  All attempts failed. Last error: {last_error}')
    return None

def _f(v, d=0.0):
    try: return float(v)
    except: return d

def _i(v, d=0):
    try: return int(float(v))
    except: return d

def _r4(x): return math.floor(x * 10000 + 0.5) / 10000
def cid(name): return 'g_' + hashlib.md5(name.encode()).hexdigest()[:8]
def _sbh(): return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}',
                    'Content-Type': 'application/json'}

_ROW_COL = None  # 'project' (dashboard) or legacy 'key'

def load_state():
    global _ROW_COL
    for col in ('project', 'key'):
        r = requests.get(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?{col}=eq.{SUPABASE_ROW}&select=payload',
                         headers=_sbh(), timeout=30)
        if r.status_code == 400:  # column does not exist
            continue
        r.raise_for_status()
        d = r.json()
        if d:
            _ROW_COL = col
            print(f'  Supabase row found by column "{col}"')
            return d[0]['payload'] or {}
    raise RuntimeError(f'Supabase row "{SUPABASE_ROW}" not found in {SUPABASE_TABLE} — aborting to avoid data loss')

def save_state(state):
    if not _ROW_COL:
        raise RuntimeError('save_state called before successful load_state')
    r = requests.patch(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?{_ROW_COL}=eq.{SUPABASE_ROW}',
                       headers={**_sbh(), 'Prefer': 'return=minimal'},
                       json={'payload': state}, timeout=30)
    r.raise_for_status()

def quarter_range(d):
    q = (d.month - 1) // 3
    sm = q * 3 + 1; em = sm + 2
    ed = 31 if em == 12 else (date(d.year, em+1, 1) - timedelta(days=1)).day
    return date(d.year, sm, 1).isoformat(), date(d.year, em, ed).isoformat()

def period_key(f, t): return f'{f}|{t}'

def rows_to_daily_snapshot(rows):
    camps = []
    for r in rows:
        c = r.get('campaign', {}); m = r.get('metrics', {})
        name = c.get('name', '').strip()
        if not name: continue
        cost = round(_i(m.get('costMicros', 0)) / 1_000_000, 2)
        camps.append({'id': cid(name), 'name': name, 'budget': cost,
            'impressions': _i(m.get('impressions', 0)),
            'clicks': _i(m.get('clicks', 0)),
            'conversions': round(_f(m.get('conversions', 0))),
            'status': c.get('status', 'ENABLED').lower()})
    tb = round(sum(c['budget'] for c in camps), 2)
    return {'budget': tb, 'impressions': sum(c['impressions'] for c in camps),
            'clicks': sum(c['clicks'] for c in camps), 'campaigns': camps,
            'updated': datetime.now(timezone.utc).isoformat()}

def build_period_google(agg, existing):
    """Метрики — из API; planfix_leads (CRM, ручной ввод) — из прежних данных по id или названию."""
    old = existing.get('campaigns', []) or []
    by_id = {c.get('id'): c for c in old if c.get('id')}
    by_name = {(c.get('name') or '').strip().lower(): c for c in old}
    mc = []
    for c in agg['campaigns']:
        p = by_id.get(c['id']) or by_name.get(c['name'].strip().lower()) or {}
        mc.append({**c, 'planfix_leads': p.get('planfix_leads', 0)})
    mc.sort(key=lambda c: -c['budget'])
    tb = round(sum(c['budget'] for c in mc), 2)
    ti = sum(c['impressions'] for c in mc); tc = sum(c['clicks'] for c in mc)
    tcv = sum(c['conversions'] for c in mc); tpf = sum(c['planfix_leads'] or 0 for c in mc)
    return {'budget': tb, 'impressions': ti, 'clicks': tc,
            'ctr': round(tc / ti * 100, 2) if ti else 0,
            'cpc': _r4(tb / tc) if tc else 0,
            'conversions': tcv, 'cpl': round(tb / tcv, 2) if tcv else 0,
            'planfix_leads': tpf, 'campaigns': mc,
            'source': 'google-ads-api',
            'updated': datetime.now(timezone.utc).isoformat()}

def sync_period(state, f, t):
    print(f'\nFetching campaign totals {f} .. {t} ...')
    rows = fetch_campaigns(query=GAQL_RANGE.format(start=f, end=t))
    if rows is None:
        print('Could not fetch — aborting')
        sys.exit(1)
    agg = rows_to_daily_snapshot(rows)
    print(f'  {len(agg["campaigns"])} campaigns, budget ${agg["budget"]}, '
          f'impressions {agg["impressions"]}, clicks {agg["clicks"]}')
    if not agg['campaigns']:
        print('  No campaigns with impressions in this range — period not changed')
        return False
    # период хранится под ключом полного квартала (или заданного диапазона)
    return agg

def write_period(state, pkey, agg):
    state.setdefault('periods', {})
    state['periods'].setdefault(pkey, {})
    eg = state['periods'][pkey].get('google', {}) or {}
    if eg and eg.get('source') != 'google-ads-api':
        state.setdefault('backups', {})[f'{pkey}.google.{datetime.now(timezone.utc).date().isoformat()}'] = eg
        print('  Previous (manual) google block saved to payload.backups')
    state['periods'][pkey]['google'] = build_period_google(agg, eg)
    g = state['periods'][pkey]['google']
    print(f'  periods[{pkey}].google: ${g["budget"]}, CTR {g["ctr"]}%, CPC ${g["cpc"]}, '
          f'conv {g["conversions"]}, planfix {g["planfix_leads"]}')

def parse_quarter(spec):
    y, q = spec.upper().split('-Q'); y, q = int(y), int(q)
    return quarter_range(date(y, 3 * (q - 1) + 1, 1))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quarter', help='e.g. 2026-Q3 — recompute a whole quarter from the API')
    ap.add_argument('--from', dest='dfrom'); ap.add_argument('--to', dest='dto')
    args = ap.parse_args()

    missing = [(n, v) for n, v in [
        ('GOOGLE_ADS_DEVELOPER_TOKEN', DEVELOPER_TOKEN),
        ('GOOGLE_ADS_CLIENT_ID', CLIENT_ID),
        ('GOOGLE_ADS_CLIENT_SECRET', CLIENT_SECRET),
        ('GOOGLE_ADS_REFRESH_TOKEN', REFRESH_TOKEN),
        ('GOOGLE_ADS_CUSTOMER_ID', CUSTOMER_ID),
        ('SUPABASE_URL', SUPABASE_URL),
        ('SUPABASE_ANON_KEY', SUPABASE_KEY)] if not v]
    if missing:
        for n, _ in missing:
            print(f'ERROR: {n} is not set')
        sys.exit(1)

    today = datetime.now(timezone.utc).date()
    yesterday = today - timedelta(days=1)
    print(f'Login customer ID set: {bool(LOGIN_CUSTOMER_ID)}')

    # ── Пересчёт заданного периода ──
    if args.quarter or (args.dfrom and args.dto):
        f, t = parse_quarter(args.quarter) if args.quarter else (args.dfrom, args.dto)
        end = min(t, yesterday.isoformat())
        agg = sync_period(None, f, end)
        if not agg:
            sys.exit(0)
        state = load_state()
        write_period(state, period_key(f, t), agg)
        save_state(state)
        print('Done ✓')
        return

    # ── Ежедневный режим ──
    y_str = yesterday.isoformat()
    q_from, q_to = quarter_range(yesterday)
    pkey = period_key(q_from, q_to)
    print(f'Google Ads sync — {y_str}; quarter {q_from} -> {q_to}')

    rows = fetch_campaigns(y_str)
    if rows is None:
        print('Could not fetch — aborting')
        sys.exit(1)
    snap = rows_to_daily_snapshot(rows)
    print(f'  Yesterday: {len(rows)} campaigns, ${snap["budget"]}, clicks {snap["clicks"]}')

    agg = sync_period(None, q_from, y_str)

    state = load_state()
    state.setdefault('days', {}).setdefault(y_str, {})['google'] = snap
    if agg:
        write_period(state, pkey, agg)
    save_state(state)
    print('Done ✓')

if __name__ == '__main__':
    main()
