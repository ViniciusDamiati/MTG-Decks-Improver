---
name: card-check
description: Fetch and report the exact verified oracle text of one or more Magic - The Gathering cards from Scryfall. Use when the user asks what a card does, disputes a card's behavior, or before making any claim about card text. Argument - card name(s), comma-separated.
---

# Card Check — verified oracle text

Never answer card-text questions from memory. Check the local DB first, Scryfall for misses:

1. Run `python .claude/scripts/card_db.py "<name>" ...` from the project root. Use the
   `"found": true` rows directly. For any `"found": false` rows, or if the user is instead
   *searching* for cards by criteria ("what cards do X" — the local DB only supports lookup
   by name, not arbitrary queries), fall back to the live API below. For larger misses
   batches, launch the `card-verifier` agent instead of doing it inline.
2. Endpoint: `GET https://api.scryfall.com/cards/named?fuzzy=<urlencoded name>` with BOTH
   headers `User-Agent: deck-helper/1.0` and `Accept: application/json`; ~0.12s sleep
   between requests. Double-faced cards: read the `card_faces` array.
   Docs: https://scryfall.com/docs/api/cards/named. For criteria search, use the search
   endpoint (https://scryfall.com/docs/api/cards/search) with the query syntax at
   https://scryfall.com/docs/syntax, ordered by `order=edhrec`.
3. Report per card: name, mana cost, type line, P/T, and the complete oracle text —
   verbatim, not paraphrased. Flag fuzzy mismatches.
4. If the check was triggered by a dispute about deck decisions, state plainly whether the
   verified text confirms or contradicts the prior claim, and what should change as a
   result.
