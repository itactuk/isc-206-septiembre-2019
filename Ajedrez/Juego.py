from .TableroLibreria import Tablero

mi_tablero = Tablero()


def main():
    turno_jugador_blancas = True
    jugador_blancas = input("Digite nombre jugador blancas: ")
    jugador_negras = input("Digite nombre jugador negras: ")
    colocar_fichas_en_posicion_inicial(mi_tablero)
    while True:
        imprime_tablero(mi_tablero)
        if turno_jugador_blancas:
            print(f"Le toca a las blancas ({jugador_blancas})")
        else:
            print(f"Le toca a las negras ({jugador_negras})")
        jugada_valida = False
        while not jugada_valida:
            columna_pieza, fila_pieza = leer_coordenada_notacion_algebraica("Digite jugada en notacion algebraica: ")
            mover_a_columna, mover_a_fila = leer_coordenada_notacion_algebraica("Digite jugada en notacion algebraica: ")
            resultado = mover_pieza(mi_tablero, columna_pieza, fila_pieza, mover_a_columna, mover_a_fila)
            if resultado == True:
                jugada_valida = True
            else:
                print(resultado)
        if esta_en_jaquemate(mi_tablero):
            if turno_jugador_blancas:
                ganador = jugador_blancas
            else:
                ganador = jugador_negras
            print("Jaque Mate. Ganó " + ganador + ". Fin del juego")
            break
        elif esta_en_jaque(mi_tablero):
            print("Jaque")
        turno_jugador_blancas = not turno_jugador_blancas


def es_pieza_seleccionada_valida(tablero: Tablero, columna: int, fila: int, turno_blancas: bool):
    """

    :param tablero:
    :param columna:
    :param fila:
    :param turno_blancas:
    :return:
    """


def leer_coordenada_notacion_algebraica(mensaje_usuario: str):
    """
    Lee coordena en notacion algebraica
    :return: Retorna coordenada en indices de matrices (0,1,2,3,4,5,6,7), (0,1,2,3,4,5,6,7)
    """
    coordenada_valida = False
    while not coordenada_valida:
        jugada = input(mensaje_usuario)
        if len(jugada) == 2:
            col = jugada[0]
            fil = int(jugada[1])
            if col in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] and fil in range(0, 9):
                coordenada_valida = True
    col, fil = convierte_notacion_algebraica_a_indices_de_matrices(col, fil)
    return col, fil


def convierte_notacion_algebraica_a_indices_de_matrices(col_algebraica: str, fila_algebraica: int):
    """
    Convierte de notacion algebraica (a1, a2, a3,...) a representacion de matriz (0,1;0,2;0,3,...)
    :param col_algebraica:
    :param fila_algebraica:
    :return: tupla col, fil
    """


def imprime_tablero(tablero: Tablero):
    """
    muestra el tablero en la pantalla. Incluir letras de notacion algebraicas https://es.wikipedia.org/wiki/Notaci%C3%B3n_algebraica
    :param tablero:
    :return:
    """


def esta_en_jaquemate(tablero: Tablero):
    """
    Verifica si uno de los jugadores esta en jaque
    :param tablero:
    :return:
    """


def esta_en_jaque(tablero: Tablero):
    """
    Verifica si uno de los jugares esta en jaque
    :param tablero:
    :return:
    """


def esta_ahogado(tablero: Tablero, turno_blancas: bool):
    """
    Verifica si el juego esta empatado. Esto ocurre cuando al jugador que le toca jugar no puede jugar y no esta en jaque
    :param turno_blancas:
    :param tablero:
    :return:
    """


def colocar_fichas_en_posicion_inicial(tablero: Tablero):
    tablero.casillas[0]


def colocar_pieza(tablerito: Tablero, columna: int, fila: int):
    """
    Posiciona una pieza en una casilla especifica del tablero
    :param tablerito:
    :param columna: Debe de ser un numero que represente el indice de la casilla (0, 1, 2, 3, 4, 5, 6, 7)
    :param fila: Debe de ser un numero que represente el indice de la casilla (0, 1, 2, 3, 4, 5, 6, 7)
    :return:
    """
    pass


def mover_pieza(tablerito: Tablero, columna_actual: int, fila_actual: int, nueva_columna: int, nueva_fila: int):
    """
    mueve una pieza y verifica que sea una jugada válida.
    Se recomienda usar la funcion esta en jaque y demas funciones para determinar si una jugada es valida
    :param nueva_fila:
    :param nueva_columna:
    :param fila_actual:
    :param columna_actual:
    :param tablerito:
    :return: True si se pudo mover la pieza exitosamente, o un str que contiene una descripcion del motivo del rechazo
    """

if __name__ == '__main__':
    main()
