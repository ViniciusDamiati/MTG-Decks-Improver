# Bright-Palm, Soul Awakener — Round 2: Competitive/High-Power Review (August 2026)

This is a follow-up pass on top of the July 2026 upgrade (see git history for that swap
table). The user asked whether the deck needs more work to be competitive in EDH/cEDH.
Every card mentioned below was re-verified against its exact Scryfall/local-DB oracle text
this session — nothing was carried over from memory. The deck was, and remains, **exactly
100 cards** (99 + commander).

Data sources:

- mtgtop8 cEDH format page: https://mtgtop8.com/format?f=cEDH (checked first, per project rule)
- mtgtop8 commander search: https://mtgtop8.com/search?commander=Bright-Palm%2C+Soul+Awakener&format=cEDH
- EDHREC commander page (3,292 decks): https://edhrec.com/commanders/bright-palm-soul-awakener
- EDHREC average decklist: https://edhrec.com/average-decks/bright-palm-soul-awakener
- Card texts: local `mtg_cards` Postgres DB (Scryfall oracle-cards dump)

## The headline finding: there is no cEDH ceiling to chase

- **Bright-Palm has zero results on mtgtop8's cEDH format page** — no archetype entry, no
  event placements, nothing.
- **On EDHREC itself, only 1 of 3,292 registered decks self-tags as Bracket 5 (cEDH)**, and
  only 3 decks carry a "cEDH" theme tag at all. The bracket breakdown: Bracket 2 "Core" 684,
  Bracket 3 "Upgraded" 256, Bracket 4 "Optimized" 50, Bracket 1 "Exhibition" 12, Bracket 5
  "cEDH" 1. This is overwhelmingly a casual-to-upgraded commander.
- **EDHREC's "Game Changers" panel** (their own flag for high-power staples) shows almost no
  adoption on this commander: Teferi's Protection 10.5%, Farewell 8.8%, Worldly Tutor 6.9%,
  Enlightened Tutor 5.8%, Smothering Tithe 5.5%. The playerbase for this commander simply
  doesn't reach for tournament-caliber staples.
- Salt score is 0.67 (low) and EDHREC rank is #771 overall — a well-liked, off-meta pick,
  not a competitive one.

**Conclusion presented to the user, who confirmed:** true cEDH tier-1 status isn't a
realistic target for this commander — that would mean choosing a different commander
entirely. The productive question is how far to push within "as strong as this commander
can be," and the user chose **high power** (Bracket 4, cEDH-adjacent in spirit even without
tournament pedigree): add free/efficient interaction, a combo tutor, and a real sweeper.

## The deck was already at the EDHREC ceiling for commander-specific data

Cross-referencing the July-upgraded list against every EDHREC category (creatures,
instants, sorceries, enchantments, artifacts, lands) turned up **zero missing cards** above
meaningful inclusion/synergy thresholds — the list already runs essentially every top
synergy card EDHREC has for this commander (Kalonian Hydra 71%, Forgotten Ancient 70%,
Conclave Sledge-Captain 67%, Uncivil Unrest 66%/0.632 synergy, Strionic Resonator 45%,
Gavony Township 61%/0.528 synergy — all present), plus several bombs that exceed what the
*average* EDHREC pilot runs (Doubling Season, Vorinclex, the verified Heliod + Walking
Ballista infinite combo, Aragorn, Mayael's Aria). Round 1 already captured this commander's
data-driven ceiling. There was no further EDHREC-sourced swap to make.

That means round 2's additions are **generic high-power Commander staples**, not
commander-specific synergy picks — chosen because they raise the deck's functional power
level (free interaction, combo tutoring, efficient removal) regardless of what EDHREC's
casual playerbase happens to register for this card.

## The swaps (4 out, 4 in)

| # | Out | In | Reason (verified against oracle text) |
|---|-----|----|--------------------------------------|
| 1 | **Master Chef** | **Eladamri's Call** | Verified Master Chef's oracle text: *"Commander creatures you own have 'This creature enters with an additional +1/+1 counter on it' and 'Other creatures you control enter with an additional +1/+1 counter on them.'"* This text only applies to a commander with **Choose a Background** — Master Chef is a Background card. Verified Bright-Palm, Soul Awakener's oracle text directly: it has **no Choose a Background ability**. Master Chef was doing **literally nothing** in this deck — a carried-over error from the July audit. Eladamri's Call ({G}{W} instant) searches for any creature card to hand — it can find **either half of the deck's verified Heliod, Sun-Crowned + Walking Ballista infinite-lifegain combo**, or any other bomb (Kalonian Hydra, Guardian Scalelord), turning "hope to draw both combo pieces" into "tutor for whichever one is missing." |
| 2 | **Return to Nature** | **Solitude** | Return to Nature is a generic 2-mode instant (destroy artifact / destroy enchantment / exile graveyard card) — reactive utility with zero +1/+1 counter synergy, and this deck already has other narrow answers. Solitude ({3}{W}{W}, or **evoke for free** by exiling a white card from hand) is a premier Commander-format staple: a 3/2 flash lifelink body that exiles a creature on ETB, castable for **zero mana**. This is exactly the "free interaction" density the deck lacked entirely — before this swap the deck ran no pitch/free spells at all. |
| 3 | **Mirror-Style Master** | **Deflecting Swat** | Verified Mirror-Style Master's text: its copy-attackers trigger only belongs to *itself* unless another creature is granted Backup at ETB, and that borrowed ability only lasts the turn it enters — a narrow, one-shot effect at a clunky CMC 6. Deflecting Swat ({2}{R}, **free if you control your commander** — which is true almost every turn) redirects a targeted spell or ability. This protects the deck's single point of failure (the counter-loaded attacker) from targeted removal, or redirects an opponent's removal/wrath onto their own board — free, always-live interaction the deck had zero of. |
| 4 | **Juniper Order Ranger** | **Winds of Abandon** | Juniper Order Ranger only grows off *other* creatures entering — a slow, incremental value engine with no interaction, evasion, or protection text of its own. Winds of Abandon ({1}{W}) exiles a single opposing creature early, or **overloads for {4}{W}{W} to exile every creature every opponent controls** (ramping them with tapped basics) while leaving your own board — including the countered attacker — completely untouched. A genuine one-sided sweeper this "one tall threat" deck had no equivalent of. |

Color identity check: Eladamri's Call (G/W), Solitude (W), Deflecting Swat (R), Winds of
Abandon (W) — all inside Bright-Palm's R/G/W identity. **Mana Crypt and Jeweled Lotus were
both considered and rejected: both are banned in Commander**, regardless of color identity
or power level.

## Cards re-verified and kept (round-2 audit)

The second-pass oracle-text check confirmed these are pulling real weight and should stay:

- **Virtue of Loyalty** — puts a +1/+1 counter on **every** creature you control each end
  step and untaps them; direct board-wide counter synergy, plus its adventure half makes a
  body first.
- **All Will Be One** — triggers off *any* counter placement (not just +1/+1), converting
  every counter your board generates into direct damage to an opponent or their creature.
- **Elite Scaleguard** — bolster 2 on ETB plus a tap-down attack trigger for any creature
  carrying a +1/+1 counter — fits a one-tall-threat plan exactly.
- **Defiler of Vigor** — 6/6 trample body; its ongoing counter trigger scales with how many
  more green permanents get cast afterward, but the body alone justifies the slot.
- **Sword of Truth and Justice** — colorless equipment that adds a counter and proliferates
  on combat damage; genuine counter-engine value despite narrow protection colors.
- **Akroma's Will** — with a commander in play (always true here) grants **both** modes at
  once: flying/vigilance/double strike *and* lifelink/indestructible/protection from every
  color. Double strike is a real payoff on a heavily-countered attacker.
- **Rhythm of the Wild** — riot lets every nontoken creature choose a +1/+1 counter or
  haste on ETB; uncounterable creature spells is a real protection clause too.
- **Hindervines** — narrower than it first looks, but it's a genuine one-sided fog against
  any board of unmodified creatures (i.e., almost every opponent's board), which matters
  more for a single-big-threat deck than it would for a go-wide list.

## Why the changes are stronger — the proof

**The commander's ceiling was already hit; the floor needed raising.** Bright-Palm turns N
counters into 2N per attack, and round 1 already assembled nearly every card EDHREC tracks
for that plan. What the deck lacked for a genuine high-power table was **interaction density
at zero mana cost** — before this round, the entire 100 cards contained no free spells.
Solitude and Deflecting Swat fix that: a removal spell and a universal redirect that cost
nothing and don't compete for turns spent building the board.

**The combo goes from "lucky" to "found."** The Heliod, Sun-Crowned + Walking Ballista
infinite (verified in round 1: Heliod grants Ballista lifelink; remove a counter → 1 damage
→ 1 life → Heliod replaces the counter, indefinitely) previously required drawing both
pieces naturally. Eladamri's Call finds either one on demand.

**A real sweeper closes games instead of stalling them.** Winds of Abandon overloaded wipes
every opponent's board for six mana while the countered attacker — the actual win
condition — is never a legal target. No other card in the 100 did this.

**One dead card is gone.** Master Chef contributed nothing; verifying it directly against
Bright-Palm's oracle text (no Choose a Background) caught an error the July pass missed.

## Optional upgrades not applied (would push further into Bracket 4-5 territory)

- **Fierce Guardianship / Deflecting Swat's blue cousin** — not castable; this deck has no
  blue, so true "free counterspell" protection isn't available in this color identity.
- **Green Sun's Zenith** — a second creature tutor (green creatures only, up to CMC X); would
  add consistency for Kalonian Hydra or Incubation Druid specifically, but the deck only had
  room for one tutor this round.
- **Open the Armory** — tutors Bone Sabres or Swiftfoot Boots; a reasonable fifth swap if the
  user wants to go even further.
- **Idyllic Tutor** — enchantment-only tutor (would find Doubling Season, Court of Garenbrig,
  or Uncivil Unrest); reconsidered from the July cut but held back to avoid stacking three
  tutors into one deck.
