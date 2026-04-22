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
    
    lista_caminhos = inicializacao.lista_caminhos.copy()

    while parada == False:
        # cálculo da fitness de cada caminho
        for caminho in lista_caminhos:
            src.genetico.calcula_fitness(caminho)
            
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

        melhor = src.genetico.captura_melhor_individuo(nova_lista_caminhos)
        historico_melhores_individuos.append(melhor)
        print(melhor.distancia_total)
        
        #estabelecimento da nova população
        lista_caminhos = nova_lista_caminhos.copy()

        #avaliação do critério de parada ou repetição do processo
        parada, melhor_individuo_atual, count_geracoes_sem_melhora = src.genetico.criterio_parada(lista_caminhos, historico_melhores_individuos[-1], count_geracoes_sem_melhora)