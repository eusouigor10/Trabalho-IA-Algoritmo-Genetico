# Arquivo contendo todos os metodos relacionados ao algoritmo genetico, como a funcao de fitness, selecao, crossover e mutacao

import random
from src.enum.operacao import Operacao
from src.const.probabilidades import OP_PROB


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
    return None


def crossover(individuo1, individuo2):
    # Realiza o crossover entre dois individuos
    return None


def reproducao(individuo):
    # Realiza a reproducao da populacao
    return None


def mutacao(individuo):    
    # Realiza a mutacao do individuo
    return None


def criterio_parada(populacao):
    # Verifica se o criterio de parada foi atingido
    return None


def substituicao_geracao():
    return None