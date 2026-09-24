# Momo, Friendly Flier — MTG Arena Brawl/Commander upgrade

## Sources

- Local card DB (`.claude/scripts/card_db.py`, Scryfall `oracle-cards` bulk dump) — oracle text,
  mana costs, color identity for every card in the current list and every candidate.
- mtgtop8 cEDH check: https://mtgtop8.com/format?f=cEDH — no entry for Momo, Friendly Flier
  (expected; this is a budget/limited-power commander, not a competitive one).
- EDHREC: https://edhrec.com/commanders/momo-friendly-flier and
  https://edhrec.com/average-decks/momo-friendly-flier — 2,187 decks, rank #1,053, themes
  Flying (163 decks) / Tempest Hawk (42) / Aggro (41) / Birds (41).
- `arena-legality-checker` agent — verified every candidate add against real Arena/Brawl
  legality data (`legalities.brawl`, `games` field), not just paper legality.

## Commander (verified oracle text)

**Momo, Friendly Flier** — {W}, Legendary Creature — Lemur Bat Ally, 1/1
> Flying. The first non-Lemur creature spell with flying you cast during each of your turns
> costs {1} less to cast. Whenever another creature you control with flying enters, Momo gets
> +1/+1 until end of turn.

Scales on: **casting flying creatures cheaply and often** — a go-wide flying-aggro axis, not a
combo or control shell. EDHREC's own theme breakdown (Flying/Aggro/Birds as the top three tags)
confirms this is the commander's intended and best-supported plan.

## Methodology note — Arena legality verification

Every candidate add was run through the `arena-legality-checker` agent, which checks
`legalities.brawl` plus an all-printings `games:arena` search — not just whether the card is
paper-legal in Commander. This caught real traps in both directions:

- **False negatives avoided**: Sephara, Sky's Blade and Selfless Spirit's *default* Scryfall
  printings (CMM 54 and SOC 167) are paper/MTGO-only, which would read as "not on Arena" from a
  naive single-printing lookup. Earlier printings (**M20 36** and **SIR 42**) are genuinely
  Arena-legal — those are the set/collector numbers used below.
- **Cards correctly rejected despite strong EDHREC synergy**: Windborn Muse (no Arena printing
  at all), Cartographer's Hawk, Senu Keen-Eyed Protector, Skyhunter Strike Force, and Firemane
  Commando — all paper/MTGO-only. High EDHREC inclusion is irrelevant if the card can't be
  imported.
- **Alchemy-native cards already in the deck were confirmed legal, not flagged as suspect**:
  Prairie Survivalist (YOTJ 1) and Waystone's Guidance (YTDM 3) have no paper printing at all
  (`games: [arena]` only) — that's expected for Arena-exclusive digital cards and does not
  affect their Brawl legality. Both confirmed `brawl: legal`.

## Diagnosis

- **Flying creature count**: strong — roughly 30 of the deck's 35 creatures fly, correctly
  built around the commander's cost-reduction/pump triggers.
- **Board wipes — the deck's core problem.** The list ran **6 symmetric or near-symmetric
  sweepers**: Wrath of God, Day of Judgment, Split Up, Final Showdown's wipe mode, Farewell, and
  Elspeth Sun's Champion's −3. Wrath of God and Day of Judgment are functionally identical
  ("destroy all creatures") — running both is pure redundancy, not redundancy-as-insurance. A
  go-wide flying-aggro deck that wants to win on combat damage should not be carrying this much
  incentive to blow up its own board, especially in 1v1 where there's no third player's board to
  selectively spare.
- **Filler creatures with no live ability**: City Pigeon (marginal death trigger), Rustwing
  Falcon (vanilla 1/2 flyer), Mothrider Patrol (a {3}{W} tap ability on a 1/1 body is far too
  slow), Duskborne Skymarcher (only pumps *attacking Vampires* — the deck has one other Vampire,
  Welcoming Vampire, so this is a dead ability almost every game), Incisor Glider (Corrupted
  requires the opponent to have 3+ poison counters — this deck has zero infect/poison support,
  so it's a vanilla 1/3 flyer for {1}{W}).
- **Haste**: only Swiftfoot Boots and Lightning Greaves (plus the 7-mana Akroma's Memorial).
  Thin, but partially mitigated by the low curve — this deck rebuys board presence every turn
  rather than relying on one hasty threat, so this wasn't judged severe enough to force a swap
  this pass. Flagged as an optional future upgrade below.
- **Ramp**: only Arcane Signet and Mind Stone are true mana rocks (Pearl Medallion and Oketra's
  Monument are cost reducers, not ramp). Adequate for a curve that tops out at a handful of big
  finishers, not touched this pass.
- **Land count**: 40 Plains vs. EDHREC's average of 35. High for a curve this low, but changing
  land count wasn't necessary to fix the diagnosed problems, so it was left alone rather than
  forced into the swap count — flagged below as an optional future trim.

## Swaps (8, all verified Arena/Brawl-legal, all mono-white)

| Out | Why cut | In | Why added | Arena legality |
|---|---|---|---|---|
| Wrath of God (AKR 46) | Exact duplicate effect of Day of Judgment — redundant, not insurance | **Tempest Hawk** (TDM 31) | 2/2 flyer, draws a card off unblocked combat damage; EDHREC's #1 synergy card for this commander (64% inclusion, 0.624 synergy) — turns evasive damage into card advantage | `brawl: legal` |
| Day of Judgment (FDN 140) | Second copy of the same "destroy all creatures" effect; kept Farewell as the deck's one true wipe | **Sephara, Sky's Blade** (M20 36) | 7/7 flying lifelink Angel that gives *all* your flyers indestructible — directly answers the deck's own remaining wipes and any opposing removal; alt-cost of {W} + tapping 4 flyers makes it castable well under curve in a go-wide deck | `brawl: legal` (default CMM printing is paper-only — M20 is the Arena-legal printing) |
| Split Up (DSK 32) | Symmetric wipe (destroys all tapped *or* all untapped creatures) — kills your own attackers or blockers along with theirs | **Selfless Spirit** (SIR 42) | 2/1 flyer for {1}{W}; sac to give the whole team indestructible — a proactive answer to board wipes instead of running more of them | `brawl: legal` (default SOC printing is not on Arena — SIR is) |
| City Pigeon (SPM 4) | Marginal 1/1 flyer, death trigger is a single Food token | **Herald's Horn** (JMP 469) | Choose Bird (the deck's most common creature type): creature spells of that type cost {1} less and it digs for more Birds every upkeep — real cost reduction and card selection | `brawl: legal` |
| Rustwing Falcon (M19 36) | Vanilla 1/2 flyer, no ability | **Flare of Fortitude** (MH3 26) | Free (sac a nontoken white creature) or {2}{W}{W}: locks your life total and gives your board hexproof + indestructible — a full team fog/wrath-proof effect, castable off a chump-able 1-drop | `brawl: legal` |
| Mothrider Patrol (NEO 30) | {3}{W} tap-down ability on a 1/1 body is far too slow for an aggro plan | **Steel-Plume Marshal** (JMP 5) | 3/3 flyer that gives every other attacking flyer +2/+2 when it attacks — a real payoff for the go-wide flying alpha strike | `brawl: legal` |
| Duskborne Skymarcher (XLN 9) | Only pumps attacking Vampires; deck has one other Vampire (Welcoming Vampire) so the ability is dead most games | **Dawn's Truce** (BLB 9) | {1}{W} instant: hexproof for you and your permanents (indestructible too if the gift is promised) — cheap, flexible wrath/removal protection at instant speed | `brawl: legal` |
| Incisor Glider (ONE 15) | Corrupted ability needs the opponent to have 3+ poison counters; deck has zero infect support, so it's a vanilla 1/3 for {1}{W} | **Rally of Wings** (WAR 27) | {1}{W} instant: untap your whole team and give flyers +2/+2 — lets the board swing and still block, or acts as a combat trick that wins races | `brawl: legal` |

## Challenged and kept

Nothing was challenged by the user this pass — this is the first upgrade for this deck.

One internal reversal during research: I initially considered cutting **Final Showdown**
(its top mode is a board wipe) alongside the other sweepers, but its cheap modes ({1} strip
abilities, {1} protect-a-creature) are live and useful independent of the wipe mode, and one
symmetric wipe as an emergency valve (on top of Farewell) is not the redundancy problem Wrath of
God / Day of Judgment / Split Up were — kept.

## Proof — go-wide flying alpha strike vs. a single opponent's life total

Turn 5 example board (very achievable given the low curve): Momo, Friendly Flier (1/1, buffed to
4/4 from three flyers having entered this game — +1/+1 per flyer ETB), Battlefield Raptor (1/2
flying first strike), Healer's Hawk (1/1 flying lifelink), Segovian Angel (1/1 flying vigilance),
and newly-added Steel-Plume Marshal (3/3 flying) attacking.

Base power: 4 + 1 + 1 + 1 + 3 = 10. Steel-Plume Marshal's attack trigger gives every *other*
attacking flyer +2/+2: Momo becomes 6/6, Battlefield Raptor 3/4, Healer's Hawk 3/3, Segovian
Angel 3/3, Marshal itself stays 3/3 (only pumps others). Total damage: 6 + 3 + 3 + 3 + 3 = **18
unblocked flying damage** — more than half of a 1v1 Brawl starting life total (30 or 40
depending on format) in a single swing, on curve, before Sephara or Tempest Hawk's card
advantage even come online. Against a single opponent (not a 3-way-split multiplayer table),
this is a two-to-three-turn clock once the board is online.

## Optional upgrades not applied this pass

- **Land count**: trimming 2-3 Plains toward EDHREC's 35-land average (in exchange for 2-3 more
  spells) would reduce flood risk on a curve this low. Not forced into this pass since it wasn't
  needed to fix the diagnosed problems; worth revisiting if the deck floods in practice.
- **Haste package**: currently just Swiftfoot Boots + Lightning Greaves. If games are being lost
  to summoning sickness rather than to running out of gas, look for additional Arena-legal white
  haste sources in a future pass.
- **Windborn Muse** (Ghostly Prison stapled to a 2/1 flyer) would have been an excellent add for
  this shell but has no Arena printing — confirmed unavailable, not a viable future pickup either
  unless Wizards prints it into a Standard/Historic-legal set.
