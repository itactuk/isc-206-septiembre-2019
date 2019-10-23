
# ENTRADA: 3, 4, 5, 6
# SALIDA: 7, 8, 9
from typing import List


def suma_primer_valor_al_resto(valor_a_sumar: float, *valores) -> List:
    lista_res = []
    for v in valores:
        lista_res.append(v + valor_a_sumar)  # Append agrega un elemento a la lista
    return lista_res

# El parametro de tamano variable debe de estar al final de los parametros convencionales. Si hay otros parametros
def mayor(*valores): # Cuando se pone el asterisco, la variable es una tupla
    m = valores[0]
    for v in valores:
        if m < v:
            m = v
    return m

# Ejemplos de llamar la funcion
print(mayor(2,3,6,7))
print(mayor(2,3))


res = suma_primer_valor_al_resto(4,55,7,8)
print(res)
