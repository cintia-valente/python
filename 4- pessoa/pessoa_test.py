import unittest

from pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def setUp(self):
        self.p1 = Pessoa('Camila', 15, 60, 1.60)

    def test_envelhecer(self):
        self.assertEqual(self.p1.envelhecer(5), 20)
        
    def test_crescer(self):
        self.assertEqual(self.p1.crescer(5), 1.6500000000000001)

    def test_engordar(self):
        self.assertEqual(self.p1.engordar(10.0), 70)

    def test_emagrecer(self):
        self.assertEqual(self.p1.emagrecer(5.0), 55)

if __name__ == '__main__':
    unittest.main()

   
