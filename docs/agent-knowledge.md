# agent-knowledge.md — актуальные факты и грабли (для всех агентов)

> **Обновлено:** 2026-09-28. Читать перед любой задачей: здесь то, что уже
> проверено на реальных данных, и ошибки, которые уже допускали.
> Обновлять при каждом новом аудите, gap-анализе или съёме позиций.
> Если факт отсюда противоречит свежим данным, верить данным и обновить файл.

---

## 1. Источники правды (читать их, а не июньские версии)

| Тема | Файл | Дата |
|---|---|---|
| Реальная структура URL | `data/site-structure.md` | 2026-09-16 |
| Полный аудит + baseline | `reports/full-audit-2026-09-16.md`, `data/baseline-2026-09-16.json` | 2026-09-16 |
| Конкуренты (DataForSEO) | `reports/competitor-gap-summary-2026-09-25.md` (+ ePIC / EMCD / PiTBiT) | 2026-09-25 |
| Приоритеты кластеров, объёмы US | `reports/cluster-repriorization-2026-09-25.md` | 2026-09-25 |
| Архитектура контента v2 (17 URL) | `reports/content-architecture-2026-09-25.md`, `content/internal-linking.md` | 2026-09-25 |
| Позиции (30 ключей) + GSC | `data/rank-tracking/baseline-2026-09-25.json`, `reports/rank-tracking-baseline-2026-09-25.md` | 2026-09-28 |
| Сохранённые ответы LLM (GEO) | `data/geo-{epic,emcd,pitbit}-2026-09-25/`, `data/dfs-llm-mentions-*` | 2026-09-25 |

Отчёты от 2026-06-xx частично ложные: выводы опирались на WebFetch и самотесты. Использовать их только как историю.

---

## 2. Факты о бизнесе, которые нельзя перепутать

- **Dev fee существует:** 2.8% стандартно, 2% для Whatsminer M2x (подтверждено аудитом 2026-09).
  **Никогда не писать «no dev fee» / «zero fee».** Нейтральная формулировка — «transparent dev fee».
  Текущую ставку каждый раз помечать `[VERIFY: current rate with the team]`.
  - **Сайт сам противоречив:** `/en/faq` — «1.8%–2.8%»; `-m2x` Pricing 2.8% против FAQ 2% (2026-09-28, в dev-task P0-4).
  - Известные места с ошибкой «no dev fee»: `launch.bixbitusa.io` (партнёры, ChatGPT цитирует «AMS не берёт dev fee» — только пометка человеку). Брифы и `content/geo/entity-definition-homepage.md` исправлены.
  - GEO-риск: LLM приписывают BiXBiT комиссию 2.75% от PiTBiT (источник — altcoinlog.com).
- **Партнёрский домен `bixbitusa.io` (и его поддомены) не наш и вне работы.** Не считать
  его позиции нашими, не записывать в конкуренты, не поднимать как каннибализацию, не брать в link-gap.
  Для SERP сопоставлять только `bixbit.io` / `www.bixbit.io`.
- **7 legacy-страниц Antminer** (`/en/firmwares/asic-s19`, `asic-S17-S17Pro`, …) стоят noindex и убраны из sitemap.
  Скорее всего, это намеренная консолидация в `/en/firmwares/antminer` [VERIFY]. Не предлагать их «чинить».
- **Архитектура v2:** оптимизируем существующие URL (`/en/firmwares/*`, `/en/asics-cooling/*`, `/en/ams`)
  и не плодим `/en/antminer-firmware/*`. Новых страниц всего 4: `/en/firmwares/comparison`,
  `/en/firmwares/dev-fee`, `/en/documentation/antminer-firmware-install`, `/en/ams/comparison`.
  Слаги ещё не утверждены командой [VERIFY].

## 3. Что уже известно о сайте (не «открывать» заново)

- Canonical, meta description и JSON-LD (WebSite + Organization) **есть на всех страницах**.
  Реальные баги:
  - `Organization.description` на всём сайте — рекламный текст про охлаждение (P0, entity consistency);
  - на `/en/firmwares` и `/en/documentation` отдаётся **пустой** `FAQPage`;
  - на `/en/faq` FAQ-контент есть, а `FAQPage` нет.
- Sitemap: вне sitemap `/en/products/pdu`, `/en/asics-cooling/*` и хаб `/en/documentation`;
  дубль `coolant`; URL с пробелом `/en/products/ container-1k`; lastmod застыл на 2024-09-04.
- Пустой `FAQPage` (page-snapshot 2026-09-28): `/en/firmwares`, `/en/documentation`, страница кодов ошибок Whatsminer, `/es/firmwares`.
  hreflang: на 22 страницах старого шаблона есть, но без ссылки на себя и без es; на новом шаблоне (главная, прошивки, AMS, охлаждение, документация) его нет.
  Переключатель языка в документации ведёт на 404: slug-и разные. Детали — `content/hreflang-spec.md`, проверка — `scripts/hreflang-check.py`.
  `/es/` переведена частично (Whatsminer, server — на EN; `/es/documentation` пуст). `/ru/firmwares/antminer`: title/description на EN.
  docs.bixbit.io — VitePress, дублирует страницу кодов ошибок на 93–94% (решение в `content/localization-plan.md`).
- **Краул 2026-09-28** (`reports/crawl-2026-09-28.md`): 1 760 HTML (en 299 / ru 1 461).
  - RU-меню ведёт на `/ru/products/server`, а там 404 (1 477 ссылок).
  - Хаб `whatsminer-all-series` — сирота.
  - Пустой FAQPage на 52 страницах документации.
  - Пустой alt у 3 149 из 15 429 изображений.
  - 9 постов с битым JSON-LD.
  - Блог уходит на глубину до 22 из-за линейной пагинации.
  - `/en/products/pdu`: 14 входящих ссылок, 0 из блога.
- **Блог (2026-10-10, `content/blog-plan.md` §0.1):** из октябрьского плана не выполнено ничего (краул 10-10). Новый RU-пост `asic-i-pul-…` ставит в тексте ссылки на `bixbit.tech/ru/*`, а не на `/ru/*`, — вопрос к команде (§6 № 10).
  Сезонность для планирования: `mining container` (Ads US) — пик в октябре–ноябре (1 300 в окт 2025 → 20 в авг 2026); `antminer s21` / `whatsminer` — ноябрь–декабрь и апрель–май; `immersion cooling` — апрель–июнь (`data/dfs-blog-2026-10-10.json`).
- **Индексация (2026-09-28):** 25/25 ключевых URL — PASS, Google-canonical = наш. **Проверка на угрозы не используется:** Web Risk требует оплаты в Google Cloud, а Google блокирует привязку платёжного аккаунта (2026-09-29). Safe Browsing v4 устарел и разрешён только для некоммерческого использования. Замена — уведомления GSC о безопасности. Код в `index-check.py` остался и заработает, если появится `WEB_RISK_API_KEY` с оплатой.
  IndexNow: нужен `INDEXNOW_KEY` в .env + файл `https://bixbit.io/<key>.txt` (разработчик). Bing-квота на переобход — 10 000/день.
- **AIO (2026-09-28, 30 ключей US):** AI Overview есть в 28/30; bixbit цитируется в 5 (все firmware: whatsminer firmware, whatsminer/antminer custom firmware, best antminer custom firmware). Featured Snippet — 0 (вытеснен AIO), PAA — 17, нас в PAA нет. Чаще всего AIO цитирует youtube, reddit, nicehash, mineshop.eu, zeusbtc, braiins.
- **Каннибализация (GSC 28 дн):** 222 same_locale, 53 cross_locale. Крупные: `whatsminer firmware` (-m3x vs хаб), `antminer firmware` (/antminer vs хаб vs noindex legacy asic-T9-plus 15% показов).
- **Ссылки (DataForSEO rank 0–100):** bixbit 39 (891 RD) · braiins 53 (4094) · emcd 64 · luxor 50 · awesomeminer 70 · hiveon 62 · minerstat 74 · ePIC 29 · vnish-firmware.com 12.
  За 31 день: +25 / −9 доменов; среди новых — спам-сеть `link-legion-*.xyz` (spam 75) и др. — возможный негатив, проверить; потерян bitcointalk.org.
- **Документация (2026-09-28):** 106 индексируемых URL (52 EN / 54 RU). Картинки встроены как base64, поэтому страницы весят до 11.7 MB.
  28 живых старых подстраниц `user-guide-for-whatsminer-asic/*` — сироты с трафиком: нужны 301. Мета, H1 и ALT готовы в `content/documentation/`.
  Карта переводов EN↔RU — `content/documentation/translation-map-docs.csv` (slug-и не совпадают).
- **Готовый контент 2026-09-28:**
  - RU-брифы — `content/briefs/ru/` (6);
  - Hardware — `content/clusters/hardware.md` + 6 брифов `hardware-*`;
  - блог — `content/blog-plan.md` + `data/blog-audit-2026-09-28.csv` (865 постов);
  - ES — `content/es/` (ядро, мета, план).
- **docs.bixbit.io (2026-09-29):** 58 страниц (29 EN + 29 RU) на VitePress. Мета и ALT для всех страниц готовы в `content/documentation/docs-bixbit-io/` (`README.md`, `alt-all.csv`). На сайте уже есть свой `transformHead` (og-теги), поэтому og-блоки во frontmatter не нужны. Найдено около 65 ошибок в контенте, в том числе неверное имя файла в инструкции Whatsminer.
- **bixbit.io заблокирован в РФ решением суда (РКН).** Российская аудитория ходит на **bixbit.tech** (95.163.222.17, NS Cloudflare). Обходить блокировку не предлагать.
  - Яндекс.Вебмастер по bixbit.io: `FATAL CONNECT_FAILED` — **ожидаемо**, в алертах подавлено (`YANDEX_EXPECTED` в `scripts/seo_common.py`). ИКС 360; страниц в поиске 1 285 → 0 (06–24.09) → ~1 211; запросы за 28 дней: 2 050 показов, 125 кликов. Из РФ TCP 80/443 к 129.212.254.154 не проходит (`data/yandex/reachability-2026-09-30.md`).
  - **bixbit.tech (2026-09-30):** на всех страницах `noindex, nofollow`; в robots.txt `Sitemap: https://bixbit.io/sitemap.xml`; свой sitemap есть (lastmod 2024-09-04); canonical на себя; в Вебмастере хост добавлен, но **не подтверждён**. Итог: у российской аудитории в Яндексе нет индексируемого сайта BiXBiT. Задача — dev-task P0-0.
  - **Никогда не рекомендовать 301 bixbit.tech → bixbit.io и «склейку» доменов.** Рекомендации competitor-gap 2026-09-25 об этом отменены.
- **Командная страница** (2026-09-30): https://claude.ai/artifact/UHBkEQArj11sA5f7Y5MD1v (`reports/team-hub.html`). Там алерты и KPI (db `metrics/current`, пишет только Claude/редактор), решения команды (`decisions/<id>`), статусы задач (`tasks/<id>`), лента (`news`). Ответы команды читать через ArtifactData перед планированием.
- `llms.txt` не задеплоен (404). Готовый файл — `content/geo/llms.txt` (2026-09-28, 46 URL, все 200); блокеры деплоя — `content/geo/llms-txt-deploy-notes.md`.
- `/en/firmwares/whatsminer-series-m7x` — 200, но noindex и title от M6x.
- Страница firmware весит около 23.8 MB (P0 из competitor-gap). PSI mobile perf плавает 27–46 между прогонами; CrUX (origin, PHONE): LCP p75 = 3.7 с — needs improvement (2026-09-28).
- Вне `site-structure.md` найдены (через Bing): поддомен `docs.bixbit.io` и локаль `/es/` [VERIFY: живые ли, canonical/hreflang].
- **По локалям (GSC, 28 дней):** ru 1 272 клика, en 1 100, es 32. RU-страницы показываются в США, Бразилии и Аргентине: следствие отсутствия hreflang.
- **География кликов Google (28 дней):** Россия 907 (40%), Иран 150, Венесуэла 140, Бразилия 132, Беларусь 105, США 76.
- Блог: около 400 URL, публикуется активно. Много трафика на нерелевантные темы (ERC-20 wallets, PUE, ETC).

## 4. Спрос и позиции (US) — как приоритизировать

- Спрос в US крошечный. У 251 из 308 ключей нет объёма в Google Ads (n/d), остальные в основном на пороге 10/мес.
  **Объём не главный критерий.** Смотреть на CPC, текущую позицию (#4–20 = quick win), GEO-разрыв и показы в GSC.
- Для ключей с объёмом n/d **сначала смотреть показы в GSC** и только потом решать, делать ли страницу.
- **Главная проблема — CTR, а не позиции:** в US 23.7k показов → 76 кликов за 28 дней (CTR 0.32%; в RU 2.3%).
  По видимым запросам почти все клики брендовые.
  По ключам в топ-5 кликов ноль. Title/description на `/en/firmwares`, `-m3x` и `/en/ams` — первый рычаг.
- Сильные зоны: Whatsminer firmware (#2–4), `asic firmware` (GSC 4.7), AMS по `asic monitoring*` (GSC 3–10).
  Разрывы: `mining software` / `mining monitoring software`, бренды конкурентов (`braiins os`, `vnish firmware`).
  По `immersion cooling mining` ранжируется блог, а не коммерческая страница.

## 5. Конкуренты (реальная картина 2026-09)

- **Прошивки:** Braiins (выдача по бренду целиком их), Vnish (множество доменов), ePIC (выигрывает нарратив
  про dev fee и ChatGPT, но органически слабее BiXBiT), LuxOS (в выдаче не встречается), EMCD (LLM цитируют
  их статью-сравнение), Awesome Miner (стабильно в топ-3 по firmware-запросам), Hiveon.
- **Мониторинг:** Awesome Miner, Minerstat, Hiveon, Braiins.
- **Охлаждение:** LiquidStack, Engineered Fluids, Submer.
- PiTBiT почти невидим. Их EN-сайт закрыт noindex. Риск только в перепутанной комиссии (см. §2).

---

## 6. Источники данных и грабли

Статус всех источников: `./scripts/check-connectors.sh` (печатает только статусы, секреты не выводит).
Состояние на 2026-09-28: **все OK** — GSC, GA4, PageSpeed, CrUX (400 был багом скрипта, исправлен), **Bing OK** (verified, данные с 2025-05),
**Moz: сознательно не подключаем** (бесплатный тир ≈ 50 строк/мес — бесполезен; бэклинки берём из DataForSEO).
`.env` Claude читать запрещено: секреты читают только скрипты.

### Скрипты (все читают `.env` сами, общий код — `scripts/seo_common.py`)
| Скрипт | Что | Пример |
|---|---|---|
| `check-connectors.sh` | статус всех источников | `./scripts/check-connectors.sh` |
| `gsc-query.py` | Search Console | `--days 28 --dimensions query,page --country usa --out ...` |
| `ga4-query.py` | GA4 (пресеты `organic-landing`, `channels`, `countries`) | `--preset channels --days 28 --out ...` |
| `bing-query.py` | Bing Webmaster | `--report queries` / `pages` / `traffic` / `crawl` / `links` `--out ...` |
| `serp-rank.py` | позиции DataForSEO (платно, $0.018/ключ) | `--dry-run`, `--out data/rank-tracking/rank-YYYY-MM-DD.json` |
| `crawl.py` | полный краул сайта (замена Screaming Frog): 404, битые ссылки, редиректы, дубли, ALT, сироты, sitemap, перелинковка | `./scripts/crawl.py` → `data/crawl-YYYY-MM-DD/` (issues/*.csv, summary.json) |
| `index-check.py` | индексация ключевых URL (URL Inspection), diff — ежедневно; угрозы (Web Risk) — только при наличии оплаты в GCP | `--out data/index-check/index-YYYY-MM-DD.json` |
| `index-submit.py` | переобход: Bing SubmitUrlBatch (10k/день) + IndexNow (Bing/Yandex/…); Google — только вручную | `--urls ... [--submit]` (без `--submit` — dry run) |
| `cannibalization.py` | «запрос → несколько страниц» по GSC (same_locale / cross_locale / brand) — еженедельно | `--out data/cannibalization/cannibal-YYYY-MM-DD.json` |
| `serp-features.py` | AI Overview (цитируют ли нас) / Featured Snippet / PAA — еженедельно, ~$0.10 за 30 ключей | `--out data/serp-features/serp-features-YYYY-MM-DD.json` |
| `backlinks-monitor.py` | ссылки: summary нас и 8 конкурентов + новые/потерянные домены — ежемесячно, ~$0.27 | `--out data/backlinks/backlinks-YYYY-MM-DD.json` |
| `yandex-query.py` | Яндекс.Вебмастер: hosts, summary, diagnostics, queries, indexing, insearch, sitemaps, links, recrawl (`--submit`, квота 1 020 в день) | `--report diagnostics`, `--report queries --days 28 --out ...` |
| `alerts.py` | алерты в Telegram (основной отправитель — GitHub workflow `seo-data.yml`; ручной запуск — `--always`): доступность, robots, Яндекс, индексация, noindex/canonical, позиции, краул, ссылки; только новые + «решено» | `--dry-run`, `--test`, `--digest`, `--get-chat-id` |
| `sitemap-monitor.py` | sitemap ↔ GSC: новые/удалённые URL (vs прошлый снимок), URL Inspection новых, URL без показов, страницы с показами вне sitemap, ошибки sitemap в GSC Sitemaps API → `data/sitemap/` | `--inspect N`, `--days 28` |
| `site-diff.py` | сравнение двух краулов: новые/пропавшие страницы (пагинация и сбои загрузки отдельно), код ответа, title, description, H1, H2, текст (хэш основного текста без шапки/меню/подвала), ALT, canonical, noindex → `data/site-diff/` | `--old/--new` |
| `quarterly-report.py` | квартальный HTML-отчёт с SVG-графиками: Google (недели, страны, страницы, запросы, позиции отслеживаемых ключей), GA4, Bing, AI Overview, техсостояние vs прошлый квартал → `reports/quarterly-YYYY-Qn.html`, кэш `data/quarterly/` | `--quarter 2026Q3`, `--to-date`, `--refresh` |
| `daily-local.sh` | запасная проверка, ежедневно в 12:00 на Mac (launchd `io.bixbit.seo.daily`): Яндекс diagnostics/insearch → `alerts.py --dry-run` (в Telegram **не шлёт** с 2026-10-16 — алерты идут из GitHub-бота в 07:00 МСК). Лог `~/Library/Logs/bixbit-seo-daily.log` | `launchctl kickstart gui/$(id -u)/io.bixbit.seo.daily` |
| `hreflang-check.py` | валидация hreflang по снимку page-snapshot | `data/<снимок>.json --langs en,ru,es` |
| `page-snapshot.py` | (с 2026-10-16 также H2/H3, ALT, основной текст по абзацам; diff показывает добавленные/удалённые абзацы)  тех-элементы страниц по сырому HTML + diff | `--out data/page-snapshot-YYYY-MM-DD.json` (список — `data/tracked-pages.txt`) |

**Автоматизация:** `.github/workflows/seo-data.yml` — ежедневно index-check; еженедельно GSC/GA4/Bing/page-snapshot/
cannibalization/serp-features; ежемесячно crawl, serp-rank, backlinks-monitor; коммитит снимки в `data/`, при критичном drift открывает issue. Работает после push и добавления
секретов в GitHub (см. шапку workflow). Анализ — вручную (`/weekly-drift`, `/rank-check`).

### GA4
- Органика — **2.7% сессий** (2 877 из 108k за 28 дн). Основной трафик — реклама: Cross-network (PMax) 57.6k, Paid Search 31k.
- `keyEvents` в Cross-network ≈ числу сессий (56k/57k) — похоже, key event срабатывает почти на каждый визит [VERIFY настройку].
  Для SEO-конверсий не доверять `keyEvents` без проверки, какие события отмечены ключевыми.
- Есть канал **AI Assistant** (68 сессий/28 дн) — прямая GEO-метрика, отслеживать в динамике.
- Топ органических посадочных: `/en`, коды ошибок Whatsminer (en+ru), `/ru`, `/en/firmwares`, `/en/ams`, `-m3x`.

### Bing Webmaster Tools
- Бесплатный. `./scripts/bing-query.py --report sites|queries|pages|traffic|crawl|links --out data/bing-....json`.
- Ценность: запросы/индексация в Bing — косвенный сигнал видимости в ChatGPT search (опирается на индекс Bing),
  плюс второй источник бэклинков. Ключ — один на пользователя (Settings → API Access).
- В API нет разбивки по странам. `GetLinkCounts` пока пуст (2026-09-28) — ссылки из DataForSEO.
- Срез 2026-09-28 (`reports/bing-webmaster-baseline-2026-09-28.md`): ~6% кликов от Google; показы −51% год к году;
  индекс 4188 → 3108 (март → сентябрь); небрендовой видимости почти нет.

### Google Search Console
- MCP-инструмента для GSC **нет**. Использовать `scripts/gsc-query.py`:
  `./scripts/gsc-query.py --days 28 --dimensions query,page --country usa --out data/gsc-....json`
- **Разрез `query` не включает анонимизированные запросы:** итог кликов и показов по нему занижен
  (US: 29 кликов по запросам против 76 по стране). Итоги считать в разрезе `country`/`page` или без измерений.
- Окно заканчивается на «сегодня−3» (лаг GSC). Позиция в GSC — среднее по показам, её нельзя напрямую сравнивать со снимком SERP.
- На этом Mac у Python с python.org нет CA-сертификатов: скрипты берут certifi или `/etc/ssl/cert.pem`.
  **Не отключать проверку TLS.**

### DataForSEO
- **Съём позиций — через `scripts/serp-rank.py`**, а не через MCP. MCP тратит около 10k токенов на одну выдачу.
- Если используешь MCP для SERP, **всегда `noAiMode: true`.** AI-optimized режим обрезает список
  (у `bitmain firmware` 17 результатов вместо 85): «не найден» в этом режиме недостоверен.
- Live-эндпоинты принимают **1 задачу на запрос**, лишние молча отбрасываются.
- 40101 / 40106 (ошибка SE / partial) — ретрай один раз. Короткие выдачи (<60 результатов) у Google бывают на самом деле.
  Для них «не найден» ≠ «не ранжируется», проверять по GSC.
- Выдача волатильна между вызовами: в отчётах помечать `volatile`.
- Labs не поддерживает Russia / Belarus (40501). Для СНГ брать Kazakhstan (2398, ru).
- Labs `regex`-фильтр не работает (40501), вместо него — цепочка `like`.
- `backlinks/domain_intersection` игнорирует exclude-target: разрыв считать локально, как разность множеств referring_domains.
- AI Optimization (ответы ChatGPT / Perplexity / Claude / Gemini, LLM Mentions, AIO) работает и принимает промпты на русском.
  Стоимость около $1.3–2.3 за 20–40 промптов. Сначала переиспользовать сохранённые ответы (§1).
- Большие ответы разбирать python-скриптом из tool-results, не читать их в контекст.

### Чтение страниц сайта
- **WebFetch не видит `<head>` и `<script>`:** он даёт ложные «нет canonical / schema / hreflang».
  Для мета и JSON-LD — `./scripts/page-snapshot.py --urls <url> --out ... --compare none` (сырой HTML, head/JSON-LD).
  `curl` в проекте запрещён настройками.
- Перед тем как предлагать schema, **сверяться с тем, что уже стоит на живой странице**,
  и предлагать diff к существующему, а не делать «с нуля».
