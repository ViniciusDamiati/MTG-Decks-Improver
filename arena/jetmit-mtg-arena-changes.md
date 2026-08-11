# Jetmir, Nexus of Revels — MTG Arena 1v1 Rebuild (August 2026)

Changes applied to `jetmit-mtg-arena.txt`, the **MTG Arena** build (100-card 1-on-1
Commander/Brawl, not the 4-player paper build in `jetmir.txt`). Every card mentioned below was
verified against exact Scryfall oracle text. **13 swaps**, deck stays at exactly 100 cards
(99 + commander).

## Critical methodology note: Arena's card pool ≠ paper Commander legality

This rebuild required a different verification process than a normal paper deck-improvement pass,
because MTG Arena's playable card pool is a curated subset of paper Magic, and the two lists don't
map cleanly onto each other in either direction:

- **Some paper Commander staples are simply absent from Arena.** Sol Ring — an 80%-inclusion,
  near-auto-include per EDHREC — has **zero Arena printing** and reads `legalities.brawl:
  not_legal`. So do Mana Crypt, Ancient staples like Skullclamp's competition, and a long tail of
  MH2/MH3-era or Reserved-List-adjacent cards. Never assume "great on EDHREC" means "exists on
  Arena."
- **Alchemy-exclusive/rebalanced cards are real, powerful, and fully legal in Arena's Brawl
  formats** even though they fail paper `legalities.commander` (Scryfall flags them `not_legal`
  there since they don't exist in paper). Two of the swaps below (A-Ocelot Pride, A-Cori-Steel
  Cutter) are exactly this: Arena-only cards, `games: ['arena']`, `legalities.brawl: legal`. Their
  paper-illegal flag is irrelevant on Arena — per the deck owner, count on them.
- **A single Scryfall `named` (fuzzy) lookup is unreliable for the "is this on Arena" question**,
  because it returns one *default* printing, which is often the original paper printing even when
  the card was later ported to Arena via a Historic/Explorer/Multiverse-Legends-style anthology or
  a Remastered set. Esper Sentinel, Ragavan, Krenko Tin Street Kingpin, Skyclave Apparition,
  Wedding Announcement, Voice of Resurgence, and Trostani Discordant all show `arena_legal: false`
  on their default printing and yet are genuinely available (Jumpstart: Historic Horizons, Final
  Fantasy: Through the Ages, War of the Spark, Zendikar Rising, Innistrad: Crimson Vow, Explorer
  Anthology 3, Guilds of Ravnica respectively).
- **The authoritative check used for every card in this document:** (1) Scryfall search across
  ALL printings, `q=!"Card Name" game:arena`, confirms a real Arena printing exists, and (2)
  `legalities.brawl` / `legalities.competitivebrawl` read `legal` (not `banned`/`not_legal`).
  Paper `legalities.commander` was ignored as a filter — it's not the ruleset in play here.

## Data sources

- EDHREC commander page + JSON (9,766 decks, rank #234): `https://edhrec.com/commanders/jetmir-nexus-of-revels`
- mtgtop8 cEDH: `https://mtgtop8.com/format?f=cEDH` — **Jetmir has no cEDH presence at all**; not a
  recognized competitive archetype, so this rebuild leans entirely on the EDHREC baseline plus
  1v1-specific reasoning (see below).
- Card texts + Arena/Brawl legality: Scryfall API (`/cards/named` and `/cards/search`)
- Two reference decklists supplied by the user (both cross-checked against Scryfall for Arena
  legality before anything was borrowed from them)

## What Jetmir actually grants (re-verified)

- **3+ creatures:** +1/+0 and vigilance
- **6+ creatures:** another +1/+0 and trample
- **9+ creatures:** another +1/+0 and double strike (total at 9+: +3/+0, vigilance, trample,
  double strike)

## Why 1v1 changes the plan versus a 4-player pod

Several EDHREC-popular Jetmir cards explicitly scale "for each opponent" or "to each opponent" —
in a 4-player pod that's a 3x multiplier; in 1v1 it's 1x. None of these are traps exactly, but
their reputation overstates their 1v1 output (Adeline, Impact Tremors, Purphoros, Warleader's
Call — kept anyway since their base rate is still fine). The genuine 1v1 trap found during
research is **Primal Vigor**: its token/counter doubling is symmetric — it also doubles the
*opponent's* tokens and counters. It isn't in this deck and shouldn't be added.

Conversely, single-opponent games reward things a 4-player pod dilutes or can't support:
undiluted removal (every removal spell answers the *one* threat that matters), haste (tempo swings
a whole game when there's no third player to buy you time), and outright alpha-strike finishers
(Craterhoof-style "kill the table" effects only need to kill one 40-life opponent, not three).

## The diagnosis

1. **Multiplier/doubler pileup — the same disease as the paper build.** Divine Visitation,
   Anointed Procession, Parallel Lives, and Second Harvest were four separate token-doubling/
   copying effects stacked on top of Doubling Season (a fifth), all fighting for the same role,
   most of them dead on an empty board. Divine Visitation specifically *transforms* tokens into
   4/4 Angels rather than multiplying their count — it trades quantity for quality on a commander
   whose payoff is entirely about hitting 3/6/9 creature-count thresholds. Cut all four, kept
   Doubling Season, and added **Mondrak, Glory Dominus** — a doubler that's also a body (feeds the
   very thresholds it doubles).
2. **Too few creatures, no turn-1 plays.** ~21 creature cards (20 + commander) against an EDHREC
   average of 31. Zero 1-mana dorks. A mana dork here is double value — it ramps *and* counts
   toward Jetmir's thresholds a turn earlier. Added Llanowar Elves and Delighted Halfling.
3. **Zero haste package.** Nothing in the list grants haste. In 1v1, tempo is the whole game —
   every turn your board sits still is a free turn for the single opponent to stabilize. Added
   Urabrask the Hidden (team haste, permanently), Aurelia the Warleader (haste + a second combat
   phase — doubles the alpha strike outright), Devilish Valet (haste/trample body that snowballs
   its own power), and A-Cori-Steel Cutter (haste equipment that also makes its own attacker).
4. **Three redundant board-scaling ramp engines** (Growing Rites of Itlimoc, Cryptolith Rite,
   Mirari's Wake) all do the same job — convert an already-wide board into more mana — and are
   all dead before the board exists. Kept Mirari's Wake (its +1/+1 anthem is unconditional even
   without the mana half); cut the other two for cheap dorks that solve the actual problem
   (turn-1 mana, not turn-6 mana).
5. **No finisher.** Nothing in the list ends a game outright; the plan was "keep attacking and
   hope." Added Craterhoof Behemoth — the single best "close the game right now" card for a wide
   creature board, and in 1v1 it only has to get through one life total.
6. **Weak/off-plan slots.** Ghired needs same-turn nontoken taps on tokens made *that turn* —
   two conditions that rarely align (verified text; identical finding to the paper build).
   Urabrask's Forge sacrifices its token every end step — never a permanent body, never crosses a
   threshold. Battle for Bretagard is a three-turn saga in a deck that wants to be doing something
   turn 1. Roxanne is a 5-drop artifact/mana engine off the deck's actual plan. Quina's mid-game
   token bonus loses to Llanowar Elves' turn-1 acceleration (same call as the paper build). Oketra's
   Monument only discounts/rewards *white* creatures in a deck whose best new threats are red and
   green. Dollmaker's Shop is a slow value enchantment that needs an established attack step to
   do anything.

## The swaps (13 out, 13 in)

| # | Out | In | Reason (verified oracle text + Arena/Brawl legality) |
|---|-----|----|--------------------------------------|
| 1 | Divine Visitation (5) | **Mondrak, Glory Dominus** (4) | "If one or more tokens would be created under your control, twice that many... instead" — doubles *count*, unlike Visitation's quality-swap. Itself a 4/4 body that counts toward 3/6/9. Zendikar-era printing confirmed on Arena (Phyrexia: All Will Be One). |
| 2 | Anointed Procession (4) | **Craterhoof Behemoth** (8) | 4th doubler cut outright — deck doesn't need a 5th/4th token multiplier, it needs a finisher. Craterhoof: haste, +X/+X trample to the whole team on ETB (X = creature count). At even 8 creatures, that's a team-wide +8/+8 trample swing that ends a 40-life 1v1 game on the spot. Confirmed Arena via Tarkir: Dragonstorm. |
| 3 | Parallel Lives (4) | **Aurelia, the Warleader** (6) | 3rd doubler cut. Aurelia: flying, vigilance, haste, and untaps your team + grants a second combat phase the first time she attacks each turn — a literal second Jetmir alpha strike in the same turn. Confirmed Arena (Foundations). |
| 4 | Second Harvest (4) | **Urabrask the Hidden** (5) | Last doubler cut (one-shot instant copy, most redundant of the five). Urabrask: "Creatures you control have haste. Creatures your opponents control enter tapped." Permanent team haste plus a tempo tax on the single opponent's own blockers — exactly the missing piece for a fast 1v1 clock. Confirmed Arena (Multiverse Legends). |
| 5 | Ghired, Mirror of the Wilds (3) | **Jinnie Fay, Jetmir's Second** (3) | Ghired's copy ability needs tokens made *this turn*, tapped by *nontoken* creatures — conditions that rarely align (verified, same finding as the paper build). Jinnie Fay: "If you would create one or more tokens, you may instead create that many 2/2 green Cat creature tokens with haste or 3/1 green Dog tokens with vigilance" — turns *every* token maker in the deck (Doubling Season copies included) into hasty attackers. Exact Naya identity, flavor-matched ("Jetmir's Second"). Confirmed Arena (Streets of New Capenna). |
| 6 | Urabrask's Forge (3) | **Skyclave Apparition** (3) | Forge's Horror token is sacrificed at the next end step — never a permanent body, never crosses a threshold (verified, same finding as the paper build). Skyclave Apparition: proactive exile removal on a body — answers the single opponent's best sub-5-mana permanent while still counting as a creature. Confirmed Arena (Zendikar Rising). |
| 7 | Battle for Bretagard (3) | **Lightning Bolt** (1) | Three-turn saga for two 1/1s and a copy effect that needs different-named tokens — slow payoff. Lightning Bolt: 1 mana, 3 damage to anything — efficient single-target removal or reach to the opponent's face, undiluted in 1v1. Confirmed Arena (many printings, e.g. Secrets of Strixhaven). |
| 8 | Roxanne, Starfall Savant (5) | **The Wandering Emperor** (4) | Roxanne is a 5-drop artifact/mana-fixing engine off the deck's actual plan (same finding as the paper build). Wandering Emperor: flash, so it answers a blocker or protects your alpha strike at instant speed even on the opponent's turn — exactly the kind of instant-speed flexibility that matters when there's no other player to share the answer-burden with. Confirmed Arena (Kamigawa: Neon Dynasty). |
| 9 | Quina, Qu Gourmet (3) | **Llanowar Elves** (1) | Quina's token-bonus is a mid-game payoff; the deck's actual hole is turn-1 acceleration (closest call, same call as the paper build — the 1-mana dork wins). Confirmed Arena (many printings). |
| 10 | Growing Rites of Itlimoc (3) | **Delighted Halfling** (1) | 1st of three redundant board-scaling ramp engines cut. Halfling taps for colorless or, for legendary spells, any color and makes them uncounterable — this deck runs many legendary creatures (Jetmir, Aurelia, Torens, Myrel, Adeline, Brimaz, Jinnie Fay...). Turn-1 play, counts as a body immediately. Confirmed Arena (The Hobbit Eternal). |
| 11 | Cryptolith Rite (2) | **Devilish Valet** (3) | 2nd redundant ramp engine cut — needs creatures tapping for mana, dead on an empty board exactly like the ramp pile it belonged to. Devilish Valet: trample, haste, and doubles its own power every time another creature enters — a single card that can close a game by itself once the board is wide. Confirmed Arena (Streets of New Capenna). |
| 12 | Dollmaker's Shop (2) | **A-Ocelot Pride** (2, Alchemy) | Dollmaker's Shop only does anything once you're already attacking with non-Toys — slow, conditional. A-Ocelot Pride: first strike, lifelink, and at end step (if you gained life) makes a 1/1 Cat — then once you hit Ascend's city's blessing (10+ permanents), it *copies every token that entered that turn*, snowballing the whole board. Arena-exclusive rebalance (`games: ['arena']`), `legalities.brawl: legal` — paper-illegal flag is irrelevant on Arena. |
| 13 | Oketra's Monument (3) | **A-Cori-Steel Cutter** (2, Alchemy) | Monument only discounts/rewards *white* creature spells — this deck's best new threats (Craterhoof, Aurelia Warleader, Urabrask, Devilish Valet, Llanowar Elves, Jinnie Fay) are red and green, so the discount is diluted. A-Cori-Steel Cutter: equipped creature has haste, and on your second spell each turn it makes its own 1/1 prowess Monk and can auto-attach — a self-contained haste engine. Arena-exclusive rebalance, `legalities.brawl: legal`. |

## Legality sweep of the rest of the current list

Ran the same Arena-Brawl-legality check across every remaining card in the deck. Two cards read
`legalities.commander: not_legal` (Thunderbond Vanguard, Tajic, Legion's Valor) — both are also
Alchemy-exclusive rebalances (`games: ['arena']` only). Both show `legalities.brawl: legal`, so
per the "Alchemy cards are fair game" ruling above, both stay untouched — no action needed, they
were never actually a legality problem on Arena. (Tajic showed `legalities.competitivebrawl:
banned`, which is why the check used `brawl`, not `competitivebrawl`, as the operative field — see
methodology note above.) Waystone's Guidance was initially misflagged for the same reason and is
correctly kept in the deck.

## Why the changes are stronger — the proof

**The haste package turns Jetmir's math into a same-turn kill.** At 9 creatures Jetmir himself
swings as an 8/4 double striker (16) and each 1/1 as a 4/1 double striker (8) — Jetmir + eight
1/1 tokens is **80 damage in one combat** (unchanged commander math, verified again this session).
Previously that required surviving to a turn where the board was already established *and*
summoning-sick creatures had a turn to sit. With Urabrask the Hidden in play, every token and
creature that resolves this turn is already attacking-eligible — the 80-damage swing can happen
the same turn the board is finished, not a turn later. Against a single 40-life opponent, that's
lethal on its own without needing a second combat step.

**Aurelia, the Warleader doubles it again.** Her extra-combat trigger means the exact same board
(now-untapped, still pumped by Jetmir) attacks *twice* in one turn — a hypothetical 80-damage
alpha strike becomes a 160-damage turn if the opponent survives the first swing.

**Craterhoof is the "board isn't even that wide yet" backup finisher.** Even at a modest 8
creatures (below the 9-creature double-strike threshold), Craterhoof's ETB alone adds +8/+8
trample to the whole team — more than enough to close a 1v1 game through a small number of
blockers, since trample punches through chump blocks that would otherwise stall a wide-but-not-yet-
overwhelming board.

**Creature count moved from ~21 to 28 (commander included).** Net across the 13 swaps: 3 creatures
cut (Ghired, Roxanne, Quina) against 8 creatures added (Mondrak, Craterhoof, Aurelia Warleader,
Urabrask the Hidden, Jinnie Fay, Skyclave Apparition, Llanowar Elves, Delighted Halfling, Devilish
Valet, A-Ocelot Pride = actually 10 creatures added) for a net of +7 creatures — closer to the
EDHREC average of 31 while staying leaner than a pure value pile, appropriate for a 1v1 clock that
wants to end the game rather than grind it.

## Optional upgrades not applied

- **Skrelv, Defector Mite** (1-drop, grants hexproof + toxic to a key attacker) — verified Arena
  legal, strong protection piece for whichever creature is carrying the game plan that turn; left
  out only because 13 swaps already covers every diagnosed hole without overcorrecting deck
  identity.
- **A-Sizzling Soloist / A-Celebrity Fencer / A-Elderleaf Mentor** — several more true Alchemy
  rebalances in Naya colors turned up in the search (see methodology note); all playable and
  reasonable, none clearly better than what's already in the 100.
- **Elesh Norn, Grand Cenobite** — confirmed Arena-legal (Multiverse Legends) and devastating
  (+2/+2 to your team, -2/-2 to the opponent's, often a one-sided board wipe on top of an anthem),
  but 7 mana is slow for a deck now built to close games faster than that.
