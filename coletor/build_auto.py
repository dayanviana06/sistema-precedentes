# -*- coding: utf-8 -*-
"""Construtor automático mínimo e robusto para publicação diária.
Fonte automática única: STJ Dados Abertos (Temas.csv). A base curada
(dados-manual.json: STF/TJMA/Súmulas verificados) tem prioridade e nunca
é apagada. Sem dependências além de 'requests'. Fontes opcionais (STF,
informativos) permanecem disponíveis no coletor completo, fora deste fluxo."""
from util import log
import consolidar

def _seguro(nome, fn):
    try:
        return fn()
    except Exception as e:
        log(f"{nome}: indisponível hoje ({e}) — base anterior/curada preservada.")
        return []

def main():
    import coletor_stj
    coletas = [_seguro("STJ", coletor_stj.coletar)]
    novos, alterados = consolidar.consolidar(coletas)
    log(f"Publicação preparada: {novos} novos, {alterados} alterados (+ base curada sempre presente).")

if __name__ == "__main__":
    main()
