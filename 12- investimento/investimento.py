meses = 5
class ContaInvestimento:
    def __init__(self, num, nome, saldo, tx):
        self.numero = num
        self.nome = nome
        self.saldo = saldo
        self.taxa = tx

    def adicione_juros(self):
        tx = self.taxa / 100
        juros = self.saldo * tx * meses
        return juros
        
    def alterar_nome(self, nome):
        self.nome = nome
        return self.nome

    def deposito(self, valor_deposito):
        self.saldo = valor_deposito
        return self.saldo

    def saque(self, valor_saque):
        saque = valor_saque
        return saque
'''
    def saldo_atual(self, valor_deposito, valor_saque):
        v = self.saldo + self.deposito(valor_deposito)
        x = v - self.saque(valor_saque)
        t = x - self.adicione_juros()
        return t
'''
    
        
        
