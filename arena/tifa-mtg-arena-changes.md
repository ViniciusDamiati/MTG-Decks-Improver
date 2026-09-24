# Tifa, Martial Artist — MTG Arena 1v1 Upgrade (August 2026)

Changes applied to `tifa-mtg-arena.txt` (100-card 1-on-1 Commander/Brawl build). Every card
mentioned below was verified against exact Scryfall/local-DB oracle text and live Arena printing
data. **7 collector-number corrections + 5 power-level swaps**, deck stays at exactly 100 cards
(99 + commander).

## Data sources

- EDHREC commander page + JSON (7,414 decks, rank #360):
  `https://edhrec.com/commanders/tifa-martial-artist`
- mtgtop8 cEDH: `https://mtgtop8.com/format?f=cEDH` — **Tifa has zero deck submissions or
  tournament results** in any mtgtop8 format, including cEDH. No competitive record to lean on;
  this upgrade runs entirely on the EDHREC baseline plus 1v1-specific reasoning.
- Card texts + Arena/Brawl legality: local `mtg_cards` DB + Scryfall API (`/cards/named`,
  `/cards/search`)

## Tifa, Martial Artist — verified text

> {1}{R}{G}{W}, Legendary Creature — Human Monk, 4/4
> Melee (Whenever this creature attacks, it gets +1/+1 until end of turn for each opponent you
> attacked this combat.)
> Whenever one or more creatures you control with power 7 or greater deal combat damage to a
> player, untap all creatures you control. If it's the first combat phase of your turn, there is
> an additional combat phase after this phase.

Axis: raw creature power. She wants power-7+ attackers connecting to chain untaps and extra
combat phases. Melee itself caps at +1/+1 in 1v1 (only one opponent to attack), so her own combat
trigger — not Melee — is the real engine here.

## Methodology note: Arena legality verification

Every card already in the list and every candidate add was run through `arena-legality-checker`
(live Scryfall across all printings, not just the local DB's newest-printing snapshot), checking
`games` includes `arena`, `legalities.brawl` reads `legal`, and color identity stays within
Tifa's {R, G, W}. The sweep caught **seven mis-filed printings already sitting in the decklist**
— real, Arena-legal cards filed under a paper-only collector number — plus flagged one candidate
add (Sephiroth, Fallen Hero) as genuinely absent from Arena despite scoring well on EDHREC synergy.

## 1v1-specific read

Tifa's Melee is diluted in 1v1 (+1/+1 max instead of a multiplayer pod's +2/+2 or +3/+3), but her
core payoff — untap-and-extra-combat off power-7 damage — is undiluted: it only needs to connect
with the *one* opponent present. No symmetric-effect traps were found among the counter-doubling
package already in the deck (Doubling Season, Branching Evolution, Hardened Scales, Vorinclex are
all restricted to "you"/"your").

## The diagnosis

1. **Seven collector-number errors** — cards genuinely on Arena, filed under printings that
   aren't:
   - `Hamza, Guardian of Arashin (CMR) 278` → real Arena printing `(HA4) 18`.
   - `Shalai, Voice of Plenty (DAR) 35` → real Arena printing `(DOM) 35`.
   - `Elvish Mystic (M14) 169` → real Arena printing `(HOC) 205`.
   - `Hardened Scales (J21) 99` (that number is a different card on Arena) → `(J21) 582`.
   - `Mirari's Wake (JUD) 139` → real Arena printing `(HA3) 23`.
   - `Abzan Falconer (J21) 2` (wrong number) → `(J21) 34`.
   - `Abzan Battle Priest (J21) 1` (wrong number) → `(J21) 33`.
2. **Five filler creatures that don't advance the power-7 plan.** Verified oracle text on each:
   - `Sovereign Okinec Ahau` only equalizes *other* creatures' power up to its own base power
     (3) — it can't push anything toward 7, and its own power is too low to trigger Tifa itself.
   - `Grumgully, the Generous` grants only +1/+1 and only to non-Humans — negligible movement
     toward the threshold.
   - `Good-Fortune Unicorn` grants a single +1/+1 counter per creature ETB — same problem, too
     slow and too small.
   - `Pridemalkin` is a second, weaker copy of the trample-on-countered-creatures effect Kodama
     of the West Tree already provides — redundant.
   - `Warden of the Grove` scales off its *own* counter count over several turns before its
     endure ability matters — too slow for a deck that wants to hit power 7 and swing.
3. **Removal is thin (4 pieces) and instant-speed interaction is light (5 cards against an
   EDHREC average of 9)** for a 1-on-1 format where every removal spell has to answer the one
   opponent's one best blocker or threat — there's no third player's turn to buy time.
4. **The haste package is nearly empty** — only Lightning Greaves and Rhythm of the Wild grant
   haste anywhere in the 100. A power-7+ creature that has to wait a turn to attack gives the
   single opponent a free turn to develop an answer.

## The swaps

### Collector-number corrections (7, same card kept, printing fixed)

| Card | Wrong printing | Corrected printing |
|---|---|---|
| Hamza, Guardian of Arashin | (CMR) 278 | (HA4) 18 |
| Shalai, Voice of Plenty | (DAR) 35 | (DOM) 35 |
| Elvish Mystic | (M14) 169 | (HOC) 205 |
| Hardened Scales | (J21) 99 | (J21) 582 |
| Mirari's Wake | (JUD) 139 | (HA3) 23 |
| Abzan Falconer | (J21) 2 | (J21) 34 |
| Abzan Battle Priest | (J21) 1 | (J21) 33 |

### Power-level swaps (5 out, 5 in)

| # | Out | In | Reason (verified oracle text + Arena/Brawl legality) |
|---|-----|----|--------------------------------------|
| 1 | Sovereign Okinec Ahau (3) | **Iroas, God of Victory** (4) | Okinec Ahau can only pump others up to its own power 3 — no path to Tifa's threshold. Iroas: universal menace for your team (makes big attackers far harder to chump-block in 1v1) plus damage prevention on your attackers; itself a power-7 indestructible body once devotion is met. Confirmed Arena via Pioneer Masters (PIO 309), `brawl: legal`, CI {R,W}. |
| 2 | Grumgully, the Generous (3) | **Anzrag, the Quake-Mole** (4) | Grumgully's +1/+1-to-non-Humans is too small to matter. Anzrag is an 8-power body on its own — already past the power-7 bar on a single hit — and its extra-combat trigger fires off being *blocked*, not just damage dealt, generating a second combat even through a chump block. Confirmed Arena (MKM 186), `brawl: legal`, CI {G,R}. |
| 3 | Good-Fortune Unicorn (3) | **Xenagos, God of Revels** (5) | Unicorn's one +1/+1 counter per ETB doesn't scale fast enough. Xenagos doubles a creature's power and grants haste at the start of combat — a 4-power creature becomes an 8-power hasty attacker in the same turn it enters, directly solving both the power-7 gap and the haste gap at once. Confirmed Arena (PIO 318), `brawl: legal`, CI {G,R}. |
| 4 | Pridemalkin (3) | **Goreclaw, Terror of Qal Sisma** (4) | Pridemalkin duplicates Kodama of the West Tree's trample-on-counters effect for less value. Goreclaw reduces the cost of power-4+ creatures (getting them down faster) and buffs+tramples the entire power-4+ subset on attack — pushing exactly the creatures on the doorstep of Tifa's threshold over the line, with trample to guarantee damage gets through. Confirmed Arena (M19 186), `brawl: legal`, CI {G}. |
| 5 | Warden of the Grove (3) | **Path to Exile** (1) | Warden is a slow, self-referential value engine that doesn't reliably enable power 7. Path to Exile is the most efficient removal spell in Naya colors — 1 mana, unconditional creature exile — directly answering the "removal is thin" diagnosis; the opponent's optional basic-land fetch is a minor, acceptable downside in exchange for tempo. Confirmed Arena (OTP 6), `brawl: legal`, CI {W}. |

**Considered and rejected:** Sephiroth, Fallen Hero scored as the single best synergy fit found
(enters at power 7, can set a whole modified board to base 7/5 on attack) but has **zero Arena
printing** (`games: ['paper','mtgo']` only, `brawl: not_legal`) — excluded on legality grounds,
not power level. Iroas was substituted in as the next-best verified-legal option.

## Legality sweep of the rest of the current list

Ran the full Arena/Brawl-legality check across all 100 cards (initial pass had a transient
network-retry bug that produced false negatives; re-verified with proper error handling and a
clean third pass on the flagged subset). Beyond the 7 collector-number fixes above, all remaining
72 cards — Vorinclex, Krenko Tin Street Kingpin, Toski, The Ozolith, Chromatic Lantern, every
fetch/shock/pain land, Cathars' Crusade, Boseiju, Journey to Nowhere, Swords to Plowshares,
Cultivate, Command Tower, Reliquary Tower, Cavern of Souls, Lightning Greaves, Birds of Paradise,
Akroma's Will, Krosan Grip, Arid Mesa, and the three basics — resolved to their listed printing
exactly, confirmed present on Arena, `brawl: legal`, color identity within R/G/W. Zero banned
cards, zero color-identity violations.

## Why the changes are stronger — the proof

**Anzrag alone clears the power-7 bar on cast.** An 8/4 body that generates its own extra combat
phase when blocked means the single opponent can't simply chump it away — blocking Anzrag *is*
the trigger. Combined with Tifa's own ability (which also grants an extra combat once a power-7+
creature connects), a single unanswered Anzrag attack can produce two full extra-combat chains in
one turn.

**Xenagos turns any mid-size threat into a same-turn attacker at power 7+.** A creature at 4 power
(Kutzil, Anim Pakal, or any counter-loaded body already in the 100) becomes an 8-power hasty
attacker the turn Xenagos is online — no more waiting a turn for summoning sickness to clear
*and* a turn for counters to accumulate before Tifa's trigger becomes live.

**Haste sources moved from 2 to 3** (Lightning Greaves, Rhythm of the Wild, Xenagos), directly
answering the "board sits still for a turn" 1v1 tempo tax the methodology flags as a real cost
against a single opponent.

**Removal moved from 4 to 5 pieces**, with Path to Exile specifically being the cheapest,
least-conditional answer in the deck's colors — a genuine gap-filler against whatever the
opponent's best blocker turns out to be.

## Optional upgrades not applied

- **Sephiroth, Fallen Hero** — excellent synergy (see above) but confirmed absent from Arena;
  revisit if it's ever ported.
- **Adriana, Captain of the Guard** — confirmed Arena-legal and R/W, grants Melee to the whole
  team, but Melee's ceiling is capped at +1/+1 in 1v1 (only one opponent to attack), making it a
  much weaker pickup here than in the 4-player pod EDHREC's data reflects. Left out in favor of
  Iroas, whose menace/damage-prevention has full value regardless of pod size.
- **38 lands (vs. an EDHREC average of 35)** was noted during diagnosis but left untouched — the
  deck already runs real top-end mana sinks (The Great Henge, Mirari's Wake, Cathars' Crusade)
  and a full ramp package (8 pieces), so the land count wasn't the priority fix versus the
  power-7-enablement and haste gaps addressed above. Worth revisiting if future games show
  consistent flood.
