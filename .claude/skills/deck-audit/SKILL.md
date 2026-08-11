---
name: deck-audit
description: Legality and health audit of a Commander decklist file - card count, duplicate detection, color identity against the commander, and composition stats versus EDHREC averages. Use for a quick check without proposing swaps. Argument - the deck .txt filename.
---

# Deck Audit — legality and health check

Read the deck file and report. No swaps, no edits (unless the user asks to fix findings).

## Checks

1. **Count**: quantities must sum to exactly 100 including the commander
   (`awk 'NF{n+=$1}END{print n}' <deck>.txt`). Report over/under precisely.
2. **Singleton**: flag any duplicated non-basic-land line. (Basics: Plains, Island, Swamp,
   Mountain, Forest, Wastes and their snow versions may repeat.)
3. **Color identity**: fetch the commander's `color_identity` (local DB first —
   `python .claude/scripts/card_db.py "<commander name>"` — falling back to Scryfall if not
   found); spot-check any card suspected of being outside it the same way (verify, not
   memory — mana costs miss identity from abilities and back faces).
4. **Composition**: count creatures / lands / draw / ramp / multipliers / protection /
   interaction and compare against the checklist table in `DECK-IMPROVEMENT-GUIDE.md` and
   the EDHREC average for that commander (edhrec-researcher agent if numbers are needed).

## Output

A short report: PASS/FAIL per legality check with exact numbers, then the composition table
with "healthy range" comparisons, then a one-paragraph verdict naming the biggest weakness.
Recommend `/deck-upgrade` if the composition problems warrant a full pass.
