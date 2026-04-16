# Arquivo da entidade da classe Cidade, que possuira id, fitness, coordenadas x e y, e um dicionario de distancias para as outras cidades

class Cidade:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.lista_adjacencias = []
    
    def preencher_lista(self, linhas):
            self.lista_adjacencias = [0.0] * (linhas + 1)