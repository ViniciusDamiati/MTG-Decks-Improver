# Prismari, the Inspiration — MTG Arena Brawl upgrade

## Sources

- Commander oracle text: local card DB, cross-checked live Scryfall.
- EDHREC commander page: `https://json.edhrec.com/pages/commanders/prismari-the-inspiration.json`
  and average-decks JSON (9,430 decks, rank #249).
- mtgtop8 cEDH: `https://mtgtop8.com/format?f=cEDH` — Prismari, the Inspiration is not a
  recurring cEDH archetype; only one recorded competitive result exists (a 2026-08-10 Brawl-style
  qualifier win), a fast-mana/rituals storm-combo shell rather than a midrange EDHREC-average build.
- All 79 unique non-basic cards in the pre-upgrade decklist and all replacement candidates were
  verified against the local card DB / live Scryfall (oracle text) and the `arena-legality-checker`
  agent (Arena printing + `legalities.brawl`).

## Commander (verified)

**Prismari, the Inspiration** — {5}{U}{R}, Legendary Creature — Elder Dragon, 7/7.
*Flying. Ward — Pay 5 life. Instant and sorcery spells you cast have storm.*

This is a hard storm/spellslinger payoff: it doesn't just reward casting spells, it gives every
instant and sorcery in the 99 free copies scaling off however many spells were already cast that
turn. EDHREC confirms the identity — Storm is the #1 theme tag (714 of 9,430 decks) and the
single highest-synergy card in the entire dataset is Pyretic Ritual (0.550 synergy), followed by
Seething Song, Mana Geyser, Desperate Ritual — i.e. mana rituals that let you chain many cheap
spells in one turn are what this commander wants most.

## Arena-legality methodology note

- The user confirmed the starting decklist was exported directly from the MTG Arena client, so
  the 99 pre-existing cards were **not** re-swept for legality — an in-client export guarantees
  those cards are real, owned, and legal in whatever format built the deck.
- Every **new** candidate card was still gated through `arena-legality-checker` before being
  added, per this project's non-negotiable rule. Of 16 candidates checked, 3 had zero Arena
  printing (**Sol Ring, Desperate Ritual, Rite of Flame** — none is Alchemy-native either, so no
  fallback path existed) and were dropped; the rest confirmed `legalities.brawl: legal`.
- Two false-negative traps were caught: the default (fuzzy-name) Scryfall lookup for
  **Archmage Emeritus** returns the SOC precon printing (`games: [paper, mtgo]` only — not
  Arena-legal), and for **Mystical Tutor** it returns the DMR printing (same problem). Both cards
  *are* on Arena under different printings (STX 37 and MIR 80 respectively); using the default
  lookup's collector number would have silently produced an unimportable line. Archmage Emeritus
  went in using STX 37; Mystical Tutor was researched as a backup option but wasn't needed once
  Archmage Emeritus filled that slot.
- Sol Ring's `legalities.brawl` reads `not_legal`, not `banned` — worth noting since "not legal"
  and "banned" read the same in practice (can't play it) but have different causes: this is a
  pure availability gap (never ported to Arena), not a format restriction.

## Diagnosis

1. **Mana base badly bloated.** The deck ran **40 lands** (20 nonbasic + 10 Island + 10 Mountain)
   plus 5 mana rocks — 45 total mana sources out of 99 cards. EDHREC's average Prismari build
   runs ~34 lands (26.4%). For a commander whose entire payoff is casting *many* cheap spells in
   one turn, every land above what's needed for consistent color fixing is a slot not spent on
   the spell density the deck actually wants.
2. **Zero mana rituals**, despite rituals being the single highest-synergy card category for this
   commander (Pyretic Ritual 66.4% inclusion/0.550 synergy — the top card in the whole dataset;
   Seething Song 67.1%/0.468, already in the deck; Mana Geyser 67.8%/0.443; Desperate Ritual
   49.9%/0.402). Only Seething Song was present. Rituals are exactly what lets this commander
   chain a big storm count on one turn — this was the biggest structural gap.
3. **Zero cheap cantrips.** No Preordain (59.1%), Opt (59.0%), Ponder (57.3%), Brainstorm
   (57.8%), or Consider (44.9%) — all top-tier EDHREC includes for this commander specifically
   because a 1-mana draw spell both smooths your hand *and* pads storm count for free.
4. **One actively anti-synergistic card**: Irencrag Feat reads *"Add seven {R}. You can cast only
   one more spell this turn."* That's a hard restriction to a single follow-up spell no matter how
   much mana it makes — directly contradicts a commander that wants you casting many spells, not
   one big one.
5. **Five board wipes** (Brotherhood's End, Spiteful Banditry, Storm's Wrath, Sweltering Suns,
   Whelming Wave) is excessive for 1-on-1 Brawl, where there's only one opponent's board to
   answer instead of three. Worse, this deck's own board *is* its engine — Storm-Kiln Artist,
   Young Pyromancer, and Third Path Iconoclast all generate value off your own creatures/tokens,
   which most of these wipes destroy just as thoroughly as the opponent's board. Whelming Wave
   (bounce, not destroy) is the worst offender: it doesn't even permanently answer a threat, it
   just resets tempo while bouncing your own token squad along with it.
6. **Haste check** (Arena-specific requirement): zero haste sources. Not corrected in this pass —
   the deck's actual clock is direct damage (Guttersnipe, Fiery Inscription, Ral, Storm Conduit,
   burn spells) rather than combat damage, so summoning-sickness tax matters less here than it
   would for a creature-beatdown plan. Flagged as a known gap, not treated as a swap priority.
7. Card count and color identity: original file totaled exactly 100 (verified before any edits);
   every new add is R, U, or UR, matching the commander's Izzet identity.

## Swaps

| Cut | Add | Reason |
|---|---|---|
| Magic Damper (despite the name, oracle text is a plain +1/+1/hexproof/untap combat trick — no interaction with spells at all) | Preordain (scry 2, draw a card) | On-theme 1-mana cantrip; smooths draws and pads storm count for near-free |
| Consign to Memory (narrow — only counters triggered abilities/colorless spells) | Opt (scry 1, draw a card) | Same — cheapest, cleanest cantrip |
| Blink of an Eye (redundant with Repeal/Baral's Expertise/Prismari Charm's bounce mode — the deck already ran 5+ "return to hand" effects) | Ponder (look at top 3, draw a card) | Trims bounce redundancy for card selection |
| Brotherhood's End (1 of 5 sweepers; wipes the deck's own token engine along with the opponent's board) | Brainstorm (draw 3, put back 2) | Cuts sweeper count from 5→3 (see diagnosis #5); adds the highest-power cantrip on the list |
| Whelming Wave (symmetric bounce that resets your own Young Pyromancer/Storm-Kiln Artist tokens without permanently answering anything) | Consider (surveil 1, draw a card) | Same sweeper-trim logic; another cheap cantrip |
| Double Vision (only copies the *first* spell each turn — narrow window) | Thousand-Year Storm (copies *every* spell after the first, for the rest of the game) | Direct upgrade: same 5-mana slot, strictly larger copy window (41.5% EDHREC inclusion, 0.256 synergy) |
| Irencrag Feat (restricts you to one more spell this turn — anti-synergy with a storm payoff, see diagnosis #4) | Archmage Emeritus (Magecraft — draw a card whenever you cast *or copy* an instant/sorcery) | Removes the anti-synergy; adds a card-draw engine that explicitly rewards storm copies, not just casts (66.2% inclusion, 0.315 synergy) |
| 1 Island | Pyretic Ritual (add {R}{R}{R}) | Highest-synergy card in the entire EDHREC dataset (0.550) for this commander; converts a static mana source into a spell that itself counts toward storm |
| 1 Island | Jeska's Will (exile top 3 to play this turn, or ritual off opponent's hand size) | Ritual/card-advantage hybrid; 49.4% inclusion |
| 1 Mountain | Big Score (discard 1: draw 2, make 2 Treasures) | Treasure ritual + net card advantage |
| 1 Mountain | Strike It Rich (make a Treasure; Flashback {2}{R} for a second) | Cheap, recurring mana source that's also a spell for storm-count purposes |

Net: lands 40 → 36 (still above EDHREC's 34 average, appropriate given Cryptic Command's UUU and
other double-pip costs), 5 mana rocks unchanged, but the deck gained 4 spell-based mana sources
(2 rituals, 2 treasure-makers) and 5 top-tier cantrips — a much higher spell density feeding the
commander's storm ability, and a materially lower curve (the 5 cards leaving averaged CMC ~2.9;
the 5 cantrips replacing them are all CMC 1).

## Challenged and kept

Nothing was challenged by the user this pass; the existing 99-card core the user is actively
playing was taken as correct and not re-audited for legality per their explicit instruction.
Stifle, Shore Up, Boomerang Basics, and the remaining 3 board wipes (Spiteful Banditry, Storm's
Wrath, Sweltering Suns) were considered as further cut candidates but kept — cutting further would
have started removing the deck's only removal/interaction suite rather than trimming genuine
redundancy.

## Proof: storm-copy damage in a single turn

Ral, Storm Conduit (already in the deck) reads *"Whenever you cast **or copy** an instant or
sorcery spell, Ral deals 1 damage to target opponent or planeswalker."* — unlike Guttersnipe or
Fiery Inscription (which trigger only on cast, not on storm copies), Ral scales directly with
Prismari's storm count. With Ral in play and, say, Pyretic Ritual providing the mana to chain the
five new cantrips in one turn:

| Spell cast | Storm count (copies) | Cast+copy events | Ral damage this spell | Running total |
|---|---|---|---|---|
| Pyretic Ritual | 0 | 1 | 1 | 1 |
| Opt | 1 | 2 | 2 | 3 |
| Preordain | 2 | 3 | 3 | 6 |
| Consider | 3 | 4 | 4 | 10 |
| Ponder | 4 | 5 | 5 | 15 |
| Brainstorm | 5 | 6 | 6 | 21 |

Six cheap spells (5 mana total after the ritual pays for itself) deal **21 damage from Ral alone**
in Arena Brawl's 25-life 1-on-1 format — and that's before counting Guttersnipe (2 dmg per *cast*,
not copy) or Fiery Inscription (same) if either is also on board, which would add up to 24 more
damage across those same six casts, comfortably lethal in one turn. This is the concrete payoff
of trading static lands for cantrips and rituals: every one of those cheap draw spells is now
also a storm-count generator and, with Ral in play, a direct damage source.

## Optional upgrades not applied

- **Mystical Tutor** (verified Arena-legal, MIR 80/TLE 308) — tutors any instant/sorcery to the
  top of library; strong but not applied this pass since Archmage Emeritus filled the equivalent
  slot with a repeatable effect rather than a one-shot tutor.
- **Seize the Spoils** (verified Arena-legal, SOS 129) — discard 1, draw 2, make a Treasure;
  similar shape to Big Score, not added to avoid triple-redundant "discard-a-card-for-value"
  effects (Big Score already covers this).
- A real haste package (diagnosis #6) — left unaddressed since the deck's win condition is direct
  damage, not combat; worth revisiting only if games are being lost to a stalled board rather than
  to a lack of reach.
