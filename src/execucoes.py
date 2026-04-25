import src.genetico
from src.inicializacao import Inicializacao
from src.enum.operacao import Operacao
import time

class Execucoes:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        # Variáveis globais para controle do algoritmo
        self.melhor_distancia = None # * Numero
        self.count_geracoes_sem_melhora = 0
        self.historico_melhor_dist = []
        # TODO Historico de fitness
        self.parada = False

    def execucao(self):
        inicio = time.perf_counter()

        inicializacao = Inicializacao(self.arquivo)

        # inicialização com a criação da população inicial, caminhos iniciais e distâncias
        inicializacao.parte_1()

        print(f"Iniciando o algoritmo genético para {len(inicializacao.cidades)} cidades...")
            
        # Geração inicial
        lista_caminhos = inicializacao.lista_caminhos.copy()

        geracao_atual = 0

        while self.parada == False:

            geracao_atual += 1
            if geracao_atual % 1000 == 0:
                print(f"Geração: {geracao_atual}")

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
            self.parada, melhor_distancia, self.count_geracoes_sem_melhora = src.genetico.criterio_parada(nova_lista_caminhos, self.melhor_distancia, self.count_geracoes_sem_melhora)

            if geracao_atual > 10000:
                self.parada = True

            # Salvando melhor indivíduo
            self.historico_melhor_dist.append(melhor_distancia)
                
            #estabelecimento da nova população
            lista_caminhos = nova_lista_caminhos.copy()

        fim = time.perf_counter()

        tempo = fim - inicio

        print(f"\n\nAlgoritmo genético finalizado para 51 cidades com tempo de {tempo:.4f}.\n")
        print(f"Gerações Totais: {len(self.historico_melhor_dist)}\n")
        print(f"Melhor distância encontrada: {melhor_distancia}\n")