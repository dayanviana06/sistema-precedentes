# Entrega de 27.10.2026 — gabinete-pje 4.77.0 e fábrica 4.65.0 (pacote de lacunas do cumprimento de sentença e alteração da regra 53)

Esta pasta contém os dois plugins atualizados, prontos para instalação, e o pacote normalizado que lhes deu origem. O material de entrada foi o pacote em Word de 27.10.2026, resultante da triagem de cobertura de 71 processos conclusos nas tarefas de alvará, homologação de cálculo, impugnação e sentença de extinção, revisado pelo cofre do Obsidian. A base foi o gabinete-pje 4.75.0 e a fábrica 4.63.1 instalados.

## O que mudou no gabinete-pje (4.76.0 e 4.77.0)

Foram criados dez módulos novos de elaboração, todos da matéria cível e da fase de cumprimento, com 42 ramos codificados e carregamento por ramo (regra 73). O módulo `minutar-decisao-recusa-contadoria-e-quem-calcula` (RCQ-01 a RCQ-04) decide quem calcula quando a Contadoria persiste na recusa. O módulo `minutar-decisao-impugnacao-com-homologacao` (IHO-01 a IHO-05) julga a impugnação ao cálculo da Contadoria Judicial Única e homologa no mesmo ato. O módulo `minutar-decisao-alvara-composto-cumprimento` (ALC-01 a ALC-04) trata do alvará condicionado à multa do art. 523, à restituição de excedente, à natureza do depósito ou a vários beneficiários. O módulo `minutar-decisao-habilitacao-herdeiros-cumprimento` (HAB-01 a HAB-04) cuida da habilitação de sucessores e dos alvarás a eles. O módulo `minutar-decisao-sequestro-rpv-e-alvara-fazenda` (SEQ-01 a SEQ-04) trata do que vem depois do sequestro por RPV não paga. O módulo `minutar-decisao-ordem-publica-cumprimento-fazenda` (OPF-01 a OPF-03) reúne o reexame necessário omitido, a coisa julgada de outra demanda e o controle de ofício do demonstrativo. O módulo `minutar-decisao-fazenda-casos-especiais` (FZE-01 a FZE-05) abrange o título extrajudicial, o cumprimento misto, os entes solidários, o sindicato e a cessão de crédito. O módulo `minutar-decisao-executado-recuperacao-judicial` (RJU-01 a RJU-07) trata da executada em recuperação judicial ou falida. O módulo `minutar-decisao-excecao-preexecutividade-e-embargos-penhora` (EPE-01 a EPE-04) decide a exceção de pré-executividade contra o bloqueio, os embargos à penhora, as multas dos arts. 81 e 774 e os embargos contra astreinte no Juizado. Por fim, o módulo `minutar-despacho-decisao-cumprimento-casos-isolados` (CIS-01 e CIS-02) cobre dois casos isolados.

O texto dos ramos é cópia literal do pacote, sem reescrita, em `references/modelos-ramos.md` de cada skill. O triador passa a reconhecer as dez situações novas de encaminhamento, e as situações e os cartões de competência vizinhos receberam apenas acréscimos de exclusão e de destino. Nenhuma skill preexistente teve o texto alterado. Foram registrados como "pendente" 39 dispositivos e precedentes citados nos módulos que não constavam do registro de normas. O teor ficou em branco, porque nada foi preenchido de memória, e o `pesquisador-vigencia` deve conferi-los em fonte oficial antes da primeira minuta.

## O que mudou na fábrica (4.64.0 e 4.65.0)

A fábrica ganhou dois scripts. O `converter_pacote_word.py` leva o pacote em Word ao formato de Markdown da fábrica, sem reescrever o texto. O `instalar_pacote_modulos.py` instala o pacote numa cópia do gabinete e faz todos os registros; sem `--aplicar`, apenas relata o que faria. O método está descrito em `skills/criar-modulo-de-ato/references/pacote-de-modulos.md`. O molde do núcleo foi atualizado com as espécies, a matéria "cumprimento" do esqueleto, as normas pendentes e a tabela da entrada, de modo que a próxima sincronização não desfaz a instalação.

## Pendências que dependem do magistrado

Todos os módulos nascem em versão 0.1.0, como esqueleto sem modelo vigente do gabinete. As exceções são o FZE-05, que adota o modelo vigente de cessão de crédito, e o RJU-05 e o RJU-06, que seguem atos assinados do juízo. As decisões de mérito saem como DECISÃO RESERVADA (ponto C), com a via adotada e a alternativa. Cada módulo passa a 1.0 só depois da ratificação dos modelos após o uso real.

Por autorização do magistrado de 27.10.2026, a regra 53, item 3, foi alterada na versão 4.77.0 do gabinete e 4.65.0 da fábrica. No cumprimento do rito comum, a executada em recuperação judicial ou falência passou a ser minutada pelo módulo `minutar-decisao-executado-recuperacao-judicial`, observados os portões do módulo. Continuam na ficha de devolução a falência sem prova da decretação, a recuperação extrajudicial, o cumprimento no Juizado e o caso em que algum portão falhar. A natureza do crédito, o destino do valor constrito e a escolha entre suspender e extinguir com certidão de crédito seguem como DECISÃO RESERVADA. A alteração alcançou o texto da regra, o cartão de regras, o triador, a tabela da entrada, o encaminhamento, as competências e as remissões de sete skills vizinhas.

O ramo RCQ-01 admite homologar a conta do exequente sem cálculo da Contadoria quando a Fazenda não impugna, e essa via precisa ser confirmada. Os demais pontos C, como suspender ou extinguir com certidão de crédito na recuperação judicial e o fundamento das multas do EPE-03, estão listados em cada módulo.

## Verificação

`verificar_gabinete.py` e `validar_cowork.py` resultaram válidos nos dois plugins, sem erro. `esqueleto_ramos.py verificar` conferiu 64 skills sem erro, e `aferir_competencia.py validar` deu o catálogo como válido. Os dez exemplos de autoteste passam em `checar_minuta.py` sem BLOQUEIO. Restam neles os mesmos apontamentos CORRIGIR do exemplo da skill de rito e cadastro: blocos finais próprios da minuta real e itens numerados do dispositivo.

Os testes do núcleo registram 2 falhas em 130, ambas nos testes de Drive (`TesteDriveDaContaDoClaude`). As mesmas duas falhas ocorrem no gabinete 4.75.0 original, sem nenhuma alteração.

## Instalação

Instale os dois arquivos `.plugin` desta pasta e desative as versões anteriores (gabinete-pje 4.75.0 ou 4.76.0 e fábrica 4.63.1 ou 4.64.0). A pasta `pacote-normalizado` só serve para reinstalação ou auditoria e não precisa ser instalada. Os textos dos ramos citam, na linha "Cofre", números de processos e Ids. de atos do juízo, tal como vieram no pacote; as minutas fictícias de autoteste não trazem dados reais.

## Versão posterior

Os arquivos `.plugin` desta entrega foram substituídos pelos da pasta `entregas/2026-10-27-gabinete-pje-4.78.0-triagem-blocos/` (gabinete-pje 4.78.0 e fábrica 4.66.0), que contêm também tudo o que está descrito aqui.
