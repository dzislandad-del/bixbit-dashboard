#!/usr/bin/env python3
"""hreflang-check.py — валидация hreflang по снимку scripts/page-snapshot.py (сырой HTML).

Проверяет для каждой страницы с hreflang (статус 200):
  - self-reference: есть тег своего языка, указывающий на сам URL (x-default не считается);
  - есть x-default;
  - canonical страницы == её URL (hreflang ставим только на канонические URL);
  - каждый target отдаёт 200 (если он есть в снимке);
  - взаимность: target ссылается обратно (своим языковым тегом, не только x-default);
  - код языка из разрешённого списка (--langs).
Target, которого нет в снимке, печатается как [SKIP] — добавь его в --urls и пересними.

Пример:
  ./scripts/page-snapshot.py --urls <u1>,<u2>,... --out /tmp/hl.json --compare none
  ./scripts/hreflang-check.py /tmp/hl.json
  ./scripts/hreflang-check.py data/hreflang-snapshot-locales-2026-09-28.json --langs en,ru,es
Код возврата: 0 — ошибок нет, 1 — есть ошибки.
"""
import argparse, json, sys


def parse(entries):
    out = {}
    for x in entries or []:
        lang, _, href = x.partition("=")
        out.setdefault(lang, []).append(href)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("snapshot")
    ap.add_argument("--langs", default="en,ru,es", help="разрешённые коды hreflang, кроме x-default")
    args = ap.parse_args()
    allowed = set(args.langs.split(",")) | {"x-default"}
    pages = {p["url"]: p for p in json.load(open(args.snapshot))["pages"]}
    errors = checked = 0

    for url, p in pages.items():
        if p.get("status") != 200 or not p.get("hreflang"):
            continue
        checked += 1
        alt = parse(p["hreflang"])

        def bad(msg):
            nonlocal errors
            errors += 1
            print(f"[ERR] {url}: {msg}")

        for lang, hrefs in alt.items():
            if lang not in allowed:
                bad(f"неожиданный код hreflang '{lang}'")
            if len(hrefs) > 1:
                bad(f"hreflang '{lang}' повторяется {len(hrefs)} раз")
        own = [h for l, hs in alt.items() if l != "x-default" for h in hs]
        if url not in own:
            bad("нет self-reference (тег своего языка на сам URL)")
        if "x-default" not in alt:
            bad("нет x-default")
        if p.get("canonical") != url:
            bad(f"canonical {p.get('canonical')} != URL")
        for lang, hrefs in alt.items():
            for href in hrefs:
                if href == url:
                    continue
                q = pages.get(href)
                if q is None:
                    print(f"[SKIP] {url}: {lang}={href} нет в снимке")
                    continue
                if q.get("status") != 200:
                    bad(f"{lang}={href} отдаёт {q.get('status')}")
                    continue
                if q.get("canonical") != href:
                    bad(f"{lang}={href} не канонический (canonical {q.get('canonical')})")
                if lang != "x-default":
                    back = [h for l, hs in parse(q.get("hreflang")).items() if l != "x-default" for h in hs]
                    if url not in back:
                        bad(f"нет обратной ссылки с {href}")

    print(f"страниц с hreflang: {checked}, ошибок: {errors}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
