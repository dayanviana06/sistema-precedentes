# Entrega de 27.10.2026 — parâmetros da remessa à Contadoria Local e do retorno para esclarecimentos: fábrica 4.67.0 e gabinete-pje 4.79.0

Esta pasta contém os dois plugins prontos para instalação. A base foi o gabinete-pje 4.78.0 e a fábrica 4.66.0. A alteração foi feita primeiro na fábrica (molde do núcleo) e levada ao gabinete pela sincronização oficial (`sincronizar_nucleo.py --aplicar`). As skills próprias do gabinete foram ajustadas pela fábrica, com nova data, nova versão e registro no histórico.

## A ordem aplicada

As minutas que determinam a remessa à Contadoria Judicial Local passam a seguir o mesmo modelo da remessa à Contadoria Judicial Única quanto à fixação dos parâmetros. Mantém-se a intimação prévia da parte exequente para, querendo, apresentar os cálculos (BLOCO-CALC); se não apresentar, os autos vão à Contadoria Judicial Local. A decisão que devolve os autos à Contadoria para esclarecimentos também passa a explicitar os parâmetros do modelo, previstos no art. 11 da Resolução GP nº 64/2025 do TJMA.

A ordem foi registrada como complemento da regra 91 (R-16). O texto completo das variações está numa fonte única, `shared/nucleo/referencias/parametros-remessa-contadoria.md`.

## O que o modelo exige em cada ato

Os tópicos de parâmetros são os do modelo obrigatório de remessa da trilha cível:

- regras de transição, em texto literal;
- títulos executivos e parâmetros judiciais, em parágrafos corridos com Id.;
- bases de cálculo e verbas acessórias, em alíneas;
- base documental;
- pagamentos parciais, quando houver.

Quando a executada é a Fazenda Pública, valem os tópicos do modelo mandatório da Fazenda, com o Item I imutável. Esses tópicos cumprem os incisos I a IX do art. 11:

- indexador;
- juros e taxas;
- capitalização;
- base de cálculo;
- multas;
- acréscimos e descontos;
- documentos com Id. e página;
- honorários;
- termos inicial e final.

O que muda em cada ato:

- **Remessa à Contadoria Local no Juizado Cível (M-JEC-4 e ramo JIMP-05):**
  - mesmos tópicos de parâmetros;
  - frase de delimitação: "Diante da divergência aritmética instalada, **DELIMITO** os parâmetros para a elaboração de cálculos pela Contadoria Judicial Local, conforme parâmetros acima e observados os elementos do art. 11 da Resolução GP n.º 64/2025...";
  - em seguida, o BLOCO-CALC e a remessa à Local;
  - o tópico de custas dá lugar à frase do art. 55 da Lei nº 9.099/1995.
- **Juizado da Fazenda (M-JEC-5):** modelo mandatório da Fazenda, com a mesma frase de delimitação, 30 dias para a Fazenda e RPV ou precatório.
- **Retorno para esclarecimentos (adaptação A.12 da homologação e devolução nos ramos IHO-02 e IHO-03):**
  - os parâmetros da decisão anterior são explicitados de novo, por completo, sem inovar;
  - um parágrafo indica o ponto a esclarecer, com o Id.;
  - a ordem é: "**DETERMINO** o retorno dos autos à Contadoria Judicial Única (ou Local, se Juizado), para manifestação técnica sobre ... e, sendo o caso, retificação do cálculo, no prazo de 15 (quinze) dias, observados rigorosamente os parâmetros acima, de acordo com o art. 11 da Resolução GP n.º 64/2025.";
  - depois da manifestação técnica, as partes têm 5 dias e os autos voltam conclusos.
- **Nova remessa depois da devolução sem cálculo (`minutar-decisao-complementar-pos-contadoria`):**
  - parâmetros completos;
  - roteiro (item 4), moldura COMP-01 e ramos COMP-C e COMP-F refeitos;
  - ramo novo COMP-L para o Juizado.
- **Remessa à Local depois da recusa da Única (RCQ-02):** os parâmetros são explicitados, em lugar de "sem a necessidade de nova delimitação".
- **Despacho de remessa à Local por inércia do exequente (JIMP-08):** os parâmetros da decisão anterior são explicitados de novo.

## Verificador

`checar_destino_contadoria.py`, que também roda dentro do `checar_minuta.py`, passou a dar duas acusações quando o ato remete à Contadoria, devolve os autos para esclarecimentos ou faz a nova remessa:

- **CORRIGIR:** quando faltam o indexador, os juros, a base de cálculo, os documentos com Id. ou o termo inicial;
- **AVISO:** quando faltam a multa, os acréscimos e descontos ou os honorários, para que se confirme que são inaplicáveis.

O `checar_minuta.py` também foi ajustado. Ele deixou de tratar como "tópico numerado" os itens 1.1 e 1.2 do bloco literal das regras de transição, que não podem ser reescritos.

Na fábrica, as skills `criar-modulo-de-ato` e `auditar-plugin-minutas` passaram a exigir esse padrão.

## Resultado dos testes

- **Suíte do núcleo no gabinete:** 134 de 136 testes passam, inclusive os quatro novos da regra 91. Os testes novos cobrem três situações:
  - remessa à Local sem os parâmetros, acusada;
  - retorno sem os parâmetros, acusado;
  - retorno com os parâmetros, aprovado.
  
  As duas falhas são as já conhecidas dos testes de pastas do Drive, alheias a esta alteração.
- **Exemplos fictícios da impugnação no Juizado (AH e AE):** refeitos na estrutura nova. Passam sem acusação no `validar_impugnacao_jec.py`, no `checar_destino_contadoria.py` e no `checar_minuta.py`.
- **Exemplo da decisão complementar:** refeito com os parâmetros completos. Passa no verificador da regra 91.
- **Demais verificadores:** `verificar_gabinete.py`, `validar_cowork.py` (gabinete e fábrica), `esqueleto_ramos.py verificar` e `aferir_competencia.py validar` estão sem erro.

## Decisões que dependem do magistrado (via conservadora já adotada)

- <mark><b><span style="color:red">Art. 11 na Contadoria Local: o art. 11 da Resolução GP nº 64/2025 trata, no texto, da Contadoria Judicial Única. Por sua ordem, a remessa à Local usa "observados os elementos do art. 11", com ponto B em cada minuta. Mantém essa redação ou prefere "de acordo com o art. 11", como na Única?</span></b></mark>
- <mark><b><span style="color:red">Retorno sem BLOCO-CALC: no retorno para esclarecimentos e na nova remessa, não reabri a faculdade do exequente de apresentar cálculos, porque ele já a teve (regra 91, conflito 5). No lugar dela, ficou a remessa direta: "Ausente oposição sobre os parâmetros estabelecidos, DETERMINO a remessa imediata...". Mantém, ou quer reabrir a faculdade nesses atos?</span></b></mark>
- <mark><b><span style="color:red">Retorno como decisão: como passa a fixar parâmetros, o ato de retorno da adaptação A.12 é chamado "decisão" (a A.12 dizia "despacho"). Confirma?</span></b></mark>
- <mark><b><span style="color:red">Despacho JIMP-08 (remessa à Local por inércia do exequente): ele só cumpre o BLOCO-CALC da decisão de parâmetros. Adotei a repetição dos parâmetros, pela literalidade da ordem; a alternativa é a simples remissão à decisão de Id. Qual prefere?</span></b></mark>
- <mark><b><span style="color:red">Prazo sobre os parâmetros no Juizado da Fazenda: usei 5 dias, como no M-JEC-4. O modelo mandatório da Fazenda no rito comum usa 10 dias. Mantém 5?</span></b></mark>

## Observações

Dois exemplos antigos, anteriores a esta entrega, continuam com acusações do `checar_minuta.py` e não foram refeitos. As acusações são CORRIGIR e não BLOQUEIO, e o texto dos modelos dessas skills já segue o modelo mandatório da Fazenda (ramo FAZ-03) e o modelo do IHO:

- o exemplo da `minutar-fazenda-impugnacao-intempestiva-ausente-titulo-ambiguo`, um esboço curto de remessa à Contadoria Única sem os parâmetros nem o BLOCO-CALC;
- o exemplo da `minutar-decisao-impugnacao-com-homologacao`.

## Instalação

Instale os dois arquivos `.plugin` desta pasta e desative as versões anteriores (gabinete-pje 4.78.0 e fábrica 4.66.0).
