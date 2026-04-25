import src.genetico
from src.inicializacao import Inicializacao
from src.enum.operacao import Operacao
import time

# para 51 cidades
# Variáveis globais para controle do algoritmo
melhor_distancia = None # * Numero
count_geracoes_sem_melhora = 0
historico_melhor_dist = []
# TODO Historico de fitness
parada = False

inicio = time.perf_counter()
print("Iniciando o algoritmo genético para 51 cidades...")

inicializacao = Inicializacao('src/eil51.txt')

# inicialização com a criação da população inicial, caminhos iniciais e distâncias
inicializacao.parte_1()
    
# Geração inicial
lista_caminhos = inicializacao.lista_caminhos.copy()

while parada == False:

    # Nova geração
    nova_lista_caminhos = []
        
    # cálculo da fitness de cada caminho
    for caminho in lista_caminhos:
        src.genetico.calcula_fitness(caminho)

    #elitismo
    melhor_individuo_atual = src.genetico.captura_melhor_individuo(lista_caminhos)
    nova_lista_caminhos.append(melhor_individuo_atual)

    # seleção e envio para crossover, mutação ou reprodução
    while len(nova_lista_caminhos) < 100:
        operacao = src.genetico.escolha_operacao()


        if operacao == Operacao.CROSSOVER:
            individuo_1 = src.genetico.selecao_roleta(lista_caminhos)
            individuo_2 = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.crossover(individuo_1, individuo_2, inicializacao))
                
        elif operacao == Operacao.REPRODUCAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.reproducao(individuo, inicializacao))
                
        elif operacao == Operacao.MUTACAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)
                
            nova_lista_caminhos.append(src.genetico.mutacao_inversao(individuo, inicializacao))

    #avaliação do critério de parada ou repetição do processo
    parada, melhor_distancia, count_geracoes_sem_melhora = src.genetico.criterio_parada(nova_lista_caminhos, melhor_distancia, count_geracoes_sem_melhora)

    # Salvando melhor indivíduo
    historico_melhor_dist.append(melhor_distancia)
        
    #estabelecimento da nova população
    lista_caminhos = nova_lista_caminhos.copy()

fim = time.perf_counter()

tempo = fim - inicio

print("\n\nAlgoritmo genético finalizado para 51 cidades com tempo de {tempo:.4f}.\n")
print(f"Gerações Totais: {len(historico_melhor_dist)}\n")
print(f"Melhor distância encontrada: {melhor_distancia}\n")

#575 cidades
print("Iniciando o algoritmo genético para 575 cidades...")

inicializacao = Inicializacao('src/rat575.txt')

# inicialização com a criação da população inicial, caminhos iniciais e distâncias
inicializacao.parte_1()
    
# Geração inicial
lista_caminhos = inicializacao.lista_caminhos.copy()

while parada == False:

    # Nova geração
    nova_lista_caminhos = []
        
    # cálculo da fitness de cada caminho
    for caminho in lista_caminhos:
        src.genetico.calcula_fitness(caminho)

    #elitismo
    melhor_individuo_atual = src.genetico.captura_melhor_individuo(lista_caminhos)
    nova_lista_caminhos.append(melhor_individuo_atual)

    # seleção e envio para crossover, mutação ou reprodução
    while len(nova_lista_caminhos) < 100:
        operacao = src.genetico.escolha_operacao()


        if operacao == Operacao.CROSSOVER:
            individuo_1 = src.genetico.selecao_roleta(lista_caminhos)
            individuo_2 = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.crossover(individuo_1, individuo_2, inicializacao))
                
        elif operacao == Operacao.REPRODUCAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.reproducao(individuo, inicializacao))
                
        elif operacao == Operacao.MUTACAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)
                
            nova_lista_caminhos.append(src.genetico.mutacao_inversao(individuo, inicializacao))

    #avaliação do critério de parada ou repetição do processo
    parada, melhor_distancia, count_geracoes_sem_melhora = src.genetico.criterio_parada(nova_lista_caminhos, melhor_distancia, count_geracoes_sem_melhora)

    # Salvando melhor indivíduo
    historico_melhor_dist.append(melhor_distancia)
        
    #estabelecimento da nova população
    lista_caminhos = nova_lista_caminhos.copy()


print("\n\nAlgoritmo genético finalizado.\n")
print(f"Gerações Totais: {len(historico_melhor_dist)}\n")
print(f"Melhor distância encontrada: {melhor_distancia}\n")

print("Iniciando o algoritmo genético para 1379 cidades...")

inicializacao = Inicializacao('src/nrw1379.txt')

# inicialização com a criação da população inicial, caminhos iniciais e distâncias
inicializacao.parte_1()
    
# Geração inicial
lista_caminhos = inicializacao.lista_caminhos.copy()

while parada == False:

    # Nova geração
    nova_lista_caminhos = []
        
    # cálculo da fitness de cada caminho
    for caminho in lista_caminhos:
        src.genetico.calcula_fitness(caminho)

    #elitismo
    melhor_individuo_atual = src.genetico.captura_melhor_individuo(lista_caminhos)
    nova_lista_caminhos.append(melhor_individuo_atual)

    # seleção e envio para crossover, mutação ou reprodução
    while len(nova_lista_caminhos) < 100:
        operacao = src.genetico.escolha_operacao()


        if operacao == Operacao.CROSSOVER:
            individuo_1 = src.genetico.selecao_roleta(lista_caminhos)
            individuo_2 = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.crossover(individuo_1, individuo_2, inicializacao))
                
        elif operacao == Operacao.REPRODUCAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)

            nova_lista_caminhos.append(src.genetico.reproducao(individuo, inicializacao))
                
        elif operacao == Operacao.MUTACAO:
            individuo = src.genetico.selecao_roleta(lista_caminhos)
                
            nova_lista_caminhos.append(src.genetico.mutacao_inversao(individuo, inicializacao))

    #avaliação do critério de parada ou repetição do processo
    parada, melhor_distancia, count_geracoes_sem_melhora = src.genetico.criterio_parada(nova_lista_caminhos, melhor_distancia, count_geracoes_sem_melhora)

    # Salvando melhor indivíduo
    historico_melhor_dist.append(melhor_distancia)
        
    #estabelecimento da nova população
    lista_caminhos = nova_lista_caminhos.copy()


print("\n\nAlgoritmo genético finalizado.\n")
print(f"Gerações Totais: {len(historico_melhor_dist)}\n")
print(f"Melhor distância encontrada: {melhor_distancia}\n")