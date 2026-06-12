"""Inline the darosh tech-tree SVG into guide.src.html -> guide.html.
Annotates each node with data-label and each edge with data-src/data-dst (matched by
geometry), strips the SVG's leaky global <style>, adds a viewBox, and drops it into the
<!--TREE_SVG--> placeholder. Re-run any time:  python build_guide.py
"""
import re, math, xml.etree.ElementTree as ET

BASE = r"C:\Users\matth\Desktop\AI\xcom 2 vanilla"
SVG  = BASE + r"\xcom2-tech-tree.svg"
SRC  = BASE + r"\guide.src.html"
OUT  = BASE + r"\guide.html"
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

with open(SRC, encoding="utf-8") as f: src = f.read()
if "<!--TREE_SVG-->" not in src:
    raise SystemExit("placeholder <!--TREE_SVG--> not found in guide.src.html")
out = src.replace("<!--TREE_SVG-->", svg_markup)
with open(OUT, "w", encoding="utf-8") as f: f.write(out)

labeled = sum(1 for e in edges if e[4].get("data-src"))
print("Built %s  (%d nodes, %d edges labeled)" % (OUT, len(nodes), labeled))
