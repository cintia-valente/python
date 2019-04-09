import unittest

from tv import TV

class TestTV(unittest.TestCase):

    def setUp(self):
        self.tv1 = TV(5, 10)

    def test_canal(self):
        self.assertEqual(self.tv1.canal, 5)

    def test_aumenta(self):
        self.assertEqual(self.tv1.aumentar(15), 25)

    def test_diminui(self):
        self.assertEqual(self.tv1.diminuir(6), 4)

if __name__ == '__main__':
    unittest.main()
