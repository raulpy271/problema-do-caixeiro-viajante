
from math import inf
from itertools import chain

from src.cities import CaminhoDoCaixeiro, obtem_custo, obtem_distancia


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

def seleciona_melhor_caminho(caminhos: list[CaminhoDoCaixeiro]) -> CaminhoDoCaixeiro:
    melhor_caminho = caminhos[0]
    melhor_custo = obtem_custo(melhor_caminho)
    for i in range(1, len(caminhos)):
        custo = obtem_custo(caminhos[i])
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_caminho = caminhos[i]
    return melhor_caminho

def busca(caminho_inicial: CaminhoDoCaixeiro) -> CaminhoDoCaixeiro:
    caminho = caminho_inicial.copy()
    custo_atual = obtem_custo(caminho)
    while True:
        print(f'Melhor custo atual: {custo_atual}')
        caminhos_vizinhos = gera_vizinhos_apartir_de_heuristica(caminho)
        melhor_caminho_entre_vizinhos = seleciona_melhor_caminho(caminhos_vizinhos)
        custo_melhor_vizinho = obtem_custo(melhor_caminho_entre_vizinhos)
        if custo_melhor_vizinho < custo_atual:
            caminho = melhor_caminho_entre_vizinhos
            custo_atual = custo_melhor_vizinho
            continue
        else:
            break
    return caminho
     