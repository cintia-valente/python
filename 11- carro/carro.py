class Carro:
    def __init__(self, consumo, combustivel):
        self.consumo = consumo
        self.combustivel = 0

    def adicionar_gasosa(self, comb):
        self.combustivel = comb
        return self.combustivel

    def andar(self, km):
        litro = 0
        for i in range(0, km, self.consumo):
            litro += 1
        return litro

    def obter_gasosa(self, km, comb):
        return self.adicionar_gasosa(comb)- self.andar(km)

    

