import unittest

from investimento import ContaInvestimento

class TestInvestimento(unittest.TestCase):

    def setUp(self):
        self.inv = ContaInvestimento(42424, 'Cíntia', 1000, 10)

    def test_juros(self):
        self.assertEqual(self.inv.adicione_juros(), 500)
        
    def test_nome(self):
        self.assertEqual(self.inv.alterar_nome('Yasmim'), 'Yasmim')
       
    def test_deposito(self):
        self.assertEqual(self.inv.deposito(200), 200)

    def test_saque(self):
        self.assertEqual(self.inv.saque(100), 100)

    def test_saldo_atual(self):
        self.assertEqual(self.inv.saldo_atual(200, 100), 600)

if __name__ == '__main__':
    unittest.main()

