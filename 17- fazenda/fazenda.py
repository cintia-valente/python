bichos = []
aux = []
quantidade = 50
class Fazenda:
    def __init__(self, nome, fome, tedio):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio
        
    def preenche(self, nome, fome, tedio):
        for pos in range(0, 1):
            bichos.append(nome)
            bichos.append(fome)
            bichos.append(tedio)
        print(bichos)
        return bichos
    
    def paux(self, aux, nome):
        for pos in range(0, 1):
           aux.append(nome)
        print(aux)
        return aux

    def alterar_nome(self, bichos, aux):
        for i in range(0, len(bichos)):
            for j in range(0, len(bichos[i])):
                bichos[i][0] = aux[i]
        return bichos

    def paux(self, aux, fome):
        for pos in range(0, 1):
           aux.append(fome)
        print(aux)
        return aux

    def alterar_fome(self, bichos, aux):
        for i in range(0, len(bichos)):
            for j in range(0, len(bichos[i])):
                bichos[i][1] = aux[i]
        return bichos

    
    def paux(self, aux, tedio):
        for pos in range(0, 1):
           aux.append(tedio)
        print(aux)
        return aux
    
    def tempo_brincar(self, bichos, aux):
        for i in range(0, len(bichos)):
            for j in range(0, len(bichos[i])):
                bichos[i][2] += aux[i]
        return bichos

    def calcula_humor(self, bichos, aux):
        humor = self.alterar_fome(bichos, aux) + self.tempo_brincar(bixos, aux)
        for b in bichos:
            if self.tempo_brincar(bixos, aux) > quantidade:
                for i in range(quantidade):
                    humor -= 1
                
            if humor >= 150:
                return f'ESTOU TRISTE :('

            else:
                return f'MUITO FELIZ :)'
            
        
            
