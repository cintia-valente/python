import unittest

from restaurante import Restaurante

class TestRestaurante(unittest.TestCase):

    def setUp(self):
        self.restaurante1 = Restaurante('melhor sabor', 'brasileiro')
        self.restaurante2 = Restaurante('tudo acaba em pizza', 'italiano')

    def test_imprime_atributos_do_restaurante(self):
        self.assertEqual(self.restaurante1.descreve(), ['melhor sabor', 'brasileiro'])
        self.assertEqual(self.restaurante2.descreve(), ['tudo acaba em pizza', 'italiano'])

    def test_imprime_mensagem(self):
        self.assertEqual(self.restaurante1.open_restaurante(), 'O restaurante está aberto')
        self.assertEqual(self.restaurante2.open_restaurante(), 'O restaurante está aberto')

if __name__ == '__main__':
    unittest.main()
