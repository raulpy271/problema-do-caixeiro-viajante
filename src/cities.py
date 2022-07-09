
from math import sqrt

CaminhoDoCaixeiro = list[tuple[float, float]]

def separa_cordenadas(pares: CaminhoDoCaixeiro) -> tuple[list[float], list[float]]:
    xs = []
    ys = []
    for x, y in pares:
        xs.append(x)
        ys.append(y)
    return xs, ys

def obtem_distancia(caminho: CaminhoDoCaixeiro, ponto_inicial_index: int, ponto_final_index: int) -> float:
    x_i, y_i = caminho[ponto_inicial_index]
    x_f, y_f = caminho[ponto_final_index]
    return sqrt(
        ((x_f - x_i) ** 2) + ((y_f - y_i) ** 2)
    )

def obtem_custo(caminho: CaminhoDoCaixeiro) -> float:
    custo_total = 0.0
    for i in range(0, len(caminho) - 1):
        custo_total += obtem_distancia(caminho, i, i + 1)
    custo_total += obtem_distancia(caminho, 0, len(caminho) - 1)
    return custo_total

def seleciona_melhor_caminho(caminhos: list[CaminhoDoCaixeiro]) -> CaminhoDoCaixeiro:
    melhor_caminho = caminhos[0]
    melhor_custo = obtem_custo(melhor_caminho)
    for i in range(1, len(caminhos)):
        custo = obtem_custo(caminhos[i])
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_caminho = caminhos[i]
    return melhor_caminho
