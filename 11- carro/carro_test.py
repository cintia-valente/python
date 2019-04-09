import unittest

from carro import Carro

class TestCarro(unittest.TestCase):

    def setUp(self):
        self.onix = Carro(15, 0)
        self.toyota = Carro(10, 0)
        
    def test_abastecer(self):
        self.assertEqual(self.onix.adicionar_gasosa(20), 20)
        self.assertEqual(self.toyota.adicionar_gasosa(30), 30)

    def test_andar(self):
        self.assertEqual(self.onix.andar(105), 7)
        self.assertEqual(self.toyota.andar(100), 10)

    def test_obter(self):
        self.assertEqual(self.onix.obter_gasosa(105, 20), 13)
        self.assertEqual(self.toyota.obter_gasosa(100, 30), 20)

if __name__ == '__main__':
    unittest.main()

    
    
