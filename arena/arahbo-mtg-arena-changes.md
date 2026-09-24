# Arahbo, the First Fang — MTG Arena build (from scratch)

## Sources

- Commander oracle text: local `card_db.py` (Postgres cache of Scryfall `oracle-cards`), cross-checked
  live against Scryfall (`cards/named` + `cards/search`, all 5 printings of the card).
- Competitive record: https://mtgtop8.com/format?f=cEDH (searched for "Arahbo") — no hits.
- Archetype data: `edhrec-researcher` agent → https://edhrec.com/commanders/arahbo-the-first-fang
  (3,366 decks, commander rank #773).
- Card legality/pool: `card-verifier` agent (oracle text, 78 candidates across 3 batches) and
  `arena-legality-checker` agent (real Arena/Brawl availability + set/collector numbers, same 78
  candidates, run in parallel with the verifier).

## Critical correction before any build work

The name "Arahbo, the First Fang" is easy to confuse with **Arahbo, Roar of the World**
(Commander 2017), a Naya (RGW) Cat commander. They are two different cards. **Arahbo, the First
Fang** is a Foundations (FDN, 2024) card and is **mono-White**:

> **Arahbo, the First Fang** — {2}{W}, Legendary Creature — Cat Avatar, 2/2
> Other Cats you control get +1/+1.
> Whenever Arahbo or another nontoken Cat you control enters, create a 1/1 white Cat creature
> token.

Verified against the local DB and live Scryfall (all 5 printings — FDN 2/294/363/442, PFDN 2s —
carry identical text and color identity `["W"]`). This deck is built as mono-White from the
ground up; there is no green or red in the manabase or spell base.

- **cEDH presence: none.** Confirmed absent from mtgtop8's cEDH metagame page — this is a
  casual/mid-power tribal commander, not a competitive combo shell. "Competitive" for this build
  means a tightly curved, high-consistency mono-White Cats aggro/tokens deck optimized for 1-on-1
  Arena Brawl, not a cEDH line.
- **EDHREC**: 3,366 decks, rank #773. Dominant themes: Cats (528 decks), Tokens (176), Lifegain
  (138), +1/+1 Counters (75), Aggro (41), Anthems (18).

## Game plan

Arahbo does two things every time a nontoken Cat (including itself) enters: it hands out a
permanent +1/+1 to your other Cats, and it drips out 1/1 Cat tokens. The deck is built to
maximize both halves:

1. **Go wide fast** — a curve stacked with 1–3 mana Cats (Savannah Lions, Sacred Cat, Ajani's
   Pridemate, Helpful Hunter, Prideful Parent, Skyknight Squire, Brimaz) that each add a body and
   often another token on entry.
2. **Payoff the tokens** — Divine Visitation (every token becomes a 4/4 flying vigilance Angel),
   Anointed Procession (double every token), Intangible Virtue and the tribal anthem artifacts
   (Heraldic Banner, Patchwork Banner, Banner of Kinship, Vanquisher's Banner) turn the flood of
   1/1s into real damage.
3. **Lifegain sub-theme** — Sacred Cat, Ajani's Sunstriker-style lifelink bodies (Regal Caracal,
   Felidar Savior, Leonin Warleader's tokens), Ajani's Welcome, and Ajani's Pridemate/Qala reward
   every life-gain trigger with growth; Felidar Sovereign is a real alternate win condition off
   the same lifegain the deck already generates.
4. **Undiluted 1v1 removal and protection** — real unconditional exile effects (Swords to
   Plowshares, Path to Exile, Winds of Abandon, Cast Out, Portable Hole, Prison Realm) instead of
   multiplayer-scaling cards, plus a protection suite (Giver of Runes, Mother of Runes, Selfless
   Spirit, Swiftfoot Boots, Unbreakable Formation, Akroma's Will, Ephemerate) so the token board
   survives combat tricks and sweepers. No symmetric board wipes were included — this deck is the
   beatdown, so a Wrath effect would only ever hurt it more than the single opponent.

## The Sol Ring lesson — cards that don't exist on Arena

Every one of the 78 candidates pulled from EDHREC's top inclusion/synergy lists and generic
mono-White staples was run through `arena-legality-checker` against live Scryfall (`games` field
across every printing, not just the newest). Several genuine EDHREC staples for this commander
are simply **absent from Arena's digital card pool** — not banned, just never printed there:

- **Sol Ring** (82% inclusion on EDHREC!), **White Sun's Zenith** (58% inclusion), **Path of
  Ancestry** (47% inclusion), **Idol of Oblivion**, **Windbrisk Heights**, **Myriad Landscape**,
  **War Room**, **Folk Hero**.
- Also excluded for real Arena reasons found mid-check: **Ocelot Pride** (the paper card is
  `brawl: not_legal` on Arena — Alchemy replaced it with the digital-only `A-Ocelot Pride`, which
  *is* legal; left out to keep the list free of rebalanced cards) and **Flawless Maneuver**
  (exists on Arena but is explicitly `brawl: banned`, even though `competitivebrawl: legal`).
- Ten more EDHREC-average-decklist creatures have no Arena printing at all and were cut on sight:
  Healer of the Pride, Enlightened Ascetic, Alms Collector, Whitemane Lion, Ajani's Sunstriker,
  Trained Caracal, Skyhunter Strike Force, Prava of the Steel Legion (also a Partner card, which
  doesn't fit a normal singleton Brawl build), Oreskos Explorer, Kemba, Kha Regent.
- **Sunblast Angel** (a one-sided-feeling sweeper vs. tapped creatures) — also genuinely absent
  from Arena.

None of these made the final 100. Every classic false-negative case (a card whose *default*
cached printing is paper-only but which has a real Arena reprint) was also caught by searching
across all printings instead of trusting one: **Esper Sentinel** (J21, not the cached MH2),
**Giver of Runes** (HA7, not MH1), **Mother of Runes** (AA2, not CLB), **Selfless Spirit** (SIR,
not SOC), **Felidar Sovereign** (J25, not BFZ), **Brimaz, King of Oreskos** (J25, not BNG),
**Mind Stone** (HA1, not MBC), **Ephemerate** (MAR, not MH1), **Divine Visitation** (GRN, not
MSC), **Swords to Plowshares** (SPG, not MSC), **Restoration Angel** (J21, not AVR).

## Deck composition (99 + commander)

| Category | Count |
|---|---|
| Creatures | 32 |
| Instants | 7 |
| Sorceries | 2 |
| Enchantments | 10 |
| Artifacts | 10 |
| Planeswalkers | 2 |
| Nonbasic lands | 4 |
| Basic Plains | 32 |
| **Total lands** | **36** |
| Commander | 1 |
| **Deck total** | **100** |

**Creatures (32)**: Savannah Lions, Sacred Cat, Ajani's Pridemate, Qala Ajani's Pridemate,
Helpful Hunter, Prideful Parent, King of the Pride, Skyknight Squire, Regal Caracal, Brimaz King
of Oreskos, Jazal Goldmane, Leonin Warleader, Felidar Savior, Cat Collector, Adorned Pouncer,
Lion Sash, Leonin Vanguard, Kutzil's Flanker, Felidar Sovereign, Esper Sentinel, Giver of Runes,
Mother of Runes, Selfless Spirit, Felidar Cub, Lionheart Glimmer, Kemba Kha Enduring, Restoration
Angel, Thalia Guardian of Thraben, Monastery Mentor, Elite Spellbinder, Ranger-Captain of Eos,
Angel of Invention.

**Interaction (7 instants + 3 exile-enchantments/artifact)**: Swords to Plowshares, Path to
Exile, Winds of Abandon, Cast Out, Portable Hole, Prison Realm, Stroke of Midnight — seven
unconditional-or-near-unconditional answers, all exile- or destroy-based, none symmetric.

**Protection (7)**: Giver of Runes, Mother of Runes, Selfless Spirit, Swiftfoot Boots,
Unbreakable Formation, Akroma's Will, Ephemerate.

**Token payoffs (5)**: Divine Visitation, Anointed Procession, Intangible Virtue, Cathars'
Crusade, Caretaker's Talent.

**Tribal anthems / cost reducers (6)**: Heraldic Banner, Patchwork Banner, Banner of Kinship,
Vanquisher's Banner, Herald's Horn, Pearl Medallion, Rally the Ranks.

**Lifegain payoffs (2)**: Ajani's Welcome, Authority of the Consuls.

**Ramp/rocks (2)**: Arcane Signet, Mind Stone.

**Card advantage/tutor (1)**: Idyllic Tutor (fetches Divine Visitation).

**Planeswalkers (2)**: Ajani, Caller of the Pride; Ajani, Strength of the Pride.

**Lands (36)**: 32 Plains + Three Tree City (taps for colored mana off your Cat count), Cavern of
Souls (choose Cat — uncounterable Cat spells, relevant vs. blue interaction on Arena), Minas
Tirith (untapped off a legendary creature — Arahbo, Brimaz, Kemba, Thalia, Ranger-Captain, Jazal,
Qala all qualify), Animal Sanctuary (counter sink hitting Cats directly).

## A concrete turn

Board: Arahbo (2/2, untouched so far — its own anthem doesn't buff itself), Intangible Virtue in
play, one pre-existing 1/1 Cat token. Cast Regal Caracal (5 mana, 3/3):

- Regal Caracal enters → its own ETB creates two 1/1 lifelink Cat tokens, and being a nontoken
  Cat entering also triggers **Arahbo** for a third 1/1 Cat token.
- Regal Caracal's static ability gives every *other* Cat +1/+1 and lifelink (this now includes
  Arahbo, since Arahbo is a Cat too); Arahbo's static gives every *other* Cat +1/+1; Intangible
  Virtue gives all creature *tokens* +1/+1 and vigilance.
- **Arahbo**: 2/2 base + Caracal's anthem only (its own ability doesn't self-apply) = **3/3
  lifelink**.
- **Regal Caracal**: 3/3 base, no self-buff from its own static, no lifelink of its own = **3/3**.
- **The four 1/1 tokens** (three new + one pre-existing) each get +1/+1 from Arahbo, +1/+1 and
  lifelink from Caracal, and +1/+1 + vigilance from Intangible Virtue (tokens only) = **4/4
  lifelink vigilance** each.
- Attacking with Arahbo (3/3) + Regal Caracal (3/3) + four 4/4 token Cats into an open board is
  22 power for **6 total mana invested this turn** (Regal Caracal's cost) — a plausible turn 5–6
  clock against a 20-life 1v1 opponent, before Divine Visitation or Anointed Procession are even
  live.

## Notes for future upgrade passes

- **Sol Ring's absence** is the single biggest power gap versus the paper EDHREC build — Arcane
  Signet and Mind Stone are the best replacements Arena's pool currently allows.
- If games are being lost to opposing removal on Arahbo specifically, consider adding more
  hexproof/indestructible-granting equipment — the current package (Swiftfoot Boots, Giver of
  Runes, Mother of Runes) is protection-light for a one-commander payoff engine.
- A-Ocelot Pride (Alchemy rebalance, MH3 A-38) is a legal, on-theme lifegain-into-tokens engine if
  a future pass wants to lean further into the lifegain sub-theme and is fine using digital-only
  rebalanced cards.
