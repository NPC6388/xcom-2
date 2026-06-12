# XCOM 2 Vanilla — Personal Commander Playbook · Project Brief

## Goal
A personal, decision-making playbook that tells **me** what to do next during my own
XCOM 2 runs on **Commander** difficulty. Timing/tempo is the spine; "what to pick next"
and "traps to avoid" ride along on every recommendation.

## Locked decisions (from interview)
| Dimension | Decision |
|-----------|----------|
| Audience | Personal playbook (me), during live playthroughs |
| Difficulty | Commander (tuned specifically; no hedging across difficulties) |
| Game scope | Base game + integrated DLC (Alien Hunters, Shen's Last Gift). **No** War of the Chosen. |
| Decision focus | All three, **timing/tempo leads**; priorities + trap-avoidance support |
| Major sections | Research order · Facilities order · Upgrade order |
| Phases | Early · Mid · Late |
| Structure | Chronological **backbone** + **9 small phase×section cell specs** |
| Spec format | Small markdown files, tables + notes (one per cell) |
| Deliverable | Single self-contained **guide.html**, light JS (collapsible cells, sticky nav, "jump to my current phase") |
| Sources handling | **Fetch + reconcile**: where sources disagree, flag it and recommend for Commander tempo with reasoning |

## Phase boundaries (working definitions — refine from sources)
- **Early:** Gatecrasher → first Skulljack / first blacksite.
- **Mid:** Skulljack → Codex → Avatar Project reveal.
- **Late:** Avatar facilities → final mission.

## Compartmentalization map (9 cells + backbone)
```
                 RESEARCH            FACILITIES           UPGRADES
   EARLY   early-research.md   early-facilities.md   early-upgrades.md
   MID     mid-research.md     mid-facilities.md     mid-upgrades.md
   LATE    late-research.md    late-facilities.md    late-upgrades.md
   ------------------------------------------------------------------
   BACKBONE: 00-backbone.md  (stitches all 9 along the timeline)
```

## Build order (process)
1. ✅ Interview → brief locked.
2. ✅ Record sources (`sources.md`).
3. ⬜ Fetch + reconcile each source; fill cell specs with cited orders + conflict notes.
4. ⬜ Fill backbone with tempo beats + phase-transition triggers.
5. ⬜ Compile specs → `guide.html`.
6. ⬜ Review pass: each cell audited standalone; backbone walked end-to-end.

## Done = 
Every cell spec has a complete, sourced order table with a "why now" and a "trap" per row;
the backbone walks early→late with explicit transition triggers; `guide.html` opens by
double-click and lets me jump to my current phase.
