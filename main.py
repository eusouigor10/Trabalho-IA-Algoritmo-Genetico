# Arquivo que sera o centro de tudo, importanto os outros metodos e rodando o algoritmo genetico, alem de mostrar os graficos e resultados finais

import src.genetico
from src.inicializacao import Inicializacao
from src.enum.operacao import Operacao
from src.execucoes import Execucoes

# Variáveis globais para controle do algoritmo
melhor_distancia = None # * Numero
count_geracoes_sem_melhora = 0
historico_melhor_dist = []
# TODO Historico de fitness
parada = False

if __name__ == "__main__":
    #execucao_51 = Execucoes('src/eil51.txt')
    #execucao_51.execucao()

    #execucao_101 = Execucoes('src/eil101.txt')
    #execucao_101.execucao()

    execucao_200 = Execucoes('src/kroB200.txt')
    execucao_200.execucao()