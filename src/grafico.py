import matplotlib.pyplot as plt

def centralizar_janela():
    mng = plt.get_current_fig_manager()
    try:
        mng.window.wm_geometry("+{}+{}".format(
            int((mng.window.winfo_screenwidth() - 800) / 2),
            int((mng.window.winfo_screenheight() - 500) / 2)
        ))
    except:
        pass 

def plotar_evolucao(valores, titulo="Evolução", ylabel="Valor"):
    plt.figure(figsize=(8, 5))

    plt.plot(valores, color='red')
    
    plt.title(titulo)
    plt.xlabel("Geração")
    plt.ylabel(ylabel)
    
    plt.grid(True)

    centralizar_janela()
    
    plt.show()


def plotar_tempo_execucao(tamanhos, tempos):
    plt.figure(figsize=(8, 5))
    
    plt.plot(tamanhos, tempos, color='red')
    
    plt.title("Tempo de Execução vs Tamanho do TSP")
    plt.xlabel("Número de Cidades")
    plt.ylabel("Tempo de Execução (segundos)")
    
    plt.grid(True)

    centralizar_janela()
    
    plt.show()