#!/bin/bash
# daily-local.sh — ежедневная проверка на этом Mac (launchd, 12:00): индексация Google,
# диагностика Яндекса, алерты в Telegram (по понедельникам — сводка). Лог: ~/Library/Logs/bixbit-seo-daily.log
export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
cd "$(dirname "$0")/.." || exit 1
D=$(date +%F)
echo "===== $(date '+%F %T') ====="
./scripts/index-check.py --out "data/index-check/index-$D.json" | tail -3 || true
./scripts/yandex-query.py --report diagnostics --out "data/yandex/yandex-diagnostics-$D.json" || true
./scripts/yandex-query.py --report insearch --days 14 --out "data/yandex/yandex-insearch-$D.json" || true
if [ "$(date +%u)" = "1" ]; then
  ./scripts/alerts.py --digest
else
  ./scripts/alerts.py
fi
echo "===== done $(date '+%T') ====="
