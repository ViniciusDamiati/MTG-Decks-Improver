# Tyvar the Bellicose — MTG Arena 1v1 Curve Upgrade (September 2026)

Changes applied to `tyvar-mtg-arena.txt`, the **MTG Arena** 100-card 1-on-1 Commander/Brawl
build. Every card mentioned below was verified against exact Scryfall/local-DB oracle text.
**5 swaps**, deck stays at exactly 100 cards (99 + commander).

## Revision note

An earlier pass at this upgrade targeted protection/haste/draw gaps; the deck owner reviewed
it and identified the diagnosis itself as wrong — the deck's real problem is **mana curve and
speed**, not those categories. That version was fully reverted (confirmed back to the original
99-card list) before this pass began. Everything below is a fresh diagnosis and swap set built
specifically around curve/speed.

## Data sources

- Local card DB (`card_db.py`) for CMC/oracle text on all 69 nonland cards in the deck, falling
  back to live Scryfall for 2 entries the local DB returned stale/wrong data for (Llanowar Elves
  resolved to a token printing; Tarmogoyf resolved to a non-legal token variant — both corrected
  via live lookup).
- EDHREC commander page + raw JSON (3,644 decks, rank #742) for the baseline curve to compare
  against: `https://edhrec.com/commanders/tyvar-the-bellicose`.
- Arena/Brawl legality: `arena-legality-checker` agent (Scryfall `game:arena` +
  `legalities.brawl` cross-check), run in four separate batches as candidate after candidate
  turned out to be paper/MTGO-only (see below).

## What Tyvar the Bellicose actually grants (re-verified)

`{2}{B}{G}` Legendary Creature — Elf Warrior, 5/4:
> Whenever one or more Elves you control attack, they gain deathtouch until end of turn.
> Each creature you control has "Whenever a mana ability of this creature resolves, put a
> number of +1/+1 counters on it equal to the amount of mana this creature produced. This
> ability triggers only once each turn."

Relevant to the curve diagnosis: mana-ability creatures are only useful once they can actually
tap — and a summoning-sick creature cannot activate a {T} ability the turn it enters (it needs
haste or to have been under your control since your last turn began). So every dork in this
deck is inherently a turn-behind unless you already have one in play. The fewer 1-drops you
have, the more often your ramp plan itself starts a turn late.

## The (corrected) diagnosis: curve, not categories

Full CMC histogram of the original 69 nonland cards (commander excluded):

| CMC | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8+ |
|---|---|---|---|---|---|---|---|---|
| Count | **4** | **23** | 23 | 14 | 0 | 0 | 2 | 2 |

(1-drop creatures only: Llanowar Elves, Allosaurus Shepherd, Elvish Mystic, Birds of Paradise —
plus Bone Splinters, a non-creature spell, at CMC 1.)

Compare to EDHREC's own average Tyvar decklist curve: **10** cards at CMC 1, 15 at CMC 2, 22 at
CMC 3, 13 at CMC 4. This deck was running **less than half** the EDHREC-average count of
1-drops, while carrying **20 separate mana-dork creatures plus 30 lands** — an unusually heavy
mana base that, paradoxically, makes the deck *slower*, not faster: with so few 1-drops, the
ramp chain itself frequently doesn't start until turn 2, and the deck was leaning on quantity of
redundant 2-3 mana dorks rather than a reliable turn-1 start. The 7+ CMC top end (Craterhoof
Behemoth, Nyxbloom Ancient, Zopandrel, The Great Henge) is only 4 cards total — not the actual
bottleneck; cutting into it wouldn't meaningfully speed the deck up.

**The fix:** cut the weakest, most redundant 2-mana dorks (the deck has 20 mana sources — it
doesn't need all of them) and replace them with genuine 1-mana plays: efficient interaction that
protects the board/clears blockers cheaply, plus real early bodies/utility. This compresses the
curve toward the EDHREC baseline and gets the deck doing something relevant on turn 1 far more
consistently.

## Arena availability reality check — this took 4 rounds

Classic EDH/cEDH-staple 1-drops for B/G turned out to be **almost entirely absent from Arena**.
Checked and rejected, in order, because none has ever had an Arena printing
(`legalities.brawl: not_legal`, zero printings with `arena` in `games`):

- Nettle Sentinel, Fyndhorn Elves, Joraga Treespeaker (round 1)
- Elves of Deep Shadow, Arbor Elf (round 2)
- Carrion Feeder, Gravecrawler (round 3)

Round 4 pivoted toward cheap black removal instead of more creature bodies, and all three
candidates cleared: Disfigure, Tragic Slip, Cast Down. Fatal Push and Deathrite Shaman (rounds
1–2) and Diregraf Ghoul (round 3) had already cleared. Final selection favored the strongest of
the confirmed-legal pool.

## The swaps (5 out, 5 in)

| # | Out | In | Reason (verified oracle text + Arena/Brawl legality) |
|---|-----|----|--------------------------------------|
| 1 | Elfhame Druid `{1}{G}` 0/2 — taps for {G}, or {G}{G} restricted to kicked spells (none in this deck, dead clause) | **Fatal Push** `{B}` instant — "Destroy target creature if it has mana value 2 or less. Revolt — ...mana value 4 or less instead if a permanent left the battlefield under your control this turn." | Weakest dork in the deck, worse than Llanowar Elves (2 mana vs 1, smaller body). Fatal Push is 1-mana efficient removal that clears an opposing blocker/threat without costing a turn of development. Verified Arena-legal: KLR 84, `brawl: legal`. |
| 2 | Druid of the Cowl `{1}{G}` 1/3 — taps for {G}, no upside beyond the body | **Deathrite Shaman** `{B/G}` 1/2 — "{T}: Exile target land card from a graveyard. Add one mana of any color. / {B},{T}: exile an instant/sorcery from a graveyard, opponent loses 2 life. / {G},{T}: exile a creature from a graveyard, you gain 2 life." | Pure vanilla dork with no reason to exist alongside the deck's other 19 mana creatures. Deathrite Shaman is a true 1-drop that's simultaneously a flexible mana source, reach (direct life loss), and lifegain — far higher ceiling than another {T}: add {G} body. Verified Arena-legal: EA3 15, `brawl: legal`. |
| 3 | Lys Alana Dignitary `{1}{G}` 2/3 — additional cost to cast (behold an Elf you control, or pay {2} more if you don't have one yet), tap ability dead until an Elf is in your graveyard | **Diregraf Ghoul** `{B}` 2/2 (enters tapped) | Verified text shows Lys Alana Dignitary is effectively a 4-mana play in the early game (no Elf to behold yet) with a mana ability that's dead until something dies — bad tempo exactly when tempo matters most. Diregraf Ghoul is a clean, real 2-power body for 1 mana — actual pressure, not more ramp. Verified Arena-legal: FDN 171, `brawl: legal`. |
| 4 | Incubation Druid `{1}{G}` 0/2 — taps for one mana of a type your lands make, triples if it has a +1/+1 counter, needs {3}{G}{G} to adapt | **Cast Down** `{B}` instant — "Destroy target nonlegendary creature." | A fine late-game mana filter but a do-nothing 0/2 body early, another redundant dork in a 20-dork pile. Cast Down is unconditional 1-mana removal for almost anything the single Arena opponent plays (nonlegendary covers the large majority of real threats). Verified Arena-legal: DOM 81, `brawl: legal`. |
| 5 | Fanatic of Rhonas `{1}{G}` 1/4 — taps for {G}, or {G}{G}{G}{G} only if you already control a 4-power creature (rarely true turns 1-3) | **Tragic Slip** `{B}` instant — "Target creature gets -1/-1 until end of turn. Morbid — ...-13/-13 instead if a creature died this turn." | Ferocious mode is dead in the exact window (early turns) where the deck needs action most. Tragic Slip is nominally weak but the deck already runs 10+ pieces of removal/sac-adjacent value that regularly kill something first — morbid is easy to enable, turning this into a 1-mana near-unconditional kill spell. Verified Arena-legal: SPG 22, `brawl: legal`. |

**New CMC histogram:** 1-drop count goes from 4 to **10** — an exact match to the EDHREC
average — while the bloated 2-drop slot drops from 23 to 18. Removal count rises from 11 to 14
(all 3 new pieces cost 1 mana, versus the old suite's 2-3 mana average), meaningfully cheaper on
average. Net creature count: 43 → 40 (two of the five adds, Deathrite Shaman and Diregraf Ghoul,
are creatures; the deck loses 5 weak dorks and gains 2 real bodies + 3 cheap removal spells).
Color identity check: Fatal Push, Diregraf Ghoul, Cast Down, and Tragic Slip are mono-B; Deathrite
Shaman is B/G hybrid — all legal inside Tyvar's B/G identity.

## Why the changes are stronger — the proof

**Turn-1 consistency roughly doubles.** With 4 of ~69 nonland cards live on turn 1, the odds of
having *any* play in a 7-card opening hand were low; at 10 of 69, a 1-drop (creature or cheap
removal) shows up in an opening hand far more often, and — critically — several of the new
1-drops (Fatal Push, Cast Down, Tragic Slip) are live on *any* turn, not just turn 1, so they're
never a dead draw the way a 5th or 6th redundant mana dork often was in the late game.

**Diregraf Ghoul and Deathrite Shaman start the clock a turn earlier than the dorks they
replaced.** A 2/2 for {B} on turn 1 is real pressure the old 2-mana 0/2 and 1/3 vanilla dorks
never provided — those bodies couldn't attack profitably into anything. Against a single 40-life
opponent, a turn-1 2-power creature is 4 extra unanswered combat damage by turn 3 alone if
unanswered.

**The cheap removal suite keeps the (still-intact) big-turn plan on schedule.** The deck's real
finishers — Craterhoof Behemoth, Zopandrel Hunger Dominus, Nyxbloom Ancient, Abomination of
Llanowar, Shaman of the Pack — are untouched by this pass. Fatal Push/Cast Down/Tragic Slip exist
to clear the single opponent's best blocker or racing threat for 1 mana instead of 2-3,
preserving tempo on the turns leading up to that payoff turn rather than trading a full turn's
mana for the same job the old, pricier removal suite (Doom Blade, Infernal Grasp, Murder, Hero's
Downfall, all 2-3 CMC) already did less efficiently.

## Optional upgrades not applied

- **Disfigure** (`{B}`, -2/-2) — verified Arena-legal (BRO 91) but strictly weaker than Tragic
  Slip's morbid upside in this deck (which regularly has something die before the removal spell
  is needed); left out as the redundant option among the three cheap removal candidates found in
  round 4.
- **A wider haste/protection package** was considered in an earlier (reverted) version of this
  upgrade and may still be worth revisiting separately — it targets a different weakness (board
  wipes / summoning sickness) than the curve/speed problem this pass focused on, and the deck
  owner can request that pass again independently if desired.
- **Bloodghast** — surfaced during research as an on-color recursive threat, but its Arena
  legality was never checked (it's a 2-mana card, `{B}{B}`, so it didn't fit the 1-drop slot this
  pass needed regardless) — would need verification before considering in a future pass.
