import unittest

from modela_quadrado import Quadrado

class TestQuadrado(unittest.TestCase):
    
    def setUp(self):
        self.quad = Quadrado(4)

    def test_ladosquad(self):
        self.assertEqual(self.quad.getLadosquad(), 4)
        
    def test_muda_lado(self):
        self.assertEqual(self.quad.mudar_lado(6), 6)

    def test_retorna_lado(self):
        self.assertEqual(self.quad.retorna_valor(6),
        'O novo lado é igual a 6')

    def test_valor_area(self):
        self.assertEqual(self.quad.calcula_area(6),
        'A área é igual a 36')

if __name__ == '__main__':
    unittest.main()
