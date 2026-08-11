# Decks — Commander (EDH) deck workshop

This folder holds Commander decklists and their upgrade documentation. The full methodology
lives in `DECK-IMPROVEMENT-GUIDE.md` — read it before doing any deck-improvement work.

## File conventions

- Decklists: `<commander-short-name>.txt` — one card per line as `1 Cardname`, list kept
  **alphabetical**, then a blank line, then the commander as the last line.
- **MTG Arena decklists are the exception**: `<commander-short-name>-mtg-arena.txt` uses the
  MTGA client's native import/export shape instead — `Commander` header, `1 <Name> (SET) NUM`,
  blank line, `Deck` header, then the remaining 99 cards (order not required to be alphabetical;
  MTGA's own exports aren't). Do not rewrite an Arena file into the paper alphabetical format —
  it won't re-import into the client. See `arena-deck-upgrade` skill and `arena-legality-checker`
  agent below — Arena decks additionally require every card to be verified as actually available
  and legal on Arena, which is a materially different check from paper Commander legality.
- Every deck must total **exactly 100 cards including the commander**. Verify with:
  `awk 'NF{n+=$1}END{print n}' <deck>.txt` for paper lists (a PostToolUse hook also checks this
  on every edit); for Arena lists, skip the `Commander`/`Deck` header lines when counting
  (`awk 'NF{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/){n+=$i; break}}END{print n}' <deck>.txt`).
- Change documentation: `<commander-short-name>-changes.md` next to the list.

## Non-negotiable rules

1. **Verify oracle text before every decision.** Never cut, add, keep, or describe a card
   from memory — look it up first (local card DB, falling back to live Scryfall — see
   below). Past sessions were corrected multiple times because remembered card text was
   wrong (Divine Visitation, Toby, Brigid, Aragorn).
2. **Swaps are 1:1.** The deck stays at 100 through every edit.
3. **Every swap needs a data point** (EDHREC inclusion/synergy %, tournament presence) plus
   a reason derived from verified text.
4. **Check color identity** of every added card against the commander.
5. If the user challenges a cut, verify their claim against oracle text — historically the
   user has been right. Restore the card and find a weaker cut if their claim holds.
6. Deliver both the updated `.txt` and the `-changes.md` via SendUserFile when done.

## Data sources (what works / what doesn't)

- **Local card database — always check FIRST for oracle text/color identity**:
  `python .claude/scripts/card_db.py "Card Name" ["Card Name" ...]` queries a local
  Postgres DB (`mtg_cards`, table `cards`) loaded from Scryfall's `oracle-cards` bulk
  dump (one row per unique card, exact name match then trigram fuzzy fallback). Prints
  one JSON object per line; `"found": false` means the card isn't in the local dump
  (brand new card, or DB stale) — fall back to the live Scryfall lookup below for those.
  Refresh periodically (new sets/errata land every few weeks) with
  `python .claude/scripts/refresh_card_db.py`. Schema: `.claude/scripts/schema.sql`.
  **Does not replace `arena-legality-checker`** — the dump has only the newest printing
  per card, not full per-printing/Arena-availability data.
- **mtgtop8 cEDH — always the FIRST reference for competitive data**:
  https://mtgtop8.com/format?f=cEDH. Check the commander's competitive record there
  before consulting EDHREC or anything else; if the commander is absent from cEDH,
  record that as a finding.
- **Scryfall API** (docs: https://scryfall.com/docs/api) — use when the local DB misses:
  - Lookup: `GET https://api.scryfall.com/cards/named?fuzzy=<name>`
    (https://scryfall.com/docs/api/cards/named) — requires BOTH `User-Agent` and
    `Accept: application/json` headers. Loop per card (~0.1s sleep); the batch POST
    endpoint returns 400s. DFCs: read `card_faces`, not top-level `oracle_text`.
  - Discovery: `GET https://api.scryfall.com/cards/search?order=edhrec&q=<query>`
    (https://scryfall.com/docs/api/cards/search, syntax: https://scryfall.com/docs/syntax)
    — find candidates by color identity/text/type, sorted by EDHREC popularity,
    e.g. `q=id<=rgw t:creature mv<=3 o:"+1/+1 counter" legal:commander`.
- **EDHREC**: `https://edhrec.com/commanders/<slug>`, `https://edhrec.com/average-decks/<slug>`,
  and `https://json.edhrec.com/pages/commanders/<slug>.json` — all fetchable.
- **Moxfield**: blocked (403). Use the EDHREC average decklist as the aggregate proxy.
- Write Python fetch scripts to the scratchpad directory and run them as files; piping
  scripts to `python -` via heredoc fails on this machine.

## Tooling in this project

- Skill `/deck-upgrade <deck>.txt` — run the full improvement methodology on a paper deck.
- Skill `/arena-deck-upgrade <deck>.txt` — the same methodology adapted for MTG Arena decks:
  Arena-legality-gated swaps, 1v1-aware reasoning, MTGA import format preserved. Use this
  instead of `/deck-upgrade` whenever the deck is an Arena deck (`*-mtg-arena.txt`) or the user
  says they play on Arena.
- Skill `/card-check <card names>` — fetch verified oracle text for specific cards.
- Skill `/deck-audit <deck>.txt` — legality pass: count, duplicates, color identity.
- Agent `card-verifier` — batch-fetches oracle texts, local DB first then Scryfall for misses.
- Agent `edhrec-researcher` — pulls commander stats, top cards, and the average decklist.
- Agent `arena-legality-checker` — verifies whether specific cards actually exist and are
  legal on MTG Arena (distinct from paper Commander legality — see the Arena file-convention
  note above). Use before adding any card to an Arena deck, or to sweep an existing Arena deck.
- Hook `.claude/hooks/check-deck-count.py` — warns automatically when an edited deck file
  doesn't total 100.
