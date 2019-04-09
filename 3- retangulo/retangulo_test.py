import unittest

from r import Retangulo

class TestRetangulo(unittest.TestCase):

    def setUp(self):
        self.ret = Retangulo(4, 2)

    def test_mudar(self):
        self.assertEqual(self.ret.mudar_lados(8, 3), [8, 3])

    def test_retorna(self):
        self.assertEqual(self.ret.retorna_lados(8, 3), [8, 3])

    def test_area(self):
        self.assertEqual(self.ret.calcula_area(8, 3, [8, 3]), 24)

    def test_perimetro(self):
        self.assertEqual(self.ret.calcula_perimetro(8, 3, [8, 3]), 22)

if __name__ == '__main__':
    unittest.main()
