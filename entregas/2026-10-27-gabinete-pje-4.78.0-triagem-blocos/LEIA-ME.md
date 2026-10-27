# Entrega de 27.10.2026 — triagem prévia em blocos de afinidade (regra 95): fábrica 4.66.0 e gabinete-pje 4.78.0

Esta pasta contém os dois plugins prontos para instalação, o inventário do passo 1 (`INVENTARIO-TRIAGEM.md`) e um relatório sintético gerado e aprovado pelo verificador (`EXEMPLO-TRIAGEM-SINTETICA.md`, só com dados fictícios). A base foi o gabinete-pje 4.77.0 e a fábrica 4.65.0 instalados. O comando foi aplicado primeiro na fábrica (molde do núcleo) e propagado ao gabinete pela sincronização oficial (`sincronizar_nucleo.py --aplicar`); nenhum conteúdo jurídico foi alterado.

## O que mudou na fábrica (4.66.0)

- **Regra e gabarito no molde:** regra 95, gabarito do bloco em `molde-nucleo/shared/nucleo/referencias/gabarito-bloco-triagem.md`, gerador `listas_distribuicao.py` reescrito, relatório de triagem sem tabela em `relatorio_onda.py`, verificador `checar_triagem.py` com autoteste, limite de 8 processos por bloco em `limites.json` e testes `TesteTriagemBlocos2710` na suíte do núcleo.
- **Conferidor da fábrica:** `scripts/conferir_triagem_plugin.py` é chamado por `validar_cowork.py` e `verificar_gabinete.py`. A auditoria, a validação e o empacotamento recusam plugin com triagem em tabela, sem o verificador ou sem a regra 95. Aplicado ao gabinete 4.77.0 original, ele aponta 13 erros; no 4.78.0, nenhum.
- **Skills da fábrica:** `auditar-plugin-minutas`, `validar-plugin-cowork`, `criar-plugin-minutas` (padrão do gabinete), `criar-modulo-de-ato` (cabeçalho do bloco e campos `portoes` e `parametros_comuns` no pacote de módulos), `criar-agente-especialista`, `incluir-regra`, `sincronizar-nucleo` e `empacotar-gabinetes` passaram a trazer o item da regra 95. O instalador de pacotes leva esses campos à tabela de encaminhamento.

## Regra criada

**Regra 95 — Triagem prévia em listas por blocos de afinidade autossuficientes** (`95-triagem-previa-em-blocos-de-afinidade`, 27.10.2026), no catálogo `regras.json` 4.54.0. Etapas: triagem e entrega. Atos: todos. O enunciado é o do passo 2 do comando, e o formato completo do passo 3 está no gabarito. A regra 67 continua ativa, com um complemento que remete à 95; no cartão de regras, as duas dividem uma linha para caber no teto de 20.000 caracteres (19.997).

## O que mudou em cada plugin

- **gabinete-pje 4.78.0:**
  - Núcleo sincronizado: regra, gabarito, gerador, verificador, triador, `triar-processos`, `orquestrar-ondas` (modo `triar` e formato do bloco reconhecido), `entrada-gabinete` e `consultar-fila`.
  - O bloco mantém o marcador `[GABINETE-PJE — LISTA DE DISTRIBUIÇÃO DA TRIAGEM]`. A linha de comando fica antes dele, e o leitor aceita tanto o formato novo quanto o anterior. Assim, o bloco copiado é reconhecido numa conversa nova sem adaptação.
  - Convertidos do formato em tabela: `triagem-pendencias-execucao-pje` (o gerador Node.js em tabelas foi retirado), o relatório por pendências e o relatório de diagnóstico da `contadoria-diagnostico-e-minutas` e a Fase 3 da `sentencas-progressao-horizontal-pje`.
- **sessao-juri-pje e relatorios-para-aij-criminal-ou-civel:** não têm triagem prévia e não foram alterados.
- **gestor-emergencias-urgencias:** não foi alterado (ver as decisões abaixo).

## O que permaneceu em tabela e por quê

- Quadro dos modos do orquestrador e resumo das tabelas de encaminhamento da entrada: documentação interna, não relatório de triagem.
- Quadro de auditoria e Tabela 2 da pré-triagem dos consignados suspensos: análise por processo gravada na instrução, não relatório de distribuição. A distribuição desses processos já sai em blocos.
- Quadro comparativo VIA A × VIA B da remessa interativa: referência jurídica.
- `triagem.csv` e `triagem_<CNJ>.json`: registros internos de trabalho, que não são entregues.
- Relatório da onda, minutas prontas, livro de distribuição interna, gestão, consumo, cálculo, auditoria de fase e ficha de audiência: fora do escopo do comando. Ficaram apenas listados como observação, sem conversão.

## Verificador

`shared/nucleo/scripts/checar_triagem.py` (no molde e no gabinete):

- **Uso:** `--relatorio <arquivo .md, .html ou .docx>` confere um relatório; `autoteste` roda o teste sintético.
- **Na fábrica:** `scripts/conferir_triagem_plugin.py` executa a conferência do plugin inteiro.

## Resultado dos testes

- **Autoteste sintético:** 16 processos em 6 grupos, com um processo em segredo de justiça e um de autos a baixar. Um processo traz remissão ao bloco da impugnação. Há ainda um grupo de 10 subdividido pelo limite de 8 e um grupo dividido por afinidade (família e modelo diferentes). Resultado:
  - 7 blocos;
  - contagem fechada;
  - nenhum campo perdido em relação à versão em tabela;
  - cada bloco, colado sozinho, é reconhecido e roteado à skill indicada;
  - a versão em tabela é recusada.
- **Relatório em Word:** o relatório completo da triagem foi gerado também em Word e aprovado pelo verificador, sem nenhuma tabela.
- **Suíte do núcleo:** 130 de 132 testes passam, inclusive os dois novos. As duas falhas são dos testes de pastas do Drive e ocorrem igualmente no plugin original. O script se recusa a criar pastas numa máquina temporária do Cowork, de modo que as falhas não têm relação com esta alteração.
- **Demais verificadores:** `verificar_gabinete.py`, `validar_cowork.py` (gabinete e fábrica), `esqueleto_ramos.py verificar`, `aferir_competencia.py validar` e o sumário de skills estão sem erro.

## Decisões que dependem do magistrado (via conservadora já adotada)

- <mark><b><span style="color:red">Limite do bloco: adotei 8 processos, que é o lote do gabinete; cada bloco é executado em ondas de 4 (regra 80). Alternativa: 4, o que daria uma onda por bloco. Mantém 8?</span></b></mark>
- <mark><b><span style="color:red">Partes no bloco: incluí o nome das partes na primeira linha de cada processo, como o comando determina. A fila persistente do cofre continua a guardar só o número e a classificação (regra 23). Confirma que as partes podem constar dos blocos e dos arquivos da sessão?</span></b></mark>
- <mark><b><span style="color:red">Rótulo "sem modelo — supletiva": usei o texto do comando sempre que a tabela não indica modelo, inclusive nos módulos em esqueleto que têm ramos próprios. Alternativa: "sem modelo vigente". Mantém o rótulo do comando?</span></b></mark>
- <mark><b><span style="color:red">Pedido do bloco: mantive o texto atual ("blocos de oito, com no mínimo quatro redatores em paralelo, regra 44"), embora o fluxo padrão do lote seja o da regra 80 (ondas de quatro assessores). Atualiza o pedido para a regra 80?</span></b></mark>
- <mark><b><span style="color:red">Remessa interativa à Contadoria: o "Relatório de Triagem e Diagnóstico" dela trata de um processo por vez e não foi convertido. Confirma que fica fora do padrão?</span></b></mark>
- <mark><b><span style="color:red">gestor-emergencias-urgencias: a triagem dele é de emergência e urgência (perfil, caixa e responsável), e o plugin não é gerado pela fábrica; não foi alterado. Confirma que fica fora do padrão?</span></b></mark>
- <mark><b><span style="color:red">Exemplo de bloco com o grupo HOM encurtado: não recebi esse exemplo nesta conversa. O gabarito seguiu o texto do comando, e o exemplo fictício do gabarito usa o grupo de homologação. Se quiser, envie o exemplo para que eu ajuste a ordem ou o rótulo das linhas.</span></b></mark>

Também retirei o arquivo `scripts/example_data.js` da `triagem-pendencias-execucao-pje`, junto com o gerador em tabelas. Ele trazia números de processos e nomes de partes reais como dados de exemplo.

## Instalação

Instale os dois arquivos `.plugin` desta pasta e desative as versões anteriores (gabinete-pje 4.77.0 e fábrica 4.65.0).
