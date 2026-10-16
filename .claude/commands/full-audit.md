---
description: Полный SEO-аудит bixbit.io/en — technical + content + backlinks + GEO. Оркестрирует все агенты, заполняет site-structure.md, сохраняет baseline.
argument-hint: "[опц. url или раздел]"
---

Запусти полный SEO-аудит для **https://bixbit.io/en** (область: $ARGUMENTS — если
пусто, весь сайт). Действуй строго по `RUNBOOK.md`, `CLAUDE.md` и `docs/agent-knowledge.md`.

## Порядок
1. **Проверь источники данных:** `./scripts/check-connectors.sh` (GSC, GA4, PageSpeed, CrUX, Moz, Bing)
   + пробный вызов DataForSEO MCP. Выведи таблицу доступности. Где нет доступа — так и напиши, **не выдумывай**.
2. **Краул и структура** → `./scripts/crawl.py --check-external` (полный краул), разбор — `technical-seo`. По итогам **заполни `data/site-structure.md`**
   реальной структурой URL (это источник правды для остальных агентов).
3. **Параллельно делегируй:**
   - `technical-seo` — индексация, CWV (8k-рендеры), schema, sitemap, канониклы.
   - `content-seo` — покрытие тем (firmware → cooling → monitoring → PDU), кластерные дыры, E-E-A-T.
   - `offpage-seo` — профиль бэклинков, токсичность, темп.
   - `geo-ai` — baseline AI-видимости в ChatGPT/Perplexity/Claude + доступ AI-краулеров.
   - `local-seo` — **сначала** проверить наличие физических точек, иначе пометить «неприменимо».
4. **Позиции и спрос:** `/rank-check` (SERP + GSC по отслеживаемым ключам).
5. **Сохрани baseline-снапшот** в `data/` с датой (основа для `/weekly-drift`).
6. **Обнови `docs/agent-knowledge.md`**: что подтвердилось, что изменилось, какие новые особенности данных всплыли.

## Требования к результату
- Всё с приоритетами **P0–P3** (impact/effort).
- Конкретика: URL, код, цифры — не общие советы.
- Тех-факты о прошивках → `[VERIFY]`.
- Никаких выдуманных метрик.

## Артефакт
`reports/full-audit-YYYY-MM-DD.md` — сводный отчёт со ссылками на под-отчёты
каждого агента. В чат — только краткое executive-резюме: топ P0, что недоступно
по данным, что ушло человеку с `[VERIFY]`, следующие шаги.

## Особенности, которые уже ломали аудит
- WebFetch не видит `<head>`/JSON-LD → июньский аудит ложно показал «нет schema/canonical». Мета и schema — только по сырому HTML.
- Сравнивай с `data/baseline-2026-09-16.json` и `reports/full-audit-2026-09-16.md`, а не с июнем.
- `bixbitusa.io` — партнёры, в аудит не включается.
