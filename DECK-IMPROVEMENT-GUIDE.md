# How to Improve a Commander Deck — The Methodology

A repeatable, evidence-based process for upgrading EDH decks, distilled from the Jetmir
(July 2026) and Bright-Palm (July 2026) upgrade projects. The core principle:

> **Never trust memory about what a card does. Verify every card's oracle text before
> cutting it, adding it, or writing a single word about it.**

Both projects had cuts reversed and arguments corrected only because the actual card text
was checked. Divine Visitation *transforms* tokens (it doesn't multiply them). Aragorn,
Hornburg Hero is secretly a second commander trigger. Bone Sabres reads unimpressive and
is actually four counters per attack. Memory lies; Scryfall doesn't.

---

## Step 0 — Read the commander. Actually read it.

Fetch the commander's exact oracle text from Scryfall first. Everything downstream depends
on what the commander literally rewards:

- **Jetmir** counts creatures (3/6/9 thresholds) → the deck wants *bodies*, cheap and wide.
- **Bright-Palm** doubles counters on *one target* per attack → the deck wants one
  exponential threat, trigger amplifiers, and evasion for a single creature.

Two "token/counter decks" with opposite correct builds. Write down, in one sentence, the
axis the commander scales on. Every later decision is judged against that sentence.

## Step 1 — Gather data (in this order)

1. **mtgtop8 cEDH — ALWAYS the first reference**: https://mtgtop8.com/format?f=cEDH
   Before touching EDHREC, check the commander's competitive record: browse the cEDH
   section's recent events and archetypes for the commander. The competitive extreme is
   a controlled experiment — with no budget limit, what axis do the best builders pick?
   (Jetmir cEDH: 50 creatures, 25 lands, 7 one-mana dorks — creature density wins.)
   If the commander has no cEDH presence, record that finding too: it means every later
   judgment is made against the casual/EDHREC baseline alone.
2. **EDHREC commander page** — `https://edhrec.com/commanders/<commander-slug>`
   Deck count, themes, top synergy cards (high synergy % = played *because of this
   commander*, not just generically good).
3. **EDHREC JSON** — `https://json.edhrec.com/pages/commanders/<slug>.json`
   Per-category top cards with inclusion % and synergy scores. The richest single source.
4. **EDHREC average decklist** — `https://edhrec.com/average-decks/<slug>`
   Composition baseline: creature count, land count, category sizes. This is the
   aggregated-Moxfield proxy (Moxfield itself blocks scrapers with 403s — don't bother).
5. **Scryfall API for every card text** — see the technical appendix.

## Step 2 — Diagnose against the checklist

Count what the deck actually has and compare with the average list:

| Check | Healthy range | Common disease |
|---|---|---|
| Creature count | Within ~5 of the EDHREC average | Too few bodies; commander scaling starves |
| Card draw | 6+ real effects (repeatable > one-shot) | The #1 hole in casual decks — both projects had ~2 |
| Ramp | 8-12 pieces, some at 1 MV, some board-independent | All ramp scales with the board = all dead after a wipe |
| Multipliers/anthems | 2-4 | "Multiplier pileup": five doublers, nothing to double |
| Protection | 3-6 | Hoarding 7+ wipes-insurance instead of refuel |
| Interaction | 5-8 removal pieces | Usually fine; don't over-add |
| Lands | 35-37 with a real reason for each tapped land | Always-tapped monocolor lands (strict upgrades exist) |
| **Total count** | **Exactly 100** | **Actually count it.** Jetmir's list was 103 and nobody had noticed. |

Rules of thumb proven across both projects:

- **Bodies/engines beat multipliers.** A multiplier is dead on an empty board; a creature
  is never dead and feeds the commander. Cut the 4th and 5th doubler before anything else.
- **Draw beats stacked protection.** Wipes are survivable if you can refuel; 7 protection
  spells are dead draws in the games where no wipe comes.
- **Card-neutral, board-neutral cards are the weakest slots** (tutors like Idyllic Tutor,
  do-nothing-on-arrival artifacts like Panharmonicon in a low-ETB deck). They cost a card
  and a turn and change nothing on the table.
- **Instant-speed versions are worth a premium** (March of the Multitudes vs Saproling
  Symbiosis; Call the Coppercoats mid-combat).
- **A 1-mana dork is double value** in creature-counting decks: it ramps AND counts.

## Step 3 — Propose swaps as 1:1 pairs

- Keep the deck at exactly 100 through every edit.
- Pair each cut with an add filling the same or a better role (same MV slot when possible).
- For every pair, write the reason **from the verified oracle texts plus a data point**
  (inclusion %, synergy score, tournament presence). "It's good" is not a reason;
  "45% inclusion, copies the commander's trigger, turns 8 counters into 32" is.
- 8-10 swaps is the sweet spot for a casual upgrade. More than that changes the deck's
  identity; fewer usually leaves the diagnosis unaddressed.

## Step 4 — The audit loop (this is where the value is)

Before finalizing, re-fetch and re-read the oracle text of:

1. every card being cut,
2. every card being added,
3. every card you *almost* cut,
4. every card your document makes a claim about (including the commander).

Expect roughly one reversal per five cuts. Real examples:

- **Kept after audit:** Toby (2 bodies + flying grant), Brigid (tokens AND mana),
  Aragorn Hornburg Hero (doubles counters on every renowned attacker), Bone Sabres
  (4 counters/attack), Mayael's Aria (a literal "win the game" check).
- **Doc errors caught:** Jetmir grants trample at 6 (not vigilance); Kutzil locks the whole
  turn (not just combat); Divine Visitation transforms (doesn't multiply).
- **Cut confirmed by text:** Ghired needs tokens made *this turn* tapped by *nontoken*
  creatures — two conditions that never line up; Urabrask's Forge token is sacrificed at
  end step and never counts toward thresholds.

If the deck owner challenges a cut — take it seriously. Both times a user pushed back
("Toby is two bodies", "Brigid makes tokens AND mana"), the user was right and the
methodology was wrong. Verify their claim against the text; if it holds, restore the card
and find a weaker cut.

## Step 5 — Legality and delivery

1. Recount: quantities must sum to exactly 100 including the commander.
2. Check color identity of every add against the commander.
3. Keep the list alphabetical, `1 Cardname` per line, blank line, commander last.
4. Write `<deck>-changes.md` next to the list: sources with URLs, verified commander text,
   diagnosis, swap table with reasons, "challenged and kept" section, proof section
   (do the damage/draw math), optional upgrades not applied.
5. Deliver both files.

## Step 6 — Prove it with math

Every document should contain at least one concrete calculation, because numbers are what
convince:

- Jetmir: at 9 creatures, Jetmir + eight 1/1s = **80 damage in one swing** (8/4 double
  strike ×2 + eight 4/1 double strikers ×8).
- Bright-Palm: 8 counters + attack trigger + Strionic Resonator = **32 counters in one
  combat**; with Doubling Season each doubling becomes a tripling (9× per combat).

If you can't compute why the new configuration wins harder, you haven't finished the
analysis.

---

## Technical appendix — data access that actually works

**Scryfall API** (the only reliable card-text source). Official docs:

- API overview: https://scryfall.com/docs/api
- Named lookup: https://scryfall.com/docs/api/cards/named
- Search endpoint: https://scryfall.com/docs/api/cards/search
- Search syntax reference: https://scryfall.com/docs/syntax

```
GET https://api.scryfall.com/cards/named?fuzzy=<urlencoded name>
```

- BOTH headers are mandatory or you get 400/403:
  `User-Agent: deck-helper/1.0` and `Accept: application/json`
- Sleep ~0.1s between requests.
- The batch endpoint `POST /cards/collection` is unreliable (400s) — loop per card instead.
- Double-faced cards have no top-level `oracle_text`; read the `card_faces` array.
- On Windows, write the Python fetch script to a file and run it — piping via heredoc to
  `python -` fails.

**Scryfall search for discovering add-candidates** — beyond looking up known cards, the
search endpoint finds cards you didn't know existed, and `order=edhrec` sorts results by
EDHREC popularity:

```
GET https://api.scryfall.com/cards/search?order=edhrec&q=<urlencoded query>
```

Example — cheap counter-synergy creatures legal in a Naya commander deck:

```
q = id<=rgw t:creature mv<=3 o:"+1/+1 counter" legal:commander
```

Useful operators (full list at https://scryfall.com/docs/syntax): `id<=rgw` (color
identity fits the commander), `o:"exact text"` (oracle text contains), `t:` (type),
`mv<=` (mana value), `legal:commander`, `-is:reprint`. Results are paginated via
`next_page`; the `has_more` flag tells you when to stop.

**mtgtop8 (cEDH)**: https://mtgtop8.com/format?f=cEDH — the mandatory first stop of every
deck-improvement task; navigate from there to the commander's archetype and recent event
lists. **EDHREC**: fetch the HTML pages or the JSON endpoint (`json.edhrec.com/pages/...`)
— both work with a normal fetch. **Moxfield**: blocked (403 on site and api2); use the
EDHREC average decklist as the aggregate proxy.

**Deck count check** (Git Bash):

```sh
awk 'NF{n+=$1}END{print n}' deckname.txt   # must print 100
```
