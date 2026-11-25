#!/usr/bin/env python3
"""yandex_direct_sync.py — Яндекс Директ → дашборд (Supabase).

Ежедневно (без аргументов) пересчитывает текущий квартал с его начала по вчера одним
отчётом Reports API и пишет payload.periods["from|to"].yandex:
расход, показы, клики, CTR, CPC, конверсии, CPL и статус по каждой кампании.

Как и для Google Ads, в дашборд попадают:
  • работающие кампании (State = ON) — всегда, даже без показов;
  • остановленные/завершённые/архивные — только если у них были показы с STOPPED_SINCE
    (по умолчанию 2026-10-01). Кварталы, закончившиеся раньше этой даты, не фильтруются.

Расход переводится в доллары (дашборд показывает Директ в $): валюта аккаунта берётся
из API, курс — ЦБ РФ для RUB, НБРБ для BYN или из DIRECT_USD_RATE (единиц валюты за 1 $).
Planfix-лиды (ручной ввод) сохраняются по названию кампании; прежняя ручная версия
блока yandex один раз копируется в payload.backups.

Примеры:
  python3 scripts/yandex_direct_sync.py                    # текущий квартал
  python3 scripts/yandex_direct_sync.py --quarter 2026-Q3  # пересчёт прошлого квартала
  python3 scripts/yandex_direct_sync.py --dry-run          # показать, ничего не записывать

Секреты: YANDEX_DIRECT_TOKEN (OAuth, доступ к API Директа), YANDEX_DIRECT_LOGIN (логин
клиента — если токен агентский/представителя; иначе пусто), SUPABASE_URL, SUPABASE_ANON_KEY.
Необязательно: DIRECT_USD_RATE, DIRECT_GOALS (ID целей Метрики через запятую — считать
конверсии только по ним), STOPPED_SINCE.
"""
import argparse, json, os, sys, time
from datetime import date, datetime, timedelta, timezone

import requests

TOKEN = os.environ.get('YANDEX_DIRECT_TOKEN', '')
LOGIN = os.environ.get('YANDEX_DIRECT_LOGIN', '')
SB_URL = os.environ.get('SUPABASE_URL', '')
SB_KEY = os.environ.get('SUPABASE_ANON_KEY', '')
STOPPED_SINCE = os.environ.get('STOPPED_SINCE') or '2026-10-01'
GOALS = [g.strip() for g in os.environ.get('DIRECT_GOALS', '').split(',') if g.strip()]
API = 'https://api.direct.yandex.com/json/v5'
ROW = 'bixbit'


# ── Директ ────────────────────────────────────────────────────────────────────
def _h(extra=None):
    h = {'Authorization': f'Bearer {TOKEN}', 'Accept-Language': 'ru', 'Content-Type': 'application/json'}
    if LOGIN:
        h['Client-Login'] = LOGIN
    return {**h, **(extra or {})}


def _explain(code, text):
    t = text[:500]
    if '"error_code":53' in t.replace(' ', '') or 'авторизац' in t.lower():
        return t + '\n  → токен недействителен или истёк: выпустите новый OAuth-токен Директа'
    if '"error_code":58' in t.replace(' ', '') or 'незавершенная регистрация' in t.lower() or 'not completed' in t.lower():
        return t + '\n  → заявка на доступ к API Директа ещё не одобрена (Директ → Инструменты → API)'
    if '"error_code":513' in t.replace(' ', '') or 'client-login' in t.lower():
        return t + '\n  → проверьте YANDEX_DIRECT_LOGIN: для агентского токена нужен логин клиента'
    return t


def call(service, method, params):
    r = requests.post(f'{API}/{service}', headers=_h(), json={'method': method, 'params': params}, timeout=60)
    d = r.json() if r.headers.get('content-type', '').startswith('application/json') else {}
    if r.status_code != 200 or 'error' in d:
        sys.exit(f'Direct API {service}.{method}: HTTP {r.status_code} ' + _explain(r.status_code, json.dumps(d.get('error', r.text), ensure_ascii=False)))
    return d['result']


def report(fields, d1, d2, tag):
    params = {'SelectionCriteria': {'DateFrom': d1, 'DateTo': d2}, 'FieldNames': fields,
              'ReportName': f'bixbit_{tag}_{d1}_{d2}_{int(time.time())}',
              'ReportType': 'CAMPAIGN_PERFORMANCE_REPORT', 'DateRangeType': 'CUSTOM_DATE',
              'Format': 'TSV', 'IncludeVAT': 'NO', 'IncludeDiscount': 'NO'}
    if GOALS and 'Conversions' in fields:
        params['Goals'] = GOALS
        params['AttributionModels'] = ['AUTO']
    hdr = _h({'returnMoneyInMicros': 'false', 'skipReportHeader': 'true', 'skipReportSummary': 'true',
              'processingMode': 'auto'})
    for _ in range(40):
        r = requests.post(f'{API}/reports', headers=hdr, json={'params': params}, timeout=120)
        if r.status_code == 200:
            lines = [l for l in r.text.strip().split('\n') if l.strip()]
            if len(lines) < 2:
                return []
            head = lines[0].split('\t')
            return [dict(zip(head, l.split('\t'))) for l in lines[1:]]
        if r.status_code in (201, 202):
            time.sleep(int(r.headers.get('retryIn', 10)))
            continue
        sys.exit(f'Direct Reports API: HTTP {r.status_code} ' + _explain(r.status_code, r.text))
    sys.exit('Direct Reports API: отчёт не готов за отведённое время')


def num(v):
    try:
        return float(v) if v not in (None, '', '--') else 0.0
    except ValueError:
        return 0.0


def usd_rate(currency):
    """Сколько единиц валюты аккаунта в 1 $."""
    if os.environ.get('DIRECT_USD_RATE'):
        return float(os.environ['DIRECT_USD_RATE']), 'DIRECT_USD_RATE'
    if currency in ('USD', 'YND_FIXED'):
        return 1.0, 'нет конвертации'
    if currency == 'RUB':
        v = requests.get('https://www.cbr-xml-daily.ru/daily_json.js', timeout=30).json()['Valute']['USD']
        return v['Value'] / v['Nominal'], 'ЦБ РФ'
    if currency == 'BYN':
        v = requests.get('https://api.nbrb.by/exrates/rates/USD?parammode=2', timeout=30).json()
        return v['Cur_OfficialRate'] / v['Cur_Scale'], 'НБРБ'
    sys.exit(f'Валюта аккаунта {currency}: задайте курс в DIRECT_USD_RATE (единиц {currency} за 1 $)')


# ── Supabase ──────────────────────────────────────────────────────────────────
def _sb():
    return {'apikey': SB_KEY, 'Authorization': f'Bearer {SB_KEY}', 'Content-Type': 'application/json'}


def sb_load():
    r = requests.get(f'{SB_URL}/rest/v1/dashboard_state?project=eq.{ROW}&select=payload', headers=_sb(), timeout=30)
    r.raise_for_status()
    d = r.json()
    if not d or not d[0].get('payload'):
        sys.exit('Supabase: строка не найдена или пустая — запись отменена')
    return d[0]['payload']


def sb_save(p):
    r = requests.patch(f'{SB_URL}/rest/v1/dashboard_state?project=eq.{ROW}',
                       headers={**_sb(), 'Prefer': 'return=minimal'},
                       json={'payload': p, 'updated_at': datetime.now(timezone.utc).isoformat()}, timeout=30)
    r.raise_for_status()


# ── Квартал ───────────────────────────────────────────────────────────────────
def quarter_bounds(spec, today):
    if spec:
        y, q = spec.upper().split('-Q'); y, q = int(y), int(q)
    else:
        y, q = today.year, (today.month - 1) // 3 + 1
    s = date(y, 3 * (q - 1) + 1, 1)
    e = date(y + (q == 4), (3 * q) % 12 + 1, 1) - timedelta(days=1)
    return s, e


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--quarter')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    missing = [n for n, v in (('YANDEX_DIRECT_TOKEN', TOKEN), ('SUPABASE_URL', SB_URL), ('SUPABASE_ANON_KEY', SB_KEY))
               if not v and not (a.dry_run and n.startswith('SUPABASE'))]
    if missing:
        sys.exit('Не заданы: ' + ', '.join(missing))

    yesterday = datetime.now(timezone(timedelta(hours=3))).date() - timedelta(days=1)
    q_from, q_to = quarter_bounds(a.quarter, yesterday)
    end = min(q_to, yesterday)
    if end < q_from:
        print('Квартал ещё не начался — пропуск'); return
    pkey = f'{q_from.isoformat()}|{q_to.isoformat()}'

    cur = (call('clients', 'get', {'FieldNames': ['Currency', 'Login']}).get('Clients') or [{}])[0]
    currency = cur.get('Currency', 'RUB')
    rate, rate_src = usd_rate(currency)
    print(f'Аккаунт {cur.get("Login", LOGIN or "—")}, валюта {currency}, курс {rate:.4f} за $ ({rate_src})')

    states = {}
    for c in call('campaigns', 'get', {'SelectionCriteria': {}, 'FieldNames': ['Id', 'Name', 'State']}).get('Campaigns', []):
        states[str(c['Id'])] = {'name': c['Name'], 'state': c['State']}

    rows = report(['CampaignId', 'CampaignName', 'Impressions', 'Clicks', 'Cost', 'Conversions'],
                  q_from.isoformat(), end.isoformat(), 'q')
    camps = {}
    for r in rows:
        cid = r.get('CampaignId', '')
        x = camps.setdefault(cid, {'id': f'y_{cid}', 'name': r.get('CampaignName', '').strip(),
                                   'budget': 0.0, 'impressions': 0, 'clicks': 0, 'conversions': 0})
        x['budget'] += num(r.get('Cost')) / rate
        x['impressions'] += int(num(r.get('Impressions')))
        x['clicks'] += int(num(r.get('Clicks')))
        x['conversions'] += int(round(num(r.get('Conversions'))))
    for cid, x in camps.items():
        x['status'] = 'active' if states.get(cid, {}).get('state') == 'ON' else 'paused'

    dropped = added = 0
    if end.isoformat() >= STOPPED_SINCE:
        since = max(q_from.isoformat(), STOPPED_SINCE)
        recent = {r['CampaignId'] for r in report(['CampaignId', 'Impressions'], since, end.isoformat(), 'since')
                  if num(r.get('Impressions')) > 0}
        for cid in list(camps):
            if camps[cid]['status'] != 'active' and cid not in recent:
                del camps[cid]; dropped += 1
        for cid, s in states.items():
            if s['state'] == 'ON' and cid not in camps:
                camps[cid] = {'id': f'y_{cid}', 'name': s['name'], 'budget': 0.0, 'impressions': 0,
                              'clicks': 0, 'conversions': 0, 'status': 'active'}
                added += 1

    cl = sorted(camps.values(), key=lambda c: -c['budget'])
    for c in cl:
        c['budget'] = round(c['budget'], 2)
    tb = round(sum(c['budget'] for c in cl), 2)
    ti = sum(c['impressions'] for c in cl); tc = sum(c['clicks'] for c in cl); tcv = sum(c['conversions'] for c in cl)
    print(f'{pkey} ({q_from}..{end}): {len(cl)} кампаний, ${tb}, показы {ti}, клики {tc}, конверсии {tcv}'
          + (f' · отфильтровано остановленных до {STOPPED_SINCE}: {dropped}, работающих без показов: {added}' if dropped or added else ''))
    if a.dry_run:
        for c in cl[:10]:
            print(f"   {c['name'][:45]:45} {c['status']:6} ${c['budget']:>9} пок {c['impressions']:>7} кл {c['clicks']:>5} конв {c['conversions']}")
        print('dry-run: в Supabase ничего не записано'); return

    payload = sb_load()
    period = payload.setdefault('periods', {}).setdefault(pkey, {})
    old = period.get('yandex') or {}
    if old.get('campaigns') and old.get('source') != 'yandex-direct-api':
        payload.setdefault('backups', {})[f'{pkey}.yandex.{date.today().isoformat()}'] = old
        print('  прежние ручные данные сохранены в backups')
    pf = {str(c.get('name', '')).strip().lower(): c.get('planfix_leads', 0) for c in old.get('campaigns', [])}
    for c in cl:
        c['planfix_leads'] = pf.get(c['name'].lower(), 0)
    period['yandex'] = {
        'budget': tb, 'impressions': ti, 'clicks': tc,
        'ctr': round(tc / ti * 100, 2) if ti else 0, 'cpc': round(tb / tc, 4) if tc else 0,
        'conversions': tcv, 'cpl': round(tb / tcv, 2) if tcv else 0,
        'planfix_leads': sum(c['planfix_leads'] or 0 for c in cl), 'campaigns': cl,
        'currency': currency, 'usd_rate': round(rate, 4), 'rate_source': rate_src,
        'source': 'yandex-direct-api', 'updated': datetime.now(timezone.utc).isoformat()}
    sb_save(payload)
    print(f'✓ Записано в Supabase: periods[{pkey}].yandex')


if __name__ == '__main__':
    main()
