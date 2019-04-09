class Retangulo:
    def __init__(self, l, h, x, y):
        self.larg = l
        self.altura = h
        self.ponto_inicial= Ponto(x, y)

    def imprime_valores(self):
        return self.ponto_inicial.valores()
    
    def centro(self):
        self.ponto_inicial.x += (self.larg / 2)
        self.ponto_inicial.y += (self.altura / 2)
        return self.ponto_inicial.x, self.ponto_inicial.y


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def valores(self):
        return self.x, self.y
    
          
   


    
        
