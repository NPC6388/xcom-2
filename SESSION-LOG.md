# Session Log — XCOM 2 Vanilla Commander Playbook

## Session 1 — 2026-06-11 → 2026-06-12

### Goal established (via interview)
Built a personal, decision-making **HTML playbook** for XCOM 2 on **Commander** difficulty.
Scope: **base game + integrated DLC** (Alien Hunters, Shen's Last Gift), **no War of the Chosen**.
Decision focus: all three of priority / trap-avoidance / timing, with **timing/tempo leading**.

### Locked decisions
| Dimension | Decision |
|-----------|----------|
| Audience | Personal playbook (the user), Commander difficulty |
| Scope | Base + integrated DLC; no WOTC |
| Lead lens | Timing/tempo |
| Sections | Research · Facilities · Upgrades |
| Phases | Early · Mid · Late |
| Structure | Chronological backbone + 9 small phase×section specs |
| Deliverable | Single self-contained `guide.html`, dark theme, light JS |
| Specialists | #1 Hacker (Combat→Haywire), #2 Medic (Medical→Restoration) — per user |

### What was built
- **Interview → brief** (`PROJECT-BRIEF.md`) capturing all decisions + build plan.
- **9 compartmentalized specs** + backbone in `specs/` (early/mid/late × research/facilities/upgrades).
- **`guide.html`** — the deliverable: sticky nav, "jump to phase", collapsible cells, tempo banners,
  priority pills, trap callouts, phase-transition triggers.
- **`sources.md`** — all 14 user links logged with fetch status; several were blocked (Reddit,
  GameFAQs, Fandom, StackExchange) and reconstructed via web search + cross-reference; WOTC-flavored
  sources filtered out.

### Tech tree — the key win
- User links to the **darosh interactive tech tree** couldn't be auto-fetched; recovered partial data
  from the compiled JS, then the user supplied **`xcom2-tech-tree.svg`**.
- Wrote **`parse_tree.py`** to parse the SVG geometry deterministically → **166 nodes / 168 edges**,
  reconstructing the full prerequisite graph (no guessing).
- This **corrected several prereqs** that were wrong/uncertain: Plated Armor ← Hybrid Materials;
  **Elerium ← Gauss Weapons + Plated Armor**; Beam/Lance/Storm ← Plasma Rifle; Proving Grounds ←
  Officer Autopsy; AWC ← Biotech; Bluescreen chain (Officer→MEC Breakdown→Bluescreen Protocol);
  EXO/Spider ← Plated Armor; full Avatar spine to Final Mission.
- Reconciled reference written to `specs/tech-tree.md`.

### Interactive viewer (final state)
- **`build_guide.py`** inlines the annotated SVG (each node tagged `data-label`, each edge
  `data-src`/`data-dst`) into `guide.src.html` → `guide.html`. Strips the SVG's leaky global styles,
  adds a viewBox.
- Visual tech tree: **pan/zoom canvas** (wheel-zoom to cursor, drag-pan, Fit/zoom buttons),
  dark theme + category color legend matching the user's in-game addon.
- **Every tech name in the tables is an auto-detected clickable link** → spotlights that node, dims the
  rest, and highlights **before (prereqs, blue)** / **after (unlocks, green)** with gold edges, then
  centers/zooms to it.

### File inventory
```
guide.html          ← built deliverable (open this)
guide.src.html      ← editable template (has <!--TREE_SVG--> placeholder)
build_guide.py      ← regenerates guide.html from template + SVG  (python build_guide.py)
parse_tree.py       ← prints the parsed node/edge/prereq lists
xcom2-tech-tree.svg ← authoritative source (user-supplied)
PROJECT-BRIEF.md · sources.md · SESSION-LOG.md
specs/  00-backbone.md · tech-tree.md · {early,mid,late}-{research,facilities,upgrades}.md
```

### Housekeeping
- Temporary screen captures (`_screenshot.png`, `_crop.png`, `_verify.png`) were created to read the
  user's screen / verify rendering, then **deleted**. No captures retained in the project.

### Open / to-verify
- A few strategic opinions (Mag-weapons timing, SPARK/hacking value, "traps") are judgment calls,
  not tech-tree facts — flagged as such in the specs.
- SPARK and hacking-method detail came from blocked links; reconstructed, marked verify.
- Rebuild after any template/SVG change: `python build_guide.py`.

### This session's final task
- **Publish ("push live")** + this session log. Publishing destination/visibility pending user choice.
