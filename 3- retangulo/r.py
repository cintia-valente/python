class Retangulo:
    lista = []
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def lados(self):
        return [self.base, self.altura]

    def mudar_lados(self, ladoA, ladoB):
        self.base = ladoA
        self.altura = ladoB
        return[self.base, self.altura]
               
    def retorna_lados(self, b, h):
        novo_lado = self.mudar_lados(b, h)
        return novo_lado
    
    def calcula_area(self, b, h, lista):
        return lista[0] * lista[1]

    def calcula_perimetro(self, x, y, lista):
        return 2 * (lista[0] + lista[1])
