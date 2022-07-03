
from math import inf
from itertools import chain

from src.cities import CaminhoDoCaixeiro, obtem_distancia

def obtem_cidade_mais_proxima(caminho: CaminhoDoCaixeiro, cidade_atual: int) -> int:
    indice_cidade_mais_proximo = inf
    valor_cidade_mais_proximo = inf
    for i in chain(range(0, cidade_atual), range(cidade_atual + 1, len(caminho))):
        distancia_i = obtem_distancia(caminho, i, cidade_atual)
        if distancia_i < valor_cidade_mais_proximo:
            valor_cidade_mais_proximo = distancia_i
            indice_cidade_mais_proximo = i
    return indice_cidade_mais_proximo

def gera_vizinho_apartir_de_heuristica(caminho: CaminhoDoCaixeiro, cidade_atual: int) -> CaminhoDoCaixeiro:
    novo_caminho = caminho.copy()
    cidade_mais_proxima_de_cidade_atual = obtem_cidade_mais_proxima(caminho, cidade_atual)
    viajante_ja_percorre_de_cidade_atual_para_cidade_ao_lado = (
        (cidade_mais_proxima_de_cidade_atual == cidade_atual + 1) or
        (cidade_mais_proxima_de_cidade_atual == cidade_atual - 1)
    )
    if viajante_ja_percorre_de_cidade_atual_para_cidade_ao_lado:
        return novo_caminho
    if cidade_atual + 1 < len(caminho):
        cidade_mais_proxima_novo_indice = cidade_atual + 1
    else:
        cidade_mais_proxima_novo_indice = 0
    novo_caminho[cidade_mais_proxima_novo_indice] = caminho[cidade_mais_proxima_de_cidade_atual]
    novo_caminho[cidade_mais_proxima_de_cidade_atual] = caminho[cidade_mais_proxima_novo_indice]
    return novo_caminho

def gera_vizinhos_apartir_de_heuristica(caminho: CaminhoDoCaixeiro) -> list[CaminhoDoCaixeiro]:
    caminhos_vizinhos = []
    for cidade_atual_index in range(len(caminho)):
        caminhos_vizinhos.append(gera_vizinho_apartir_de_heuristica(caminho, cidade_atual_index))
    return caminhos_vizinhos
