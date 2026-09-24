# Tam, the Possibility — "Superfriends" (versão 2, casual de alto poder)

Esta é a **segunda versão** do deck de Tam, the Possibility: uma companheira mais relaxada da
lista cEDH (`edh/tam.txt`). O objetivo aqui não é o combo mais rápido da mesa — é rodar o maior
número possível de planeswalkers ao mesmo tempo, empilhar motores de lealdade/proliferate e
fechar o jogo com ultimates (principalmente o −8 de Nicol Bolas, Dragon-God) em vez de uma linha
de combo de dois cards. Sem teto de orçamento.

**Contagem de tipos:** 24 planeswalkers, 10 criaturas (fora o comandante), 37 terrenos, 1
comandante (criatura) e 28 mágicas não-terreno/não-planeswalker (artefatos, encantamentos,
instantâneos, feitiços) = **100 cards exatos**.

Todo texto de oráculo citado abaixo foi verificado via `python .claude/scripts/card_db.py`
(banco local, dump da Scryfall) antes de ser usado nesta análise — nenhuma descrição vem de
memória.

## Fontes de dados

- **EDHREC — página do comandante**: https://edhrec.com/commanders/tam-the-possibility
  (1.309 decks registrados; médias da categoria: **37 terrenos / 22 planeswalkers / 13
  criaturas**).
- **EDHREC — lista média, categoria planeswalkers "expensive"**:
  https://edhrec.com/average-decks/tam-the-possibility/planeswalkers/expensive — **referência
  principal**; esta lista segue essa distribuição de perto (24 walkers em vez dos ~22 de média,
  compensando com poucas criaturas — 10 em vez de 13 — já que o motor não depende de bordo largo
  de criaturas).
- **mtgtop8 cEDH** (`https://mtgtop8.com/format?f=cEDH`): Tam, the Possibility ainda não tem
  presença registrada lá (carta nova, ainda não impressa — ver seção de legalidade). Achado
  registrado conforme exigido pela metodologia do projeto.
- **Números de sinergia/inclusão (EDHREC, % inclusão / score de sinergia)** usados para validar
  cada peça abaixo:

| Carta | Inclusão | Sinergia |
|---|---|---|
| Oath of Teferi | 84,0% | 0,815 |
| Commodore Guff | 76,9% | 0,758 |
| Ichormoon Gauntlet | 75,6% | 0,742 |
| Sanctum Lurker | 71,0% | 0,653 |
| Vraska, Betrayal's Sting | 71,1% | 0,696 |
| Nicol Bolas, Dragon-God | 70,5% | 0,672 |
| The Chain Veil | 68,9% | 0,675 |
| Tamiyo, Field Researcher | 66,9% | 0,654 |
| The Theorist, Jace Beleren | 64,7% | 0,634 |
| Wrenn and Realmbreaker | 59,1% | 0,570 |
| Loyal Tutor | 59,0% | 0,560 |
| Interplanar Beacon | 57,6% | 0,567 |
| Farseek | 54,6% | — |
| Chromatic Lantern | 55,2% | — |
| Flux Channeler | 55,7% | 0,544 |
| Teferi, Temporal Archmage | 55,2% | 0,541 |
| Oko, Thief of Crowns | 54,6% | 0,525 |
| Doubling Season | 53,2% | 0,470 |
| Chandra, Legacy of Fire | 52,6% | 0,520 |
| Ripples of Potential | 49,4% | 0,480 |
| Elspeth, Sun's Champion | 50,8% | 0,495 |
| Tekuthal, Inquiry Dominus | 48,9% | 0,479 |
| Bloom Tender | 48,8% | — |
| Onakke Oathkeeper | 46,7% | 0,462 |
| Deepglow Skate | 44,8% | 0,435 |
| Atraxa, Praetors' Voice | 44,5% | 0,417 |
| Karn's Bastion | 43,7% | 0,402 |
| Teferi, Master of Time | 46,3% | 0,453 |
| Nature's Lore | 43,2% | — |
| Chandra, Chill of Compliance | 43,4% | 0,430 |
| Chandra, Torch of Defiance | 43,2% | 0,425 |
| Ugin, the Spirit Dragon | 41,9% | 0,393 |
| Spark Double | 39,5% | 0,372 |
| Swords to Plowshares | 45,6% | — |
| Brokers Ascendancy | 37,0% | 0,356 |
| Liliana, Dreadhorde General | 36,8% | 0,359 |
| Teferi, Time Raveler | 34,8% | 0,318 |
| Teferi, Hero of Dominaria | 31,9% | 0,309 |
| Elspeth, Storm Slayer | 31,6% | 0,301 |
| Counterspell | 26,2% | — |
| Farewell | 18,9% | — |
| Cyclonic Rift | 16,3% | — |

## Motores-chave (texto de oráculo verificado)

- **Tam, the Possibility** — `{1}{G}{U}`, criatura 2/4. "Planeswalker spells you cast cost {1}
  less to cast. {W}{U}{B}{R}{G}, {T}: Proliferate X times, where X is the number of planeswalker
  types among planeswalkers you control." O desconto reduz **apenas o custo genérico** de cada
  planeswalker (nunca os símbolos coloridos — ver tabela abaixo). A habilidade ativada custa as
  cinco cores e faz Tam ter identidade de cor **WUBRG**, então qualquer carta pode entrar no
  deck. Com todos os 24 planeswalkers em jogo ao mesmo tempo (cenário teórico) há **15 tipos de
  planeswalker distintos** na lista — Bolas, Chandra, Elspeth, Grist, Guff, Jace, Karn, Liliana,
  Narset, Oko, Tamiyo, Teferi, Ugin, Vraska, Wrenn (The Wandering Emperor não tem subtipo de
  planeswalker e não conta) — ou seja, um único clique da Tam pode proliferar até 15 vezes.

- **Nicol Bolas, Dragon-God** — `{U}{B}{B}{B}{R}`. "Nicol Bolas has all loyalty abilities of all
  other planeswalkers on the battlefield. +1: You draw a card. Each opponent exiles a card from
  their hand or a permanent they control. −3: Destroy target creature or planeswalker. −8: Each
  opponent who doesn't control a legendary creature or planeswalker loses the game." Isso vale
  para **qualquer** planeswalker na mesa, incluindo os dos oponentes — se um adversário resolver
  um planeswalker, Bolas ganha acesso às habilidades dele também (ex.: o −12 de Jace, the Mind
  Sculptor de um oponente vira algo que Bolas também pode ativar). É o principal vencedor de
  jogo do deck (−8).

- **Ichormoon Gauntlet** — `{2}{U}`. "Planeswalkers you control have '[0]: Proliferate' and
  '[−12]: Take an extra turn after this one.'" Dá a **todo** planeswalker controlado uma
  proliferação gratuita e um extra-turn latente em −12 — com Doubling Season/Tekuthal isso
  acelera loyalty muito rápido.

- **Oath of Teferi + The Chain Veil** — Oath of Teferi (`{3}{W}{U}`): "You may activate the
  loyalty abilities of planeswalkers you control twice each turn rather than only once." The
  Chain Veil (`{4}`): "{4}, {T}: For each planeswalker you control, you may activate one of its
  loyalty abilities once this turn as though none of its loyalty abilities have been activated
  this turn." Juntas, cada planeswalker pode ativar **três** vezes no turno (a ativação normal +
  a segunda de Oath + a "reset" do Chain Veil, que por sua vez também é liberada pela segunda
  ativação de Oath). **A única combinação realmente infinita que sobrou da versão competitiva**:
  Teferi, Temporal Archmage (+1: filtra) + The Chain Veil + Oath of Teferi permite pagar {4} pelo
  Chain Veil e resetar as ativações de Teferi indefinidamente enquanto houver mana — nesta versão
  ela existe como **plano B latente**, não como o plano principal (não há fast mana dedicada para
  viabilizá-la turno 1 como na lista cEDH).

- **Crescimento de lealdade em massa** — **Doubling Season** ("If an effect would put one or
  more counters on a permanent you control, it puts twice that many... instead" — cobre counters
  de lealdade também) + **Deepglow Skate** (ETB: "double the number of each kind of counter on
  any number of target permanents") + **Tekuthal, Inquiry Dominus** ("If you would proliferate,
  proliferate twice instead") + **Flux Channeler** ("Whenever you cast a noncreature spell,
  proliferate") + **Atraxa, Praetors' Voice** ("At the beginning of your end step, proliferate")
  + **Brokers Ascendancy** ("At the beginning of your end step, put a +1/+1 counter on each
  creature you control and a loyalty counter on each planeswalker you control") + **Commodore
  Guff** ("At the beginning of your end step, put a loyalty counter on another target
  planeswalker you control") formam uma rede de gatilhos de fim de turno/proliferate que empurra
  todo planeswalker em direção ao ultimate muito mais rápido do que só usando +1s.

- **Sanctum Lurker** — `{2}{B}`. "Planeswalkers you control aren't put into their owners'
  graveyards for having 0 loyalty. Planeswalkers you control have '[+2]: This planeswalker deals
  1 damage to each opponent and you gain 1 life.'" Efetivamente torna qualquer planeswalker
  imortal a 0 lealdade e dá a todos um dreno passivo — segura ultimates lentos vivos até serem
  ativados.

- **Proteção do bordo de planeswalkers** — **Onakke Oathkeeper** ("Creatures can't attack
  planeswalkers you control unless their controller pays {1} for each creature... attacking a
  planeswalker you control" + recursão de `{4}{W}{W}` do cemitério), **Teferi's Protection**
  ("your life total can't change and you gain protection from everything. All permanents you
  control phase out"), **The Wandering Emperor** (flash + `−2: Exile target tapped creature`) e
  **Elspeth, Sun's Champion**/**Elspeth, Storm Slayer** (fazem bloqueadores/token walls) são a
  rede de defesa que substitui as contra-mágicas gratuitas da versão cEDH.

## Tabela de custo de mana (após o desconto de Tam, só no genérico)

| Planeswalker | Custo impresso | Custo com Tam |
|---|---|---|
| Nicol Bolas, Dragon-God | {U}{B}{B}{B}{R} | {U}{B}{B}{B}{R} (sem genérico) |
| Wrenn and Six | {R}{G} | {R}{G} (sem genérico) |
| Grist, the Hunger Tide | {1}{B}{G} | {B}{G} |
| Teferi, Time Raveler | {1}{W}{U} | {W}{U} |
| Oko, Thief of Crowns | {1}{G}{U} | {G}{U} |
| Wrenn and Realmbreaker | {1}{G}{G} | {G}{G} |
| Narset, Parter of Veils | {1}{U}{U} | {U}{U} |
| Chandra, Chill of Compliance | {1}{U}{U} | {U}{U} |
| Commodore Guff | {1}{U}{R}{W} | {U}{R}{W} |
| Tamiyo, Field Researcher | {1}{G}{W}{U} | {G}{W}{U} |
| Jace, the Mind Sculptor | {2}{U}{U} | {1}{U}{U} |
| Teferi, Master of Time | {2}{U}{U} | {1}{U}{U} |
| The Theorist, Jace Beleren | {2}{U}{U} | {1}{U}{U} |
| The Wandering Emperor | {2}{W}{W} | {1}{W}{W} |
| Chandra, Torch of Defiance | {2}{R}{R} | {1}{R}{R} |
| Karn, the Great Creator | {4} | {3} |
| Teferi, Hero of Dominaria | {3}{W}{U} | {2}{W}{U} |
| Elspeth, Storm Slayer | {3}{W}{W} | {2}{W}{W} |
| Chandra, Legacy of Fire | {4}{R} | {3}{R} |
| Elspeth, Sun's Champion | {4}{W}{W} | {3}{W}{W} |
| Liliana, Dreadhorde General | {4}{B}{B} | {3}{B}{B} |
| Vraska, Betrayal's Sting | {4}{B}{B/P} | {3}{B}{B/P} |
| Teferi, Temporal Archmage | {4}{U}{U} | {3}{U}{U} |
| Ugin, the Spirit Dragon | {8} | {7} |

## Lista completa por categoria

**Planeswalkers (24)** — Chandra, Chill of Compliance (controle/filtro); Chandra, Legacy of Fire
(dano em massa passivo escalando com contagem de walkers); Chandra, Torch of Defiance (card
advantage + remoção + ultimate de dano repetido); Commodore Guff (comandante alternativo,
enche a mão e queima o time todo no −3); Elspeth, Storm Slayer (token doubler próprio +
proteção via counters); Elspeth, Sun's Champion (exército + wipe seletivo + ultimate de
evasão); Grist, the Hunger Tide (remoção + mill/recorrência); Jace, the Mind Sculptor (filtro
supremo + ultimate de deckout, aqui só como recurso de controle); Karn, the Great Creator
(trava artefatos rivais); Liliana, Dreadhorde General (sacrifício em massa + ultimate
devastador); Narset, Parter of Veils (trava draw + filtro); Nicol Bolas, Dragon-God (motor
central e vitória via −8); Oko, Thief of Crowns (remoção pseudo/valor); Tamiyo, Field
Researcher (draw engine + ultimate de cast livre); Teferi, Hero of Dominaria (controle de
terreno + ultimate de exílio); Teferi, Master of Time (untap + extra turn no −10); Teferi,
Temporal Archmage (filtro + peça do combo latente); Teferi, Time Raveler (trava spells em
sorcery speed); The Theorist, Jace Beleren (draw passivo + ultimate de counters); The
Wandering Emperor (proteção instantânea); Ugin, the Spirit Dragon (wipe colorido + ultimate de
reconstrução); Vraska, Betrayal's Sting (draw + remoção + poison ultimate); Wrenn and
Realmbreaker (terrenos viram mana any color + criaturas + recursão via ultimate); Wrenn and
Six (recursão de terreno + retrace no ultimate).

**Criaturas (10)** — Atraxa, Praetors' Voice (proliferate passivo + corpo evasivo);
Birds of Paradise, Bloom Tender, Delighted Halfling (aceleração de mana/fixação); Deepglow
Skate (dobra counters ao entrar); Flux Channeler (proliferate a cada mágica não-criatura);
Onakke Oathkeeper (proteção de planeswalkers + recursão); Sanctum Lurker (planeswalkers
imortais + dreno passivo); Spark Double (copia seu melhor planeswalker ou criatura); Tekuthal,
Inquiry Dominus (dobra proliferate + indestrutibilidade).

**Motores de valor/proteção não-planeswalker (28)** — Arcane Signet, Chromatic Lantern,
Fellwar Stone, Mox Amber, Sol Ring (aceleração); Farseek, Nature's Lore, Three Visits (rampa
verde); Brokers Ascendancy, Doubling Season, Oath of Nissa, Oath of Teferi, Rhystic Study,
Smothering Tithe (motores de valor/counters); Ichormoon Gauntlet, Interplanar Beacon, Karn's
Bastion, The Chain Veil (suporte direto a planeswalkers); Counterspell, Cyclonic Rift,
Deflecting Swat, Fierce Guardianship, Swan Song, Swords to Plowshares, Teferi's Protection
(interação/proteção); Demonic Tutor, Loyal Tutor (tutores, reduzidos a 2 — ver diff abaixo);
Farewell (wipe modular); Ripples of Potential, Tezzeret's Gambit (proliferate + phase-out).

**Terrenos (37)** — base dual/fetch padrão de 5 cores (ABUR duals, choque, fetch, City of
Brass, Mana Confluence, Command Tower, Exotic Orchard, Reflecting Pool) + Karn's Bastion e
Interplanar Beacon como utilitários que também proliferam/rampam planeswalkers.

## Diferenças em relação à versão competitiva (cEDH)

Peças típicas de um pacote cEDH de fast mana/combo foram **removidas** desta versão relaxada:

- **Fast mana de um símbolo** (Mana Vault — "doesn't untap during your untap step... {T}: Add
  {C}{C}{C}"; Grim Monolith — mesmo padrão; Chrome Mox, Mox Diamond, Lotus Petal — mana
  artificial turno 1) foi cortada. Em uma mesa de poder alto casual, ligar Tam/Bolas um turno
  antes não compensa a fragilidade que esses artefatos trazem contra remoção de artefato em
  massa, e o plano aqui é sustentar o jogo, não vencer no turno 3-4.
- **Linhas de deckout/combo instantâneo** (Thassa's Oracle — "if X is greater than or equal to
  the number of cards in your library, you win the game"; Demonic Consultation / Tainted Pact —
  exilam a biblioteca até achar o nome escolhido) foram removidas: são vitórias de dois cards
  que ignoram completamente o tema de planeswalkers e "resolvem" o jogo sem interação de mesa —
  o oposto do que a versão Superfriends busca.
- **Isochron Scepter + Dramatic Reversal** (mana infinita com qualquer rocha/terreno produzindo
  2+ mana: "{2}, {T}: You may copy the exiled card... cast the copy without paying its mana
  cost" sobre "Untap all nonland permanents you control") foi removida — é uma combo de mana
  infinita genérica, não específica de planeswalkers.
- **Pacotes de blink/token infinito estilo Saheeli/Felidar Guardian** ("When this creature
  enters, you may exile another target permanent you control, then return that card to the
  battlefield") — removidos pelo mesmo motivo: geram loops sem interagir com o eixo de
  planeswalkers do deck.
- **Contra-mágicas grátis adicionais e a maioria dos tutores** — a versão cEDH tende a rodar
  Force of Will ("pay 1 life and exile a blue card... rather than pay this spell's mana cost")
  e um pacote grande de tutores de um card específico. Aqui ficaram só **Fierce Guardianship** e
  **Deflecting Swat** (grátis com comandante em jogo — boas mesmo fora de combo, protegem Tam/
  Bolas) e **2 tutores** (Demonic Tutor, Loyal Tutor — este último busca especificamente um
  planeswalker e bota no topo, sinergia direta com o tema).

O que **entrou** no lugar: mais 10 planeswalkers além do "core" competitivo (subindo de ~14 para
24), os motores de lealdade em massa (Doubling Season, Deepglow Skate, Tekuthal, Flux Channeler,
Brokers Ascendancy, Atraxa), a rede de proteção de planeswalkers (Onakke Oathkeeper, Sanctum
Lurker, Teferi's Protection, The Wandering Emperor) e Interplanar Beacon/Karn's Bastion como
terrenos utilitários — tudo para sustentar um plano de "vencer com ultimates" em vez de um combo
de dois cards.

## Verificação de legalidade

- **100 cards exatos** (99 + comandante), confirmado via
  `awk 'NF{n+=$1}END{print n}' edh/tam-superfriends.txt`.
- **Sem duplicatas** — cada carta aparece uma única vez na lista.
- **Identidade de cor**: Tam, the Possibility tem identidade **WUBRG** (o custo de ativação
  `{W}{U}{B}{R}{G}` na sua própria habilidade conta para a identidade de cor, mesmo com custo de
  cast `{1}{G}{U}`), então as 99 cartas do deck — de qualquer cor — são legais por identidade.
- **Todas as 100 cartas foram encontradas** no banco local (nenhum `found: false`, nenhum erro de
  nome). Saída completa salva em
  `tam-superfriends-verified.jsonl` (scratchpad da sessão).
- **5 cartas aparecem como `commander: not_legal` no banco local, mas apenas por serem do set
  ainda não lançado (`fra`, Final Fantasy... "Aetherdrift"/expansão futura — data `released_at`
  no banco)**, não por banimento:
  - **Tam, the Possibility** — set `fra`, lançamento **2026-10-02** (o próprio comandante).
  - **Chandra, Chill of Compliance** — set `fra`, **2026-10-02**.
  - **Loyal Tutor** — set `fra`, **2026-10-02**.
  - **Sanctum Lurker** — set `fra`, **2026-10-02**.
  - **The Theorist, Jace Beleren** — set `fra`, **2026-10-23**.

  Nenhuma dessas cartas está banida — a base de dados simplesmente ainda não marca como "legal"
  cartas cuja data de lançamento é futura em relação ao dump da Scryfall. Assim que o set for
  lançado (2 a 4 semanas a partir de hoje), a legalidade vira `legal` automaticamente no próximo
  refresh do banco. Nenhuma troca foi feita por causa disso, conforme instrução do usuário.
- **mtgtop8 cEDH**: Tam, the Possibility ainda não tem lista registrada em
  `https://mtgtop8.com/format?f=cEDH` (carta muito recente) — achado registrado, sem dado
  competitivo disponível para comparação direta.
