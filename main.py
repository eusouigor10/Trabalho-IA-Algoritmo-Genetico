# Arquivo que sera o centro de tudo, importanto os outros metodos e rodando o algoritmo genetico, alem de mostrar os graficos e resultados finais

import src.genetico

# Variáveis globais para controle do algoritmo
melhor_individuo_atual = None
count_geracoes_sem_melhora = 0
historico_melhores_individuos = []
parada = False

if __name__ == "__main__":
    print("Iniciando o algoritmo genético...")

#inicialização com a criação da população inicial, caminhos iniciais e distâncias

#cálculo da fitness de cada caminho

#seleção e envio para crossover, mutação ou reprodução

#estabelecimento da nova população

#avaliação do critério de parada ou repetição do processo