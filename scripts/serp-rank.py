#!/usr/bin/env python3
"""serp-rank.py — съём позиций bixbit.io в Google через DataForSEO SERP API.

Берёт список ключей из baseline (data/rank-tracking/baseline-*.json), по одному
live-запросу на ключ (endpoint принимает 1 задачу), ретрай один раз при
40101/40106 или короткой выдаче. Пишет снимок в той же схеме и печатает дельты
к baseline + фактическую стоимость из ответа API.

Логин/пароль DataForSEO читаются из .env (DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD)
и нигде не печатаются.

Примеры:
  ./scripts/serp-rank.py --dry-run
  ./scripts/serp-rank.py --out data/rank-tracking/rank-2026-10-28.json
  ./scripts/serp-rank.py --keywords "antminer firmware,asic firmware" --out /tmp/x.json

Зависимости: python3 (stdlib).
"""
import argparse, base64, datetime as dt, glob, json, os, sys, time
import urllib.error, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_common import CTX, ROOT, load_env  # noqa: E402
ENDPOINT = "https://api.dataforseo.com/v3/serp/google/organic/live/regular"
OWN_DOMAINS = {"bixbit.io", "www.bixbit.io"}  # bixbitusa.io — партнёры, не учитываем
COMPETITORS = {  # метка -> подстрока домена
    "braiins": "braiins.com", "vnish": "vnish", "vni.sh": "vni.sh", "epic": "epicblockchain.io",
    "emcd": "emcd.io", "hiveon": "hiveon.com", "awesomeminer": "awesomeminer.com",
    "minerstat": "minerstat.com", "luxor": "luxor.tech", "liquidstack": "liquidstack.com",
    "engineeredfluids": "engineeredfluids.com", "submer": "submer.com",
}
SHORT_SERP = 60








def latest_baseline():
    files = sorted(glob.glob(os.path.join(ROOT, "data/rank-tracking/baseline-*.json")))
    return files[-1] if files else None


def fetch(auth, kw, location, lang, depth):
    body = json.dumps([{"keyword": kw, "location_name": location, "language_code": lang, "depth": depth}]).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={
        "Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return {"status_code": e.code, "status_message": f"HTTP {e.code}", "items": [], "cost": 0}
    except urllib.error.URLError as e:
        return {"status_code": 0, "status_message": f"network: {e.reason}", "items": [], "cost": 0}
    task = (d.get("tasks") or [{}])[0]
    res = (task.get("result") or [{}])[0] or {}
    return {"status_code": task.get("status_code"), "status_message": task.get("status_message"),
            "items": [i for i in (res.get("items") or []) if i.get("type") == "organic"],
            "se_results_count": res.get("se_results_count"), "cost": task.get("cost") or 0}


def parse(kw, resp):
    items = resp["items"]
    own = sorted([{"rank_group": i["rank_group"], "rank_absolute": i["rank_absolute"], "url": i["url"]}
                  for i in items if i.get("domain") in OWN_DOMAINS], key=lambda x: x["rank_group"])
    comp = {}
    for label, needle in COMPETITORS.items():
        hit = next((i for i in items if needle in (i.get("domain") or "")), None)
        if hit:
            comp[label] = {"rank_group": hit["rank_group"], "domain": hit["domain"]}
    n = len(items)
    status = "ranked" if own else ("not_in_top100" if n >= 80 else "not_found_short_serp")
    flags = []
    if resp["status_code"] == 40106:
        flags.append("partial_serp_40106")
    if resp["status_code"] not in (20000, 40106):
        flags.append(f"api_error_{resp['status_code']}")
    return {"keyword": kw, "status": status,
            "position": own[0]["rank_group"] if own else None,
            "position_absolute": own[0]["rank_absolute"] if own else None,
            "ranking_url": own[0]["url"] if own else None, "all_bixbit_urls": own,
            "top3": [i["domain"] for i in items if i["rank_group"] <= 3],
            "competitors": comp, "organic_items_returned": n,
            "se_results_count": resp.get("se_results_count"),
            "api_status": resp["status_code"], "flags": flags}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=os.path.join(ROOT, ".env"))
    p.add_argument("--baseline", default=latest_baseline(), help="источник ключей и точка сравнения")
    p.add_argument("--keywords", help="через запятую; переопределяет список из baseline")
    p.add_argument("--location", default="United States")
    p.add_argument("--language", default="en")
    p.add_argument("--depth", type=int, default=100)
    p.add_argument("--out", help="путь для JSON снимка")
    p.add_argument("--dry-run", action="store_true", help="только показать, что будет снято")
    a = p.parse_args()

    base = json.load(open(a.baseline)) if a.baseline and os.path.exists(a.baseline) else None
    base_by_kw = {k["keyword"]: k for k in (base or {}).get("keywords", [])}
    kws = [k.strip() for k in a.keywords.split(",")] if a.keywords else list(base_by_kw)
    if not kws:
        sys.exit("нет ключей: укажи --keywords или --baseline")
    print(f"{len(kws)} ключей · {a.location}/{a.language} · depth {a.depth} · baseline: "
          f"{os.path.relpath(a.baseline, ROOT) if base else '—'}")
    if a.dry_run:
        print("\n".join(f"  {k}" for k in kws))
        print(f"Ожидается {len(kws)}–{2 * len(kws)} live-запросов (с ретраями).")
        return
    if not a.out:
        sys.exit("укажи --out (или --dry-run)")

    env = load_env(a.env)
    if not env.get("DATAFORSEO_LOGIN") or not env.get("DATAFORSEO_PASSWORD"):
        sys.exit("DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD не заданы в .env")
    auth = base64.b64encode(f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}".encode()).decode()

    rows, cost, calls = [], 0.0, 0
    for kw in kws:
        attempts, best = 0, None
        while attempts < 2:
            attempts += 1
            resp = fetch(auth, kw, a.location, a.language, a.depth)
            calls += 1
            cost += float(resp["cost"] or 0)
            if best is None or len(resp["items"]) > len(best["items"]):
                best = resp
            if resp["status_code"] == 20000 and len(resp["items"]) >= SHORT_SERP:
                break
            time.sleep(1)
        row = parse(kw, best)
        row["attempts"] = attempts
        b = base_by_kw.get(kw, {})
        for f in ("cluster", "priority", "search_volume_us", "target_url"):
            if f in b:
                row[f] = b[f]
        row["baseline_position"] = b.get("position")
        row["delta"] = (b["position"] - row["position"]) if (b.get("position") and row["position"]) else None
        if row["ranking_url"] and b.get("ranking_url") and row["ranking_url"] != b["ranking_url"]:
            row["flags"].append("ranking_url_changed")
        rows.append(row)
        print(f"  {kw:48} {str(row['position'] or '—'):>4}  (было {b.get('position') or '—'})"
              f"  items={row['organic_items_returned']}{' ' + ','.join(row['flags']) if row['flags'] else ''}")

    today = dt.date.today().isoformat()
    doc = {"meta": {"project": "bixbit.io", "collected_on": today, "source": "DataForSEO " + ENDPOINT.split('/v3')[1],
                    "location_name": a.location, "language_code": a.language, "device": "desktop", "depth": a.depth,
                    "position_metric": "rank_group (organic only)",
                    "domain_match": "bixbit.io / www.bixbit.io only; partner domains (bixbitusa.io) are out of scope",
                    "baseline": os.path.relpath(a.baseline, ROOT) if base else None,
                    "calls": calls, "cost_usd": round(cost, 4), "keywords_total": len(rows)},
           "keywords": rows}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(doc, open(a.out, "w"), indent=2, ensure_ascii=False)
    ranked = [r for r in rows if r["position"]]
    up = sum(1 for r in rows if (r["delta"] or 0) > 0)
    down = sum(1 for r in rows if (r["delta"] or 0) < 0)
    print(f"\nНайден: {len(ranked)}/{len(rows)} · топ-10: {sum(1 for r in ranked if r['position'] <= 10)}"
          f" · ↑{up} ↓{down} · запросов: {calls} · стоимость: ${cost:.4f} -> {os.path.relpath(a.out, ROOT)}")


if __name__ == "__main__":
    main()
