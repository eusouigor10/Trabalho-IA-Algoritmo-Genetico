# Arquivo que sera o centro de tudo, importanto os outros metodos e rodando o algoritmo genetico, alem de mostrar os graficos e resultados finais

from src.execucoes import Execucoes
import src.grafico

historico_tempo = []

if __name__ == "__main__":

    # Cidade 51
    execucao_51 = Execucoes('src/eil51.txt')
    execucao_51.execucao()

    src.grafico.plotar_evolucao(execucao_51.historico_melhor_dist, "Evolução das melhores distâncias - cidade 51", "Distância")

    historico_tempo.append(execucao_51.tempo)

    # Cidade 76
    print("\n===============================\n")

    execucao_76 = Execucoes('src/eil76.txt')
    execucao_76.execucao()

    src.grafico.plotar_evolucao(execucao_76.historico_melhor_dist, "Evolução das melhores distâncias - cidade 76", "Distância")

    historico_tempo.append(execucao_76.tempo)

    # Cidade 101
    print("\n===============================\n")

    execucao_101 = Execucoes('src/eil101.txt')
    execucao_101.execucao()

    src.grafico.plotar_evolucao(execucao_101.historico_melhor_dist, "Evolução das melhores distâncias - cidade 101", "Distância")

    historico_tempo.append(execucao_101.tempo)

    # Cidade 150 - tempo 119 - 7500
    print("\n===============================\n")

    print("Sera iniciado o algoritmo genetico para 150 cidades.\nNeste cenario leva em media 2 minutos chegando a 7500 geracoes no maximo!\n")
    print("Digite um numero para limitar o numero de geracoes (0 para sem limite): ")
    limite_geracoes = int(input())
    print("\n----------\n")

    execucao_150 = Execucoes('src/ch150.txt')
    execucao_150.execucao(limite_geracoes)

    src.grafico.plotar_evolucao(execucao_150.historico_melhor_dist, "Evolução das melhores distâncias - cidade 150", "Distância")

    historico_tempo.append(execucao_150.tempo)

    # Cidade 200 - tempo 351 - 13000
    print("\n===============================\n")

    print("Sera iniciado o algoritmo genetico para 200 cidades.\nNeste cenario leva em media 6 minutos chegando a 13000 geracoes no maximo!\n")
    print("Digite um numero para limitar o numero de geracoes (0 para sem limite): ")
    limite_geracoes = int(input())
    print("\n----------\n")

    execucao_200 = Execucoes('src/kroB200.txt')
    execucao_200.execucao(limite_geracoes)

    src.grafico.plotar_evolucao(execucao_200.historico_melhor_dist, "Evolução das melhores distâncias - cidade 200", "Distância")

    historico_tempo.append(execucao_200.tempo)

    # Plotar tempo de execução
    src.grafico.plotar_tempo_execucao([51, 76, 101, 150, 200], historico_tempo)
