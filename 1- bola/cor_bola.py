class Bola:
    def __init__(self, cor, c, material):
        self.cor = cor
        self.__circunferencia = c
        self.__material = material

    @property
    def atributos(self):
        return [self.cor, self.__circunferencia, self.__material]

    @atributos.setter
    def atributos(self, c, material):
        self.__circunferencia = c
        self.__material = material

    def troca_cor(self, cor):
        self.cor = cor
        return self.cor

    def mostra_cor(self, cor):
        self.troca_cor(cor)
        return f'A cor atual é {self.cor}'


