# Teysa Karlov — MTG Arena (Historic Brawl) — 119 → 100 cut pass

## Sources
- mtgtop8 cEDH format page: https://mtgtop8.com/format?f=cEDH
- mtgtop8 Teysa Karlov cEDH archetype: https://www.mtgtop8.com/archetype?a=1229
- EDHREC commander page: https://edhrec.com/commanders/teysa-karlov
- EDHREC JSON data: https://json.edhrec.com/pages/commanders/teysa-karlov.json
- EDHREC average decklist: https://edhrec.com/average-decks/teysa-karlov
- Scryfall API (oracle text + legality) for every card touched in this pass
- Historic Brawl life total (25, 1v1): https://mtgazone.com/introduction-to-historic-brawl-comparison-versus-commander/

## Commander — verified oracle text
**Teysa Karlov** — {2}{W}{B} — Legendary Creature — Human Advisor — 2/4 (color identity B/W)
> If a creature dying causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
> Creature tokens you control have vigilance and lifelink.

She's a pure death-trigger and token-quality doubler — she doesn't create value herself, she multiplies whatever death/token engine the rest of the deck provides. Every card kept or added was judged against that axis.

## Methodology note — how Arena legality was verified
Every one of the 84 non-basic-land cards in the pre-cut list (plus the commander) was swept through Scryfall for `legalities.brawl` / `legalities.competitivebrawl` and a real `game:arena` printing. **Result: all 85 were already genuinely Arena-legal — zero false positives from the original export.** Three cards are Alchemy-native with no paper printing (A-Blood Artist, Veko, Death's Doorkeeper, Teysa of the Ghost Council) — that's expected and doesn't affect Brawl legality, so they were kept eligible, not auto-cut. Because this pass was pure trimming (no new adds were applied to the decklist), that clean sweep is the only Arena-legality-gating this file needed. The optional-upgrades section below (not applied) was separately gated the same way, and it caught real false positives: **Skullclamp and Phyrexian Altar are both paper Commander staples with no Arena printing at all** — the same "Sol Ring lesson" the project methodology warns about.

## Diagnosis (99-card, 1v1)
- **cEDH presence:** none on the mtgtop8 format page's meta share, but Teysa Karlov does have a dedicated archetype page (a=1229) with two recorded competitive results (5th–8th of 34, and 15th of 224) — a real but very thin competitive footprint. This is a casual/midrange EDHREC build (rank #54, ~21k decks), not a tuned cEDH list, and the deck reads that way.
- **Creatures:** ~35 in the 99 (EDHREC average ≈33) — on theme, mostly cheap aristocrats pieces.
- **Card draw/advantage:** heavy — Phyrexian Arena, Midnight Reaper, Grim Haruspex, Sephiroth, Solemn Simulacrum, Deadly Dispute, Emeritus of Woe // **Demonic Tutor** (this MDFC's back face is a hard tutor — excellent, easy to undervalue at a glance), Season of Loss, Lolth. No gap here.
- **Ramp/fixing:** Arcane Signet, Command Tower, Godless Shrine, Solemn Simulacrum, Black Market, plus four treasure-makers (Pitiless Plunderer, Sephiroth, Smothering Tithe, Deadly Dispute). Adequate; the two cuts here (Dark Ritual, Orzhov Locket) don't create a hole.
- **Trigger/token multipliers:** Teysa Karlov + Drivnod, Carnage Dominus + Sephiroth's flip-side emblem all double death triggers independently; Anointed Procession doubles tokens. That's three independent doublers on top of the commander — redundant insurance, not a gap.
- **Haste package: effectively zero.** Only Swiftfoot Boots grants haste, plus Teysa of the Ghost Council gives *herself* haste when she returns from her own exile loop. In 1v1 Brawl there's no third player absorbing a turn of summoning sickness — this is a real, unaddressed weakness worth fixing on a future pass (see optional upgrades).
- **1v1 dilution check:** several EDHREC staples in this list score their reputation from hitting 3 opponents at once (Grave Pact, Zulaport Cutthroat, Cruel Celebrant, Elas il-Kor, Mirkwood Bats, Liliana's −4/−9). None of these were cut for that reason alone — they're still fine at 1x — but **Revel in Riches was cut specifically because its win condition (10 Treasures from opponents' creatures dying) scales on opponent count and is far too slow with only one opponent feeding it.**

## Cuts applied (19 → deck now totals exactly 100)

### Lands (−3)
| Cut | Reason |
|---|---|
| 1 Plains | Land count was 39 (EDHREC average ≈35); the deck's four treasure-makers plus Arcane Signet/Black Market cover the difference. Trimmed to 36 total lands (16 Plains / 15 Swamp + 5 nonbasic). |
| 2 Swamp | Same reasoning. |

### Spells (−16)
| Cut | Verified text basis | Reason |
|---|---|---|
| Revel in Riches | "Whenever a creature *an opponent* controls dies, create a Treasure... 10 Treasures, you win" | Win-con scales with opponent count; with one opponent it's a slow, low-payoff enchantment. |
| Altar of Dementia | "Sacrifice a creature: target player mills X" | Redundant sac outlet (deck already has Ashnod's Altar, Phyrexian Tower, Yawgmoth, Diabolic Intent, Deadly Dispute, Season of Loss); mill has no payoff here. |
| Bartolomé del Presidio | "Sacrifice another creature or artifact: +1/+1 counter on Bartolomé" | Only benefit is self-buff — no card advantage, weakest sac-payoff in the deck. |
| Imperious Oligarch | Vanilla 2/1 vigilance, Afterlife 1 | Strictly worse afterlife body than Seraph of the Scales/Ministrant of Obligation/Tithe Taker, all already in the deck. |
| Hunted Witness | Dies → 1/1 **Soldier** with lifelink | Under Teysa Karlov, *all* your tokens already have lifelink — the built-in lifelink is dead text. Doomed Traveler's Spirit token (kept) also plays into Teysa of the Ghost Council's Spirit anthem; this doesn't. |
| Hardened Tactician | {1}, sac a token: draw a card | One card-advantage engine too many (Phyrexian Arena/Midnight Reaper/Grim Haruspex/Bolas's Citadel/Sephiroth/Deadly Dispute/Demonic Tutor already cover it) for a plain 2/4 body. |
| Fumulus, the Infestation | Drain trigger keyed to Insect/Leech/Slug/Worm attackers only | Deck runs almost no creatures of those types — the payoff clause is nearly dead. |
| Dictate of Erebos | "Whenever a creature you control dies, each opponent sacrifices a creature" | Identical effect to Grave Pact (kept, and 1 mana cheaper) — redundant. |
| Dawn's Truce | Hexproof (+indestructible if gifted) until EOT | Situational protection; the deck already carries Swiftfoot Boots and Luminous Broodmoth for protection, and 1v1 has fewer simultaneous threats than a pod. |
| Blasphemous Edict | "Each player sacrifices thirteen creatures" (discount at 13+ creatures) | A third/fourth board wipe on top of Kaya's Wrath and The Meathook Massacre is excessive; those two are strictly more flexible. |
| Living End | Suspend 3, exile+reanimate all creatures from all graveyards | Build-around payoff with no dedicated self-mill/discard engine to fuel it in this list (and cutting Altar of Dementia removes the deck's only self-mill outlet) — a 3-turn-telegraphed effect that's currently unsupported. |
| Fleshtaker | Sac outlet, gain 1 + scry 1, pump | Another redundant sac-outlet body in a deck already saturated with them. |
| Indebted Spirit | Bestow {2}{W}, Afterlife 1, 1/1 base | Weakest of the deck's cheap afterlife/token bodies. |
| Dark Ritual | Add {B}{B}{B}, one-shot | No combo finish to power out with the extra mana — a dead draw from the mid-game on. |
| Warren Soultrader | Pay 1 life, sac a creature: Treasure | Pitiless Plunderer (kept) does the same job for free, with no life cost, and triggers automatically on any creature death. |
| Orzhov Locket | Mana rock, late-game sac for 2 cards | Weakest of the deck's ramp pieces; Arcane Signet already covers fixing more efficiently, and the real mana-base gap is haste, not another rock. |

## Challenged and kept
No cuts have been challenged yet — this is the first pass. If anything here looks wrong to you, flag it and I'll re-verify the oracle text immediately before restoring it.

## Proof — a concrete kill-line
Historic Brawl is 1v1 at **25 starting life** (source above). With Teysa Karlov out:
- Ministrant of Obligation (kept, Afterlife 2) dying makes **two** Spirit tokens instead of one (Teysa doesn't double token-creation itself, but Anointed Procession does — if both are out, one Afterlife-2 death produces **four** 1/1 flying lifelink Spirits instead of two, because Teysa grants the lifelink and Procession doubles the count).
- Each of those Spirits swinging in connects for 1 flying damage + 1 lifelink gain — 4 unblocked Spirits is 4 damage and 4 life swing in one attack step from a single 3-mana death trigger, at zero further investment.
- Layer in Cruel Celebrant + Sephiroth, Fabled SOLDIER (both undiluted "target/single opponent loses 1, you gain 1" on any creature death, kept in the list): a single board wipe (Kaya's Wrath or The Meathook Massacre) that kills, say, 6 of your own creatures with Drivnod, Carnage Dominus and Teysa Karlov both out (each death trigger fires **3 times** — base + Teysa + Drivnod) turns into 6 × 3 = 18 individual drain triggers. Against a 25-life opponent, that is lethal or near-lethal directly off your own wrath, before combat.
That's the deck's actual win line, and it doesn't depend on hitting 3 opponents to work — everything above is either undiluted (targets "a player"/"an opponent" once) or self-referential to your own board, so 1v1 Brawl doesn't weaken it.

## Optional upgrades (verified, NOT applied — future 1:1 swap candidates if you want to keep iterating)
All checked for oracle text and confirmed genuinely Arena-legal (`brawl: legal`) with a real printing:

| Card | Verified text | Real Arena printing | Why it'd help |
|---|---|---|---|
| Damn | Destroy target creature, no regen; Overload {2}{W}{W} to make it "each" | AA2 8 | A 2-mana spot removal spell that's *also* a 4-mana board wipe in the same card — pure flexibility upgrade over a dedicated single-mode removal spell. |
| Anguished Unmaking | Exile target nonland permanent, lose 3 life | OTP 35 | Answers artifacts/enchantments/planeswalkers too, not just creatures — broader than Mortify. |
| Corrupted Conviction | Sac a creature (additional cost), draw two | OTJ 84 | 1-mana, undiluted, efficient card advantage off a creature you were sacrificing anyway. |
| Bojuka Bog | Enters tapped, exile target player's graveyard, taps for B | HA2 20 | Free graveyard hate on a land slot; also answers reanimator/Living End-style opposing strategies. |
| High Market | Colorless sac outlet land, gain 1 life on sac | EOS 18 | A land that doubles as a completely free extra sac outlet — pure upside over a basic. |

**Flagged as unavailable despite strong EDHREC synergy (do not add — not on Arena):** Skullclamp (77% EDHREC inclusion, colorless equipment, no Arena printing at all) and Phyrexian Altar (43% inclusion, same issue). Both read `brawl: not_legal` — this is the exact "Sol Ring lesson" the project's methodology warns about, confirmed again here.
