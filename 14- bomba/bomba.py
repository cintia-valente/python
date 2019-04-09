class BombaCombustivel:
    def __init__(self, tipo, valor_litro, qtd_litro):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.qtd_litro = qtd_litro

    def abastecer_por_valor(self, valor):
        litro = valor / self.valor_litro
        valor_atual = self.alterar_qtd_comb(litro)
        return litro, valor_atual

    def abastecer_por_litro(self, litro):
        valor = litro * self.valor_litro
        valor_atual = self.alterar_qtd_comb(litro)
        return valor, valor_atual

    def alterar_valor(self, novo_valor):
        self.valor = novo_valor
        return self.valor

    def alterar_combustivel(self, novo_tipo):
        self.tipo = novo_tipo
        return self.tipo

    def alterar_qtd_comb(self, litro):
        total_comb = self.qtd_litro - litro
        return total_comb
