class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterar_fome(self, nivel_fome):
        self.fome = nivel_fome
        return self.fome

    def alterar_saude(self, nivel_saude):
        self.saude = nivel_saude
        return self.saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return nova_idade

    def calcula_humor(self, f, s):
        humor = self.alterar_fome(f) + self.alterar_saude(s)
        if humor >= 150:
            return f'ESTOU TRISTE :('

        else:
            return f'MUITO FELIZ :)'
            
        
            
