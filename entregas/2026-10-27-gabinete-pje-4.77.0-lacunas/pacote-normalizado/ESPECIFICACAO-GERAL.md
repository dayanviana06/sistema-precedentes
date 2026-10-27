# Especificação geral para a criação dos módulos (entrada da skill `criar-modulo-de-ato`)

Esta pasta fornece, para cada módulo, os **modelos do gabinete** na forma que a fábrica espera: o texto-base de cada ramo (em `corpo.md`) e os metadados de registro (em `meta.json`). A fábrica monta a skill, o manifesto de ramos e o registro; o Claude Code não deve reescrever os ramos.

## Arquivos de cada `modulos/<skill>/`

`corpo.md` traz o título, as seções fixas (`Finalidade`, `Quando usar e quando não usar`, `Portões`, `Ramos`, `Normas, precedentes e pesquisa obrigatória antes de redigir`, `Documentos prioritários`, `Parâmetros repetíveis`, `Dados essenciais`, `Especialistas e cálculo`, `Nomenclatura`, `Posicionamentos e decisões reservadas`) e, em `Ramos`, um modelo completo por ramo, cada um iniciado pela âncora `**CÓDIGO-NN — Título.**`. Cada ramo contém: marcos de uso, portões, relatório, fundamentação por questão (com variáveis `{{...}}`), dispositivo em itens, pontos a revisar típicos e encaminhamento seguinte.

`meta.json` traz `skill`, `descricao` (já dentro do teto de 1.024 caracteres e sem sinais de maior e menor), `titulo`, `especie` (D ou DP, para o `ESPECIES` do `esqueleto_ramos.py`), `tipo`, `familias`, `origem`, `ramos` (código, hipótese e quando usar, que alimentam o manifesto `references/ramos/_ramos.json`), `encaminhamento` (situações para `encaminhamento-civel.json`), `competencia` (cartão para `competencias.json`), `especialistas` (para `roteiros.json`), `tabela_linha` (linha da tabela da entrada-gabinete), `vizinhas_nao_cobre` (acréscimos ao `nao_cobre` das skills vizinhas) e `normas_incluir_registro` (itens que não estão em `normas-conferidas.json` e entram como "a confirmar").

`exemplo.md` é a minuta fictícia de autoteste (vai para `shared/exemplos/` e deve passar em `checar_minuta.py` sem BLOQUEIO). `adaptacoes.md` lista as variações fáticas admitidas (viram `references/adaptacoes.md`, cada uma como ponto B).

## Regras de montagem

O `SKILL.md` leva o frontmatter (`name` e `description` do `meta.json`), o ponteiro do núcleo e os blocos finais de regras inegociáveis iguais aos da skill `decidir-rito-e-competencia-do-cadastro`, o aviso de esqueleto sem modelo (versão 0.1.0, 27.10.2026) e o `corpo.md`. Não se altera nenhum arquivo de skill existente, exceto o acréscimo ao `nao_cobre` do cartão de competência das vizinhas. A espécie entra em `ESPECIES` do `esqueleto_ramos.py` do gabinete e do molde da fábrica, para a sincronização do núcleo não desfazer o registro. O módulo nasce em versão 0.1.0 e só passa a 1.0 quando o magistrado ratificar os modelos.

## Cautelas jurídicas

Os modelos citam apenas normas e precedentes já conferidos no registro do gabinete (por id) e, quando necessário, dispositivos legais marcados "a confirmar", que o `pesquisador-vigencia` confere em fonte oficial antes da primeira minuta. Pontos de mérito que o magistrado decide ficam como "DECISÃO RESERVADA" (ponto C), com a via adotada e a alternativa. Nenhum modelo traz número de processo, nome de parte, valor ou Id. reais.
