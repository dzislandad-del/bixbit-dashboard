# Бриф: посты о прошивке Whatsminer — обновление и объединение (K1)

**ID плана:** EN-OCT-2 · **Язык:** EN · **Тип:** обновление 2 постов + 1 объединение (301 — решение команды) · **Приоритет:** P0
**URL:**
- `/en/blog/post/installing-the-updated-version-of-whatsminer-firmware` — **оставить** (цель объединения);
- `/en/blog/post/firmware-update-log-for-whatsminer` — **оставить** как журнал изменений;
- `/en/blog/post/announcement-of-whatsminer-firmware` — 301 → `installing-…` [решение команды].
**Не трогать в этой задаче:** `firmware-for-whatsminer-overclocking-for-m2x-m3x-m5x-series`. Это EN-NOV-3, пост цитируется в AIO.
**Пара hreflang:** `/ru/blog/post/ustanovka-obnovlennoy-versii-proshivki-whatsminer`, `/ru/blog/post/zhurnal-obnovleniy-proshivki-dlya-whatsminer` (RU-OCT-2)
**Поддерживает (architecture v2):** `/en/firmwares/whatsminer-all-series` — хаб-сирота, 0 входящих ссылок. Также `-m2x`…`-m6x` и `/en/documentation/user-guide-for-whatsminer-asic`.
**Автор / ревьюер:** [VERIFY: инженер прошивки Whatsminer] · **Дата проверки:** —

## 1. Проблема (данные)
- **Органика:** по «whatsminer firmware *» (GSC 28 дн, все страницы — 1 489 показов) эти посты стоят на поз. 44–76. Они делят показы с `-m2x` (#2 по m20s/m21s firmware) и `-m3x`, а хаб в выдаче не участвует:
  - `installing-…` — 1 946 показов / 15 кликов / поз. 49.9 за 90 дн;
  - `announcement-…` — 1 899 / 1 / поз. 50.8, ошибка JSON-LD;
  - `firmware-update-log-…` — 368 / 3 / поз. 24.5, ошибка JSON-LD.
- **AIO:** по `whatsminer custom firmware` AI Overview цитирует `installing-…` и `firmware-for-whatsminer-overclocking-…` (serp-features 2026-09-28). Поэтому эти URL не удаляем.
- **Интенты разделяем так:**
  - «прошивка Whatsminer» (коммерческий) → хаб и серийные страницы;
  - «как установить или обновить» → документация, а пост — короткая сводка;
  - «что нового в версии» → журнал изменений.

## 2. Ключи
| Ключ | Объём | GSC | Роль |
|---|---|---|---|
| whatsminer firmware update | 10 (US) | 258 показов по сайту, поз. 47.7 | `installing-…` — H1 |
| install whatsminer firmware | n/d | — | `installing-…` |
| bixbit firmware (бренд) | n/d | 18 / поз. 28 на `update-log` | `update-log` |
| **не брать в цель:** whatsminer firmware, whatsminer m20s/m21s/m60 firmware, whatsminer custom firmware | — | цели хаба и серий | только ссылки на хаб и серии |

## 3. Правки по постам

### `installing-the-updated-version-of-whatsminer-firmware`
- **Title:** `How to Update Whatsminer Firmware to the Latest BiXBiT Version` [VERIFY длина].
- **H1:** `How to Install the Updated BiXBiT Firmware on Whatsminer`.
- **Лид (40–60 слов):** что за обновление, для каких контрольных плат и серий [VERIFY: H3/H6/H6os/H616 и 1.5.0.10 из текущего description — проверить актуальность], два способа (WhatsminerTool и SD) → ссылка на полную инструкцию в документации.
- Шаги оставить короткими (5–7 пунктов, нумерованный список). Полные шаги, откат и восстановление — только в `/en/documentation/user-guide-for-whatsminer-asic` (глава про обновление) [VERIFY точный URL главы].
- **Блок «Which Whatsminer series are supported»** — список серий со ссылками на `-m2x`, `-m3x`, `-m5x`, `-m6x` и на хаб [VERIFY список].
- **FAQ (3–4 вопроса):** откат на заводскую прошивку; сохраняются ли настройки пула; что делать при ошибке во время обновления → ссылка на страницу кодов ошибок; dev fee → «transparent dev fee [VERIFY: current rate with the team]», ссылка на `/en/firmwares/dev-fee` после W4.
- Перенести из `announcement-…` всё, что ещё полезно (история релиза, 2–3 абзаца).

### `firmware-update-log-for-whatsminer`
- **Title:** `BiXBiT Whatsminer Firmware Release Notes`.
- **H1:** `Whatsminer Firmware Release Notes`.
- Таблица версий: версия / дата / серии / изменения / известные ограничения [VERIFY]. Новые версии добавлять сверху, `dateModified` обновлять.
- Интро в одну строку со ссылкой на хаб и на пост про установку.
- Исправить JSON-LD (H1 в `content/blog-plan.md`): сейчас из-за ошибки Article не распознаётся.

### `announcement-of-whatsminer-firmware`
- После решения команды: 301 → `installing-…`, убрать из sitemap, внутренние ссылки направить сразу на итоговый URL.
- Если команда против 301: исправить JSON-LD, поставить ссылку на хаб в первом абзаце, заменить title «Globally first!» на фактический [VERIFY: утверждение «first» подтверждено?].

## 4. Внутренние ссылки (для обоих оставшихся постов)
| Куда | Анкор (пример) | Где |
|---|---|---|
| `/en/firmwares/whatsminer-all-series` | BiXBiT firmware for every Whatsminer series | лид |
| `/en/firmwares/whatsminer-series-m3x` | M30S / M31S / M32 firmware | блок серий |
| `-m2x`, `-m5x`, `-m6x` | Whatsminer M20 / M50 / M60 series firmware | блок серий |
| `/en/documentation/user-guide-for-whatsminer-asic` | full Whatsminer update and rollback guide | шаги |
| `/en/ams` | monitor Whatsminer units after the update | FAQ / конец |

Анкор «Whatsminer firmware» дословно не использовать: он закреплён за F3 и F13 в матрице v2.

## 5. [VERIFY]
Поддерживаемые серии и контрольные платы; актуальная версия прошивки; шаги установки и отката; ставка dev fee; утверждение «first».

## 6. Запреты
Не обещать прирост хешрейта без тестов; не писать «no dev fee»; не выдавать себя за официальный сайт MicroBT (в GSC есть запрос «microbt whatsminer official website»).

## 7. Замер
- Через 28 дней: показы и позиции хаба `-all-series` (baseline 75 показов / поз. 26.9, GSC 28 дн).
- Позиции `-m2x`/`-m3x` по whatsminer firmware (не должны упасть).
- `./scripts/serp-features.py --keywords "whatsminer custom firmware,whatsminer firmware update"`: сохранилась ли цитата в AIO.
