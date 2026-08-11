---
name: arena-deck-upgrade
description: Run the Commander deck improvement methodology adapted for MTG Arena's 1-on-1 Brawl/Commander format - every candidate gated on real Arena availability, 1v1-aware reasoning (haste, undiluted removal, finishers over "each opponent" scaling), and the MTGA Commander/Deck import format preserved. Use when the user asks to improve, strengthen, or upgrade a deck they play on MTG Arena specifically (not a paper deck). Argument - the deck .txt filename.
---

# Arena Deck Upgrade — MTG Arena 1v1 methodology

Same evidence-based spine as `/deck-upgrade` and `DECK-IMPROVEMENT-GUIDE.md`, with two hard
requirements layered on top: **every card is gated on real Arena availability**, and **the
analysis assumes 1-on-1, not a 4-player pod.** Skipping either produces recommendations the
deck owner literally cannot play, or that are quietly weaker than advertised in their actual
games.

## 0. Recognize the file format

Arena decklists in this project use the MTGA client's native export/import shape, not the
generic paper convention:

```
Commander
1 <Commander Name> (SET) NUM

Deck
1 <Card Name> (SET) NUM
...
```

Do **not** force this into the alphabetical `1 Cardname` / blank line / commander-last shape
used by paper lists like `jetmir.txt` — that format won't re-import into the Arena client.
Keep the `Commander` / blank / `Deck` header structure, and give every card a real
`(SET) NUM` from an actual Arena printing (the arena-legality-checker agent reports this).
Card order within `Deck` doesn't need to be alphabetical — MTGA's own exports aren't.

## 1. Establish facts

- Read the deck file; verify the `Commander` + `Deck` sections together total exactly 100
  (`awk 'NF{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/){n+=$i; break}}END{print n}' <deck>.txt` —
  note the plain `awk 'NF{n+=$1}...'` one-liner from the paper workflow breaks on the
  `Commander`/`Deck` header lines; use the version above that skips non-numeric first fields).
- Fetch the **commander's** oracle text (card-verifier agent) and write one sentence stating
  the axis it scales on — same discipline as the paper methodology.

## 2. Research — with a 1v1 lens

Run mtgtop8 cEDH check + `edhrec-researcher` agent exactly as in the paper methodology. Then,
before proposing anything, actively flag which top cards are:

- **Format-neutral or better in 1v1**: single-target removal, undiluted combat-damage
  triggers, haste enablers, alpha-strike finishers (Craterhoof-style "kill the one opponent"
  effects are *more* efficient with only one life total to punch through, not less).
- **Diluted in 1v1**: anything worded "for each opponent" / "to each opponent" — still
  functional, just 1x instead of the 3x a 4-player pod would generate. Not a reason to cut,
  but don't credit it with the multiplayer-pod version of its reputation.
- **A trap in 1v1**: any symmetric effect that also benefits the single opponent (e.g. a
  token/counter doubler worded as "if an effect would create..." with no "under your
  control" restriction — doubles their board too). Rare, but worth an explicit check on every
  proposed doubler/multiplier.

## 3. Diagnose

Same checklist as the paper guide (creature count, draw, ramp, multipliers, protection,
interaction, lands), plus one Arena-specific addition: **haste package**. A 1v1 clock punishes
summoning sickness harder than a multiplayer game does — there's no third player absorbing a
turn of "my board just sits there." Count haste sources explicitly; zero-to-few is a real
diagnosis, not a nice-to-have.

## 4. Propose swaps — gate every add through arena-legality-checker

For every candidate add (from EDHREC top cards, Scryfall discovery search, or a reference
decklist the user supplies), before it goes in the swap table:

1. Batch the candidate names through the **arena-legality-checker** agent.
2. Drop anything that comes back NOT ON ARENA or BANNED — no exceptions, regardless of how
   good it looks on EDHREC (the Sol Ring lesson: 80% inclusion, zero Arena printing).
3. **Do not drop Alchemy-exclusive cards** (`games: ['arena']` only, paper
   `legalities.commander: not_legal`) — they're fair game and often excellent; that flag is
   about paper legality, not whether they're playable here. Actively search for strong
   Alchemy-native fits when the diagnosis has an obvious hole (e.g. `game:arena -game:paper
   id<=<commander identity> o:"haste"` for a haste problem), not just whatever a reference
   list happens to include.
4. Record the verified set/collector number from the agent's output for the final file.

Also **sweep the entire current decklist** through arena-legality-checker at least once per
upgrade pass — a deck can silently carry a card that reads illegal on the exact format in play
even if it imported fine once (verify `legalities.brawl`, don't assume past legality holds).

## 5. Audit before applying

Same discipline as the paper methodology: re-fetch oracle text for every cut, every add, every
near-cut, every card the document makes a claim about. Expect roughly one reversal per five
cuts. If the user challenges a cut or an Arena-legality call, verify their claim immediately —
take it seriously, restore/correct as needed (this has been right before, on both card-text
and Arena-availability calls).

## 6. Apply and verify

- Edit the deck file, preserving the `Commander` / `Deck` header format and each card's real
  `(SET) NUM`.
- Recount to exactly 100 across both sections.
- Check color identity of every add against the commander (arena-legality-checker already
  reports `color_identity`; cross-check against the commander's).

## 7. Document

Write `<deck>-changes.md` following the structure used for
`jetmit-mtg-arena-changes.md`: sources with URLs → verified commander text → **an explicit
methodology note on how Arena legality was verified** (the false-negative / false-positive /
Alchemy-is-fair-game points above) → diagnosis (including the haste check) → swap table with
verified reasons AND confirmed Arena/brawl legality per swap → "challenged and kept" section →
proof section with at least one concrete damage/kill-turn calculation that accounts for the
single-opponent life total → optional upgrades not applied.

## 8. Deliver

SendUserFile both the updated `.txt` and the `-changes.md`. Summarize: the diagnosis, the swap
table, and anything the Arena-legality sweep caught (false negatives corrected, Alchemy cards
included, or paper staples confirmed absent).

## User pushback protocol

If the user challenges a cut, an add, or an Arena-legality verdict, verify immediately against
Scryfall — for legality specifically, re-check both `legalities.brawl` and an all-printings
`game:arena` search, not just the first lookup. If their claim holds, correct the deck and the
document; don't just apologize and move on.
