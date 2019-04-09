import unittest

from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):

    def setUp(self):
        self.f = Funcionario('Cíntia', 3.500)

    def test_nome(self):
        self.assertEqual(self.f.retorna_nome(), 'Cíntia')

    def test_salario(self):
        self.assertEqual(self.f.retorna_salario(), 3.500)

    def test_aumento(self):
        self.assertEqual(self.f.aumentar_salario(10), 3.8500000000000005)

if __name__ == '__main__':
    unittest.main()
