# Adaptações admitidas — minutar-decisao-impugnacao-com-homologacao (regra 24)

Variações fáticas que o esqueleto 0.1.0 admite. Cada uma entra na minuta como ponto B (ADAPTAÇÃO), sem rebaixar a confiança, salvo dado determinante.

- Depósito judicial integral e suficiente para o crédito homologado: o ato deixa de ser decisão e passa a ser a sentença do modelo H1 (`minutar-homologacao-calculos`); a minuta registra o encaminhamento e não prossegue.
- Depósito feito como pagamento (prova nos autos), e não como garantia: o depósito abate o débito na data em que foi feito, e o saldo é o apurado nessa data; o parágrafo do Tema 677 é substituído por "o pagamento parcial abate o débito na data do depósito", ponto B.
- Depósito já levantado por alvará anterior: o item do alvará é substituído por "o valor depositado já foi levantado (Id.), nada havendo a prover quanto a ele", ponto B.
- Depósito feito dentro do prazo do art. 523 (pagamento parcial no prazo): multa e honorários de 10% incidem sobre o restante (art. 523, § 2º); fora do prazo, sobre o total (§ 1º). A escolha vai ao relatório e ao parágrafo da multa, ponto B.
- Executado em recuperação judicial ou em falência: não se aplica constrição nem alvará; `minutar-decisao-executado-recuperacao-judicial` (regra 53, item 3, alterada em 27.10.2026) e alerta inicial de juridicidade.
- Mais de um executado (solidários), com impugnação de apenas um: conferir a intimação dos demais (Id.) e o silêncio de cada um; a homologação é do valor total, e o Sisbajud alcança apenas quem foi intimado a pagar. Ponto B.
- Impugnação e cálculo de pessoa jurídica diversa da executada (grupo econômico, sucursal, outra razão social): ponto A de legitimidade e representação; a decisão não é minutada sem a conferência do polo passivo e do instrumento de mandato.
- Peça com nome de outra parte, de outro processo ou rótulo divergente do conteúdo: o conteúdo é lido e citado pelo Id.; a peça de outro processo não é tratada como se constasse do dossiê (só com o CNJ de origem); ponto A.
- Ambas as partes discordam do cálculo: duas questões, uma por parte, na ordem em que as manifestações foram juntadas (IHO-01 e IHO-02 combinados), com a homologação ao final; ponto B.
- Duas planilhas da Contadoria (cálculo e retificação): homologa-se a última, com o Id. da primeira declarado como superado; ponto B.
- Cálculo da Contadoria sem data identificável de geração: a data-base segue a escada da regra 51; sem data, ponto A e a decisão não declara "até a data do cálculo" sem data.
- Cálculo com multa cominatória (astreintes): rubrica própria, separada das verbas indenizatórias, pelo bloco `contadoria-astreinte`; escolha entre teto nominal e atualizado é DECISÃO RESERVADA.
- Prescrição alegada na impugnação: só a superveniente à sentença (art. 525, § 1º, VII); a não reconhecida no título não é reaberta (regra 70).
- Honorários advocatícios contratuais, destaque ou cessão de crédito: capítulo para `minutar-decisao-penhora-alvara` (PA-14) ou `minutar-homologacao-calculos` (HC-06); a minuta registra o encaminhamento.
- Gratuidade do exequente: a exigibilidade das verbas de sucumbência fica suspensa (art. 98, § 3º, do CPC, a confirmar); a impugnação do exequente ao cálculo não exige custas.
- Gratuidade da executada pessoa jurídica: só com prova (Súmula 481 do STJ, `stj-sumula-481`; Tema 1.424 do STJ, `stj-tema-1424`, texto literal não lido em fonte oficial); sem prova, custas da impugnação são exigíveis (P6).
- Alegação de óbito do exequente sem certidão nos autos: etiqueta ignorada, ponto A; com certidão, SUP-AD-08 antes de qualquer alvará.
- Co-requerido ente público apenas quanto a honorários, com cálculo separado: o ato trata só do particular; o ente é objeto de ato próprio (HC-01 ou HC-02).
- Manifestação do executado depois do decurso do prazo: preclusão como via adotada; petição de fato superveniente (art. 525, § 11) só com fato novo comprovado; DECISÃO RESERVADA.
- Planilha ou documento determinante ilegível: via dos autos baixados (regra 35); sem leitura segura, o comando que dele depende não é minutado.
