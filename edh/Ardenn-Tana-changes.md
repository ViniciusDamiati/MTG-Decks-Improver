# Ardenn / Tana — Change Log

Commanders: Ardenn, Intrepid Archaeologist (W) + Tana, the Bloodsower (R/G) — Naya identity.
Format: paper Commander (cEDH/high-power EDH), equipment-Voltron/tokens shell.

## Data baseline (EDHREC, combined partner page, 936 decks)
- Archetype tags: Equipment (190 decks), Voltron (65), Tokens (46), Aggro (29).
- mtgtop8 cEDH check for this pair was attempted but the site was unreachable from the research
  environment; based on EDHREC's popularity rank (#1,650 overall) there's no indication of a
  cEDH presence, but this is inferential, not a confirmed mtgtop8 result.

## Swaps (6 out / 6 in, net 0 — deck stays at 100)

### 1. Bone Sabres → Skullclamp
- **Bone Sabres** ({2}{G}, Equip {3}): only grows the equipped creature by +4/+4 on attack — no
  value if the creature dies first, and does nothing off combat.
- **Skullclamp** ({1}, Equip {1}): +1/-1 and draw two cards whenever the equipped creature dies.
  EDHREC: **69.8% inclusion / 0.544 synergy** on the combined page — the 2nd-highest synergy
  card in the entire dataset for this pair. Combos directly with Tana's Saproling tokens
  (cheap, expendable equip targets) for repeatable card draw.

### 2. Cloak of the Bat → Helm of the Host
- **Cloak of the Bat** ({2}, Equip {2}): flying + haste only. Zero appearances anywhere in
  EDHREC's data for this commander pair (combined or either solo page) — no signal of play.
- **Helm of the Host** ({4}, Equip {5}): creates a hasty, non-legendary token copy of the
  equipped creature each combat. EDHREC: **36.6% inclusion / 0.330 synergy**. Doubles your
  Voltron threat or your token engine every turn it survives.

### 3. Danitha Capashen, Paragon → Mjölnir, Hammer of Thor
- **Danitha Capashen, Paragon** ({2}{W}): first strike/vigilance/lifelink 2/2, reduces Aura/
  Equipment casting cost by {1}. Real card (26.4% combined / 54.4% synergy in solo-Ardenn data)
  but its value (cost reduction) is redundant with Puresteel Paladin already in the list, and
  it does nothing once resolved beyond a small body.
- **Mjölnir, Hammer of Thor** ({3}{R}, Equip worthy {1}): ETB deals 4 damage to a creature
  (real removal), and doubles all combat damage dealt by the equipped creature — stacks with
  the deck's existing Sword suite and Colossus Hammer for lethal swings. Red is already in the
  Tana half of the identity, so no color-identity issue.

### 4. Heavenly Blademaster → Hulkbuster Armor
- **Heavenly Blademaster** ({5}{W}): needs Auras/Equipment already in hand/on resolution to be
  worth it — zero appearances in EDHREC data for this pair, essentially unplayed.
- **Hulkbuster Armor** ({4}, Equip {6}, or Equip Hero {3} — the reduced cost is dead text here,
  the deck runs no Hero creatures): sets equipped creature to 9/9 flying. Explicitly kept in the
  deck at the user's request even though its floor is weak without Ardenn online — Ardenn's
  "attach any number of Auras/Equipment at the beginning of combat for free" ability bypasses
  the {6} equip tax, turning this into a free 9/9 flyer whenever Ardenn resolves and survives.

### 5. The Aetherspark → Orcrist, Goblin-cleaver
- **The Aetherspark** ({4}): slow planeswalker/equipment hybrid — needs several combat steps of
  loyalty growth before its abilities matter, no immediate combat impact.
- **Orcrist, Goblin-cleaver** ({3}, Equip {3}): +2/+2 trample, and creates a Treasure per
  creature of a chosen type whenever the equipped creature connects — immediate stats plus
  ramp/fixing the turn it lands.

### 6. Thran Power Suit → Swordsman's Steel
- **Thran Power Suit** ({2}, Equip {2}): +1/+1 per Aura/Equipment attached and ward {2}.
  Real card (27.5% / 0.264 synergy) but its protection is redundant with Mithril Coat, Robe of
  Stars, and Silver Shroud Costume already in the 99.
- **Swordsman's Steel** ({4}, Equip {3}): draws a card for each Equipment you control on ETB,
  and gives +2/+2 per Equipment controlled. With ~20 equipment pieces in this list, this can
  refill the hand by several cards the turn it resolves — the deck's best pure card-advantage
  equipment.

## Net effect
The list keeps its strongest existing pieces (Colossus Hammer, Puresteel Paladin, Sram, Belt of
Giant Strength, Masterwork of Ingenuity, Nazgûl Battle-Mace, etc.) untouched and replaces its
lowest-signal cards with EDHREC-verified high-synergy staples (Skullclamp, Helm of the Host) plus
three high-power, verified-text additions from recent sets (Mjölnir, Orcrist, Swordsman's Steel)
that fit the Ardenn free-attach / Tana token-and-damage plan. Hulkbuster Armor is the one
speculative include, kept at the user's explicit call — it's live only while Ardenn is on board,
so it's worth reassessing if it underperforms in play.

Card count verified at 100 (86 singleton lines + Forest x4 + Mountain x2 + Plains x6 + 2
commanders) after all edits.
