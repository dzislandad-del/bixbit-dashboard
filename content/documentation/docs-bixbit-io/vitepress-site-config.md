# docs.bixbit.io: общие SEO-настройки VitePress (один раз на весь сайт)

**Дата:** 2026-09-29. Применяется ко всем 58 страницам: 29 EN и 29 RU.
Мета и ALT по страницам лежат в `group-a-meta.md` / `group-b-meta.md`, `group-a-alt.csv` / `group-b-alt.csv` и `whatsminer-installing-updating.md`.

## Что сейчас
- `<title>` = «{название} | Documentation» / «| Документация»: бренда нет, суффикс общий.
- `description` = «Documentation» / «Документация» на **всех** 58 страницах.
- hreflang между EN и RU нет, хотя у каждой EN-страницы есть RU-версия с тем же slug (`/x.html` ↔ `/ru/x.html`).
- `robots.txt` отдаёт 404; `sitemap.xml` есть.
- `og:title` — только название страницы, `og:description` нет, `og:site_name` нет.

## 1. `.vitepress/config.(ts|js)`: слить с текущим

> **Важно:** на сайте уже есть свой `transformHead`: его код опубликован на `/docs.html`. Он выводит `og:title` из `title` и `og:description` из `description` страницы [VERIFY по репозиторию].
> Поэтому:
> - **не заменяйте** существующую функцию, а **добавьте** в её `return` строки ниже: hreflang, `og:site_name`, `og:url`, `og:locale`;
> - во frontmatter страниц **не нужны** блоки `head` с og-тегами, иначе они задублируются. Достаточно `title` и `description`. В `group-b-meta.md` и `whatsminer-installing-updating.md` блоки `head:` с og можно пропустить.

```ts
import { defineConfig } from 'vitepress'

const SITE = 'https://docs.bixbit.io'

export default defineConfig({
  // суффикс для всех страниц; сам title страницы задаётся во frontmatter (≤ 46 символов)
  titleTemplate: ':title | BiXBiT Docs',

  // запасное описание — если у страницы нет своего description во frontmatter
  locales: {
    root: {
      label: 'English', lang: 'en-US',
      titleTemplate: ':title | BiXBiT Docs',
      description: 'BiXBiT firmware documentation for Antminer and Whatsminer ASIC miners: installation, updates, settings, AMS monitoring and troubleshooting.'
    },
    ru: {
      label: 'Русский', lang: 'ru-RU', link: '/ru/',
      titleTemplate: ':title | BiXBiT Docs',
      description: 'Документация прошивки BiXBiT для ASIC-майнеров Antminer и Whatsminer: установка, обновление, настройки, мониторинг AMS и решение проблем.'
    }
  },

  sitemap: { hostname: SITE },

  // hreflang EN↔RU + og:site_name + og:url для каждой страницы
  transformHead({ pageData }) {
    const rel = pageData.relativePath                    // 'x.md' или 'ru/x.md'
    const isRu = rel.startsWith('ru/')
    const base = (isRu ? rel.slice(3) : rel)
      .replace(/(^|\/)index\.md$/, '$1')                 // index.md -> каталог
      .replace(/\.md$/, '.html')
    const en = `${SITE}/${base}`
    const ru = `${SITE}/ru/${base}`
    return [
      ['link', { rel: 'alternate', hreflang: 'en', href: en }],
      ['link', { rel: 'alternate', hreflang: 'ru', href: ru }],
      ['link', { rel: 'alternate', hreflang: 'x-default', href: en }],
      ['meta', { property: 'og:site_name', content: 'BiXBiT Docs' }],
      ['meta', { property: 'og:url', content: isRu ? ru : en }],
      ['meta', { property: 'og:locale', content: isRu ? 'ru_RU' : 'en_US' }]
    ]
  }
})
```

**Проверить:**
- Если у сайта включён `cleanUrls: true`, убрать `.replace(/\.md$/, '.html')` и ставить URL без `.html`. Сейчас URL с `.html`, так что код рассчитан на это.
- Все 29 пар EN/RU сейчас существуют. Если появится страница только на одном языке, для неё hreflang выводить не нужно: добавить проверку по списку страниц или по наличию файла.
- В `data/docs-bixbit-io-inventory-2026-09-29/inventory.json` лежит полный список URL: по нему можно проверить, что для каждого `/x.html` есть `/ru/x.html`.

## 2. `public/robots.txt` (новый файл, попадёт в корень сайта)

```
User-agent: *
Allow: /

Sitemap: https://docs.bixbit.io/sitemap.xml
```

## 3. Пер-страничная мета
В каждом `.md` добавить frontmatter из `group-a-meta.md`, `group-b-meta.md` и `whatsminer-installing-updating.md`: `title` ≤ 46, `description` 140–160, `og:title` и `og:description`. `og:description` можно не дублировать: при необходимости его можно генерировать из `description` в том же `transformHead` (`pageData.frontmatter.description`).

## 4. ALT
В markdown VitePress ALT — это текст в `![ALT](/images/file.png)`. Готовые строки лежат в CSV (`new_alt`) по каждой странице и картинке. Одна картинка, стоящая на разных страницах или шагах, получает ALT по месту: это нормально, в CSV это отмечено как `reused`.

## 5. Связь с bixbit.io
Большая часть этих инструкций продублирована в `bixbit.io/{en,ru}/documentation/*`: страница кодов ошибок Whatsminer совпадает на 93–94%. Какой хост основной — решает команда (`content/localization-plan.md`, вопрос Q5). Мета и ALT нужны при любом решении. Если основным станет bixbit.io, на дублирующих страницах docs понадобится cross-domain canonical.
