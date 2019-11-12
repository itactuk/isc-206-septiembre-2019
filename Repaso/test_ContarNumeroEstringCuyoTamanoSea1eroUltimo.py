import unittest
import Repaso.ContarNumeroEstringCuyoTamanoSea1eroUltimo as fun

# Hacer un problema que cuente cuantos elementos en una lista tienen un tamano menor que 20
# y su segundo caracter es igual igual al primero

class PruebaEje(unittest.TestCase):
    def test_vacio(self):
        entrada = ["afadf", "fadfsdgf", "434325", "ads"]
        salida = 0
        self.assertEqual(salida, fun.contar(entrada))
    def test_1(self):
        entrada = ["aaadf", "fadfsdgf", "434325", "ads"]
        salida = 1
        self.assertEqual(salida, fun.contar(entrada))
    def test_2(self):
        entrada = ["aaadfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd", "fadfsdgf", "434325", "ads"]
        salida = 0
        self.assertEqual(salida, fun.contar(entrada))

