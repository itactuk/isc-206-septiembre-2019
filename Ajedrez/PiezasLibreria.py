from enum import Enum

from Ajedrez.TableroLibreria import Tablero


class ColorPieza(Enum):
    BLANCAS = 0
    NEGRAS = 0


class Pieza:
    def __init__(self, color: ColorPieza):
        self.color = color


class Torre(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """


class Alfil(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """


class Caballo(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """


class Peon(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """


class Rey(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """


class Reina(Pieza):
    @staticmethod
    def es_jugada_valida(tablero: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
        """

        :param tablero: el tablero donde se encuentra la pieza
        :param columna_actual:  la columna donde se encuentra la pieza
        :param fila_actual: la fila donde se encuentra la pieza
        :param nueva_columna: la columna donde se moverá la pieza
        :param nueva_fila: la fila donde se moverá la pieza
        :return: True si la jugada es valida y False si no lo es
        """
