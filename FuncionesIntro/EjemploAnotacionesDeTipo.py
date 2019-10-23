from typing import Tuple


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

def print_nombre(nombre: str):
    print("Mi nombre es: ", nombre)


print_nombre("Maria")

a = 2
valor1, valor2 = raices_eq_cuadratica(a, 3, 5)
print("valor1: ", valor1)
print("valor2: ", valor2)
# otra manera de hacerlo
resultados = raices_eq_cuadratica(4,5,6)
print("resultados:", resultados)
