# Programa que solo imprime numeros pares de una lista


lista = [1, 2, 3, 4, 8, 19, 20]
for elemento in lista:
    if elemento % 2 == 0:
        print(elemento)

## haciendo lo mismo con el continue
for elemento in lista:
    if elemento % 2 != 0:
        continue
    print(elemento)
