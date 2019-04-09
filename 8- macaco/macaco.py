class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        self.bucho = alimento
        return self.bucho

    def ver_bucho(self, alimento):
        return self.comer(alimento)
        
