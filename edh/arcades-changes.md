# Arcades, the Strategist — Upgrade Changes (July 2026)

## Sources

- EDHREC commander page + JSON: https://edhrec.com/commanders/arcades-the-strategist /
  https://json.edhrec.com/pages/commanders/arcades-the-strategist.json — **22,510 decks**
- EDHREC average decklist: https://edhrec.com/average-decks/arcades-the-strategist
- Scryfall oracle text verified for **all 79 cards in the original list and all 18 add
  candidates** (named endpoint, July 2026). Zero fuzzy mismatches.

## Verified commander text

> **Arcades, the Strategist** {1}{G}{W}{U} — Legendary Creature — Elder Dragon 3/5
> Flying, vigilance
> Whenever a creature you control with defender enters, **draw a card**.
> Each creature you control with defender **assigns combat damage equal to its toughness**
> rather than its power and **can attack** as though it didn't have defender.

One-sentence axis: Arcades pays you a card for every defender that enters and turns
toughness into attack power — the deck wants **cheap, high-toughness defenders with
attached value**, mana to dump them fast, and one-sided wraths keyed to low power.

## Diagnosis

1. **The deck had 101 cards.** Illegal; nobody had noticed (same disease as Jetmir's 103).
2. **Lands: 33 vs the 35-card EDHREC average** — the user called this one, and the data
   agrees. Worse, there was no Sol Ring (85% inclusion) and no Arcane Signet (77%);
   Obelisk of Bant was the budget stand-in.
3. **Near-mandatory synergy walls missing:** Wall of Blossoms (83%, +0.75 synergy),
   Wall of Omens (82%, +0.74), Stalwart Shield-Bearers (81%, +0.75), Wall of Frost
   (71%, +0.66), Jeskai Barricade (60%, +0.56) — while vanilla 0/7s (Glacial Wall,
   Wall of Ice) with no text at all held their slots.
4. **A layer of card-neutral filler** with zero EDHREC presence: Aegis of the Heavens,
   High Stride, High Ground, plus a literal duplicate wrath (Destined Confrontation is a
   functional reprint of Slaughter the Strong at one more mana — the deck ran both).
5. **No premium removal:** Swords to Plowshares (64%) absent.

## Swaps (12 swaps + 1 straight cut = 101 → 100 cards, 33 → 35 lands)

| # | Out | In | Why (verified text + data) |
|---|-----|----|---------------------------|
| 1 | Glacial Wall (0/7, no text) | **Wall of Blossoms** | 83% incl., +0.75 synergy. ETB draw + Arcades draw = 2 cards for {1}{G} |
| 2 | Wall of Ice (0/7, no text) | **Wall of Omens** | 82% incl., +0.74. Same 2-card package in white |
| 3 | Fog Bank | **Stalwart Shield-Bearers** | Fog Bank's verified text prevents all damage **dealt by** it — it attacks for 0 under Arcades. SSB (81%, +0.75) gives all other defenders +0/+2 = +2 damage each |
| 4 | Gomazoa (attacks for 3) | **Wall of Frost** | 71% incl., +0.66. Attacks for 7, freezes anything it blocks |
| 5 | Wall of Deceit (no EDHREC presence) | **Jeskai Barricade** | 60% incl., +0.56. Flash ambush blocker; ETB bounces your own wall to re-buy its ETB **and** the Arcades draw |
| 6 | Obelisk of Bant (3 MV, taps for 1) | **Arcane Signet** | 77% incl. Same fixing, one mana cheaper |
| 7 | Spidersilk Net ({0}, +0/+2 reach) | **Sol Ring** | 85% incl. The strongest mana rock in the format for a do-almost-nothing equipment |
| 8 | Selesnya Charm (no EDHREC presence) | **Swords to Plowshares** | 64% incl. — the format's premium removal; the deck had none |
| 9 | Destined Confrontation | **Fell the Mighty** | Verified: exact functional reprint of Slaughter the Strong ({2}{W}{W} vs {1}{W}{W}) — the deck ran both. Fell the Mighty (57%, +0.52, top sorcery) is a *different* one-sided wrath: target Arcades (power 3) and destroy everything bigger |
| 10 | Journey of Discovery (lands to hand) | **Cultivate** | 47% vs no presence; puts a land onto the battlefield instead of hand |
| 11 | Aegis of the Heavens (one-shot +1/+7) | **Seaside Citadel** (land) | 62% incl., the top Bant tri-land. Land count 33→34 |
| 12 | High Stride (one-shot +1/+3) | **Access Tunnel** (land) | 33% incl., +0.30 synergy. Makes a power-≤3 wall unblockable — a kill button. Land count 34→35 |
| 13 | High Ground — **cut, no replacement** | — | Fixes 101→100. Redundant: Brave the Sands (57% incl., verified) grants the same extra block PLUS vigilance |
| 14 | Builder's Blessing | **Captain America's Shield** | Owner's pick, data-checked. Verified: {2} equip, indestructible, +0/+8 + vigilance, attack trigger taps a blocker. +8 attack under Arcades, survives wipes (Blessing's +0/+2 only worked while untapped — off exactly when walls attack). Already in 264/2,315 recent Arcades decks (~11%, brand-new card); strictly outclasses Slagwurm Armor (+0/+6, 21%) |

## Challenged, verified, and kept

- **Freed from the Real + Axebane Guardian** — verified infinite colored mana with 2+
  other defenders (Axebane taps for X = number of defenders; {U} untaps him). Coral
  Colony is the mill outlet. Deliberate combo package — untouched.
- **Bar the Door** (31% incl., +0.28), **Stoneskin** (45%, +0.42 — +0/+10 flash aura is
  10 attack under Arcades), **Meekstone** (49%, +0.45 — our walls have power ≤3 and
  don't care), **Brave the Sands** (57%, +0.53) — all looked like filler, all verified
  as real archetype staples. Kept.
- **Weathered Sentinels / Wall of Junk / The Walls of Ba Sing Se** — 58-63% inclusion
  in their eligible pools. Kept.
- **Fog Bank** is the mirror case: looks like a strong blocker, but verified text makes
  it the single most anti-Arcades card in the deck. Cut with confidence.

## Proof — why the new configuration wins harder

**Draw engine:** Wall of Blossoms, Wall of Omens, Jungle Barrier, and Jeskai Barricade
each now represent 2 cards (own ETB + Arcades trigger); Jeskai Barricade can bounce and
replay Blossoms/Omens for 2 more. The old list drew exactly 1 extra card off its walls
(Jungle Barrier).

**Damage math:** board of Arcades + Fortified Rampart (0/6) + Wall of Denial (0/8) +
Wall of Frost (0/7) + Stalwart Shield-Bearers (0/3). SSB gives the other three +0/+2 →
they attack for 8 + 10 + 9, SSB for 3, Arcades for 3 = **33 damage**, up from 24 without
SSB. Add Tower Defense (+0/+5 to all) mid-combat: **58 damage** — lethal on two players.

**Kill button:** The Pride of Hull Clade (0/15, casts near-free with a wall board) has
power ≤3, so Access Tunnel makes it unblockable: 15 unblockable commander-deck damage,
and its own activation ({2}{U}{U}) makes that connection **draw 15 cards**. With Captain
America's Shield equipped it's a 0/23 — 23 unblockable damage, 23 cards — and the Shield
doesn't break either enabler (power stays 0, so Tetsuko and Access Tunnel still apply).

**Mana:** 35 lands (EDHREC average) + Sol Ring + Arcane Signet + the existing dork/wall
ramp (Axebane, Battlement, Wall of Roots, Cryptolith Rite) — the deck now reliably
deploys Arcades turn 3 and multiple walls per turn after.

## Optional upgrades not applied

- **Tree of Redemption** (53%, 0/13 + life-total swap) — next wall upgrade over a vanilla
  body (verified, on the shortlist).
- **Sunscape Familiar** (75%, walls-adjacent cost reducer), **Vine Trellis** (60%),
  **Wall of Runes** (49%), **Shield Sphere** (42%, {0} 0/6), **Walking Bulwark** (44%,
  gives ANY defender the full Arcades treatment) — all verified and Bant-legal.
- **Dusk // Dawn** (65%) — third one-sided wrath plus mass wall-reanimation.
- **Counterspell** (55%) — if the meta calls for it, Simic Charm is the weakest
  remaining instant.
- Land polish: **Glacial Fortress / Sunpetal Grove** (52% / 48% check-lands, nearly
  always untapped with 25 basics) over Canopy Vista / Prairie Stream if more untapped
  sources are wanted.
