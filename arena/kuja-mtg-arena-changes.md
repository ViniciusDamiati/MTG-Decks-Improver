# Kuja, Genome Sorcerer — MTG Arena 1v1 Upgrade (August 2026)

Changes applied to `kuja-mtg-arena.txt` (100-card 1-on-1 Commander/Brawl build). Every card
mentioned below was verified against exact Scryfall/local-DB oracle text and live Arena
printing data. **3 collector-number corrections + 4 power-level swaps**, deck stays at exactly
100 cards (99 + commander).

> **Correction (post-delivery):** the first pass of this upgrade incorrectly flagged
> `Unclaimed Territory (XLN) 258` as having no Arena printing and cut it for Solphim, Mayhem
> Dominus. The deck owner pushed back — this decklist was exported directly from the Arena
> client, so a card in it is definitionally real on Arena. A live re-check confirmed the
> pushback was correct: `XLN 258` shows `games: ['arena', 'paper', 'mtgo']` and
> `legalities.brawl: legal` — the original `arena-legality-checker` pass made an error on this
> one card. Unclaimed Territory is restored, and Solphim is kept by cutting the deck's weakest
> remaining card (`Blazing Bomb`) instead. Everything below reflects the corrected swap list.

## Data sources

- EDHREC commander page + JSON (21,198 decks, rank #56):
  `https://edhrec.com/commanders/kuja-genome-sorcerer`
- mtgtop8 cEDH: `https://mtgtop8.com/format?f=cEDH` — **Kuja has no cEDH presence at all** (the
  string doesn't appear anywhere in the cEDH page HTML; EDHREC's own "cEDH" tag covers only
  12/21,198 tracked decks, a background rate, not a recognized competitive archetype).
- Card texts + Arena/Brawl legality: local `mtg_cards` DB + Scryfall API (`/cards/named`,
  `/cards/search`)

## Kuja, Genome Sorcerer — verified text

> **Kuja, Genome Sorcerer** {2}{B}{R}, Legendary Creature — Human Mutant Wizard, 3/4
> At the beginning of your end step, create a tapped 0/1 black Wizard creature token with
> "Whenever you cast a noncreature spell, this token deals 1 damage to each opponent." Then if
> you control four or more Wizards, transform Kuja.
>
> **Trance Kuja, Fate Defied** (back face), Legendary Creature — Avatar Wizard, 4/6
> Flare Star — If a Wizard you control would deal damage to a permanent or player, it deals
> double that damage instead.

Axis: noncreature-spells-matter / Wizard tokens that ping the opponent, transforming into a
team-wide Wizard-damage doubler once the token count builds up.

## Methodology note: Arena legality verification

Per project convention, every card already in the list and every candidate add was run through
`arena-legality-checker` (live Scryfall, not just the local DB's newest-printing snapshot) —
checking `games` includes `arena`, `legalities.brawl`/`competitivebrawl` reads `legal`, and
color identity stays within Kuja's {B, R}. This caught three mis-filed printings (see below).
It also produced one false positive — `Unclaimed Territory` was initially misflagged as absent
from Arena; a live re-check after the deck owner's pushback confirmed `XLN 258` is genuinely
`games: ['arena', ...]` and `brawl: legal`. Lesson for future passes: verify a "not on Arena"
verdict with a direct printing lookup, not just the agent's summary, especially for a card that
came from a real client export.

## 1v1-specific read

Kuja's "deals 1 damage to **each opponent**" wording is only 1x instead of a 4-player pod's 3x,
but that's not a dilution problem here — the deck's actual win condition (chip damage from many
small triggers, backed by damage doublers) still adds up against a single 40-life target just
fine, and undiluted single-target removal (Bloodchief's Thirst, Infernal Grasp, Murder, Hero's
Downfall, etc.) is *more* efficient in 1v1 since every removal spell answers the one blocker
that matters. No symmetric-effect traps were found — Solphim and City on Fire's damage-doubling
only affects "a source **you control**," never the opponent's.

## The diagnosis

1. **Three collector-number errors** — cards genuinely on Arena, filed under printings that
   aren't:
   - `Melt Through (Y23) 10` doesn't exist; Melt Through is Alchemy-exclusive, its only
     printing is `YBRO 10`.
   - `A-Rockslide Sorcerer (ZNR) 154` (no `A-` prefix) is actually the plain paper/MTGO
     **Rockslide Sorcerer**, a different card object that's `brawl: not_legal`. The Alchemy
     rebalance you want is `ZNR A-154`.
   - `Harmonic Prodigy (MH2) 132` is a paper/MTGO-only printing (`games` doesn't include
     `arena`). The real Arena printing is `J21 466` (Jumpstart: Historic Horizons).
2. **40 lands against an EDHREC average of 35** — five over, in a low-curve burn/spellslinger
   shell that wants to be casting multiple cheap spells a turn, not sitting on excess mana.
   Compounding this, two of those lands are narrow: `Secluded Courtyard`'s colored-mana mode
   only works for Wizard creature spells/abilities (dead for the instant/sorcery half of the
   deck), and `Three Tree City`'s colored mode costs {2} to activate and scales off your board's
   Wizard count — a slow, conditional mana sink, not real ramp. (`Unclaimed Territory` has the
   same narrow Wizard-only-mana restriction, but is genuinely Arena-legal and kept in the 100 —
   see correction note above.)
3. **A weak filler creature with no fallback mode.** `Blazing Bomb`'s counter trigger needs 4+
   mana spent on a spell (many of this deck's cheap burn/cantrips won't hit that), and its
   removal ability needs the opponent to have a creature to sacrifice into — narrow on both axes,
   with no cycling or alternate mode to fall back on.
4. **A dead-card artifact-hate slot with no fallback.** `Smash to Smithereens` has no cycling or
   alternate mode (unlike `Shredded Sails`/`Skycrash`, both kept for their cycling), so it's a
   brick in any matchup where the single opponent isn't running artifacts.
5. **Missing the deck's own damage-doubling payoffs.** EDHREC's high-synergy list is otherwise
   almost fully represented in this build (Black Waltz No. 3, Circle of Power, Black Mage's Rod,
   Cornered by Black Mages, Coruscation Mage, Lindblum, Queen Brahne, Mysidian Elder all already
   present) — but `Solphim, Mayhem Dominus` and `Artist's Talent`, both direct multipliers on the
   exact "noncombat damage from a source you control" text Kuja's tokens use, were absent.

## The swaps

### Collector-number corrections (3, same card kept, printing fixed)

| Card | Wrong printing | Corrected printing |
|---|---|---|
| Melt Through | (Y23) 10 | (YBRO) 10 |
| A-Rockslide Sorcerer | (ZNR) 154 | (ZNR) A-154 |
| Harmonic Prodigy | (MH2) 132 | (J21) 466 |

### Power-level swaps (4 out, 4 in)

| # | Out | In | Reason (verified oracle text + Arena/Brawl legality) |
|---|-----|----|--------------------------------------|
| 1 | Blazing Bomb (FIN) 130 | **Solphim, Mayhem Dominus** (ONE) 150 | Blazing Bomb's counter trigger (4+ mana spent) and removal mode (needs an opponent creature) are both conditional, with no fallback. Solphim: "If a source you control would deal noncombat damage to an opponent or a permanent an opponent controls, it deals double that damage instead" — doubles every one of Kuja's Wizard-token pings and every burn spell in the deck. Confirmed `brawl: legal`, CI {R}. |
| 2 | Secluded Courtyard (FDN) 267 | **Artist's Talent** (BLB) 124 | Courtyard's colored mana only fires for Wizard creature spells/abilities — dead for most of this instant/sorcery-heavy shell. Artist's Talent: loots on every noncreature spell (fuels the plan directly), then at Level 3 makes every noncombat-damage source deal +2 — a second damage-boost stacking with Solphim/Kuja. Confirmed `brawl: legal`, CI {R}. |
| 3 | Three Tree City (BLB) 260 | **City on Fire** (MOM) 135 | Three Tree City's colored mode costs {2} and scales off Wizard count — slow, conditional ramp. City on Fire (Convoke, so the wide Wizard-token board helps cast it): "it deals triple that damage instead" — a third stacking multiplier on the same damage-doubling axis as Kuja and Solphim. Confirmed `brawl: legal`, CI {R}. |
| 4 | Smash to Smithereens (PIO) 343 | **Wizard's Lightning** (DOM) 152 | Smash to Smithereens is a dead card with no fallback against any opponent running zero artifacts. Wizard's Lightning: costs {2} less (so often {1}{R}) whenever you control a Wizard — which this deck does from turn 1 onward via its own tokens — for 3 damage to any target, itself subject to every multiplier above. Confirmed `brawl: legal`, CI {R}. |

## Legality sweep of the rest of the current list

Ran the full Arena/Brawl-legality check across all 100 cards. Beyond the 3 collector-number
fixes above, every remaining card (all removal, all burn/ping payoffs, both mana rocks, Dark
Ritual, all 15 nonbasic lands including Unclaimed Territory, and both basics) resolved to a
real Arena printing with `legalities.brawl: legal` and color identity within {B, R}. Zero
banned cards, zero color-identity issues.

## Why the changes are stronger — the proof

**The damage multipliers now stack.** Solphim and City on Fire are both replacement effects on
"a source you control deals noncombat damage" — with both in play alongside Kuja's own Flare
Star doubler (once transformed), a single Wizard-token ping (1 damage) becomes 1 × 2 (Solphim) ×
3 (City on Fire) = **6 damage per noncreature spell cast**, before Kuja's own post-transform
doubling is even counted. A single **Wizard's Lightning** (3 damage, often cast for just {1}{R}
once any Wizard token is in play) becomes an **18-damage burn spell** under that same stack —
more than enough to close a 1v1 game outright from a stabilized board state.

**Land count moved from 40 to 38**, closer to the EDHREC average of 35 for a deck that wants to
chain cheap spells rather than sit on flood, while two of the narrowest lands (Secluded
Courtyard, Three Tree City) were replaced with cards that directly advance the win condition
instead of just producing mana. Unclaimed Territory stays despite sharing that narrow-fixing
issue, since power level was never the reason it was in question.

## Optional upgrades not applied

- **Fandaniel, Telophoroi Ascian**, **Vivi's Persistence**, **Kefka, Dancing Mad**, **Gleeful
  Arsonist**, **Mana Geyser**, and **Transpose** all scored well on EDHREC synergy but are
  confirmed **not on Arena** (`historic`/`games` checks came back negative on every printing) —
  excluded on legality grounds alone, not power level.
- **Withering Torment / Nocturnal Hunger / Bake into a Pie** (broadly-useful creature removal)
  were confirmed strong and kept rather than cut for more payoffs — 1v1 removal density is a
  real asset against a single opponent's best blocker, not overkill the way it can be in a
  4-player pod.
