# CLAUDE.md — BiXBiT SEO Automation Context

> Этот файл загружается Claude Code автоматически в каждой сессии. Он задаёт
> контекст бренда, ICP, правила и приоритеты для всех субагентов и команд.
> **Держи его коротким и актуальным.** Подробности выноси в `/docs` или skills.

---

## 1. О компании

**BiXBiT** — индустриальный провайдер инфраструктуры для промышленного майнинга
Bitcoin. Позиционирование: высокотехнологичная "Cyber-Industrial" экосистема,
объединяющая ПО, мониторинг и аппаратное охлаждение.

**Главный сайт:** https://bixbit.io
**Локаль для оптимизации:** https://bixbit.io/en (английская версия — основная для B2B-экспансии)

### Продуктовая экосистема (целевые сущности для SEO)
- **Firmware (прошивки)** — оптимизация для **Antminer** и **Whatsminer**. Это
  флагманский продукт и главный SEO-приоритет.
- **Monitoring (AMS)** — облачный дашборд централизованного мониторинга ферм.
- **Cooling Solutions** — Hydro Cooling, Immersion Cooling, Server Cooling.
- **Power Distribution** — управляемые PDU.

---

## 2. ICP (целевая аудитория)

B2B. Решения принимают:
- Операторы майнинг-ферм (от 100 до 100 000+ ASIC).
- Технические директора / инженеры дата-центров.
- Хостинг-провайдеры майнинга.
- Институциональные майнеры и фонды.

**География приоритета:** США, Канада, Казахстан, Парагвай, ОАЭ, страны
Латинской Америки, СНГ. Английский — основной язык экспансии.

**Болевые точки аудитории (используй в контенте):** эффективность (J/TH),
теплоотвод, простои, надёжность прошивок, безопасность (нет ли бэкдоров /
dev fee), масштабируемость, мониторинг парка устройств.

---

## 3. SEO-стратегия и приоритеты

Приоритет тем (по убыванию коммерческой ценности):
1. **ASIC firmware** — `custom firmware`, `Antminer firmware`, `Whatsminer firmware`,
   `overclocking`, `underclocking`, `efficiency tuning`, `autotuning`.
2. **Immersion / Hydro cooling** для промышленного майнинга.
3. **Mining monitoring software / fleet management**.
4. **PDU / power distribution** для майнинга.

### GEO / AI-видимость — КРИТИЧНО для B2B
Покупатели B2B активно используют ChatGPT / Perplexity / Claude для ресёрча
поставщиков. Оптимизация под цитируемость в AI-ответах = отдельный приоритет
наравне с классическим SEO. См. агента `geo-ai`.

### Главные конкуренты (для gap-анализа)
- **Braiins (Braiins OS+)** — лидер по open-source прошивкам, сильный контент.
- **Vnish** — популярные кастомные прошивки.
- **ePIC firmware** — выигрывает нарратив dev fee в LLM.
- **EMCD**, **Awesome Miner** — реально в топе SERP по firmware (данные 2026-09).
- **LuxOS (Luxor)** — в выдаче US почти не встречается.
- По мониторингу: Awesome Miner, Minerstat, Hiveon.
- По охлаждению: LiquidStack, Engineered Fluids, Immersion-провайдеры.

---

## 4. Бренд-голос и правила контента

- Тон: технический, точный, экспертный, без маркетингового "воды".
- Английский: американский, профессиональный B2B-регистр.
- Всегда подкрепляй заявления цифрами (J/TH, %, °C, $) — это усиливает E-E-A-T.
- **НИКОГДА** не выдумывай технические спеки прошивок, цифры эффективности,
  совместимость моделей или результаты тестов. Помечай как `[VERIFY: ...]` и
  оставляй человеку на проверку. Ложные тех-данные = репутационный риск.
- Не давай инвестиционных советов и не делай заявлений о доходности майнинга.
- Учитывай, что майнинг регулируется по-разному в разных юрисдикциях —
  не давай юридических гарантий.

---

## 5. Технический контекст сайта

- **Фреймворк:** HTML/CSS, Tailwind-совместимая структура.
- **Доступ:** полный доступ к коду (GitHub/CMS).
- **Дизайн-токены:** "Cyber-Industrial Precision". Фон `#151216`, акцент
  magenta `#d1127d`, заголовки шрифт Onest, тело Inter, белый текст.
- При генерации schema/мета учитывай реальную структуру URL (заполни после
  первого `/full-audit` — см. `data/site-structure.md`).

---

## 6. Источники данных (MCP / API)

Статус всех источников: `./scripts/check-connectors.sh`. Актуальные факты и
особенности каждого источника — `docs/agent-knowledge.md` (**читать перед работой**).
- **Google Search Console** — `./scripts/gsc-query.py` (service account; MCP для GSC нет).
- **GA4 Data API** — `./scripts/ga4-query.py` (service account).
- **DataForSEO MCP** — объёмы, бэклинки, AI Optimization. Для SERP через MCP — `noAiMode: true`.
  Массовый съём позиций — `./scripts/serp-rank.py` (команда `/rank-check`).
- **PageSpeed / CrUX** — работают (`check-connectors.sh`).
- **Тех-элементы страниц** — `./scripts/page-snapshot.py` (сырой HTML; WebFetch не видит `<head>`).
- **Индексация / переобход** — `./scripts/index-check.py`, `./scripts/index-submit.py` (Bing, IndexNow).
- **Каннибализация, AIO/FS, ссылки** — `cannibalization.py`, `serp-features.py`, `backlinks-monitor.py`.
- **Автосбор** — `.github/workflows/seo-data.yml` в **приватном** репозитории `dzislandad-del/bixbit-seo` (remote `seo`, push по умолчанию туда). Ежедневно / еженедельно / ежемесячно, бот коммитит снимки в `data/` → перед push всегда `git pull --rebase --autostash`. **Никогда не пушить в `origin`** (`bixbit-dashboard`, публичный).
- **Bing Webmaster** — `./scripts/bing-query.py` (бесплатно; сигнал для ChatGPT search).
- **Яндекс.Вебмастер** — `./scripts/yandex-query.py` (диагностика, запросы, индекс, переобход).
- **Moz** — не используем (бесплатный тир бесполезен), бэклинки из DataForSEO.

Ключи — в `.env` (НЕ коммитить, Claude его не читает — только скрипты). Если источник
недоступен — сообщи об этом и работай с тем, что есть, не выдумывая данные.

**Вне работы:** `bixbitusa.io` — домен партнёров (не наш сайт, не конкурент).

**Россия:** `bixbit.io` заблокирован в РФ решением суда (РКН) — `CONNECT_FAILED` в Яндексе ожидаем. Российская аудитория ходит на `bixbit.tech`: Яндекс-SEO делается на нём. Блокировку не обходить, 301 `bixbit.tech → bixbit.io` не рекомендовать.

---

## 7. Правила работы агентов

1. **Никогда не выдумывай данные.** Нет доступа к API → скажи об этом.
2. **Снапшоть перед изменениями.** Любой аудит сохраняй в `data/` с датой для
   drift-сравнения.
3. **Приоритизируй по impact/effort.** Маркируй проблемы P0/P1/P2/P3.
4. **Создавай артефакты, не болтай.** Отчёты → `reports/`, контент → `content/`.
5. **Перед коммитом мета/schema/контента** — прогоняй SEO-регрессионную проверку.
6. **Тех-факты о прошивках** всегда помечай `[VERIFY]` для человека.

---

## 7a. SEO Workspace (веб-приложение)

`python3 app/server.py` → http://127.0.0.1:8765 (или двойной клик по `SEO Workspace.command`). Обзор-KPI и алерты, документы из `reports/`, `content/`, `docs/`, `data/`, запуск скриптов из белого списка с подтверждением платных, заметки → `content/notes/`. После каждого запуска — отчёт понятным языком в `reports/runs/<дата>-<команда>.md` (`scripts/run_report.py`); из очереди онлайн-хаба команды запускаются через `scripts/run-command.py`.

## 8. Карта субагентов

| Агент | Файл | Зона ответственности |
|---|---|---|
| Technical SEO | `.claude/agents/technical-seo.md` | Crawl, индексация, CWV, schema, sitemap, drift |
| Content & Clusters | `.claude/agents/content-seo.md` | Кластеры, брифы, E-E-A-T, контент-план |
| GEO / AI-видимость | `.claude/agents/geo-ai.md` | Цитируемость в LLM, llms.txt, passage opt |
| International SEO | `.claude/agents/international-seo.md` | hreflang, локализация, мультирынки |
| Off-page / Backlinks | `.claude/agents/offpage-seo.md` | Профиль ссылок, gap, мониторинг упоминаний |
| Local / Maps | `.claude/agents/local-seo.md` | NAP, GBP, дата-центры (Global Presence) |

## 9. Карта команд

| Команда | Файл | Что делает |
|---|---|---|
| `/full-audit` | `.claude/commands/full-audit.md` | Полный аудит: tech + content + backlinks |
| `/page-optimize` | `.claude/commands/page-optimize.md` | On-page оптимизация URL |
| `/new-cluster` | `.claude/commands/new-cluster.md` | Seed → кластер → брифы → перелинковка |
| `/weekly-drift` | `.claude/commands/weekly-drift.md` | Сравнение с baseline, алерты |
| `/competitor-gap` | `.claude/commands/competitor-gap.md` | Gap против конкурента |
| `/geo-check` | `.claude/commands/geo-check.md` | Проверка AI-видимости бренда |
| `/rank-check` | `.claude/commands/rank-check.md` | Съём позиций (SERP + GSC) против baseline |
| `/monthly-report` | `.claude/commands/monthly-report.md` | Ежемесячный отчёт к звонку |
| `/strategy-report` | `.claude/commands/strategy-report.md` | Полугодовой стратегический отчёт |
| `/text-review` | `.claude/commands/text-review.md` | Проверка текста копирайтера |
| `/mockup-review` | `.claude/commands/mockup-review.md` | SEO-рекомендации по макету (Figma) |
| `/blog-plan` | `.claude/commands/blog-plan.md` | Контент-план блога EN/RU |
