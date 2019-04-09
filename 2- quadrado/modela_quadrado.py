class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def getLadosquad(self):
        return self.__lado
    
    def mudar_lado(self, lado):
        self.__lado = lado
        return self.__lado

    def retorna_valor(self, lado):
        l = self.mudar_lado(lado)
        return f'O novo lado é igual a {lado}'

    def calcula_area(self, lado):
        return f'A área é igual a {self.mudar_lado(lado) * self.mudar_lado(lado)}'
