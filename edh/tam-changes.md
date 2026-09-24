# Tam, the Possibility — build cEDH Superfriends do zero (setembro 2026)

Este é um deck novo de 100 cartas, não um upgrade de uma lista existente — construído do zero
seguindo a metodologia do projeto (mtgtop8 cEDH primeiro, depois EDHREC, depois verificação de
oracle text carta a carta antes de qualquer decisão).

## Comandante verificado

**Tam, the Possibility** — {1}{G}{U}, Legendary Creature — Gorgon Wizard, 2/4, identidade de cor
**W/U/B/R/G (cinco cores)**:
> Planeswalker spells you cast cost {1} less to cast.
> {W}{U}{B}{R}{G}, {T}: Proliferate X times, where X is the number of planeswalker types among
> planeswalkers you control.

Tradução funcional: todo planeswalker que você conjura custa {1} a menos (só reduz o genérico —
ver nota sobre Wrenn and Six abaixo); e por {W}{U}{B}{R}{G} e T você proliferata X vezes, onde X é
o número de *tipos* de planeswalker (não de permanentes) que você controla — cada planeswalker
diferente conta um tipo, então com 3+ tipos distintos em campo essa ativação sozinha já proliferata
múltiplas vezes.

**Nota sobre legalidade**: o set Reality Fractured (FRA) — onde Tam foi impressa (`fra` #276) —
lança em **2026-10-02**. Hoje (24/09/2026) a carta ainda não foi lançada, por isso o banco de dados
local retorna `"commander": "not_legal"` para Tam **e também para Sanctum Lurker e Loyal Tutor**
(ambas do mesmo set, ainda não lançado) — isso é esperado e não é um problema de legalidade real,
é só o gate de "carta ainda não existe oficialmente". As três já aparecem como `"future": "legal"`
no banco. Este deck é montado para o dia do lançamento.

## Fontes de dados

- **mtgtop8 cEDH** (https://mtgtop8.com/format?f=cEDH) — consultado primeiro, por convenção do
  projeto. Tam está ausente (carta de pré-lançamento) e **não existe arquétipo planeswalker/
  superfriends** entre os 953 arquétipos / 35.890 decks catalogados no metagame cEDH atual. Isso
  significa que não há lista de torneio para copiar — o shell precisou ser inferido a partir do
  que *funciona* em cEDH 5 cores hoje. Os comandantes 5 cores mais presentes no formato são Sisay,
  Voice of Many (42,6‰ dos decks), Najeela, the Blade-Blossom (12,3‰) e Kenrith, the Returned King
  (11,8‰) — todos vencem por combo rápido + tutores densos, não por atrito longo. Essa é a base de
  design deste deck: um shell cEDH genérico (fast mana, tutores, contra-mágica grátis) carregando
  um pacote de planeswalkers, em vez de um deck "superfriends" tradicional.
- **EDHREC — página da Tam** (https://json.edhrec.com/pages/commanders/tam-the-possibility.json):
  1.309 decks cadastrados, dos quais só **2 marcados como cEDH** — confirma que a base de jogadores
  de Tam é quase inteiramente casual. Média da comunidade: ~37 terrenos, ~22 planeswalkers, ~13
  criaturas — um perfil lento e "superfriends de verdade", que este build deliberadamente não
  segue (ver "Filosofia de design" abaixo). Sinergia alta reportada: Oath of Teferi 84,0%/0,815,
  The Chain Veil 68,9%/0,675, Teferi, Temporal Archmage 55,2%/0,541, Oko, Thief of Crowns
  54,6%/0,525, Narset, Parter of Veils 37,7%/0,363, Teferi, Time Raveler 34,8%/0,318, Chandra,
  Torch of Defiance 43,2%/0,425, Sanctum Lurker 71,0%/0,653, Loyal Tutor 59,0%/0,560, Interplanar
  Beacon 57,6%/0,567, Birds of Paradise 52,2%, Delighted Halfling 33,5%, Sol Ring 82,8%, Arcane
  Signet 80,7%, Mox Amber 13,1%. Peças de "game changer" de cEDH têm adoção baixa na base atual de
  Tam — Fierce Guardianship 13,5%, Demonic Tutor 10,8%, Vampiric Tutor 7,6%, Rhystic Study 14,8%,
  Smothering Tithe 15,1%, Ancient Tomb 6,6%, Cyclonic Rift 16,3% — sinal de que a comunidade ainda
  não monta Tam como deck competitivo, o que reforça a necessidade de montar este shell do zero em
  vez de copiar a lista média.
- **EDHREC — deck médio "planeswalkers caros"**
  (https://edhrec.com/average-decks/tam-the-possibility/planeswalkers/expensive) — usado como
  checklist de staples de alto custo que a comunidade já reconhece com a Tam: Chrome Mox, Mox
  Diamond, Mox Amber, Sol Ring, Arcane Signet, The Chain Veil, Oath of Teferi, Rhystic Study,
  Smothering Tithe, Fierce Guardianship, Swan Song, Deflecting Swat, Enlightened Tutor, Vampiric
  Tutor, Demonic Tutor, Loyal Tutor, Teferi's Protection, Swords to Plowshares, Sanctum Lurker,
  Delighted Halfling, Birds of Paradise, Jace, the Mind Sculptor, Narset, Parter of Veils, Oko,
  Thief of Crowns, Teferi, Time Raveler, Teferi, Temporal Archmage, Chandra, Torch of Defiance, as
  dual lands originais (ABUR), fetchlands, Ancient Tomb, City of Brass, Mana Confluence, Otawara,
  Soaring City e Boseiju, Who Endures. Praticamente todo esse pacote foi incorporado à lista final.
- **Atraxa, Praetors' Voice — página "planeswalkers"**
  (https://json.edhrec.com/pages/commanders/atraxa-praetors-voice/planeswalkers.json — não existe
  slug "superfriends" separado) usada como comparação secundária de que cartas de proliferate/
  superfriends o formato já valida em outro comandante 4 cores de referência.
- **Commander Spellbook** — IDs de combo conferidos: 787-1124 (The Chain Veil + Teferi, Temporal
  Archmage), 1124-2495-2858-4074 (The Chain Veil + Chandra, Torch of Defiance, análogo de dano
  infinito), 142-2781 (Saheeli Rai + Felidar Guardian), 742-1295 (Thassa's Oracle + Demonic
  Consultation), 1295-3093 (Thassa's Oracle + Tainted Pact), 4821-5261 (Isochron Scepter +
  Dramatic Reversal).

## Filosofia de design

As listas médias do EDHREC para Tam são superfriends casual: ~22 planeswalkers, muitos deles
caros e lentos, jogando para "chegar ao ultimate" em turnos tardios de mesa multiplayer relaxada.
Esse não é o objetivo aqui. Este build trata a Tam como **motor de custo reduzido + proliferate em
massa** dentro de um shell cEDH: fast mana pesado, tutores densos, contra-mágica gratuita, e um
pacote enxuto de **14 planeswalkers** escolhidos por baixo custo de mana (a maioria vira MV 2–3
com o desconto da Tam — ver seção de curva), efeito de stax/valor imediato, ou papel direto em uma
das quatro linhas de vitória. Isso significa cortar deliberadamente peças de altíssima sinergia
segundo o EDHREC porque elas são lentas ou não têm impacto instantâneo:

- **Doubling Season** ({4}{G}, Enchantment: dobra tokens e contadores) — 5 mana, não protege o
  turno de combo, não gera velocidade; é um multiplicador passivo de valor, exatamente o perfil
  "superfriends longo" que este deck evita.
- **Ichormoon Gauntlet** ({2}{U}, Artifact: dá a planeswalkers "[0]: Proliferate" e "[−12]: extra
  turn", e duplica contadores ao conjurar mágicas não-criatura) — sinergicamente forte com
  proliferate, mas é uma terceira peça de suporte (depois de Tam e Oath) num slot que preferimos
  gastar com tutor ou interação; a Tam já fornece proliferate em massa sem depender dele.
- **Commodore Guff** ({1}{U}{R}{W}, Legendary Planeswalker, pode ser comandante) — só é
  realmente forte como comandante alternativo (ganha lealdade em outro planeswalker todo end
  step); como carta solta no 99 não tem impacto imediato e compete de cor com o restante do plano.
- **Nicol Bolas, Dragon-God** ({U}{B}{B}{B}{R}, 5 mana, pips pesados) — poderoso mas lento; não
  interage com nenhuma das quatro linhas de vitória e é o tipo de bomba de meio de jogo que cEDH
  não tem tempo de esperar.
- **Deepglow Skate** ({4}{U}, criatura, dobra contadores ao entrar) — efeito único (não repetível),
  5 mana, sem proteção; dobra lealdade uma vez e morre para qualquer remoção antes de agir de novo.
- **Carth the Lion** ({2}{B}{G}) — na verdade **atrapalha o motor principal do deck**: seu oracle
  text diz "Planeswalkers' loyalty abilities you activate cost an additional [+1] to activate",
  ou seja, cada ativação de habilidade de lealdade (incluindo a nossa própria com The Chain Veil)
  fica mais cara em lealdade. Isso é diretamente anti-sinérgico com a linha de vitória 2.
- **Ugin, the Spirit Dragon** ({8}, incolor) — 8 mana é inviável para o plano de curva baixa deste
  deck; é uma carta de "boa em qualquer deck genérico", não uma peça deste plano específico.

## Linhas de vitória

Todas conferidas por oracle text (`combo-cards.txt` / consultas ao `card_db.py`).

### 1. Thassa's Oracle + Demonic Consultation / Tainted Pact
`Thassa's Oracle` ({U}{U}): ao entrar, olhe X cartas do topo (X = devoção a azul); se X ≥ cartas
restantes na biblioteca, **você vence o jogo**. `Demonic Consultation` ({B}): escolha um nome,
exile as 6 cartas do topo, revele até achar o nome escolhido; escolhendo um nome que não está no
deck, exila a biblioteca inteira. `Tainted Pact` ({1}{B}): mesmo efeito, mas sem escolher nome —
exila cartas do topo até repetir um nome ou você pôr uma na mão. Com biblioteca vazia (ou quase),
Thassa's Oracle vence de cara, independente do estado do board.

### 2. The Chain Veil + Teferi, Temporal Archmage + Oath of Teferi
`The Chain Veil` ({4}, Legendary Artifact): "{4}, {T}: para cada planeswalker que você controla,
você pode ativar uma de suas habilidades de lealdade uma vez neste turno, como se nenhuma delas
tivesse sido ativada." `Teferi, Temporal Archmage` ({4}{U}{U} → {3}{U}{U} com a Tam): +1 olha as
2 do topo e guarda 1; −1 desvira até 4 permanentes-alvo. `Oath of Teferi` ({3}{W}{U}): "Você pode
ativar as habilidades de lealdade de planeswalkers que controla **duas vezes** por turno, em vez
de só uma." Com Oath em campo: ative Teferi +1 (sobe 1, ganha carta), depois −1 (desce 1, desvira
até 4 permanentes) — líquido de lealdade **zero**. O −1 desvira a própria Chain Veil mais até 3
permanentes que produzem mana (ex.: Ancient Tomb + Sol Ring + 1 terreno, ou Grim Monolith + 2
terrenos, gerando {4}+); pague {4} para reativar a Chain Veil, repita: mana infinita, cartas
infinitas via Teferi +1, e uma ativação extra de lealdade **para cada outro planeswalker** em
campo a cada ciclo (via Chain Veil). Fechamento: Chandra, Torch of Defiance +1 (se não conjurar a
carta exilada, 2 de dano a cada oponente), Saheeli Rai +1 (1 de dano a cada oponente), ou o "[+2]"
que Sanctum Lurker concede a todo planeswalker (1 de dano a cada oponente, ganha 1 de vida) —
qualquer um deles, ativado em loop, dizima a mesa. **Nota**: o Commander Spellbook lista Chain
Veil + Teferi, Temporal Archmage como infinito sozinho, mas pelo oracle text, sem Oath (ou sem a
Tam recarregando lealdade via proliferate), cada ciclo custa 1 de lealdade líquida em Teferi (+1
depois −1 = 0 lealdade líquida na verdade — o oracle text bate certo mesmo sem Oath: +1 soma 1,
−1 subtrai 1, dá zero). Ainda assim, tratamos Oath (ou a própria Tam proliferando lealdade) como a
terceira peça confiável, porque o loop sozinho não fecha o jogo sem Oath permitir as duas
ativações no mesmo turno antes do fim da fase de combate/main.

### 3. Saheeli Rai + Felidar Guardian
`Saheeli Rai` ({1}{U}{R} → {U}{R} com a Tam): "−2: crie um token cópia de um artefato ou criatura
alvo que você controla, além de artefato; ganha haste; exile no fim do turno." `Felidar Guardian`
({3}{W}): "ao entrar, você pode exilar outro permanente alvo que controla, depois devolvê-lo ao
campo." Copie Felidar Guardian com Saheeli −2 → a cópia entra, seu ETB reseta a própria Saheeli
(exila e devolve) → Saheeli volta com lealdade cheia, ative −2 de novo → loop de tokens hasty de
Felidar Guardian (1/4) infinitos. Ataque com o exército de 1/4 com haste para o dano.

### 4. Isochron Scepter + Dramatic Reversal + mana rocks/dorks
`Isochron Scepter` ({2}): imprint uma instant de MV ≤2 ao entrar; "{2}, {T}: copie a carta
imprintada e pode conjurar a cópia sem pagar o custo de mana." `Dramatic Reversal` ({1}{U}, MV2):
"desvire todos os permanentes não-terreno que você controla." Imprint Dramatic Reversal no Scepter.
Com mana rocks/dorks somando ≥3 de mana não-terrestre em campo (Birds of Paradise, Noble Hierarch,
Arcane Signet, Mox Amber, Sol Ring, etc. — coloridos o bastante para pagar o {2} do Scepter e
sobrar), ative o Scepter (copia e conjura Dramatic Reversal de graça) → desvira tudo, incluindo o
próprio Scepter e os rocks → mana infinita colorida. Esse mesmo loop desvira **a Tam** (mana
infinita alimenta ativações repetidas de {W}{U}{B}{R}{G}, T da Tam) → proliferate infinito → todo
planeswalker sobe até a faixa de ultimate; Chandra, Torch of Defiance −7 dá o emblema "sempre que
você conjurar uma mágica, este emblema causa 5 de dano a qualquer alvo" — cada cópia do Dramatic
Reversal conjurada pelo Scepter conta como conjurar uma mágica → 5 de dano por ativação → vitória.
O mesmo loop também desvira **The Chain Veil**, dando ativações infinitas dela (e, portanto, de
Chandra +1 repetidamente) mesmo sem Teferi/Oath em campo.

## Curva de mana com o desconto da Tam

A redução da Tam só afeta mana **genérica** — custos sem símbolo genérico (como Wrenn and Six)
não mudam. Custos conferidos via `card_db.py`:

| Planeswalker | Custo impresso | Custo com Tam | MV final |
|---|---|---|---|
| Wrenn and Six | {R}{G} | {R}{G} (sem genérico — **sem redução**) | 2 |
| Dack Fayden | {1}{U}{R} | {U}{R} | 2 |
| Grist, the Hunger Tide | {1}{B}{G} | {B}{G} | 2 |
| Narset, Parter of Veils | {1}{U}{U} | {U}{U} | 2 |
| Oko, Thief of Crowns | {1}{G}{U} | {G}{U} | 2 |
| Saheeli Rai | {1}{U}{R} | {U}{R} | 2 |
| Teferi, Time Raveler | {1}{W}{U} | {W}{U} | 2 |
| Karn, the Great Creator | {4} | {3} | 3 |
| Jace, the Mind Sculptor | {2}{U}{U} | {1}{U}{U} | 3 |
| Jace, Wielder of Mysteries | {1}{U}{U}{U} | {U}{U}{U} | 3 |
| Chandra, Torch of Defiance | {2}{R}{R} | {1}{R}{R} | 3 |
| The Wandering Emperor | {2}{W}{W} | {1}{W}{W} | 3 |
| Tezzeret the Seeker | {3}{U}{U} | {2}{U}{U} | 4 |
| Teferi, Temporal Archmage | {4}{U}{U} | {3}{U}{U} | 5 |

## Últimos ajustes em relação ao primeiro rascunho

- **Mindbreak Trap, Arcane Denial → Isochron Scepter, Dramatic Reversal**: as duas contra-mágicas
  saíram para abrir espaço para a **4ª linha de vitória**, que também sinergiza diretamente com o
  motor da Tam (o loop desvira a própria Tam, multiplicando as ativações de proliferate).
- **Exotic Orchard, Gemstone Caverns → Otawara, Soaring City, Boseiju, Who Endures**: troca de
  terrenos de fixação pura por terrenos que também são interação (bounce e destruição via
  channel) sem custar um slot de spell; ambos aparecem na lista média "planeswalkers caros" do
  EDHREC para a Tam.
- **Liliana of the Veil → Smothering Tithe**: Liliana força descarte simétrico ("each player
  discards a card") — em um deck que depende de seu próprio grip de tutores e peças de combo,
  isso corta a própria mão tanto quanto a dos oponentes. Smothering Tithe é rampa assimétrica em
  mesa multiplayer (só os oponentes pagam ou geram Treasure para você) e já é staple reconhecido
  na lista média cara do EDHREC.

## Checagem de legalidade

- **100 cartas**, incluindo a comandante (`awk 'NF{n+=$1}END{print n}' edh/tam.txt` = 100).
- Sem duplicatas (uma cópia de cada carta, exceto terrenos básicos — não há básicos nesta lista,
  apenas terrenos utilitários e não-básicos únicos).
- Sem cartas banidas em Commander confirmadas via `card_db.py` (Oko, Thief of Crowns está banido
  em outros formatos como Legacy/Modern/Standard Brawl, mas `"commander": "legal"`).
- Todas as 100 cartas têm identidade de cor dentro de W/U/B/R/G — a própria Tam já é 5 cores, então
  qualquer carta mono ou multicolor nesses cinco pips é válida.
