# Arquivo contendo todos os metodos relacionados ao algoritmo genetico, como a funcao de fitness, selecao, crossover e mutacao

import random
from src.enum.operacao import Operacao
from src.const.probabilidades import OP_PROB
from src.caminho import Caminho
from src.inicializacao import Inicializacao

def calcula_fitness(individuo):
    # Calcula a fitness do individuo

    if individuo.distancia_total == 0:
        return 0
    else:
        fitness = 1 / individuo.distancia_total

    individuo.fitness = fitness

    #print(f"\nDistância Total: {individuo.distancia_total}, Fitness: {individuo.fitness}")

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

def printIndividuo(individuo, num):
    vetor = [str(cidade.id) for cidade in individuo.cidades]
    caminho_str = ", ".join(vetor)

    print(f"\nIndividuo {num}: [{caminho_str}] - Distância Total = {individuo.distancia_total}, Fitness = {individuo.fitness}")

def criarIndividuo(individuo, inicializacao):
    novoIndividuo = Caminho()

    novoIndividuo.cidades = individuo

    print(f"\nNovo individuo criado: {len(novoIndividuo.cidades)} cidades\n")

    novoIndividuo.distancia_total = inicializacao.calculo_distancia_total_caminho(novoIndividuo)

    print(f"Distância total do novo individuo: {novoIndividuo.distancia_total}\n")

    calcula_fitness(novoIndividuo)

    print(f"Fitness do novo individuo: {novoIndividuo.fitness}\n")

    return novoIndividuo
    

def crossover(individuo1, individuo2, inicializacao):
    # Realiza o crossover entre dois individuos
    # A B C D | E F G H | I J K L M N - 14 / 3 = 4.66 -> 4
    printIndividuo(individuo1, 1)

    printIndividuo(individuo2, 2)

    if(len(individuo1.cidades) != len(individuo2.cidades)):
        raise ValueError("Os individuos devem ter o mesmo numero de cidades")
    
    if individuo1.cidades[0] != individuo2.cidades[0]:
        raise ValueError("Os individuos devem iniciar na mesma cidade")

    # Retira cidade inicial
    cidade_inicial = individuo1.cidades[0]

    caminho1 = individuo1.cidades[1:-1]
    caminho2 = individuo2.cidades[1:-1]

    tamanho = len(caminho1)
    
    filho = [None] * tamanho

    corte = max(1, tamanho // 3)

    # Copia a parte central do individuo 1 para o filho
    for i in range(corte, 2 * corte):
        filho[i] = caminho1[i]

    # Preenche o restante do filho com cidades do individuo 2
    restantes = [cidade for cidade in caminho2 if cidade not in filho]

    if len(restantes) != filho.count(None):
        raise ValueError("Erro no crossover: quantidade inconsistente de cidades")

    k = 0
    for i in range(tamanho):
        if filho[i] is None:
            filho[i] = restantes[k]
            k += 1

    # Finaliza filho
    filho = [cidade_inicial] + filho + [cidade_inicial]

    novoIndividuo = criarIndividuo(filho, inicializacao)

    print("Filho:\n")
    printIndividuo(novoIndividuo, "Filho")

    return novoIndividuo


def reproducao(individuo, inicializacao):
    # Realiza a reproducao do individuo

    printIndividuo(individuo, "Reprodução")

    return criarIndividuo(individuo.cidades, inicializacao)


def mutacao(individuo, inicializacao):   
    print("Indivíduo antes da mutação:\n")
    printIndividuo(individuo, "Antes da Mutação")

    cidades = individuo.cidades

    # Guarda cidade inicial
    cidade_inicial = cidades[0]

    caminho = cidades[1:-1].copy()

    if len(caminho) < 2:
        return individuo  # nada pra mutar

    # Escolhe posições válidas no caminho
    i, j = random.sample(range(len(caminho)), 2)

    # Swap
    caminho[i], caminho[j] = caminho[j], caminho[i]

    # Reconstrói o indivíduo
    novo_caminho = [cidade_inicial] + caminho + [cidade_inicial]

    novo_individuo = criarIndividuo(novo_caminho, inicializacao)

    print("Indivíduo após a mutação:\n")
    printIndividuo(novo_individuo, "Após Mutação")

    return novo_individuo

def captura_melhor_dist(populacao):
    fitness_melhor_individuo = 0
    for individuo in populacao:
        if individuo.fitness > fitness_melhor_individuo:
            fitness_melhor_individuo = individuo.fitness
    
    for individuo in populacao:
        if individuo.fitness == fitness_melhor_individuo:
            return individuo.distancia_total


# * @param população: vetor de caminhos
# * @param melhor_individuo_passado: melhor caminho da geração passada
# * @param count_geracoes_sem_melhora: contador de gerações sem melhora
def criterio_parada(populacao, melhor_individuo_passado, count_geracoes_sem_melhora):
    # Verifica se o criterio de parada foi atingido

    # Limite de gerações sem melhora
    limite = 1000 # ? Alterar este valor?

    # Tolerância para considerar que houve melhora
    tolerancia = 0.001 # ? Alterar este valor?

    melhor_dist = captura_melhor_dist(populacao)

    # Primeira geração
    if melhor_individuo_passado is None:
        return False, melhor_dist, 0
    
    if melhor_dist < melhor_individuo_passado:
        if melhor_individuo_passado == 0:
            melhora = 0
        else:
            melhora = (melhor_individuo_passado - melhor_dist) / melhor_individuo_passado

        if melhora >= tolerancia:
            count_geracoes_sem_melhora = 0
        else:
            count_geracoes_sem_melhora += 1
    else:
        count_geracoes_sem_melhora += 1

    parar = count_geracoes_sem_melhora >= limite

    '''
        Retorno:
        - parar: booleano indicando se o critério de parada foi atingido
        - melhor_dist: melhor caminho da geração atual
        - count_geracoes_sem_melhora: contador atualizado de gerações sem melhora
    '''
    return parar, melhor_dist, count_geracoes_sem_melhora

# ! Talvez este método não será necessário
def substituicao_geracao():
    return None