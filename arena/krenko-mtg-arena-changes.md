# Krenko, Mob Boss — MTG Arena Brawl/Commander Upgrade

## Sources
- Local card database (`.claude/scripts/card_db.py`) — primary oracle-text source for all cards touched.
- mtgtop8 cEDH: https://mtgtop8.com/format?f=cEDH — Krenko has **no cEDH presence** (0 decklists; only appears in the commander dropdown).
- EDHREC: https://json.edhrec.com/pages/commanders/krenko-mob-boss.json, https://edhrec.com/commanders/krenko-mob-boss, https://edhrec.com/average-decks/krenko-mob-boss — 43,099 decks, rank #5 overall commander.
- Scryfall API (`api.scryfall.com`) — Arena availability, legalities, and exact set/collector numbers for every card checked.

## Verified commander text
**Krenko, Mob Boss** — {2}{R}{R}, Legendary Creature — Goblin Warrior, 3/3.
`{T}: Create X 1/1 red Goblin creature tokens, where X is the number of Goblins you control.`
A pure exponential go-wide engine: each activation roughly doubles the Goblin count. The deck's entire job is (1) get to a critical mass of Goblins fast, (2) protect/untap Krenko to activate repeatedly, (3) convert the token flood into damage before the single Arena opponent stabilizes.

## Methodology note — how Arena legality was verified
Every current and candidate card was run through the `arena-legality-checker` agent, which checks `games` on every printing (not just the newest) plus `legalities.brawl` / `legalities.competitivebrawl` via live Scryfall — the local DB only holds the newest printing per card, which isn't enough to prove Arena availability. Key findings from that process:
- **False positives caught**: three cards already in the deck had a set/collector pair that doesn't exist as a real Arena printing (would have failed to import) — corrected below.
- **True negatives found**: several EDHREC top-10-synergy staples (Skullclamp, Coat of Arms, Goblin King, Brightstone Ritual, Goblin Recruiter, Goblin War Strike, Massive Raid, Battle Hymn) have **never been printed to Arena** — not banned, just absent from the digital pool. These were excluded even though EDHREC ranks them extremely highly, per the "Sol Ring lesson" in the project methodology. Skullclamp in particular is not currently banned in Brawl; it simply doesn't exist as a `games: ['arena']` printing on any of its 29 real-world printings.
- **Alchemy-native cards are fair game**: Raging Goblin and Tin Street Cadet (both from Alchemy Horizons: Baldur's Gate, `ANB`) have no paper printing and read `commander: not_legal` in paper terms, but are genuinely playable on Arena Brawl — kept as-is.
- All 16 additions below were confirmed `brawl: legal` / `competitivebrawl: legal`, mono-red or colorless, with a real Arena set/collector number.

## Diagnosis
- **Deck count/health**: exactly 100 going in, no duplicates, no color-identity violations (mono-red, all cards are R or colorless) — the deck was legally clean but strategically underpowered.
- **Missing nearly every goblin-tribal payoff card**: of EDHREC's top 10 highest-synergy cards for Krenko (Warchief 87.5%, Skirk Prospector 86.3%, Matron 83.8%, Chieftain 77.4%, Impact Tremors 84.6%, Bombardment 73.8%, Pashalik Mons 67.7%, Brightstone Ritual 68.2%, Goblin King 63.9%, Hobgoblin Bandit Lord 63.0%), the deck only had 3 (Skirk Prospector, Impact Tremors, Goblin Bombardment). **No lords, no anthems, no sacrifice payoff** — the deck could make a wide board but had almost nothing to turn "wide" into "lethal."
- **No haste-doubling tribal lords**: Krenko's tokens enter without haste; without a "Goblins you control have haste" effect, every activation's tokens sit for a full turn cycle before they can swing — a much bigger tempo loss in 1v1 (no third player to occupy the downtime) than in a 4-player pod.
- **Too many lands for the curve**: 40 lands (38 Mountain + Cavern of Souls + Three Tree City) against an EDHREC average of 34 and a deck curve that's almost entirely 1-3 mana. Excess lands in an aggressive low-curve deck are dead draws late.
- **Equipment overload, anthem void**: 8 single-target buff pieces (Swiftfoot Boots, Lavaspur Boots, Boots of Speed, Diamond Pick-Axe, Cloak of the Bat, Dragonfire Blade, Chainsaw, The Aetherspark) but zero board-wide anthems. In a token-swarm deck, a card that buffs one creature is far weaker than one that buffs the whole board — Shared Animosity alone (below) outperforms the entire equipment suite in a wide-board scenario.
- **Disjointed artifact-hate/artifact-sac subtheme with no payoff**: Skycrash, Smash to Smithereens, Overwhelming Surge, Gearbane Orangutan, Crime Novelist, and Daretti all reference artifacts, but the deck has no artifact sac-outlet worth using and no guarantee the 1v1 opponent even plays artifacts — this was 5-6 slots doing very little for the core plan.
- **Narrow/dead-trigger fillers**: several commons had conditions the deck can't reliably meet (Mad Ratter needs a second draw each turn with no card-draw engine; Devoted Duelist needs a second spell each turn in a creature-heavy list; Innocent Bystander needs 3+ damage dealt to itself; Goblin Surveyor needs the "speed" mechanic with no other speed synergy).

## Swap table

| # | Cut | Why cut (verified text) | Add | Why add (verified text + EDHREC data) | Arena printing |
|---|---|---|---|---|---|
| 1 | Innocent Bystander (MKM 133) | "Whenever dealt 3+ damage, investigate" — narrow, needs to survive a big hit | Goblin Warchief | Goblin spells cost {1} less; **Goblins you control have haste** — the single biggest fix for the haste gap | DOM 130 |
| 2 | Crime Novelist (MKM 121) | Needs to sacrifice artifacts for value — no sac outlet supports this | Goblin Chieftain | Haste; other Goblins get +1/+1 and haste — second lord, doubles down on the haste fix | JMP 324 |
| 3 | Goblin Picker (DMU 128) | Tempo-negative card filtering, weak in an aggro shell | Goblin Matron | ETB: tutor any Goblin to hand — consistency piece, finds Krenko or the best lord live | HA1 11 |
| 4 | Goblin Tunneler (ANB 73) | Redundant unblockable-power-2-or-less effect, already covered by Underfoot Underdogs | Hobgoblin Bandit Lord | Other Goblins +1/+1; tap for damage = # Goblins that entered this turn — direct payoff for a Krenko activation | AFR 147 |
| 5 | Mad Ratter (ELD 130) | Needs a 2nd draw each turn — deck has no card-draw engine, dead trigger most games | Pashalik Mons (67.7% incl., 0.559 synergy) | Goblin dies → 1 damage to any target; sac a Goblin for two more Goblins — turns the token army into reach and a sac outlet | J21 495 |
| 6 | Goblin Surveyor (DFT 131) | "Start your engines" speed mechanic — no other speed synergy in the deck | Siege-Gang Commander (64.9% incl.) | ETB 3 Goblin tokens; sac a Goblin for 2 damage — three bodies plus a second Bombardment-style burn outlet | DOM 143 |
| 7 | Goblin Gathering (ANB 71) | 2 tokens for 3 mana with no scaling (only 1 copy possible in singleton) — weak rate | Krenko, Tin Street Kingpin (63.5% incl.) | Attacks → +1/+1 counter, then makes tokens equal to its power — a second Krenko-shaped engine that doesn't need to be tapped down first | WAR 137 |
| 8 | Goblin Surprise (FDN 200) | Weak modal — both a tiny +2/+0 anthem and 2 tokens for 3 mana underwhelm | Conspicuous Snoop | Casts Goblin spells off the top of the library and gains their activated abilities — extra card advantage/redundancy for the Goblin-spell package | M21 139 |
| 9 | Devoted Duelist (TDM 104) | Needs a 2nd spell cast every turn — this list isn't spell-dense enough to trigger reliably | Krenko's Command | 2 Goblin tokens for {1}{R} — flatly better rate than the cut Goblin Gathering | J25 140 |
| 10 | Prowcatcher Specialist (DFT 142) | Self-buff with no token/tribal payoff, mediocre rate | Goblin Ringleader | Haste; ETB reveal top 4, take all Goblins — card advantage plus another hasty attacker | M20 143 |
| 11 | Smash to Smithereens (PIO 343) | Narrow artifact-only removal, redundant with Skycrash/Overwhelming Surge in a deck with no artifact-hate payoff | Muxus, Goblin Grandee (50.3% incl.) | ETB reveal 6, put all Goblins MV≤5 onto the battlefield free — potential game-ending burst of bodies | JMP 24 |
| 12 | Gearbane Orangutan (MKM 129) | Same artifact-hate redundancy as above | Legion Warboss | Makes a hasty attacking Goblin token every combat, mentor — a second Krenko-adjacent token engine that doesn't need mana to activate | GRN 109 |
| 13 | 4x Mountain (38→34) | 40 total lands vs. 34 EDHREC average on a curve that peaks at 2-3 mana — excess lands are dead late draws in an aggro shell | Purphoros, God of the Forge | Indestructible; every other creature ETB deals 2 to the opponent — turns every Krenko token (and every Goblin spell) into direct damage, huge in 1v1 where there's only one life total to punch through | FCA 14 |
| 13b | — | — | Shared Animosity (51.3% incl., 0.405 synergy) | Every attacker gets +1/+0 for each other attacker sharing a type — with an all-Goblin board this is a board-wide anthem that scales with token count, strictly better than any single-target equipment already in the deck | MOR 104 |
| 13c | — | — | Empty the Warrens | 2 Goblin tokens with Storm — copies itself for every spell already cast that turn, can dump a huge token wave off a low-curve turn | SOA 43 |
| 13d | — | — | Ashnod's Altar | Sac any creature for {C}{C} — a real sac outlet finally backs Pashalik Mons/Siege-Gang Commander's sac abilities and converts excess tokens into mana to chain more activations | BRR 4 |

**Corrections to existing cards (import-breaking set/collector errors caught by the Arena sweep, no gameplay change):**
| Card | Old (broken) | Corrected |
|---|---|---|
| Foundry Street Denizen | (J21) 72 | (J21) 446 |
| Akroma's Memorial | (SPG) 0 | (SPG) 81 |
| Skirk Prospector | (DAR) 144 | (DOM) 144 |

## Challenged and kept
No cuts were challenged this session (first pass). Cards intentionally kept despite being non-staples, with reasoning:
- **Draconautics Engineer, Goro-Goro, Crashing Drawbridge** — kept as the deck's remaining dedicated haste-granting effects; even with Warchief/Chieftain now covering most of the roster, these still matter for non-Goblin tokens (Eldrazi Spawn, Dragon/Dinosaur tokens) that the lords don't cover.
- **Patchwork Banner, Banner of Kinship, Heraldic Banner** — all three name-a-type/color anthems synergize directly with the now-larger Goblin lord package and were already pulling real weight; not cut.
- **Overwhelming Surge, Skycrash** — kept one flexible removal spell (Overwhelming Surge, modal creature/artifact answer) and one low-opportunity-cost artifact answer (Skycrash has cycling, so it's never a dead card) rather than cutting all artifact interaction to zero.
- **Daretti, Rocketeer Engineer** — kept; with Diamond Pick-Axe, Chainsaw, Aetherspark, and the banners still in the deck, there's enough artifact density in the graveyard over a game to make its recursion occasionally live, and its body is fine on curve.

## Proof — sample kill-turn math (single opponent, starting at 40 life)
Turn 4 line assuming an average start (2-3 Goblins in play by turn 4, common with Skirk Prospector/Krenko's Command/Dragon Fodder on curve):
- Krenko, Mob Boss resolves turn 4 (already summoning sick historically — now **irrelevant**, since Goblin Warchief or Goblin Chieftain in play gives Krenko haste as a Goblin himself).
- Tap Krenko with, say, 3 Goblins already in play → creates 3 more tokens (6 Goblins total).
- If Goblin Chieftain is out, those tokens are +1/+1 and hasty → 6 hasty 2/2 Goblins attack immediately.
- With Shared Animosity out as well, each of the 6 attackers gets +1/+0 for each of the other 5 sharing the Goblin type → each swings as a 7/2 → 42 damage, lethal through a 40-life opponent on the spot.
- Even without Shared Animosity, Purphoros alone turns that single Krenko activation into 3 ETBs × 2 damage = 6 immediate direct damage before combat even happens, on top of whatever combat damage connects.
This is the payoff the old list was missing entirely: it could build the board, but had no way to convert "6 Goblins" into "game over" in the same turn.

## Optional upgrades not applied
- **Skullclamp** — the single highest-synergy artifact for this archetype (61.2% incl.) but confirmed to have **no Arena printing on any of its 29 real-world printings**; not a ban, just unavailable. Worth revisiting if it's ever digitized.
- **Coat of Arms, Goblin King, Brightstone Ritual, Goblin Recruiter, Goblin War Strike, Massive Raid, Battle Hymn** — all strong EDHREC-verified staples, all confirmed **not on Arena**. Same treatment.
- **Thornbite Staff / Goblin Chirurgeon infinite-combo package** — EDHREC lists this combo shell; not pursued here since it pushes toward a combo-kill plan rather than the aggressive go-wide beatdown this upgrade targets, and would need a dedicated legality/availability pass of its own.
