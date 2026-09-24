# Najeela, the Blade-Blossom — cEDH build from scratch

This is a new 100-card paper Commander deck, not an upgrade of an existing list. Built directly
off real, recent competitive cEDH tournament results per project convention (mtgtop8 first).

## Sources
- **mtgtop8 cEDH — primary source, per instruction.** Najeela has a real, active cEDH archetype
  page: https://www.mtgtop8.com/archetype?a=1211. Three full decklists were pulled and
  cross-referenced:
  1. **Chavadon Nunthapusithanon — 1st place, Commander Royale TH, 2026-08-30**
     https://mtgtop8.com/event?e=90313&d=885560&f=cEDH — most recent result, and the one this
     build is based on directly (see "Why this list" below).
  2. **Donald Brorson — 2nd place, cEDH monthly GOLD (August), 2026-08-22**
     https://mtgtop8.com/event?e=89961&d=882778&f=cEDH
  3. **Jefe — top 17-32, 105-player cEDH event, 2026-01-17**
     https://mtgtop8.com/event?d=801550&e=79198&f=cEDH
- **Local card DB** (`.claude/scripts/card_db.py`) — every one of the 100 cards verified for
  oracle text, color identity, and Commander-format legality before being written to the list.
  All 100 returned `"found": true`, `"commander": "legal"`, and a color identity that is a
  subset of Najeela's WUBRGB/G/R/U/W identity.

### Why this list (methodology note)
The three decklists overlap heavily — 11 creatures, 17 instants/sorceries, and 8 artifacts/
enchantments appear in **all three** independent tournament results, confirming a stable
"Najeela Breach" cEDH shell. List #1 (Chavadon, 1st place, most recent event) is a strict
superset of that 3-way consensus core and is both the newest and the highest-placing result
of the three, so it was used as the deck directly rather than hand-splicing pieces from all
three — cross-checking confirmed it isn't missing anything the other two consider essential.

## Verified commander text
**Najeela, the Blade-Blossom** — {2}{R}, Legendary Creature — Human Warrior, 3/2, color
identity **B/G/R/U/W (five-color)**:
> Whenever a Warrior attacks, you may have its controller create a 1/1 white Warrior creature
> token that's tapped and attacking.
> {W}{U}{B}{R}{G}: Untap all attacking creatures. They gain trample, lifelink, and haste until
> end of turn. After this phase, there is an additional combat phase. Activate only during
> combat.

Axis the deck scales on: every attacking Warrior makes another attacking Warrior, and a flat
5-mana (one of each color) activation chains that into another full combat phase with the whole
team hasty, trampling, and lifelinking. The more mana you can generate in a turn, the more
combats you get — which is exactly the "infinite combat" reputation this commander has.

## Deck plan
This is **not** a creature-beatdown Warriors tribal deck — the tournament-proven build is a
fast-mana/tutor control shell (16 creatures, 43 instants/sorceries, 15 artifacts/enchantments,
25 lands) that assembles one of three verified win conditions, protected by a full suite of
free/near-free interaction, and closes the game the same turn it goes off.

### Win condition 1 — Najeela's own ability chained into extra combats
With abundant mana (from the ritual package below, or from Treasures off Grim Hireling/Ragavan/
Lotho combat triggers), repeatedly paying {W}{U}{B}{R}{G} untaps the whole attacking team, grants
trample/lifelink/haste, and adds another combat phase. Each combat, every attacking Warrior
(Najeela included) makes a new tapped-and-attacking token, so the attacker count and total damage
compound every phase — this is the literal, oracle-text "infinite combat" line the deck is famous
for, not a metaphor.

### Win condition 2 — Thassa's Oracle + Demonic Consultation / Tainted Pact
`Demonic Consultation` (verified): name a card, exile the top 6, dig until you hit it or your
library runs out. Naming a card you know isn't in the deck exiles the **entire library**.
`Thassa's Oracle` (verified): on ETB, look at the top X cards (X = blue devotion) — if X ≥ cards
remaining in library, **you win the game**. With an empty library, X ≥ 0 is always true. This is
a board-state-independent win: it doesn't care how many opponents are alive or what they control.

### Win condition 3 — Underworld Breach + fast-mana loop into a storm/mill or into win 1/2
`Underworld Breach` (verified): every nonland card in your graveyard gains escape for its mana
cost + exile 3 other graveyard cards. Cheap 0-mana artifacts already in the yard (Lotus Petal,
Chrome Mox) or rituals (Dark Ritual, Culling the Weak) can be re-cast this way for a net mana
gain each time, fueled by the graveyard rather than your hand. This doesn't need to be
mathematically infinite to win — it generates far more mana than the game has answers for in one
turn, which either fuels enough `Brain Freeze` storm copies to mill an opponent out, or just pays
for repeated Najeela activations (win 1) or an Ad Nauseam into win 2.

## The package, by role
- **Fast mana (10):** Sol Ring, Mana Vault, Arcane Signet, Fellwar Stone, Chrome Mox, Mox Amber,
  Mox Diamond, Lotus Petal, Lion's Eye Diamond, Ancient Tomb.
- **Rituals (4):** Dark Ritual, Culling the Weak, Simian Spirit Guide, Elvish Spirit Guide
  (the latter two exile from hand for mana — effectively free, one-shot rituals).
- **Tutors (9):** Demonic Tutor, Vampiric Tutor, Mystical Tutor, Enlightened Tutor, Worldly
  Tutor, Eladamri's Call, Diabolic Intent, Wishclaw Talisman, Chord of Calling.
- **Free/near-free interaction (10):** Force of Will, Force of Negation, Fierce Guardianship,
  Deflecting Swat, Deadly Rollick, Flusterstorm, Mental Misstep, Pact of Negation, An Offer You
  Can't Refuse, Swan Song.
- **Protection for the combo turn (3):** Silence, Angel's Grace, Final Fortune.
- **Card advantage (5):** Rhystic Study, Mystic Remora, Esper Sentinel, The One Ring,
  Necropotence.
- **Combat-damage value creatures (7):** Ragavan, Grim Hireling, Lotho, Voice of Victory,
  Orcish Bowmasters, Samut, Derevi — all generate Treasures, cards, or extra attackers off the
  same combat step Najeela wants to be in anyway.
- **Manabase (25 lands, 0 basics):** 7 fetches (Arid Mesa, Marsh Flats, Misty Rainforest,
  Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills) targeting 7 original duals
  (Badlands, Plateau, Savannah, Scrubland, Taiga, Tundra, Underground Sea) plus 3 shocklands
  (Breeding Pool, Overgrown Tomb, Steam Vents) — every fetch has a same-color-pair target even
  with zero basics in the deck. Utility lands (Ancient Tomb, Cavern of Souls, City of Brass,
  Command Tower, Exotic Orchard, Gaea's Cradle, Gemstone Caverns, Mana Confluence) round it out.
  **Known trade-off, inherited from the tournament list as-is:** zero basic lands means this
  deck is exposed to nonbasic-land hate (Blood Moon, Back to Basics) — the real-world Aug 2026
  1st-place pilot accepted that risk in exchange for maximum fixing speed, so this build does too.

## Multiplayer vs. 1-on-1
- **Multiplayer (the deck's primary design target, per the tournament pilots it's built from):**
  the free-interaction suite (Force of Will, Fierce Guardianship, Deflecting Swat, Flusterstorm,
  Mental Misstep, Swan Song, Pact of Negation) is what lets this deck protect a combo turn against
  a full pod's worth of answers, and win condition 2 (Thassa's Oracle) doesn't care how many
  opponents are still developing boards — it just needs one clean window.
- **Against a single opponent:** the same shell holds up — there's simply less total interaction
  to play around, so the combo turn usually comes online faster. The one card worth flagging for
  a 1v1 read is `Final Fortune` / `Ad Nauseam`-adjacent lines where you take an extra turn and
  then lose unless you've already won — against one opponent there's no "someone else eats the
  loss" cushion a pod sometimes gives, but the deck's actual finishers (Najeela combats, Thassa's
  Oracle) don't depend on Final Fortune, so this is a minor, situational tool, not a load-bearing
  piece.

## Proof — a representative Najeela combat line
Once Najeela and two prior Warrior tokens are attacking (3 attackers, all Warriors), and mana is
flowing from the fast-mana/Breach package: paying {W}{U}{B}{R}{G} untaps all 3, grants trample/
lifelink/haste, and starts a new combat. Najeela's static trigger fires once per attacking
Warrior, so all 3 create a new tapped-and-attacking token — 6 attackers. Paying WUBRG again
untaps and re-triggers all 6 attacking Warriors → 6 more tokens join → **12 attackers**, all
trampling and lifelinking. Each additional {W}{U}{B}{R}{G} activation **doubles** the attacking
Warrior count (n → 2n) while granting trample+lifelink+haste to the whole team — three
activations turns 3 attackers into 24, more than enough trampling/lifelink damage to end a game
at any commander life total, and the lifelink cushions against a race back in the games where the
combo doesn't fully close it out.

## Cross-validation note
The January 2026 (Jefe) and August 2026 #2 (Brorson) results diverge from the base list on a
handful of slots — e.g. Jefe runs `Rite of Flame` and `Cabal Ritual` where the base list runs
`Fire Covenant` and an extra tutor/interaction slot; Brorson runs a heavier land count (29) with
`Chatterfang, Squirrel General` and `Opposition Agent`. None of these are clear upgrades over the
base list's choices — they read as metagame calls (more anti-hate pieces, a slower manabase) by
individual pilots rather than consensus-best swaps, so per the "why this list" note above, the
most recent/highest-placing single source was kept as-is rather than hand-splicing.
