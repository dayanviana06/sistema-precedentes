# Decisão no cumprimento de sentença contra empresa em recuperação judicial

## Finalidade

Decidir, em ato próprio, o cumprimento de sentença movido contra pessoa jurídica de direito privado em recuperação judicial quando a executada alega que o crédito é concursal (fato gerador anterior ao pedido). O ato resolve a natureza do crédito, define os efeitos processuais dessa natureza (vedação de constrição, juízo universal, certidão de crédito para habilitação, suspensão ou prosseguimento só da liquidação), fixa os parâmetros de cálculo quando a executada questiona juros, correção e novação, e ordena a sequência quando a executada pede a gratuidade da justiça na própria impugnação. Desde 27.10.2026, o módulo também traz o despacho de suspensão com intimações (RJU-05), a decisão que dá vista ao exequente quando a executada é declarada falida (RJU-06) e a orientação para a sentença de extinção com certidão de crédito (RJU-07), todos a partir de atos assinados do cofre. Antes deste módulo, a executada em recuperação judicial caía no portão 3 da regra 53 (ficha de devolução), no portão interno de `minutar-sem-modelo-cumprimento-sentenca`, no portão 2 de `minutar-decisao-penhora-alvara` e na pendência do IMP-03 de `contadoria-diagnostico-e-minutas`, sem texto para o magistrado. A decisão de mérito sobre a concursalidade é reservada ao magistrado: a minuta traz a via adotada e a alternativa em ponto C, nunca como conclusão definitiva.

## Quando usar e quando não usar

Usar quando, no cumprimento de sentença do rito comum, a executada é sociedade empresária privada em recuperação judicial (processamento deferido, com Id.) e há controvérsia ou necessidade de decidir sobre: a natureza do crédito (RJU-01); os efeitos processuais da natureza do crédito (RJU-02); o cálculo, quando a executada limita juros e correção à data do pedido ou invoca a novação (RJU-03); ou a gratuidade da justiça da executada formulada na impugnação e ainda não apreciada (RJU-04). Também se usa para suspender o cumprimento em razão da recuperação judicial, com as intimações do ato do cofre (RJU-05); para dar vista ao exequente quando a executada passa a falida (RJU-06); e para orientar a sentença de extinção com certidão de crédito, na recuperação judicial ou na falência (RJU-07). Os ramos RJU-01 a RJU-03 saem, em regra, no mesmo ato; RJU-04 precede o mérito; RJU-05 e RJU-06 são alternativas à decisão de mérito, e RJU-07 é o ato final de qualquer das vias.

Não usar, com o destino de cada hipótese vizinha:

- Falência decretada: RJU-06 (vista ao exequente, com o interesse na certidão de crédito) e, depois, a extinção orientada no RJU-07 (→ `minutar-sentenca-extincao-civel`). Falência sem prova da decretação nos autos (Id. e data): ficha de devolução (regra 53), RESERVADO AO GABINETE.
- Recuperação extrajudicial (homologação ou juntada de plano): sem ramo. O cofre tem uma decisão sobre a juntada de plano de recuperação extrajudicial (0802873-18.2019.8.10.0131), que não foi adotada.
- Executada que é ente público, empresa pública ou sociedade de economia mista: AGUARDANDO CONFIRMAÇÃO do regime; não presumir. Fazenda Pública: `minutar-homologacao-calculos` e `contadoria-diagnostico-e-minutas` (trilha da Fazenda).
- Processo de conhecimento com a ré em recuperação judicial: suspensão pelo → `minutar-decisao-suspensao-sobrestamento`, ramo SUS-05, subramo E.
- Cumprimento no Juizado Especial com executada em recuperação judicial: sem ramo; ficha de devolução (→ `minutar-impugnacao-cumprimento-jec`, passo 2).
- Devolução da Contadoria sem cálculo sem questão de recuperação judicial: → `minutar-decisao-complementar-pos-contadoria`, ramo COMP-C. Com a questão de recuperação judicial, o ato é este, e o texto da remessa é o literal de COMP-C.
- Cálculo da Contadoria já juntado e impugnado: → `minutar-homologacao-calculos`.
- Gratuidade da justiça como único objeto do ato: → `minutar-decisao-gratuidade`, ramo GRAT-05. Este módulo só define a sequência quando a gratuidade vem com a impugnação (RJU-04).
- Cancelamento da distribuição da impugnação por falta de custas, depois de decidida a gratuidade e decorrido o prazo: → `contadoria-diagnostico-e-minutas`, ramo IMP-07.
- Bloqueio, desbloqueio, transferência e alvará em processo de executada que não esteja em recuperação judicial: → `minutar-decisao-penhora-alvara`. Quando a executada está em recuperação judicial, o destino do valor já constrito é capítulo do RJU-02, em ponto C.
- Impugnação sem relação com a recuperação judicial: → `contadoria-diagnostico-e-minutas`.

## Portões

0.  Regra 53, item 3 ("executada em recuperação judicial ou falência — não minutar"). Este módulo é o destino do portão para o magistrado que decidir minutar. O cofre mostra que o magistrado já decidiu e despachou esses casos (RJU-05, RJU-06 e RJU-07 reproduzem os atos); a divergência entre a regra 53 e a prática fica registrada no ponto B do ramo e no relatório, sem alterar a regra. Se qualquer portão abaixo falhar, não se minuta: ficha de devolução (regra 53) com o que falta, as duas vias possíveis e o Id. de cada prova.
1.  Recuperação judicial provada nos autos, com Id.: decisão de deferimento do processamento (data), data do pedido, e, havendo, decisão de homologação ou concessão do plano. Documento determinante ilegível, não lido ou cujo conteúdo dos anexos não foi aberto: via dos autos baixados (regra 35) ou corroboração por fonte independente (regra 38); sem uma delas, não se afirma a data do pedido nem o plano.
2.  Rito comum provado (capa, classe, sentença). Dúvida: AGUARDANDO CONFIRMAÇÃO. Cadastro de Juizado com título de rito comum: → `decidir-rito-e-competencia-do-cadastro`.
3.  Fato gerador do crédito com data e Id. (contrato, evento danoso, ato ilícito, sentença que o declara). Sem a data, ou com fato gerador contínuo ou em vários eventos, a natureza não se decide: ficha de devolução, ou RJU-01 com ponto C reforçado (divisão do crédito por evento).
4.  Decisão do juízo da recuperação sobre este crédito (habilitação, divergência, impugnação de crédito, exclusão do plano), se houver Id.: a minuta não a contraria e a cita como premissa; se o juízo da recuperação já decidiu a natureza, o ramo RJU-01 vira reconhecimento da decisão, sem juízo próprio.
5.  Contraditório (art. 10 do CPC, registro `cpc-10`): a parte exequente teve oportunidade de falar sobre a concursalidade (Id. da resposta ou da intimação). Sem ela, a minuta é o despacho de vista, e não esta decisão, pela trilha geral (→ `minutar-despacho-decisao-civel-geral`).
6.  Gratuidade formulada na impugnação e não apreciada: entra o RJU-04 antes de qualquer capítulo de mérito. Intimação anterior para custas sem apreciação do pedido (Id.): ponto C sobre a reabertura do prazo.
7.  Constrições e depósitos nos autos: listar cada um com Id., valor, data e natureza (garantia ou pagamento). O destino deles é capítulo do RJU-02, em ponto C. Nenhum alvará nesta decisão (trava 13.1).
8.  Demonstrativos de cálculo legíveis: tabela em imagem no corpo da petição é checagem manual (regra 17); não se conferem rubricas de documento não lido.
9.  Texto do art. 6º da Lei nº 11.101/2005: o registro (`lei-11101-art-6`, conferido em 23.10.2026) confirma a norma, mas não traz o teor; transcrição literal só depois de conferida no original, com ponto A até lá.
10. Falência: decretação provada nos autos com Id. e data (sentença de quebra, certidão do juízo falimentar ou, no mínimo, o comprovante cadastral da Receita Federal, que é prova secundária e deve ser confirmada pelo juízo falimentar). A data da decretação é o termo final dos juros e da correção para a certidão de crédito, e não se afirma sem o documento.
11. Grupo Oi: o Aviso nº 39/2023 do TJRJ, transcrito no ato 0800160-02.2021.8.10.0131 (Id. 158708257), serve de premissa para a natureza dos créditos do grupo e para o rumo do cumprimento. Não consta do registro: entra como "a confirmar", com ponto A, até a conferência em fonte oficial do TJRJ.

## Ramos

**RJU-01 — Natureza do crédito alegado como concursal (fato gerador anterior ao pedido).**

**Cofre (27.10.2026).** COMPLEMENTAÇÃO — sentenças assinadas 0800160-02.2021.8.10.0131 (29.08.2025) e 0001403-92.2013.8.10.0131 (16.09.2026), íntegras lidas em `Atos do Juízo/Íntegras/2025` e `/2026`; sem modelo do PJe para o tema — o cofre confirma a via do módulo (art. 49, caput, e Tema 1.051 do STJ, fato gerador anterior ao pedido) e traz a premissa do Aviso nº 39/2023 do TJRJ para o Grupo Oi, acrescentada como parágrafo opcional, com 🟡 por não constar do registro.

**Quando usar.** A executada sustenta, na impugnação ou em petição, que o crédito exequendo é concursal porque o fato gerador ocorreu antes do pedido de recuperação judicial; ou o juízo da recuperação comunica ou a executada informa a recuperação em curso, e a natureza do crédito precisa ser definida antes de qualquer ato executivo ou de cálculo. Marcos: Id. do pedido e do deferimento do processamento; Id. do título e do evento que gerou o crédito; Id. da impugnação e da resposta.

**Portões do ramo.** Portões 1, 3, 4 e 5. Se o título tem condenações de fatos geradores distintos (por exemplo, dano moral por evento e repetição de indébito por prestações em datas diferentes), a decisão separa o crédito por fato gerador, e a natureza é declarada por parcela; nesse caso o ponto C é reforçado e a divisão vai ao dispositivo.

**Relatório.** Primeiro parágrafo na forma da regra 36: "Trata-se de cumprimento de sentença proposto por **{{EXEQUENTE}}** em face de **{{EXECUTADA}}**, em recuperação judicial." Depois, um parágrafo por evento ou grupo, na ordem cronológica:

- "Em {{data}}, a parte exequente requereu o cumprimento da sentença (Id. {{id_requerimento}}), relativo a crédito decorrente de {{fato gerador}}, reconhecido no título de Id. {{id_titulo}}."
- "Em {{data}}, o juízo da recuperação deferiu o processamento da recuperação judicial da parte executada, em pedido formulado em {{data_pedido}} (Id. {{id_deferimento}})." [SE plano homologado: "Em {{data}}, foi homologado o plano de recuperação judicial (Id. {{id_plano}})."]
- "Em {{data}}, a parte executada impugnou o cumprimento (Id. {{id_impugnacao}}) e sustentou que o crédito é concursal, porque o fato gerador ocorreu em {{data_fato}}, antes do pedido de recuperação judicial{{, e que foi novado pelo plano}}{{, e que o valor deve ser limitado à data do pedido}}."
- "Em {{data}}, a parte exequente respondeu que {{síntese da resposta}} (Id. {{id_resposta}})."
- [SE decisão anterior] "Em {{data}}, a decisão de Id. {{id_decisao_anterior}} delimitou parâmetros para o cálculo sem decidir a natureza do crédito."
- [SE devolução da Contadoria] "Em {{data}}, a Contadoria Judicial Única devolveu os autos sem cálculo e pediu a definição de {{pontos pedidos}} (Id. {{id_certidao}})."
- [SE constrição ou depósito] "Em {{data}}, {{foi bloqueado | foi depositado}} o valor de R$ {{valor}} ({{extenso}}) (Id. {{id_valor}})."

Termina com "**É o relatório. DECIDO.**".

**Fundamentação — ordem das questões.** (1) Natureza do crédito; (2) novação alegada, se houver; (3) efeitos processuais (parágrafo-âncora no RJU-02). Cada questão abre com "Passo à análise de \<questão\>.".

Questão 1, natureza do crédito:

"Passo à análise da natureza do crédito. A parte executada requereu a recuperação judicial em {{data_pedido}}, e o processamento foi deferido em {{data}} (Id. {{id_deferimento}}), enquanto o crédito exequendo decorre de {{fato gerador}}, ocorrido em {{data_fato}} (Id. {{id_prova_fato}}), e foi reconhecido em título formado em {{data_titulo}} (Id. {{id_titulo}}). A matéria é regida pelo art. 49, caput, da Lei nº 11.101/2005, segundo o qual estão sujeitos à recuperação judicial os créditos existentes na data do pedido, ainda que não vencidos. **==Dispositivo a confirmar no registro: o art. 49 não consta do registro de normas.==** 🟡 **[REVISAR]**"

"Aplica-se ao caso o Tema 1.051 do Superior Tribunal de Justiça, segundo **==[TESE A TRANSCREVER SOMENTE DEPOIS DE CONFERIDA EM FONTE OFICIAL: o tema aparece citado na triagem, mas não consta do registro; texto, situação e trânsito não foram conferidos]==** 🟡 **[REVISAR]**. No caso, **==o fato gerador de {{data_fato}} (Id. {{id_prova_fato}}) se enquadra nessa tese porque é anterior ao pedido de {{data_pedido}}==** 🟡 **[REVISAR]**."

"Nos autos, a prova do fato gerador (Id. {{id_prova_fato}}) e a data do pedido (Id. {{id_deferimento}}) demonstram que o crédito já existia quando a recuperação foi requerida. Conclui-se, portanto, que **==DECISÃO RESERVADA — natureza do crédito: via adotada, crédito sujeito à recuperação judicial (concursal), por ter fato gerador anterior à data do pedido; alternativa, crédito não sujeito (extraconcursal), se o fato gerador for posterior ao pedido, se o juízo da recuperação o houver excluído do plano ou se o magistrado entender de outro modo==** 🔴 **[REVISAR]**."

"O argumento da parte exequente de que o crédito seria posterior ao pedido, porque a condenação foi proferida e liquidada depois dele (Id. {{id_resposta}}), não altera a conclusão, porque **==o marco é a data do fato gerador, e não a da sentença; fundamento a confirmar pelo Tema 1.051 do STJ==** 🟡 **[REVISAR]**." [Usar só se o argumento foi deduzido.]

[ACRÉSCIMO DO COFRE — SE a executada integra o Grupo Oi] "Registra-se que o Tribunal de Justiça do Estado do Rio de Janeiro, por meio do Aviso nº 39/2023, orientou os juízos de origem quanto aos créditos detidos em face do Grupo Oi, distinguindo os concursais, de fato gerador constituído até 01/03/2023, dos extraconcursais, de fato gerador posterior a essa data. **==Teor do Aviso nº 39/2023 do TJRJ conforme transcrito no ato 0800160-02.2021.8.10.0131 (Id. 158708257); não consta do registro; conferir em fonte oficial do TJRJ antes de citar==** 🟡 **[REVISAR]**. A data de 01/03/2023 é a do pedido da segunda recuperação judicial (Id. {{id_deferimento}}); o crédito de {{data_fato}} {{é | não é}} anterior a ela." Nos dois atos lidos, a executada é do Grupo Oi (a primeira recuperação foi pedida em 20/06/2016, Id. do ato 0001403-92); em outra executada, o parágrafo não se aplica.

Variante se a via for o crédito extraconcursal (após decisão do magistrado): "Nos autos, a prova do fato gerador (Id. {{id_prova_fato}}) mostra que o crédito surgiu em {{data_fato}}, depois do pedido de {{data_pedido}} (Id. {{id_deferimento}}). Conclui-se, portanto, que o crédito não está sujeito à recuperação judicial e que o cumprimento prossegue pelas regras comuns, **==observada a competência do juízo da recuperação para atos de constrição sobre bens da executada (RJU-02, trilha B)==** 🔴 **[REVISAR]**."

Questão 2, novação (só se alegada): "Passo à análise da novação alegada. O plano de recuperação judicial foi homologado em {{data}} (Id. {{id_plano}}), e a parte executada sustenta que ele novou o crédito (Id. {{id_impugnacao}}). A matéria é regida pelo art. 59, caput, da Lei nº 11.101/2005, segundo o qual o plano implica novação dos créditos anteriores ao pedido e obriga o devedor e os credores a ele sujeitos. **==Dispositivo a confirmar no registro (art. 59 não consta).==** 🟡 **[REVISAR]** Nos autos, **==o plano (Id. {{id_plano}}) {{prevê | não prevê}} tratamento para o crédito do tipo {{tipo}}; o conteúdo do anexo {{foi | não foi}} lido==** 🟡 **[REVISAR]**.

Conclui-se, portanto, que **==DECISÃO RESERVADA — efeito da novação sobre o cumprimento: via adotada, o crédito concursal fica sujeito ao plano e ao pagamento no juízo da recuperação, e o cumprimento não prossegue para cobrar o valor original; alternativa, rejeitar a novação por falta de prova de que o crédito integra o plano==** 🔴 **[REVISAR]**."

**Dispositivo — modelo.**

DISPOSITIVO

Ante o exposto,

1)  **DECLARO** que o crédito exequendo, reconhecido no título de Id. {{id_titulo}}, é **==concursal (sujeito à recuperação judicial)==** 🔴 **[REVISAR]**, por ter fato gerador anterior ao pedido de recuperação judicial formulado em {{data_pedido}} (Id. {{id_deferimento}}). [SE crédito dividido: repetir o item por parcela, com o fato gerador de cada uma.]

2)  **{{ACOLHO | ACOLHO EM PARTE | REJEITO}}** a impugnação (Id. {{id_impugnacao}}) na parte em que alega {{a natureza concursal do crédito | a novação}}.

3)  a 8) Itens do RJU-02 (trilha A, se concursal; trilha B, se extraconcursal), copiados no ato, sem remissão: vedação de constrição, destino do valor já constrito, certidão de crédito, intimação para habilitação, liquidação e conclusão.

4)  Parâmetros de cálculo e remessa: itens do RJU-03, quando a impugnação ou a Contadoria exigir a definição.

Fecho, assinatura e pontos conforme o esqueleto fixo da decisão.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Tema 1.051/STJ e arts. 49 e 59 da Lei 11.101/2005: sem item no registro. Conferir em fonte oficial (pesquisador-vigencia) antes de assinar.==**
- 🟡 **==A2 — Art. 6º da Lei 11.101/2005: norma confirmada no registro, sem o teor. Transcrição literal a conferir no original.==**
- 🟢 **==B1 — Ato sem modelo do gabinete: esqueleto 0.1.0.==**
- 🟡 **==B2 — Regra 53, item 3 ("não minutar"): divergente da prática do cofre, que decide e despacha esses casos (atos 9000371-30, 0800160-02, 0001403-92, 0001120-93, 0000604-44 e 0800162-06). Confirmar a aplicação.==**
- 🟡 **==A3 — Aviso nº 39/2023 do TJRJ (Grupo Oi): fora do registro. Conferir em fonte oficial.==**
- 🔴 **==C1 — DECISÃO RESERVADA: natureza do crédito. Via: concursal (fato gerador anterior ao pedido). Alternativa: extraconcursal.==**
- 🔴 **==C2 — DECISÃO RESERVADA: efeito da novação do plano sobre o cumprimento. Via: pagamento no juízo da recuperação. Alternativa: rejeitar a novação.==**

**Encaminhamento seguinte.** Concursal: RJU-02 (trilha A), no mesmo ato, e RJU-03 para os parâmetros. Extraconcursal: RJU-02 (trilha B) e, no cálculo, `contadoria-diagnostico-e-minutas` ou COMP-C. Gratuidade pendente: RJU-04 primeiro. Habilitado o crédito no juízo da recuperação, a Secretaria cumpre a certidão e o processo aguarda na suspensão ou no sobrestamento decididos no RJU-02.

**RJU-02 — Consequências processuais da natureza do crédito.**

**Cofre (27.10.2026).** DIVERGENTE (andamento) e COMPLEMENTAÇÃO (certidão e habilitação) — sentenças 0800160-02.2021 (29.08.2025), 0001403-92.2013 (16.09.2026), 0001120-93.2018 (23.03.2026), 0000604-44.2016 (29.09.2025) e 9000371-30.2012 (23.01.2026), e despacho de suspensão 9000371-30.2012 (10.03.2025), íntegras lidas; sem modelo do PJe — a "via adotada" anterior (prosseguir só na liquidação e suspender os demais atos) não é a prática do cofre, que ou suspende por meio do art. 313, V, "a" (RJU-05) ou liquida, expede a certidão de crédito e extingue (RJU-07); a escolha continua em ponto C (C2), agora com as vias reais.

**Quando usar.** Declarada a natureza do crédito (RJU-01, no mesmo ato ou em ato anterior com Id.), é preciso decidir o que acontece com o cumprimento: constrições e valores já nos autos, certidão de crédito, habilitação no juízo universal e andamento da liquidação. Marcos: Id. da declaração de natureza; Id. de bloqueios, depósitos e pedidos de constrição ou de alvará pendentes; Id. da decisão de deferimento do processamento (para contar o prazo do art. 6º, § 4º).

**Portões do ramo.** Portões 1, 4 e 7. Contar, por script (`calculista`), o prazo de 180 (cento e oitenta) dias do art. 6º, § 4º, da Lei nº 11.101/2005 a partir do deferimento do processamento: se já decorreu, o texto do `minutar-decisao-suspensao-sobrestamento` (SUS-05, subramo E), que suspende por 180 dias, não se aplica, e o sobrestamento passa a depender da novação e da habilitação (ponto C). Valor constrito ou depositado: nenhum alvará nem transferência nesta decisão.

**Relatório.** Os eventos do RJU-01 e, em parágrafo próprio, os da constrição: "Em {{data}}, {{o Sisbajud tornou indisponível | foi depositado em garantia}} o valor de R$ {{valor}} ({{extenso}}) (Id. {{id_valor}})." e "Em {{data}}, a parte exequente requereu {{a transferência | o alvará | nova constrição}} (Id. {{id_pedido}})."

**Fundamentação — ordem das questões.** (1) Vedação de constrição e juízo universal; (2) destino do valor já constrito, se houver; (3) certidão de crédito e habilitação; (4) liquidação e andamento. A primeira é sempre a primeira.

Questão 1, constrição: "Passo à análise dos atos de constrição. Declarada a natureza concursal do crédito (item anterior), a parte executada permanece em recuperação judicial desde o deferimento do processamento em {{data}} (Id. {{id_deferimento}}). A matéria é regida pelo art. 6º, incisos II e III, da Lei nº 11.101/2005, que, deferido o processamento, suspende as execuções e proíbe a retenção, o arresto, a penhora, o sequestro, a busca e apreensão e qualquer constrição sobre bens do devedor relativas a créditos sujeitos à recuperação (registro `lei-11101-art-6`; **==transcrição literal a conferir no original, porque o registro não traz o teor==** 🟡 **[REVISAR]**). Nos autos, a parte exequente requereu {{ato}} (Id. {{id_pedido}}) para satisfazer crédito concursal. Conclui-se, portanto, que a satisfação do crédito se faz no juízo da recuperação, por meio da habilitação, e que não cabem neste juízo novas constrições sobre bens da executada para esse fim."

Questão 2, valor já constrito (só se houver): "Passo à análise do valor já constrito. Nos autos, o valor de R$ {{valor}} (Id. {{id_valor}}) {{foi bloqueado em {{data}} | foi depositado em {{data}} em garantia}}. **==DECISÃO RESERVADA — destino do valor: via adotada, desbloquear o valor em favor da executada e extinguir com a certidão de crédito, como no único ato do cofre com valor bloqueado (0001120-93.2018, sentença de 23.03.2026, que acolheu a impugnação à penhora e determinou o levantamento do bloqueio); alternativa, manter o valor vinculado aos autos, sem levantamento, até a comunicação ao juízo da recuperação e a definição por ele (ou, no depósito, mantê-lo em conta judicial vinculada, sem alvará)==** 🔴 **[REVISAR]**. Conclui-se, portanto, que não se defere alvará nem transferência enquanto a natureza do crédito e a competência do juízo universal não estiverem definidas."

Questão 3, certidão e habilitação: "Passo à análise da certidão de crédito. O crédito concursal é habilitado no juízo da recuperação judicial, e a habilitação ou a divergência se apresenta com a indicação do valor atualizado até a data do pedido, da origem e da classificação do crédito. **==Dispositivos da Lei nº 11.101/2005 sobre habilitação e divergência (arts. 7º, § 1º, 9º e 10) a confirmar no registro; nenhum consta==** 🟡 **[REVISAR]**. Nos autos, o título e o trânsito em julgado estão certificados (Id. {{id_transito}}), mas o valor do crédito ainda {{está | não está}} liquidado. Conclui-se, portanto, que a certidão de crédito deve conter o valor liquidado, a data-base e a natureza, para uso na habilitação."

Questão 4, liquidação e andamento: "Passo à análise do andamento do cumprimento. O cumprimento não pode seguir para constrição, mas a liquidação do valor é necessária para instruir a certidão. **==DECISÃO RESERVADA — andamento: via adotada, liquidar o valor (RJU-03), expedir a certidão de crédito e extinguir o cumprimento por sentença (RJU-07), que é o desfecho dado pelo magistrado em cinco atos do cofre (0800160-02, 0001403-92, 0001120-93, 0000604-44 e 9000371-30, este depois de suspenso em 10.03.2025); alternativas, suspender o cumprimento por meio do despacho do RJU-05 (art. 313, V, "a", como no ato 9000371-30 de 10.03.2025) ou prosseguir só na liquidação e suspender os demais atos até a habilitação (via do esqueleto anterior, sem ato do cofre que a adote)==** 🔴 **[REVISAR]**. Conclui-se, portanto, que a liquidação prossegue e os atos de constrição ficam vedados."

**Dispositivo — modelo.**

DISPOSITIVO

Ante o exposto, trilha A (crédito concursal):

1)  **DETERMINO** que a Secretaria se abstenha de registrar ordens de constrição (Sisbajud, Renajud e Infojud) sobre bens da parte executada para satisfação deste crédito, e **INDEFIRO**, por ora, os pedidos de constrição e de alvará de Id. {{id_pedido}}.

2)  [SE há valor constrito] **==DETERMINO o desbloqueio do valor de R$ {{valor}} (Id. {{id_valor}}) em favor da parte executada, com o levantamento do bloqueio pelo sistema, e TORNO SEM EFEITO a ordem de constrição; [alternativa: MANTENHO o valor vinculado aos autos, sem levantamento, até a definição pelo juízo da recuperação judicial, e COMUNIQUE-SE àquele juízo a existência do valor e deste crédito]==** 🔴 **[REVISAR]**.

3)  **DETERMINO** a expedição de certidão de crédito em favor da parte exequente, com o valor liquidado, a data-base (data do pedido de recuperação judicial), a natureza concursal e o Id. do título e do trânsito em julgado, para uso na habilitação ou na divergência perante o juízo da recuperação judicial.

4)  **INTIME-SE** a parte exequente, por seu advogado, para, no prazo de {{N}} ({{extenso}}) dias **==[prazo a confirmar: sem fonte no registro]==** 🟡 **[REVISAR]**, comprovar a habilitação ou a divergência do crédito perante o juízo da recuperação judicial.

5)  **==PROSSIGA-SE apenas na liquidação do valor, nos termos dos parâmetros do RJU-03, e SUSPENDO os demais atos do cumprimento até a comprovação da habilitação, ou até o decurso do prazo do item 4, o que ocorrer primeiro. [Via do cofre: se o magistrado optar pela extinção, substituir os itens 4 a 6 pelo RJU-07; se optar pela suspensão com intimações, usar o despacho do RJU-05.]==** 🔴 **[REVISAR]**.

6)  Decorrido o prazo do item 4, com ou sem manifestação, **CERTIFIQUE** a Secretaria e façam-se os autos conclusos.

Trilha B (crédito não sujeito à recuperação), quando o magistrado decidir pela alternativa do RJU-01:

1)  **DETERMINO** o prosseguimento do cumprimento pelas regras comuns, com os parâmetros do RJU-03 quando houver divergência de cálculo.

2)  **==OFICIE-SE ao juízo da recuperação judicial, com cópia da decisão de Id. {{id_deferimento}} e desta decisão, antes de qualquer ordem de constrição sobre bens da parte executada, e INTIME-SE a parte exequente para requerer o que entender de direito em {{N}} ({{extenso}}) dias==** 🔴 **[REVISAR]**.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Arts. 7º, § 1º, 9º e 10 da Lei 11.101/2005 (habilitação e divergência): sem item no registro. Confirmar em fonte oficial.==**
- 🟡 **==A2 — Prazo da habilitação (item 4): sem fonte no registro. Confirmar ou fixar com base em norma.==**
- 🟢 **==B1 — Ato sem modelo do gabinete: esqueleto 0.1.0.==**
- 🟡 **==B2 — Prazo de 180 dias do art. 6º, § 4º, contado do deferimento (Id.): conferir por script se já decorreu.==**
- 🔴 **==C1 — DECISÃO RESERVADA: destino do valor constrito. Via: desbloquear e restituir (ato 0001120-93, único do cofre com valor bloqueado). Alternativa: manter vinculado, sem alvará.==**
- 🔴 **==C2 — DECISÃO RESERVADA: andamento. Via: liquidar, expedir a certidão e extinguir (RJU-07; cinco atos do cofre). Alternativas: suspensão com intimações (RJU-05, ato 9000371-30 de 10.03.2025) ou só a liquidação com os demais atos suspensos.==**
- 🔴 **==C3 — DECISÃO RESERVADA (trilha B): competência do juízo da recuperação para constrição. Via: ofício prévio. Alternativa: prosseguir.==**

**Encaminhamento seguinte.** RJU-03 para a liquidação; `minutar-decisao-suspensao-sobrestamento` (SUS-05, subramo E) se o magistrado optar pela suspensão total dentro do prazo do § 4º; certificada a habilitação, o ato é de sentença de extinção (→ `minutar-sentenca-extincao-civel`), por decisão do magistrado.

**RJU-03 — Impugnação da recuperanda sobre juros e correção até a data do pedido e novação: parâmetros de cálculo.**

**Cofre (27.10.2026).** COMPLEMENTAÇÃO — sentenças 0001403-92.2013 (16.09.2026: valor atualizado até 20.06.2016, INPC e juros legais da citação, art. 9º, II) e 0800160-02.2021 (29.08.2025: valor consensual atualizado até 01.02.2021) e sentença da falência 0800162-06.2020 (31.08.2026: INPC e 1% ao mês, limitados à data da quebra), íntegras lidas; sem modelo do PJe — o termo final do crédito concursal na data do pedido (Q1) é o que o magistrado adotou, mas a data varia entre os atos do Grupo Oi (01/03/2023 no ato 9000371-30, conforme o Aviso nº 39/2023; 20/06/2016 no ato 0001403-92; 21/10/2016 no ato 0000604-44, por valor consensual), o que mantém o ponto C; a multa e os honorários (Q4) aparecem de formas diferentes e ganham o registro das vias.

**Quando usar.** A executada pede que juros e correção monetária sejam calculados só até a data do pedido de recuperação judicial, ou impugna o termo inicial dos juros, a cumulação com a SELIC ou o termo final; ou a Contadoria devolveu os autos sem cálculo pedindo essas definições. Marcos: Id. da impugnação e do demonstrativo; Id. da decisão anterior de parâmetros e da certidão da Contadoria, se houver.

**Portões do ramo.** Portões 1, 3 e 8. Depende da natureza declarada (RJU-01): no crédito concursal, o termo final é a data do pedido; no extraconcursal, segue-se a regra comum do termo final (dia exato em que a planilha ou o laudo foi gerado, posicionamento ratificado em 22.10.2026, `minutar-decisao-complementar-pos-contadoria`). Sem natureza declarada, não se fixa termo final.

**Relatório.** Os eventos do RJU-01 que importam para o cálculo, mais: "Em {{data}}, a parte executada declarou como devido o valor de R$ {{valor}}, com atualização até {{data}} (Id. {{id_calculo_executada}})." e "Em {{data}}, a parte exequente apresentou demonstrativo de R$ {{valor}}, atualizado até {{data}} (Id. {{id_demonstrativo}})."

**Fundamentação — ordem das questões.** (1) Termo final dos juros e da correção; (2) termo inicial e taxa dos juros; (3) correção e transição legal; (4) multa e honorários do art. 523, § 1º; (5) remessa ou escada da regra 91.

Questão 1, termo final: "Passo à análise do termo final dos juros e da correção. O crédito concursal é habilitado com o valor atualizado até a data do pedido de recuperação judicial, formulado em {{data_pedido}} (Id. {{id_deferimento}}). **==A matéria é regida pelo art. 9º, inciso II, da Lei nº 11.101/2005, que exige, na habilitação, o valor do crédito atualizado até a data do pedido de recuperação judicial; dispositivo a confirmar no registro, que não o traz==** 🟡 **[REVISAR]**. Nos autos, o crédito é concursal (declaração do ato) e o demonstrativo da parte exequente (Id. {{id_demonstrativo}}) atualiza o valor até {{data}}, depois do pedido. Conclui-se, portanto, que **==DECISÃO RESERVADA — termo final no crédito concursal: via adotada, a data do pedido de recuperação judicial; alternativa, a data da liquidação, deixando ao juízo da recuperação a definição dos encargos posteriores==** 🔴 **[REVISAR]**."

Questão 2, juros: "Passo à análise dos juros. O título fixou {{taxa}} com termo inicial em {{termo_inicial}} (Id. {{id_titulo}}, p. {{p}}). A matéria é regida pelo que o título decidiu, que não se rediscute na fase de cumprimento. Nos autos, o demonstrativo da parte exequente aplicou o termo inicial de {{data}} (Id. {{id_demonstrativo}}), e a parte executada sustenta {{data}} (Id. {{id_impugnacao}}). Conclui-se, portanto, que o termo inicial dos juros é {{data}}, conforme o título. [SE o título é omisso, escrever: ==termo inicial dos juros não definido no título (Id.); DECISÃO RESERVADA == 🔴 **[REVISAR]**]"

Questão 3, correção e transição legal: aplicar o bloco de transição da Lei nº 14.905/2024 dos blocos da `contadoria-diagnostico-e-minutas` e a fórmula única do `parametros_AD.json` (`tema_677_formula`) quando houver depósito. A cumulação de juros com a SELIC é decidida pelo bloco de transição; fora dele, ponto C. Texto: "Passo à análise da correção monetária e da taxa legal. A correção incide {{índice}} desde {{termo_inicial_correcao}}, conforme o título (Id. {{id_titulo}}), e a taxa legal do período posterior segue o bloco de transição da Lei nº 14.905/2024 **==(texto do bloco a incluir pela skill contadoria-diagnostico-e-minutas; registro cc-389-406-lei-14905 para a taxa legal)==** 🟡 **[REVISAR]**. Conclui-se, portanto, que {{proposição}}."

Questão 4, multa e honorários do art. 523, § 1º: "Passo à análise da multa e dos honorários do art. 523, § 1º, do Código de Processo Civil. A multa e os honorários de 10% incidem, nos termos do art. 523 (registro `cpc-523`), se não houver pagamento voluntário no prazo, contado da intimação para pagar (Id. {{id_intimacao}}). **==DECISÃO RESERVADA — natureza da multa e dos honorários: via adotada, tratá-los como acessórios do crédito principal, com o mesmo termo final; alternativa, considerá-los posteriores ao pedido de recuperação (se a intimação para pagar for posterior a {{data_pedido}}) e, portanto, não sujeitos==** 🔴 **[REVISAR]**. Quanto aos honorários da impugnação, o cofre mostra três soluções nos atos de recuperação: 10% sobre o proveito econômico da impugnação acolhida, a cargo do exequente (0800160-02, 29.08.2025; 0000604-44, 29.09.2025); honorários de 10% sobre o excesso reconhecido, a cargo do exequente, com exigibilidade suspensa pela gratuidade (9000371-30, 23.01.2026); e nenhum honorário na impugnação, por conformidade da liquidação e concordância do credor (0001403-92, 16.09.2026). **==A escolha entre elas é do magistrado; o texto adota a que o caso real indicar e a registra==** 🔴 **[REVISAR]**."

Questão 5: remessa. "Passo à análise da via de apuração do valor. **==Nenhum dos cálculos aplica todos os parâmetros do título (Id.), e o valor não se declara com segurança nesta decisão==** 🟡 **[REVISAR]**. Conclui-se, portanto, que a apuração depende de novo demonstrativo ou de cálculo da Contadoria Judicial Única, na escada da regra 91." Se o valor se declara com segurança (degraus 1 e 2), a conclusão é a do IMP-03 ou do degrau 2 (script, ponto B).

**Dispositivo — modelo.**

DISPOSITIVO

Ante o exposto,

1)  **FIXO** os seguintes parâmetros para o cálculo do crédito, conforme o título (Id. {{id_titulo}}): a) principal: {{base}}; b) correção monetária: {{índice}}, desde {{termo_inicial}}; c) juros: {{taxa}}, desde {{termo_inicial_juros}}; d) transição legal: bloco da Lei nº 14.905/2024; e) termo final: **==a data do pedido de recuperação judicial ({{data_pedido}}), se o crédito for concursal; ou o dia em que a planilha ou o laudo for gerado, se extraconcursal==** 🔴 **[REVISAR]**; f) multa e honorários do art. 523, § 1º: **==conforme a decisão reservada==** 🔴 **[REVISAR]**.

2)  **DETERMINO** a intimação das partes para ciência e manifestação sobre os parâmetros, no prazo de até 5 (cinco) dias, e **CONSTE** na intimação que a oposição sem fundamento no título será considerada litigância de má-fé ou ato atentatório à dignidade da justiça. Havendo oposição, **CONCLUAM-SE** os autos.

3)  Sem oposição, **INTIME-SE** a parte exequente para, querendo, no prazo de até 15 (quinze) dias, apresentar cálculos atualizados segundo estes parâmetros; apresentados, **INTIME-SE** a parte executada, em 15 (quinze) dias, para manifestar-se sobre a concordância (BLOCO-CALC, regra 91; **==pagamento só se o crédito for extraconcursal; no concursal, a manifestação serve à certidão de crédito==** 🔴 **[REVISAR]**).

4)  Decorrido o prazo sem cálculos, ou havendo desinteresse expresso do exequente, **CERTIFIQUE** a Secretaria e **REMETAM-SE** imediatamente os autos à Contadoria Judicial Única, que observará rigorosamente os parâmetros desta decisão. [SE a Contadoria já devolveu os autos sem cálculo: a remessa é direta, sem a faculdade do item 3, no texto literal de COMP-C (`minutar-decisao-complementar-pos-contadoria`, `references/ramos/COMP-C.md`), com os parâmetros acima no lugar dos genéricos.]

5)  **CONSIGNO** que não serão expedidos alvarás até a definição do valor.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Art. 9º, II, da Lei 11.101/2005 (atualização até o pedido): sem item no registro. Confirmar em fonte oficial.==**
- 🟡 **==A2 — Bloco de transição da Lei 14.905/2024: conferir a versão atual na contadoria-diagnostico-e-minutas.==**
- 🟢 **==B1 — Ato sem modelo do gabinete: esqueleto 0.1.0.==**
- 🟢 **==B2 — Contadoria Judicial Única (rito comum), regra 91. Demonstrativo em imagem: checagem manual.==**
- 🔴 **==C1 — DECISÃO RESERVADA: termo final do crédito concursal. Via: data do pedido. Alternativa: data da liquidação.==**
- 🔴 **==C2 — DECISÃO RESERVADA: multa e honorários do art. 523, § 1º, no crédito em recuperação. Via: acessórios. Alternativa: posteriores ao pedido.==**
- 🔴 **==C3 — DECISÃO RESERVADA: honorários da impugnação. O cofre tem 10% contra o exequente, 10% com exigibilidade suspensa e nenhum honorário (atos 0800160-02, 9000371-30 e 0001403-92).==**

**Encaminhamento seguinte.** Contadoria Judicial Única; juntada a conta, `minutar-homologacao-calculos` (H1 ou H2). No crédito concursal, a homologação serve à certidão de crédito, e o pagamento se dá no juízo da recuperação.

**RJU-04 — Gratuidade da justiça da pessoa jurídica em recuperação, formulada na impugnação e não apreciada (sequência; o capítulo é de outra skill).**

**Cofre (27.10.2026).** SEM CORRESPONDENTE — nenhum modelo ou ato do cofre lido trata da gratuidade da pessoa jurídica em recuperação judicial formulada na impugnação; a nota de entendimentos de Execução de Título Extrajudicial (gerada por IA, só indício) registra o indeferimento da gratuidade da pessoa jurídica com base na Súmula 481 do STJ, em outro contexto — o ramo fica como está.

**Quando usar.** A executada em recuperação judicial pede, na impugnação, a gratuidade da justiça ou o diferimento das custas, e o pedido não foi apreciado (ainda que o juízo já a tenha intimado para recolher as custas da impugnação sem decidir o pedido). Marcos: Id. do pedido de gratuidade; Id. da intimação anterior para as custas e a data da ciência; Id. das provas de insuficiência juntadas; Id. de petição posterior que cobre a decisão.

**Portões do ramo.** Portões 1 e 6. Este ramo NÃO redige o capítulo da gratuidade. O capítulo é o GRAT-05 da skill `minutar-decisao-gratuidade` (arquivo `references/partes/fundamentos-e-modelos/06-grat-05-pessoa-j.md`), que o redator convoca e copia com suas variáveis, sem reescrita: fundamentação comum (art. 98 do CPC, Súmula 481 do STJ, registro `stj-sumula-481`, e Tema 1.424 do STJ, registro `stj-tema-1424`, cuja tese literal e a lista de demonstrativos ainda estão a confirmar no registro) e um dos subramos 05-A (intimação para comprovar), 05-B (indeferimento) ou 05-C (deferimento). A recuperação judicial, por si, não comprova a insuficiência: a comprovação é a dos esclarecimentos sobre a situação financeira e patrimonial exigidos pelo Tema 1.424 (ponto C se a prova for apenas a decisão de deferimento do processamento ou a queda de faturamento).

**Relatório.** Eventos do RJU-01 que importam e, em parágrafos próprios: "Em {{data}}, a parte executada impugnou o cumprimento e pediu a gratuidade da justiça ou o diferimento das custas (Id. {{id_impugnacao}})." "Em {{data}}, a decisão de Id. {{id_decisao_custas}} intimou a parte executada para recolher as custas da impugnação em 15 (quinze) dias, sem apreciar o pedido." "Em {{data}}, a parte executada pediu decisão expressa sobre a gratuidade e a suspensão da exigência das custas (Id. {{id_pedido_decisao}})." "Em {{data}}, a parte exequente {{se manifestou | não se manifestou}} sobre o pedido (Id. {{id_resposta}})."

**Fundamentação — ordem das questões.** (1) Gratuidade da justiça, decidida antes de qualquer questão de mérito da impugnação; (2) custas da impugnação, só se a gratuidade for indeferida; (3) mérito (RJU-01 a RJU-03), só se a gratuidade for deferida ou se as custas forem recolhidas.

Questão 1: "Passo à análise do pedido de gratuidade da justiça." Em seguida, o parágrafo-âncora e a subsunção do subramo GRAT-05 aplicável, copiados da skill `minutar-decisao-gratuidade` (05-A se a prova não traz os esclarecimentos do Tema 1.424; 05-B se, intimada, a parte não os trouxe ou os trouxe insuficientes; 05-C se os trouxe). Escolha pelo estado dos autos: sem intimação prévia para comprovar a insuficiência (art. 99, § 2º, do CPC, registro `cpc-98-102`), sempre 05-A, porque o indeferimento sem ela é vedado. Intimação anterior apenas para custas não vale como intimação para comprovar a insuficiência.

Questão 2 (só se 05-B): "Passo à análise das custas da impugnação. Indeferida a gratuidade, as custas de ingresso da impugnação são devidas. A matéria é regida pelo art. 290 do Código de Processo Civil (registro `cpc-290`), segundo o qual será cancelada a distribuição do feito se a parte, intimada na pessoa de seu advogado, não pagar as custas de ingresso em 15 (quinze) dias.

Aplica-se ao caso o Tema 675 do Superior Tribunal de Justiça (registro `stj-tema-675`), segundo a tese firmada: 'Cancela-se a distribuição da impugnação ao cumprimento de sentença ou dos embargos à execução na hipótese de não recolhimento das custas no prazo de 30 dias, independentemente de prévia intimação da parte.' No caso, a parte executada pediu a gratuidade na impugnação e o pedido só é decidido agora, o que se enquadra no uso delimitado do tema, com prazo de 15 (quinze) dias e intimação do advogado, conforme o posicionamento ratificado em 22.10.2026. Nos autos, a intimação de Id. {{id_decisao_custas}} não apreciou o pedido de gratuidade.

Conclui-se, portanto, que **==DECISÃO RESERVADA — reabertura do prazo: via adotada, novo prazo de 15 dias a contar da intimação desta decisão, sem considerar o prazo anterior; alternativa, aproveitar o prazo anterior==** 🔴 **[REVISAR]**."

**Dispositivo — modelo.**

DISPOSITIVO

Ante o exposto,

1)  Itens do subramo GRAT-05 aplicável (05-A, 05-B ou 05-C), copiados da skill `minutar-decisao-gratuidade`, na ordem dela. No 05-B, a última frase (conclusos para sentença de extinção) é trocada por "façam-se os autos conclusos para decidir o cancelamento da distribuição da impugnação" **==(ponto B: adaptação do 05-B, que trata de custas iniciais, às custas da impugnação)==** 🟡 **[REVISAR]**, e o prazo e a consequência do item de custas são os do art. 290 do CPC.

2)  [SE 05-A] A impugnação não é apreciada neste ato; **==DETERMINO que o prazo das custas fique sem curso até a decisão sobre a gratuidade==** 🔴 **[REVISAR]**.

3)  [SE 05-C] **PROSSIGA-SE** o feito com o mérito da impugnação, nos termos dos itens do RJU-01 a RJU-03, no mesmo ato ou em ato seguinte, conforme o estado dos autos.

4)  [SE 05-B] Decorrido o prazo sem o comprovante das custas, **CERTIFIQUE** a Secretaria e façam-se os autos conclusos para o cancelamento da distribuição da impugnação (→ `contadoria-diagnostico-e-minutas`, IMP-07). Comprovado o recolhimento, **PROSSIGA-SE** com o mérito (RJU-01 a RJU-03).

**Sequência (definida por este ramo).**

1.  Gratuidade primeiro: nenhuma questão de mérito da impugnação é decidida antes dela.
2.  Sem prova dos esclarecimentos do Tema 1.424: GRAT-05, subramo 05-A (intimar para comprovar, 15 dias); o mérito aguarda.
3.  Prova insuficiente depois da intimação: 05-B (indeferir e intimar para as custas, 15 dias, art. 290; novo prazo, ponto C).
4.  Prova suficiente: 05-C (deferir) e mérito (RJU-01 a RJU-03).
5.  Custas não recolhidas no prazo: cancelamento da distribuição da impugnação (IMP-07; Tema 675, uso delimitado). O cumprimento prossegue, com a natureza do crédito resolvida de ofício? **==DECISÃO RESERVADA — cancelada a impugnação, a natureza concursal, que o juízo da recuperação pode reconhecer, ainda pode ser conhecida de ofício neste juízo? Via adotada: sim, quando constar dos autos o deferimento do processamento (Id.) e o RJU-02 impedir constrição; alternativa, não conhecer e prosseguir pelo cumprimento comum==** 🔴 **[REVISAR]**.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Tema 1.424/STJ: tese literal e lista de demonstrativos não lidas em fonte oficial (registro). Conferir antes de citar a tese.==**
- 🟢 **==B1 — Ato sem modelo do gabinete: esqueleto 0.1.0. Capítulo da gratuidade copiado de GRAT-05, sem reescrita.==**
- 🟡 **==B2 — Subramo 05-B adaptado às custas da impugnação (original trata de custas iniciais).==**
- 🔴 **==C1 — DECISÃO RESERVADA: reabertura do prazo das custas. Via: novo prazo de 15 dias. Alternativa: aproveitar o prazo anterior.==**
- 🔴 **==C2 — DECISÃO RESERVADA: conhecer de ofício a concursalidade se a impugnação for cancelada. Via: sim. Alternativa: não.==**

**Encaminhamento seguinte.** Gratuidade deferida ou custas recolhidas: RJU-01 a RJU-03. Custas não recolhidas: `contadoria-diagnostico-e-minutas`, IMP-07. Pedido de diferimento ou parcelamento das custas, em vez de gratuidade total: `minutar-decisao-gratuidade`, GRAT-04.

**RJU-05 — Suspensão do cumprimento em razão da recuperação judicial, com intimações (despacho).**

**Cofre (27.10.2026).** ADOÇÃO — despacho assinado `AD_DEC_suspensão_recuperação judicial`, processo 9000371-30.2012.8.10.0131 (10.03.2025), íntegra lida em `Atos do Juízo/Íntegras/2025`; não é modelo vigente do PJe, e sim ato assinado do magistrado — o texto passa a seguir o ato, com os marcadores `{{...}}` e as fórmulas finais do gabinete; a espécie do ramo é DESPACHO (`<CNJ>_AD_DESP_...`).

**Quando usar.** Executada em recuperação judicial provada nos autos (Id.) e o magistrado opta por suspender o cumprimento, em vez de decidir a natureza do crédito (RJU-01) ou de extinguir (RJU-07). Marcos: Id. do deferimento do processamento e, se houver, da informação da recuperação nos autos.

**Portões do ramo.** Portões 1 e 2. O ato do cofre foi proferido em processo que ainda tinha classe de Juizado Especial e mandou evoluir a classe para cumprimento de sentença; se o cadastro for de Juizado, o portão 2 manda para `decidir-rito-e-competencia-do-cadastro`. **==O enquadramento no art. 313, V, "a", do CPC é o do ato do cofre (registro cpc-313, que confirma o artigo e não o enquadramento); conferir a aptidão da hipótese à recuperação judicial antes de assinar==** 🟡 **[REVISAR]**.

**Relatório.** Dispensado. O despacho não tem relatório.

**Fundamentação.** Nenhuma. O ato do cofre é despacho sem fundamentação própria, e o fundamento é a remissão ao art. 313, V, "a".

**Texto do despacho (adoção do ato do cofre).**

DESPACHO

{{SE a classe ainda não for de cumprimento de sentença:}} Proceda-se à evolução da classe processual para cumprimento de sentença.

Diante da recuperação judicial da parte executada (Id. {{id_deferimento}}), **SUSPENDO** o processo (art. 313, V, "a", do CPC).

**INTIME(M)-SE** a(s) parte(s) exequente(s), por meio de advogado(a) constituído(a), para que promova(m) o regular andamento do processo, no prazo de até 5 (cinco) dias, sob pena de extinção.

Permanecendo inerte(s), **INTIME(M)-SE** a(s) parte(s) exequente(s), pessoalmente, para que promova(m) o regular andamento do processo, no prazo de até 5 (cinco) dias, sob pena de extinção.

Na mesma oportunidade, **INTIME(M)-SE** a(s) parte(s) executada(s), por meio de advogado(s) constituído(s), para que manifeste(m) interesse no prosseguimento do processo, no prazo de até 5 (cinco) dias.

Cumpra-se o Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes.

Proceda-se à revisão da classe processual e/ou do assunto da autuação, se necessário e caso não tenha feito previamente.

Imponho força de mandado de intimação no Pje e de edital de intimação a este ato.

Cumpra-se. Intimem-se.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Art. 313, V, "a", do CPC como fundamento da suspensão por recuperação judicial: enquadramento do ato do cofre; conferir.==**
- 🟡 **==A2 — O ato do cofre usa "Imponho força de mandado de citação/intimação às partes a este ato judicial, desde que os endereços... estejam atualizados"; aqui entrou a fórmula do gabinete (intimação no Pje e edital de intimação). Conferir qual o magistrado quer.==**
- 🟢 **==B1 — Prazo de 5 dias nas três intimações: copiado do ato do cofre.==**
- 🔴 **==C1 — DECISÃO RESERVADA: suspender (este ramo) ou decidir a natureza e extinguir com certidão (RJU-01 e RJU-07). O cofre tem as duas vias, e no processo 9000371-30 a suspensão de 10.03.2025 foi seguida da sentença de extinção de 23.01.2026.==**

**Encaminhamento seguinte.** Cumpridas as intimações, nova conclusão: RJU-07 (extinção com certidão de crédito) ou, se a executada manifestar interesse e a recuperação se encerrar, retomada do cumprimento pelas skills de cumprimento.

**RJU-06 — Falência da executada: vista ao exequente sobre a quebra e o interesse na certidão de crédito.**

**Cofre (27.10.2026).** ADOÇÃO — decisão assinada 0800162-06.2020.8.10.0131 (24.04.2026, "Falência da executada — intimação"), íntegra lida em `Atos do Juízo/Íntegras/2026`; ato assinado, sem modelo vigente do PJe — o texto segue o ato; o desfecho do mesmo processo (sentença de 31.08.2026) alimenta o RJU-07.

**Quando usar.** Juntada aos autos de prova de que a executada foi declarada falida (Id.), sem manifestação do exequente sobre o fato. Marcos: Id. do documento que noticia a quebra; data da decretação; última intimação da executada.

**Portões do ramo.** Portões 2, 5 e 10. **==O cofre registra datas diferentes para a decretação da falência do mesmo processo: 03/02/2020 ("data de situação especial", na decisão de 24.04.2026) e 03/02/2025 (na sentença de 31.08.2026); conferir no documento de Id. antes de qualquer data no ato, porque ela é o termo final do crédito==** 🟡 **[REVISAR]**. O comprovante cadastral da Receita Federal é prova secundária da quebra.

**Relatório.** Dispensado: "O relatório é dispensável. Decido."

**Fundamentação — ordem das questões.** (1) Efeito da falência e competência do juízo universal; (2) contraditório. Sem subtópicos.

"Compulsando os autos, verifica-se a juntada de {{documento}} (Id. {{id_documento}}), o qual noticia a alteração do status jurídico da empresa executada para "falido", com data de situação especial em {{data_decretacao}}. Nesse sentido, a decretação da falência atrai a competência do juízo falimentar, sendo este o foro indivisível e universal para a satisfação dos créditos contra a massa, nos termos do art. 76 da Lei nº 11.101/2005 **==(art. 76 a conferir; o registro só traz o art. 6º)==** 🟡 **[REVISAR]**. Tal circunstância, em tese, obsta o prosseguimento de atos executórios neste juízo, impondo a habilitação do crédito no juízo universal."

"Todavia, em observância ao princípio da não surpresa e ao dever de consulta (arts. 9º e 10 do Código de Processo Civil; registro `cpc-10` para o art. 10), faz-se indispensável facultar à parte exequente o pronunciamento sobre fatos ou fundamentos que possam alterar o curso do processo."

**Dispositivo — modelo.**

DISPOSITIVO

Ante o exposto,

1)  **INTIME-SE** a parte exequente, por meio de seu patrono, para que, no prazo de 15 (quinze) dias, manifeste-se sobre o documento de Id. {{id_documento}}, o qual indica a falência da executada;

2)  No mesmo prazo, deverá a parte exequente dizer se possui interesse na expedição de certidão de crédito para fins de habilitação perante o juízo da falência;

3)  Transcorrido o prazo com manifestação, **VOLTEM-ME** os autos conclusos para decisão. Em caso de inércia, **CERTIFIQUE-SE** e venham os autos conclusos para extinção ou suspensão, conforme o caso.

Cumpra-se o Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes.

Imponho força de mandado de intimação no Pje e de edital de intimação a este ato.

Cumpra-se. Intimem-se.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Art. 76 da Lei 11.101/2005: sem item no registro (só o art. 6º). Confirmar em fonte oficial.==**
- 🟡 **==A2 — Data da decretação da falência: o cofre tem 03/02/2020 e 03/02/2025 para o mesmo processo. Conferir no documento.==**
- 🟢 **==B1 — Prazo de 15 dias e a alternativa "extinção ou suspensão" na inércia: copiados do ato do cofre.==**
- 🟡 **==B2 — Regra 53, item 3 ("não minutar" falência): divergente do ato do cofre. Confirmar a aplicação.==**
- 🔴 **==C1 — DECISÃO RESERVADA: na inércia ou após a manifestação, extinção (RJU-07) ou suspensão. O cofre tem a extinção com certidão no mesmo processo (sentença de 31.08.2026).==**

**Encaminhamento seguinte.** Manifestada a concordância com a certidão, RJU-07 (sentença de extinção). Inércia: certidão da Secretaria e conclusão, por decisão do magistrado.

**RJU-07 — Sentença de extinção com certidão de crédito (orientação à** `minutar-sentenca-extincao-civel`**).**

**Cofre (27.10.2026).** COMPLEMENTAÇÃO (orientação) — sentenças assinadas 0001403-92.2013 (16.09.2026), 0800160-02.2021 (29.08.2025), 0800162-06.2020 (31.08.2026, falência), 0001120-93.2018 (23.03.2026), 0000604-44.2016 (29.09.2025) e 9000371-30.2012 (23.01.2026), íntegras lidas; sem modelo do PJe — este módulo não redige a sentença, que é da `minutar-sentenca-extincao-civel`; ele fornece os parâmetros que o cofre mostra e as vias a decidir.

**Quando usar.** Crédito liquidado e valor homologado ou concordado (recuperação judicial), ou executada falida com manifestação do exequente sobre a certidão (falência), e o magistrado decide extinguir o cumprimento e entregar a certidão de crédito.

**Portões do ramo.** Portões 1, 4 e 10. A natureza do crédito (RJU-01) e o valor (RJU-03) devem estar decididos, no mesmo ato ou em ato anterior com Id.

**Parâmetros que o cofre mostra, para transmitir à skill de extinção.** Recuperação judicial: extinção do cumprimento com fundamento no art. 924, II (0800160-02 e 0000604-44), II e III c/c art. 59 da Lei nº 11.101/2005 (0001403-92), III c/c art. 59 (0001120-93) ou III (9000371-30), todos do CPC; valor homologado e atualizado até a data do pedido de recuperação (20/06/2016 no ato 0001403-92) ou até a data que as partes aceitaram (01/02/2021 no ato 0800160-02; 21/10/2016 no ato 0000604-44) ou ainda até 01/03/2023, conforme o Aviso nº 39/2023 (ato 9000371-30); ordem à Secretaria de expedir a certidão de crédito em favor do exequente, com o Id. do título, para habilitação no juízo da recuperação (processo e juízo citados no ato); ressalva de que os créditos concursais serão pagos na forma do plano. Falência: extinção sem resolução do mérito, por perda superveniente do interesse processual (art. 485, VI, do CPC, c/c arts. 6º, § 1º, 76 e 9º da Lei nº 11.101/2005), certidão de crédito com principal e honorários discriminados e atualizados pelos índices do título até a data da decretação da quebra (art. 9º, II, c/c art. 124, caput), indeferimento do pedido de remessa dos autos ao juízo falimentar (a habilitação é iniciativa do credor, perante o administrador judicial ou o juízo universal) e certificação do trânsito e arquivamento. Em ambos: custas e honorários conforme o caso (ver C2). O art. 924, II e III, do CPC consta do registro (`cpc-924-ii` e `cpc-924`); os arts. 9º, 59, 76 e 124 e o art. 6º, § 1º, da Lei nº 11.101/2005 **==não constam do registro (que traz o art. 6º sem o teor) e ficam a confirmar==** 🟡 **[REVISAR]**.

**Pontos a revisar típicos.**

- 🟡 **==A1 — Arts. 9º, 59, 76 e 124 da Lei 11.101/2005: sem item no registro. Confirmar em fonte oficial.==**
- 🟡 **==A2 — Fundamento da extinção: art. 924, II, III ou ambos (recuperação; cinco atos com combinações diferentes) ou art. 485, VI (falência, ato 0800162-06). Conferir qual o magistrado adota.==**
- 🟢 **==B1 — A redação da sentença é da minutar-sentenca-extincao-civel: este ramo só leva os parâmetros.==**
- 🔴 **==C1 — DECISÃO RESERVADA: extinguir com a certidão (cinco atos do cofre) ou manter suspenso (RJU-05).==**
- 🔴 **==C2 — DECISÃO RESERVADA: custas e honorários na extinção. O cofre tem custas finais pela executada com exigibilidade conforme o plano e sem honorários na impugnação (0001403-92), custas pela executada e honorários de 10% do proveito contra o exequente (0800160-02 e 0000604-44), e honorários de 10% do excesso contra o exequente com exigibilidade suspensa (9000371-30); o ato 0001120-93 não trata de honorários.==**

**Encaminhamento seguinte.** `minutar-sentenca-extincao-civel`, com os parâmetros acima. Certificado o trânsito, a Secretaria cumpre a certidão de crédito e arquiva.

## Normas, precedentes e pesquisa obrigatória antes de redigir

Nenhum número de artigo, tema ou súmula é afirmado de memória. Antes de redigir, o redator consulta `normas-conferidas.json` (a cópia de `_Gabinete IA/Padrões/` do cofre prevalece): item confirmado entra pelo id; item sem registro, vencido ou conferido só por intermediário vai ao `pesquisador-vigencia` antes do fecho (regra 36); o que não se confirmar fica "a confirmar", com um único ponto A pelo `ponto_a_padrao` (regra 52).

Do registro, usados neste módulo: `lei-11101-art-6` (art. 6º, I a III e §§ 4º e 4º-A, da Lei nº 11.101/2005; confirmado em 23.10.2026, sem o teor transcrito: ponto A para a transcrição literal); `cpc-523` (multa e honorários de 10%); `cpc-525-p1-p4-p5` (excesso e causa extintiva superveniente); `cpc-507` (preclusão); `cpc-10` (contraditório); `cpc-98-102` (gratuidade); `stj-sumula-481` e `stj-tema-1424` (gratuidade da pessoa jurídica; a tese literal do Tema 1.424 está a confirmar); `cpc-290` e `stj-tema-675` (custas e cancelamento da distribuição); `ma-lei-12193-2023-art-6-p3` (cancelamento da distribuição por falta de custas de ingresso); `stj-tema-677-revisado` (depósito em garantia); `cc-389-406-lei-14905` (taxa legal, transição da Lei nº 14.905/2024).

A confirmar (nenhum consta do registro; vão à seção "Normas a incluir no registro"): arts. 49, caput, 59, caput, 9º, II, 7º, § 1º, e 10, 76 e 124 da Lei nº 11.101/2005; Aviso nº 39/2023 do TJRJ (créditos do Grupo Oi); Tema 1.051 do STJ (fato gerador como critério de sujeição à recuperação judicial; aparece citado na triagem e no IMP-03); entendimento do STJ sobre a competência do juízo da recuperação para atos de constrição sobre bens da recuperanda quando o crédito é extraconcursal. Enquanto não confirmados, a minuta os escreve com o marcador e o ponto A, sem transcrever a tese.

## Documentos prioritários (ordem de leitura do extrator)

- capa (classe, rito, partes)
- decisão de deferimento do processamento da recuperação judicial e petição do pedido (data)
- decisão de homologação ou concessão do plano e o plano (anexos lidos)
- sentença e acórdão (fato gerador, parâmetros e trânsito)
- prova do fato gerador (contrato, evento, comunicação)
- documento que noticia a falência (sentença de quebra, certidão do juízo falimentar ou comprovante cadastral), com a data da decretação
- requerimento de cumprimento e demonstrativo do exequente
- impugnação da executada, com o demonstrativo, e resposta do exequente
- pedido de gratuidade e documentos de insuficiência
- decisão que intimou para custas e petição posterior
- certidão ou informação da Contadoria
- extratos de bloqueio e comprovantes de depósito

## Parâmetros repetíveis (conferência de divergência, regra 22)

- via adotada sobre a natureza do crédito (concursal por fato gerador anterior ao pedido)
- desfecho do cumprimento da executada em recuperação (liquidar, certidão e extinção; ou suspensão com intimações de 5 dias)
- prazo de 15 dias ao exequente na falência da executada, com a pergunta sobre a certidão de crédito
- destino do valor constrito (vinculado, sem alvará)
- andamento (só a liquidação, atos suspensos até a habilitação)
- termo final do crédito concursal (data do pedido)
- prazo da habilitação e da manifestação sobre os parâmetros
- tratamento da multa e dos honorários do art. 523, § 1º
- prazo e reabertura das custas da impugnação
- fórmula do Tema 677/STJ (`parametros_AD.json`) e bloco de transição da Lei 14.905/2024

## Dados essenciais (regra 24)

- data do pedido e do deferimento do processamento, com Id.
- falência: documento, Id. e data da decretação (termo final do crédito)
- plano homologado: data e Id., e se o anexo foi lido
- fato gerador do crédito: data e Id. da prova
- trânsito em julgado e data da sentença, com Id.
- valores constritos ou depositados, com Id., data e natureza
- decisão do juízo da recuperação sobre o crédito, se houver
- pedido de gratuidade, provas de insuficiência e intimação de custas, com Id.
- demonstrativos das partes e parâmetros do título (índice, taxa, termos), com Id. e página

## Especialistas e cálculo

O roteiro inclui o `calculista` e o `pesquisador-vigencia`. O `calculista` conta o prazo do art. 6º, § 4º, a partir do deferimento do processamento, refaz por script os demonstrativos e apura os valores conforme o termo final decidido; o redator incorpora `onda/calculo_<CNJ>.md` sem recalcular. O `pesquisador-vigencia` confere em fonte oficial os itens "a confirmar" (Lei nº 11.101/2005, arts. 9º, 49, 59, 7º e 10; Tema 1.051/STJ) e a tese do Tema 1.424 antes do fecho. Contadoria: Judicial Única, no rito comum (regra 91).

## Nomenclatura

`<CNJ completo>_AD_DEC_<assunto>_<especificação>`, em minúsculas com acentos, sem data (regra 06; `shared/nucleo/scripts/nomear_minuta.py`). Exemplos: `0000000-00.0000.8.10.0000_AD_DEC_recuperação judicial_natureza do crédito`; `..._AD_DEC_recuperação judicial_parâmetros de cálculo`; `..._AD_DEC_recuperação judicial_gratuidade e custas`. O RJU-05 é despacho: `..._AD_DESP_recuperação judicial_suspensão`. O RJU-06 é decisão: `..._AD_DEC_falência da executada_intimação`. Repetição numerada (1, 2, 3); inteiro teor com o sufixo "_inteiro teor".

## Posicionamentos e decisões reservadas

Reservado ao magistrado, sempre em ponto C (via adotada e alternativa): a natureza do crédito (concursal ou não); suspender (RJU-05) ou extinguir com certidão (RJU-07) o cumprimento da executada em recuperação ou falida; os honorários e as custas na extinção; o efeito da novação pelo plano sobre o cumprimento; o destino do valor já constrito; o andamento do cumprimento (só liquidação, suspensão total ou extinção após a habilitação); a competência do juízo da recuperação para constrição em crédito extraconcursal; o termo final do crédito concursal; o tratamento da multa e dos honorários do art. 523, § 1º; a reabertura do prazo das custas; e o conhecimento de ofício da concursalidade se a impugnação for cancelada.

Posicionamentos ratificados aplicados sem ponto C: custas da impugnação pelo art. 290 do CPC, com intimação do advogado e prazo de 15 dias (Tema 675 só no uso delimitado); termo final do cálculo no dia exato em que a planilha ou o laudo for gerado, no crédito comum; depósito em garantia do juízo, salvo prova de pagamento, e Tema 677/STJ; nenhum alvará antes da definição do valor (trava 13.1). A minuta nunca decide a concursalidade como conclusão definitiva: o redator marca a via adotada e deixa a assinatura ao magistrado.
