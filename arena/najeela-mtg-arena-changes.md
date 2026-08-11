# Najeela, the Blade-Blossom — MTG Arena upgrade

## Sources
- mtgtop8 cEDH: https://mtgtop8.com/format?f=cEDH — checked first per methodology. **No Najeela decks
  found** in the indexed cEDH event archive (searched both as commander and as a card in the 99).
  Finding: Najeela has no recorded tournament footprint on mtgtop8; her reputation as a combo
  commander is a Commander-community/EDHREC phenomenon, not a competitive-metagame one.
- EDHREC: https://edhrec.com/commanders/najeela-the-blade-blossom,
  https://json.edhrec.com/pages/commanders/najeela-the-blade-blossom.json,
  https://edhrec.com/average-decks/najeela-the-blade-blossom — 13,821 decks tracked, rank #143.
- Scryfall API (`cards/named`, `cards/search`) — oracle text and Arena-printing verification for
  every card touched in this pass.
- Format rules: MTG Arena's Historic Brawl is 1-on-1 at **25 starting life** (confirmed via web
  search, multiple sources) — used for the proof-of-damage calculation below.

## Verified commander text
**Najeela, the Blade-Blossom** — {2}{R}, Legendary Creature — Human Warrior, 3/2, color identity
**W/U/B/R/G (five-color)**:
> Whenever a Warrior attacks, you may have its controller create a 1/1 white Warrior creature
> token that's tapped and attacking.
> {W}{U}{B}{R}{G}: Untap all attacking creatures. They gain trample, lifelink, and haste until
> end of turn. After this phase, there is an additional combat phase. Activate only during combat.

Axis the deck scales on: **every Warrior that attacks makes another attacking Warrior**, and a
flat 5-mana activation (one of each color) can chain that into extra combat phases. The deck's
job is to (a) get Warriors attacking, (b) generate WUBRG cheaply/repeatedly, and (c) close the
game once the loop is running.

## Methodology note — how Arena legality was verified
Every candidate card was checked against a real Arena printing (`game:arena` search across ALL
printings, not just the default one — avoids false negatives) and against `legalities.brawl`
specifically, not paper `legalities.commander` (avoids false positives from paper-only staples).
Two traps this caught on this pass:
- **Skullclamp** looked like the single best token-payoff for this deck (it kills a 1-toughness
  token as a state-based action on attach, drawing 2) — it has **no Arena printing and no Alchemy
  version**. Confirmed absent, not added, despite being an obvious EDHREC-style recommendation.
- **Deflecting Swat** and **Fierce Guardianship** both have real Arena printings and read as
  paper-legal/Competitive-Brawl-legal, but are **explicitly banned in Arena's standard Historic
  Brawl**. Neither was added.

Per project convention, Alchemy-exclusive cards would have been fair game if any fit — none of
the final adds needed one; all six went in on real paper-matching Arena printings.

**Per your confirmation:** the current 99 cards in the deck were not re-swept — you exported this
list directly from the Arena client, which is ground truth that everything already in it is owned
and legal. Only the new candidate adds below were checked.

**Timing note:** you flagged that **Orcrist, Goblin-cleaver releases on Arena tomorrow
(2026-08-11)**, one day after this session. It's Arena-legal and importable into this list now;
you just won't be able to cast it in a live match until the set goes live.

## Diagnosis
- **Mana base was bloated for a 1v1 aggro-combo shell.** 40 lands, *plus* Arcane Signet,
  Chromatic Lantern, Cultivate, Farseek, and Rampant Growth on top — well above EDHREC's own
  35-land average for this commander, in a deck whose commander wants to be attacking by turn 3-4,
  not durdling on mana. Rampant Growth in particular (`Search your library for a basic land card,
  put it onto the battlefield tapped, then shuffle`) is strictly the same effect as Cultivate for
  1 less mana and no card to hand — Cultivate already covers that role better.
- **Card advantage was thin outside combat-damage payoffs.** The Great Henge, Raiders' Spoils, and
  Professional Face-Breaker are all "deal combat damage first" draw — good backup, bad if the
  board gets swept or removal snipes Najeela before she connects. No opponent-taxed draw engine
  (Rhystic Study/Mystic Remora-style) was in the 99 at all.
- **Reliquary Tower and Herald's Horn are both measurably weak here per EDHREC's own synergy
  data** (-0.120 and -0.016 synergy respectively, among the lowest of any card in their
  categories) — Reliquary Tower's "no maximum hand size" barely matters in a deck that wants to
  dump its hand and attack, not hoard cards.
- **Tribute to the World Tree costs {G}{G}{G}** — a genuinely awkward ask in a 5-color manabase
  that's already stretched thin fixing WUBRG for Najeela's own ability.
- **Banner of Kinship** is a 5-mana enchantment-adjacent artifact that does nothing the turn it
  lands and only rewards a creature type you already committed to before casting it — slow for
  what this deck wants to be doing on turn 5.
- **Haste/protection check (Arena-specific, 1v1 clock):** only 2 haste sources in the 99 (Devilish
  Valet has it natively, Ogre Battledriver grants it on ETB) plus Najeela's own ability, which only
  grants haste to creatures *already attacking* — no proactive way to protect Najeela herself or
  push a freshly-cast threat into service the same turn outside combat. This is a real gap for a
  1v1 clock where there's no third player's turn to absorb summoning sickness.

## Swap table

| # | Out | In | Why (verified) | Arena legality |
|---|---|---|---|---|
| 1 | Reliquary Tower (land, EDHREC synergy -0.120) | **Orcrist, Goblin-cleaver** {3} artifact equipment, +2/+2 & trample; on combat damage, choose a creature type and make a Treasure per creature you control of that type | Requested add. Equip Najeela (or any Warrior), choose "Warrior" on the damage trigger — every attacking Najeela-made token counts, so this converts the token swarm directly into Treasures, which fund the very next WUBRG activation. Also trims the land count toward the 35-average benchmark. | LEGAL — HOB 177, brawl: legal |
| 2 | Herald's Horn (artifact, EDHREC synergy -0.016) | **Rhystic Study** — "Whenever an opponent casts a spell, you may draw a card unless that player pays {1}" | Closes the card-draw-engine gap; in 1v1 a single opponent either taxes every spell by {1} or you draw off nearly everything they do all game — undiluted compared to a 4-player pod where 3 opponents share the tax. | LEGAL — FCA 31, brawl: legal |
| 3 | Banner of Kinship (5-mana do-nothing-on-ETB artifact) | **Ignoble Hierarch** {G} 0/1, Exalted, {T}: add B/R/G | Replaces a slow anthem with a turn-1 mana dork that fixes 3 of Najeela's 5 colors and adds a body to a deck that wants a wide, cheap board fast. | LEGAL — AA2 14 (Arena Anthology 2 printing), brawl: legal |
| 4 | Tribute to the World Tree ({G}{G}{G}, narrow color ask) | **Smothering Tithe** — "Whenever an opponent draws a card, that player may pay {2}. If they don't, you create a Treasure." | Fires on every opponent draw step for the whole game (not just combat-damage-gated), directly refuels the mana this deck burns activating Najeela's ability. | LEGAL — RNA 22, brawl: legal |
| 5 | Rampant Growth (strictly worse than Cultivate, already in the 99) | **Lightning Greaves** — "Equipped creature has haste and shroud," Equip {0} | Directly answers the haste/protection gap: puts a freshly cast threat (or a recast Najeela) into combat the same turn, and shroud protects her from removal the instant before/after a WUBRG activation — the single point of failure the whole combo depends on. | LEGAL — MRD 199, brawl: legal |

Net effect: lands 40 → 39, and the deck trades three of its weakest, most passive cards
(EDHREC-confirmed low/negative synergy) plus one strictly-dominated ramp spell for two premium
card-advantage engines, a color-fixing 1-drop, a haste/protection piece, and the requested Orcrist
package. Every other card in the 99 was left untouched — no forced symmetry cuts.

## Challenged and kept
- **Cryptolith Rite** was a candidate cut on "too much redundant ramp" grounds, but its verified
  text (`Creatures you control have "{T}: Add one mana of any color"`) is not textually redundant
  with the land-tutor spells — it's a repeatable engine that turns Najeela's Warrior-token swarm
  into a WUBRG-producing mana base every combat. Kept.
- **Aven Wind Guide** was flagged mid-research as a possible color-identity violation (U/W) under
  an assumption that Najeela is Mardu+Green (no blue). Cross-checked against two independent
  sources (Scryfall oracle text and EDHREC's own commander page) — **Najeela is five-color
  (WUBRG)**, so blue is fully legal. False alarm, not cut.
- **Farseek** looked redundant with Rampant Growth/Cultivate at a glance; verified text shows it
  can also fetch nonbasic lands that merely *have* a Plains/Island/Swamp/Mountain type (duals,
  shocks, triomes), which the other two cannot — kept as-is, not textually redundant.

## Proof — a concrete kill line at 25 life
Historic Brawl is 1v1 at 25 starting life. A representative turn-5 line with the new package:
Najeela (3/2) equipped with Orcrist (+2/+2/trample → 5/4) attacks alongside two prior Warrior
tokens. All three are Warriors, so Najeela's own trigger fires three times → three more 1/1
tapped-and-attacking Warrior tokens join, for 6 total attackers, all Warriors. Najeela's combat
damage (trampling through blockers or unblocked) triggers Orcrist — choosing "Warrior" creates
**6 Treasures** (one per Warrior you control). Those 6 Treasures produce 6 mana of any color,
comfortably covering the {W}{U}{B}{R}{G} activation cost with one floating. Activating: all 6
attackers untap, gain trample/lifelink/haste, and an additional combat phase begins — in which
the newly-created tokens (now hasty) can also attack, triggering Najeela again and generating
more Orcrist Treasures to fund the next activation. Six trampling/lifelink attackers alone already
clear a meaningful chunk of a 25-life opponent in the first extra combat; the loop typically only
needs to sustain two or three cycles before lethal trample damage exceeds 25, and lifelink cushions
against any race back.

## Optional upgrades not applied
Confirmed Arena-legal but left out of this pass (budget of changes kept tight and 1:1-justified;
worth considering in a future upgrade round):
- **Esper Sentinel** (J21 75) — another opponent-taxed draw engine, would have been swap #6 if a
  clean sixth cut had verified out; nothing else in the 99 justified removal on checked oracle text.
- **Mystic Remora** (TLE 16), **Champion of Lambholt** (JMP 383), **Ragavan, Nimble Pilferer**
  (FCA 43 — note: `competitivebrawl: banned`, fine for standard Historic Brawl only), **Grim
  Hireling** (HBG 158), **Voice of Victory** (TDM 33), **Ares, God of War** (MSH 202),
  **Sevinne's Reclamation** (MH3 267), **Diabolic Intent** (BRO 89), **Eldritch Evolution**
  (SIR 195) — all verified Arena-legal, all reasonable future includes.
- Notably absent from Arena entirely, so ruled out for good: **Bramblewood Paragon**, **Herald of
  Dromoka**, **Mindblade Render**, **Rushblade Commander**, **Blood-Chin Rager**, **Druids'
  Repository**, **Mirri, Weatherlight Duelist**, **Simian Spirit Guide** — several of these are
  strong paper Warrior-tribal staples with no Arena/Alchemy printing at all.
