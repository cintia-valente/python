class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def canal(self):
        return self.canal

    def aumentar(self, volume):
        self.volume += volume
        return self.volume

    def diminuir(self, volume):
        self.volume -= volume
        return self.volume
        

    
        
