import unittest

from ponto import Retangulo

class TestRetangulo(unittest.TestCase):

    def setUp(self):
        self.ret_a = Retangulo(20, 10, 2, 4)
        self.ret_b = Retangulo(40, 20, 3, 6)

    def test_valores(self):
        self.assertEqual(self.ret_a.imprime_valores(), (2, 4))
        self.assertEqual(self.ret_b.imprime_valores(), (3, 6))

    def test_centro(self):
        self.assertEqual(self.ret_a.centro(), (12, 9))
        self.assertEqual(self.ret_b.centro(), (23, 16))
        
if __name__ == '__main__':
    unittest.main()
