# Complemento de lacunas do gabinete-pje — comandos e modelos (27.10.2026)

Origem: triagem de cobertura de 71 processos conclusos nas tarefas de alvará, homologação de cálculo, impugnação e sentença de extinção da Vara Única de Senador La Rocque. Base: gabinete-pje 4.72.0 e fábrica 4.61.0. Nenhuma skill foi criada nem alterada: este pacote traz só os **comandos** (para você pedir a criação no Claude Code) e os **modelos** (o conteúdo de cada módulo novo).

## Revisão pelo cofre do Obsidian (27.10.2026)

Os dez módulos foram comparados com os modelos do PJe, os atos anonimizados do juízo e as notas de entendimentos do cofre. O quadro por ramo (adoção, complementação, sem correspondente ou divergente) está em `COMPARACAO-COM-O-COFRE.md`, e cada ramo traz a linha "Cofre (27.10.2026)" com as fontes. Resultado: foram acrescentados o ramo FZE-05 (cessão de crédito contra a Fazenda, modelo vigente adotado) e os ramos RJU-05 (despacho de suspensão), RJU-06 (falência da executada) e RJU-07 (orientação para a sentença de extinção com certidão de crédito), e vários pontos de decisão reservada passaram a registrar as vias reais do cofre.

## Conteúdo

`comandos/` — onze comandos de criação e um de triagem: `criar-modulos-lacunas` (cria os dez módulos de uma vez), `criar-modulo-rcq`, `-fze`, `-iho`, `-cis`, `-alc`, `-hab`, `-seq`, `-opf`, `-rju` e `-epe` (um módulo cada), e `triar-cobertura-cumprimento` (repete a triagem de cobertura no PJe, somente leitura).

`modelos-lacunas-27-10-2026/modulos/<skill>/` — para cada um dos dez módulos: `corpo.md` (um modelo completo por ramo, com relatório, fundamentação, dispositivo e pontos a revisar), `meta.json` (descrição, ramos, encaminhamento, competência, roteiro e vizinhas), `exemplo.md` (minuta fictícia de autoteste) e `adaptacoes.md`. Também `ESPECIFICACAO-GERAL.md` (como a fábrica deve montar), `MAPA-DE-LACUNAS.md` (processo da triagem → módulo) e `NORMAS-A-CONFIRMAR.md` (dispositivos que não estão no registro).

## Como usar

1.  Copie `comandos/*.md` para `.claude/commands/` do projeto (ou `~/.claude/commands/`) e a pasta `modelos-lacunas-27-10-2026` para a pasta de trabalho do Claude Code, com os plugins gabinete-pje e fábrica instalados.
2.  Rode `/criar-modulos-lacunas` (ou um `/criar-modulo-<prefixo>` por vez). O comando manda a fábrica (`criar-modulo-de-ato`) montar a skill em cópia do gabinete, registrar encaminhamento, competências e roteiros, gerar os ramos, rodar os verificadores, sincronizar o núcleo, subir a versão e empacotar o `.plugin`.
3.  Instale o `.plugin` gerado. Depois do uso real, ratifique os modelos para sair da versão 0.1.0.

## Módulos

RCQ recusa persistente da Contadoria e quem calcula · IHO impugnação julgada e cálculo homologado no mesmo ato · ALC alvará composto (multa do art. 523, restituição de excedente, depósito como garantia, vários beneficiários) · HAB habilitação de herdeiros e alvarás · SEQ sequestro de RPV e alvará contra a Fazenda · OPF ordem pública e controle de ofício contra a Fazenda · FZE casos especiais contra a Fazenda (título extrajudicial, cumprimento misto, astreintes solidárias, sindicato) · RJU executada em recuperação judicial · EPE exceção de pré-executividade, embargos à penhora e embargos no Juizado · CIS casos isolados (cumprimento de acórdão que manda arquivar; novo cumprimento após indeferimento).

## O que exige sua atenção

Todos os módulos nascem como **esqueleto sem modelo do gabinete** (0.1.0) e trazem decisões de mérito como "DECISÃO RESERVADA" (ponto C), com a via adotada e a alternativa. Os dispositivos que não constam do registro de normas estão em `NORMAS-A-CONFIRMAR.md` e entram nas minutas como "a confirmar". O módulo RJU diverge da regra 53, item 3 (pausar executada em recuperação judicial), embora o cofre mostre atos seus de suspensão, de extinção com certidão de crédito e de falência; ele só deve ser acionado depois de você autorizar a mudança de regra. O RCQ-01 admite homologar a conta do exequente sem cálculo da Contadoria quando a Fazenda não impugna: confirme essa via. Os modelos derivam da leitura de dois a cinco documentos por processo; confira os autos antes de adotar um ramo.
