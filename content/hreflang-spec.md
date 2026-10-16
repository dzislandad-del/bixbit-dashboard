# hreflang-spec.md: спецификация hreflang для bixbit.io (en / ru / es)

> **Версия:** 2026-09-28. Заменяет `content/seo-fixes/hreflang-all-pages.md` (2026-06-17). Тот файл знал только en/ru,
> содержал 7 legacy-страниц Antminer (сейчас noindex) и предполагал, что ru-URL = en-URL с другим префиксом. Для документации и блога это неверно.
> **Владелец:** international-seo. **Исполнитель:** dev (шаблон `<head>`, sitemap, переключатель языка).
> **Источники (всё по сырому HTML, не WebFetch):**
> `data/hreflang-snapshot-locales-2026-09-28.json` (90 URL: 30 путей × en/ru/es), `data/page-snapshot-2026-09-28.json`,
> живые sitemap (2026-09-28), `data/gsc-pages-all-2026-09-28.json`, `data/site-structure.md`.
> Проверка: `./scripts/hreflang-check.py <snapshot.json>` (новый скрипт, см. §8).

---

## 0. Короткая версия для dev

1. hreflang генерирует **шаблон страницы** из одной таблицы переводов (translation group). Руками по URL его не прописывают.
2. На каждой индексируемой канонической странице выводится полный кластер: **все существующие переводы + сама страница + `x-default` → EN-версия**.
3. Язык попадает в кластер, только если перевод отдаёт 200, у него self-canonical, нет noindex и **контент действительно на этом языке**.
4. Переключатель языка берёт URL из той же таблицы. Сейчас он строится подменой префикса и ведёт на 404 (см. §1, B3).
5. `/es/` добавить в sitemap. hreflang можно дублировать в sitemap через `xhtml:link`, но только из той же таблицы.

---

## 1. Текущее состояние (валидация 2026-09-28)

Снимок 90 URL: 30 ключевых путей × 3 локали. Canonical на всех 200-страницах self-referencing, noindex на них нет.

### 1.1. Какие страницы существуют (факт)

| Группа | Пути | en | ru | es | hreflang сейчас |
|---|---|---|---|---|---|
| **A. Новый шаблон** | `/`, `/firmwares`, `/firmwares/antminer`, `/firmwares/whatsminer-all-series`, `/firmwares/whatsminer-series-m2x`, `-m3x`, `-m5x`, `-m6x`, `/ams`, `/ams/connect`, `/asics-cooling`, `/asics-cooling/immersion-systems`, `/asics-cooling/hydro-systems`, `/documentation`, `/faq`, `/about`, `/contacts` | 200 | 200 | 200 | **нет** |
| **B. Старый шаблон** | `/products`, `/products/container`, `/products/container-hydro`, `/products/container-1k`, `/products/rack`, `/products/rack-hydro`, `/products/cell`, `/products/coolant`, `/calc`, `/blog`, `/sustainability` | 200 | 200 | **404** | `ru` + `x-default` (en) / `en` + `x-default` (ru) |
| **C. Без RU** | `/products/pdu`, `/products/server` | 200 | **404** | 200 | нет |
| **D. Документация** | статьи со **своими slug на каждом языке** (§4) | 200 | 200 | хаб есть, статей нет | нет |
| **E. Блог** | `/{lang}/blog/post/{slug}`, slug на каждом языке свой, общих slug 0 | 106 URL | 733 URL | 404 | нет |

Бриф говорил о hreflang на 4 страницах из 23. После расширения выборки картина такая: hreflang стоит на **22 страницах** (11 en + 11 ru), это весь старый шаблон (группа B). На новом шаблоне (группа A: главная, прошивки, AMS, охлаждение, документация) hreflang нет.

### 1.2. Ошибки

| # | Ошибка | Где | Приоритет |
|---|---|---|---|
| B1 | hreflang отсутствует | весь шаблон A (17 путей × 3 языка = 51 URL), группа C, документация, блог-посты | **P0** |
| B2 | Нет self-reference: EN-страница не объявляет `hreflang="en"` (есть только `x-default` на себя), RU-страница не объявляет `hreflang="ru"` | все 22 страницы группы B (`./scripts/hreflang-check.py`: 22 ошибки) | P1 |
| B3 | **Переключатель языка строится подменой префикса и ведёт на 404.** С `/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1` ссылка ведёт на `/ru/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1`, а там **404**. С RU-страницы `/ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia` ссылка ведёт на `/en/documentation/kody-oshibok-…`, тоже **404**. Эта RU-страница — **№1 по органике на всём сайте** (271 клик за 28 дней) | документация, [VERIFY] блог | **P0** |
| B4 | `/es/` нигде не заявлена: 0 URL в sitemap, нет в hreflang, в сыром HTML EN- и RU-страниц нет ссылок на `/es/` (с ES-страниц на EN/RU ссылки есть). При этом Google её индексирует: 11 URL, 1 030 показов, 32 клика за 28 дней | вся локаль es | **P0** (сначала решение команды, §9 Q1) |
| B5 | Часть `/es/` не переведена: `whatsminer-all-series`, `-m2x`, `-m3x`, `-m5x`, `-m6x` — `lang="es"`, но тело, title и description на английском, H1 пустой. `/es/products/server` — тело на английском. `/es/asics-cooling/immersion-systems` и `/hydro-systems` — смесь языков, description пустой, H1 «Hidroeléctrica» переведён неверно (это «гидроэлектрический», а речь о жидкостном охлаждении). `/es/documentation` — пустой хаб (55 слов). `/es/products/pdu` — пустые title и description | 11 ES-URL | P0 для кластера (такие URL **не включать** в hreflang, пока не переведены) |
| B6 | На RU-страницах есть английские мета: `/ru/firmwares/antminer` — title и description на английском (H1 и тело на русском) | `/ru/firmwares/antminer` | **P0** (RU-разрыв, см. localization-plan §5) |
| B7 | Нет пары между локалями у группы C: RU-версии нет (404) | `/products/pdu`, `/products/server` | P2 (кластер en+es без ru — это нормально) |
| B8 | В `sitemap-category.xml` дважды `/en/sustainability` и дважды `/ru/sustainability` (новая находка, раньше знали только дубль `coolant`) | sitemap | P2 |

**Симптом, что без hreflang выдача путает языки** (GSC page×country, 28 дней; выборка неполная, анонимизированные строки отброшены):
RU-страницы получают **833 показа в США, 912 в Бразилии, 194 в Аргентине, 102 в Венесуэле**. Пользователь из Венесуэлы видит EN (1 245 показов) и ES (410) вперемешку. Это прямой эффект отсутствия кластеров.

---

## 2. Правила

| # | Правило |
|---|---|
| R1 | **Коды языков:** `en`, `ru`, `es`, без региона. На каждый язык у нас одна версия, регионального варианта нет. `es` покрывает всю LatAm и Испанию, `ru` покрывает RU/BY/KZ/UA/СНГ, `en` покрывает всех остальных. Региональные коды (`es-419`, `ru-KZ`) вводить только тогда, когда появится **отдельная** региональная версия страницы. |
| R2 | **`x-default` = EN-версия той же страницы** (не главная). Если EN-версии нет, `x-default` не ставим, пока команда не решит отдельно [VERIFY]. |
| R3 | **Self-reference обязателен:** страница указывает сама на себя своим языком (`/en/ams` → `hreflang="en" href="…/en/ams"`). Одного `x-default` на себя недостаточно, это ошибка B2. |
| R4 | **Взаимность:** если A ссылается на B, B ссылается на A. Весь кластер у всех членов **одинаковый** (одинаковый набор тегов, порядок не важен). |
| R5 | **Только канонические индексируемые URL:** href в hreflang = canonical целевой страницы, абсолютный, `https://bixbit.io`, без слеша в конце (как в canonical сейчас), без query, lowercase-пути как в sitemap. Страница с `noindex` или с canonical на другой URL не входит ни в один кластер (к примеру, 7 legacy `/en/firmwares/asic-*`). |
| R6 | **Готовность перевода:** язык входит в кластер, только если на странице переведены title, description, H1 и основной текст. Страницы из B5 до перевода из кластера **исключаются**. Их судьбу (перевести или временно `noindex,follow`) решает команда (§9 Q2). |
| R7 | **Одна таблица истины:** hreflang в `<head>`, `xhtml:link` в sitemap и переключатель языка генерируются из одного источника (translation group). Расхождения между ними запрещены. |
| R8 | **Разные slug допустимы:** пары документации и блога связываются по ID перевода, не по пути. |
| R9 | **Никаких hreflang на внешние домены:** `bixbitusa.io` (партнёры, вне работы) и `docs.bixbit.io` (§7) в кластеры `bixbit.io` не входят. |
| R10 | **`<html lang>`** совпадает с hreflang страницы (сейчас `en`/`ru`/`es` — совпадает, не ломать). |

---

## 3. Шаблон для dev

### 3.1. Модель данных

Нужна одна сущность «группа переводов». Минимально это поле `translation_group_id` у каждой страницы/поста/статьи (в CMS или в конфиге роутов).

```
translation_group_id | lang | url_path                                              | indexable | translated
fw-antminer          | en   | /en/firmwares/antminer                                | true      | true
fw-antminer          | ru   | /ru/firmwares/antminer                                | true      | true
fw-antminer          | es   | /es/firmwares/antminer                                | true      | true
doc-wm-errors-list   | en   | /en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1 | true | true
doc-wm-errors-list   | ru   | /ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia | true | true
fw-wm-m3x            | es   | /es/firmwares/whatsminer-series-m3x                   | true      | FALSE  <- не в кластере (B5)
```

- `indexable` = статус 200, нет `noindex`, canonical = сам URL. Лучше вычислять из тех же полей, из которых шаблон строит `<meta robots>` и `<link rel=canonical>`, а не хранить руками.
- `translated` — флаг редактора: «перевод готов к индексации». По умолчанию `false` для новых ES-страниц.
- Для шаблона A и групп B/C (одинаковый slug на всех языках) группу можно заполнить автоматически по пути, **но с проверкой существования** (группа C: ru = 404, группа B: es = 404).
- Для документации и блога — только явная связь (поле «translation of» в админке). Автоподмена префикса запрещена (ошибка B3).

### 3.2. Логика в шаблоне `<head>` (псевдокод, язык шаблонизатора не важен)

```text
page    = current page
if not page.indexable:            # noindex / canonical на другой URL / не 200
    emit nothing                  # ни hreflang, ни x-default
    return

members = [m for m in group(page.translation_group_id)
           if m.indexable and m.translated]

if len(members) < 2:              # перевода нет, кластер из одной страницы не нужен
    emit nothing
    return

for m in sort(members, by=lang):  # en, es, ru — порядок любой, но стабильный
    emit <link rel="alternate" hreflang="{m.lang}" href="https://bixbit.io{m.url_path}">

en = find(members, lang="en")
if en:
    emit <link rel="alternate" hreflang="x-default" href="https://bixbit.io{en.url_path}">
```

Условия:
- `page` всегда входит в `members` (иначе нарушен R3). Если у текущей страницы `translated=false`, hreflang на ней не выводится, и остальные члены группы на неё не ссылаются.
- Абсолютные URL строить из того же хелпера, что и canonical (одинаковое правило про слеш в конце).
- В `<head>`, до первого `<script>`, в серверном HTML (не через JS).

### 3.3. Переключатель языка (исправление B3)

```text
for lang in [en, ru, es]:
    target = find(group(page.translation_group_id), lang=lang, translated=true)
    href   = target.url_path if target else "/{lang}"     # нет перевода → главная языка, НЕ 404
```

Сейчас на EN-постах блога переключатель уже ведёт на `/ru` (главная), это приемлемый fallback. На документации fallback сломан: ведёт на несуществующий путь.
Отдельно: на EN- и RU-страницах в сыром HTML нет ссылки на ES. Если `/es/` утверждают как публичную локаль, нужно добавить `ES` в переключатель (§9 Q1).

### 3.4. Итоговый вывод: примеры

**Шаблон A, полный кластер** (`/en/firmwares/antminer`, `/ru/firmwares/antminer` и `/es/firmwares/antminer` получают один и тот же блок):

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer">
<link rel="alternate" hreflang="es" href="https://bixbit.io/es/firmwares/antminer">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer">
```

**Шаблон A, ES не переведена** (`/en/firmwares/whatsminer-series-m3x` и `/ru/…`; на `/es/…-m3x` hreflang не выводится до перевода):

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/whatsminer-series-m3x">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/whatsminer-series-m3x">
```

**Группа B, diff к существующему** (`/en/products`; на `/ru/products` добавить `ru` на себя):

```diff
+<link rel="alternate" hreflang="en" href="https://bixbit.io/en/products">
 <link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/products">
 <link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/products">
```

**Документация, разные slug** (одинаково на обеих страницах):

```html
<link rel="alternate" hreflang="en" href="https://bixbit.io/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1">
<link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia">
<link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1">
```

---

## 4. Таблица кластеров для ключевых страниц

Статусы проверены 2026-09-28 (`data/hreflang-snapshot-locales-2026-09-28.json`). «ES: ждёт перевода» означает, что URL живой, но по R6 в кластер не входит.

### 4.1. Шаблон A (en/ru/es = 200)

| Путь (после `/{lang}`) | en | ru | es | Кластер после деплоя | Примечание |
|---|---|---|---|---|---|
| `` (главная) | ✓ | ✓ | ✓ | en, ru, es + x-default | |
| `/firmwares` | ✓ | ✓ | ✓ | en, ru, es + x-default | на en и es пустой FAQPage (отдельный баг) |
| `/firmwares/antminer` | ✓ | ✓ | ✓ | en, ru, es + x-default | RU: title/description на английском (B6) |
| `/firmwares/whatsminer-all-series` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | ES на английском, H1 пустой |
| `/firmwares/whatsminer-series-m2x` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | то же |
| `/firmwares/whatsminer-series-m3x` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | то же |
| `/firmwares/whatsminer-series-m5x` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | то же |
| `/firmwares/whatsminer-series-m6x` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | то же |
| `/ams` | ✓ | ✓ | ✓ | en, ru, es + x-default | |
| `/ams/connect` | ✓ | ✓ | ✓ | en, ru, es + x-default | [VERIFY: оставляем индексируемой? В июне её предлагали закрыть noindex. Если закрываем, то из кластера убрать на всех трёх] |
| `/asics-cooling` | ✓ | ✓ | ✓ | en, ru, es + x-default | |
| `/asics-cooling/immersion-systems` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | ES: смесь языков |
| `/asics-cooling/hydro-systems` | ✓ | ✓ | ES: ждёт перевода | en, ru + x-default | ES: «Hidroeléctrica» → исправить, description пустой |
| `/documentation` (хаб) | ✓ | ✓ | ES: пустой | en, ru + x-default | `/es/documentation` без статей → [VERIFY] noindex до наполнения |
| `/faq` | ✓ | ✓ | ✓ | en, ru, es + x-default | |
| `/about` | ✓ | ✓ | ✓ | en, ru, es + x-default | |
| `/contacts` | ✓ | ✓ | ✓ | en, ru, es + x-default | |

### 4.2. Группа B (es = 404): кластер en + ru

`/products`, `/products/container`, `/products/container-hydro`, `/products/container-1k`, `/products/rack`, `/products/rack-hydro`, `/products/cell`, `/products/coolant`, `/calc`, `/blog`, `/sustainability`.
Нужно только добавить self-reference (B2). ES не добавлять, пока страница не появится.

### 4.3. Группа C (ru = 404): кластер en + es

| Путь | Кластер | Условие |
|---|---|---|
| `/products/pdu` | en, es + x-default | сначала заполнить ES title/description (сейчас пустые) |
| `/products/server` | en + x-default → **кластер не нужен**, пока ES на английском | ES: ждёт перевода |

### 4.4. Новые страницы архитектуры v2

`/en/firmwares/comparison`, `/en/firmwares/dev-fee`, `/en/documentation/antminer-firmware-install`, `/en/ams/comparison` (слаги не утверждены [VERIFY]). Они создаются с `translation_group_id` сразу. RU/ES-версии входят в кластер только после перевода (R6). Для `dev-fee` при переводе действует правило: «transparent dev fee», ставка `[VERIFY: current rate with the team]`, формулировки «no dev fee» запрещены на всех языках.

### 4.5. Legacy — не включать

7 страниц `/en/firmwares/asic-*` (noindex, follow). Их RU/ES-аналоги не проверялись и в кластеры не входят (R5).

---

## 5. Документация и блог: пары с разными slug

### 5.1. Документация (из `sitemap-documentation.xml` и хабов `/en|ru/documentation`)

Пары подобраны по смыслу. **Подтвердить по ID в CMS** [VERIFY: пары].

| Группа | en | ru |
|---|---|---|
| Коды ошибок (раздел) | `/en/documentation/error-codes-for-whatsminer-asic` | `/ru/documentation/kody-oshibok-dlia-whatsminer-asic` |
| Коды ошибок (список) | `…/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1` | `…/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia` |
| Руководство Whatsminer | `/en/documentation/user-guide-for-whatsminer-asic` | `/ru/documentation/rukovodstvo-polzovatelia-whatsminer-asic` |
| Новое руководство Whatsminer | `/en/documentation/new-user-guide-for-whatsminer-asic` | [VERIFY: RU-аналог? В RU-хабе отдельного «нового» руководства нет, возможно это тот же `rukovodstvo-…`] |
| Доп. БП | `/en/documentation/connecting-an-additional-power-supply-unit` | `/ru/documentation/podkliuchenie-dopolnitelnogo-bloka-pitaniia` |
| Доп. регулируемый БП | `/en/documentation/connecting-an-additional-variable-power-supply-unit` | `/ru/documentation/podkliuchenie-dopolnitelnogo-reguliruemogo-bloka-pitaniia` |
| Подразделы (главы 1–7, приложения) | `…/new-user-guide…/4-firmware-installation-and-update` и т. д. | `…/rukovodstvo-…/4-obnovlenie-proshivki-mainera` и т. д. |

Подразделы не сопоставлены один к одному: в EN у руководства суффиксы `-1`, в RU есть главы вроде `7-3-sbros-nastroek…`, которых в EN-хабе нет. Сопоставление глав делает редактор документации в CMS. Для глав без пары hreflang не выводится.

Существующие RU-главы с трафиком (приоритет связывания): `…/4-obnovlenie-proshivki-mainera` (49 кликов), `…/7-3-sbros-nastroek-mainera-do-zavodskikh-znachenii` (36), `…/3-1-identifikatsiia-mainera-v-seti` (24).

### 5.2. Блог

- В sitemap en 106 / ru 733 поста, общих slug **0**. Один EN-пост со slug-транслитом: `/en/blog/post/kak-maynit-kriptovalyutu-i-pri-etom-vygodno-ispolzovat-teplo-1` [VERIFY: это перевод или ошибочная публикация RU-поста в EN?].
- Большая часть RU-постов переводов не имеет. hreflang для поста выводится **только при явной связи** «translation of» в CMS. Без неё тегов нет.
- Пилот: связать 10–20 пар по GSC-трафику (например, EN `how-does-immersion-cooling-work` ↔ RU-аналог [VERIFY: какой slug]), затем развернуть на весь блог.

---

## 6. Sitemap

### 6.1. Добавить `/es/` (P0 после решения Q1)

Сейчас: en 137, ru 763, **es 0**. Добавить только ES-URL, которые проходят R5 + R6. На 2026-09-28 это:
`/es`, `/es/firmwares`, `/es/firmwares/antminer`, `/es/ams`, `/es/ams/connect` [VERIFY], `/es/asics-cooling`, `/es/faq`, `/es/about`, `/es/contacts`, плюс `/es/products/pdu` после заполнения мета.
Остальные ES-URL добавлять по мере перевода.

### 6.2. Вариант `xhtml:link` (по желанию, дублирует `<head>`)

Google принимает hreflang либо в `<head>`, либо в sitemap. Основной метод — `<head>` (его видно в `page-snapshot.py`). Sitemap-вариант имеет смысл, если его генерирует **тот же** код из той же таблицы (R7). Иначе лучше не делать: два расходящихся источника хуже одного.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://bixbit.io/en/firmwares/antminer</loc>
    <lastmod>2025-10-31</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://bixbit.io/en/firmwares/antminer"/>
    <xhtml:link rel="alternate" hreflang="es" href="https://bixbit.io/es/firmwares/antminer"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://bixbit.io/ru/firmwares/antminer"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://bixbit.io/en/firmwares/antminer"/>
  </url>
  <url>
    <loc>https://bixbit.io/es/firmwares/antminer</loc>
    <!-- тот же набор из 4 xhtml:link -->
  </url>
  <url>
    <loc>https://bixbit.io/ru/firmwares/antminer</loc>
    <!-- тот же набор из 4 xhtml:link -->
  </url>
</urlset>
```

Каждый член кластера — отдельный `<url>` с полным набором ссылок.

### 6.3. Попутно в sitemap (из `data/site-structure.md` + новое)

Эти пункты — зона technical-seo, но они влияют на кластеры:
- добавить сироты: `/en/products/pdu`, `/en/asics-cooling`, `/en/asics-cooling/immersion-systems`, `/en/asics-cooling/hydro-systems`, `/en/documentation` и их RU/ES-версии;
- убрать дубли `coolant` и `sustainability` (B8), исправить `/en/products/ container-1k` (пробел);
- lastmod из реальной даты изменения (сейчас застыл на 2024-09-04).

---

## 7. docs.bixbit.io: риск дублей

**Факт (2026-09-28, сырой HTML):** VitePress v2 alpha на GitHub Pages. Локали: `/` (en-US) и `/ru/`. Canonical нет, hreflang нет, `sitemap.xml` 404, `robots.txt` 404. Title вида «Error codes for Whatsminer ASIC | Documentation», meta description у всех страниц одна: «Documentation». Bing индексирует минимум 2 URL (`/additional_instructions/whatsminer_error_codes.html`, `/installing_and_updating_bixbit_firmware/whatsminer.html`).
В GSC-свойстве `https://bixbit.io/` этот поддомен не виден.

**Дубли (пересечение 8-словных шинглов):**

| docs.bixbit.io | bixbit.io | Совпадение |
|---|---|---|
| `/additional_instructions/whatsminer_error_codes.html` | `/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1` | **94%** |
| `/ru/additional_instructions/whatsminer_error_codes.html` | `/ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia` (№1 по органике) | **93%** |

На docs.bixbit.io есть и **уникальный** контент, которого нет в `/en/documentation`: установка и обновление прошивки для Antminer, разделы интерфейса прошивки Antminer (dashboard, settings, logs…), подключение устройств к AMS. Это ровно та тема, под которую архитектура v2 планирует `/en/documentation/antminer-firmware-install`.

**Риск:** две почти одинаковые страницы кодов ошибок на двух хостах. Google сам выбирает каноническую, и без сигналов может выбрать docs.bixbit.io. Тогда самая трафиковая RU-страница теряет позиции. Плюс каннибализация будущей `antminer-firmware-install`.

**Рекомендация [VERIFY: решение команды и владельца docs]:**
1. Основной хост для индексируемой документации — `bixbit.io/{lang}/documentation`: там трафик, schema и перелинковка с коммерческими страницами.
2. На дублирующих страницах docs.bixbit.io поставить **cross-domain canonical** на соответствующий URL bixbit.io. В VitePress это делается через `transformHead` по карте соответствий. Где соответствия нет — оставить self-canonical.
3. Уникальные Antminer-страницы: либо перенести в `/en|ru/documentation/*` с 301 (предпочтительно, закрывает `antminer-firmware-install` без новой страницы с нуля), либо оставить на docs со self-canonical и перелинковать с `/en/firmwares/antminer`.
4. На docs.bixbit.io включить `sitemap: { hostname: 'https://docs.bixbit.io' }`, отдать `robots.txt`, сделать уникальные description. Внутри docs включить hreflang `en` ↔ `ru` (VitePress i18n `locales`). В кластеры bixbit.io docs **не** включать (R9).
5. Альтернатива, если docs — это «продуктовая» документация прошивки, которая должна жить отдельно: наоборот, `noindex` на её дублях кодов ошибок. Выбор за командой (§9 Q5).

---

## 8. Чек-лист валидации после деплоя

Все проверки по сырому HTML. WebFetch `<head>` не видит и даёт ложное «hreflang нет».

1. **Снять кластеры** (90 URL: 30 путей × 3 языка, плюс документация):
   ```bash
   U=$(python3 -c "
   P='/ /firmwares /firmwares/antminer /firmwares/whatsminer-all-series /firmwares/whatsminer-series-m2x /firmwares/whatsminer-series-m3x /firmwares/whatsminer-series-m5x /firmwares/whatsminer-series-m6x /ams /ams/connect /asics-cooling /asics-cooling/immersion-systems /asics-cooling/hydro-systems /products /products/pdu /products/container /products/container-hydro /products/container-1k /products/rack /products/rack-hydro /products/server /products/cell /products/coolant /documentation /faq /calc /blog /about /contacts /sustainability'.split()
   D=['/en/documentation/error-codes-for-whatsminer-asic/list-of-errors-and-solutions-1','/ru/documentation/kody-oshibok-dlia-whatsminer-asic/spisok-oshibok-i-sposoby-resheniia','/en/documentation/user-guide-for-whatsminer-asic','/ru/documentation/rukovodstvo-polzovatelia-whatsminer-asic']
   print(','.join(['https://bixbit.io/'+l+('' if p=='/' else p) for l in ['en','ru','es'] for p in P]+['https://bixbit.io'+d for d in D]))")
   ./scripts/page-snapshot.py --urls "$U" --out data/page-snapshot-locales-YYYY-MM-DD.json \
       --compare data/hreflang-snapshot-locales-2026-09-28.json
   ```
2. **Проверить правила:** `./scripts/hreflang-check.py data/page-snapshot-locales-YYYY-MM-DD.json --langs en,ru,es`.
   Ожидание: `ошибок: 0`. Скрипт проверяет self-reference, x-default, canonical = URL, 200 у target, canonical у target и взаимность. Базовая линия 2026-09-28: 22 страницы с hreflang, 22 ошибки (все про self-reference).
3. **Покрытие:** в снимке у каждой индексируемой страницы из таблиц §4.1–4.3 непустой `hreflang` с ожидаемым набором языков. ES-страницы с `translated=false` без hreflang, и на них никто не ссылается.
4. **Переключатель языка (B3):** на 4 URL документации из шага 1 ссылки на другую локаль ведут на 200. Проверка: raw HTML → все `href="/ru/…"`/`"/en/…"`/`"/es/…"` → статус. В снимке этого поля нет, проверять вручную или простым python-скриптом на urllib.
5. **Sitemap:** в `sitemap*.xml` появились ES-URL из §6.1, нет дублей, нет URL с пробелом. Если внедрён `xhtml:link`, наборы совпадают с `<head>` на 3–5 выборочных URL.
6. **Регрессия:** в выводе `--compare` не изменились `canonical`, `robots`, `title` у EN-страниц (деплой hreflang не должен их трогать).
7. **GSC через 2–4 недели:** `./scripts/gsc-query.py --days 28 --dimensions page,country --row-limit 25000 --out data/gsc-page-country-YYYY-MM-DD.json`. Ожидаем падение показов RU-страниц в USA/BRA/ARG/VEN (сейчас 833 / 912 / 194 / 102) и рост ES-показов в LatAm. Отчёт GSC «International targeting» устарел; ошибки hreflang смотреть по нашему скрипту.
8. Добавить в `data/tracked-pages.txt` по одному URL каждой локали для 2–3 кластеров (`/ru/firmwares/antminer`, `/es/firmwares/antminer`, RU-страница кодов ошибок), чтобы еженедельный drift ловил пропажу hreflang. Правка tracked-pages — на усмотрение technical-seo.

---

## 9. Вопросы к команде (блокируют часть деплоя)

| # | Вопрос | Что блокирует |
|---|---|---|
| Q1 | `/es/` — это утверждённая публичная локаль или тихий запуск? Кто владелец перевода? | ES в кластерах, ES в sitemap, ES в переключателе |
| Q2 | Непереведённые ES-страницы (B5): переводим в ближайший спринт или временно `noindex,follow`? | 11 ES-URL |
| Q3 | Где хранить `translation_group_id` (CMS-поле, конфиг роутов)? Кто связывает документацию и блог? | документация, блог |
| Q4 | `/ams/connect` индексируем или закрываем? | один кластер |
| Q5 | docs.bixbit.io: основной хост документации или вспомогательный? Кто владелец репозитория VitePress? | §7 |
| Q6 | Нужен ли `x-default` там, где EN-версии нет (сейчас таких страниц нет)? | R2, на будущее |

## 10. [VERIFY]-список

- [VERIFY] Пары документации en↔ru из §5.1 по ID в CMS; RU-аналог `new-user-guide-for-whatsminer-asic`.
- [VERIFY] EN-пост со slug-транслитом `kak-maynit-kriptovalyutu-…-1`.
- [VERIFY] Слаги 4 новых страниц v2 (`comparison`, `dev-fee`, `antminer-firmware-install`, `ams/comparison`).
- [VERIFY] Что `/es/documentation` без статей закрывается noindex или наполняется.
- [VERIFY] Ставка dev fee на всех языках: `[VERIFY: current rate with the team]`, формулировки «no dev fee» / «sin comisión» / «без комиссии» запрещены.
- [VERIFY] Решение по docs.bixbit.io (canonical или noindex, перенос Antminer-разделов).
