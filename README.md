# MTG-Decks-Improver

A Commander (EDH) deck workshop for Claude Code — decklists, upgrade documentation, and
an evidence-based methodology (EDHREC + mtgtop8 + Scryfall) for improving them.

See `CLAUDE.md` for the full working conventions and `DECK-IMPROVEMENT-GUIDE.md` for the
improvement methodology itself.

## Layout

- `edh/` — paper Commander decklists, one card per line (`<commander>.txt`), alphabetical
  with the commander last, plus a `<commander>-changes.md` documenting each upgrade.
- `arena/` — MTG Arena decklists in the MTGA client's native import/export format
  (`<commander>-mtg-arena.txt`), plus matching `-changes.md` files.
- `DECK-IMPROVEMENT-GUIDE.md` — the deck-improvement methodology.
- `.claude/skills/` — `/deck-upgrade`, `/arena-deck-upgrade`, `/card-check`, `/deck-audit`.
- `.claude/agents/` — `card-verifier`, `edhrec-researcher`, `arena-legality-checker`.
- `.claude/hooks/check-deck-count.py` — verifies every deck totals 100 cards on edit.

## Usage

Open this folder in Claude Code and run one of the skills above against a decklist, e.g.:

```
/deck-upgrade edh/jetmir.txt
/arena-deck-upgrade arena/najeela.txt
```
