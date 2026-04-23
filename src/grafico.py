# Arquivo contendo a biblioteca de graficos e seus metodos

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plotar_evolucao(valores, titulo="Evolução", ylabel="Valor"):
    plt.figure(figsize=(8, 5))
    
    plt.plot(valores, marker='o')
    
    plt.title(titulo)
    plt.xlabel("Geração")
    plt.ylabel(ylabel)
    
    plt.grid(True)
    
    plt.show()


def plotar_tempo_execucao(tamanhos, tempos):
    plt.figure(figsize=(8, 5))
    
    plt.plot(tamanhos, tempos, marker='o')
    
    plt.title("Tempo de Execução vs Tamanho do TSP")
    plt.xlabel("Número de Cidades")
    plt.ylabel("Tempo de Execução (segundos)")
    
    plt.grid(True)
    
    plt.show()