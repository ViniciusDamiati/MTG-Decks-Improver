---
name: card-check
description: Fetch and report the exact verified oracle text of one or more Magic - The Gathering cards from Scryfall. Use when the user asks what a card does, disputes a card's behavior, or before making any claim about card text. Argument - card name(s), comma-separated.
---

# Card Check — verified oracle text

Never answer card-text questions from memory. Fetch from Scryfall:

1. For 1-3 cards, run an inline Python script (written to the scratchpad, then executed —
   never piped to `python -`). For larger batches, launch the `card-verifier` agent.
2. Endpoint: `GET https://api.scryfall.com/cards/named?fuzzy=<urlencoded name>` with BOTH
   headers `User-Agent: deck-helper/1.0` and `Accept: application/json`; ~0.12s sleep
   between requests. Double-faced cards: read the `card_faces` array.
   Docs: https://scryfall.com/docs/api/cards/named. If the user is instead *searching* for
   cards by criteria ("what cards do X"), use the search endpoint
   (https://scryfall.com/docs/api/cards/search) with the query syntax at
   https://scryfall.com/docs/syntax, ordered by `order=edhrec`.
3. Report per card: name, mana cost, type line, P/T, and the complete oracle text —
   verbatim, not paraphrased. Flag fuzzy mismatches.
4. If the check was triggered by a dispute about deck decisions, state plainly whether the
   verified text confirms or contradicts the prior claim, and what should change as a
   result.
