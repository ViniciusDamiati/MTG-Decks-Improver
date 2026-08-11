# Jetmir, Nexus of Revels — Upgrade Notes (July 2026)

Changes applied to `jetmir.txt`. Every card mentioned below was verified against its exact
Scryfall oracle text during the final audit. The deck is now **exactly 100 cards** (99 +
commander) — note: the original list was **103 cards, 3 over the legal limit** (see "Deck size
fix" below).

Data sources:

- EDHREC commander page (9,725 Jetmir decks): https://edhrec.com/commanders/jetmir-nexus-of-revels
- EDHREC tokens theme: https://edhrec.com/commanders/jetmir-nexus-of-revels/tokens
- EDHREC average decklist (aggregated from Moxfield): https://edhrec.com/average-decks/jetmir-nexus-of-revels
- MTGTop8 cEDH archetype (Krisle, 2nd place, Nov 2025): https://mtgtop8.com/archetype?a=1375&meta=327&f=cEDH
- Card texts: Scryfall API

## What Jetmir actually grants (verified)

- **3+ creatures:** +1/+0 and vigilance
- **6+ creatures:** another +1/+0 and trample
- **9+ creatures:** another +1/+0 and double strike (total +3/+0, vigilance, trample, double strike)

## The diagnosis

1. **Too few creatures (18 mainboard).** The EDHREC average Jetmir deck runs 28-32; the cEDH
   list runs 50. Jetmir counts creatures — the 3/6/9 thresholds are the deck's engine.
2. **Too many multipliers/upgraders, not enough to multiply.** Doubling Season, Parallel
   Lives, Anointed Procession, Second Harvest, plus Divine Visitation (which transforms
   created tokens into 4/4 Angels) — all sitting on a thin base of actual producers, and all
   dead on an empty board.
3. **Almost no card draw and zero one-mana ramp.** Draw was Skullclamp, Toski, Idol of
   Oblivion, Rabble Rousing. Nothing to do on turn 1. A mana dork here is double-value:
   it ramps *and* counts toward Jetmir's thresholds.

## The swaps (10 out, 10 in)

| # | Out | In | Reason (verified against oracle text) |
|---|-----|----|--------------------------------------|
| 1 | Divine Visitation (5 MV) | **Mondrak, Glory Dominus** (4 MV) | Visitation transforms tokens into 4/4 Angels — quality, not quantity, and Jetmir already provides quality (+3/+0, double strike). Mondrak doubles token *count*, is itself a body toward 3/6/9, costs 1 less, and can go indestructible. |
| 2 | Battle for Bretagard | **Kutzil, Malamet Exemplar** | #1 non-removal card in Jetmir (54%). Opponents can't cast spells **during your entire turn** — your combats are uninterruptible. And since Jetmir pumps everything, every combat draws cards (one per player damaged, doubled by double strike). Bretagard was a 3-turn saga. |
| 3 | Druidic Satchel | **Shamanic Revelation** | Satchel: 3 mana + 2/activation for a coin-flip trinket. Revelation with 8+ creatures draws 8+ cards, plus 4 life per 4-power creature (Jetmir-pumped boards qualify) — the refuel after a wipe. |
| 4 | Roxanne, Starfall Savant | **Krenko, Tin Street Kingpin** | 42% inclusion. Under Jetmir's pump Krenko attacks as a 4/2+, making 4+ Goblins per swing that snowball every threshold. Roxanne is a 5-drop artifact-token engine — real synergy with Smothering Tithe's Treasures, but off this deck's plan. |
| 5 | Growing Rites of Itlimoc | **Birds of Paradise** | Itlimoc is powerful but is the *fifth* board-scaling mana engine (Cryptolith Rite, Jaheira, Mirari's Wake, Brigid) — all dead on an empty board. Birds is the deck's *first* board-independent turn-1 play: it fixes three colors, lands Jetmir on turn 3, and is a body. *(Originally Brigid was slated here; she stays — see below.)* |
| 6 | Quina, Qu Gourmet | **Llanowar Elves** | The closest call of all cuts. Quina's "+1 Frog per token event" is genuinely synergistic and compounds with Mondrak/Procession. But the deck's hole was turn-1 acceleration, not more mid-game bodies — and the cEDH list's seven one-mana dorks show which axis wins. |
| 7 | Saproling Symbiosis | **March of the Multitudes** | Both make X tokens; March is instant-speed with convoke — end of turn, tap your untapped board (vigilance from 3+ creatures) and make a second army nearly free, with lifelink. Symbiosis needed +2 mana for flash and made vanilla Saprolings. |
| 8 | Idyllic Tutor | **Call the Coppercoats** | 43% in token builds. Instant speed; X = creatures your targeted opponents control, so in a 4-player pod it's routinely 5-10+ Soldiers — and it can flip Jetmir from 6 to 9 mid-combat. Idyllic Tutor was card-neutral, zero board impact, and mostly fetched the doubler category the deck was over-invested in. |
| 9 | Rootborn Defenses | **Grand Crescendo** | The deck ran 7 protection spells — the most redundant slot. Crescendo IS protection (indestructible) that also makes X bodies: protects and rebuilds in one card. Rootborn's populate made a single token copy. 6 protection effects remain. |
| 10 | Ghired, Mirror of the Wilds | **Ohran Frostfang** | Ghired only copies tokens *that entered this turn*, via tap abilities on *nontoken* creatures — two conditions that rarely line up. Frostfang: attackers have deathtouch (blocking pumped 1/1s becomes suicidal) and every creature that connects draws a card. |

## Deck size fix (103 → 100)

The original list was 3 cards over the 100-card limit. Trimmed:

1. **1 Forest** (36 lands → 35) — correct count now that the deck has Sol Ring, two Signets,
   Birds, Llanowar Elves, Cryptolith Rite, Jaheira, and Brigid.
2. **Urabrask's Forge** — verified: its Horror token is *sacrificed at the next end step*.
   It never adds a permanent body toward Jetmir's thresholds; one temporary attacker per turn
   is far below the deck's rate.
3. **Second Harvest** — the fifth mass-doubling effect and the most board-dependent of them:
   pure win-more at instant speed, dead when behind or after a wipe.

## Cards challenged, verified, and kept

- **Toby, Beastie Befriender** — two bodies ({2}{W} for a 1/1 + a 4/4 Beast), and with 4+
  creature tokens all your tokens fly. Jetmir grants trample at 6+, but flying is strictly
  better evasion: fliers take zero blocker interaction and dodge ground deathtouch blocks.
- **Brigid, Clachan's Heart** — front face makes a Kithkin on entry/flip-back; back face taps
  for X mana (X = other creatures), fueling instant-speed X-spells (Coppercoats, March,
  Crescendo) on opponents' turns. Kept at the pilot's call; Growing Rites cut instead as the
  more redundant scaling engine.
- **Securitron Squadron** — every creature token you create enters with a +1/+1 counter
  (all 1/1s become 2/2s); squad {3} makes it multiple bodies itself.
- **Champions from Beyond** — X bodies on entry; scry 2 + draw every combat with 4+ attackers
  (in this deck: every combat). Note: it's an enchantment, not a creature.
- **Windcrag Siege** (Mardu) — doubles attack triggers: Adeline, Anim Pakal, Cadira, Torens,
  Myrel, and Andúril all trigger twice per swing.
- **Andúril, Flame of the West** — on Jetmir (legendary): two 1/1 fliers *tapped and attacking*
  every swing — permanent bodies that count toward thresholds.
- **Idol of Oblivion, Rabble Rousing, Eldrazi Monument, Dalkovan Encampment** — all verified;
  all earn their slots (Dalkovan usually enters untapped here via Mountain-typed duals/triome).

## Why the changes are stronger — the proof

**Jetmir's math rewards bodies, not buffs.** At 9 creatures: Jetmir swings as an 8/4 double
striker (16) and each 1/1 as a 4/1 double striker (8). Jetmir + eight tokens = **80 damage in
one swing**. Going from 6 to 9 creatures roughly triples output (double strike turns on);
adding another doubler to a 3-token board adds a handful of 1/1s. Bodies cross thresholds;
multipliers don't.

**Draw beats hoarding protection.** Board wipes are how token decks lose. The old plan was 7
protection spells — dead when no wipe comes. The new plan adds engines (Kutzil, Frostfang,
Shamanic Revelation): ~7 repeatable/mass draw effects instead of 4, while keeping 6 protection
spells — still above the field average.

**The cEDH list is the controlled experiment.** Built with no budget ceiling, Jetmir is 50
creatures, 25 lands, seven one-mana dorks, and a curve stopping at ~3. The competitive extreme
shows the winning axis: cheap creature density and speed, not enchantment stacking.

**Speed.** Mainboard creatures go from 18 to 21 with a far cheaper curve, plus four
instant-speed token spells that add bodies mid-combat. The dorks bring Jetmir out turn 3
instead of 4-5 — one full turn earlier on a commander that converts every later play into
damage.

## Optional upgrades (not applied)

- **Gaea's Cradle** — the cEDH list runs it; absurd here.
- **Esper Sentinel, Ocelot Pride** — premium 1-drops from the average list.
- **Voice of Victory** — opponents can't cast spells during your turn (redundant with Kutzil, but stacking the effect on a body is strong).

---

## August 2026 review — 2 more swaps

Follow-up pass, prompted by a much richer EDHREC dataset gathered while separately rebuilding
the MTG Arena version of this deck (9,766-deck sample, full per-category inclusion/synergy
data). Re-verified oracle text for every card flagged as a possible cut before touching
anything — full texts confirmed via Scryfall.

**Correction caught during this pass:** the review started from an assumption that the deck ran
only one 1-mana dork (Birds of Paradise) — wrong. Llanowar Elves was already in the list; it was
missed on a first skim. No swap was made against it. Recorded here per the project's own rule
that memory errors get corrected in the doc, not quietly dropped.

Two cards from the July "optional upgrades, not applied" list turned out to be worth actually
applying, against two genuinely weak/narrow current slots (verified by full oracle text, not
assumption — several other suspects, listed below, turned out to be *stronger* than remembered
and were explicitly kept):

| # | Out | In | Reason (verified oracle text + EDHREC data) |
|---|-----|----|--------------------------------------|
| 1 | Grove of the Guardian | **Craterhoof Behemoth** | Grove: `{3}{G}{W}, {T}, Tap two untapped creatures you control, Sacrifice this land: Create an 8/8... vigilance` — a one-shot 8/8 for a land, two tapped creatures, and 5 mana; narrow and slow. Craterhoof: haste, and "creatures you control gain trample and get +X/+X... where X is the number of creatures you control" on ETB — the actual "kill the table" button flagged but never added in July (22% EDHREC inclusion on the fresh dataset). At even 10 creatures that's a team-wide +10/+10 trample swing across all opponents in one turn. |
| 2 | Idol of Oblivion | **Jinnie Fay, Jetmir's Second** | Idol: `{T}: Draw a card. Activate only if you created a token this turn` — solid but conditional, and this deck already runs Skullclamp, Rabble Rousing, Grand Crescendo, and Shamanic Revelation for draw. Jinnie Fay: "If you would create one or more tokens, you may instead create that many 2/2 green Cat creature tokens with haste or that many 3/1 green Dog creature tokens with vigilance" — turns *every* token-making card in the deck (including the copies from Doubling Season/Anointed Procession/Parallel Lives, and the X-tokens from March of the Multitudes/Grand Crescendo/Champions from Beyond) into immediate attackers. Exact Naya color identity, and literally the "Jetmir's Second" card — 34.9% EDHREC inclusion, previously overlooked. |

### Verified and kept (suspected weak, turned out strong on re-read)

Re-checked oracle text on several cards before deciding whether to touch them. All of these
were stronger than remembered and were left alone:

- **Triumph of the Hordes** — `creatures you control get +1/+1 and gain trample and infect`
  until EOT. This isn't a narrow combo piece; it's a genuine alpha-strike finisher, and it
  stacks nastily with Jetmir's own double strike at 9+ creatures — double strike means each
  attacker deals *two* instances of infect damage, so a lethal poison swing needs half as much
  raw power as it looks like on the card.
- **Champions from Beyond** — beyond the X-bodies-on-ETB noted in July, it also has "Full
  Party — whenever you attack with eight or more creatures, those creatures get +4/+4 until end
  of turn," a second finisher mode this deck's creature count regularly hits.
- **Impact Tremors, Windcrag Siege, Securitron Squadron** — all confirmed to do exactly what
  the July doc said; all correctly credited as strong in a 4-player pod specifically (the "to
  each opponent" wording is a *multiplier* here, not a dilution — that only becomes a 1v1-format
  caveat, which does not apply to this paper build).

### Play-pattern caution (not a cut — a warning)

- **Hour of Reckoning** destroys all *nontoken* creatures, including your own — Jetmir himself,
  Myrel, Kutzil, Krenko, Toski, and every other legendary/value creature in the 99 are nontoken
  and die to it too. It's still correctly in the deck (20.8% EDHREC inclusion, and convoke makes
  it cheap off a wide board of *tokens*, which survive) — but sequence it for after your nontoken
  threats have already gotten their value, or when the token half of your board can carry the
  game on its own, not as a reflexive answer while Jetmir is your only real threat on board.

Deck re-verified at exactly 100 cards after both swaps; no duplicates; color identity of both
adds confirmed within Naya (G, and G/R/W respectively).
