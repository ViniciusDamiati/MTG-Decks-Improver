---
name: deck-upgrade
description: Run the full evidence-based Commander deck improvement methodology on a decklist file - EDHREC research, diagnosis, verified 1:1 swaps, audit loop, legality check, and change documentation. Use when the user asks to improve, refine, strengthen, or upgrade an EDH/Commander deck. Argument - the deck .txt filename.
---

# Deck Upgrade — full methodology

Follow `DECK-IMPROVEMENT-GUIDE.md` in the project root. Condensed workflow:

## 1. Establish facts

- Read the deck file; verify it totals 100 (`awk 'NF{n+=$1}END{print n}' <deck>.txt`).
  If it doesn't, that's finding #1 — fix it as part of the plan.
- Fetch the **commander's oracle text** from Scryfall (card-verifier agent, or inline
  script per CLAUDE.md). Write one sentence stating the axis the commander scales on.
  Do not skip this — Jetmir (wide bodies) and Bright-Palm (one tall threat) are both
  "token/counter" commanders with opposite correct builds.

## 2. Research

**First reference, always: mtgtop8 cEDH** — https://mtgtop8.com/format?f=cEDH. Check the
commander's competitive presence and what the top-placing lists do before consulting
EDHREC; note explicitly if the commander has no cEDH record.

Then launch the `edhrec-researcher` agent for the commander. In parallel, categorize the
current list yourself: creatures / lands / draw / ramp / multipliers / protection /
interaction, with counts.

## 3. Diagnose

Compare against the guide's checklist table. State the 2-3 real problems (typical: draw
near zero, multiplier pileup, creature count far below average, card-neutral slots).

## 4. Propose 1:1 swaps (8-10)

Each pair: cut candidate + add candidate + reason citing an EDHREC number. Prefer same-MV
replacements filling the diagnosed holes. If EDHREC's top cards don't cover a diagnosed
hole, discover candidates with Scryfall search
(https://scryfall.com/docs/api/cards/search, syntax: https://scryfall.com/docs/syntax):
`GET https://api.scryfall.com/cards/search?order=edhrec&q=id<=<commander identity>
<criteria> legal:commander` — `order=edhrec` surfaces the most-played options first.

## 5. Audit before applying — THE CRITICAL STEP

Batch-fetch oracle text (card-verifier agent) for: every cut, every add, every near-cut,
and every card the document will mention. Expect ~1 reversal per 5 cuts. Check color
identity of adds. If a "weak" card's text reveals hidden strength (Aragorn, Bone Sabres,
Toby, Brigid pattern), keep it and cut something verifiably weaker.

## 6. Apply and verify

- Edit the deck file with 1:1 swaps, preserving alphabetical order and the
  `1 Cardname` / blank line / commander-last format.
- Recount to exactly 100 (the PostToolUse hook will also flag failures).

## 7. Document

Write `<deck>-changes.md` following the structure of `jetmir-changes.md` /
`bright-palm-changes.md`: sources with URLs → verified commander text → diagnosis →
swap table with verified reasons → "challenged, verified, and kept" → proof section with
at least one concrete damage/draw calculation → optional upgrades not applied.

## 8. Deliver

SendUserFile both the updated `.txt` and the `-changes.md`. Summarize: the diagnosis, the
swap table, and any cards the audit saved from cutting.

## User pushback protocol

If the user challenges a cut, verify their claim against oracle text immediately.
Historically the user has been right every time. If their claim holds: restore the card,
find a weaker cut, and correct the document.
