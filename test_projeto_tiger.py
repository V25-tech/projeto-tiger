import unittest
from projeto_tiger import calcular_media, verificar_aprovacao

class TestProjetoTiger(unittest.TestCase):
    def test_calcular_media(self):
        self.assertEqual(calcular_media([8.0, 7.0, 9.0]), 8.0)
        self.assertEqual(calcular_media([]), 0.0)
        self.assertAlmostEqual(calcular_media([6.5, 7.5]), 7.0)

    def test_verificar_aprovacao(self):
        self.assertEqual(verificar_aprovacao(8.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(6.5), "Reprovado")
        self.assertEqual(verificar_aprovacao(7.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(7.5, media_minima=8.0), "Reprovado")

if __name__ == "__main__":
    unittest.main()
