from typing import Tuple

def main():
    print(raices_eq_cuadratica(2, 3, 5))
    print("Hola")


def raices_eq_cuadratica(a: float,b: float,c: float) -> Tuple[float, float]:
    """
    Esta funcion resuelve una ecuacion de la forma ax^2+bx+c=0
    :param a: coeficiente de x^2
    :param b: coeficiente de x
    :param c: alone
    :return: tupla con ambas raices
    """
    x1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1, x2  # equivale a (x1, x2)

def raices_eq_primer_grado(a: float, b: float) -> float:
    """
    Esta funcion resulve una ecuacion de la forma ax + b =0
    :param a:
    :param b:
    :return: valor de x
    """
    return -b/a

if __name__ == '__main__':
    main()
