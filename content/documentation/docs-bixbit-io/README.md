# docs.bixbit.io: мета-теги и ALT (все 58 страниц)

**Дата:** 2026-09-29 · **Сайт:** VitePress · **Страниц:** 58 (29 EN + 29 RU) · **Вставок изображений:** 212 (122 уникальных скриншота, все просмотрены)

## Файлы
| Файл | Что внутри |
|---|---|
| `vitepress-site-config.md` | Один раз на весь сайт: `titleTemplate ':title \| BiXBiT Docs'`, hreflang EN↔RU, `og:site_name` / `og:url`, `robots.txt` |
| `group-a-meta.md` | Frontmatter (`title`, `description`) для 30 страниц: главная, installing (хаб, Antminer), additional_instructions/*, AMS, `/docs.html` |
| `group-b-meta.md` | Frontmatter для 26 страниц: basic_asic_miner_configuration, functionality_of_the_bixbit_firmware/* (Antminer, Whatsminer) |
| `whatsminer-installing-updating.md` | Frontmatter и ALT для installing/whatsminer (EN + RU) |
| **`alt-all.csv`** | **Все 212 ALT одной таблицей**: page_url, locale, image_src, current_alt, new_alt, len, note |
| `group-a-alt.csv`, `group-b-alt.csv` | То же, по группам |

## Проверено
- Все 58 блоков frontmatter проходят YAML-парсер: значения в кавычках.
- Все 58 title уникальны. С суффиксом ` | BiXBiT Docs` — не длиннее 60 символов. Description — 140–160 символов.
- ALT: 212 из 212 вставок, все ≤ 125 символов. EN-страницы — ALT на английском, RU — на русском.
  - 2 пустых ALT: GIF на `/docs.html` и `/ru/docs.html` отдаёт 404, описывать нечего.
  - 15 строк помечены `[VERIFY]`: скриншот расходится с текстом.

## Как внедрять
1. Конфиг из `vitepress-site-config.md`. Существующий `transformHead` дополнить, а не заменять.
2. В каждый `.md` вставить `title` и `description` из meta-файлов. Блоки `head` с og не нужны: og выводит `transformHead`.
3. ALT: в markdown `![ALT](/images/файл.png)` — значение из `new_alt` для этой страницы и файла.
4. `/docs.html` и `/ru/docs.html` — внутренняя инструкция для редакторов PageCMS. Её стоит закрыть через `robots: noindex, follow` (предложено в `group-a-meta.md`) [VERIFY с командой].

## Ошибки в контенте (найдены по ходу, не исправлены)
Около 65 пунктов: §3 в `group-a-meta.md`, конец `group-b-meta.md`, §4 в `whatsminer-installing-updating.md`. Самые важные:
- **installing/whatsminer:** в шаге 3 промежуточной установки указан файл `bixbit_before_1.8.bin`, а на скриншоте — `Whatsminer-ALL-Models_CustomCleanupBefore1.8_h616.bin` (EN и RU).
- **PSU Control:** на скриншоте есть предупреждение «Returning to air-cooled mode will be impossible», а в тексте его нет.
- **log_export:** в шаге 3 написано «Export Log», а на скриншоте отмечен Mining Control.
- **asic_overclock:** правила (±50, PSU Max на 200 W выше Limit) противоречат примеру M32 и скриншоту (±100 и +100 W).
- **Кнопки и меню в тексте не совпадают с интерфейсом:** Start Upgrade ↔ Start Update, Miner ↔ CGMiner Configuration, Find Device ↔ Locate miner, PSU Firmware ↔ PSU Control.
- **EN-версии короче RU:** в `sd-card_formatting` нет раздела troubleshooting, в `sd-card_flashing` нет примечаний и двух скриншотов.
- **Ссылки:** WhatsPower на EN-странице ведёт на `bixbit.tech/ru`; PSU Control — на старый `bixbit-dev.github.io`; регистрация в AMS — `http://ams.bixbit.io`, без https.
- **Хабы:** 6 страниц без H1 и без текста.
- **Опечатки:** около 30 в RU.
- **Приватные данные:** на скриншотах видны MAC-адреса, серийные номера и имена воркеров — размыть при следующем обновлении.
