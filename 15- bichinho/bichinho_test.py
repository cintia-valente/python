import unittest

from bichinho import Tamagushi

class TestTamagushi(unittest.TestCase):

    def setUp(self):
        self.fofo = Tamagushi('fofucho', 500, 30, 5, 40, 20)
        self.lindinho = Tamagushi('bbzinho', 50, 80, 10, 20, 15)

    def test_nome(self):
        self.assertEqual(self.fofo.alterar_nome('bebe'), 'bebe')
        self.assertEqual(self.fofo.alterar_nome('gatinho'), 'gatinho')

    def test_fome(self):
        self.assertEqual(self.fofo.alterar_fome(80, 200), 200)
        self.assertEqual(self.lindinho.alterar_fome(20, 40), 30)

    def test_saude(self):
        self.assertEqual(self.fofo.alterar_saude(15), 15)
        self.assertEqual(self.lindinho.alterar_saude(60), 60)

    def test_idade(self):
        self.assertEqual(self.fofo.alterar_idade(5), 5)
        self.assertEqual(self.lindinho.alterar_idade(8), 8)
        
    def test_comida(self):
        self.assertEqual(self.fofo.comida(80), 80)
        self.assertEqual(self.fofo.comida(20), 20)

    def test_tempo(self):
        self.assertEqual(self.fofo.num_tempo(30), 30)
        self.assertEqual(self.fofo.num_tempo(25), 25)
        
    def test_humor(self):
        self.assertEqual(self.fofo.calcula_humor(80, 200, 15, 30), 'ESTOU TRISTE :(')
        self.assertEqual(self.lindinho.calcula_humor(20, 40, 60, 25), 'MUITO FELIZ :)')

if __name__ == '__main__':
    unittest.main()

    
        

        

        

        
