class Restaurante:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def descreve(self):
        return [self.nome, self.tipo]

    def open_restaurante(self):
        return 'O restaurante está aberto'

    
