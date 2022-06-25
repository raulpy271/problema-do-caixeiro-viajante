
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from src.cities import CaminhoDoCaixeiro, separa_cordenadas, obtem_custo

def desenha_pontos(ax, solucao):
    xs, ys = separa_cordenadas(solucao)
    ax.scatter(xs, ys, c='blue')

def desenha_caminho(ax, solucao):
    codigos = [Path.MOVETO] + (len(solucao) * [Path.LINETO])
    path = Path(solucao + [solucao[0]], codigos)
    patch = patches.PathPatch(path, facecolor='none', lw=1)
    ax.add_patch(patch)

def desenha_ponto_inicial(ax, solucao):
    ax.scatter(solucao[0][0], solucao[0][1], c='red')

def desenha_solucao(solucao: CaminhoDoCaixeiro, title: str, file_path: str):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    desenha_pontos(ax, solucao)
    desenha_ponto_inicial(ax, solucao)
    desenha_caminho(ax, solucao)
    ax.set_title(f'{title} - Custo: {obtem_custo(solucao)}')
    fig.savefig(file_path)
    plt.close('all')