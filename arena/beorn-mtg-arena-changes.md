# Beorn the Fierce — MTG Arena build

New deck (no prior list to upgrade) — built from scratch for MTG Arena Brawl/Commander (1v1).

## Sources

- Commander oracle text + candidate oracle text/color identity: local `card_db.py` (Postgres
  cache of Scryfall `oracle-cards`)
- Competitive record: https://mtgtop8.com/format?f=cEDH — searched for "Beorn the Fierce"
- Archetype data: `edhrec-researcher` agent → https://edhrec.com/commanders/beorn-the-fierce
  (live, populated page despite the commander being 13 days old at build time — 3,946 decks
  already indexed) and the average decklist at that page
- Final printing/legality confirmation: `arena-legality-checker` agent (live Scryfall,
  cross-printing search) for all 70 candidates plus the commander

## Commander

**Beorn the Fierce** — {3}{G}{G}, Legendary Creature — Bear Shapeshifter Warrior, 6/6.
> Trample. Other Bears you control get +2/+2. At the beginning of combat on your turn, put a
> trample counter on up to one target creature you control. It becomes a Bear in addition to
> its other types. Then if you control three or more Bears, draw two cards.

HOB (2026-08-14), mythic. Mono-green.

- **cEDH presence: none.** Confirmed absent from mtgtop8's cEDH page — expected for a
  brand-new mono-color commander with no combo shell.
- **EDHREC**: 3,946 decks, rank #692. Bracket distribution skews low/mid-power (bracket 2/3 =
  485 of ~521 bracketed decks). Dominant themes: Bears (160 decks), +1/+1 Counters (91), Aggro
  (64), Ramp (62).

Axis: Beorn rewards a **wide, growing Bears board** two ways at once — the static +2/+2 anthem
on other Bears, and a combat-trigger engine that converts any one creature per turn into a Bear
(with a permanent trample counter), paying off with a two-card draw once three-plus Bears are
in play. The deck wants real Bear creatures for anthem density and turn-1 draw consistency,
*plus* generically strong green threats that become Bears (and start growing) over a few turns.

## Deck plan (63 nonland spells + 36 lands)

- **Ramp (9)**: Llanowar Elves, Elvish Mystic, Birds of Paradise, Rampant Growth, Cultivate,
  Arcane Signet, Wood Elves, Selvala Heart of the Wilds, Solemn Simulacrum — get to Beorn on
  curve (T4–5) and keep casting threats after.
- **Interaction (7)**: Beast Within (any permanent), Ram Through, Prizefight, Voracious Hydra,
  Kogla the Titan Ape (fight + artifact/enchantment hate), Chomping Changeling, Ugin the
  Ineffable — mono-green's classic weakness is unconditional removal, so this slice leans on
  fight effects (which scale with the deck's big creatures) plus Beast Within/Ugin for
  noncreature threats. **Ram Through is a direct oracle-text match for Beorn's plan**: "if the
  creature you control has trample, excess damage is dealt to that creature's controller
  instead" — every creature Beorn converts to a Bear picks up a permanent trample counter, so
  Ram Through becomes reach/removal-plus-damage on any converted attacker.
- **Card advantage (5)**: Beast Whisperer, Shamanic Revelation, Rishkar's Expertise, Toski
  Bearer of Secrets, Tireless Tracker.
- **Recursion (2)**: Eternal Witness, Regrowth.
- **Protection (3)**: Heroic Intervention, Veil of Summer, Tamiyo's Safekeeping — keep Beorn
  (and whatever it's grown) alive through a board wipe or removal spell in 1v1, where losing
  the commander is losing the whole engine for a turn.
- **Equipment/artifacts (5)**: Swiftfoot Boots, Shadowspear, The Great Henge (cost reduced by
  {X} = greatest power you control — with Beorn (6 power) in play this is regularly a 1–2 mana
  draw engine), Rhonas's Monument, Roaming Throne (choose Bear — **doubles Beorn's own combat
  trigger**, i.e. two trample-counter conversions and two 3-Bear draw checks per combat).
- **Non-Bear finishers (6)**: Elder Gargaroth, Craterhoof Behemoth, Vaultborn Tyrant, Rampaging
  Baloths, Titan of Industry, Vorinclex Voice of Hunger — top-end threats that become Bears
  (and thus +2/+2 bigger) the turn after they land, since Beorn's trigger targets any creature.
- **Bear tribal (19)**: Ayula Queen Among Bears (87.2% EDHREC inclusion, 0.857 synergy — highest
  synergy card on the whole page), Goreclaw Terror of Qal Sisma (90.3% inclusion), Beorn
  Reluctant Host, Lumra Bellow of the Woods, Surrak and Goreclaw, Owlbear, Professor of
  Zoomancy, Little Bear, Ordinary Bear, Gigantic Big Bear, Mother Bear, Grizzly Bears, Bear Cub,
  Studious First-Year, Vastlands Scavenger, The Earth King (ETB 4/4 Bear token), Radagast of
  Rhosgobel, Beorn's Hospitality, Dancing from Dark to Dawn — this slice both fills the anthem's
  "other Bears" clause and reliably hits the 3-Bear draw threshold without depending on the
  once-per-turn conversion trigger alone.
- **Consistency/utility (7)**: Nissa Who Shakes the World, Once Upon a Time, Explore, Inspiring
  Call, Snakeskin Veil, Ozolith the Shattered Spire (preserves trample/+1/+1 counters when a
  Bear dies and rebuilds them elsewhere), Vorinclex Monstrous Raider (doubles every counter you
  add — directly doubles Beorn's trample-counter output and every +1/+1 counter in the deck).
- **Lands (36)**: 29 Forest + Argoth Sanctum of Nature (repeatable 2/2 Bear token maker —
  {2}{G}{G}, {T}: create a Bear, direct support for the 3-Bear draw threshold), Three Tree City
  (choose Bear), Castle Garenbrig, Rogue's Passage (evasion for a huge trampler when a single
  blocker can still eat it), Boseiju Who Endures (modal land/removal), Nykthos Shrine to Nyx
  (heavy green-devotion ramp), Reliquary Tower.

## Arena-legality notes

Every one of the 70 candidates plus the commander was checked against **all** Arena printings
(not just whichever printing the local DB caches), per the project's known false-negative trap.
A large fraction only clear Arena via an older or Arena-exclusive printing even though a newer
paper-only printing exists — e.g. **Birds of Paradise** (BLC, not the default MSC), **Cultivate**
(M21, not MSC), **Arcane Signet** (ELD, not MSC), **Ram Through** (IKO, not CMM), **Ugin, the
Ineffable** (WAR, not CMM), **The Great Henge** (ELD, not CMM), **Rhonas's Monument** (AKR —
Arena-exclusive; the paper GNT printing doesn't count), **Ayula, Queen Among Bears** (J21 —
Arena-exclusive), **Mother Bear** and **Grizzly Bears** (both J21 — Arena-exclusive), **Nykthos,
Shrine to Nyx** (EA2 — Arena-exclusive), **Eternal Witness** (AA2 — Arena-exclusive). The
collector numbers in the `.txt` are the verified Arena-legal ones, not Scryfall's default.

One card was cut mid-build for exactly this kind of check, but by **oracle text** rather than
Arena availability: **Farseek** was an early ramp candidate, but its actual text is "Search your
library for a Plains, Island, Swamp, or Mountain card" — it cannot fetch a Forest and would be a
dead card in a mono-green deck. Replaced with **Solemn Simulacrum** (fetches *any* basic land,
plus draws a card on death).

No card was found to be banned in Arena's Brawl/Commander format; nothing was cut for that
reason this pass.

## Card count

100 cards total (1 commander + 99 main deck: 63 nonland spells + 36 lands), verified with
`awk 'NF{for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/){n+=$i; break}}END{print n}' arena/beorn-mtg-arena.txt`.
