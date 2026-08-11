# Aragorn, the Uniter — Upgrade Notes (August 2026)

Changes applied to `Aragorn, the Uniter.txt`. Every card mentioned below was verified against
its exact oracle text via the local `mtg_cards` database before being cut, added, or kept. The
deck was already exactly 100 cards — no count fix needed this pass. Flagged by the deck owner
as built when Aragorn was printed (June 2023) and not revisited since.

Data sources:

- mtgtop8 cEDH format check: https://mtgtop8.com/format?f=cEDH — **no cEDH presence**; zero
  recorded tournament decklists for this commander. Non-competitive, casual/high-power pod
  commander — the upgrade below targets structural gaps, not a bracket-4 power push.
- EDHREC commander page (22,261 tracked decks): https://edhrec.com/commanders/aragorn-the-uniter
  (rank reported inconsistently between EDHREC's own two surfaces — #46 on the commander page,
  #72 on the JSON API dated July 2026 — noted rather than resolved, doesn't change the analysis)
- EDHREC per-category data: https://json.edhrec.com/pages/commanders/aragorn-the-uniter.json
- EDHREC average decklist: https://edhrec.com/average-decks/aragorn-the-uniter
- Card texts: local `mtg_cards` Postgres database (Scryfall `oracle-cards` bulk data) — all 95
  current-deck cards plus 37 audit candidates resolved with zero live-API fallback needed.

## What Aragorn actually does (verified)

> Whenever you cast a white spell, create a 1/1 white Human Soldier creature token.
> Whenever you cast a blue spell, scry 2.
> Whenever you cast a red spell, Aragorn deals 3 damage to target opponent.
> Whenever you cast a green spell, target creature gets +4/+4 until end of turn.

The axis: cast spells of every color to accrue tokens, card selection, direct damage, and
combat pump — a 4-color (no black) "cast a spell of each color" value/aggro engine, not a
tribal lord in the mechanical sense, though the existing build layers a genuine Human-tribal
and legendary-matters shell underneath it (both of which synergize naturally: more Humans/
legendaries cast = more color triggers).

## The diagnosis — corrected from the initial assumption

Going in, a near-3-year-old, untouched decklist looked like it would need a wholesale rebuild.
**That assumption didn't survive the audit.** All 26 "possibly weak" current-deck cards were
verified card-by-card, and all but a handful read as genuinely synergistic with the Human-
tribal/legendary-matters/token shell (Roaming Throne doubling Human ETB triggers, Katilda
turning every Human into a fixed mana dork, Hero of Precinct One rewarding Aragorn's own
multicolor-cast plan directly, etc.) — this is a well-conceived list, not a pile of forgotten
filler. The real problems were structural, found by comparing category counts against the
current EDHREC average (99-card, non-commander basis):

| Category | This deck (before) | EDHREC average | Gap |
|---|---|---|---|
| Land | 34 | 36 | **-2** |
| Creature | 32 | 27 | +5 (see note below) |
| Instant | 10 | 13 | **-3** |
| Sorcery | 8 | 8 | matched |
| Artifact | 8 | 8 | matched |
| Enchantment | 7 | 7 | matched |

1. **2 lands short** for a 4-color manabase — real risk of getting stuck off-color.
2. **3 instants short** — meaningfully less instant-speed interaction/protection than an
   average pod-tuned build of this exact commander.
3. **Only one real mana dork** (Noble Hierarch) despite running 4 colors — everything else
   ramping was sorcery-speed (Cultivate, Farseek, Nature's Lore, Rampant Growth, Three Visits,
   all present and correctly kept).
4. **Five separate "choose a creature type, get an anthem/payoff" effects** stacked in one
   list (Door of Destinies, Herald's Horn, Vanquisher's Banner, Kindred Discovery, Roaming
   Throne) — real redundancy once verified side-by-side; the weakest two were the least
   impactful use of a card slot.
5. **Missing Pippin, Guard of the Citadel** (44.4% EDHREC inclusion, #4 creature by inclusion)
   — the one clear "notable absence" this deck actually had.

Creature count running +5 over average was **not** treated as a problem to fix by cutting
bodies — the audit showed nearly every creature is a verified, active payoff for this specific
shell (Human-tribal, legendary-matters, or token generation), so a wider-than-average creature
base is this deck's legitimate identity, not bloat. The fix targeted the categories that were
genuinely thin: lands and instants.

## The swaps (7 out, 7 in)

| # | Out | In | Reason (verified against oracle text + EDHREC data) |
|---|-----|----|--------------------------------------|
| 1 | Hajar, Loyal Bodyguard | **Pippin, Guard of the Citadel** (44.4% incl) | Hajar is a one-shot sacrifice effect (+1/+0 and indestructible to legendaries, once). Pippin grants repeatable, chosen protection ("gains protection from the card type of your choice") to another creature every turn for {T} — ongoing board insurance instead of a single combat trick. |
| 2 | Prince Imrahil the Fair | **Faeburrow Elder** | Imrahil's token trigger needs "draw your second card each turn," which this deck has no dedicated support for — usually dead. Faeburrow Elder taps for **one mana of every color among your permanents**, not just creatures — uniquely strong fixing for a commander whose entire plan is casting one spell of each color, and directly attacks the land-count/color-consistency gap. |
| 3 | Riders of Rohan | **Delighted Halfling** | Redundant with the still-kept Riders of the Mark (same Human-Knight-token idea, verified stronger: recurring, scales with toughness, vs. Rohan's one-time ETB). Delighted Halfling ramps AND makes the deck's dense legendary-spell suite (nearly every creature in the 99) uncounterable — direct upgrade for this exact list. |
| 4 | Herald's Horn | **Rivendell** | 5th redundant "choose a type" tribal payoff, verified as the weakest (cost reduction + conditional top-of-library peek, Human-only). Rivendell is a land — closes part of the diagnosed land deficit, taps for blue, and scries off the deck's legendary density. |
| 5 | Door of Destinies | **Windswept Heath** | 4th redundant "choose a type" tribal payoff (slow-building anthem, verified as narrow early). Windswept Heath is an on-color G/W fetch — closes the rest of the land deficit (34→36, now matches average exactly) and thins the deck. |
| 6 | Mass Appeal | **Jeskai Charm** | Mass Appeal draws off Human count with zero board impact of its own — pure payoff, no floor. Jeskai Charm is modal instant-speed interaction (bounce a threat to library, 4 damage to an opponent/planeswalker, or team pump+lifelink) — directly closes the diagnosed instant-count gap with real flexibility. |
| 7 | Warleader's Call | **Friendly Rivalry** | 3rd redundant go-wide static anthem (alongside the kept Flowering of the White Tree and Shared Animosity — verified all three do meaningfully different things, but three was one too many). Friendly Rivalry is instant-speed removal (fight-style damage from your creature, optionally doubled by a legendary creature you control) — more interaction, more color-cast triggers off an instant. |

## Cards challenged during the audit and kept as-is

Every one of these was suspected as a possible weak link on a first skim and verified to have
real, active synergy — none were cut:

- **Riders of the Mark, Beregond of the Guard, Kyler, Sigardian Emissary, Coppercoat Vanguard,
  Heronblade Elite, Champion of Lambholt, Hero of Precinct One, Torens, Fist of the Angels** —
  all confirmed as active Human-tribal or token-shell payoffs, several (Hero of Precinct One
  especially) directly rewarding Aragorn's own multicolor-cast plan.
- **Roaming Throne** — sets its chosen type to Human and doubles every Human ETB trigger in
  the deck (Beregond, Kyler, Riders of the Mark, etc.) — verified as a genuine engine piece,
  not a vanilla 4/4.
- **Katilda, Dawnhart Prime** — turns every Human you control into a fixed-color mana dork,
  directly enabling the "cast one spell of every color each turn" plan. One of the strongest
  verified synergy pieces in the list.
- **Inga and Esika, Sigarda, Font of Blessings, Adeline, Resplendent Cathar** — all verified as
  high-impact engines (creature-cast ramp+draw, board-wide hexproof + card advantage, and a
  scaling attack-trigger token generator respectively), not filler.
- **Kindred Discovery, Shared Animosity, Vanquisher's Banner, Flowering of the White Tree,
  Annie Joins Up, Kellan Joins Up** — all verified as real card-advantage or damage engines
  for the Human-tribal/legendary-matters/token shell; kept despite the "5 tribal-type-choice
  effects" redundancy note above, since these four were confirmed the strongest of that group
  (Door of Destinies and Herald's Horn were the two cut instead).

## Why the changes are stronger — the proof

**Manabase:** 34 → 36 lands, matching the EDHREC average exactly, plus Faeburrow Elder added as
a mana source that taps for every color among permanents you control (not just lands) — for a
4-color deck whose commander rewards casting one spell of *each* color every turn, this
directly reduces the odds of a "stuck on 3 colors" turn that skips one of Aragorn's four
triggers.

**Interaction:** instants go from 10 to 12 (closing most of the -3 gap), with both new instants
(Jeskai Charm, Friendly Rivalry) doubling as color-cast triggers for Aragorn himself — unlike
the sorcery-speed and enchantment-based effects they're layered alongside, these can be held up
and cast reactively, on an opponent's end step or in response to a threat, instead of only on
your own turn.

**Redundancy trimmed, not power:** of five "choose a creature type" payoff effects running at
once, the two weakest (Door of Destinies' slow-building anthem, Herald's Horn's Human-only cost
reduction) were cut; Vanquisher's Banner, Kindred Discovery, and Roaming Throne — verified as
the three strongest of the five — remain, so the tribal payoff plan loses redundancy, not
capability.

**Pippin closes the one real EDHREC gap.** At 44.4% inclusion, it was the highest-profile card
missing from this build relative to the field; it's in now.

## Optional upgrades (not applied)

- **Bloom Tender, Birds of Paradise** — two more mana dorks from the EDHREC average list;
  not added since Faeburrow Elder + Delighted Halfling + Noble Hierarch, plus the deck's
  existing 5 ramp sorceries, already substantially close the fixing gap — a good next add if
  the deck wants to go even lower to the ground.
- **Counterspell, Simic Charm** — more generic instant-speed interaction (18% incl. each);
  left out to avoid pushing the instant count past the EDHREC average rather than toward it.
- **Flooded Strand** — a second W/U-adjacent fetch beyond Windswept Heath; the land count
  already matches the average exactly after this pass, so adding it would require a further
  cut elsewhere.
- **Jetmir, Nexus of Revels, Galadriel, Light of Valinor, Rienne, Angel of Rebirth, Merry,
  Esquire of Rohan, Aragorn and Arwen Wed** — all present in the EDHREC average decklist but
  not individually verified this pass; worth a look in a future update once one of the above
  optional dorks/interaction pieces is prioritized.

Deck re-verified at exactly 100 cards after all swaps; no duplicate entries; color identity of
every add confirmed as a subset of Aragorn's R/G/W/U identity (no black in any add).
