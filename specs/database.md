# XCOM 2 Complete Database — Missions · Research · Facilities · Armor · Weapons

**Source:** the official Fandom wiki (`xcom.fandom.com`), pulled **2026-06-12** via the
MediaWiki API (`api.php?action=parse&prop=wikitext`) — the normal page URLs 403 to bots,
but the API endpoint returns clean wikitext. Cached wikitext lives in `wiki_raw/`.

**Scope filter:** base game **+ Alien Hunters + Shen's Last Gift** (the integrated DLC this
playbook covers). **War of the Chosen content is excluded** and flagged where it appears in
shared wiki tables. DLC items are tagged `[AH]` (Alien Hunters) / `[SLG]` (Shen's Last Gift).

**Companion file:** `specs/tech-tree.md` holds the *authoritative prerequisite graph* parsed
from the darosh SVG. This file adds the wiki's quantitative data (rewards, costs, corpse
counts, stats) and the **mission database**, which the tech tree doesn't cover.

---

# 1 · MISSIONS

Missions split into **Generic** (repeatable, don't advance the plot) and **Key** (story
spine). Plus DLC one-offs and the non-optional Avenger Defense.

## 1.1 Generic missions

| Mission family | Sub-mission | Timed? | Conceal start? | Trigger / how it appears | Objective | Guaranteed rewards |
|---|---|---|---|---|---|---|
| **Guerrilla Ops** | Recover Item | Yes (6 turns) | Yes | Spawns to counter a pending **Dark Event**; 2–3 offered at once, only **one** completable | Hack & disable self-detonating charges; don't let the object be destroyed | Cancels the chosen Dark Event |
| Guerrilla Ops | Hack Workstation | Yes (8 turns) | Yes | ″ | Hack ADVENT workstation before network lockout | Cancels Dark Event |
| Guerrilla Ops | Destroy Alien Relay | Yes (8 turns) | Yes | ″ | Destroy the relay (6–8 HP, scales w/ difficulty) before data transfer ends | Cancels Dark Event |
| Guerrilla Ops | Protect Device | Implicit (~9–12 turns) | Yes | ″ | Defend a 30-HP data tap until secured | Cancels Dark Event |
| **Council Missions** | Rescue VIP | Yes (12 turns) | Yes | Council offers periodically | Recover VIP from van/cell, EVAC all soldiers | **Intel** + (Engineer / Scientist / recovered captured soldier) |
| Council Missions | Extract VIP | Yes (12 turns) | **No** | ″ | Start holding the VIP; EVAC all | **Intel** + Resistance-VIP reward |
| Council Missions | Neutralize Enemy VIP | Yes (12 turns) | Yes | ″ | Kill/subdue enemy VIP & EVAC; killing forfeits Intel | **Supplies** (alive/dead) + Intel (if captured alive) |
| **Supply Raids** | Supply Raid | **No** | Yes | Resistance sabotages an ADVENT supply line | Kill all hostiles; loot scattered crates (don't blow them up) | **Supplies + Alien Alloys + Elerium Crystals**, chance of Elerium Core |
| Supply Raids | Landed UFO | **No** | Yes | ″ (UFO sabotaged) | Secure UFO; after reveal, 6 turns to disable distress beacon | Same as Supply Raid |
| **Alien Facility Assault** | — | **No** | Yes | Make **contact** with the facility's region, **or** unlock a **Facility Lead** (rare hack reward / ADVENT Datapad research) for an immediate assault | Plant **X4** on the facility, EVAC; killing all enemies not required | **Reduces Avatar Project** by the pips that facility contributed; resets timer to next facility |
| **ADVENT Retaliation** | — | **No** | **No** | Auto every **4–5 weeks** vs a Resistance Haven | Rescue ≥6 of 13 civilians **and** kill all hostiles | +3 income/civ saved (4 on Easy). Only generic mission where **Faceless & Chryssalids** spawn naturally |

**Skip/fail penalties:** Guerrilla Op skipped/failed → *all* pending Dark Events fire.
Council / Supply Raid / Retaliation skipped or failed → **lose contact** with that region
(higher Intel cost + time to re-establish).

## 1.2 Key (story) missions — the golden path

Ordered along the campaign spine. Each Key mission reduces the Avatar Project (if underway)
and usually drops a key research item.

| # | Mission | Unlocked by (prerequisite) | Timed? | Conceal? | Objective | Reward → next step |
|---|---|---|---|---|---|---|
| 1 | **Operation Gatecrasher** (Sabotage ADVENT Monument) | Game start (after intro). Tutorial adds *Recover the ADVENT Power Converter* as a 2nd scripted op | No | Yes | 4 soldiers kill 6 hostiles, plant X4 on the Elder statue | Opens the campaign / Avenger |
| 2 | **ADVENT Blacksite Assault** | Spokesman's Avatar-Project cutscene **+ research [[Resistance Communications]] + make contact with the Blacksite region** (no Facility-Lead shortcut here) | No | Yes | Recover the Blacksite Vial, EVAC the carrier | **125 Supplies, −1 Avatar (−2 Legend), [[Blacksite Vial]] item.** Activates the **Doom Counter** |
| 3 | **ADVENT Forge Facility Assault** | Complete the **[[Blacksite Vial]]** Shadow Project (needs Shadow Chamber) **+ contact the Forge region** | No | Yes | Reach Clean Room, steal **ADVENT Stasis Suit**, carry to EVAC | **Supplies, −3 Avatar, Recovered Stasis Suit item.** 20–30 days later → **UFO triggers Avenger Defense** |
| 4 | **Codex Data Coordinates Investigation** | Complete the **[[Codex Brain]]** Shadow Project **+ contact the coordinate region** | No | Yes | Reach the alien **Psi Gate**, kill all (Chryssalids + a Gatekeeper emerges) | **Supplies, −3 Avatar, [[Psionic Gate]] item.** 20–30 days later → **UFO triggers Avenger Defense** |
| 5 | **ADVENT Network Tower Assault** | Complete the **[[Avatar Autopsy]]** Shadow Project | No | Yes | Hack the Network Tower workstation. Spend **Intel** pre-mission for up to 4 squad bonuses; squad capped at 3 unless you buy the size bonus | No reward — leads straight to the finale |
| 6 | **Alien Fortress Assault** (Operation Leviathan) | Immediately after the Network Tower. **Locks out all other Geoscape activity** | No | **No** | Reach the Psi Gate hub, kill 3 Avatars, keep the Commander's Avatar alive | **Win the game** |

**Avenger Defense** (non-optional, *not* a story mission): triggers from the **Hunt XCOM**
Dark Event UFO **or** 20–30 days after Forge **or** Codex-Coordinates (whichever finishes
first). No reward; **failure = instant game over**. Doesn't start concealed, no timer; destroy
the Disruptor and keep enemies off the ramp. Bradford feeds reinforcements every other turn;
the **Defense Matrix** facility donates 4 recycled ADVENT Turrets.

## 1.3 Skulljack-driven mid-game beats

These aren't separate map types but gate the late story (see `tech-tree.md` Avatar spine):
- **Skulljack an ADVENT Officer** (carry a Skulljack, melee a stunned/standing Officer) →
  spawns a **Codex** → kill it for the **Codex Brain** item → research opens Encryption /
  Shadow Chamber line.
- **Skulljack a Codex** (after **Encrypted Codex Data** research) → spawns the **Avatar** →
  **Neutralize Avatar**, a prereq of the **Avatar Autopsy**.

## 1.4 DLC missions (one-off, optional, persist on the Geoscape)

| Mission | DLC | Forced squadmate | Objective | Unlocks on success |
|---|---|---|---|---|
| **Alien Nest Investigation** (Operation Regal Beast) | Alien Hunters `[AH]` | Bradford (Colonel Ranger, Blademaster) — must survive | Kill/repel the **Viper King** in Vahlen's old facility, then clear Vipers | Begins **Alien Ruler** spawns; unlocks **Bolt Caster / Shadowkeeper / Hunter's Axe** upgrades + Supplies |
| **Lost Towers Investigation** (Operation Last Gift) | Shen's Last Gift `[SLG]` | Lily Shen (Colonel Specialist) + the SPARK — both must survive | Clear an abandoned ADVENT facility, activate the SPARK prototype, destroy **Julian** | Rewards 1 **SPARK** + unlocks **SPARK production** in the Proving Ground + Supplies |

*(WotC's "Lost and Abandoned", Ambush, Recover ADVENT Crates, and the Chosen Avenger-Defense
variant are out of scope.)*

## 1.5 Mission grade (end-of-mission rating)
Flawless (no wounds) · Excellent (wounds, no deaths) · Good (1–2 lost) · Fair (½ squad lost)
· Poor (failure or most of squad lost).

---

# 2 · RESEARCH

Prerequisite **graph** is authoritative in `specs/tech-tree.md`. Below is the wiki's
project list + what each unlocks. `(corpse)` = also needs that unit's corpse recovered.

## 2.1 Standard projects (Lab)

| Research | Requires | Key unlocks |
|---|---|---|
| **Alien Biotech** | Gatecrasher (start) | Gates **every autopsy**; **Advanced Warfare Center** |
| **Modular Weapons** | Gatecrasher | Weapon upgrade slots; → **Magnetic Weapons** |
| **Magnetic Weapons** | Modular Weapons | Mag Rifle / Shard Gun / Mag Pistol / Mag Cannon-line; → **Gauss Weapons** |
| **Gauss Weapons** | Magnetic Weapons | Gauss Rifle (sniper), Mag Cannon; feeds **Elerium** |
| **Hybrid Materials** | Gatecrasher | Nanoscale Vest; → **Plated Armor** |
| **Plated Armor** | Hybrid Materials | Predator Armor + EXO/Spider suit projects; feeds **Elerium** |
| **Elerium** | **Gauss Weapons + Plated Armor** | → **Plasma Rifle**, **Powered Armor**, Elerium Conduit. *(WotC also needs ADVENT MEC Breakdown — not in vanilla)* |
| **Plasma Rifle** | Elerium | Plasma Rifle/Pistol; → **Beam Cannon / Plasma Lance / Storm Gun** |
| Beam Cannon / Plasma Lance / Storm Gun | Plasma Rifle | Top-tier cannon / sniper / shotgun |
| **Powered Armor** | Elerium | Warden Armor + WAR/Wraith suit projects |
| **Resistance Communications** | (early, via Guerrilla Ops) | **Resistance Comms** facility, Make Contact, Blacksite region |
| **Resistance Radio** | Resistance Communications | Cheaper/faster contact & comms range |
| **Alien Encryption** | (story item) | **Shadow Chamber** facility |
| **Psionics** | **Sectoid Autopsy** | **Psi Lab** facility (Psi Operatives) |
| **Facility Lead** | ADVENT Datapad (loot) | Reveals an Alien Facility for immediate assault |
| ADVENT Datapad Decryption / Alien Data Cache Decryption | loot items | Intel / Supplies / chance of Facility Lead |
| **Experimental Weapons** `[AH]` | Alien Hunters intro | Bolt Caster / Shadowkeeper / Hunter's Axe lines |

## 2.2 Shadow Chamber projects (built in the Shadow Chamber)

Pause all standard research while active. The Avatar spine:

| Shadow Project | Requires (item from mission) | Unlocks / next |
|---|---|---|
| **Blacksite Vial** | Blacksite Vial (from Blacksite Assault) | → **Forge Facility** mission available |
| **Codex Brain** | Codex Brain (kill a Skulljacked-Officer's Codex) | → **Codex Data Coordinates** mission |
| **Encrypted Codex Data** | Codex Brain line | → enables **Skulljack a Codex** → spawns Avatar |
| **Recovered ADVENT Stasis Suit** | ADVENT Stasis Suit (from Forge) | A prereq of Avatar Autopsy |
| **Psionic Gate** | Psi Gate (from Codex Coordinates) | A prereq of Avatar Autopsy |
| **Avatar Autopsy** | **Neutralize Avatar + Psionic Gate + Recovered Stasis Suit** | → **Network Tower** → **Final Mission** |

## 2.3 Autopsies (each ← Alien Biotech + the unit's corpse)

"Corpses for instant" = corpses banked to make the research instant, per difficulty
(R/V/**C**/L — Commander is the 3rd value). WotC-only autopsies (Priest, Purifier, Spectre,
The Lost) omitted.

| Autopsy | Corpses for instant (R/V/**C**/L) | Item unlocked | Other unlock |
|---|---|---|---|
| **ADVENT Officer** | n/a | — | **Proving Ground** + opens MEC/Shieldbearer/Stun Lancer/Trooper/Turret breakdowns |
| **Sectoid** | 6/6/**6**/10 | Mindshield | **Psionics** |
| **Muton** | 5/6/**6**/9 | Advanced Grenade Launcher | Plasma Grenade (project) |
| **Viper** | 5/5/**5**/8 | — | Battlefield Medicine |
| **Faceless** | 3/4/**4**/7 | **Mimic Beacon** | — |
| **Berserker** | 6/6/**6**/9 | Overdrive Serum | — |
| **Archon** | 5/5/**5**/8 | Fusion Blade | — |
| **Gatekeeper** | 3/6/**6**/9 | **Alien Psi Amp** | — |
| **Andromedon** | 5/5/**5**/8 | Proximity Mine | — |
| **Chryssalid** | 15/15/**15**/20 | **Hellweave** | — |
| **Sectopod Breakdown** | 3/6/**6**/9 | **GREMLIN Mark III** | — |
| ADVENT MEC Breakdown | 3/4/**4**/7 | **GREMLIN Mark II** | **Bluescreen Protocol**; feeds Elerium (WotC only) |
| ADVENT Shieldbearer | 4/4/**4**/7 | — | **Experimental Armor** (vests) |
| ADVENT Stun Lancer | 4/6/**6**/9 | **Arc Blade** | — |
| ADVENT Trooper | 10/15/**15**/25 | **Battle Scanner** | — |
| ADVENT Turret Breakdown | 3/3/**3**/6 | — | **Defense Matrix** |

### Alien Hunters boss autopsies `[AH]` (instant; from the Ruler kills)
| Autopsy | Armor unlocked |
|---|---|
| **Viper King Autopsy** | **Serpent Suit** |
| **Berserker Queen Autopsy** | **R.A.G.E. Suit** |
| **Archon King Autopsy** | **Icarus Armor** |

---

# 3 · FACILITIES (the Avenger)

**Power note:** Power Relay *produces* power; everything else consumes it. Costs are **vanilla**
Supplies (the wiki lists `vanilla (WotC)`; WotC values dropped). Only **Resistance Comms** and
**Power Relay** may be built more than once. Upgrades are instant (no build time).

## 3.1 Static facilities (pre-built, can't be removed)
Bridge · Research · Engineering · Armory · Living Quarters · Bar/Memorial · Commander's Quarters.

## 3.2 Buildable facilities (12 clearable rooms: 4 rows × 3 cols)

| Facility | Cost (Supplies) | Power | Upkeep/mo | Build time | Research prereq | Purpose |
|---|---|---|---|---|---|---|
| **Guerrilla Tactics School** | 85 | 3 | 25 | 14 d | — | Squad Size I & II, class training, Equip PCS |
| **Proving Ground** | 100 | 3 | 25 | 14 d | **ADVENT Officer Autopsy** | Experimental ammo/grenades/armor, Skulljack, suits, SPARKs |
| **Power Relay** | 80 | — (produces) | 10 | 12 d | — | +power; Power/Elerium Conduit on exposed coils |
| **Resistance Comms** | 110 | 3 | 25 | 16 d | **Resistance Communications** | +contact capacity (build multiples) |
| **Advanced Warfare Center** | 80 | 3 | 35 | 21 d | **Alien Biotech** | Heal wounded faster; random bonus ability per soldier *(removed in WotC)* |
| **Laboratory** | 150 | 3 | 35 | 20 d | — | +research speed |
| **Workshop** | 250 | 3 | 35 | 20 d | — | Gremlin engineers staff adjacent facilities |
| **Defense Matrix** | 75 | 2 | 10 | 14 d | **Defense Matrix** (← Turret Breakdown) | Turrets for Avenger Defense |
| **Psi Lab** | 175 | 5 | 55 | 21 d | **Psionics** | Train Psi Operatives |
| **Shadow Chamber** | 125 | 5 | 30 | 14 d | **Alien Encryption** | Hosts Shadow Projects (Avatar spine) |

*(WotC-only facilities — Resistance Ring, Training Center, Infirmary — excluded.)*

## 3.3 Proving Ground projects (built once Proving Ground exists)

| Project | Result |
|---|---|
| **Experimental Ammo** | Random: AP / Dragon / Talon / Tracer / Venom Rounds |
| **Experimental Grenade** | Random: Acid / Gas / Incendiary Grenade (→ Bombs after **Advanced Explosives**) |
| **Experimental Armor** | Random: Hazmat / Plated / Stasis **Vest** (needs Shieldbearer Autopsy) |
| **Experimental Heavy Weapon** | Random: Flamethrower or Shredder Gun (unlocked by EXO Suit project) |
| **Experimental Powered Weapon** | Random: Blaster Launcher / Hellfire Projector / Plasma Blaster / Shredstorm Cannon (unlocked by WAR Suit project) |
| **E.X.O. Suit** / **Spider Suit** | Heavy / Light suit (needs **Plated Armor**) |
| **W.A.R. Suit** / **Wraith Suit** | Heavy / Light suit (needs **Powered Armor**) |
| Serpent / R.A.G.E. / Icarus Armor `[AH]` | From the matching boss autopsy |
| **Battlefield Medicine** | All Medikits → Nanomedikits (needs Viper Autopsy) |
| **Bluescreen Protocol** | Unlocks Bluescreen Rounds + EMP Grenades (needs MEC Breakdown) |
| **Skulljack** → **Skullmining** | Builds/upgrades the Skulljack (+25 Hack, enables skullmining) |
| **Plasma Grenade** | All Frag Grenades → Plasma Grenades (needs Muton Autopsy) |
| **Advanced Explosives** | Upgrades grenades → Bombs |
| **Mechanized Warfare** `[SLG]` | Unlocks building SPARKs (after Lost Towers mission) |

---

# 4 · ARMOR

`+` values are bonuses over Kevlar. Suits marked "1 per project" are built individually in the
Proving Ground; Predator/Warden are squad-wide Engineering purchases. (Resistance/SPARK armor +
WotC excluded except SPARK below.)

| Armor | Class | +HP | +Armor | +Mob | +Dodge | Util slots | Heavy wpn | Notes | Research / source |
|---|---|---|---|---|---|---|---|---|---|
| **Kevlar Armor** | Basic | — | — | — | — | 1 | — | Starting armor | — |
| **Predator Armor** | Medium | +4 | — | — | — | 2 | — | Squad-wide | **Plated Armor** |
| **Warden Armor** | Medium | +6 | +1 | — | — | 2 | — | Squad-wide | **Powered Armor** |
| **Spider Suit** | Light | +4 | — | +1 | +20 | 1 | — | Grapple | Spider Suit Project (← Plated Armor) |
| **Wraith Suit** | Light | +6 | — | +2 | +25 | 1 | — | Grapple + **Wraith** (phase through) | Wraith Suit Project (← Powered Armor) |
| **E.X.O. Suit** | Heavy | +5 | +1 | — | — | 1 | ✔ | Mounts a Heavy Weapon | EXO Suit Project (← Plated Armor) |
| **W.A.R. Suit** | Heavy | +6 | +2 | — | — | 1 | ✔ | **Shieldwall** | WAR Suit Project (← Powered Armor) |
| **Serpent Suit** `[AH]` | Light | +5 | — | +1 | +35 | 1 | — | Grapple, Frostbite, panics Vipers | **Viper King Autopsy** |
| **Icarus Armor** `[AH]` | Medium | +7 | +1 | +1 | — | 2 | — | Vault, Icarus Jump, panics Archons | **Archon King Autopsy** |
| **R.A.G.E. Suit** `[AH]` | Heavy | +6 | +1 | +1 | — | 1 | ✔ | Rage Strike, panics Mutons/Berserkers | **Berserker Queen Autopsy** |

*(Serpent/R.A.G.E. upgrade to "Serpent Armor / R.A.G.E. Armor" — +HP/Armor — once **Powered
Armor** is researched.)*

### Vests (Experimental Armor / Proving Ground, utility-slot items)
Nanoscale Vest (← Hybrid Materials) · Plated Vest · Hazmat Vest · Stasis Vest · Hellweave (←
Chryssalid Autopsy).

### SPARK Armor `[SLG]` (SPARK units only, no utility slots)
| Tier | +HP | +Armor | +Mob |
|---|---|---|---|
| SPARK Armor | — | — | — |
| Reinforced Frame | +3 | +1 | +1 |
| Anodized Chassis | +5 | +2 | +2 |

---

# 5 · WEAPONS

Three tech tiers everywhere: **Conventional → Magnetic/Gauss → Beam/Plasma**. Tiers gate on
the research in §2.1. Ranges/clips constant within a class. WotC tiers (Disruptor, Arashi,
Darklance, Darkclaw, Katana), Tactical Legacy weapons, and the WotC hero classes
(Reaper/Skirmisher/Templar) are excluded.

## 5.1 Primary weapons

**Assault Rifles** — Rookie, Specialist, Psi Op, Ranger · clip 4 · Medium range
| Tier | Damage | Crit dmg | Mod slots |
|---|---|---|---|
| Assault Rifle | 3–5 | +2 | 1 |
| Magnetic Rifle | 5–7 | +3 | 2 |
| Plasma Rifle | 7–9 | +4 | 2 |

**Shotguns** — Ranger only · clip 4 · Short range
| Tier | Damage | Crit dmg | Crit % | Mod slots |
|---|---|---|---|---|
| Shotgun | 4–6 | +3 | +10% | 1 |
| Shard Gun | 6–8 | +4 | +15% | 2 |
| Storm Gun | 8–10 | +5 | +20% | 2 |

**Cannons** — Grenadier only · clip 3 · Medium range
| Tier | Damage | Crit dmg | Shred* | Mod slots |
|---|---|---|---|---|
| Cannon | 4–6 | +2 | 1 | 1 |
| Mag Cannon | 6–8 | +3 | 2 | 2 |
| Beam Cannon | 8–10 | +4 | 3 | 2 |

\* with Shredder ability.

**Sniper Rifles** — Sharpshooter only · clip 3 · Long range · +10% crit · 2 AP to fire
| Tier | Damage | Crit dmg | Mod slots |
|---|---|---|---|
| Sniper Rifle | 4–6 | +2 | 1 |
| Gauss Rifle | 6–8 | +3 | 2 |
| Plasma Lance | 8–10 | +4 | 2 |

**Bolt Casters** `[AH]` — Rookie/Specialist/Psi Op/Ranger · clip 1, reload each shot · no mod slots · +15 aim · ignores Dodge · 20% Stun (50% vs Rulers)
| Tier | Damage |
|---|---|
| Bolt Caster | 6–8 |
| Magnetic Bolt Caster | 8–10 |
| Plasma Bolt Caster | 10–12 |

**Heavy Autocannons** `[SLG]` — SPARK only · clip 3 · Medium range (mirror Grenadier cannons)
| Tier | Damage | Shred |
|---|---|---|
| Heavy Autocannon | 4–6 | 1 |
| Helix Rail-Cannon | 6–8 | 2 |
| Elerium Phase-Cannon | 8–10 | 3 |

## 5.2 Secondary weapons

**Pistols** — Sharpshooter · no reload · Short-optimal
| Tier | Damage | Crit dmg |
|---|---|---|
| Pistol | 2–3 | +1 |
| Mag Pistol | 3–4 | +1 |
| Beam Pistol | 3–6 | +2 |

**Shadowkeeper Pistols** `[AH]` — Sharpshooter · +10 aim, +15% crit, grants **Shadowfall** (guaranteed hit; re-conceal on kill). One per playthrough.
| Tier | Damage | Crit dmg |
|---|---|---|
| Shadowkeeper | 2–3 | +1 |
| Enhanced Shadowkeeper | 3–4 | +1 |
| Powered Shadowkeeper | 3–6 | +2 |

**Swords** — Ranger · Melee · +20 aim
| Tier | Damage | Crit dmg | Crit % | Effect |
|---|---|---|---|---|
| Sword | 3–5 | +2 | +10% | — |
| Arc Blade | 4–6 | +2 | +15% | 25% stun/disorient |
| Fusion Blade | 5–7 | +3 | +20% | 100% set Burning |

**Axes** `[AH]` — Ranger · Melee · +20 aim · throwable once/mission (free action). One set per playthrough.
| Tier | Damage | Crit dmg | Crit % | Effect |
|---|---|---|---|---|
| Hunter's Axe | 4–6 | +2 | +10% | — |
| Ionic Axe | 5–7 | +2 | +15% | 25% stun/disorient |
| Fusion Axe | 6–8 | +3 | +20% | 100% set Burning |

**Grenade Launchers** — Grenadier · extends range/radius of thrown grenades
| Tier | +Range | +Radius |
|---|---|---|
| Grenade Launcher | +4 | +1 |
| Advanced Grenade Launcher | +5 | +2 |

**Psi Amps** — Psi Operative
| Tier | +Psi Offense |
|---|---|
| Psi Amp | +0 |
| Advanced Psi Amp | +20 |
| Alien Psi Amp | +40 |

**GREMLINs** — Specialist · drives Aid/Medical/Combat/Scan/Capacitor protocols + Hack
| Tier | Hack | Combat Protocol (org/rob) | Capacitor (org/rob) |
|---|---|---|---|
| GREMLIN | +0 | 2 / 4–5 | 3–6 / … |
| GREMLIN Mark II | +20 | 4 / 7–8 | 5–8 / … |
| GREMLIN Mark III | +40 | 6 / 10–11 | 7–10 / … |

**SPARK BITs** `[SLG]` — SPARK · Bombard/Nova + Hack (Nova ignores armor)
| Tier | Bombard | Nova | Hack |
|---|---|---|---|
| SPARK BIT | 3–4 | 6 | +0 |
| Plated BIT | 5–6 | 6 | +10 |
| Powered BIT | 7–8 | 6 | +20 |

## 5.3 Heavy Weapons (mounted on Heavy Armor / EXO·WAR·SPARK)

| Weapon | Damage | Crit dmg | Shred | Radius | Range | Notes | Source |
|---|---|---|---|---|---|---|---|
| Rocket Launcher | 4–7 | +2 | 2 | 4 | 27 | Needs direct path | EXO/WAR base |
| Flamethrower | 4–7 | +2 | — | 7 | 25 | Biological only, 20° cone, Burning + Panic | Exp. Heavy Weapon |
| Hellfire Projector | 6–9 | +2 | — | 7 | 25 | ″ (upgraded) | Exp. Powered Weapon |
| Shredder Gun | 6–9 | +1 | 2 | 12 | 25 | Ignores ½ armor, 20° cone | Exp. Heavy Weapon |
| Shredstorm Cannon | 8–11 | +2 | 4 | 12 | 25 | ″ (upgraded) | Exp. Powered Weapon |
| Plasma Blaster | 7–10 | +3 | — | 12 | 25 | Ignores 4 armor, straight line | Exp. Powered Weapon |
| Blaster Launcher | 7–10 | +2 | 3 | 6 | 45 | No LoS needed, paths around corners | Exp. Powered Weapon |

## 5.4 Skulljack (hacking tool)
Equipping a Skulljack with **Skullmining** researched gives **+25 Hack**. GREMLIN/BIT hack
bonuses do **not** apply to Skulljack/Skullmine attempts.

---

## Provenance / regenerate
All tables transcribed from `wiki_raw/*.txt` (MediaWiki API dumps, 2026-06-12). To refresh:
re-run the API fetch in PowerShell (`api.php?action=parse&page=<Title>&prop=wikitext`) with a
browser User-Agent — the direct `/wiki/` URLs 403. Prereq conflicts defer to `specs/tech-tree.md`.
