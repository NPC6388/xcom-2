# Research Prerequisite Reference (vanilla) — AUTHORITATIVE

Source: **parsed directly from the darosh tech-tree SVG** the user supplied
(`xcom2-tech-tree.svg`), via `parse_tree.py` (geometry → 159 nodes, 178 edges).
These are the actual drawn dependencies, not reconstructed. `(corpse)` = also needs that
unit's corpse recovered in-game.

> Note on names: darosh labels the first mag research **"Magnetized Weapons"** (in-game menu:
> "Magnetic Weapons"). The tree distinguishes the *research* node from the *item* it unlocks
> (e.g. "Magnetized Weapons" research → "Magnetic Rifles" item).

## Critical path (the spine that matters for tempo)
```
Operation Gatecrasher
  ├─ Modular Weapons ─► Magnetic Weapons ─► Gauss Weapons ─┐
  │                          (rifle/sg/pistol) (cannon/sniper)│
  ├─ Hybrid Materials ─► Plated Armor ─────────────────────┐ │
  ├─ Biotech ─► (all autopsies) ─► Officer Autopsy ─► Proving Grounds ─► Skulljack
  └─ Guerilla Ops ─► Resistance Communications              │ │
                                                            ▼ ▼
                                         ELERIUM  ◄── Gauss Weapons + Plated Armor
                                            │
                        ┌───────────────────┼───────────────────┐
                        ▼                   ▼                   ▼
                   Plasma Rifle        Powered Armor        (Elerium Conduit)
                        │                   │
        ┌───────────────┼─────────┐         ├─► Warden Armor
        ▼               ▼         ▼         ├─► W.A.R. Suit
   Beam Cannon    Plasma Lance  Storm Gun   └─► Wraith Suit
```

## Weapons
| Research | Requires | Unlocks |
|----------|----------|---------|
| Modular Weapons | Gatecrasher | Apply Weapon Upgrades; Magnetic Weapons |
| Apply Weapon Upgrades | Modular Weapons | weapon mod slots |
| **Magnetic Weapons** *(darosh: Magnetized Weapons)* | Modular Weapons | Magnetic Rifles, Shard Guns, Mag Pistol; **Gauss Weapons** |
| **Gauss Weapons** | Magnetic Weapons | Mag Cannon, Gauss Rifle (sniper); **Elerium** |
| **Plasma Rifle** | **Elerium** | Plasma Rifles, Beam Pistol; **Beam Cannon, Plasma Lance, Storm Gun** |
| Beam Cannon / Plasma Lance / Storm Gun | Plasma Rifle | gunner / sniper / shotgun top tier |

## Armor
| Research | Requires | Unlocks |
|----------|----------|---------|
| Hybrid Materials | Gatecrasher | Nanoscale Vest; **Plated Armor** |
| **Plated Armor** | Hybrid Materials | Predator Armor, **E.X.O. Suit, Spider Suit**; feeds Elerium |
| **Powered Armor** | **Elerium** | **Warden Armor, W.A.R. Suit, Wraith Suit** |
| Experimental Armor *(PG project)* | Shieldbearer Autopsy | Plated/Hazmat/Stasis **Vests** (≠ the suits above) |

## The Elerium gate (top-tier bottleneck)
**Elerium ← Gauss Weapons + Plated Armor.** Unlocks Plasma Rifle, Powered Armor, Elerium Conduit.
This is the single most important mid-game research target.

## Economy / infrastructure
| Research | Requires | Unlocks |
|----------|----------|---------|
| Biotech | Gatecrasher | **every autopsy**; Advanced Warfare Center |
| Resistance Communications | Guerilla Ops (early) | Resistance Comms facility, Resistance Radio, Make Contact, Blacksite Region |
| Power Relay | Gatecrasher | Power Conduit; (Elerium Conduit with Elerium) |
| Guerrilla Tactics School | Gatecrasher | Squad Size I & II, class perks, Equip PCS |

## Autopsies (all ← **Biotech** + the unit's corpse) and what they give
| Autopsy | Notable unlock |
|---------|----------------|
| Sectoid | **Mindshield → Psionics** (Psi path) |
| **Officer** | **Proving Grounds**, MEC Breakdown, Sectopod Breakdown, Trooper/Stun Lancer/Shieldbearer/Turret breakdowns |
| Muton | Plasma Grenade → Advanced Explosives (bombs) |
| Viper | Battlefield Medicine → Nanomedikit |
| Faceless | **Mimic Beacon** |
| Berserker | Overdrive Serum |
| Archon | Fusion Blade |
| Gatekeeper | Psi Amp |
| Andromedon | Proximity Mine |
| Chryssalid | Hellweave |

### Officer-Autopsy sub-tree (robotics & Proving Ground)
```
Officer Autopsy
 ├─ Proving Grounds ─► Skulljack ─► Skulljack Officer ─► Kill a Codex ─► Codex Brain (Avatar chain)
 │                   ├─ Experimental Grenade ─► Acid/Gas/Incendiary Grenade
 │                   └─ Experimental Ammo ─► AP/Talon/Tracer/Venom/Dragon Rounds
 ├─ MEC Breakdown ─► Bluescreen Protocol ─► **Bluescreen Rounds** / EMP Grenade ; GREMLIN Mk II
 ├─ Sectopod Breakdown ─► GREMLIN Mk III
 ├─ Turret Breakdown ─► Defense Matrix ─► Quad Turrets
 └─ Shieldbearer Autopsy ─► Experimental Armor (vests)
```

## Psi path
Sectoid Autopsy → **Mindshield** & **Psionics** → Psi Lab, Advanced Psi Amp (→ Psi Lab → Second Cell).

## Avatar / endgame spine (the win condition)
```
Skulljack Officer ─► Kill a Codex ─► Codex Brain ──► Codex Brain Coordinates ─► Psionic Gate ─┐
                                         ├─► Encrypted Codex Data ─► Skulljack Codex ─► Neutralize Avatar
Shadow Chamber (facility) feeds: Codex Brain, Blacksite Vial, Psionic Gate,                   │
   Recovered Stasis Suit, Mission Intel                                                       │
Resistance Communications ─► Blacksite Region ─► Blacksite Mission ─► Blacksite Vial ─► (coords) ─► Stasis Suit ─► Recovered Stasis Suit
                                                                                              │
   Neutralize Avatar  +  Psionic Gate  +  Recovered Stasis Suit  ──►  AVATAR AUTOPSY  ──► Broadcast Tower ──► FINAL MISSION
```
- **Shadow Chamber ← Encryption** (which is gated by the Codex Brain / Blacksite Vial line). The
  Shadow Chamber then hosts the Shadow Projects above. (A few Shadow-Chamber hub edges are tangled
  in the source layout; the Avatar Autopsy's three direct prereqs — Neutralize Avatar, Psionic
  Gate, Recovered Stasis Suit — are unambiguous.)

## Proving Ground items (built in the facility)
- **Skulljack** ← Proving Grounds (then Skulljack Officer / Skullmining).
- **Experimental Grenade** ← Proving Grounds → Acid/Gas/Incendiary (→ bombs via Advanced Explosives).
- **Experimental Ammo** ← Proving Grounds → AP/Talon/Tracer/Venom/Dragon Rounds.
- **Bluescreen Rounds** ← Bluescreen Protocol ← MEC Breakdown ← Officer Autopsy.
- **EXO Suit / Spider Suit** ← Plated Armor research. **W.A.R. / Wraith Suit** ← Powered Armor.

---
*Regenerate any time: `python parse_tree.py` against `xcom2-tech-tree.svg`.*
