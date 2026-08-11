# Nekusar, the Mindrazer — Upgrade Notes (August 2026)

Changes applied to `Nekuzar, the Mindrazer.txt`. Every card mentioned below was verified
against its exact oracle text (local `mtg_cards` database, cross-checked live on Scryfall
where noted) before being cut, added, or kept. The deck is now **exactly 100 cards** (99 +
commander) — the original list was **101 cards, 1 over the legal limit**.

Data sources:

- mtgtop8 cEDH format check: https://mtgtop8.com/format?f=cEDH — **no cEDH presence**; Nekusar
  has zero recorded tournament decklists. Treat this as a non-competitive, casual-metagame
  commander with no bracket-4 record — the upgrade below targets power within an
  average/high-power pod, not a cEDH bracket.
- EDHREC commander page (31,388 tracked decks, overall rank #18): https://edhrec.com/commanders/nekusar-the-mindrazer
- EDHREC per-category data: https://json.edhrec.com/pages/commanders/nekusar-the-mindrazer.json
- EDHREC average decklist: https://edhrec.com/average-decks/nekusar-the-mindrazer
- Card texts: local `mtg_cards` Postgres database (loaded from Scryfall's `oracle-cards` bulk
  data), cross-verified live against `api.scryfall.com` for one card (see "memory correction"
  below).

## What Nekusar actually does (verified)

> At the beginning of each player's draw step, that player draws an additional card.
> Whenever an opponent draws a card, Nekusar deals 1 damage to that player.

The axis: force *everyone* to draw extra cards, then punish opponents 1-for-1 on every card
they draw — from Nekusar's own static ability, from other "extra draw" effects, and from
one-shot wheels. The deck needs (a) redundant sources of the "everyone draws extra" effect,
(b) direct damage-per-draw payoffs stacked on top, and (c) enough of its own card advantage
to not just be handing opponents free cards.

## The diagnosis

1. **Deck was 101 cards — 1 over the limit.** Fixed as part of this pass (see below).
2. **Several EDHREC-flagged "notable absence" staples were missing.** The existing list
   already carried most of the archetype's top enchantment payoffs (Fevered Visions, Forced
   Fruition, Font of Mythos, Propaganda) — a good sign — but was missing four cards that clear
   both the >40% inclusion and >0.35 synergy bar: **Peer into the Abyss** (51.1%/0.459),
   **Kami of the Crescent Moon** (53.0%/0.490), **Dictate of Kruphix** (40.8%/0.376), and
   **Reforge the Soul** (48.7%/0.440).
3. **Several slots were doing too little for their cost.** A handful of cards were either
   low-EDHREC-visibility punisher relics (Black Vise), off-theme value (Sangromancer's
   lifegain, Geth's Grimoire's narrow discard-only trigger), fragile one-shot effects that
   need to survive combat or be sacrificed to matter (Magus of the Jar, Elder Brain), or
   simply outclassed by a strictly better effect at the same or lower cost (Worn Powerstone's
   tapped ramp vs. Thought Vessel; Jace Beleren's 17.7% inclusion vs. Dictate of Kruphix's
   40.8%).
4. **Manabase had one weak, purely conditional land.** Temple of the False God only produces
   mana with 5+ lands already in play and only makes colorless — in a 3-color deck a real dual
   does strictly more work.

## The swaps (9 out, 9 in)

| # | Out | In | Reason (verified against oracle text + EDHREC data) |
|---|-----|----|--------------------------------------|
| 1 | Black Vise (no EDHREC top-list presence) | **Peer into the Abyss** (51.1% incl, 0.459 synergy) | Black Vise only pings for hand size above 4 — this deck's own wheels regularly empty opponents' hands, neutering it. Peer into the Abyss, pointed at an opponent, makes them draw half their library and lose half their life **in one shot** — with Nekusar out, that single card can be a full alpha strike of face damage from the draw trigger alone, independent of the life loss. |
| 2 | Temple of the False God (conditional, colorless-only) | **Watery Grave** (55.1% incl) | Real UB dual vs. a land that whiffs before turn 5 and never fixes red or black. |
| 3 | Worn Powerstone (enters tapped) | **Thought Vessel** (56.7% incl, 0.355 synergy) | Same colorless ramp, untapped, plus "no maximum hand size" — real upside in a deck whose whole plan is holding/generating extra cards. |
| 4 | Jace Beleren (17.7% incl) | **Dictate of Kruphix** (40.8% incl, 0.376 synergy) | Jace's +2 gives everyone a card with no damage attached and a loyalty total that dies to any attack. Dictate is flash and a second, more resilient copy of Nekusar's own "everyone draws an extra card" ability — stacks the core damage engine instead of competing with it. |
| 5 | Elder Brain (7 mana, ability needs to connect in combat) | **Kami of the Crescent Moon** (53.0% incl, 0.490 synergy) | Elder Brain does nothing unless it survives to attack. Kami is a third static copy of "everyone draws an extra card" for 2 mana, on a body that can also block. |
| 6 | Magus of the Jar (fragile, needs to survive to sacrifice) | **Seizan, Perverter of Truth** (37.2% incl, 0.343 synergy) | Magus of the Jar is a one-shot effect that dies to any removal before it matters. Seizan triggers on **every player's every upkeep** — 2 life loss + 2 cards drawn, repeatable, resilient, and every one of those opponent draws is a Nekusar damage trigger too. |
| 7 | Geth's Grimoire (only triggers on discard, no other payoff) | **Waste Not** (57.3% incl, 0.452 synergy) | Grimoire only rewards opponent discards with a draw. Waste Not rewards *every* opponent discard type (creature → token, land → mana, other → draw) — directly amplifies the deck's own discard-forcing wheels (Dark Deal, Winds of Change, Careful Consideration). |
| 8 | Sangromancer (lifegain payoff, off-theme) | **Molten Psyche** (57.2% incl, 0.529 synergy) | Lifegain isn't this deck's plan. Molten Psyche is an X-cost wheel (scales with mana available, unlike a fixed wheel) that also deals bonus damage to each opponent equal to cards they drew this turn once the deck hits metalcraft (3+ artifacts — trivial here with Sol Ring, two Signets, Fellwar Stone, Darksteel Ingot, Obelisk of Grixis, Thought Vessel, Lightning Greaves, Swiftfoot Boots all in the 99). |
| 9 | Sign in Blood (single-target, 2 cards) | **Reforge the Soul** (48.7% incl, 0.440 synergy) | Sign in Blood draws 2 for one player. Reforge the Soul wheels **everyone** to 7 cards (with a Miracle discount to {1}{R} if drawn naturally) — every opponent's 7 new cards are 7 Nekusar damage triggers, not just card selection for one player. |

## Deck size fix (101 → 100)

The original list was 1 card over the 100-card limit. Cut with no replacement:

- **Turn Aside** — only counters a spell that targets a permanent you already control; narrow,
  situational, and redundant with Lightning Greaves + Swiftfoot Boots already providing
  broader, standing protection against targeted removal.

## Memory correction caught during the audit

The audit batch initially flagged **Dictate of Kruphix** as a suspected off-color (green) card
before it was checked — a misremembering, not a database error. Verified against both the
local database and a direct live Scryfall API call: Dictate of Kruphix is **{1}{U}{U}, blue**,
with the "at the beginning of each player's draw step, that player draws an additional card"
text used in the swap table above. Both sources agreed exactly, confirming the local database
is accurate; the error was in memory, caught before it reached the decklist, per the project's
standing rule to verify before every claim.

## Cards challenged during the audit and kept as-is

- **Painful Quandary** — "Whenever an opponent casts a spell, that player loses 5 life unless
  they discard a card" reads narrow on a skim, but 5 life per spell cast is a real, repeatable
  damage/tax engine that compounds with every turn an opponent plays Magic. Kept.
- **Psychic Corrosion** — mills opponents on your own draws rather than dealing direct damage;
  it's an alternate (mill) win condition with no other mill support in the 99, making it the
  single weakest verified card in the final list. Not cut this pass (only 9 swaps were needed
  to reach the diagnosed holes and fix the count) — flagged as the top candidate for a future
  pass; see optional upgrades below.
- **Collective Defiance, Cunning Rhetoric, Curiosity, Zurzoth Chaos Rider, Mystic Retrieval,
  Careful Consideration** — all verified to do exactly what the deck wants (flexible
  removal/wheel modality, value off being attacked, evasive card draw, token generation off
  off-turn draws, instant/sorcery recursion, and 4-draw/2-discard selection respectively). No
  hidden weakness found; no changes made.

## Why the changes are stronger — the proof

With Nekusar, Kami of the Crescent Moon, and Dictate of Kruphix all in play, a single
opponent's draw step alone now produces **4 draws instead of 1** (their normal draw + 3
static "extra card" triggers) — and every one of those draws is a separate instance of
Nekusar's damage trigger, so that's **4 damage per opponent, every turn, before a single
card is cast.** Add Seizan, Perverter of Truth's upkeep trigger (2 more forced draws + 2
direct life loss) and it's **6 damage + 2 life loss per opponent per turn cycle from board
state alone** — 18 damage and 6 life loss spread across a 3-opponent pod, every round,
doing nothing else. Resolving one wheel on top of that — Reforge the Soul, Molten Psyche, or
Whispering Madness, all now in the 99 — draws each opponent 6-7 more cards in one shot,
which is **6-7 additional simultaneous Nekusar triggers per opponent**, i.e. an 18-21 damage
burst across the table from a single card.

## Optional upgrades (not applied)

- **Jace's Archivist** — 65.5% inclusion, a stronger wheel-planeswalker than anything
  currently in the 99; a good next add if another slot opens up.
- **Wheel and Deal** (46.4% incl) — a fourth/fifth wheel effect; the deck already added three
  this pass (Reforge the Soul, Molten Psyche, plus the existing Whispering Madness/Windfall/
  Winds of Change/Dark Deal), so this was left for a future pass rather than over-loading one
  effect type.
- **Fierce Guardianship / Cyclonic Rift** — both "Game Changer"-tagged, high-power free/
  overloaded interaction; not added to keep this pass focused on the draw-damage engine rather
  than raising the deck's overall power ceiling.
- **Cutting Psychic Corrosion** for one of the above — see "Cards challenged... and kept" —
  it's the weakest verified card in the final 99 and the strongest candidate for the next
  upgrade pass.

Deck re-verified at exactly 100 cards after all swaps; no duplicate non-basic entries; color
identity of every add confirmed as a subset of Nekusar's U/B/R identity (including the U/B
Watery Grave and the mono-U, mono-B, and mono-R spell adds).
