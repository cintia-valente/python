class Pessoa:
    def __init__(self, nome, idade, peso, alt):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = alt

    def envelhecer(self, idade_mais):
        self.idade += idade_mais
        return self.idade
            
    def crescer(self, idade_mais):
        if self.envelhecer(idade_mais) < 21:
            self.altura += 0.05
        return self.altura
            
    def engordar(self, kg_mais):
        self.peso += kg_mais
        return self.peso

    def emagrecer(self, kg_menos):
        self.peso -= kg_menos
        return self.peso
            
            
