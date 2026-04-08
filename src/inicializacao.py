# Arquivo responsavel por inicializar o cenario, calcular distancias, e criar a populacao inicial

from cidade import Cidade
import random

class Inicializacao:

    def __init__(self):
        self.cidades = []
        self.cidade_inicial = None

    # criar o grafo  
    def criacao_grafo(self):
        with open('cenario1.txt', 'r', encoding='utf-8') as arquivo:
            while True:
                linha = arquivo.readline()

                if not linha:
                    break

                linha_limpa = linha.split()

                if len(linha_limpa) == 3:
                    id, x, y = linha_limpa
                    cidade = Cidade(int(id), float(x), float(y))
                    self.cidades.append(cidade)
        
        #sorteio ponto inicial
        self.cidade_inicial = random.choice(self.cidades)

    # cálculo de distância
    def calculo_distancia(self, c1, c2):
        id1, x1, y1 = c1.id, c1.x, c1.y
        id2, x2, y2 = c2.id, c2.x, c2.y

        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5




    # criação dos caminhos iniciais