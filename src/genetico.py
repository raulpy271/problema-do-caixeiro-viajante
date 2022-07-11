
from random import choice, choices, randint, shuffle
from math import sqrt

from src.cities import CaminhoDoCaixeiro, seleciona_melhor_caminho, obtem_custo


def busca_indice_de_cidade(solucao: CaminhoDoCaixeiro, par_buscado: tuple[float, float]) -> int:
    indice = -1
    for par in solucao:
        indice += 1
        if par == par_buscado:
            break
    return indice

def obtem_indice_de_vizinho(solucao: CaminhoDoCaixeiro, indice_atual: int) -> int:
    cidades_len = len(solucao)
    if indice_atual >= (cidades_len - 1):
        return 0
    else:
        return indice_atual + 1

def reproduz(pai: CaminhoDoCaixeiro, mae: CaminhoDoCaixeiro) -> tuple[CaminhoDoCaixeiro, CaminhoDoCaixeiro]:
    filho_1 = pai.copy()
    filho_2 = mae.copy()
    indice_onde_sera_alterado_seu_vizinho_pai = randint(0, len(pai) - 1)
    par_onde_sera_alterado_seu_vizinho_pai = pai[indice_onde_sera_alterado_seu_vizinho_pai]
    indice_onde_sera_alterado_seu_vizinho_mae = busca_indice_de_cidade(mae, par_onde_sera_alterado_seu_vizinho_pai)
    indice_vizinho_pai = obtem_indice_de_vizinho(pai, indice_onde_sera_alterado_seu_vizinho_pai)
    indice_vizinho_mae = obtem_indice_de_vizinho(mae, indice_onde_sera_alterado_seu_vizinho_mae)
    indice_do_novo_vizinho_pai = busca_indice_de_cidade(pai, mae[indice_vizinho_mae])
    indice_do_novo_vizinho_mae = busca_indice_de_cidade(mae, pai[indice_vizinho_pai])
    filho_1[indice_do_novo_vizinho_pai] = pai[indice_vizinho_pai]
    filho_1[indice_vizinho_pai] = mae[indice_vizinho_mae]
    filho_2[indice_do_novo_vizinho_mae] = mae[indice_vizinho_mae]
    filho_2[indice_vizinho_mae] = pai[indice_vizinho_pai]
    return filho_1, filho_2 

def realiza_mutacao_individual(individuo: CaminhoDoCaixeiro) -> CaminhoDoCaixeiro:
    tamanho_do_pedaco = 4
    pedaco_de_genes_inicio_index = randint(0, len(individuo) - tamanho_do_pedaco)
    genes = []
    for i in range(pedaco_de_genes_inicio_index, pedaco_de_genes_inicio_index + tamanho_do_pedaco):
        genes.append(individuo[i])
    shuffle(genes)
    for i in range(0, tamanho_do_pedaco):
        individuo[pedaco_de_genes_inicio_index + i] = genes[i]
    return individuo

def gera_populacao_inicial(solucao_inicial: CaminhoDoCaixeiro, tamanho_populacao: int) -> list[CaminhoDoCaixeiro]:
    populacao = []
    for _ in range(tamanho_populacao):
        solucao_i = solucao_inicial.copy()
        shuffle(solucao_i)
        populacao.append(solucao_i)
    return populacao

def seleciona_mais_aptos_para_reproducao(populacao: list[CaminhoDoCaixeiro]) -> list[CaminhoDoCaixeiro]:
    nova_populacao = []
    individuos_escolhidos_aleatoriamente = 2
    for _ in range(len(populacao)):
        filhos = choices(populacao, k=individuos_escolhidos_aleatoriamente)
        melhor_filho = seleciona_melhor_caminho(filhos)
        nova_populacao.append(melhor_filho)
    return nova_populacao

def realiza_reproducao_de_populacao(populacao: list[CaminhoDoCaixeiro]) -> list[CaminhoDoCaixeiro]:
    nova_populacao = []
    for _ in range(int(len(populacao) / 2)):
        pai, mae = choices(populacao, k=2)
        filho1, filho2 = reproduz(pai, mae)
        nova_populacao += [filho1, filho2]
    if len(nova_populacao) < len(populacao):
        pai, mae = choices(populacao, k=2)
        filhos = reproduz(pai, mae)
        nova_populacao.append(choice(filhos))
    return nova_populacao

def adiciona_mutacao_aleatoriamente(populacao: list[CaminhoDoCaixeiro]) -> list[CaminhoDoCaixeiro]:
    porcentagem_de_mutacao = 0.2
    nova_populacao = populacao.copy()
    for _ in range(int(len(populacao) * porcentagem_de_mutacao)):
        individuo_index = randint(0, len(nova_populacao) - 1)
        nova_populacao[individuo_index] = realiza_mutacao_individual(nova_populacao[individuo_index])
    return nova_populacao

def busca_genetica(solucao_inicial: CaminhoDoCaixeiro) -> CaminhoDoCaixeiro:
    tamanho_populacao = 500
    maximo_de_geracoes_sem_progresso = 50
    geracoes_sem_progresso = 0
    populacao = gera_populacao_inicial(solucao_inicial, tamanho_populacao)
    mais_apto_geracao_atual = seleciona_melhor_caminho(populacao)
    custo_mais_apto_geracao_atual = obtem_custo(mais_apto_geracao_atual)
    mais_apto = mais_apto_geracao_atual
    custo_mais_apto = custo_mais_apto_geracao_atual
    i = 0
    while geracoes_sem_progresso < maximo_de_geracoes_sem_progresso:
        print(f'Mais apto global: {custo_mais_apto}')
        print(f'Mais apto atual: {custo_mais_apto_geracao_atual}')
        print(f'sem progresso: {geracoes_sem_progresso}')
        populacao = seleciona_mais_aptos_para_reproducao(populacao)
        populacao = realiza_reproducao_de_populacao(populacao)
        populacao = adiciona_mutacao_aleatoriamente(populacao)
        mais_apto_geracao_atual = seleciona_melhor_caminho(populacao)
        custo_mais_apto_geracao_atual = obtem_custo(mais_apto_geracao_atual)
        if custo_mais_apto <= custo_mais_apto_geracao_atual:
            geracoes_sem_progresso += 1
        else: 
            geracoes_sem_progresso = 0
            mais_apto = mais_apto_geracao_atual
            custo_mais_apto = custo_mais_apto_geracao_atual
        i += 1
    print(f'Passos: {i}')
    return mais_apto
