import unittest

from macaco import Macaco

class TestMacaco(unittest.TestCase):

    def setUp(self):
        self.macaco_a = Macaco('king', 'banana')
        self.macaco_b = Macaco('kong', 'maça')
        self.macaco_c = Macaco('mico', 'chocolate')
        self.macaco_d = Macaco('nulo', 'macaco_a')

    def test_comer(self):
        self.assertEqual(self.macaco_a.comer('banana'), 'banana')
        self.assertEqual(self.macaco_b.comer('maça'), 'maça')
        self.assertEqual(self.macaco_c.comer('chocolate'), 'chocolate')
        self.assertEqual(self.macaco_a.comer(self.macaco_a), self.macaco_a)

    def test_bucho(self):
        self.assertEqual(self.macaco_a.ver_bucho('banana'), 'banana')
        self.assertEqual(self.macaco_b.ver_bucho('maça'), 'maça')
        self.assertEqual(self.macaco_c.ver_bucho('chocolate'), 'chocolate')
        self.assertEqual(self.macaco_a.ver_bucho(self.macaco_a), self.macaco_a)

if __name__ == '__main__':
    unittest.main()

