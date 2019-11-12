import unittest
import Torneo.primo_ejemplo as p

class PruebaPrimo(unittest.TestCase):

    def test_ejemplo(self):
        entrada = 13195
        salida = 29
        self.assertEqual(salida, p.halla_factor_primo_mas_grande(entrada))
