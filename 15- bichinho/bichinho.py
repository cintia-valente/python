quantidade = 50
class Tamagushi:
    def __init__(self, nome, fome, saude, idade, come, tmp):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.come = come
        self.tmp = tmp

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterar_fome(self, qtd, nivel_fome):
        self.fome = nivel_fome
        if self.comida(qtd) < quantidade:
            for i in range(self.fome, quantidade):
                self.fome -= 1
            return self.fome
        return self.fome

    def alterar_saude(self, nivel_saude):
        self.saude = nivel_saude
        return self.saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return self.idade

    def comida(self, qtd_comida):
        self.come = qtd_comida
        return self.come

    def num_tempo(self, tmp):
        self.tempo = tmp
        return self.tempo
    
    def calcula_humor(self, f, n, s, t):
        humor = self.alterar_fome(f, n) + self.alterar_saude(s) + self.num_tempo(t)
        if self.num_tempo(t) > quantidade:
            for i in range(quantidade):
                humor -= 1
                
        if humor >= 150:
            return f'ESTOU TRISTE :('

        else:
            return f'MUITO FELIZ :)'
            
        
            
