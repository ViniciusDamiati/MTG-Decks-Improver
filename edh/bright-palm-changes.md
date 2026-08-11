# Bright-Palm, Soul Awakener — Upgrade Notes (July 2026)

Changes applied to `bright-palm.txt`. Every card mentioned below was verified against its
exact Scryfall oracle text before any decision. The deck was — and remains — **exactly 100
cards** (99 + commander).

Data sources:

- EDHREC commander page (3,308 Bright-Palm decks): https://edhrec.com/commanders/bright-palm-soul-awakener
- EDHREC average decklist (aggregated from Moxfield): https://edhrec.com/average-decks/bright-palm-soul-awakener
- Card texts: Scryfall API

## What Bright-Palm actually does (verified)

- **{1}{R}{G}{W}, 4/3 Fox Shaman**
- **Backup 1** — on entry, put a +1/+1 counter on target creature; if it's another creature,
  it also gains the attack trigger below until end of turn.
- **Attack trigger:** *double* the number of +1/+1 counters on **one target creature**, and
  that creature can't be blocked by creatures with power 2 or less this turn.

This is the opposite of Jetmir: not "go wide," but **grow one exponential threat**. Every
counter you can stack before combat gets doubled — then doubled again next turn. The deck's
job is (1) get counters down early, (2) amplify or copy the doubling trigger, (3) convert one
huge creature into a win, and (4) refill the hand while doing it.

## The diagnosis

The list was already good — it ran 13 of EDHREC's top-15 synergy cards. Three real problems:

1. **Card draw was nearly absent.** Real draw was Inspiring Call, The Great Henge, and the
   monarchy from Court of Garenbrig. A deck that goes tall gets 2-for-1'd by every removal
   spell; it needs to refuel harder than any other archetype.
2. **No way to amplify the commander's own trigger.** The single most Bright-Palm card in
   the data — Strionic Resonator (45% inclusion, highest synergy artifact) — was missing.
   Copying "double the counters" turns ×2 into ×4 per attack.
3. **A few verified duds.** Cards that read like counter synergy but do almost nothing on
   inspection (see the swap table).

## The swaps (8 out, 8 in)

| # | Out | In | Reason (verified against oracle text) |
|---|-----|----|--------------------------------------|
| 1 | Falkenrath Exterminator | **Strionic Resonator** | Exterminator is a 1/1 that only gains a counter when *it* connects with a player — off-plan and tiny. Resonator (45% inclusion, top-synergy artifact) copies Bright-Palm's attack trigger: 8 counters → 16 → **32 in one combat**, for {2}. It also copies Aragorn's doubling, Kalonian Hydra, Armorcraft Judge's draw, Guardian Scalelord's reanimation… |
| 2 | Panharmonicon | **Armorcraft Judge** | Panharmonicon only amplifies ETB triggers of *artifacts/creatures entering* — this deck has few, and it does nothing the turn it lands (11% inclusion, near-zero synergy). Judge (41%): "draw a card for each creature you control with a +1/+1 counter" — in this deck that's routinely 4-8 cards on a body. |
| 3 | Idyllic Tutor | **Rishkar's Expertise** | Same verdict as in the Jetmir audit: 3 mana, card-neutral, zero board impact. Expertise draws cards equal to your greatest power — behind Bright-Palm that's 8-20+ — **then free-casts a 5-drop from your hand**. |
| 4 | Resourceful Defense | **Incubation Druid** | Defense is insurance that only pays off when your things die, with a clunky {4}{W} activation; absent from EDHREC's top lists. Druid (64% inclusion) taps for **3 mana** once it has any counter on it — trivial here (Backup, Rishkar, Master Chef, Good-Fortune Unicorn all do it for free). |
| 5 | Together Forever | **Evolution Sage** | Support 2 plus a death-insurance ability that rarely gets used. Sage proliferates on **every landfall** — with 37 lands and four fetches (Arid Mesa, Windswept Heath, Wooded Foothills, Fabled Passage = two triggers each), every counter on the board grows every single turn. |
| 6 | Cathars' Crusade | **Guardian Scalelord** | Crusade needs a *stream* of creatures entering; this deck runs zero token production, so it's a 5-drop that adds ~1 counter per creature per turn — and it isn't even in EDHREC's top-12 enchantments for Bright-Palm. Scalelord (60%, #2 synergy creature), same 5 MV: Backup 1 on entry, and every attack returns a nonland permanent with MV ≤ its power from your graveyard — its power grows every time Bright-Palm targets it. |
| 7 | Bramblewood Paragon | **Kodama of the West Tree** | Paragon's Warrior clause is dead (almost no Warriors) — it was a 2-mana trample anthem, and Pridemalkin already covers that. Kodama grants the same trample to all modified creatures **plus** fetches a basic land onto the battlefield every time any of them connects — trample and ramp in one slot. |
| 8 | Uncharted Haven | **Exotic Orchard** | Haven always enters tapped for one fixed color. Orchard (67% inclusion) enters untapped and taps for any color an opponent's lands produce — in a 4-player pod that's nearly always all three of yours. |

## Cards challenged, verified, and kept

The audit almost cut these — the oracle text saved them:

- **Aragorn, Hornburg Hero** — far stronger than it looks: all your attackers get first
  strike and renown 1, and whenever any renowned creature you control hits a player,
  **double the number of +1/+1 counters on it**. It's a second Bright-Palm that works on
  every attacker, every combat.
- **Bone Sabres** — puts **four** +1/+1 counters on the equipped creature every attack —
  before Bright-Palm's doubling resolves. Turn N: equip + attack = 4 → 8 counters from two
  cards.
- **Mayael's Aria** — verified: win the game at 20+ power. With doubling (8 → 16 → 32) this
  is a real, uncounterable win condition checked every upkeep, from a 3-mana enchantment.
- **Court of Garenbrig** — monarch (draw every turn) plus, while you keep the crown,
  **double the counters on EVERY creature you control** each upkeep — not just one target.
- **Heliod, Sun-Crowned + Walking Ballista** — confirmed infinite: Heliod grants Ballista
  lifelink; remove a counter → 1 damage → 1 life → Heliod replaces the counter. Both stay,
  always.
- **Uncivil Unrest** — riot for all nontoken creatures *and* creatures with counters deal
  **double damage**. On top of Bright-Palm's doubling, a 10-counter attacker hits for 20+.
- **Doubling Season / Branching Evolution** — kept: Bright-Palm's "double the counters"
  places N new counters, and these make it 2N placed — the trigger becomes a **tripling**.
  With Resonator copying it: 9× per combat.
- **Defiler of Vigor, Elite Scaleguard, Master Chef, Mirror-Style Master, Sword of Truth
  and Justice, Virtue of Loyalty, All Will Be One** — all verified, all synergistic, all
  kept. (All Will Be One turns every counter placement into face damage — with a doubling
  trigger on a 10-counter creature, that's 10+ damage per attack before combat even starts.)

## Why the changes are stronger — the proof

**The commander's math is exponential; feed the exponent.** Bright-Palm turns N counters
into 2N per attack. The swaps add multipliers to that exponent: Strionic Resonator (×4 per
combat), Evolution Sage (+1 every land, twice per fetch), Guardian Scalelord (bigger every
loop). Turn 4 attack on a creature with 4 counters, with Resonator: 16 counters. Turn 5:
32-64. Mayael's Aria checks at 20; Kessig Wolf Run and Rogue's Passage push it through.

**Draw beats a perfect board.** The deck's tall threat is a lightning rod for removal. The
new package — Armorcraft Judge (≈4-8 cards), Rishkar's Expertise (≈8-20 cards + free
5-drop), plus the retained Inspiring Call / Great Henge / monarchy — means a wipe costs you
a turn, not the game. Every replaced card was verified to add zero cards or zero board.

**The data agrees.** All eight additions are in EDHREC's top cards for this exact commander
(Resonator 45%, Incubation Druid 64%, Scalelord 60%, Judge 41%, Orchard 67%); all eight cuts
sit at or below the bottom of their category lists (Panharmonicon 11%, Cathars' Crusade and
Falkenrath Exterminator not charting at all).

**Creature count moves the right way.** 26 → 29 mainboard creatures (EDHREC average: 33-34),
and two of the new bodies (Incubation Druid, Evolution Sage) are engines the deck can deploy
early and win through.

## Optional upgrades (not applied)

- **Roaming Throne** (name Fox) — Bright-Palm's attack trigger happens twice; stacks with
  Resonator for ×8 combats.
- **Innkeeper's Talent** — level 3 is Doubling Season for counters at half the install cost,
  plus ward for your whole board at level 2.
- **Invigorating Hot Spring** — haste for all modified creatures; lets Bright-Palm (Backup
  targets itself) attack the turn it lands.
- **Inscription of Abundance / Return of the Wildspeaker** — instant-speed counters/removal
  and a second "draw = greatest power" spell if the deck still feels thirsty.
- **Sunscorch Regent / Abzan Battle Priest / Mikaeus, the Lunarch** — cheap ways to push
  creature count toward the 33-34 average.
