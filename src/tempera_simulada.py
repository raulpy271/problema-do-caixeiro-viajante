
from math import e as numero_de_euler
from random import choice, random

from src.cities import CaminhoDoCaixeiro, obtem_custo
from src.heuristica import gera_vizinhos_apartir_de_heuristica


def seleciona_caminho_aleatorio(caminhos: list[CaminhoDoCaixeiro]) -> CaminhoDoCaixeiro:
    return choice(caminhos)

def busca(caminho_inicial: CaminhoDoCaixeiro, temperatura: int = 10000, fator_esfriamento: float = 0.995) -> tuple[CaminhoDoCaixeiro, list[float]]:
    caminho = caminho_inicial.copy()
    custo_atual = obtem_custo(caminho)
    custos = []
    while temperatura != 0:
        custos.append(custo_atual)
        print(f'Custo atual: {custo_atual}, temperatura: {temperatura}')
        caminhos_vizinhos = gera_vizinhos_apartir_de_heuristica(caminho)
        vizinho_aleatorio = seleciona_caminho_aleatorio(caminhos_vizinhos)
        custo_vizinho = obtem_custo(vizinho_aleatorio)
        variacao_custo = custo_vizinho - custo_atual
        print(f'Variação: {variacao_custo}')
        if variacao_custo <= 0:
            print(f'Selecionando proxímo nó')
            caminho = vizinho_aleatorio
            custo_atual = custo_vizinho
        else:
            probabilidade_escolher_vizinho = (
                numero_de_euler ** ((-(variacao_custo))/ temperatura)
            )
            print(f'Probabilidade de selecionar próximo nó: {probabilidade_escolher_vizinho}')
            if random() < probabilidade_escolher_vizinho:
                print(f'Selecionando proxímo nó')
                caminho = vizinho_aleatorio
                custo_atual = custo_vizinho
        temperatura = int(temperatura * fator_esfriamento)
    return caminho, custos
     