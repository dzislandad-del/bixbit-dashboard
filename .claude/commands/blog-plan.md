---
description: Обновить контент-план блога EN/RU — аудит постов, темы (GSC, конкуренты, Google Trends), план по месяцам, брифы на ближайшие статьи.
argument-hint: "[опц. период или тема]"
---

Обнови контент-план блога BiXBiT. Фокус: $ARGUMENTS (пусто = следующие 3 месяца). Действуй по `docs/agent-knowledge.md`,
делегируй `content-seo` (AEO-формат — `geo-ai`).

## Шаги
1. Текущий план — `content/blog-plan.md` (если есть): что выполнено (сверь с `data/crawl-*/pages.json` — опубликованные посты).
2. Аудит блога: свежий `./scripts/crawl.py` (или последний) + GSC по `/blog/post/` (клики/показы/позиции), GA4 органика,
   каннибализация `./scripts/cannibalization.py`. Кандидаты: обновить / объединить / noindex (решение команды).
3. Темы: GSC-запросы с показами без хорошей страницы; конкуренты (`data/serp-features/` — кого цитирует AIO, `/competitor-gap`);
   DataForSEO Google Trends (`/v3/keywords_data/google_trends/explore/live`) и Labs keyword_suggestions (бюджет ≤ $0.5,
   сохранять в `data/dfs-blog-*.json`). Ahrefs — если коннектор авторизован. Объёмы не выдумывать.
4. Каждая тема обязана поддерживать продвигаемую страницу (firmware / AMS / cooling / hardware / PDU) и ссылаться на неё.

## Артефакт
Обновлённый `content/blog-plan.md` (план по месяцам: тема | EN/RU | тип | ключ+объём | поддерживаемая страница | ссылки |
AEO-формат | приоритет) + брифы на 2–4 ближайшие статьи в `content/briefs/blog/<slug>.md`.
Правила: тех-спеки [VERIFY], dev fee — «transparent dev fee» + [VERIFY], без доходности. В чат — список тем месяца.
