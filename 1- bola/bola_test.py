import unittest

from cor_bola import Bola

class TestBola(unittest.TestCase):

    def setUp(self):
        self.bola1 = Bola('azul', 25, 'couro')

    def test(self):
        self.assertEqual(self.bola1.troca_cor('rosa'), 'rosa')

    def test_2(self):
        self.assertEqual(self.bola1.mostra_cor('rosa'), 'A cor atual é rosa')

if __name__ == '__main__':
    unittest.main()
