import re, xml.etree.ElementTree as ET, math, sys

SVG = r"C:\Users\matth\Desktop\AI\xcom 2 vanilla\xcom2-tech-tree.svg"
NS = "{http://www.w3.org/2000/svg}"

tree = ET.parse(SVG)
root = tree.getroot()

def translate_of(el):
    t = el.get("transform", "") or ""
    m = re.search(r"translate\(\s*([-\d.]+)\s*[ ,]\s*([-\d.]+)\s*\)", t)
    if m:
        return float(m.group(1)), float(m.group(2))
    m = re.search(r"translate\(\s*([-\d.]+)\s*\)", t)
    if m:
        return float(m.group(1)), 0.0
    return 0.0, 0.0

def classes(el):
    return (el.get("class") or "").split()

nodes = []   # (cx, cy, label)
edges = []   # (x0,y0,x1,y1)

def walk(el, ox, oy):
    tx, ty = translate_of(el)
    cx, cy = ox + tx, oy + ty
    cls = classes(el)
    tag = el.tag.replace(NS, "")

    if "node" in cls:
        # gather all tspan text under this node
        texts = []
        for tsp in el.iter(NS + "tspan"):
            if tsp.text:
                texts.append(tsp.text.strip())
        label = " ".join(t for t in texts if t).strip()
        if label:
            nodes.append((cx, cy, label))
        # don't descend further into node internals for node-collection,
        # but still recurse so we don't miss anything (labels already grabbed)

    if tag == "path" and "path" in cls:
        d = el.get("d", "")
        pts = re.findall(r"(-?\d+\.?\d*)[ ,](-?\d+\.?\d*)", d)
        if len(pts) >= 2:
            x0, y0 = float(pts[0][0]), float(pts[0][1])
            x1, y1 = float(pts[-1][0]), float(pts[-1][1])
            edges.append((cx + x0, cy + y0, cx + x1, cy + y1))

    for child in el:
        walk(child, cx, cy)

walk(root, 0, 0)

def nearest(x, y):
    best, bestd = None, 1e18
    for (nx, ny, lab) in nodes:
        d = (nx - x) ** 2 + (ny - y) ** 2
        if d < bestd:
            bestd, best = d, lab
    return best, math.sqrt(bestd)

# Deduplicate nodes
seen = set(); uniq = []
for n in nodes:
    if n[2] not in seen:
        seen.add(n[2]); uniq.append(n)

print("=== NODES (%d) ===" % len(uniq))
for cx, cy, lab in sorted(uniq, key=lambda n: (round(n[1]), round(n[0]))):
    print(f"  ({cx:8.1f},{cy:8.1f})  {lab}")

print("\n=== EDGES (%d) ===" % len(edges))
rels = []
for (x0, y0, x1, y1) in edges:
    a, da = nearest(x0, y0)
    b, db = nearest(x1, y1)
    if a and b and a != b:
        rels.append((a, b, da, db))

# dedupe
seen = set(); out = []
for a, b, da, db in rels:
    k = (a, b)
    if k not in seen:
        seen.add(k); out.append((a, b, da, db))

for a, b, da, db in sorted(out):
    print(f"  {a}  ->  {b}    (d={da:.0f}/{db:.0f})")

print("\n=== PREREQS (target: [sources]) ===")
from collections import defaultdict
pre = defaultdict(list)
for a, b, da, db in out:
    pre[b].append(a)
for tech in sorted(pre):
    print(f"  {tech}  <-  {', '.join(sorted(pre[tech]))}")
