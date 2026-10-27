# Inventário da triagem prévia — comando único de 27.10.2026 (passo 1)

Base: gabinete-pje 4.77.0 e fábrica 4.65.0 (cópias idênticas às instaladas). Os caminhos do gabinete valem também para o molde da fábrica (`molde-nucleo/`), quando o arquivo é do núcleo. Classificação: (a) a converter; (b) tabela de conteúdo por natureza, que permanece; (c) dúvida (ponto C).

## (a) A converter

- `shared/nucleo/scripts/listas_distribuicao.py:131-166` (`bloco`, `bloco_especial`) — bloco atual traz só CNJ, urgência e sinal; sem linha de comando, sem partes, sem Situação, Providência, Ids a ler e Conferir; sem subdivisão obrigatória por limite (`--por-lote` opcional, l. 189); sem afinidade por rito e parâmetros (l. 119-121); sem panorama nem conferência de contagem (l. 175-184); leitor `ler_blocos` (l. 233-251) só aceita o CNJ no início da linha.
- `shared/nucleo/scripts/relatorio_onda.py:337-387` (`montar_triagem`) — relatório de triagem: resumo e exame direto a ajustar ao gabarito; `relatorio_onda.py:189` (`secao_via_de_leitura`) — **tabela Markdown** de via de leitura dentro do relatório de triagem; `relatorio_onda.py:416-426` (`md_para_docx`) — o bloco copiável vira **tabela de uma célula** no Word.
- `shared/nucleo/regras/67-resultado-da-triagem-em-listas-copiaveis.md:7` e `regras.json` (regra 67) — enunciado diz que a lista traz só CNJ e urgência por processo; complementado pela regra nova.
- `shared/nucleo/regras/00-cartao-de-regras.md:75` — cartão sem a regra nova.
- `shared/nucleo/config/limites.json:235` (`triagem`) — sem limite de processos por bloco da triagem.
- `skills/triar-processos/SKILL.md:16-22, 33` e `agents/triador.md:14` — produto da triagem e campos de `triagem_<CNJ>.json` (sem partes, fatos com Id., Ids a ler, pontos a conferir, parâmetros e remissão).
- `skills/orquestrar-ondas/references/modo-minutar-lista.md:9-31` — entrega e formato do bloco reconhecido; `skills/orquestrar-ondas/SKILL.md:40` (descrição do modo `triar`).
- `skills/entrada-gabinete/SKILL.md:34` — reconhecimento do bloco colado (marcador mantido; a linha de comando vem antes do marcador).
- `skills/triagem-pendencias-execucao-pje/SKILL.md:64-83`, `references/logica-analise.md:94-129` e `scripts/build_report_template.js`, `report_helpers.js`, `example_data.js` — relatório de triagem em Word paisagem com **uma tabela por categoria** (U, A, B, C, D, E, F), legenda e síntese em tabela.
- `skills/contadoria-diagnostico-e-minutas/references/logica-analise-impugnacoes.md:125-212` — relatório por pendências das impugnações (Fase 2, antes das minutas) com legenda em **tabela HTML**, ficha individual em **tabela HTML** e **tabela-resumo** por seção.
- `skills/sentencas-progressao-horizontal-pje/SKILL.md:143-147` — Fase 3, resultado da triagem em **tabela única** no chat; `references/mapa-conformidade.md:119` e `references/partes/mapa-conformidade/07-6-portoes-de-exc.md:3` — "informar na tabela de triagem".
- Fábrica: `skills/criar-plugin-minutas/references/padrao-gabinete.md`, `skills/criar-modulo-de-ato/SKILL.md` e `references/pacote-de-modulos.md`, `scripts/instalar_pacote_modulos.py`, `skills/auditar-plugin-minutas/SKILL.md`, `skills/validar-plugin-cowork/SKILL.md` e `scripts/validar_cowork.py`, `scripts/verificar_gabinete.py`, `skills/incluir-regra/SKILL.md`, `skills/sincronizar-nucleo/SKILL.md`, `skills/empacotar-gabinetes/SKILL.md`, `skills/criar-agente-especialista/SKILL.md` — nenhum traz o gabarito do bloco nem verifica a triagem; passam a trazê-lo ou a rodá-lo.

## (b) Tabela de conteúdo por natureza, que permanece

- `skills/orquestrar-ondas/SKILL.md:38-50` — quadro dos modos do orquestrador (documentação interna, não relatório de triagem).
- `skills/entrada-gabinete/references/tabelas-encaminhamento.md` — resumo humano das tabelas de encaminhamento (documentação; a fonte é o JSON).
- `skills/minutar-sentenca-emprestimo-consignado/references/pre-triagem-suspensos.md:19-21` e `lote-suspensos-tema12.md:21` — QUADRO DE AUDITORIA e TABELA 2 por processo, gravados na instrução (`pretriagem_<CNJ>.md`); a distribuição desses processos já sai pelas listas de `listas_distribuicao.py` e passa ao gabarito novo automaticamente.
- `skills/remessa-contadoria-interativa/references/00-NUCLEO.md:218-224` — quadro comparativo VIA A × VIA B (referência jurídica).
- `triagem.csv` e `triagem_<CNJ>.json` — registros internos de trabalho, nunca entregues (regra 67).

## (c) Dúvida — ponto C

- `skills/remessa-contadoria-interativa` (Etapa 1, "Relatório de Triagem e Diagnóstico Técnico"): é o diagnóstico de um processo por vez, em modo interativo, e não relatório de distribuição; não convertido. **CONFERIR: confirmar que fica fora do padrão.**
- Plugin `gestor-emergencias-urgencias`: a triagem dele é de emergência e urgência (perfil, caixa e responsável), não de distribuição de minutas, e o plugin não é gerado pela fábrica; não alterado. **CONFERIR: confirmar que fica fora do padrão.**

## Fora do escopo (só observação, sem conversão)

- `skills/orquestrar-ondas/SKILL.md:120` (modo `status` da fila: resumo "em uma tabela no chat"); `shared/nucleo/scripts/relatorio_onda.py:80, 144, 208` (relatório da onda, minutas prontas e distribuição interna); `shared/nucleo/scripts/mesa_distribuicao.py` (`livro`); `shared/nucleo/scripts/medir_consumo.py:11`; `skills/relatorio-gestao-gabinete/SKILL.md:12`; `skills/calcular-liquidacao/references/roteiro-homologacao-calculadora.md:85` ("quadro de triagem" do cálculo); `skills/auditar-fase-processual/references/01_NUCLEO.md:293` (auditoria); `skills/relatorios-para-aij-criminal-ou-civel/SKILL.md:98-122` (ficha de audiência).
- Plugins `sessao-juri-pje` e `relatorios-para-aij-criminal-ou-civel`: sem relatório de triagem prévia.
