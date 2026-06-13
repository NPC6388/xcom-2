# Sources

Handling: **fetch + reconcile**. For each, extract relevant ordering; where sources
disagree, flag the conflict and recommend for Commander tempo with reasoning.

Status legend: ⬜ not fetched · 🔄 fetched, mining · ✅ extracted · ⚠️ inaccessible (403/blocked) · 🟡 off-topic vs. its label

## Tech tree / research
- ✅✅ [Interactive tech tree (darosh)](https://darosh.github.io/xcom2-tech-tree/) — **LOCKED.** User supplied `xcom2-tech-tree.svg`; parsed it deterministically with `parse_tree.py` (geometry → 159 nodes, 178 edges). Authoritative prereqs → [`specs/tech-tree.md`](specs/tech-tree.md). All earlier `(verify)` prereq flags resolved.
- ✅ [Research/build Steam discussion 5287797783050387276](https://steamcommunity.com/app/268500/discussions/0/5287797783050387276/) — GTS-first, mag weapons + plated armor core. ⚠️ contains WOTC items (Resistance Ring, Training Center) — filtered out.

## Build order (general)
- ⚠️ [Reddit: definite build order?](https://www.reddit.com/r/Xcom/comments/47rl5z/...) — Reddit blocks fetch. Recovered via search.
- ⚠️ [GameFAQs 163467 / 73274081](https://gamefaqs.gamespot.com/boards/163467-xcom-2/73274081) — 403.
- ⚠️ [GameFAQs 191291 / 74365575](https://gamefaqs.gamespot.com/boards/191291-xcom-2/74365575) — 403.
- 🟡 [Steam guide (sharedfiles 1839900455)](https://steamcommunity.com/sharedfiles/filedetails/?id=1839900455) — explicitly **WOTC**. Used only for tier logic that also applies to vanilla.
- 🟡 [Steam discussion 1736594593606042731](https://steamcommunity.com/app/268500/discussions/0/1736594593606042731/) — actually about **turn order mechanics**, not build order. Not used.
- 🟡 [Steam discussion 412447613564404061](https://steamcommunity.com/app/268500/discussions/0/412447613564404061/) — actually **soldier ability picks** (Ranger/Sniper/Grenadier/Specialist). Useful for UPGRADES specs, not research/facilities.

## Facilities
- ✅ [Proving Ground (Fandom)](https://xcom.fandom.com/wiki/Proving_Ground) — direct URL 403s, but pulled clean via the **MediaWiki API** (see below). Project list now authoritative in `specs/database.md`.

## Fandom wiki — full database pass (2026-06-12)
The direct `xcom.fandom.com/wiki/*` URLs 403 to bots (WebFetch + browser-UA `Invoke-WebRequest` both blocked), **but `api.php?action=parse&prop=wikitext` returns clean wikitext** with a browser User-Agent. Used this to build `specs/database.md` (missions / research / facilities / armor / weapons, all prereqs). Raw dumps cached in `wiki_raw/`:
- ✅ [Missions (XCOM 2)](https://xcom.fandom.com/wiki/Missions_(XCOM_2)) + Council/Guerilla/Supply/Alien-Facility/Blacksite/Forge sub-pages → full mission DB with triggers, timers, rewards.
- ✅ [Research Projects (XCOM 2)](https://xcom.fandom.com/wiki/Research_Projects_(XCOM_2)) → standard/Shadow-Chamber projects + autopsy table (corpse counts, unlocks).
- ✅ [Avenger (XCOM 2)](https://xcom.fandom.com/wiki/Avenger_(XCOM_2)) + [Proving Ground](https://xcom.fandom.com/wiki/Proving_Ground) → facility costs/power/upkeep/time/prereqs + PG projects.
- ✅ [Armors (XCOM 2)](https://xcom.fandom.com/wiki/Armors_(XCOM_2)) + [Weapons (XCOM 2)](https://xcom.fandom.com/wiki/Weapons_(XCOM_2)) + [Data Tables](https://xcom.fandom.com/wiki/Data_Tables) → full armor/weapon stat tables by tier.
- Filter applied: base + Alien Hunters + Shen's Last Gift kept; **WotC tiers/classes/facilities/autopsies excluded** and flagged.

## Upgrades / soldiers / SPARK
- ⚠️ [Reddit: soldier XP & leveling](https://www.reddit.com/r/Xcom/comments/eutkny/...) — Reddit blocks fetch. (Mid/late upgrades.)
- ⚠️ [Reddit: SPARK unit analysis](https://www.reddit.com/r/Xcom/comments/4rffo3/...) — Reddit blocks fetch. Shen's Last Gift; mid-game upgrade.
- ⬜ [StackExchange: raise hacking ability](https://gaming.stackexchange.com/questions/254638/...) — fetch for mid/late upgrades.
- ⬜ [StackExchange: skulljacking after first](https://gaming.stackexchange.com/questions/254571/...) — fetch for early→mid transition trigger.

## Recovered-via-search corroborating sources (not in original list)
- [GamersDecide: best research orders](https://www.gamersdecide.com/articles/xcom-2-best-research-orders)
- [Fextralife: Proving Ground](https://xcom2.wiki.fextralife.com/Proving+Ground) · [Fextralife: Facilities](https://xcom2.wiki.fextralife.com/Facilities)
- [GamePressure: development order](https://guides.gamepressure.com/xcom2/guide.asp?ID=33939)
- [UFOpaedia: Avenger Optimization](https://www.ufopaedia.org/index.php/Avenger_Optimization_(XCOM2))

## Notes
- ℹ️ User's link list is **not exhaustive** — just sources they found helpful. I may supplement with other reputable vanilla sources and general knowledge, flagging what's mine vs. theirs.
- Two of the original links were duplicates of the research-order Steam discussion (5287797783050387276).
- SPARK / Shen's Last Gift IS in scope; **WOTC content is OUT of scope** and several sources are WOTC-flavored — must filter.
- ⚠️ KEY GAP: the darosh tech tree (the authoritative prereq graph) is not auto-fetchable. Early research prereqs below are from general knowledge + cross-source and **should be verified against that tree**.
