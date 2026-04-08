# Arquivo da entidade da classe Cidade, que possuira id, fitness, coordenadas x e y, e um dicionario de distancias para as outras cidades

class Cidade:
    def __init__(self, id, x, y, dist):
        self.id = id
        self.x = x
        self.y = y
        self.dist = dist

    def calcular_distancia(self, outra_cidade):
        return ((self.x - outra_cidade.x) ** 2 + (self.y - outra_cidade.y) ** 2) ** 0.5

    def __repr__(self):
        return f"Cidade(id={self.id}, x={self.x}, y={self.y})"