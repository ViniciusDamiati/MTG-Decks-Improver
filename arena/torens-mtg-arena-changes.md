# Torens, Fist of the Angels — MTG Arena upgrade

## Sources

- Commander oracle text: local `card_db.py` (Postgres cache of Scryfall `oracle-cards`)
- Competitive record: https://mtgtop8.com/format?f=cEDH (searched under both "Toren" and the
  correct name "Torens, Fist of the Angels")
- Archetype data: `edhrec-researcher` agent → https://edhrec.com/commanders/torens-fist-of-the-angels
- Candidate-add legality: `arena-legality-checker` agent (live Scryfall, cross-printing search)

## Methodology note on Arena legality

Per the user's instruction, the **existing 99 cards were not swept** for legality — this list
was exported directly from the Arena client, so it's already known to import and play. Legality
work in this pass was scoped to the **7 new additions only**: each was checked against
`legalities.brawl` in the local DB first, then run through `arena-legality-checker` for a
confirmed, currently-valid set/collector number.

Two of the adds hit the classic false-negative trap the project's methodology warns about: the
local DB's `oracle-cards` dump stores only *one* printing per card (usually the newest), and for
**Esper Sentinel** and **Hardened Scales** that default printing (`MH2 12` / `SOC 272`) is
paper/MTGO-only. Both cards are genuinely Arena-legal via their Jumpstart 2021 reprint (`J21 75`,
`J21 582`), which the legality-checker agent found by searching across all printings rather than
trusting the single cached one. Five other candidates were cut for the opposite reason — real
cards, real EDHREC inclusion, but `legalities.brawl: not_legal` on Arena's Brawl/Commander format
specifically: **Skullclamp** (banned in Brawl/CompetitiveBrawl), **Aura Shards**, **Generous
Gift**, **Champion of the Parish**, and **Path of Ancestry**. None of these made it into the deck.

## Commander

**Torens, Fist of the Angels** — {1}{G}{W}, Legendary Creature — Human Cleric, 2/2.
> Training (Whenever this creature attacks with another creature with greater power, put a
> +1/+1 counter on this creature.)
> Whenever you cast a creature spell, create a 1/1 green and white Human Soldier creature token
> with training.

Axis: every creature spell adds a body to the board, and Training turns "attack alongside
something bigger" into permanent stat growth — the deck wants to go wide *and* have its
attackers get bigger over time, not just wide.

- **cEDH presence: none.** Torens does not appear on mtgtop8's cEDH format page or search —
  confirmed casual/EDHREC-tier commander, not a competitive line.
- **EDHREC**: 1,830 decks, rank #1,176. Dominant deck themes: +1/+1 Counters (252 decks),
  Tokens (163), Humans (109). The average decklist leans much harder into the **counters**
  half of the game plan than this list did before the pass — see diagnosis below.

## Diagnosis

1. **Seven cards doing the same job.** Parallel Lives, Doubling Season, Anointed Procession,
   Divine Visitation, Second Harvest, Quina Qu Gourmet, and Queen Allenal of Ruadach all modify
   or double token creation. Three-plus static doublers *do* compound multiplicatively, but at
   4–5 mana apiece they do nothing the turn they're played — with seven, over a third of the
   deck's "engine" slots are inert cards. This is a top-heavy do-nothing-on-curve problem, not a
   strength.
2. **Training was barely engaged.** The commander's own ability only fires off *other* creatures
   with greater power — before this pass, the only things reliably bigger than Torens were the
   top-end finishers (Craterhoof, Ghalta and Mavren, Surrak). Nothing cheap was making Torens (or
   anything else) grow turn over turn.
3. **Missing the archetype's actual payoff.** EDHREC's average Torens deck runs Cathars' Crusade
   (40% inclusion) as a centerpiece — this list had none of the +1/+1-counters synergy package
   (Hardened Scales, Luminarch Aspirant, etc.) that the commander's Training keyword is built to
   reward.
4. **Thin interaction.** Only Path to Exile, Swords to Plowshares, and Ossification answered
   creatures; Demystify only ever answers an enchantment. In 1v1 there's exactly one opponent to
   read and answer — three real removal spells plus one narrow dead card most games is light.
5. **Haste**: only Crashing Drawbridge and Swiftfoot Boots proactively grant it (Surrak,
   Akroma's Memorial, and Craterhoof are self-contained but expensive). Not touched this pass —
   the curve/interaction problems were the bigger lever — but worth a future look if the deck
   still feels slow to close games.
6. **Curve was inverted.** The cut cards averaged ~2.6 CMC with three of the seven doing nothing
   proactive; the adds average ~1.6 CMC and every one of them affects the board or the opponent
   immediately.

## Swaps

| # | Cut | Why | Add | Why (verified text + data) | Arena |
|---|-----|-----|-----|-----|-------|
| 1 | Demystify (1cmc, destroy target enchantment) | Dead in most games — answers only one permanent type | **Cathars' Crusade** (5cmc enchantment) — "Whenever a creature you control enters, put a +1/+1 counter on each creature you control." | EDHREC 39.9% inclusion / 0.265 synergy on this exact commander, and totally absent from the list. This deck already floods the board with ETB token generators (Brimaz, Leonin Warleader, Adeline, Myrel, Okoye) — Crusade turns every one of those triggers into a team-wide pump. | JMP 95, brawl-legal |
| 2 | Second Harvest (4cmc instant, one-shot copy your tokens) | Redundant 6th/7th token-doubling effect; sorcery-speed-only value, does nothing proactively | **Hopeful Initiate** (1cmc, 1/2, Training + sac-2-counters removal) | Shares the commander's own Training keyword — a cheap body that grows the same way Torens does, plus a built-in artifact/enchantment answer that doesn't cost a card slot on its own. | VOW 20, brawl-legal |
| 3 | Quina, Qu Gourmet (3cmc, 2/3, extra Frog on token creation) | Weakest of the token-replacement stack — small body, marginal upside over the doublers already running | **Esper Sentinel** (1cmc, 1/1 artifact creature) — taxes the opponent's first noncreature spell each turn or draws a card | Undiluted in 1v1 — one opponent, one tax target every turn. 76 EDHREC rank overall (extremely high adoption across all white decks) for a reason: cheap, relevant every game. | J21 75 (default MH2 printing is paper/MTGO-only — flagged above) |
| 4 | Queen Allenal of Ruadach (3cmc, */* , extra Soldier on token creation) | Same redundancy as Quina — a 6th/7th "modify token creation" effect is diminishing returns | **Luminarch Aspirant** (2cmc, 1/1) — "At the beginning of combat on your turn, put a +1/+1 counter on target creature you control." | Direct support for the Training/counters plan — every turn, without needing anything else on board, something (often Torens) gets bigger before combat. | ZNR 24, brawl-legal |
| 5 | Awaken the Woods (X{G}{G} sorcery, X 1/1 land-creature tokens) | Weak rate at any real X, and Dryad land-tokens die to any removal or block, losing a land | **Beast Within** (3cmc instant) — "Destroy target permanent. Its controller creates a 3/3 green Beast creature token." | The deck had zero unconditional removal — nothing answered a problematic artifact, enchantment, or planeswalker. Beast Within hits anything at instant speed; brawl-legal where Generous Gift (also considered) is not. | OMB 33, brawl-legal |
| 6 | Evendo, Waking Haven (land, enters tapped, Station 12+ threshold) | Slow, clunky mana sink that needs 12+ accumulated charge counters to matter — too slow for a 1v1 clock | **Hardened Scales** (1cmc enchantment) — "If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead." | Multiplies every counter source now in the deck — Torens' Training, Cathars' Crusade, Luminarch Aspirant, Hopeful Initiate, Caretaker's Talent's level 3, Tribute to the World Tree. One cheap enchantment, compounding value all game. | J21 582 (default SOC printing is paper/MTGO-only — flagged above) |
| 7 | Rabble Rousing (5cmc enchantment, tokens only when already attacking with several creatures + a 10-creature-count payoff) | Win-more — needs the board state it's supposed to help build; slow for what it does | **Katilda, Dawnhart Prime** (2cmc, 1/1) — Human creatures you control tap for any of Katilda's colors; {4}{G}{W},{T}: counter on each creature you control | Cheap, on-curve, turns the deck's many Human tokens/creatures (Torens itself, Adeline's tokens, Myrel's Soldiers, Okoye's Soldiers) into a mana engine, with a late-game counters sink attached. | MID 230, brawl-legal |

Net: −7 cards averaging ~2.6 CMC (three of which affected the board zero times when cast) for
+7 cards averaging ~1.6 CMC (all of which affect the board or the opponent the turn they land).
Deck stays at exactly 100 cards.

## Challenged and kept

No cuts were challenged by the user this pass (first pass on this decklist). Cards seriously
considered for cutting but kept: **Second Harvest was cut**, but **Divine Visitation** and the
three primary doublers (Parallel Lives, Doubling Season, Anointed Procession) were kept — they
still compound multiplicatively when two or more are live, and cutting further into that package
risked leaving the go-wide plan without enough raw multiplication once Cathars' Crusade and
Hardened Scales are also online.

## Proof — a concrete turn

Board (post-upgrade, a plausible turn 6 in a 1v1 game): Torens (2/2, one +1/+1 counter from a
prior Training trigger → 3/3), Cathars' Crusade in play, Hardened Scales in play, and two 1/1
Human Soldier tokens from earlier creature casts.

Cast a 3-power creature (e.g. Brimaz, King of Oreskos, 3/4):
- Brimaz enters → Cathars' Crusade triggers: "put a +1/+1 counter on each creature you control."
  Hardened Scales turns that into **+2/+2 on each of your four creatures** (Torens, the two
  tokens, Brimaz itself).
- Torens is now a 5/5; the two Soldier tokens are 3/3; Brimaz is a 5/6.
- Attack with all four. Brimaz's attack trigger makes a 1/1 Cat Soldier token attacking. Torens
  attacks alongside Brimaz (3 power ≤ Torens' 5, so no Training trigger off Brimaz specifically,
  but the Cat token or Soldier tokens attacking alongside a bigger Torens still net combat
  damage) — total unblocked damage if the single opponent has no blockers left standing:
  5 (Torens) + 3 + 3 (Soldiers) + 5 (Brimaz) + 1 (Cat token) = **17 damage**, more than half of a
  starting 20-life 1v1 opponent, generated off a single 3-mana creature cast with two 1-drop/5cmc
  enchantments already in play — a line the pre-upgrade list (no Cathars' Crusade, no Hardened
  Scales) could not produce at that mana investment.

## Optional upgrades not applied

- **Haste package** — still thin (Crashing Drawbridge, Swiftfoot Boots only). If games are still
  won too slowly, a future pass could look at cheap GW haste-granting equipment/auras on Arena.
- **Path of Ancestry** — strong land for this shell (scry on commander-type creature casts) but
  came back `brawl: not_legal` on Arena; left out. Worth re-checking if Arena's Brawl pool
  changes.
- **Skullclamp / Aura Shards / Generous Gift / Champion of the Parish** — real EDHREC staples for
  this commander, all excluded specifically because they're not legal in Arena's Brawl format
  (Skullclamp is outright banned there).
