class Usuario:
    def __init__(self, prim_nome, ult_nome):
        self.prim_nome = prim_nome
        self.ult_nome = ult_nome

    def descrever_usuario(self):
        return f'{self.prim_nome} {self.ult_nome}'

    def saudacao(self):
        return f'Olá {self.descrever_usuario()}!'
