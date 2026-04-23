# Arquivo que sera o centro de tudo, importanto os outros metodos e rodando o algoritmo genetico, alem de mostrar os graficos e resultados finais

import src.genetico
from src.inicializacao import Inicializacao
from src.enum.operacao import Operacao

# Variáveis globais para controle do algoritmo
melhor_individuo_atual = None
count_geracoes_sem_melhora = 0
historico_melhores_individuos = []
parada = False
inicializacao = Inicializacao()

if __name__ == "__main__":
    print("Iniciando o algoritmo genético...")

    # inicialização com a criação da população inicial, caminhos iniciais e distâncias
    inicializacao.parte_1()
    
    # Geração inicial
    lista_caminhos = inicializacao.lista_caminhos.copy()

    while parada == False:
        # cálculo da fitness de cada caminho
        for caminho in lista_caminhos:
            src.genetico.calcula_fitness(caminho)
            
        # Nova geração
        nova_lista_caminhos = []

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
                nova_lista_caminhos.append(src.genetico.mutacao(individuo, inicializacao))

        #avaliação do critério de parada ou repetição do processo
        parada, melhor_individuo_atual, count_geracoes_sem_melhora = src.genetico.criterio_parada(nova_lista_caminhos, melhor_individuo_atual, count_geracoes_sem_melhora)

        # Salvando melhor indivíduo
        historico_melhores_individuos.append(melhor_individuo_atual)
        print(melhor_individuo_atual.distancia_total)
        
        #estabelecimento da nova população
        lista_caminhos = nova_lista_caminhos.copy()

        