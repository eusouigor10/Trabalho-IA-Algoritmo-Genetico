# Arquivo responsavel por inicializar o cenario, calcular distancias, e criar a populacao inicial

from cidade import Cidade
from caminho import Caminho
import random

class Inicializacao:

    def __init__(self):
        self.cidades = []
        self.cidade_inicial = None
        self.matriz_adjacencias = []
        self.linhas = 0
        self.cidade_aleatoria = None
        self.lista_caminhos = []

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

    def sorteio_ponto_inicial(self):
        self.cidade_inicial = random.choice(self.cidades)

    # cálculo de distância
    def calculo_distancia(self, c1, c2):
        id1, x1, y1 = c1.id, c1.x, c1.y
        id2, x2, y2 = c2.id, c2.x, c2.y

        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    # criação da matriz de adjacências que representa o grafo
    def criacao_matriz_grafo(self):
        self.linhas = len(self.cidades)
        self.matriz_adjacencias = [[0.0 for _ in range(self.linhas)] for _ in range(self.linhas)]

        for cidade in self.cidades:
            cidade.preencher_lista(self.linhas)
            for adjacente in self.cidades:
                if cidade != adjacente:
                    cidade.lista_adjacencias[adjacente.id] = self.calculo_distancia(cidade, adjacente)
            self.matriz_adjacencias[cidade.id] = cidade.lista_adjacencias
    
    # criação dos caminhos iniciais
    def criacao_caminhos_iniciais(self):
        for _ in range(100):
            novo_caminho = Caminho()
            novo_caminho.preenchimento_caminho(len(self.cidades))
            self.sorteio_ponto_inicial()
            novo_caminho.cidades[0] = self.cidade_inicial
            novo_caminho.cidades[len(self.cidades)] = self.cidade_inicial

            cidades_meio = []
            for i in range(len(self.cidades)):
                if self.cidades[i] != self.cidade_inicial:
                    cidades_meio.append(self.cidades[i])
            random.shuffle(cidades_meio)

            cidades_meio = [self.cidade_inicial] + cidades_meio
            cidades_meio.append(self.cidade_inicial)

            for i in range(len(self.cidades) + 1):
                novo_caminho.cidades[i] = cidades_meio[i]

            self.lista_caminhos.append(novo_caminho)
        