# Tezzeret, Master of the Bridge — Arena (Historic Brawl) Upgrade

## Sources

- Commander oracle text: local `card_db.py` + live Scryfall (matched exactly).
- mtgtop8 cEDH (`https://mtgtop8.com/format?f=cEDH`): no presence — expected, planeswalker
  commanders don't exist in paper Commander, so there is no cEDH data for this card.
- EDHREC (`edhrec.com/commanders/tezzeret-master-of-the-bridge`,
  `json.edhrec.com/pages/commanders/tezzeret-master-of-the-bridge.json`, `edhrec.com/brawl`):
  **404/403 across every URL tried — EDHREC has no page for this commander at all.** No Brawl
  section exists on EDHREC.
- Moxfield: blocked (403) per project convention, not fetched directly.
- **mtgdecks.net** Historic Brawl archetype tracker
  (`mtgdecks.net/Historic-Brawl/tezzeret-master-of-the-bridge`): ~16 submitted ladder decks,
  win rates clustered 40–60%.
- **AetherHub** aggregated meta build (`aetherhub.com/Deck/tezzeret-master-of-the-bridge-1346306`):
  49% win rate (95W-97L) aggregate, composition stats.
- **MTGGoldfish** archetype page (`mtggoldfish.com/archetype/brawl-tezzeret-master-of-the-bridge`):
  one fully retrievable 100-card decklist ("tezzy" by Sharpio) used as the primary structural
  reference for this upgrade.
- MTG Arena Zone deck (2020, 60-card pre-2022-format-change) checked but discarded as stale —
  Historic Brawl moved to 100 cards in 2022.

## Commander (verified oracle text)

**Tezzeret, Master of the Bridge** — {4}{U}{B} — Legendary Planeswalker — Tezzeret, 5 loyalty
> Creature and planeswalker spells you cast have affinity for artifacts.
> +2: Deal X damage to each opponent, where X is the number of artifacts you control. You gain X life.
> −3: Return target artifact card from your graveyard to your hand.
> −8: Exile the top ten cards of your library. Put all artifact cards from among them onto the battlefield.

Axis it scales on: **number of artifacts you control** — simultaneously a cost-reducer
(affinity, applies to creatures *and* planeswalkers) and a damage/lifegain engine (+2). Every
artifact in the deck is doing double duty; the commander rewards a high, steady artifact count
far more than it rewards any single big artifact.

## Methodology note — Arena legality verification

Per user instruction, **the existing 99 cards were not re-swept** — this list was exported
directly from the Arena client, so it's already known-legal. All 27 candidate additions
considered for this upgrade (finishers, planeswalkers, counterspells, removal, utility lands)
were independently verified through the `arena-legality-checker` agent against live Scryfall
before being added — checking `legalities.brawl`, actual Arena availability (`games` includes
`arena`), and color identity. This caught several **false-negative traps**: cards whose default
Scryfall printing is paper/MTGO-only (Karn's Bastion, Castle Locthwain) that do have a separate
Arena-legal printing once every printing is searched — those would look "not on Arena" on a
naive single-printing lookup. It also confirmed several premium finishers are only reachable on
Arena through non-default anthology/remaster printings (Ulamog via HA3, Kozilek via EA2, Emrakul
via SIR, Wurmcoil Engine and Platinum Angel via BRR) — the deck's added cards below use those
verified set/numbers, not the default paper printing. No Alchemy-exclusive cards were needed
here, but the existing **Emporium Thopterist** (Y24, an Arena-only conjure card) was confirmed
fair game under this ruleset and left untouched.

## Diagnosis

- **Zero counterspells.** For a UB shell in 1v1, a hard counter is undiluted — it stops *the*
  threat, not just one of several opponents' threats. This deck had none.
- **Thin, narrow-only interaction.** Removal was limited to Cyclonic Rift, Feed the Swarm,
  Withering Torment, and Urn of Godfire (a 6-mana sink) — plus **Singularity Rupture**, a
  symmetric "destroy all creatures" wipe with no restriction to opponents' creatures, which
  actively works against a deck whose plan is to hold a wide artifact board for the commander's
  +2 damage/lifegain scaling.
- **No resilient win condition.** The deck's plan (chip damage off +2, grind card advantage)
  has no way to close a game quickly or protect against being ground out itself. Kappa Cannoneer
  is a fine attacker but dies to any removal.
- **Four dead-weight artifacts.** Mox Amber (needs a legendary *creature* — this deck runs none,
  only legendary planeswalkers, so it was a 0-cost do-nothing all game), Esoteric Duplicator
  (marginal card-draw-for-2-plus-sac value), Worldwalker Helm (needs artifact *token*
  generation the deck barely has), and Sculpting Steel (situational, can whiff or even copy an
  opponent's artifact).
- **Two narrow utility lands.** Amonkhet Raceway and Muraganda Raceway both require building up
  "speed" over several turns before doing anything relevant, and Amonkhet Raceway's haste grant
  has no "creature you control" restriction (technically usable to speed up an opponent's
  creature, though irrelevant in practice).
- **Haste count: effectively zero.** No creature in the deck has haste; only Amonkhet Raceway
  could theoretically grant it, and only after 4 turns of accruing speed. Not the top problem —
  this commander's plan is grindy value/damage-over-time, not an alpha-strike aggro clock — but
  worth naming per the methodology's explicit haste check. Not addressed directly here since
  Wurmcoil Engine/Platinum Angel (the finisher adds) are value-resilience threats, not haste
  threats, which fits the deck's actual plan better than forcing in a haste package it wasn't
  built around.
- **Mana base is large (36 lands) but not actually excessive** given ~11 ramp/fixing artifacts
  that double as commander fuel — left the count at 36, upgrading quality (see swaps) rather
  than cutting into a deck that wants to hit land drops into 6-mana finishers.

## Swaps (7, all verified Arena/Brawl-legal)

| # | Cut | Why | Add | Why | Arena legality |
|---|-----|-----|-----|-----|-----------------|
| 1 | Mox Amber (BRR) 35 | Dead card — needs a legendary *creature*, deck has none, only legendary planeswalkers | **Wurmcoil Engine** (BRR) 63 | Colorless finisher, affinity-discounted; lifelink+deathtouch halves are resilient to removal (still gain value if it dies) and stabilize the life total this commander is also trying to protect via +2 lifegain | Verified: on Arena, `brawl: legal`, colorless |
| 2 | Esoteric Duplicator (BIG) 5 | Marginal value (pay 2, sac another artifact, maybe get a copy later) — too slow/conditional | **Platinum Angel** (BRR) 41 | "You can't lose the game and your opponent can't win the game" while it survives — a hard stabilizer in 1v1 where there's only one opponent's win condition to shut off; affinity-discounted from {5} | Verified: on Arena, `brawl: legal`, colorless |
| 3 | Worldwalker Helm (BIG) 7 | Needs artifact *token* generation this deck barely does; low standalone impact | **Counterspell** (MAR) 52 | First hard counter in the deck — in 1v1 a counter is undiluted, it answers the one threat that matters, not 1-of-3 | Verified: on Arena, `brawl: legal`, U |
| 4 | Sculpting Steel (BRR) 50 | Situational — can whiff (nothing worth copying) or even copy an opponent's better artifact | **Swan Song** (HA3) 9 | 1-mana answer to the removal/wipes/enchantments aimed at this deck's engine (incl. protecting itself from a mirrored Encroaching Mycosynth-style effect); cheap tempo-positive interaction | Verified: on Arena (Historic Anthology 3 printing), `brawl: legal`, U |
| 5 | Singularity Rupture (EOE) 228 | Unconditional "destroy all creatures" — symmetric, actively undercuts this deck's own go-wide artifact-creature board that feeds the commander's +2 | **Infernal Grasp** (MID) 107 | Efficient 2-mana unconditional creature removal, single-target so it doesn't blow up our own board | Verified: on Arena, `brawl: legal`, B |
| 6 | Amonkhet Raceway (DFT) 248 | Narrow — 4 turns of speed-building before any effect matters; the haste mode targets "any creature," not restricted to yours | **Otawara, Soaring City** (NEO) 271 | Strictly better utility land: taps for U, and doubles as a late-game bounce spell (`{3}{U}, discard: return target artifact/creature/enchantment/planeswalker to hand`) — real interaction stapled to a land slot | Verified: on Arena (NEO printing), `brawl: legal`, U |
| 7 | Muraganda Raceway (DFT) 257 | Narrow — colorless-only ramp gated behind the same slow speed mechanic | **Command Tower** (ELD) 333 | Unconditional perfect fixing for the commander's exact UB identity — strictly better than a colorless-only land in a two-color deck | Verified: on Arena, `brawl: legal`, colorless (taps for U or B) |

Net effect: mana base stays at 36 lands (quality upgrade, not a count change), interaction goes
from 4 narrow/risky spells to 6 (1 counter added, 1 counter-protection, symmetric wipe swapped
for single-target removal), and the deck gains two resilient finishers that both get cheaper
from the commander's own affinity static.

## Challenged and kept

No cuts were challenged by the user in this session — this was a first-pass upgrade request.
Cards reconsidered and explicitly kept during diagnosis:

- **Demonic Junker** (DFT) 83 — initially flagged as a possible "symmetric" cut on a first read
  of "for each player, destroy up to one target creature that player controls." Re-verified: the
  controller of the trigger chooses targets, and "up to one" means 0 is a legal choice for your
  own side — so in practice this is a one-sided removal spell on a 4/3 body (that can also
  self-target for a +1/+1 counter payoff if you want to feed it a creature you don't need). Kept.
- **Vexing Bauble** (MH3) 212 — symmetric in wording (counters any player's free spells) but
  purely defensive in practice for a deck with no free-spell plan of its own; a cheap 1-drop
  that also pads the artifact count for affinity/damage. Kept.
- **Paradox Engine** (KLR) 259 — banned in paper Commander, but that's a paper-only restriction;
  confirmed still `brawl: legal` for Historic Brawl, and it's a real payoff for this deck's low
  curve of cheap artifacts (recast a cheap spell, untap rocks/creatures). Kept, unchanged.
- **Encroaching Mycosynth** (ONE) 47 — text only affects permanents *you* control/own, not
  symmetric despite the "trap doubler" pattern the methodology calls out to check. Kept.

## Proof — closing the game in 1v1

Starting at a typical Historic Brawl 25 life. With ~10 artifacts online (very achievable by
turn 7-8 given ~11 ramp/fixing pieces plus cheap artifact creatures), the commander's +2 alone
deals 10 and gains 10 — two activations (turns 4 apart if untouched) is 20 damage and swings the
life gap by 40 total, which most 1v1 games don't survive. With **Wurmcoil Engine** or
**Platinum Angel** now in the 99, the deck has two independent ways to end a game that stalls
past that: Wurmcoil's 6/6 lifelink+deathtouch splits into two more threats if it dies, and
Platinum Angel simply removes "your opponent can win" from the table while the +2 engine keeps
ticking the damage/life gap in the background. **Counterspell** and **Swan Song** exist purely
to protect that plan from the single removal spell or board wipe that would otherwise blank the
whole gameplan in one card, which matters more in 1v1 than in a pod where a wipe only 1/3-costs
the caster relative to the value they remove.

## Optional upgrades not applied

- **Ugin, the Ineffable / Karn, Scion of Urza / Tezzeret, Artifice Master** — all verified
  Arena/Brawl-legal and on-color, and would stack further with the existing Tezzeret-tribal
  package (Betrayer of Flesh, Cruel Captain already in the 99), but adding a 4th-5th planeswalker
  on top of an already-heavy 6-drop curve (Wurmcoil, Platinum Angel now added) risks clunky
  hands. Left out this pass; a natural next upgrade if the games feel too grindy rather than too
  slow to stabilize.
- **Ulamog, the Ceaseless Hunger / Kozilek, the Great Distortion / Emrakul, the Promised End /
  Sundering Titan / Metalwork Colossus / Cityscape Leveler** — all verified legal, huge
  affinity-discounted payoffs, but the deck doesn't yet have enough artifact count consistency
  to reliably discount an 8-11 mana spell down to castable range this early in the rebuild;
  worth revisiting once the current swap's ramp/artifact density proves itself over a few games.
- **Bitter Triumph / Heartless Act / Go for the Throat** — additional verified-legal removal
  options if the single Infernal Grasp added here still isn't enough interaction in practice.
