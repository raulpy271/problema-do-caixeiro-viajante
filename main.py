
from uuid import uuid1

from src.tsp_file_reader import reader
from src.subida_encosta import busca
from src.renderiza_caminho import desenha_solucao


if __name__ == '__main__':
    path = 'data-samples/wi29.tsp'

    c1 = [(0, 0), (0, 1), (1, 1)]

    _, caminho = reader(path)

    solution = busca(caminho)

    id = str(uuid1())

    desenha_solucao(caminho, id, f'result.png')
