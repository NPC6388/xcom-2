"""Build guide.html from guide.src.html.

Two placeholders are filled:
  <!--TREE_SVG-->  the darosh tech-tree SVG, annotated (data-label on nodes,
                   data-src/data-dst on edges by geometry), global <style> stripped,
                   viewBox added.
  <!--WIKI-->      the searchable "Database · Wiki" section, compiled from
                   specs/database.md (markdown -> themed HTML cells).

Re-run any time:  python build_guide.py
"""
import re, math, xml.etree.ElementTree as ET

BASE = r"C:\Users\matth\Desktop\AI\xcom 2 vanilla"
SVG  = BASE + r"\xcom2-tech-tree.svg"
SRC  = BASE + r"\guide.src.html"
OUT  = BASE + r"\guide.html"
DB   = BASE + r"\specs\database.md"
NS   = "http://www.w3.org/2000/svg"
NSb  = "{%s}" % NS
ET.register_namespace("", NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

tree = ET.parse(SVG)
root = tree.getroot()

def translate_of(el):
    t = el.get("transform", "") or ""
    m = re.search(r"translate\(\s*([-\d.]+)\s*[ ,]\s*([-\d.]+)\s*\)", t)
    if m: return float(m.group(1)), float(m.group(2))
    m = re.search(r"translate\(\s*([-\d.]+)\s*\)", t)
    if m: return float(m.group(1)), 0.0
    return 0.0, 0.0

def classes(el): return (el.get("class") or "").split()

nodes, edges = [], []
def walk(el, ox, oy):
    tx, ty = translate_of(el); cx, cy = ox + tx, oy + ty
    cls = classes(el)
    if "node" in cls:
        texts = [t.text.strip() for t in el.iter(NSb+"tspan") if t.text and t.text.strip()]
        label = " ".join(texts).strip()
        if label:
            el.set("data-label", label)
            nodes.append((cx, cy, label))
    if "edgePath" in cls:
        p = el.find(NSb+"path")
        if p is not None:
            pts = re.findall(r"(-?\d+\.?\d*)[ ,](-?\d+\.?\d*)", p.get("d",""))
            if len(pts) >= 2:
                x0,y0 = float(pts[0][0]), float(pts[0][1])
                x1,y1 = float(pts[-1][0]), float(pts[-1][1])
                edges.append((cx+x0, cy+y0, cx+x1, cy+y1, el))
    for c in el: walk(c, cx, cy)
walk(root, 0, 0)

def nearest(x, y):
    best, bd = None, 1e18
    for nx, ny, lab in nodes:
        d = (nx-x)**2 + (ny-y)**2
        if d < bd: bd, best = d, lab
    return best

for x0,y0,x1,y1,el in edges:
    s, t = nearest(x0,y0), nearest(x1,y1)
    if s and t and s != t:
        el.set("data-src", s); el.set("data-dst", t)

# strip the global <style> (it would leak body/table/etc rules into the page)
for child in list(root):
    if child.tag == NSb+"style":
        root.remove(child)

# add a viewBox so it scales cleanly
W = root.get("width", "3195.125"); H = root.get("height", "2929")
root.set("viewBox", "0 0 %s %s" % (W, H))

svg_markup = ET.tostring(root, encoding="unicode")

# ---------------------------------------------------------------------------
# specs/database.md  ->  searchable "Database · Wiki" HTML
# A small, purpose-built markdown subset (headings, GFM pipe tables, bold/italic,
# inline code, links, [[wikilinks]], "- " lists, paragraphs, --- rules).
# ---------------------------------------------------------------------------
def md_inline(s):
    s = s.replace("\\*", "\x00")                              # protect escaped asterisks
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)                 # [[wikilink]] -> text (linkify catches it)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               r'<a class="cite" href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", s)
    s = s.replace("\x00", "*")
    return s

def _cells(row):
    r = row.strip()
    if r.startswith("|"): r = r[1:]
    if r.endswith("|"):   r = r[:-1]
    return [c.strip() for c in r.split("|")]

def render_table(rows):
    if not rows: return ""
    header = _cells(rows[0])
    body = rows[1:]
    if len(rows) >= 2 and set(rows[1].replace("|","").replace("-","").replace(":","").strip()) == set():
        body = rows[2:]                                       # drop the |---| separator row
    html = ["<table>", "<tr>" + "".join("<th>"+md_inline(c)+"</th>" for c in header) + "</tr>"]
    for r in body:
        html.append("<tr>" + "".join("<td>"+md_inline(c)+"</td>" for c in _cells(r)) + "</tr>")
    html.append("</table>")
    return "".join(html)

def md_body(md):
    lines = md.split("\n"); n = len(lines); i = 0
    out, para, lst = [], [], []
    def flush_para():
        if para: out.append("<p>" + md_inline(" ".join(para)) + "</p>"); para.clear()
    def flush_list():
        if lst: out.append("<ul>" + "".join("<li>"+md_inline(x)+"</li>" for x in lst) + "</ul>"); lst.clear()
    while i < n:
        st = lines[i].strip()
        if not st or st == "---":
            flush_para(); flush_list(); i += 1; continue
        if st.startswith("|"):
            flush_para(); flush_list()
            tbl = []
            while i < n and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip()); i += 1
            out.append(render_table(tbl)); continue
        m = re.match(r"^(#{2,4})\s+(.*)$", st)
        if m:
            flush_para(); flush_list()
            out.append("<h4>" + md_inline(m.group(2)) + "</h4>"); i += 1; continue
        if st.startswith("- "):
            flush_para(); lst.append(st[2:]); i += 1; continue
        flush_list(); para.append(st); i += 1
    flush_para(); flush_list()
    return "\n".join(out)

def slug(title):
    word = title.split("·")[-1].strip().split()[0].lower()  # "1 · MISSIONS" -> "missions"
    return re.sub(r"[^a-z0-9]+", "-", word).strip("-")

def build_wiki(md):
    # split on H1 lines: parts = [pre, h1_1, body_1, h1_2, body_2, ...]
    parts = re.split(r"(?m)^#\s+(.+)$", md)
    preamble = parts[2] if len(parts) > 2 else ""
    sects = list(zip(parts[3::2], parts[4::2]))              # (title, body) pairs

    # peel a trailing "## Provenance ..." block off the last section into a footer
    footer = ""
    if sects:
        t, b = sects[-1]
        mm = re.search(r"(?m)^##\s+Provenance.*", b)
        if mm:
            footer = b[mm.start():]; sects[-1] = (t, b[:mm.start()])

    cells = []
    for title, body in sects:
        sid = slug(title)
        name = title.split("·")[-1].strip().title()
        cells.append(
            f'<details id="wiki-{sid}"><summary>{name} '
            f'<span class="sec">Database</span></summary>'
            f'<div class="body">{md_body(body)}</div></details>'
        )

    html = [f'<div class="wiki-intro">{md_body(preamble)}</div>']
    html.append(
        '<div class="wikisearch">'
        '<input id="wikiq" type="search" autocomplete="off" spellcheck="false" '
        'placeholder="Search the database — e.g. &quot;Blacksite&quot;, &quot;Elerium&quot;, &quot;Bluescreen&quot;, &quot;Proving Ground&quot;…">'
        '<span id="wikicount" class="tthint"></span></div>'
    )
    html.append('<div id="wikiroot">' + "\n".join(cells) + "</div>")
    if footer:
        html.append('<div class="wiki-foot">' + md_body(footer) + "</div>")
    return "\n".join(html)

with open(DB, encoding="utf-8") as f: db_md = f.read()
wiki_html = build_wiki(db_md)

with open(SRC, encoding="utf-8") as f: src = f.read()
for ph in ("<!--TREE_SVG-->", "<!--WIKI-->"):
    if ph not in src:
        raise SystemExit("placeholder %s not found in guide.src.html" % ph)
out = src.replace("<!--TREE_SVG-->", svg_markup).replace("<!--WIKI-->", wiki_html)
with open(OUT, "w", encoding="utf-8") as f: f.write(out)

labeled = sum(1 for e in edges if e[4].get("data-src"))
wiki_cells = wiki_html.count("<details ")
wiki_tables = wiki_html.count("<table>")
print("Built %s  (%d nodes, %d edges labeled; wiki: %d cells, %d tables)"
      % (OUT, len(nodes), labeled, wiki_cells, wiki_tables))
