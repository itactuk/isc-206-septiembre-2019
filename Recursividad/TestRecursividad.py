import Recursividad.EjemploRecursividad as ej
import unittest

class Pruebas(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(120, ej.factorial_recursivo(5))
        self.assertEqual(1, ej.factorial_recursivo(0))
        self.assertEqual(24, ej.factorial_recursivo(4))
