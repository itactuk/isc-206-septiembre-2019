
class Tablero:
    def __init__(self):
        cantidad_columnas = 8
        cantidad_filas = 8
        self.casillas = []
        for i in range(cantidad_columnas):
            self.casillas[i] = []
            for j in range(cantidad_filas):
                self.casillas[i].append(None)

