
from random import randint
from src.cities import CaminhoDoCaixeiro


def busca(caminho_inicial: CaminhoDoCaixeiro) -> CaminhoDoCaixeiro:
    caminho = caminho_inicial.copy()
    tamanho_esperado = len(caminho)
    pares_randomicos: CaminhoDoCaixeiro = []
    while len(pares_randomicos) < tamanho_esperado:
        par_index = randint(0, tamanho_esperado - 1)
        par_randomico = caminho[par_index]
        if par_randomico:
            pares_randomicos.append(par_randomico)
            caminho[par_index] = None
    return pares_randomicos
     