
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
    return custo_total
