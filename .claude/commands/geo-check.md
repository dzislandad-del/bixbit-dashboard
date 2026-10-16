---
description: Проверка AI-видимости бренда BiXBiT в LLM — цитируют ли в ChatGPT/Perplexity/Claude/AI Overviews по ключевым B2B-запросам, gap против конкурентов.
argument-hint: "[опц. тема/набор промптов]"
---

Проверь AI-видимость бренда **BiXBiT** в LLM. Тема/фокус: $ARGUMENTS (пусто = базовый
набор по firmware и cooling). Действуй по `RUNBOOK.md`/`CLAUDE.md` и `docs/agent-knowledge.md` (актуальные факты и особенности данных). Делегируй `geo-ai`
(skills `seo-geo`, `searchfit-seo:ai-visibility`).

## Метод (только реальные замеры)
1. Сформируй набор B2B-промптов, как их задают ICP (операторы ферм, тех-директора):
   напр. «best custom firmware for Antminer», «immersion cooling providers for mining»,
   «Whatsminer overclocking firmware», «mining fleet monitoring software».
2. Прогони по платформам: ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews — через DataForSEO
   AI Optimization (LLM responses / LLM Mentions / AIO; ~$1.3–2.3 за 20–40 промптов). Сначала переиспользуй
   сохранённые ответы `data/geo-*-2026-09-25/` и сравни с ними; новые — в `data/geo-<тема>-YYYY-MM-DD/`.
3. **Зафиксируй дословно**: промпт → ответ → упомянут ли BiXBiT → какие конкуренты
   (Braiins/Vnish/ePIC/EMCD/LuxOS) → какие источники цитируются.
   **Не выдумывай результаты** — если платформа недоступна, отметь это.

## Анализ
- Где бренд цитируется / отсутствует.
- Какие источники «кормят» AI по нашим темам (куда нужно попасть).
- Passage-дыры на собственных страницах (что мешает цитированию).

## Артефакт
`reports/geo-check-YYYY-MM-DD.md` — матрица (платформа × промпт × упоминание ×
конкуренты × источник) + рекомендации (llms.txt, passage-правки, целевые источники).
Сохрани как baseline для сравнения. В чат — сводка: доля упоминаний, ключевые gap'ы.

## Что проверять каждый раз
- Какую **dev fee** LLM называют для BiXBiT (реальная 2.8% / 2% M2x [VERIFY]) — особенно ошибочную 2.75% (PiTBiT через altcoinlog.com).
- Упоминания `bixbitusa.io` не засчитываются как BiXBiT.
- Сравнение с baseline 2026-09-25: BiXBiT 13/50, ePIC 7/50 (`reports/competitor-gap-summary-2026-09-25.md`).
