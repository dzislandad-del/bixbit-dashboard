#!/bin/bash
# daily-local.sh — ежедневная проверка на этом Mac (launchd, 12:00). Лог: ~/Library/Logs/bixbit-seo-daily.log
# С 2026-10-16 основной сбор и Telegram-алерты идут из GitHub (dzislandad-del/bixbit-seo, 07:00 МСК).
# Здесь — только запасная проверка без отправки в Telegram (alerts.py --dry-run пишет в лог, что ушло бы)
# и Яндекс.Вебмастер, пока его токена нет в секретах GitHub.
# Индексацию Google здесь не снимаем: её файл data/index-check/index-<дата>.json пишет бот в GitHub,
# одинаковый локальный файл мешал бы git pull.
export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
cd "$(dirname "$0")/.." || exit 1
D=$(date +%F)
echo "===== $(date '+%F %T') ====="
./scripts/yandex-query.py --report diagnostics --out "data/yandex/yandex-diagnostics-$D.json" || true
./scripts/yandex-query.py --report insearch --days 14 --out "data/yandex/yandex-insearch-$D.json" || true
./scripts/alerts.py --dry-run || true
echo "===== done $(date '+%T') ====="
