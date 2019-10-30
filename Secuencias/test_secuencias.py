import unittest

class MisPruebas(unittest.TestCase):
    def test_indice_lista(self):
        # esto tambien funciona para tuplas
        lista = [1,3,5,-2]
        self.assertEqual(-2, lista[3])

    def test_indice_negativo(self):
        # esto tambien funciona para tuplas
        lista = [1, 3, 5, -2]
        self.assertEqual(5, lista[-2])

    def test_slicing_lista(self):
        # esto tambien funciona para tuplas
        lista = [1, 3, 5, -2, 7, 77, 8]
        self.assertEqual([5, -2, 7], lista[2:5])

    def test_append_list(self):
        # NO funciona para tuplas
        lista = [1, 3, 5, -2]
        self.assertEqual([1, 3, 5, -2], lista)
        lista.append(4)
        self.assertEqual([1, 3, 5, -2, 4], lista)

    def test_insert_lista(self):
        lista = [1, 3, 5, -2]
        self.assertEqual([1, 3, 5, -2], lista)
        lista.insert(2, 4)
        self.assertEqual([1, 3, 4, 5, -2], lista)

    def test_remove_lista(self):
        lista = [1, 3, 5, -2]
        self.assertEqual([1, 3, 5, -2], lista)
        lista.remove(3)
        self.assertEqual([1, 5, -2], lista)

    def test_len_lista(self):
        lista = [2, 3, 4, [2, 3, 4, 5, 8]]
        self.assertEqual(4, len(lista))
        self.assertEqual(5, len(lista[3]))

    def test_actualiza_diccionario(self):
        diccionario = {'nombre': 'maria', 'edad': 21}
        diccionario['edad'] = 22
        self.assertEqual({'nombre': 'maria', 'edad': 22}, diccionario)

    def test_crea_llave_diccionario(self):
        diccionario = {'nombre': 'maria', 'edad': 21}
        diccionario['hijos'] = 2
        self.assertEqual({'nombre': 'maria', 'edad': 21, 'hijos': 2}, diccionario)

    def test_elimina_llave_dict(self):
        diccionario = {'nombre': 'maria', 'edad': 21}
        del diccionario['edad']
        self.assertEqual({'nombre': 'maria'}, diccionario)

    def test_len_dict(self):
        diccionario = {'nombre': 'maria', 'edad': 21}
        self.assertEqual(2, len(diccionario))

    def test_string_find(self):
        texto = "hola como estas"
        self.assertEqual(3, texto.find("a"))

    def test_string_replace(self):
        texto = "hola como estas"
        texto = texto.replace("a", "o")
        self.assertEqual("holo como estos", texto)

    def test_string_split(self):
        texto = "hola como estas"
        self.assertEqual(["hola", "como", "estas"], texto.split(" "))

    def test_string_slicing(self):
        texto = "hola como estas"
        self.assertEqual("a como est", texto[3:-2])
