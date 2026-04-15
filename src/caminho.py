from cidade import Cidade

class Caminho:
    def __init__(self):
        self.cidades = []
        self.fitness = 0
        self.distancia_total = 0
    
    def preenchimento_caminho(self, n_cidades):
        self.cidades = [None] * (n_cidades + 1)