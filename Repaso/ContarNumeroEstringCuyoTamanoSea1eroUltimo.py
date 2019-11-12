from typing import List

# Hacer un problema que cuente cuantos elementos en una lista tienen un tamano menor que 20
# y su segundo caracter es igual igual al primero

def contar(lista: List[str]) -> int:
    contador = 0
    for elemento in lista:
        if len(elemento) < 20 and elemento[0]==elemento[1]:
            contador += 1  # contador = contador + 1
    return contador
