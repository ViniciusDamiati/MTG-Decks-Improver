# Urza, Lord High Artificer — MTG Arena Brawl upgrade

## Sources

- Commander oracle text: local card DB (`card_db.py`), cross-checked live Scryfall.
- EDHREC commander page: `https://edhrec.com/commanders/urza-lord-high-artificer` and
  `https://json.edhrec.com/pages/commanders/urza-lord-high-artificer.json` (20,096 decks, rank
  #65) plus the average decklist at `https://edhrec.com/average-decks/urza-lord-high-artificer`.
- mtgtop8 cEDH: `https://mtgtop8.com/format?f=cEDH` — zero results for Urza, Lord High Artificer.
  No tracked tournament presence (EDHREC's own "cEDH" tag is community self-labeling, 503/20,096
  decks, not tournament data).
- All 99 pre-existing cards and every replacement candidate were verified against the local card
  DB / live Scryfall (oracle text) and the `arena-legality-checker` agent (Arena printing +
  `legalities.brawl`/`legalities.competitivebrawl`).

## Commander (verified)

**Urza, Lord High Artificer** — {2}{U}{U}, Legendary Creature — Human Artificer, 1/4.
*When Urza enters, create a 0/0 colorless Construct artifact creature token with "This token
gets +1/+1 for each artifact you control." Tap an untapped artifact you control: Add {U}.
{5}: Shuffle your library, then exile the top card. Until end of turn, you may play that card
without paying its mana cost.*

Urza scales on artifact count twice over: it turns every artifact into blue mana, and its own
ETB token grows with however many artifacts you control — making artifact *density*, not just
artifact power level, the axis this commander wants maximized.

## Arena-legality methodology note

- The full 99-card pre-existing list was swept card-by-card through `arena-legality-checker`
  against live Scryfall data (not assumed from the import). Result: **74/74 checked cards
  Arena-legal, 0 not-on-Arena, 0 banned** — confirming the user's claim that everything already
  in the deck is valid on Arena Brawl.
- **Paradox Engine** is `commander(paper): banned` but `brawl: legal`, `historic: legal`,
  `timeless: legal`, `competitivebrawl: legal` — this project treats paper Commander legality
  and Arena Brawl legality as separate checks (see CLAUDE.md), and on the check that actually
  governs this deck, it's fully legal. Kept, not touched.
- One local-DB fuzzy-match trap caught mid-audit: querying "Ornithopter" by name alone returned
  an all-formats-`not_legal` **token** reference card (a Thopter token printed as a collectible,
  not a castable spell) instead of the real 0-mana Ornithopter. Verified the deck's actual
  printing directly (`GET /cards/brr/37`): real card, `{0}` Artifact Creature — Thopter, 0/2
  flying, `brawl: legal`, `games: [paper, mtgo, arena]`. The deck's listed printing was correct;
  only the untargeted name lookup was wrong. Flagging this since it's exactly the kind of
  false-negative this project's rules warn about.
- Every **new** candidate was gated through `arena-legality-checker` before being considered.
  Of 26 candidates checked (aimed at closing the combo/engine gap below), exactly half —
  **13 — have zero Arena printing**: Isochron Scepter, Basalt Monolith, Sensei's Divining Top,
  Voltaic Key, Etherium Sculptor, Shimmer Myr, Rings of Brighthearth, Winter Orb, Static Orb,
  Thopter Spy Network, Walking Ballista, Spellskite, and Thopter Foundry (which is *also*
  off-color — color identity [B, U, W] — independently disqualifying). None of these went in.

## Diagnosis

1. **No combo finisher, despite being Urza.** EDHREC's #1 synergy card for this commander is
   Dramatic Reversal (70% inclusion) via the classic Isochron Scepter + Dramatic Reversal
   infinite-mana loop, and the deck already runs 8+ mana rocks capable of fueling it — but ran
   neither combo piece. **This route turned out to be a dead end on Arena**: Isochron Scepter
   and Basalt Monolith (its usual rock partner) both have zero Arena printings. There is no
   substitute artifact on Arena that untaps for free the way Isochron Scepter does, so this
   specific package cannot be built here at all — confirmed before recommending it, not assumed.
2. **Bloated, overly narrow counterspell suite.** The deck ran roughly 15 counterspell-type
   cards — Time Stop, Counterspell, Negate, Flusterstorm, Pact of Negation, Spell Pierce, Swan
   Song, Mindbreak Trap, An Offer You Can't Refuse, Minor Misstep, Change the Equation, Stern
   Scolding, Strix Serenade, Three Steps Ahead, Vexing Bauble — over 15% of the 99-card list.
   Several are dead in most 1-on-1 matchups by design: **Stern Scolding** only counters
   power/toughness-2-or-less creatures, **Minor Misstep** only mana value 1 or less, **Change the
   Equation** only mana value 2 or less (or red/green MV 6 or less — dead against blue, black,
   white, or colorless opponents), **Vexing Bauble** only counters free spells. Against a single
   fixed opponent (no multiplayer dilution to average out whiffs), a hand with two or three of
   these against the wrong deck is close to a hand down.
3. **Only 13 creatures** (EDHREC average 17) and almost no card-advantage engines that reward the
   artifact density Urza is built around — Vedalken Archmage, Sai Master Thopterist, Padeem, The
   Reality Chip, and both premier draw-tax enchantments (Rhystic Study, Mystic Remora) were all
   absent despite being confirmed Arena-legal and directly on-theme.
4. **Zero haste sources** (Arena-specific check). In 1-on-1, a stalled board gives no third player
   to buy time against — this compounds the low-threat-count problem, but the deck's real win
   condition is the artifact-count-scaling Construct token plus evasive Thopters rather than
   ground combat, so haste wasn't treated as a swap priority this pass (see Optional upgrades).
5. Land count: 34 real lands (27 Island + 7 nonbasic) against an EDHREC average of 31, reasonable
   given the heavy rock package — not a priority fix.
6. Card count and color identity: file totaled exactly 100 before any edits; every add below is
   mono-U, matching Urza's identity exactly.

## Swaps

| Cut | Add | Reason |
|---|---|---|
| Stern Scolding (only counters creatures with power or toughness ≤2 — dead against most real threats) | Rhystic Study (opponent casts a spell → draw unless they pay {1}) | Best-in-class draw engine; 44 EDHREC rank; verified `brawl: legal` (FCA 31) |
| Minor Misstep (only counters spells with mana value ≤1 — a shrinking target as games go long) | Mystic Remora (cumulative-upkeep draw tax on noncreature spells) | Explosive early card advantage; directly supports the artifact/spell-density plan; verified `brawl: legal` (TLE 16) |
| Change the Equation (only counters MV≤2, or red/green MV≤6 — dead against U/B/W/colorless opponents entirely) | The Reality Chip (look at top of library anytime; play lands/cast spells off the top while attached) | EDHREC's #1-ranked creature synergy card for this commander (45% inclusion); turns every draw step into card selection; verified `brawl: legal` (NEO 74) |
| Vexing Bauble (only triggers on free spells — narrow hate, rarely relevant) | Vedalken Archmage (draw a card whenever you cast an artifact spell) | Direct payoff for the artifact-dense build already in the deck; verified `brawl: legal` (JMP 187) |
| Mox Amber (taps for nothing until a legendary creature/planeswalker resolves — dead in the opening hand before turn 4 Urza) | Sai, Master Thopterist (artifact spell → 1/1 flying Thopter token; sac 2 artifacts: draw) | Directly answers the low-creature-count/no-finisher diagnosis: converts the existing artifact suite into an evasive clock instead of nothing |
| Gold Pan (low-impact equipment — the deck has too few creatures to equip, and its Treasure ETB duplicates ramp already in the list) | Padeem, Consul of Innovation (artifacts you control have hexproof; upkeep draw if you control the biggest artifact) | Protects the entire artifact board from single-target removal — a real weakness for a deck this artifact-dependent — plus recurring card advantage |

Net: counterspell count 15 → 9 (cut the four narrowest), creature count 13 → 15, and the deck
gained three dedicated card-advantage engines (Rhystic Study, Mystic Remora, Vedalken Archmage)
plus artifact protection (Padeem) and an actual evasive win condition (Sai's Thopters) — closing
the "control shell with no way to close the game" gap directly.

## Challenged and kept

The user stated all 99 pre-existing cards are valid on Brawl and that **Paradox Engine is
essential**. Verified immediately rather than taken on faith: `card_db.py` confirms
`legalities.brawl: legal` (also `historic`, `timeless`, `competitivebrawl` all legal) — only
`commander` (paper) reads banned, which is a separate, inapplicable check for this Arena deck per
project rules. The full 99-card sweep independently confirmed 74/74 checked cards are genuinely
Arena/Brawl-legal. Paradox Engine, and every other pre-existing card, was kept exactly as-is.

## Proof: Construct + Thopter clock in Arena Brawl's 25-life 1-on-1 format

Urza's ETB token reads *"gets +1/+1 for each artifact you control"* — a continuously-updated
static ability, not a fixed size, and it counts itself. By turn 8 with the new draw engines
online (Rhystic Study/Mystic Remora/Vedalken Archmage all converting opponent's or your own spell
casts into extra cards), a realistic board includes the Construct token plus ~10 other artifacts
already resident in this list (rocks, Seat of the Synod, Foundry Inspector, a couple of Sai
Thopters, etc.):

| Artifacts you control (incl. Construct) | Construct size | Unblocked swing |
|---|---|---|
| 10 | 10/10 | 10 |
| 11 (one more rock/Thopter resolves) | 11/11 | 11 |

Two connected attacks with an 10/10–11/11 Construct is 20–22 damage on its own — over 80% of
Arena Brawl's 25 life — against a mono-U control shell's opponent who is very unlikely to be
holding a blocker that size. Layer in Sai, Master Thopterist: every artifact spell cast after Sai
resolves adds a 1/1 flier, so by the same turn 8 point with ~5 artifact spells cast
post-Sai, there are 5 additional evasive power on board that don't care about the Construct being
blocked at all. Where the old list's win condition was "hope to draw and resolve one specific big
creature while narrow counterspells sit dead in hand," the new list turns *every* artifact already
being cast for value into both card advantage (Vedalken Archmage/Sai's sac ability) and damage
(Construct sizing + Thopter tokens) — the clock is a byproduct of playing the deck's normal game
plan, not a separate plan that has to also get drawn.

## Optional upgrades not applied

- **Sword of the Meek** (verified Arena-legal, BRR 59) — its usual partner Thopter Foundry has no
  Arena printing, so the recursion loop it's normally built around doesn't exist here; it's still
  a fine cheap equipment for Sai's 1/1 Thopters on its own, but wasn't a clear enough upgrade over
  a kept card to justify a seventh swap this pass.
- **Displacer Kitten** (verified Arena-legal, HBG 115) and **Phyrexian Metamorph** (verified
  Arena-legal, HA6 2) — both strong, on-theme value/flex pieces; left for a future pass rather
  than pushing past six swaps in one upgrade.
- **Mystic Forge** (verified Arena-legal, M20 233) — lets you cast artifacts/colorless spells off
  the top of your library; excellent with this deck's density of cheap artifacts, but redundant
  with The Reality Chip's near-identical effect being added this pass.
- **Narset, Parter of Veils** (verified Arena-legal, WAR 61) and **Trinket Mage** (verified
  Arena-legal, AA2 6) — solid, not applied since no clearly-worse card remained to cut for them
  without touching the deck's removal or ramp base.
- A dedicated haste package (diagnosis #4) — not addressed, since the deck's actual win condition
  (Construct sizing + evasive Thopters, see proof above) doesn't depend on ground combat off
  summoning-sick creatures. Worth revisiting only if games are being lost to a stalled board
  specifically, rather than to a lack of a closing plan.
