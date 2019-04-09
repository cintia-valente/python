class ContaCorrente:
    def __init__(self, num, nome, saldo):
        self.numero = num
        self.nome = nome
        self.saldo = 0
    
    def alterar_nome(self, nome):
        self.nome = nome
        return self.nome

    def deposito(self, valor_deposito):
        self.saldo = valor_deposito
        return self.saldo

    def saque(self, valor_saque):
        saque = valor_saque
        return saque

    def saldo_atual(self, valor_deposito, valor_saque):
        return self.deposito(valor_deposito) - self.saque(valor_saque)

    
        
        
