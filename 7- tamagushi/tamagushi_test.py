import unittest

from tamagushi import Tamagushi

class TestTamagushi(unittest.TestCase):

    def setUp(self):
        self.fofo = Tamagushi('fofucho', 500, 30, 5)
        self.lindinho = Tamagushi('bbzinho', 50, 80, 10)

    def test_nome(self):
        self.assertEqual(self.fofo.alterar_nome('bebe'), 'bebe')
        self.assertEqual(self.fofo.alterar_nome('gatinho'), 'gatinho')

    def test_fome(self):
        self.assertEqual(self.fofo.alterar_fome(200), 200)
        self.assertEqual(self.lindinho.alterar_fome(10), 10)

    def test_saude(self):
        self.assertEqual(self.fofo.alterar_saude(15), 15)
        self.assertEqual(self.lindinho.alterar_saude(120), 120)

    def test_idade(self):
        self.assertEqual(self.fofo.alterar_idade(5), 5)
        self.assertEqual(self.lindinho.alterar_idade(8), 8)

    def test_humor(self):
        self.assertEqual(self.fofo.calcula_humor(200, 15), 'ESTOU TRISTE :(')
        self.assertEqual(self.lindinho.calcula_humor(10, 120), 'MUITO FELIZ :)')

if __name__ == '__main__':
    unittest.main()

    
        

        

        

        
