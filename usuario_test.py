import unittest

from usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario('Cíntia', 'Valente')

    def test_imprime_nome_completo(self):
        self.assertEqual(self.usuario.descrever_usuario(), 'Cíntia Valente')
        
    def test_imprime_saudacao(self):
        self.assertEqual(self.usuario.saudacao(), 'Olá Cíntia Valente, você será Engenheira da Globo!')


if __name__ == '__main__':
    unittest.main()
