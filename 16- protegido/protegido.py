quantidade = 50
class Tamagushi:
    def __init__(self, nome, fome, saude, idade, come, tmp):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__come = come
        self.__tmp = tmp

    def getImprime(self):
        v = str(f'O nome é {self.__nome}'
                  f'Nível de fome de {self.__nome} é {self.__fome}'
                  f'Nivel de saúde de {self.__nome} é {self.__saude}'
                  f'A idade de {self.__nome} é {self.__idade}'
                  f'Proporção de comida recebida pelo {self.__nome} foi de {self.__come}'
                  f'O {self.__nome} ficou brincando durante {self.__tmp}')
        return v
       
        
    def alterar_nome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome

    def alterar_fome(self, qtd, nivel_fome):
        self.__fome = nivel_fome
        if self.comida(qtd) < quantidade:
            for i in range(self.__fome, quantidade):
                self.__fome -= 1
            return self.__fome
        return self.__fome

    def alterar_saude(self, nivel_saude):
        self.__saude = nivel_saude
        return self.__saude

    def alterar_idade(self, nova_idade):
        self.__idade = nova_idade
        return self.__idade

    def comida(self, qtd_comida):
        self.__come = qtd_comida
        return self.__come

    def num_tempo(self, tmp):
        self.__tempo = tmp
        return self.__tempo
    
    def calcula_humor(self, f, n, s, t):
        humor = self.alterar_fome(f, n) + self.alterar_saude(s) + self.num_tempo(t)
        if self.num_tempo(t) > quantidade:
            for i in range(quantidade):
                humor -= 1
                
        if humor >= 150:
            return f'ESTOU TRISTE :('

        else:
            return f'MUITO FELIZ :)'
            
        
            
