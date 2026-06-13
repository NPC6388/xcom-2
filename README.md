# XCOM 2 Vanilla — Commander Playbook

A personal, **tempo-first** decision guide for XCOM 2 (base game + integrated DLC, **no War of the Chosen**) on **Commander** difficulty.

**▶ Live guide:** https://npc6388.github.io/xcom-2/

## What's inside
- **Research / Facilities / Upgrades** order across **Early / Mid / Late** game, with a tempo-driven backbone tying them together.
- Every recommendation leads with *why now* and flags the *trap to avoid*.
- An **interactive tech tree** (pan/zoom, dark themed): click any tech name in the tables to spotlight that node and light up its **prerequisites (before)** and **unlocks (after)**.
- Prerequisites are **parsed deterministically** from the darosh tech-tree SVG (166 nodes / 168 edges) — not guessed.
- A searchable **Database · Wiki**: every mission, research, facility, armor and weapon (with prereqs, triggers and stats), pulled from the Fandom wiki and compiled from `specs/database.md`. Type to filter across all tables; tech names stay clickable into the tree.

## Files
- `guide.html` — the built guide (served live; open this locally too)
- `guide.src.html` — editable template (`<!--TREE_SVG-->` + `<!--WIKI-->` placeholders)
- `build_guide.py` — rebuilds `guide.html` from the template + SVG + `specs/database.md`: `python build_guide.py`
- `parse_tree.py` — prints the parsed node/edge/prereq lists
- `xcom2-tech-tree.svg` — authoritative tech-tree source
- `specs/` — source specs: backbone + 9 phase×section cells + `tech-tree.md` + `database.md` (the wiki)
- `wiki_raw/` — cached Fandom wikitext dumps (provenance for `database.md`)
- `PROJECT-BRIEF.md`, `sources.md`, `SESSION-LOG.md`

See **`SESSION-LOG.md`** for how it was built.
