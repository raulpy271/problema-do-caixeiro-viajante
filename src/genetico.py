
from random import randint

from src.cities import CaminhoDoCaixeiro

def busca_indice_de_cidade(solucao: CaminhoDoCaixeiro, par_buscado: tuple[float, float]) -> int:
    indice = -1
    for par in solucao:
        indice += 1
        if par == par_buscado:
            break
    return indice

def obtem_indice_de_vizinho(solucao: CaminhoDoCaixeiro, indice_atual: int) -> int:
    cidades_len = len(solucao)
    if indice_atual >= (cidades_len - 1):
        return 0
    else:
        return indice_atual + 1

def reproduz(pai: CaminhoDoCaixeiro, mae: CaminhoDoCaixeiro) -> tuple[CaminhoDoCaixeiro, CaminhoDoCaixeiro]:
    filho_1 = pai.copy()
    filho_2 = mae.copy()
    indice_onde_sera_alterado_seu_vizinho_pai = randint(0, len(pai) - 1)
    par_onde_sera_alterado_seu_vizinho_pai = pai[indice_onde_sera_alterado_seu_vizinho_pai]
    indice_onde_sera_alterado_seu_vizinho_mae = busca_indice_de_cidade(mae, par_onde_sera_alterado_seu_vizinho_pai)
    indice_vizinho_pai = obtem_indice_de_vizinho(pai, indice_onde_sera_alterado_seu_vizinho_pai)
    indice_vizinho_mae = obtem_indice_de_vizinho(mae, indice_onde_sera_alterado_seu_vizinho_mae)
    indice_do_novo_vizinho_pai = busca_indice_de_cidade(pai, mae[indice_vizinho_mae])
    indice_do_novo_vizinho_mae = busca_indice_de_cidade(mae, pai[indice_vizinho_pai])
    filho_1[indice_do_novo_vizinho_pai] = pai[indice_vizinho_pai]
    filho_1[indice_vizinho_pai] = mae[indice_vizinho_mae]
    filho_2[indice_do_novo_vizinho_mae] = mae[indice_vizinho_mae]
    filho_2[indice_vizinho_mae] = pai[indice_vizinho_pai]
    return filho_1, filho_2 
