# llms.txt: заметки к деплою (2026-09-28)

**Файл:** `content/geo/llms.txt` → деплоить в корень: `https://bixbit.io/llms.txt`
(сейчас 404, проверено 2026-09-28; `/llms-full.txt` тоже 404).
**Формат:** спецификация llmstxt.org: H1 → blockquote (сущность) → блок ключевых фактов → H2-секции со списками `- [Title](url): описание`, секция `## Optional` для второстепенного.

## Перед деплоем (блокеры)

1. Закрыть 3 метки `[VERIFY]` в файле (см. ниже). После подтверждения метку удалить, текст оставить.
   Если ставку dev fee не подтвердили к деплою, заменить первую строку Key facts на:
   `BiXBiT firmware is free to download and has a transparent dev fee that is automatically deducted during operation; current rates per series are listed on https://bixbit.io/en/firmwares.`
   «No dev fee» / «0%» не писать ни в каком варианте.
2. Отдавать с `200`, `Content-Type: text/plain; charset=utf-8` (или `text/markdown`), без редиректа на `/en/...`.
3. В `robots.txt` путь `/llms.txt` не закрыт. Правки robots не нужны: AI-краулеры разрешены через `User-Agent: *`.
4. После деплоя: `./scripts/page-snapshot.py --urls https://bixbit.io/llms.txt --out /tmp/llms-live.json --compare none` → 200.

## [VERIFY] для команды

| # | Где | Что подтвердить | Что видно на сайте 2026-09-28 |
|---|---|---|---|
| V1 | llms.txt, Key facts | Текущая ставка dev fee | `/en/firmwares`: 2.8% на всех сериях, M2x 2%. **Сайт противоречит сам себе:** `/en/faq` пишет «usually 1.8%–2.8%»; `-m2x` в блоке Pricing показывает «2.8% DevFee», а FAQ на той же странице — 2% для M2x. LLM могут подхватить 1.8% или 2.8% для M2x. Исправить FAQ и блок Pricing на `-m2x` (задача для content/tech) |
| V2 | llms.txt, Key facts | Цены AMS: бесплатно с прошивкой BiXBiT; AMS HUB для заводской и сторонней прошивки | `/en/ams` FAQ: бесплатно с прошивкой BiXBiT; HUB «currently free». Временное условие в llms.txt не выносили |
| V3 | llms.txt, Company | Год начала работы (2016) | meta `/en/about`: «since 2016» |
| V4 | llms.txt, Key facts | Упоминание PiTBiT (дисамбигуация против ошибочной атрибуции 2.75%) | Решение команды. Строку можно удалить без ущерба для остального файла. Чужую ставку в файл специально не добавляли |
| V5 | не в файле | Модели и J/TH | В llms.txt нет ни списка моделей, ни цифр эффективности: источником правды названа `/en/firmwares`. Маркетинговые цифры со страниц (80/130 TH/s, −10–20% энергии, +40% hashrate) не переносили: без проверки LLM будут повторять их как факт |

## Что изменилось против старого черновика

| Было | Стало | Почему |
|---|---|---|
| `/en/monitoring` | `/en/ams` | старый URL 404 |
| `/en/cooling/immersion`, `/en/cooling/hydro`, `/en/cooling/server` | `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`, `/en/products/server` | старые URL 404 |
| `/en/pdu` | `/en/products/pdu` | старый URL 404 |
| Whatsminer: только `-m3x`, `-m6x` | хаб `-all-series` + m2x/m3x/m5x/m6x | хаб по архитектуре v2 |
| «Dev fee: [VERIFY — confirm 0%…]» | transparent dev fee 2.8% / 2% M2x + `[VERIFY]` | dev fee есть; «0%» подталкивал к ложному утверждению |
| Списки моделей S19/S21/M30S… с [VERIFY] | ссылка на `/en/firmwares` как источник правды | на живой странице уже шире (T21, T19, L9, L7, M7x) |
| «No backdoors», PUE, «one of few providers covering both» | удалено | неподтверждённые claims |
| Секция конкурентов (Braiins, Vnish, LuxOS…) | удалена | llms.txt описывает нас; конкуренты в нём размывают сущность |
| Не было | docs.bixbit.io (7 страниц), документация, продукты охлаждения, `/ru`, `/es`, блог | живые 200-страницы |
| «Deployment note» внутри файла | вынесено сюда | служебный текст не должен попадать в LLM |

## Проверенные URL (page-snapshot, сырой HTML, 2026-09-28)

**В llms.txt 46 URL: все 200, без noindex и редиректов** (`/tmp/llms-check-final.json`).
- bixbit.io (39): firmware (7), AMS (1), cooling и продукты (12), PDU (1), документация и FAQ (4 + 3 в Optional), About/Contacts (2), блог (3), calc, sustainability, `/ru`, `/ru/firmwares`, `/es`, `/es/firmwares`. Все с self-canonical.
- docs.bixbit.io (7): установка на Antminer и Whatsminer, откат на заводскую прошивку, оверклок, подготовка к иммерсии, функции прошивки, подключение к AMS. **Canonical на docs.bixbit.io нет** (задача для `technical-seo`).

**Проверено и НЕ включено:**

| URL | Статус | Почему нет |
|---|---|---|
| `/en/firmwares/whatsminer-series-m7x` | 200, **noindex** | закрыта от индексации; в title копипаст «…M6x software». Добавить после снятия noindex и правки title |
| `/en/ams/connect` | 200 | страница регистрации, не контент |
| `/en/firmwares/asic-*` (7 legacy) | 200, noindex | намеренная консолидация в `/en/firmwares/antminer` [VERIFY] |
| `/en/documentation/error-codes-for-whatsminer-asic` | 200 | родительская страница; вместо неё взят список решений (топ-посадочная) |
| docs.bixbit.io `/additional_instructions/whatsminer_error_codes.html` | 200 | дубль кодов ошибок с bixbit.io; оставили версию на основном домене |
| `/en/monitoring`, `/en/cooling/*`, `/en/pdu` | 404 | URL из старого черновика |
| `/en/firmwares/comparison`, `/en/firmwares/dev-fee`, `/en/documentation/antminer-firmware-install`, `/en/ams/comparison` | 404 | ещё не опубликованы (архитектура v2) |
| `bixbitusa.io` | — | партнёрский домен, вне работы |

## Добавить после публикации (архитектура v2)

Вставлять после проверки, что страница отдаёт 200 и индексируется:
- `## Firmware`: `- [Firmware dev fee and security](https://bixbit.io/en/firmwares/dev-fee): How the BiXBiT dev fee is charged, rates per series and firmware security.` Затем в Key facts заменить ссылку на `/en/firmwares` ссылкой на эту страницу как на каноническую по dev fee.
- `## Firmware`: `- [ASIC firmware comparison](https://bixbit.io/en/firmwares/comparison): Comparison of BiXBiT firmware with other Antminer and Whatsminer firmware options.`
- `## Documentation`: `/en/documentation/antminer-firmware-install`. **Внимание:** на `docs.bixbit.io/installing_and_updating_bixbit_firmware/antminer.html` такая инструкция уже есть. Перед созданием новой страницы решить, какой URL канонический, чтобы не завести дубль (вопрос к `content-seo` / `technical-seo`).
- `## Monitoring (AMS)`: `- [Mining monitoring software comparison](https://bixbit.io/en/ams/comparison): How to choose ASIC monitoring software; AMS compared with alternatives.`
- `/en/firmwares/whatsminer-series-m7x`: после снятия noindex.

## Следующие шаги (вне этой задачи)

- `llms-full.txt` пока не нужен. Делать после публикации `/en/firmwares/dev-fee` и появления проверенного текста для passage-извлечения.
- Та же фраза о сущности (blockquote) должна совпадать с `Organization.description` в JSON-LD (P0 с `technical-seo`) и с hero на `/en`: см. `content/geo/entity-definition-homepage.md`.
- В следующем замере GEO отслеживать, какую ставку dev fee LLM называют для BiXBiT (2.8% / 2% / 1.8% из FAQ / 2.75% от PiTBiT).
