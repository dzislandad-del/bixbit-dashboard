---
description: Полугодовой стратегический SEO-отчёт — итоги 6 месяцев, что сработало, рынки EN/RU/ES, конкуренты, стратегия и план на следующее полугодие.
argument-hint: "[опц. период, напр. 2026-H2]"
---

Подготовь полугодовой стратегический отчёт BiXBiT за: $ARGUMENTS (пусто = последние 6 месяцев).
Действуй по `RUNBOOK.md`/`CLAUDE.md`, `docs/agent-knowledge.md`. Только реальные данные; где динамики нет (данные начались позже) — честно укажи точку отсчёта.

## Источники
- Все `reports/monthly-*.md` за период + baseline: `data/baseline-2026-09-16.json`, `data/rank-tracking/baseline-*.json`, `reports/rank-tracking-baseline-*.md`, `reports/bing-webmaster-baseline-*.md`, `reports/crawl-*.md`.
- GSC за 6 мес. против предыдущих 6 мес. (`./scripts/gsc-query.py --start ... --end ... --dimensions country` / `page`), GA4 каналы за те же периоды, Bing traffic (история с 2025-05).
- Конкуренты: свежий `/competitor-gap` или `./scripts/backlinks-monitor.py` + `data/serp-features/` (кого цитирует AIO).
- GEO: `/geo-check` (или последний), GA4 AI Assistant.

## Структура `reports/strategy-YYYY-HN.md`
1. Executive summary (1 страница): итог полугодия в цифрах, 3 главных вывода, 3 решения для руководства.
2. Что сработало / не сработало — по инициативам (CTR-правки, hreflang, переезд RU, кластеры, блог, линкбилдинг), с эффектом в цифрах.
3. Рынки: EN / RU / ES — доля трафика, тренд, потенциал (спрос DataForSEO), рекомендация по приоритету (с учётом CLAUDE.md §2 vs факт).
4. Конкурентная позиция: Braiins, Vnish, ePIC, EMCD, Awesome Miner — ссылки, AIO-цитирование, позиции по общим ключам.
5. AI-видимость: AIO-цитаты, LLM-упоминания, AI Assistant трафик, ошибки атрибуции (dev fee).
6. Стратегия на следующее полугодие: цели (измеримые), 5–7 инициатив с impact/effort, ресурсы, риски, KPI по кварталам.
7. Решения за командой.
Без обещаний доходности, тех-факты [VERIFY]. В чат — executive summary.
