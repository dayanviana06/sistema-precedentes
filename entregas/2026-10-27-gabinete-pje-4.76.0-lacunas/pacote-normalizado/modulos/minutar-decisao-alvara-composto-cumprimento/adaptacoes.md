# Adaptações admitidas — minutar-decisao-alvara-composto-cumprimento (0.1.0)

Cada variação abaixo entra na minuta como ponto B (adaptação/ciência), com o ramo e o Id. do fato que a motivou.

- Depósito intempestivo menor que o principal (ALC-01): a base da multa e dos honorários é o débito inteiro no termo do prazo; o saldo soma o principal restante, a multa e os honorários, e o item 3 do dispositivo cobra o conjunto.
- Depósito intempestivo feito por um de vários executados, ou executados solidários (ALC-01): a multa e os honorários incidem contra o executado que não pagou no prazo; o pagamento parcial de um deles aproveita aos demais até a concorrência (arts. 275 e 277 do Código Civil, a confirmar no registro).
- Depósito feito no prazo, mas parcial (ALC-01 e ALC-03): aplica-se o art. 523, § 2º, do CPC, com multa e honorários só sobre o restante; o ramo ALC-01 é adaptado, e o prazo do saldo é o do item 3.
- Procuração com poderes especiais e conta do advogado (ALC-01, ALC-02, ALC-04): alvará em nome do advogado. Sem a cláusula, ou procuração não localizada: alvará em nome da parte, intimação em 5 (cinco) dias para os dados bancários da parte, ponto A.
- Matéria bancária ou de seguros (família AC): acrescentar o item 1.2 do modelo vigente AC do PA-10 (alvará só em conta de titularidade da parte, Recomendação CNJ nº 159/2024, a confirmar no registro) e usar a família AC no nome do arquivo.
- Vários depósitos em datas distintas, com levantamento anterior parcial (ALC-02): o saldo é o conferido por script; o excedente desconta o levantado; duplicidade de pagamento vai a ponto A 🔴.
- Concordância de todas as partes (ALC-02): bloco R64 (preclusão lógica) no item 3 do dispositivo; sem concordância expressa de todas, o trânsito aguarda o prazo recursal.
- Depósito de garantia, e não de pagamento (ALC-02 e ALC-03): o cálculo que corta o crédito na data do depósito é revisto à luz do Tema 677 do STJ; a via adotada é homologar quando ninguém impugnou, com ponto C 🔴.
- Prazo de impugnação ainda aberto (portão 5): a minuta é o despacho de aguardar, sem decisão sobre a multa.
- Alegação de quitação sem peça formal de impugnação (ALC-03): a petição é conhecida como impugnação, com ponto C 🔴.
- Depósito de pagamento no prazo e integral (ALC-03, desfecho B): a impugnação é acolhida, não há multa nem honorários, e segue o alvará do depósito e do excedente (ALC-02) e a extinção.
- Quantificação por parâmetros (ALC-03, desfecho A'): BLOCO-CALC da regra 91, com a Contadoria Judicial Única; nos Juizados, o ato é de outra skill.
- Parte exequente com prioridade legal (idade, doença grave): registrar a urgência típica na ficha; a ordem das questões não muda.
- Honorários periciais com gratuidade da parte (ALC-04): a verba é requisitada ao Estado (ramo PRV-07 de `minutar-decisao-prova-pericia`) e não sai do saldo da conta; o alvará do perito sai do ramo PRV, não deste.
- Saldo insuficiente para todas as rubricas (ALC-04): pagamento na ordem do dispositivo até o limite do saldo e intimação do devedor pela diferença, com ponto C 🔴.
- Remanescente e restituição de custas por alvará: PA-12 e PA-16 da skill vizinha, sem adaptação aqui.
- Dado ausente dos autos: nunca inventado; sai `[INFORMAÇÃO NÃO ENCONTRADA NOS AUTOS — PREENCHER MANUALMENTE]` e ponto A 🔴.
