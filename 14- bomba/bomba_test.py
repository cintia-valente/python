import unittest

from bomba import BombaCombustivel

class TestBomba(unittest.TestCase):

    def setUp(self):
        self.bomba = BombaCombustivel('alcool', 4.00, 1000)

    def test_abastecer_v(self):
        self.assertEqual(self.bomba.abastecer_por_valor(40.00), (10, 990))

    def test_abastecer_l(self):
        self.assertEqual(self.bomba.abastecer_por_litro(10), (40.00, 990))

    def test_valor(self):
        self.assertEqual(self.bomba.alterar_valor(5.00), 5.00)

    def test_combustivel(self):
        self.assertEqual(self.bomba.alterar_combustivel('diesel'), 'diesel')

    def test_qtd_combustivel(self):
        self.assertEqual(self.bomba.alterar_qtd_comb(10), 990)

if __name__ == '__main__':
    unittest.main()
        
