import unittest
import FuncionesIntro.libreria_ecuaciones as lib

class MiPrueba(unittest.TestCase):

    def test_prueba_ecuacion_primerg(self):
        resultado = lib.raices_eq_primer_grado(4,2)
        self.assertEqual(-0.5, resultado)

    def test_prueba_cuad(self):
        x1, x2 = lib.raices_eq_cuadratica(2,9,10)
        self.assertEqual(x1, -2)
        self.assertEqual(x2, -2.5)
