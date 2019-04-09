import unittest

from fazenda import Fazenda

class TestFazenda(unittest.TestCase):

    def setUp(self):
        self.fofucho = Fazenda('fofucho', 30, 10)
        self.bbzinho = Fazenda('bbzinho', 15, 35)
        self.fazendinha = Fazenda(self.fofucho, self.bbzinho)
        
    def test_preenche(self):
        self.assertEqual(self.fazendinha.insere_nome(['fofucho', 30, 10], ['bbzinho', 15, 35]),
                                                     [['fofucho', 30, 10], ['bbzinho', 15, 35]])

    def test_nome(self):
        self.assertEqual(self.fazendinha.alterar_nome(['fofucho', 30, 10], ['bbzinho', 15, 35], ['bebe', 'gatinho']),
                                                      [['bebe', 30, 10], ['gatinho', 15, 35]])

    def test_fome(self):
        self.assertEqual(self.fazendinha.alterar_fome(['fofucho', 30, 10], ['bbzinho', 15, 35], [40, 5]),
                                                      [['fofucho', 40, 10], ['bbzinho', 5, 35]])   

    def test_tempo(self):
        self.assertEqual(self.fazendinha.tempo_brincar(['fofucho', 30, 10], ['bbzinho', 15, 35], [5, 20]),
                                                      [['fofucho', 40, 15], ['bbzinho', 5, 55]])   
                                 
    def test_humor(self):
        self.assertEqual(self.fazendinha.calcula_humor(['fofucho', 40, 15], ['bbzinho', 5, 55], [5, 10],
                                                       'MUITO TRISTE :(', 'ESTOU FELIZ :)'))

if __name__ == '__main__':
    unittest.main()


        

        

        

        
