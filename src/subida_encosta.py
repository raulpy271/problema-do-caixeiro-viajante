
from src.cities import CaminhoDoCaixeiro, obtem_custo, seleciona_melhor_caminho
from src.heuristica import gera_vizinhos_apartir_de_heuristica


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
     