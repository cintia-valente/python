import unittest

from conta_corrente import ContaCorrente

class TestCC(unittest.TestCase):

    def setUp(self):
        self.cc = ContaCorrente(42424, 'Cíntia', 0)

    def test_nome(self):
        self.assertEqual(self.cc.alterar_nome('Yasmim'), 'Yasmim')
       
    def test_deposito(self):
        self.assertEqual(self.cc.deposito(1200), 1200)

    def test_saque(self):
        self.assertEqual(self.cc.saque(200), 200)

    def test_saldo_atual(self):
        self.assertEqual(self.cc.saldo_atual(1200, 200), 1000)

if __name__ == '__main__':
    unittest.main()
