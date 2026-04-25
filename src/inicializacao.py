
from src.cidade import Cidade
from src.caminho import Caminho
import random

class Inicializacao:

    def __init__(self, arquivo):
        self.cidades = []
        self.cidade_inicial = None
        self.matriz_adjacencias = []
        self.linhas = 0
        self.cidade_aleatoria = None
        self.lista_caminhos = []
        self.arquivo = arquivo

    def parte_1(self):
        self.criacao_grafo()
        self.criacao_matriz_grafo()
        self.criacao_caminhos_iniciais()

    # criar o grafo  
    def criacao_grafo(self):
        with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
            while True:
                linha = arquivo.readline() # lê linha por linha

                if not linha:
                    break

                linha_limpa = linha.split() #tira os espaços desnecessários da linha lida

                if len(linha_limpa) == 3: #se a linha tiver os 3 componentes, lê os componentes
                    id, x, y = linha_limpa
                    cidade = Cidade(int(id), float(x), float(y))
                    self.cidades.append(cidade) # cria a cidade e adiciona na lista de cidades

    def sorteio_ponto_inicial(self):
        self.cidade_inicial = random.choice(self.cidades) #faz o sorteio de uma das cidades e escolhe como ponto inicial

    # cálculo de distância
    def calculo_distancia(self, c1, c2):
        id1, x1, y1 = c1.id, c1.x, c1.y
        id2, x2, y2 = c2.id, c2.x, c2.y

        return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5) #retorna a distância entre as duas cidades passadas como parâmetro
    
    # criação da matriz de adjacências que representa o grafo
    def criacao_matriz_grafo(self):
        self.linhas = len(self.cidades)
        self.matriz_adjacencias = [[0.0 for _ in range(self.linhas + 1)] for _ in range(self.linhas + 1)] #cria uma matriz quadrada com o tamanho da lista de cidades

        for cidade in self.cidades:
            cidade.preencher_lista(self.linhas) #preenche a lista de adjacências de cada cidade
            for adjacente in self.cidades:
                if cidade != adjacente: #se não for a mesma cidade referida (d = 0), calcula a distância entre elas e adiciona posição correta da matriz
                    cidade.lista_adjacencias[adjacente.id] = self.calculo_distancia(cidade, adjacente)
            self.matriz_adjacencias[cidade.id] = cidade.lista_adjacencias
    
    # criação dos caminhos iniciais
    def criacao_caminhos_iniciais(self):
        self.sorteio_ponto_inicial()
        for _ in range(100):
            novo_caminho = Caminho()
        
            # filtra todas as cidades que não são a inicial
            cidades_meio = [c for c in self.cidades if c.id != self.cidade_inicial.id]
        
            # embaralha apenas o meio do caminho
            random.shuffle(cidades_meio)

            # monta a rota completa: início + meio + retorno ao Início
            rota_final = [self.cidade_inicial] + cidades_meio + [self.cidade_inicial]
        
            # atribui a lista
            novo_caminho.cidades = rota_final
        
            # calcula a distância total
            novo_caminho.distancia_total = self.calculo_distancia_total_caminho(novo_caminho)

            self.lista_caminhos.append(novo_caminho)

    def calculo_distancia_total_caminho(self, caminho):
        distancia_total = 0

        for i in range(len(caminho.cidades) - 1):
            distancia_total = distancia_total + self.matriz_adjacencias[caminho.cidades[i].id][caminho.cidades[i + 1].id]

        return distancia_total
        