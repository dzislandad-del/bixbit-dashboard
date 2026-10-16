"""report_export.py — экспорт HTML-отчёта в PDF, Excel (XLSX) и Markdown.

- PDF  — печать через установленный Google Chrome (headless), графики SVG сохраняются.
- XLSX — все таблицы отчёта по листам + «Сводка» (карточки показателей) + «Данные графиков»;
         пишется без сторонних библиотек (XLSX = zip с XML).
- MD   — заголовки, абзацы, карточки списком, таблицы Markdown (графики — ссылкой на HTML/PDF).

Использование из кода:  export(html_path, ["pdf", "xlsx", "md"]) -> [пути]
Из командной строки:    python3 scripts/report_export.py reports/quarterly-2026-Q3.html pdf xlsx md
"""
import html as htmllib, os, re, subprocess, sys, zipfile
from html.parser import HTMLParser
from xml.sax.saxutils import escape

CHROME = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
          "/Applications/Chromium.app/Contents/MacOS/Chromium",
          "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"]


class Doc(HTMLParser):
    """Разбирает отчёт в последовательность блоков: ('h', уровень, текст) | ('p', текст) | ('cards', [(k, v, s)]) | ('table', заголовок, head, rows, is_chart_data)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self._txt, self._mode = [], "", None
        self._skip = 0
        self._table = None
        self._row = None
        self._cell = None
        self._cards = None
        self._card = None
        self._cls_stack = []
        self.last_heading = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag in ("style", "script", "svg", "title"):
            self._skip += 1
            return
        if self._skip:
            return
        if tag in ("h1", "h2", "h3"):
            self._mode, self._txt = tag, ""
        elif tag in ("p", "li") and self._table is None and self._card is None:
            self._mode, self._txt = tag, ""
        elif tag == "div" and "cards" in cls.split():
            self._cards = []
        elif tag == "div" and "card" in cls.split() and self._cards is not None:
            self._card = {"k": "", "v": "", "s": ""}
        elif tag == "div" and self._card is not None and cls in ("k", "v", "s"):
            self._mode, self._txt = "card-" + cls, ""
        elif tag == "table":
            self._table = {"title": self.last_heading, "head": [], "rows": [], "chart": "chartdata" in cls, "caption": a.get("data-title")}
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = ""
        self._cls_stack.append((tag, cls))

    def handle_endtag(self, tag):
        if tag in ("style", "script", "svg", "title"):
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return
        t = " ".join(self._txt.split())
        if tag in ("h1", "h2", "h3") and self._mode == tag:
            self.blocks.append(("h", int(tag[1]), t)); self.last_heading = t; self._mode = None
        elif tag in ("p", "li") and self._mode == tag:
            if t:
                self.blocks.append(("p" if tag == "p" else "li", t))
            self._mode = None
        elif tag == "div" and self._mode and self._mode.startswith("card-"):
            self._card[self._mode[5:]] = t; self._mode = None
        elif tag == "div" and self._card is not None and self._mode is None and self._cls_stack and self._cls_stack[-1][1] == "card":
            self._cards.append((self._card["k"], self._card["v"], self._card["s"])); self._card = None
        elif tag == "div" and self._cards is not None and self._card is None and self._cls_stack and self._cls_stack[-1][1] == "cards":
            self.blocks.append(("cards", self._cards)); self._cards = None
        elif tag in ("td", "th") and self._cell is not None:
            self._row.append(" ".join(self._cell.split())); self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                if not self._table["head"]:
                    self._table["head"] = self._row
                else:
                    self._table["rows"].append(self._row)
            self._row = None
        elif tag == "table" and self._table is not None:
            tb = self._table
            self.blocks.append(("table", tb["caption"] or tb["title"], tb["head"], tb["rows"], tb["chart"])); self._table = None
        if self._cls_stack:
            self._cls_stack.pop()

    def handle_data(self, data):
        if self._skip:
            return
        if self._cell is not None:
            self._cell += data
        elif self._mode:
            self._txt += data


def parse(path):
    d = Doc()
    d.feed(open(path, encoding="utf-8").read())
    return d.blocks


# ---------- Markdown ----------

def to_md(path, out):
    md, base = [], os.path.basename(path)
    for b in parse(path):
        if b[0] == "h":
            md += ["", "#" * b[1] + " " + b[2], ""]
            if b[1] == 2 and ("динамика" in b[2].lower()):
                md.append(f"_Графики — в HTML/PDF-версии отчёта ({base}); ниже — их данные._\n")
        elif b[0] == "p":
            md += [b[1], ""]
        elif b[0] == "li":
            md.append(f"- {b[1]}")
        elif b[0] == "cards":
            md += [f"- **{k}:** {v} {('— ' + s) if s else ''}".rstrip() for k, v, s in b[1]] + [""]
        elif b[0] == "table":
            head, rows = b[2], b[3]
            if b[4]:
                md.append(f"_Данные графика «{b[1]}»:_\n")
            e = lambda c: c.replace("|", "\\|")
            md += ["| " + " | ".join(map(e, head)) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(map(e, r)) + " |" for r in rows] + [""]
    open(out, "w", encoding="utf-8").write("\n".join(md).strip() + "\n")
    return out


# ---------- XLSX ----------

NUM = re.compile(r"^[-+]?\d[\d\s  ]*([.,]\d+)?$")


def cell_xml(ref, v):
    s = (v or "").strip()
    if NUM.match(s):
        num = s.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", ".")
        return f'<c r="{ref}"><v>{num}</v></c>'
    return f'<c r="{ref}" t="inlineStr"><is><t xml:space="preserve">{escape(s)}</t></is></c>'


def col(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def sheet_xml(rows, bold_first=True):
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetViews><sheetView workbookViewId="0">'
           '<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>']
    widths = {}
    for r in rows:
        for j, v in enumerate(r):
            widths[j] = min(70, max(widths.get(j, 8), len(str(v or "")) + 2))
    if widths:
        out.append("<cols>" + "".join(f'<col min="{j + 1}" max="{j + 1}" width="{w}" customWidth="1"/>' for j, w in widths.items()) + "</cols>")
    out.append("<sheetData>")
    for i, r in enumerate(rows):
        cells = "".join(cell_xml(f"{col(j)}{i + 1}", v) for j, v in enumerate(r))
        if i == 0 and bold_first:
            cells = cells.replace("<c ", '<c s="1" ')
        out.append(f'<row r="{i + 1}">{cells}</row>')
    out.append("</sheetData></worksheet>")
    return "".join(out)


def to_xlsx(path, out):
    blocks = parse(path)
    sheets, used = [], set()

    def name(t):
        t = " ".join(re.sub(r"[\[\]:*?/\\]", " ", t or "Таблица").split())[:28].strip() or "Таблица"
        base, k = t, 2
        while t.lower() in used:
            t = f"{base[:25]} {k}"; k += 1
        used.add(t.lower())
        return t

    title = next((b[2] for b in blocks if b[0] == "h" and b[1] == 1), "Отчёт")
    summary = [["Показатель", "Значение", "Изменение"]]
    for b in blocks:
        if b[0] == "cards":
            summary += [[k, v, s] for k, v, s in b[1]]
    meta = next((b[1] for b in blocks if b[0] == "p"), "")
    sheets.append((name("Сводка"), [[title], [meta], []] + summary if summary[1:] else [[title], [meta]]))
    chart = []
    for b in blocks:
        if b[0] == "table" and b[4]:
            chart += [[b[1]]] + [b[2]] + b[3] + [[]]
        elif b[0] == "table":
            sheets.append((name(b[1]), [b[2]] + b[3]))
    if chart:
        sheets.append((name("Данные графиков"), chart))

    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    ct += [f'<Override PartName="/xl/worksheets/sheet{i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(sheets))]
    ct.append("</Types>")
    wb = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
          + "".join(f'<sheet name="{escape(n)}" sheetId="{i + 1}" r:id="rId{i + 1}"/>' for i, (n, _) in enumerate(sheets)) + "</sheets></workbook>")
    wbrels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
              + "".join(f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i + 1}.xml"/>' for i in range(len(sheets)))
              + f'<Relationship Id="rId{len(sheets) + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
              '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font></fonts>'
              '<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>'
              '<borders count="1"><border/></borders><cellStyleXfs count="1"><xf/></cellStyleXfs>'
              '<cellXfs count="2"><xf fontId="0"/><xf fontId="1" applyFont="1"/></cellXfs></styleSheet>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "".join(ct))
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", wb)
        z.writestr("xl/_rels/workbook.xml.rels", wbrels)
        z.writestr("xl/styles.xml", styles)
        for i, (_, rows) in enumerate(sheets):
            z.writestr(f"xl/worksheets/sheet{i + 1}.xml", sheet_xml(rows, bold_first=i > 0))
    return out


# ---------- PDF ----------

def to_pdf(path, out):
    chrome = next((c for c in CHROME if os.path.exists(c)), None)
    if not chrome:
        raise RuntimeError("PDF: не найден Google Chrome / Chromium / Edge")
    p = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                        f"--print-to-pdf={out}", "file://" + os.path.abspath(path)],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=180)
    if not os.path.exists(out) or os.path.getsize(out) < 1000:
        raise RuntimeError("PDF не создан: " + p.stdout.strip()[-300:])
    return out


def export(path, formats):
    res, root = [], os.path.splitext(path)[0]
    for f in formats:
        f = f.strip().lower()
        if f in ("", "html"):
            continue
        fn = {"pdf": to_pdf, "xlsx": to_xlsx, "md": to_md}.get(f)
        if not fn:
            raise ValueError(f"неизвестный формат: {f}")
        res.append(fn(path, f"{root}.{f}"))
    return res


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    for p in export(sys.argv[1], sys.argv[2:]):
        print(f"-> {p}")
