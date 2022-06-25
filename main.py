
from random import shuffle

from src.tsp_file_reader import reader
from src.subida_encosta import busca
from src.renderiza_caminho import desenha_solucao


if __name__ == '__main__':
    path = 'data-samples/qa194.tsp'

    _, caminho = reader(path)

    shuffle(caminho)

    solucao = busca(caminho)

    desenha_solucao(caminho, 'inicial', 'result_inicial.png')
    desenha_solucao(solucao, 'final', 'result_final.png')
