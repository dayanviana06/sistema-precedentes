# Adaptações admitidas — minutar-decisao-habilitacao-herdeiros-cumprimento (0.1.0)

Cada variação abaixo entra na minuta como ponto B (adaptação/ciência), com o ramo e o Id. do fato que a motivou.

- Executado falecido (HAB-01 a HAB-04, variante E): o exequente promove a habilitação ou a citação do espólio ou dos sucessores, em prazo de 2 a 6 meses (art. 313, § 2º, I, id `cpc-313`); os sucessores passam ao polo passivo, dentro das forças da herança (art. 796 do CPC e art. 1.792 do Código Civil, a confirmar no registro).
- Inventário aberto, com inventariante nomeado (ramo B do SUP-AD-08): sucessão pelo espólio, representado pelo inventariante; a notícia do inventário vai à ficha, e a abertura ou a partilha não são deste módulo.
- Sucessor conhecido não habilitado (ramo C do SUP-AD-08): prosseguimento na quota dos habilitados, reserva da quota restante e intimação pessoal do sucessor remanescente em 15 (quinze) dias.
- Sucessor menor ou incapaz: vista ao Ministério Público e representação legal antes da decisão (art. 178, II, do CPC, a confirmar no registro); o HAB-03 sai depois da vista.
- Sucessor sem procuração: prazo para regularizar (art. 76 do CPC, a confirmar no registro), com a consequência de reserva da quota em ponto C 🟡.
- Parte contrária sem advogado constituído: citação pessoal, e não intimação (HAB-02, item 2); a intimação do advogado vale quando há procuração nos autos.
- Parte contrária que impugna a habilitação com necessidade de prova: autuação em apartado e instrução (art. 691 do CPC, a confirmar), ponto C 🟡; a decisão sobre a impugnação sem prova segue no HAB-03.
- Pedido de habilitação incompleto: SUS-03-C (`minutar-decisao-suspensao-sobrestamento`), sem minutar o HAB-02.
- Inércia dos sucessores depois do prazo designado: SUS-03-D e, depois, sentença de extinção (`minutar-sentenca-extincao-civel`); não se minuta o HAB-03.
- Alvará já levantado em nome do falecido depois do óbito: ponto A 🔴, sem alvará novo até a conferência; restituição ou ajuste pelo PA-13 (`minutar-decisao-penhora-alvara`).
- Honorários periciais já levantados a maior, apontados em laudo ou extrato (HAB-04): tratar antes pelo PA-13 e só então expedir o alvará do perito.
- Pagamento informado pelo executado com valores ambíguos (HAB-04): conferir por script o depósito contra o crédito homologado, a correção, a multa e os honorários; insuficiência leva ao ramo ALC-01 do módulo irmão e à postergação dos alvarás de crédito.
- Polos com nomes diferentes para a mesma parte (por exemplo, duas denominações da instituição executada): conferir o polo antes de redigir, ponto A 🟡; a decisão usa a denominação da autuação.
- Crédito alimentar ou obrigação personalíssima do falecido: transmissibilidade a decidir, ponto C 🔴, fora do esqueleto.
- Executada Fazenda Pública: HC-06 de `minutar-homologacao-calculos`; Juizados: `minutar-cumprimento-juizado-especial`.
- Dado ausente dos autos: nunca inventado; sai `[INFORMAÇÃO NÃO ENCONTRADA NOS AUTOS — PREENCHER MANUALMENTE]` e ponto A 🔴.
