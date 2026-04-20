# Arquivo contendo todos os metodos relacionados ao algoritmo genetico, como a funcao de fitness, selecao, crossover e mutacao

import random
from src.enum.operacao import Operacao
from src.const.probabilidades import OP_PROB
from src.caminho import Caminho


def calcula_fitness(individuo):
    # Calcula a fitness do individuo

    fitness = 1 / individuo.distancia_total

    individuo.fitness = fitness

    return fitness


def escolha_operacao():
    # Escolhe a operacao a ser realizada com base nas probabilidades definidas

    num = random.random()

    if num < OP_PROB[Operacao.CROSSOVER]:
        return Operacao.CROSSOVER
    elif num < OP_PROB[Operacao.CROSSOVER] + OP_PROB[Operacao.REPRODUCAO]:
        return Operacao.REPRODUCAO
    else:
        return Operacao.MUTACAO


def selecao_roleta(populacao):
    # Realiza a selecao por roleta

    fitness_total = sum(individuo.fitness for individuo in populacao)

    num_aleatorio = random.uniform(0, fitness_total)

    acumulado = 0

    for individuo in populacao:
        acumulado += individuo.fitness

        if acumulado >= num_aleatorio:
            return individuo

    return None

def criarIndividuo(individuo):
    novoIndividuo = Caminho()
    novoIndividuo.cidades = individuo
    # TODO: Calcular a distancia total do novo individuo
    # TODO: Calcular a fitness do novo individuo

    return novoIndividuo
    

def crossover(individuo1, individuo2):
    # Realiza o crossover entre dois individuos
    # A B C D | E F G H | I J K L M N - 14 / 3 = 4.66 -> 4

    if(len(individuo1.cidades) != len(individuo2.cidades)):
        raise ValueError("Os individuos devem ter o mesmo numero de cidades")

    filho = [None] * len(individuo1.cidades)

    corte = len(individuo1.cidades) // 3

    # Copia a parte central do individuo 1 para o filho
    for i in range(corte, 2 * corte):
        filho[i] = individuo1.cidades[i]

    # Preenche o restante do filho com cidades do individuo 2
    j = 0

    for i in range(len(filho)):
        if corte <= i < 2 * corte:
            continue

        while individuo2.cidades[j] in filho:
            j += 1

        filho[i] = individuo2.cidades[j]
        j += 1

    novoIndividuo = criarIndividuo(filho)

    return novoIndividuo


def reproducao(individuo):
    # Realiza a reproducao do individuo

    return criarIndividuo(individuo.cidades)


def mutacao(individuo):    
    # Realiza a mutacao do individuo
    i, j = random.sample(range(len(individuo.cidades)), 2)

    backup = individuo.cidades[i]

    individuo.cidades[i] = individuo.cidades[j]
    
    individuo.cidades[j] = backup

    novoIndividuo = criarIndividuo(individuo.cidades)

    return novoIndividuo


# * @param população: vetor de caminhos
# * @param melhor_individuo_passado: melhor caminho da geração passada
# * @param count_geracoes_sem_melhora: contador de gerações sem melhora
def criterio_parada(populacao, melhor_individuo_passado, count_geracoes_sem_melhora):
    # Verifica se o criterio de parada foi atingido

    # Limite de gerações sem melhora
    limite = 50 # ? Alterar este valor?

    # Tolerância para considerar que houve melhora
    tolerancia = 0.05 # ? Alterar este valor?

    melhor_individuo_atual = min(individuo.distancia_total for individuo in populacao)

    # Primeira geração
    if melhor_individuo_passado is None:
        return False, melhor_individuo_atual, 0
    
    melhora = (melhor_individuo_passado - melhor_individuo_atual) / melhor_individuo_passado

    if melhora < tolerancia:
        count_geracoes_sem_melhora += 1
    else:
        count_geracoes_sem_melhora = 0

    parar = count_geracoes_sem_melhora >= limite

    '''
        Retorno:
        - parar: booleano indicando se o critério de parada foi atingido
        - melhor_individuo_atual: melhor caminho da geração atual
        - count_geracoes_sem_melhora: contador atualizado de gerações sem melhora
    '''
    return parar, melhor_individuo_atual, count_geracoes_sem_melhora


def substituicao_geracao():
    return None