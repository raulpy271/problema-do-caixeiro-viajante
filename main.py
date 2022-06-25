
from random import shuffle

import matplotlib.pyplot as plt

from src.tsp_file_reader import reader
from src.subida_encosta import busca
from src.renderiza_caminho import desenha_solucao, desenha_pontos

PATHS = [
    'data-samples/wi29.tsp',
    'data-samples/qa194.tsp'
]

def gera_mapas_de_pontos():
    for path in PATHS:
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 10)
        _, caminho = reader(path)
        desenha_pontos(ax, caminho)
        fig.savefig(f'{path}.png')
        plt.close('all')

def gera_solucoes():
    numero_de_tentantivas = 2
    caminhos = list(map(lambda path: reader(path)[1], PATHS))
    for tentativa in range(numero_de_tentantivas):
        for caminho_index, caminho in enumerate(caminhos):
            shuffle(caminho)
            solucao = busca(caminho)
            desenha_solucao(caminho, f'inicial {tentativa}', f'{PATHS[caminho_index]}_inicial_{tentativa}.png')
            desenha_solucao(solucao, f'final {tentativa}',   f'{PATHS[caminho_index]}_final_{tentativa}.png')

if __name__ == '__main__':
    gera_solucoes()
