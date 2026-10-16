---
description: Drift-мониторинг — сравнить текущее состояние SEO-критичных элементов с сохранённым baseline, выдать регрессии с приоритетом и алертами.
argument-hint: "[опц. раздел/url]"
---

Сравни текущее состояние с baseline и найди регрессии. Область: $ARGUMENTS (пусто = весь
отслеживаемый набор). Действуй по `RUNBOOK.md`/`CLAUDE.md` и `docs/agent-knowledge.md` (актуальные факты и особенности данных). Делегируй `technical-seo`
(skill `seo-drift`).

## Предусловие
Нужен сохранённый baseline в `data/`. **Если baseline нет** — сообщи об этом и
предложи сначала `/full-audit` (он создаёт baseline). Не выдумывай «прошлые» значения.

## Сбор
`./scripts/page-snapshot.py --out data/page-snapshot-YYYY-MM-DD.json` — сам сравнит с последним снимком
(title, description, robots, canonical, hreflang, H1, JSON-LD, вес HTML). Если снимок уже сделал workflow
`seo-data.yml` — используй его. Список URL — `data/tracked-pages.txt`.
Трафик: `./scripts/gsc-query.py --dimensions country` и `--dimensions page`, `./scripts/ga4-query.py --preset channels`
(органика, AI Assistant), `./scripts/bing-query.py --report crawl` (индекс Bing) — против прошлых выгрузок в `data/`.

Раз в месяц (или после деплоя) — `./scripts/crawl.py`: сравни `data/crawl-*/summary.json` с прошлым краулом
(рост error_pages, broken_links, links_to_redirects, noindex — алерт).

## Что сравнивать с baseline
- Индексация/покрытие (GSC), статус-коды, канониклы, robots, sitemap.
- Title/description/H1 ключевых страниц.
- JSON-LD schema (наличие/валидность).
- Core Web Vitals (PageSpeed/CrUX).
- hreflang-теги (если есть локали).
- **Позиции и CTR:** последний `data/rank-tracking/rank-*.json` против `data/rank-tracking/baseline-*.json`
  (свежий съём — `/rank-check`) + GSC за 28 дней (`./scripts/gsc-query.py`) против предыдущей выгрузки `data/gsc-*`.
  Флаги `volatile` / `not_found_short_serp` не считаются регрессией без подтверждения GSC.
Все значения — из реальных источников. Недоступно → пометь, не подставляй цифры.

## Классификация
Каждое изменение: **severity P0/P1/P2/P3** + что было → что стало → вероятная причина → фикс.
P0/P1 — выноси как алерт наверх отчёта.

## Артефакт
`reports/drift-YYYY-MM-DD.md` — таблица регрессий с severity. Обнови baseline в
`data/` после разбора (по решению — что считать новой нормой). В чат — только
алерты P0/P1 и сводку «N изменений, M регрессий».

## Особенности
- Baseline тех-элементов — `data/baseline-2026-09-16.json` (не июньский: там ложные «нет schema»).
- Мета/schema сравнивай по сырому HTML, не WebFetch.
- Источники: `./scripts/check-connectors.sh` (CrUX работает с 2026-09-28).
