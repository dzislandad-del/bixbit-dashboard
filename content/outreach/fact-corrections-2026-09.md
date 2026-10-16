# Fact corrections — 2026-09

> **Для человека.** Список внешних источников, где о BiXBiT написано неверно или устарело, и LLM повторяют эти ошибки. Письма отправляет человек. Агент не ведёт переписку и не редактирует чужие страницы.
> Правильные значения тоже нужно сверить с командой перед отправкой: `[VERIFY: current rate with the team]`.

**Дата:** 2026-09-28 · **Агент:** offpage-seo
**Источники:**
- `reports/sub/competitor-gap-PiTBiT-geo-2026-09-25.md` §3 (F1–F8, часть проверена через WebFetch 2026-09-25);
- `reports/sub/competitor-gap-EMCD-geo-2026-09-25.md` («Attribution risks»);
- `data/geo-pitbit-2026-09-25/p2.json`;
- `data/dfs-backlinks-mention-check-bixbit.io-2026-09-28.json` (статус ссылок).

## Эталон (что правильно)

| Факт | Значение | Статус |
|---|---|---|
| Dev fee, стандарт | 2.8% | `[VERIFY: current rate with the team]` |
| Dev fee, Whatsminer M2x | 2% | `[VERIFY: current rate with the team]` |
| Dev fee, Whatsminer M3x/M5x/M6x | — | `[VERIFY]` |
| Модель лицензирования | Только dev fee, без разовой оплаты (предположение по данным аудита) | `[VERIFY]` |
| Формулировка во внешних текстах | «transparent dev fee». **Никогда** «no dev fee», «zero fee», «lowest dev fee» | правило |
| Поддержка | Antminer и Whatsminer (M2x–M6x) | `[VERIFY: список моделей]` |
| Экосистема | Firmware + AMS (облачный мониторинг) + охлаждение (hydro, immersion) + PDU | подтверждено структурой сайта |
| Канонический URL | `https://bixbit.io/en/firmwares` (позже `/en/firmwares/dev-fee`, слаг `[VERIFY]`) | — |

---

## 1. altcoinlog.com — P0

| | |
|---|---|
| **Где** | `https://altcoinlog.com/prochivka-asic/` («Лучшие прошивки для асиков (ASIC) в 2026 году», RU). Наша ссылка: nofollow → `/ru/firmwares`, с 2023-11, last_seen 2026-08-08 |
| **Что написано** | (а) В разделе Bixbit: «1.8%-2.8% DevFee» (F7). (б) Раздел PITBIT стоит сразу перед разделом Bixbit. Claude (p2, RU) прочитал страницу и приписал BiXBiT условия PiTBiT: «devfee 2,75% … либо единоразовую оплату» и совместимость с «Antminer L9, L7, S21+, T21» (F1). Это проверено через WebFetch 2026-09-25 |
| **Что правильно** | 2.8% стандарт, 2% для M2x `[VERIFY: current rate with the team]`. Разовой лицензии нет `[VERIFY]`. Список моделей берётся с официальной страницы `[VERIFY]` |
| **Что просим** | 1. Обновить dev fee в разделе Bixbit. 2. Чётко отделить разделы PITBIT и Bixbit: отдельные заголовки H2/H3, у каждого своя строка «Комиссия». 3. По желанию редакции добавить ссылку на EN-страницу. Тип ссылки не требуем |
| **Шаблон** | `templates.md` → Template C (RU-версию адаптирует человек) |
| **Проверка после** | Повторить промпт p2 в Claude через 4–6 недель. Ошибка F1 должна исчезнуть |

## 2. saashub.com — P1

| | |
|---|---|
| **Где** | Страница сравнения `saashub.com/compare-minetheasic-vs-bixbit-whatsminer-antminer-firmware` (цитируют Claude e4 и p6) и карточка BiXBiT. В RD bixbit.io: rank 10, 7 bl |
| **Что написано** | «Free to download», «Increases hashrate up to 80 TH/s, cuts power usage by 10–20%» (F6). Claude повторил эту цифру в двух прогонах (e4 и p6) |
| **Что правильно** | Абсолютное «80 TH/s» без модели ничего не значит. Прирост и экономия зависят от модели и режима `[VERIFY: цифры по моделям]`. «Free to download» допустимо, только если рядом написано «transparent dev fee applies» `[VERIFY: current rate with the team]` |
| **Что просим** | Заявить (claim) листинг вендора и заменить описание фактическим текстом без абсолютных цифр `[VERIFY: есть ли у saashub claim-процесс]` |
| **Шаблон** | Template C или правка через кабинет вендора |

## 3. top-mining.ru — P1 (вместе с просьбой о ссылке)

| | |
|---|---|
| **Где** | `/rating/rejting-proshivok-dlya-asikov-top-5/`: Braiins, **Bixbit (#2)**, HiveOn, Vnish, PitBit. DFS не видит ни одной ссылки на bixbit.io |
| **Что написано** | «Bixbit является … производителем систем иммерсионного охлаждения». Прошивка подана как вторичный продукт (F8). Это объясняет, почему Gemini описывает BiXBiT как «immersion first» |
| **Что правильно** | BiXBiT — экосистема: прошивки Antminer и Whatsminer, AMS, охлаждение, PDU. В рейтинге прошивок ведущим должен быть firmware-блок |
| **Что просим** | Поправить описание и поставить ссылку на официальный сайт, как у других участников рейтинга (у PiTBiT там df-ссылки). Предложить карточку `/proshivka/bixbit/` |
| **Шаблон** | Template B (mention → link) + пункт про описание |

## 4. crazy-mining.org — P2

| | |
|---|---|
| **Где** | `https://crazy-mining.org/en/mining/custom-antminer-asic-firmware-to-reduce-power-consumption/`. Gemini цитирует её в RU-ответе p1 |
| **Что написано** | «Даунвольт до -50%» (F3). Это встречается только в этом источнике. Рядом у Gemini «профили для двухфазных иммерсионных ванн», их источник не установлен |
| **Что правильно** | `[VERIFY: реальный диапазон undervolt по моделям; есть ли профили для two-phase immersion]` |
| **Что просим** | Если у команды нет подтверждения −50%, попросить заменить цифру диапазоном с официальной страницы |
| **Шаблон** | Template C |

## 5. d-central.tech — P0 (совмещено с аутричем)

| | |
|---|---|
| **Где** | Страницы сравнения прошивок (`/firmware-comparison/`, `/braiins-os-vs-vnish-vs-luxos-…`). При этом d-central уже ставит 2 df-ссылки на наши Whatsminer-docs (troubleshooting, 2026-06/08) |
| **Что написано** | Claude (r1, RU) со ссылкой на d-central пишет, что Vnish — «единственная крупная сторонняя прошивка, поддерживающая как Antminer, так и Whatsminer». Дословно ли так на странице, не проверено `[VERIFY вручную]`. BiXBiT в сравнениях не назван (WebFetch 2026-09-25) |
| **Что правильно** | BiXBiT поддерживает Whatsminer M2x–M6x и Antminer `[VERIFY: список моделей]` |
| **Что просим** | Добавить BiXBiT в таблицу. Если формулировка «only» там есть, уточнить её. Повод: они уже ссылаются на нашу документацию по Whatsminer |
| **Шаблон** | Template A (данные / фактшит) с абзацем из Template C |

---

## 6. Ошибки без внешнего источника (не аутрич, чинится своим контентом)

Эти утверждения LLM выдают без ссылки или по нашему собственному устаревшему контенту. Письмо здесь не поможет. Лечение — блок фактов на `/en/firmwares`, `llms.txt`, страница dev fee (задачи `geo-ai` / `content-seo`).

| Утверждение LLM | Движок / промпт | Правильно |
|---|---|---|
| «Dev fee: ~2%» | Claude e4 | 2.8% / 2% M2x `[VERIFY: current rate with the team]` |
| «30-day free trial, followed by a 2.8% DevFee» | Gemini e4 | `[VERIFY: есть ли trial]` |
| «up to 40% hashrate / up to 35% energy», «Farm Protect» | Gemini e4 | `[VERIFY]` |
| «Telegram @bixbit_official» | Claude e4 | `[VERIFY: официальный handle]` |
| «Российский разработчик», «разработчик: BiXBiT, Россия» | Gemini r1, Claude p2 | Решение brand/legal: формулировка юрисдикции |
| S21-рекомендация на основе поста про S17 (~2019, «до 60%») | ChatGPT p1 | Нужна своя S21-страница или раздел `[VERIFY модели]` |

## 7. Вне охвата (только к сведению человека)

- **launch.bixbitusa.io** — партнёрский домен, вне работы, не цель аутрича. ChatGPT цитирует его про AMS: «бесплатная», «не взимает платы за разработку», «BiXBiT Prime firmware» (F5). Фраза «не взимает платы за разработку» противоречит факту о dev fee. **Передать человеку для согласования с партнёром.** Агент в это не вмешивается.
