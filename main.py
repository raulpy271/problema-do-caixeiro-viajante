
from random import shuffle

import matplotlib.pyplot as plt

from src.tsp_file_reader import reader
from src import subida_encosta
from src import tempera_simulada
from src import genetico
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
    caminhos = list(map(lambda path: reader(path)[1], PATHS))
    for caminho_index, caminho in enumerate(caminhos):
        shuffle(caminho)
        solucao_subida_encosta = subida_encosta.busca(caminho)
        solucao_tempera_simulada = tempera_simulada.busca(caminho)
        solucao_genetico = genetico.busca(caminho)
        desenha_solucao(caminho, 'inicial', f'{PATHS[caminho_index]}_inicial.png')
        desenha_solucao(solucao_subida_encosta, 'final subida encosta', f'{PATHS[caminho_index]}_final_subida_encosta.png')
        desenha_solucao(solucao_tempera_simulada, 'final tempera simulada', f'{PATHS[caminho_index]}_final_tempera_simulada.png')
        desenha_solucao(solucao_genetico, 'final genetico', f'{PATHS[caminho_index]}_final_genetico.png')

if __name__ == '__main__':
    gera_solucoes()
    gera_mapas_de_pontos()
