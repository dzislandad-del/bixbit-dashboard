#!/usr/bin/env python3
"""Google Ads auto-sync for BiXBiT dashboard."""
import json, os, sys, math, hashlib, requests
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

def get_access_token():
    resp = requests.post('https://oauth2.googleapis.com/token', data={
        'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN, 'grant_type': 'refresh_token',
    }, timeout=30)
    resp.raise_for_status()
    return resp.json()['access_token']

def ads_headers(token):
    h = {'Authorization': f'Bearer {token}', 'developer-token': DEVELOPER_TOKEN, 'Content-Type': 'application/json'}
    if LOGIN_CUSTOMER_ID:
        h['login-customer-id'] = LOGIN_CUSTOMER_ID
    return h

def fetch_campaigns(target_date):
    try: token = get_access_token()
    except Exception as e: print(f'  OAuth error: {e}'); return None
    url = f'{GOOGLE_ADS_API}/customers/{CUSTOMER_ID}/googleAds:searchStream'
    try:
        resp = requests.post(url, headers=ads_headers(token),
                             json={'query': GAQL_QUERY.format(date=target_date).strip()}, timeout=60)
    except requests.RequestException as e: print(f'  HTTP error: {e}'); return None
    if not resp.ok: print(f'  API error {resp.status_code}: {resp.text[:400]}'); return None
    rows = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if not line: continue
        try:
            chunk = json.loads(line)
            for r in chunk.get('results', []): rows.append(r)
        except: pass
    return rows

def _f(v, d=0.0):
    try: return float(v)
    except: return d

def _i(v, d=0):
    try: return int(float(v))
    except: return d

def _r4(x): return math.floor(x * 10000 + 0.5) / 10000
def cid(name): return 'g_' + hashlib.md5(name.encode()).hexdigest()[:8]
def _sbh(): return {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}', 'Content-Type': 'application/json'}

def load_state():
    r = requests.get(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?key=eq.{SUPABASE_ROW}&select=payload', headers=_sbh(), timeout=30)
    r.raise_for_status(); d = r.json()
    return d[0]['payload'] or {} if d else {}

def save_state(state):
    r = requests.patch(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?key=eq.{SUPABASE_ROW}',
                       headers={**_sbh(), 'Prefer': 'return=minimal'}, json={'payload': state}, timeout=30)
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
            'impressions': _i(m.get('impressions', 0)), 'clicks': _i(m.get('clicks', 0)),
            'conversions': round(_f(m.get('conversions', 0))), 'status': c.get('status', 'ENABLED').lower()})
    tb = round(sum(c['budget'] for c in camps), 2)
    return {'budget': tb, 'impressions': sum(c['impressions'] for c in camps),
            'clicks': sum(c['clicks'] for c in camps), 'campaigns': camps,
            'updated': datetime.now(timezone.utc).isoformat()}

def aggregate_from_days(state, fd, td):
    days = state.get('days', {}); cm = {}; tb = 0.0; ti = 0; tc = 0; has = False
    d = datetime.strptime(fd, '%Y-%m-%d').date(); end = datetime.strptime(td, '%Y-%m-%d').date()
    while d <= end:
        g = days.get(d.isoformat(), {}).get('google')
        if g:
            has = True; tb += g.get('budget', 0); ti += g.get('impressions', 0); tc += g.get('clicks', 0)
            for c in g.get('campaigns', []):
                k = c.get('id') or cid(c.get('name', ''))
                if k not in cm: cm[k] = {'id': k, 'name': c.get('name',''), 'budget': 0.0, 'impressions': 0, 'clicks': 0, 'conversions': 0, 'status': c.get('status','enabled')}
                cm[k]['budget'] += c.get('budget', 0); cm[k]['impressions'] += c.get('impressions', 0)
                cm[k]['clicks'] += c.get('clicks', 0); cm[k]['conversions'] += c.get('conversions', 0)
        d += timedelta(days=1)
    if not has: return None
    tb = round(tb, 2); camps = [{**c, 'budget': round(c['budget'], 2)} for c in cm.values()]
    ctr = round(tc / ti * 100, 2) if ti > 0 else 0; cpc = _r4(tb / tc) if tc > 0 else 0
    return {'budget': tb, 'impressions': ti, 'clicks': tc, 'ctr': ctr, 'cpc': cpc, 'campaigns': camps}

def build_period_google(agg, existing):
    ec = {c.get('id',''): c for c in existing.get('campaigns', [])}
    mc = []
    for c in agg.get('campaigns', []):
        k = c.get('id',''); p = ec.get(k, {})
        mc.append({**c, 'conversions': p.get('conversions', c.get('conversions', 0)),
                   'planfix_leads': p.get('planfix_leads', 0), 'status': p.get('status', c.get('status','enabled'))})
    return {'budget': agg['budget'], 'impressions': agg['impressions'], 'clicks': agg['clicks'],
            'ctr': agg['ctr'], 'cpc': agg['cpc'], 'conversions': existing.get('conversions', 0),
            'cpl': existing.get('cpl', 0), 'planfix_leads': existing.get('planfix_leads', 0),
            'campaigns': mc, 'updated': datetime.now(timezone.utc).isoformat()}

def main():
    missing = [(n, v) for n, v in [('GOOGLE_ADS_DEVELOPER_TOKEN', DEVELOPER_TOKEN),
        ('GOOGLE_ADS_CLIENT_ID', CLIENT_ID), ('GOOGLE_ADS_CLIENT_SECRET', CLIENT_SECRET),
        ('GOOGLE_ADS_REFRESH_TOKEN', REFRESH_TOKEN), ('GOOGLE_ADS_CUSTOMER_ID', CUSTOMER_ID),
        ('SUPABASE_URL', SUPABASE_URL), ('SUPABASE_ANON_KEY', SUPABASE_KEY)] if not v]
    if missing:
        for n, _ in missing: print(f'ERROR: {n} is not set')
        sys.exit(1)
    today = datetime.now(timezone.utc).date(); yesterday = today - timedelta(days=1); y_str = yesterday.isoformat()
    q_from, q_to = quarter_range(yesterday); pkey = period_key(q_from, q_to)
    print(f'Google Ads sync — {y_str}')
    print(f'Quarter: {q_from} → {q_to}  (key: {pkey})')
    print(f'\nFetching campaigns for {y_str} …')
    rows = fetch_campaigns(y_str)
    if rows is None: print('Could not fetch — aborting'); sys.exit(1)
    print(f'  Got {len(rows)} campaign row(s)')
    if not rows: print('No data for yesterday'); sys.exit(0)
    snap = rows_to_daily_snapshot(rows)
    print(f'  Budget: ${snap["budget"]}, clicks: {snap["clicks"]}, impressions: {snap["impressions"]}')
    print('\nLoading Supabase state …'); state = load_state()
    state.setdefault('days', {}); state['days'].setdefault(y_str, {})
    state['days'][y_str]['google'] = snap; print(f'  Wrote state.days[{y_str}].google')
    print(f'\nAggregating quarter …')
    agg = aggregate_from_days(state, q_from, min(q_to, y_str))
    if agg:
        state.setdefault('periods', {}); state['periods'].setdefault(pkey, {})
        eg = state['periods'][pkey].get('google', {})
        state['periods'][pkey]['google'] = build_period_google(agg, eg)
        print(f'  Budget: ${agg["budget"]}, ctr: {agg["ctr"]}%, cpc: ${agg["cpc"]}')
    print('\nSaving to Supabase …'); save_state(state); print('Done ✓')

if __name__ == '__main__':
    main()

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
            'impressions': _i(m.get('impressions', 0)), 'clicks': _i(m.get('clicks', 0)),
            'conversions': round(_f(m.get('conversions', 0))), 'status': c.get('status', 'ENABLED').lower()})
    tb = round(sum(c['budget'] for c in camps), 2)
    return {'budget': tb, 'impressions': sum(c['impressions'] for c in camps),
            'clicks': sum(c['clicks'] for c in camps), 'campaigns': camps,
            'updated': datetime.now(timezone.utc).isoformat()}

def aggregate_from_days(state, fd, td):
    days = state.get('days', {}); cm = {}; tb = 0.0; ti = 0; tc = 0; has = False
    d = datetime.strptime(fd, '%Y-%m-%d').date(); end = datetime.strptime(td, '%Y-%m-%d').date()
    while d <= end:
        g = days.get(d.isoformat(), {}).get('google')
        if g:
            has = True; tb += g.get('budget', 0); ti += g.get('impressions', 0); tc += g.get('clicks', 0)
            for c in g.get('campaigns', []):
                k = c.get('id') or cid(c.get('name', ''))
                if k not in cm: cm[k] = {'id': k, 'name': c.get('name',''), 'budget': 0.0, 'impressions': 0, 'clicks': 0, 'conversions': 0, 'status': c.get('status','enabled')}
                cm[k]['budget'] += c.get('budget', 0); cm[k]['impressions'] += c.get('impressions', 0)
                cm[k]['clicks'] += c.get('clicks', 0); cm[k]['conversions'] += c.get('conversions', 0)
        d += timedelta(days=1)
    if not has: return None
    tb = round(tb, 2); camps = [{**c, 'budget': round(c['budget'], 2)} for c in cm.values()]
    ctr = round(tc / ti * 100, 2) if ti > 0 else 0; cpc = _r4(tb / tc) if tc > 0 else 0
    return {'budget': tb, 'impressions': ti, 'clicks': tc, 'ctr': ctr, 'cpc': cpc, 'campaigns': camps}

def build_period_google(agg, existing):
    ec = {c.get('id',''): c for c in existing.get('campaigns', [])}
    mc = []
    for c in agg.get('campaigns', []):
        k = c.get('id',''); p = ec.get(k, {})
        mc.append({**c, 'conversions': p.get('conversions', c.get('conversions', 0)),
                   'planfix_leads': p.get('planfix_leads', 0), 'status': p.get('status', c.get('status','enabled'))})
    return {'budget': agg['budget'], 'impressions': agg['impressions'], 'clicks': agg['clicks'],
            'ctr': agg['ctr'], 'cpc': agg['cpc'], 'conversions': existing.get('conversions', 0),
            'cpl': existing.get('cpl', 0), 'planfix_leads': existing.get('planfix_leads', 0),
            'campaigns': mc, 'updated': datetime.now(timezone.utc).isoformat()}

def main():
    missing = [(n, v) for n, v in [('GOOGLE_ADS_DEVELOPER_TOKEN', DEVELOPER_TOKEN),
        ('GOOGLE_ADS_CLIENT_ID', CLIENT_ID), ('GOOGLE_ADS_CLIENT_SECRET', CLIENT_SECRET),
        ('GOOGLE_ADS_REFRESH_TOKEN', REFRESH_TOKEN), ('GOOGLE_ADS_CUSTOMER_ID', CUSTOMER_ID),
        ('SUPABASE_URL', SUPABASE_URL), ('SUPABASE_ANON_KEY', SUPABASE_KEY)] if not v]
    if missing:
        for n, _ in missing: print(f'ERROR: {n} is not set')
        sys.exit(1)
    today = datetime.now(timezone.utc).date(); yesterday = today - timedelta(days=1); y_str = yesterday.isoformat()
    q_from, q_to = quarter_range(yesterday); pkey = period_key(q_from, q_to)
    print(f'Google Ads sync — {y_str}')
    print(f'Quarter: {q_from} → {q_to}  (key: {pkey})')
    print(f'\nFetching campaigns for {y_str} …')
    rows = fetch_campaigns(y_str)
    if rows is None: print('Could not fetch — aborting'); sys.exit(1)
    print(f'  Got {len(rows)} campaign row(s)')
    if not rows: print('No data for yesterday'); sys.exit(0)
    snap = rows_to_daily_snapshot(rows)
    print(f'  Budget: ${snap["budget"]}, clicks: {snap["clicks"]}, impressions: {snap["impressions"]}')
    print('\nLoading Supabase state …'); state = load_state()
    state.setdefault('days', {}); state['days'].setdefault(y_str, {})
    state['days'][y_str]['google'] = snap; print(f'  Wrote state.days[{y_str}].google')
    print(f'\nAggregating quarter …')
    agg = aggregate_from_days(state, q_from, min(q_to, y_str))
    if agg:
        state.setdefault('periods', {}); state['periods'].setdefault(pkey, {})
        eg = state['periods'][pkey].get('google', {})
        state['periods'][pkey]['google'] = build_period_google(agg, eg)
        print(f'  Budget: ${agg["budget"]}, ctr: {agg["ctr"]}%, cpc: ${agg["cpc"]}')
    print('\nSaving to Supabase …'); save_state(state); print('Done ✓')

if __name__ == '__main__':
    main()
