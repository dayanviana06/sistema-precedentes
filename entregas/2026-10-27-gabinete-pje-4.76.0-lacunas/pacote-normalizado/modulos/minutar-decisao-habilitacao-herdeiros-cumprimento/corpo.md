# Habilitação de herdeiros e sucessão processual no cumprimento de sentença

## Finalidade

Decidir, em atos próprios e com esqueleto padronizado, o óbito de parte no cumprimento de sentença contra executado particular (rito comum, família AD): a prova do óbito noticiado e não confirmado (HAB-01, despacho); o recebimento do pedido de habilitação e a intimação ou citação da parte contrária (HAB-02, despacho); a decisão que defere a habilitação de um ou de vários sucessores, define a representação, declara a extinção do mandato com o óbito e retoma o processo (HAB-03); e a habilitação seguida de alvarás aos sucessores, ao perito e ao advogado, com rateio, poderes e custas (HAB-04). Antes deste módulo, o assunto só tinha o SUP-AD-08 de `minutar-sem-modelo-cumprimento-sentenca`, sem modelo que unisse as etapas.

## Quando usar e quando não usar

Usar quando uma das partes do cumprimento de sentença (exequente ou executado particular) tiver falecido ou o óbito for noticiado nos autos, e o ato a minutar for um dos quatro acima.

Fronteiras e destino de cada hipótese vizinha:

- Notícia de óbito sem pedido de habilitação, com suspensão e intimação do advogado e edital para habilitar (arts. 313, I, e 687 a 692 do CPC): `minutar-decisao-suspensao-sobrestamento`, ramos SUS-03-A (autor ou exequente) e SUS-03-B (réu ou executado). A suspensão em si, quando o óbito já está provado, é desse ramo; o HAB-01 só determina a prova do óbito e, confirmado, deixa a Secretaria registrar o sobrestamento.
- Pedido de habilitação com documento faltante: `minutar-decisao-suspensao-sobrestamento`, ramo SUS-03-C. Prazo da suspensão esgotado sem habilitação: SUS-03-D. Morte do único advogado: SUS-03-E.
- Óbito de parte no processo de conhecimento ou em fase recursal: `minutar-decisao-suspensao-sobrestamento` (SUS-03) e `minutar-sem-modelo-despacho-decisao-civel` (SUP-AB-06, situação `habilitacao-sucessores-civel`).
- Abertura de inventário ou arrolamento, nomeação de inventariante, partilha e sobrepartilha: `minutar-inventario-arrolamento-sobrepartilha`. Este módulo decide só a sucessão processual no cumprimento, nunca o quinhão hereditário.
- Cessão de crédito e destaque de honorários: SUP-AD-09 (`minutar-sem-modelo-cumprimento-sentenca`) e `minutar-decisao-penhora-alvara`, ramo PA-14.
- Executada Fazenda Pública e sucessão do exequente nesse caso: `minutar-homologacao-calculos`, ramo HC-06. Cumprimento nos Juizados: `minutar-cumprimento-juizado-especial`.
- Extinção do cumprimento por falta de habilitação regular depois da última intimação: `minutar-sentenca-extincao-civel` (SUP-SENT-05, abandono do art. 485, III, do CPC, a confirmar no registro) e `minutar-sem-modelo-cumprimento-sentenca`, SUP-AD-17 (intimação pessoal).
- Alvarás depois da habilitação além dos que o HAB-04 resolve: módulo irmão `minutar-decisao-alvara-composto-cumprimento` (ramo ALC-04) e `minutar-decisao-penhora-alvara` (PA-10 e PA-14).

## Portões

Valem para todos os ramos, antes de qualquer redação.

**Portão 1 — executado particular e rito comum.** Fazenda Pública executada: `minutar-homologacao-calculos`, HC-06. Rito duvidoso ou cadastro de Juizado: `decidir-rito-e-competencia-do-cadastro`; sem prova do rito com Id., ficha de devolução (regra 53).

**Portão 2 — prova do óbito.** Certidão de óbito lida, com Id., data do óbito e nome. Notícia por extensão do PJe, situação cadastral no CPF ou petição, sem certidão, não prova o óbito para a decisão de habilitação: o ato é o HAB-01. Certidão ilegível ou com dúvida de identidade (homonímia): via dos autos baixados (regra 35) ou HAB-01.

**Portão 3 — quem faleceu.** Exequente: os sucessores pedem a habilitação, e o executado é ouvido (HAB-02 e HAB-03). Executado: o exequente promove a habilitação dos sucessores ou a citação do espólio, e os sucessores são ouvidos ou citados (variante E de cada ramo; art. 313, § 2º, I, do CPC, id `cpc-313`, com prazo de 2 a 6 meses para o exequente).

**Portão 4 — direito transmissível.** O crédito do cumprimento de sentença por quantia certa, inclusive de indenização por dano moral já reconhecida, transmite-se aos sucessores (art. 943 do Código Civil, a confirmar no registro). Obrigação personalíssima ou crédito alimentar de pessoa que faleceu: a transmissão é questão a decidir, e o caso vai a ponto C 🔴 e à skill da matéria, sem minutar a habilitação.

**Portão 5 — inventário.** Conferir nos autos e no sistema se há inventário ou arrolamento aberto e inventariante nomeado. Com inventário: sucessão pelo espólio, representado pelo inventariante (art. 75, VII, do CPC, a confirmar no registro), na forma do ramo B do SUP-AD-08. Sem inventário e com todos os sucessores conhecidos presentes: habilitação direta (ramo A). Sucessor conhecido não habilitado: ramo C, com reserva de quota. A abertura do inventário não é deste módulo.

**Portão 6 — contraditório.** A decisão HAB-03 só sai depois da intimação da parte contrária (HAB-02), com certidão de decurso ou manifestação, Id. Sem ela, devolver ao HAB-02. A parte contrária não é intimada pessoalmente quando tem advogado constituído (Entendimento do juízo, SUS-03); sem procurador nos autos, a citação é pessoal.

**Portão 7 — mandato e procurações.** O mandato outorgado pelo falecido extingue-se com o óbito (art. 682, II, do Código Civil, a confirmar no registro). Conferir as procurações dos sucessores, por Id., e os poderes para receber e dar quitação (art. 105 do CPC, id `cpc-105`). Sucessor sem procuração: prazo para regularizar (art. 76 do CPC, id `cpc-76`), nunca decisão que ignore a falta.

**Portão 8 — sucessor incapaz.** Havendo sucessor menor ou incapaz, a decisão de habilitação depende de vista ao Ministério Público (art. 178, II, do CPC, a confirmar no registro) e da representação legal; sem isso, o ato é despacho de vista.

**Portão 9 — levantamentos.** Conferir se houve alvará ou levantamento depois do óbito. Alvará em nome do falecido não se expede; os alvarás pendentes ficam sobrestados até a regularização do polo, e o levantamento já feito depois do óbito vai a ponto A 🔴.

**Portão 10 — documento determinante ilegível** (certidão de óbito, procurações, comprovante do depósito): via dos autos baixados (regra 35) ou corroboração por fonte independente com observação de revisão (regra 38); sem uma nem outra, não se minuta o comando que depende do documento.

## Ramos

**HAB-01 — Óbito noticiado e não confirmado nos autos: despacho que determina a prova.**

**Cofre (27.10.2026).** COMPLEMENTAÇÃO e, quanto ao despacho de prova do óbito em si, SEM CORRESPONDENTE — o cofre não tem modelo (`AB_DESP` vigente nem `AJ_DESP`, para revisão) que apenas determine a prova do óbito com prazo de 15 dias: os modelos `AJ_DESP_habilit herdeiros autor_intimação para habilitação após notícia do óbito`, `AJ_DESP_habilit herdeiros exequente_intimação para habilitação após óbito` e `AJ_DESP_habilit herdeiros executado_suspensão e intimação do exequente` (todos para revisão) e o ato 0000460-36 (11.02.2025) já suspendem e intimam para habilitar, com edital, no mesmo ato; o ato 0000460-36 usa 2 meses com edital em um só passo, o modelo `AJ` usa 4 meses e a nota de entendimentos indica 6 meses com edital em 30 dias — acrescentados o ponto C2 e a variante registrada no fim do ramo, e mantido o despacho de prova como via adotada; fórmulas finais do cofre.

**Quando usar.** Petição, certidão da Secretaria, extensão do PJe, situação cadastral no CPF ou informação da parte contrária noticia o óbito do exequente ou do executado, sem certidão de óbito nos autos (ou com certidão ilegível), e nenhum pedido de habilitação foi apresentado.

**Portões do ramo.** (a) Portão 2. (b) Quem faleceu (portão 3), para escolher o destinatário da intimação. (c) Conferir se há alvará pendente em nome do falecido (portão 9). (d) Se a certidão já estiver nos autos, o ato não é este: é SUS-03 em `minutar-decisao-suspensao-sobrestamento`.

**Relatório.** Não há. O despacho começa pela primeira determinação (regra 45). Os fatos aparecem na própria determinação, com Id.

**Fundamentação — ordem das questões.** Não há. A razão fica em uma oração na determinação 1 (o art. 313, I, do CPC suspende o processo pela morte de qualquer das partes, id `cpc-313`).

**Dispositivo — modelo.**

"DESPACHO SERVINDO COMO MANDADO DE INTIMAÇÃO (PJE)/EDITAL DE INTIMAÇÃO

1)  **INTIME-SE** o(a) advogado(a) da parte {{exequente | executada}} para, no prazo de {{15 (quinze) dias}}, juntar a certidão de óbito de {{NOME_FALECIDO}}, noticiado em {{data_noticia}} ({{extensão do PJe | petição | certidão da Secretaria}}, Id. {{id_noticia}}), e informar se há inventário ou arrolamento aberto, com o nome do inventariante, e quem são os sucessores, porque a morte de qualquer das partes suspende o processo (art. 313, I, do CPC).

2)  {{SE falecido o executado}} **INTIME-SE** a parte exequente, por seu(sua) advogado(a), para, em igual prazo, manifestar-se sobre o óbito e informar os sucessores conhecidos. {{/SE}}

3)  Confirmado o óbito por certidão ou por manifestação da parte, a Secretaria registrará a movimentação de Suspensão/Sobrestamento, com fundamento no art. 313, I, do CPC, e fará os autos conclusos para a decisão que intimará os interessados para a habilitação (art. 313, § 2º, do CPC, e arts. 687 a 692, id `conf2310-v010`; `minutar-decisao-suspensao-sobrestamento`, SUS-03-A ou SUS-03-B).

4)  Até a regularização do polo, **FICAM SOBRESTADOS** os alvarás e os levantamentos em nome da parte falecida, e a conta judicial permanece vinculada aos autos.

5)  Decorrido o prazo sem manifestação, **CERTIFIQUE** a Secretaria e façam-se os autos conclusos.

Cumpra-se Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes.

Imponho força de mandado de intimação no Pje e de edital de intimação a este ato

Cumpra-se. Intimem-se.

Senador La Rocque/MA, data da assinatura eletrônica." (assinatura em duas linhas; fórmulas finais do cofre, **==NAO_CONFIRMADO no registro==** 🟡 **[REVISAR]**.) O prazo de {{15 (quinze) dias}} vem do ato de origem do SUS-03-C para juntada de documento e sai com ponto B; a lei não fixa prazo para a prova do óbito. **==DECISÃO RESERVADA — espécie e momento da suspensão: a via adotada é o despacho que só determina a prova, com o sobrestamento registrado pela Secretaria quando o óbito se confirmar (art. 313, I) e a intimação para habilitação em decisão posterior (SUS-03); a alternativa é decidir a suspensão e a intimação para habilitação já neste ato, na forma de SUS-03-A ou SUS-03-B==** **[REVISAR]**

**Pontos a revisar típicos.** - **A1** 🟡 Arts. 313, § 2º, e 687 a 692 do CPC: conferir no registro (o `cpc-313` está conferido; os arts. 687 a 692, a confirmar). - **A2** 🔴 Origem e data da notícia do óbito (Id.) não lidas ou ilegíveis; sem elas, o despacho não se minuta. - **B1** 🟢 Ato sem modelo do gabinete: esqueleto 0.1.0. - **B2** 🟡 Prazo de 15 (quinze) dias para a prova do óbito sem fonte legal; adotado pelo ato de origem do SUS-03-C. - **C1** 🟡 Despacho de prova e sobrestamento pela Secretaria × decisão de suspensão já neste ato. - **C2** 🟡 Prazo e estrutura quando se decide a suspensão já neste ato: 2 meses com edital em um só passo (ato 0000460-36, 11.02.2025) × 4 meses (modelo `AJ_DESP_habilit herdeiros executado_suspensão e intimação do exequente`, para revisão) × 6 meses com edital em 30 dias (nota de entendimentos, a confirmar na íntegra); o art. 313, § 2º, do CPC (id `cpc-313`) fixa 2 a 6 meses para o exequente promover a citação do espólio ou dos sucessores do executado, e prazo a designar quando falece o exequente. Nenhum desses valores foi escolhido pelo módulo: cabe ao magistrado.

**Variante do cofre [ACRÉSCIMO DO MÓDULO, a partir dos modelos** `AJ_DESP` **para revisão e do ato 0000460-36].** Quando o magistrado preferir decidir a suspensão já neste ato (alternativa do C1), o despacho passa a: suspender o processo (art. 313, I); intimar o espólio, o sucessor ou os herdeiros, por edital quando desconhecidos (arts. 256 e 257 do CPC, id `conf2310-v019`), para manifestar interesse e promover a habilitação no prazo {{prazo_designado}} (ponto C2); e, se falecido o executado, intimar o exequente para promover a citação, com curador especial se os sucessores forem citados por edital e não comparecerem (art. 72, II, do CPC, a confirmar no registro; modelo `AJ_DEC_habilit herdeiros executado_nomeação de curador especial aos sucessores`, para revisão). A evolução da classe processual para habilitação, quando prevista pelo modelo `AJ`, fica para a Secretaria.

**Encaminhamento seguinte.** Óbito confirmado: `minutar-decisao-suspensao-sobrestamento`, SUS-03-A (exequente) ou SUS-03-B (executado). Pedido de habilitação apresentado: ramo HAB-02. Inércia depois da suspensão: SUS-03-D.

**HAB-02 — Pedido de habilitação dos sucessores: intimação ou citação da parte contrária e prova da condição de sucessores.**

**Cofre (27.10.2026).** ADOÇÃO — `AB_DESP_cumprir AO_intimar_pedido de habilitação de herdeiros` (despacho, vigente, `Modelos do PJe/Despachos/AB - Modelos Gerais Cíveis`; id_pje 337269); complementado por `AJ_DESP_habilit herdeiros exequente_intimação da parte contrária sobre o pedido` e `AJ_DESP_habilit herdeiros executado_citação ou intimação dos sucessores` (para revisão) — o dispositivo passa a ser o texto do modelo vigente (ato ordinatório do art. 23, IX, da Portaria-TJ 356/2025, 5 dias, art. 690 do CPC), e os itens do módulo (recebimento, citação pessoal, Ministério Público, executado falecido) ficam como acréscimos identificados; arts. 687 a 692 conferidos no registro.

**Quando usar.** Óbito provado (certidão de Id.) e pedido de habilitação juntado, instruído com a documentação mínima dos sucessores; falta intimar a parte contrária.

**Portões do ramo.** (a) Portões 2 a 5, 7 e 8. (b) Prova da condição de sucessores: certidões de nascimento, casamento ou união estável, informação sobre inexistência de outros herdeiros e de inventário, e procurações; faltando algum, o ato é SUS-03-C (`minutar-decisao-suspensao-sobrestamento`). (c) Se a parte contrária já foi intimada para esse pedido, o ato é o HAB-03. (d) Parte contrária sem procurador constituído: citação pessoal, não intimação.

**Relatório.** Não há. Despacho (regra 45).

**Fundamentação — ordem das questões.** Não há. A razão fica em uma oração: a habilitação é requerida pelos sucessores em relação à parte e processa-se nos autos principais, com a manifestação da parte contrária em 5 (cinco) dias (arts. 687 a 692 do CPC, id `conf2310-v010`).

**Dispositivo — modelo.**

"DESPACHO SERVINDO COMO MANDADO DE INTIMAÇÃO (PJE)/EDITAL DE INTIMAÇÃO

Cumpra-se ato ordinatório previsto na PORTARIA-TJ - 356/2025 desta Comarca:

Art. 23 Independente de despacho judicial, compete ao secretário judicial ou a servidor a prática dos seguintes atos gerais: (...)

IX - intimar a parte contrária para, em 5 (cinco) dias, manifestar sobre pedido de habilitação de sucessores de parte falecida (artigo 690 do CPC); (Grifado)

[ACRÉSCIMO DO MÓDULO, depois do texto do modelo, conforme o caso:]

1)  **RECEBO** o pedido de habilitação de {{n_sucessores}} sucessor(es) de {{NOME_FALECIDO}} (Id. {{id_pedido}}), instruído com a certidão de óbito (Id. {{id_certidao}}) e com os documentos de Ids. {{ids_documentos}}, e **MANTENHO** suspenso o processo (art. 313, I, do CPC; arts. 687 a 692 do CPC, id `conf2310-v010`).

2)  {{SE a parte contrária não tiver procurador nos autos}} **CITE-SE** a parte contrária, pessoalmente, para pronunciar-se no mesmo prazo de 5 (cinco) dias (art. 690 do CPC, id `conf2310-v010`). {{/SE}}

3)  {{SE sucessor incapaz}} **DÊ-SE VISTA** ao Ministério Público, por 5 (cinco) dias, antes da decisão (art. 178, II, do CPC, a confirmar no registro). {{/SE}}

4)  {{SE falecido o executado}} Em lugar do ato ordinatório: **CITEM-SE** os sucessores indicados no Id. {{id_pedido}}, pessoalmente, para pronunciar-se em 5 (cinco) dias sobre a habilitação requerida pela parte exequente (arts. 687 a 692 do CPC, id `conf2310-v010`). {{/SE}}

5)  Decorrido o prazo, com ou sem manifestação, **CERTIFIQUE** a Secretaria e façam-se os autos conclusos para a decisão sobre a habilitação.

6)  Até a decisão, **FICAM SOBRESTADOS** os alvarás e os levantamentos em nome da parte falecida.

Cumpra-se Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes.

Imponho força de mandado de intimação no Pje e de edital de intimação a este ato

Cumpra-se. Intimem-se.

Senador La Rocque/MA, data da assinatura eletrônica." (assinatura em duas linhas.) O texto do modelo vigente vai sem alteração; o modelo traz como fecho "Imponho força de mandado de intimação no Pje e de edital de intimação a este ato" e "Cumpra-se.", e a Portaria-TJ 356/2025 está NAO_CONFIRMADA no registro (🟡 **[REVISAR]**). O prazo de 5 (cinco) dias é o do art. 690 do CPC, conforme o teor do `conf2310-v010`. **==DECISÃO RESERVADA — impugnação da parte contrária que dependa de prova: a via adotada é decidir nos próprios autos; a alternativa é a autuação em apartado, com instrução (art. 691 do CPC, id conf2310-v010)==** **[REVISAR]**

**Pontos a revisar típicos.** - **A1** 🟡 Arts. 687 a 692 do CPC conferidos no registro (`conf2310-v010`: prazo de 5 dias, citação pessoal sem procurador); art. 178, II, do CPC e Portaria-TJ 356/2025, art. 23, IX: a confirmar. - **A2** 🔴 Certidão de óbito e documentos dos sucessores (Ids.) não lidos ou incompletos; incompletos levam a SUS-03-C. - **B1** 🟢 Ato sem modelo do gabinete: esqueleto 0.1.0. - **B2** 🟢 Alvarás sobrestados até a decisão da habilitação. - **C1** 🟡 Impugnação com prova: decisão nos autos × autuação em apartado.

**Encaminhamento seguinte.** Prazo decorrido ou manifestação juntada: ramo HAB-03. Pedido incompleto: `minutar-decisao-suspensao-sobrestamento`, SUS-03-C. Inventário aberto: `minutar-inventario-arrolamento-sobrepartilha`, só para a notícia, e HAB-03 com o espólio.

**HAB-03 — Decisão que defere a habilitação (de um ou de vários sucessores), define a representação, declara extinto o mandato do falecido e retoma o processo.**

**Cofre (27.10.2026).** ADOÇÃO do item 5(a) e COMPLEMENTAÇÃO do restante — `AD_Habilit.herd.cumprim.formatoNOVO` (despacho, vigente, id_pje 374781: admite o pedido, retifica o polo e intima o exequente a reapresentar o cumprimento com os elementos do art. 524 do CPC em 15 dias), `AJ_DEC_habilit herdeiros exequente_deferimento de habilitação regular e completa`, `..._habilitação do espólio representado`, `..._habilitação parcial, com permanência de coerdeiro`, `..._determinação de emenda por ausência de comprovação`, `..._autuação em apartado do incidente de habilitação`, `..._prosseguimento autônomo quanto aos honorários`, `AJ_DEC_habilit herdeiros executado_habilitação nos limites das forças da herança`, `..._nomeação de curador especial aos sucessores`, `..._deferimento de habilitação no polo passivo` e `AJ_DESP_habilit herdeiros executado_suspensão e intimação do exequente`, `..._citação por edital dos sucessores` (todos `AJ`, para revisão), atos 0001310-27 (26.07.2026) e 0800805-56 (09.07.2026) — o item 5(a) segue o modelo vigente; acrescentadas as variantes do cofre (curador especial e edital para sucessores desconhecidos, honorários autônomos, habilitação parcial) com o aviso de que são modelos para revisão; o ato 0000129-88 (26.07.2026) trata de incorporação de pessoa jurídica, e não de sucessão por morte, e não foi usado.

**Quando usar.** Óbito provado; pedido de habilitação; parte contrária intimada ou citada (certidão de decurso ou manifestação, Id.); condição de sucessores provada; nenhuma impugnação que dependa de prova. Vale para um sucessor ou para vários (por exemplo, cônjuge e filhos), para o espólio com inventariante e para o executado falecido (variante E).

**Portões do ramo.** (a) Portões 2 a 8. (b) Contraditório cumprido (portão 6). (c) Estado do processo ao retomar: cálculo pendente, cálculo homologado, pagamento depositado ou requerimento irregular; se houver pagamento depositado e pedido de alvará, o ramo é o HAB-04. (d) Sucessor sem procuração ou não habilitado (portão 7 e ramo C do SUP-AD-08).

**Relatório.** Um parágrafo por evento ou grupo: "Trata-se de cumprimento de sentença promovido por **{{NOME_EXEQUENTE}}** em face de **{{NOME_EXECUTADO}}**."

"Em {{data_noticia}}, sobreveio a notícia do falecimento da parte {{exequente | executada}}, ocorrido em {{data_obito}}, com a certidão de óbito (Id. {{id_certidao}}), e o processo foi suspenso (Id. {{id_suspensao}})."

"Em {{data_pedido}}, {{n_sucessores}} sucessor(es) requereram a habilitação (Id. {{id_pedido}}), com os documentos de Ids. {{ids_documentos}} e as procurações de Ids. {{ids_procuracoes}}."

"Em {{data_intimacao}}, a parte {{executada | exequente}} foi {{intimada | citada}} (Id. {{id_intimacao}}) e {{concordou (Id. {{id_manifestacao}}) | nada opôs, conforme a certidão de Id. {{id_certidao_decurso}} | opôs {{síntese em uma oração}} (Id. {{id_manifestacao}})}}."

se houver: "Em {{data_ministerio_publico}}, o Ministério Público manifestou-se (Id. {{id_mp}})." Termina com **É o relatório. DECIDO.**

**Fundamentação — ordem das questões.** (1) sucessão processual e habilitação; (2) condição de sucessores e quotas; (3) representação processual e extinção do mandato; (4) retomada do processo.

Questão 1. "Passo à análise da sucessão processual. A parte {{exequente | executada}}, {{NOME_FALECIDO}}, faleceu em {{data_obito}}, conforme a certidão de Id. {{id_certidao}}, e {{n_sucessores}} pessoa(s) requereram a habilitação como sucessora(s) (Id. {{id_pedido}}). A matéria é regida pelo art. 110 do Código de Processo Civil (id `conf2310-v009`), segundo o qual, ocorrendo a morte de qualquer das partes, dá-se a sucessão pelo seu espólio ou pelos seus sucessores, observado o art. 313, §§ 1º e 2º (id `cpc-313`), e pelos arts. 687 a 692 do referido Código, que disciplinam a habilitação nos autos principais (ids `conf2310-v009` e `conf2310-v010`). Nos autos, a parte {{executada | exequente}} {{concordou com o pedido (Id. {{id_manifestacao}}) | nada opôs, conforme a certidão de Id. {{id_certidao_decurso}}}}, e não há notícia de inventário aberto nem de sucessor não representado.

Conclui-se, portanto, que a habilitação direta dos sucessores é regular." Ramo B (inventário aberto): "Havendo inventário em curso (Id. {{id_inventario}}), a sucessão se dá pelo espólio, representado pelo inventariante nomeado (termo de Id. {{id_termo}}; art. 75, VII, do CPC, a confirmar no registro)." Ramo C (herdeiro conhecido não habilitado): "A certidão de óbito (Id. {{id_certidao}}) indica {{n}} sucessores, e {{n_habilitados}} se habilitaram; a execução prossegue em favor dos habilitados, na proporção das quotas, com reserva da quota do sucessor não habilitado até a sua habilitação ou a partilha." Variante E (executado falecido): "A matéria é regida pelo art. 796 do Código de Processo Civil, segundo o qual o espólio responde pelas dívidas do falecido e, feita a partilha, cada herdeiro responde dentro das forças da herança e na proporção da parte que lhe coube, **==a confirmar no registro, assim como o art. 1.792 do Código Civil==** **[REVISAR]**.

Nos autos, a parte exequente promoveu a habilitação dos sucessores (Id. {{id_pedido}}) no prazo designado (Id. {{id_prazo}}), e os sucessores foram citados (Id. {{id_citacao}}). Conclui-se, portanto, que os sucessores passam ao polo passivo, e o cumprimento prossegue contra eles dentro das forças da herança."

Questão 2. "Passo à análise da condição de sucessores e das quotas. A habilitação pode ser requerida pelos sucessores do falecido em relação à parte (art. 688, II, do Código de Processo Civil, **==a confirmar no registro==**) **[REVISAR]**. Nos autos, a certidão de óbito (Id. {{id_certidao}}) e as certidões de Ids. {{ids_certidoes}} demonstram que {{qualificação dos requerentes, sem nomes, por exemplo: a pessoa apontada como cônjuge e os filhos do falecido}} são sucessores, e o pedido indica as quotas de {{fração}} para cada um (Id. {{id_pedido}}). Conclui-se, portanto, que a condição de sucessores está provada, e as quotas indicadas servem ao prosseguimento do cumprimento e à proporção dos futuros alvarás, sem decidir a partilha, que é matéria do inventário." Argumento da parte contrária que não altera o resultado: "O argumento da parte {{contrária}} de que {{síntese}} (Id. {{id}}) não altera a conclusão, porque {{razão em uma oração}}."

Questão 3. "Passo à análise da representação processual. A morte do outorgante extingue o mandato (art. 682, II, do Código Civil, **==a confirmar no registro==**) **[REVISAR]**, de modo que a procuração outorgada pela parte falecida (Id. {{id_procuracao_falecido}}) não habilita o advogado a representar os sucessores. Nos autos, {{cada sucessor outorgou procuração (Ids. {{ids_procuracoes}}) ao(à) advogado(a) {{nome_advogado}}, com poderes para receber e dar quitação (art. 105 do CPC, id `cpc-105`) | os sucessores {{descrição, sem nomes}} não outorgaram procuração}}.

Conclui-se, portanto, que {{os sucessores estão representados a partir das procurações de Ids. {{ids_procuracoes}}, e o mandato do falecido está extinto | a representação dos sucessores {{descrição}} deve ser regularizada em prazo razoável (art. 76 do CPC, id `cpc-76`)}}." O argumento de que a procuração do falecido basta: "O argumento de {{parte}} de que a procuração do falecido continua válida (Id. {{id}}) não altera a conclusão, porque o mandato cessa com a morte do outorgante."

Questão 4. "Passo à análise da retomada do processo. A suspensão decorre do art. 313, I, do Código de Processo Civil e cessa com a regularização do polo (id `cpc-313`). Nos autos, deferida a habilitação, o polo está regularizado e a representação definida. Conclui-se, portanto, que o processo deve ser retomado no estado em que se encontra, {{com o cálculo pendente de apresentação | com o cálculo já homologado (Id. {{id_homologacao}}) | com o requerimento de cumprimento regular}}." **==DECISÃO RESERVADA — momento da retomada: a via adotada é levantar a suspensão com a decisão que defere a habilitação, mantendo os alvarás para depois do trânsito em julgado e na proporção das quotas; a alternativa é aguardar o trânsito em julgado da habilitação (art. 692 do CPC, a confirmar)==** **[REVISAR]**

**Dispositivo — modelo.**

"DISPOSITIVO

Ante o exposto,

1)  **DEFIRO** a habilitação de {{lista de sucessores}} como sucessores de {{NOME_FALECIDO}}, para que integrem o polo {{ativo | passivo}} do cumprimento de sentença, nas quotas indicadas no Id. {{id_pedido}}, sem decidir a partilha. {{Ramo B}} **DEFIRO** a sucessão pelo espólio de {{NOME_FALECIDO}}, representado pelo inventariante {{nome_inventariante}}. {{Ramo C}} **LIMITO** o prosseguimento a {{fração}} do crédito, com **RESERVA** de {{fração}} em favor do sucessor não habilitado, e **INTIME-SE** pessoalmente o sucessor remanescente para habilitar-se no prazo de 15 (quinze) dias. {{Variante E}} **DEFIRO** a habilitação dos sucessores no polo passivo, dentro das forças da herança. {{/SE}}

2)  **DECLARO** extinto, com o óbito de {{NOME_FALECIDO}} em {{data_obito}}, o mandato outorgado ao(à) advogado(a) {{nome_advogado_falecido}} (Id. {{id_procuracao_falecido}}), e **RECONHEÇO** a representação dos sucessores pelo(a)s advogado(a)s constituído(a)s nas procurações de Ids. {{ids_procuracoes}}. {{SE alguma procuração faltar}} **INTIME-SE** o sucessor {{qualificação}}, por seu(sua) advogado(a), para, no prazo de 15 (quinze) dias, juntar procuração, **==sob pena de reserva da quota e prosseguimento em favor dos sucessores regularmente representados (decisão reservada, ramo C do SUP-AD-08)==** **[REVISAR]**. {{/SE}}

3)  **PROCEDA** a Secretaria à retificação da autuação e do polo, com a inclusão dos sucessores e dos advogados e a exclusão da parte falecida.

4)  **LEVANTO** a suspensão do processo, e a Secretaria registrará o fim do sobrestamento.

5)  {{ESCOLHER}} (a) [ADOÇÃO do modelo `AD_Habilit.herd.cumprim.formatoNOVO`, vigente; o texto integral do modelo (seções I e II sobre o art. 524 do CPC, o art. 11 da Resolução GP nº 64/2025 e as orientações sobre a Lei nº 14.905/2024) é inserido sem alteração] **ADMITO** o pedido e **DETERMINO** a retificação do polo; **INTIMEM-SE** os sucessores habilitados, por seu(sua) advogado(a), para reapresentar o requerimento de cumprimento de sentença, no prazo de 15 (quinze) dias, sob pena de indeferimento/extinção sem resolução do mérito, com os elementos das alíneas a a j do modelo (indexador, juros e taxas, capitalização, base de cálculo, multas, acréscimos e descontos, documentos com Ids. e páginas, honorários, termos inicial e final, valores já pagos), em tópicos separados para danos morais e danos materiais, e novo demonstrativo atualizado e discriminado do débito; **ADVIRTO** que informações divergentes do título podem configurar litigância de má-fé (art. 80, I a III, do CPC); apresentados os elementos, **INTIME-SE** a parte executada para manifestar-se, reiterar ou apresentar impugnação em até 15 (quinze) dias; (b) **REMETAM-SE** os autos à Contadoria Judicial Única, na forma da decisão de parâmetros de Id. {{id_parametros}} e da regra 91; (c) com o cálculo homologado e depósito em conta, o ato é o do ramo HAB-04.

6)  Os alvarás ficam condicionados ao trânsito em julgado desta decisão e à proporção das quotas indicadas.

7)  **INTIMEM-SE** as partes."

Fecho (fórmulas do cofre: `AB_DESP_cumprir AO_intimar_pedido de habilitação de herdeiros` e `AD_Habilit.herd.cumprim.formatoNOVO`, ambos vigentes): "Cumpra-se Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes." / "Imponho força de mandado de intimação no Pje e de edital de intimação a este ato" / "Cumpra-se. Intimem-se." / local, data, assinatura em duas linhas. **==Provimento nº 42/2023 e Portaria-TJ 356/2025: NAO_CONFIRMADO no registro; fórmulas mantidas como no cofre==** 🟡 **[REVISAR]**. O prazo de 15 (quinze) dias do item 5(a) é o do modelo `AD_Habilit.herd.cumprim.formatoNOVO` (vigente) e do SUP-AD-08.

**Pontos a revisar típicos.** - **A1** 🟡 Arts. 75, VII, 178, II, e 796 do CPC; arts. 682, II, e 1.792 do Código Civil: a confirmar no registro; conferidos: `cpc-313`, `conf2310-v009` (art. 110), `conf2310-v010` (arts. 687 a 692), `cpc-105`; `cpc-76` com teor a conferir. - **A2** 🔴 Certidão de óbito, certidões de parentesco e procurações (Ids.) lidas; contraditório da parte contrária comprovado (portão 6). - **B1** 🟢 Ato sem modelo do gabinete: esqueleto 0.1.0; SUP-AD-08 (ramos A, B e C) como base. - **B2** 🟡 Prazo de 15 (quinze) dias do demonstrativo, por simetria com o art. 524; o acervo usa 5 e 15 dias. - **C1** 🟡 Retomada com a decisão × aguardar o trânsito da habilitação. - **C1-bis** 🟡 Habilitação parcial com coerdeiro não habilitado: o módulo reserva a quota e intima o sucessor remanescente pessoalmente em 15 dias; o modelo `AJ_DEC_habilit herdeiros exequente_habilitação parcial, com permanência de coerdeiro` (para revisão) mantém a quota suspensa; os atos do juízo lidos não decidem a questão. Via adotada: a do módulo; alternativa: a do modelo `AJ`. - **C2** 🟡 Consequência da falta de procuração de sucessor: reserva da quota (adotada) × outra. - **C3** 🔴 Transmissibilidade duvidosa do crédito ou do dever (portão 4): decidir antes de habilitar.

**Encaminhamento seguinte.** Cálculo pendente: `contadoria-diagnostico-e-minutas` e `remessa-contadoria-interativa`. Cálculo homologado e depósito: ramo HAB-04. Inércia dos sucessores: `minutar-sem-modelo-cumprimento-sentenca`, SUP-AD-17, e `minutar-sentenca-extincao-civel`.

**HAB-04 — Habilitação seguida de alvarás aos sucessores: rateio, alvará ao perito e ao credor, poderes e custas.**

**Cofre (27.10.2026).** COMPLEMENTAÇÃO em parte DIVERGENTE (momento do alvará) e SEM CORRESPONDENTE (rateio entre sucessores e alvará ao perito) — o ato 0000103-27 (12.03.2025) defere a habilitação e determina o alvará no mesmo ato, sem aguardar o trânsito em julgado, ao passo que o módulo adota o trânsito (regra 11, trava 13.1); a divergência é decisão reservada e entra no ponto C5 com as duas vias; `AD_DESP_pagamento voluntário_alvará_arquivar` (vigente) fornece a fórmula do alvará (custas, imposto de renda, Simples Nacional), e `AA_SENT_CUMP_ALVARASExpedidos` (vigente), a forma de registrar os alvarás; nenhum modelo ou ato lido trata do rateio entre vários sucessores nem do alvará ao perito.

**Quando usar.** Habilitação a deferir (ou já deferida e transitada, Id.) e, nesse cumprimento, depósito ou pagamento em conta judicial com pedido de alvará: honorários periciais já fixados, crédito do exequente falecido a ratear entre os sucessores, honorários advocatícios. O ato junta as etapas que o acervo decide em três decisões em sequência: habilitação, alvarás e conferência do pagamento.

**Portões do ramo.** (a) Portões 2 a 9. (b) Pagamento conferido por script: o depósito cobre o saldo do crédito homologado, a correção, a multa e os honorários do art. 523, § 1º, quando devidos; petição do executado com valores ambíguos (pago, devido, remanescente) não se aceita sem conferência; insuficiência leva ao ramo ALC-01 do módulo irmão `minutar-decisao-alvara-composto-cumprimento` e à postergação (PA-11). (c) Honorários periciais: valor fixado, depósito comprovado e laudo (ALC-04, portão (b)); valor já levantado a maior por perito ou parte, apontado em laudo ou extrato, é conferido e tratado antes (PA-13). (d) Contrato de honorários do falecido juntado antes da expedição (art. 22, § 4º, da Lei nº 8.906/1994, id `conf2310-v170`), com ponto C sobre a ratificação pelos sucessores. (e) Procuração de cada sucessor com poderes para receber e dar quitação (portão 7).

**Relatório.** O do HAB-03 e, depois: "Em {{data_deposito}}, a parte executada informou o pagamento de R$ {{valor_pago}} (Id. {{id_pagamento}}), e a parte exequente concordou e requereu o alvará (Id. {{id_concordancia}})." / "Em {{data_decisao_pericia}}, este Juízo fixou os honorários periciais em R$ {{valor_perito}} (Id. {{id_decisao_pericia}}), e o depósito foi comprovado em {{data_deposito_pericia}} (Id. {{id_deposito_pericia}})." / "Em {{data_extrato}}, o extrato da conta judicial indicou saldo de R$ {{saldo_conta}} (Id. {{id_extrato}})."

**Fundamentação — ordem das questões.** Questões 1 a 4 do ramo HAB-03, sem alteração, e depois: (5) pagamento e suficiência do depósito; (6) rateio entre os sucessores, poderes e custas; (7) alvará do perito e dos honorários advocatícios.

Questão 5. "Passo à análise do pagamento e da suficiência do depósito. A parte executada informou o pagamento de R$ {{valor_pago}} (Id. {{id_pagamento}}), e o crédito homologado é de R$ {{valor_devido}} na data-base {{data_base}} (Id. {{id_homologacao}}), com saldo apontado de R$ {{saldo_apontado}}. A matéria é regida pelo art. 523, §§ 1º e 2º, do Código de Processo Civil: no pagamento parcial feito no prazo, a multa e os honorários de 10% (dez por cento) incidem sobre o restante (ids `cpc-523` e `cpc-523-p2-525-p6-507`). Nos autos, o valor depositado {{cobre | não cobre}} o saldo do crédito, a correção e, sendo devidos, a multa e os honorários, na conferência por script (Id. {{id_registro_trabalho}}).

Conclui-se, portanto, que {{o pagamento satisfaz o crédito, e o valor depositado pode ser levantado | resta saldo de R$ {{saldo}}, e o levantamento do depositado aguarda o ramo ALC-01}}." Natureza do depósito (garantia × pagamento): pelo Tema 677 do STJ e pelo posicionamento de 22.10.2026, como no ramo ALC-01, questão 2.

Questão 6. "Passo à análise do rateio entre os sucessores, dos poderes e das custas. Os sucessores habilitados detêm as quotas de {{frações}} (Id. {{id_pedido}}), e o crédito de R$ {{valor_devido}} é dividido na proporção das quotas, em R$ {{valor_sucessor_1}}, R$ {{valor_sucessor_2}} e R$ {{valor_sucessor_n}}, conferidos por script, com a soma igual ao total. O alvará em nome do advogado exige procuração com poderes específicos para receber e dar quitação (art. 105 do CPC, id `cpc-105`), e as procurações de Ids. {{ids_procuracoes}} {{os conferem | não os conferem}}. As custas respectivas são retidas no alvará, e as custas finais são apuradas antes do arquivamento.

Conclui-se, portanto, que cada sucessor recebe a sua quota, {{por alvará em seu nome | por alvará em nome do(a) advogado(a) que o represente}}." **==DECISÃO RESERVADA — critério de arredondamento dos centavos: a via adotada é que a soma dos alvarás feche com o total, com a diferença no alvará do sucessor de maior quota; a alternativa é a diferença no último alvará==** **[REVISAR]**

Questão 7. "Passo à análise do alvará do perito e dos honorários advocatícios. Os honorários periciais foram fixados em R$ {{valor_perito}} (Id. {{id_decisao_pericia}}), o depósito foi comprovado (Id. {{id_deposito_pericia}}) e o laudo foi juntado (Id. {{id_laudo}}), e a verba pericial não é crédito do exequente falecido nem depende da habilitação. Os honorários advocatícios do título pertencem ao advogado (art. 23 da Lei nº 8.906/1994, a confirmar no registro), e os contratuais só são destacados com o contrato juntado antes da expedição (art. 22, § 4º, da mesma lei). Nos autos, {{o contrato de Id. {{id_contrato}} foi juntado antes da expedição | não há contrato juntado}}.

Conclui-se, portanto, que o alvará do perito pode ser expedido desde logo, e os demais alvarás dependem do trânsito em julgado desta decisão." **==DECISÃO RESERVADA — honorários contratuais firmados com o falecido: a via adotada é destacá-los só com ratificação dos sucessores nos autos (Id.); a alternativa é destacá-los pelo contrato juntado antes da expedição, sem ratificação==** **[REVISAR]**

**Dispositivo — modelo.** Os itens 1 a 4 do dispositivo do HAB-03 (habilitação, extinção do mandato e representação, retificação do polo e levantamento da suspensão), com a mesma ordem, e depois:

"5) **DECLARO** que o valor depositado (Id. {{id_pagamento}}) {{cobre | não cobre}} o crédito homologado de R$ {{valor_devido}} ({{extenso}}), conforme a conferência dos valores.

6)  **EXPEÇA-SE**, desde logo, alvará judicial em favor do(a) perito(a) {{nome_perito}}, dos honorários periciais de R$ {{valor_perito}} ({{extenso}}) (Id. {{id_decisao_pericia}}), com a retenção das custas respectivas.

7)  Após o trânsito em julgado desta decisão, **EXPEÇAM-SE** alvarás judiciais: a) em favor de cada sucessor habilitado, na proporção da sua quota (R$ {{valor_sucessor_1}}, R$ {{valor_sucessor_2}} e R$ {{valor_sucessor_n}}), ou do(a) advogado(a) que o represente, caso a procuração (Id. {{id_procuracao}}) lhe confira poderes para receber e dar quitação, com a retenção das custas respectivas e, sendo o caso, do imposto de renda; b) em favor do(a) advogado(a) {{nome_advogado}}, dos honorários advocatícios de R$ {{valor_honorarios}}{{SE contrato}}, com o destaque dos honorários contratuais (Id. {{id_contrato}}){{/SE}}; c) em favor da parte executada, {{nome_executado}}, de eventual remanescente, com os rendimentos proporcionais da conta judicial.

8)  **INTIMEM-SE** os sucessores, por seu(sua) advogado(a), e o(a) perito(a), pelo sistema, para, no prazo de 5 (cinco) dias, informar no sistema de alvarás os dados bancários de titularidade de cada um, sem os transcrever em petição pública.

9)  Comprovados os levantamentos, **CERTIFIQUE** a Secretaria, apure as custas finais e façam-se os autos **CONCLUSOS** para sentença de extinção (arts. 924, II, e 925 do CPC)."

Fecho (fórmulas do cofre: `AB_DESP_cumprir AO_intimar_pedido de habilitação de herdeiros` e `AD_Habilit.herd.cumprim.formatoNOVO`, ambos vigentes): "Cumpra-se Provimento nº 42/2023 e a Portaria-TJ 356/2025 desta Comarca, especialmente em relação aos atos ordinatórios pertinentes." / "Imponho força de mandado de intimação no Pje e de edital de intimação a este ato" / "Cumpra-se. Intimem-se." / local, data, assinatura em duas linhas. **==Provimento nº 42/2023 e Portaria-TJ 356/2025: NAO_CONFIRMADO no registro; fórmulas mantidas como no cofre==** 🟡 **[REVISAR]**. Se o depósito não cobrir o crédito, os itens 6 e 7 saem pelo ramo ALC-01 e o item 7 fica postergado (PA-11).

**Pontos a revisar típicos.** - **A1** 🔴 Certidão de óbito, pagamento, extrato, decisão pericial, laudo e procurações (Ids.) lidos; conferência do depósito por script. - **A2** 🟡 Art. 23 da Lei nº 8.906/1994 e os dispositivos do HAB-03 ainda não conferidos: a confirmar no registro; art. 22, § 4º (`conf2310-v170`) e art. 105 (`cpc-105`) conferidos. - **A3** 🟡 Rateio e saldo conferidos por script (`conferir_calculo.py proporcao`, `somar` e `comparar`); ver REGISTRO DO TRABALHO. - **B1** 🟢 Ato sem modelo do gabinete: esqueleto 0.1.0; compõe HAB-03 e ALC-04. - **B2** 🟢 Dados bancários fora da minuta; intimação para informá-los no sistema. - **C1** 🟡 Arredondamento dos centavos entre os sucessores. - **C2** 🟡 Honorários contratuais do falecido: ratificação pelos sucessores × contrato juntado. - **C3** 🔴 Alvará do perito antes do trânsito × aguardar (regra 11). - **C4** 🟡 Retomada com a decisão × após o trânsito da habilitação (como no HAB-03). - **C5** 🔴 Alvará aos sucessores no mesmo ato da habilitação, sem aguardar o trânsito (ato 0000103-27, 12.03.2025, **==ficha e íntegra lidas em parte, a confirmar==** 🟡 **[REVISAR]**) × após o trânsito em julgado (via adotada, regra 11 e trava 13.1). O cofre segue o primeiro modelo em um ato e o segundo no módulo irmão (ALC-01, ALC-04).

**Encaminhamento seguinte.** Alvarás levantados: `minutar-sentenca-extincao-civel`, R5 (SUP-SENT-05). Pagamento insuficiente ou multa do art. 523 pendente: módulo irmão `minutar-decisao-alvara-composto-cumprimento`, ramos ALC-01 e ALC-04. Disputa entre advogados: `minutar-decisao-penhora-alvara`, PA-14. Erro material ou levantamento a maior: PA-13.

## Normas, precedentes e pesquisa obrigatória antes de redigir

Ids do registro usados (conferidos, v2.5): `cpc-313` (art. 313, incisos I a X e §§ 1º a 6º), `conf2310-v009` (art. 110 do CPC), `conf2310-v010` (arts. 687 a 692 do CPC e art. 1.791, p. ún., do CC), `conf2310-v019` (arts. 256 e 257 do CPC), `cpc-76` (art. 76; teor remetido à transcrição no módulo, **==conferir==** 🟡 **[REVISAR]**), `cpc-105` (art. 105), `cpc-1000` (art. 1.000), `conf2310-v170` (art. 22, § 4º, da Lei nº 8.906/1994), `cpc-523`, `cpc-523-p2-525-p6-507`, `cpc-924`, `cpc-925`, `cpc-10` e, por remissão ao módulo irmão, `stj-tema-677-revisado` e `stj-tema-677-situacao`.

A confirmar no registro (ponto A): art. 75, VII, do CPC (espólio representado pelo inventariante); art. 72, II, do CPC (curador especial); art. 178, II, do CPC (Ministério Público e incapaz); art. 796 do CPC e art. 1.792 do Código Civil (responsabilidade dos sucessores do executado dentro das forças da herança); art. 682, II, do Código Civil (extinção do mandato pela morte do outorgante); art. 943 do Código Civil (transmissão do direito de reparação); art. 23 da Lei nº 8.906/1994; art. 485, III, do CPC (abandono); Provimento nº 42/2023 e Portaria-TJ 356/2025 (NAO_CONFIRMADO no registro; fórmulas do fecho e art. 23, IX).

Os prazos de 5 (cinco) dias (art. 690, id `conf2310-v010`) e de 2 a 6 meses (art. 313, § 2º, id `cpc-313`) entram com a fonte indicada.

Pesquisa prévia no cofre (regra de 11.10.2026): Entendimentos do juízo sobre partes e sucessão, os atos de habilitação do acervo (SUP-AD-08, sete atos de 27.02.2025 a 09.07.2026) e os modelos AJ de habilitação de herdeiros (para revisão), antes de qualquer fundamento.

## Documentos prioritários (ordem de leitura do extrator)

- último ato do juízo e a petição ou certidão que noticiou o óbito
- certidão de óbito e documentos dos sucessores (nascimento, casamento ou união estável)
- pedido de habilitação, procurações dos sucessores e procuração do falecido
- intimação ou citação da parte contrária, certidão de decurso e manifestação
- informação sobre inventário ou arrolamento e termo de inventariante
- decisão de suspensão, decisão de parâmetros, cálculo da Contadoria ou da parte e decisão de homologação
- comprovantes de depósito e pagamento, extrato da conta judicial, alvarás já expedidos
- decisão de honorários periciais, depósito pericial e laudo
- contrato de honorários

## Parâmetros repetíveis (conferência de divergência, regra 22)

- prazo para a prova do óbito (HAB-01)
- prazo de 5 (cinco) dias da parte contrária (HAB-02)
- espécie do ato de sobrestamento (despacho com registro pela Secretaria × decisão de suspensão)
- consequência da falta de procuração de sucessor
- prazo do demonstrativo depois da habilitação
- momento da retomada (com a decisão × após o trânsito)
- critério de arredondamento do rateio
- tratamento dos honorários contratuais do falecido
- alvará do perito antes do trânsito

## Dados essenciais (regra 24)

- nome do falecido, polo, data do óbito e Id. da certidão
- sucessores, qualificação (sem documentos pessoais) e quotas, com Id.
- existência de inventário e inventariante (Id.)
- intimação ou citação da parte contrária e o resultado (Id.)
- procurações dos sucessores e poderes (Ids.)
- estado do processo ao retomar (cálculo, homologação, depósito)
- decisão de honorários periciais, depósito, laudo, extrato e alvarás anteriores (HAB-04)

## Especialistas e cálculo

`calculista`: pedido em `onda/pedidos_<CNJ>.jsonl` para a suficiência do depósito, o saldo e o rateio entre os sucessores (`shared/nucleo/scripts/conferir_calculo.py proporcao`, `somar` e `comparar`); a soma dos alvarás fecha com o total, e o script entra no REGISTRO DO TRABALHO. `pesquisador-vigencia`: confirma em fonte oficial os itens "a confirmar" da seção de normas, em especial os arts. 687 a 692 do CPC, antes do fecho (regra 36).

## Nomenclatura

`<CNJ completo>_AD_<DESP|DEC>_<assunto>_<especificação>`, em minúsculas com acentos, sem data e sem nome de parte (regra 06; `shared/nucleo/scripts/nomear_minuta.py`); repetição numerada (1, 2, 3); inteiro teor com o sufixo "_inteiro teor". Exemplos: `..._AD_DESP_habilitação de herdeiros_prova do óbito`; `..._AD_DESP_habilitação de herdeiros_intimação do executado`; `..._AD_DEC_habilitação de herdeiros_deferimento`; `..._AD_DEC_habilitação de herdeiros_deferimento e alvarás`.

## Posicionamentos e decisões reservadas

Aplicados sem ponto C: a parte contrária é intimada na pessoa do advogado, e não os herdeiros pessoalmente (Entendimento do juízo, SUS-03); a morte do outorgante extingue o mandato e, sem habilitação regular, o caminho é a extinção por falta de pressuposto (SUS-03); habilitação direta quando todos os sucessores conhecidos comparecem, sem inventário e sem dissenso (SUP-AD-08, ramo A, acervo de 09.07.2026); alvará só depois do trânsito em julgado, nunca parcial e na proporção das quotas (regra 11 e trava 13.1); o depósito é, como regra, garantia do juízo (posicionamento de 22.10.2026).

Decisões reservadas ao magistrado (ponto C, "DECISÃO RESERVADA —"): (1) espécie e momento da suspensão no HAB-01; (2) impugnação da habilitação com prova (nos autos × em apartado); (3) momento da retomada do processo; (4) consequência da falta de procuração de sucessor; (5) arredondamento dos centavos; (6) honorários contratuais do falecido; (7) alvará do perito antes do trânsito; (8) transmissibilidade do crédito quando duvidosa. Nenhum desses pontos rebaixa o nível de confiança salvo se o dado determinante do ramo faltar (regra de 25.10.2026).
