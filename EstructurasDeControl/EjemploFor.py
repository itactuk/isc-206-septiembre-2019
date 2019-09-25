# for VARIABLE_ITERACION in RANGO_STRING_O_LISTA:
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR

# El for puede iterar sobre rangos, listas, strings, o diccionarios

# Sintaxis para RANGO:
# for VARIABLE_ITERACION in range(INICIO, FIN, INCREMENTO):
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
# Nota: El INICIO es el unico valor requerido.
# El INICIO se incluye. El FIN no se incluye.
# El INCREMENTO es el valor en que se incrementará la variable de iteración

# Sintaxis para LISTA/STRING:
# for VARIABLE_ITERACION in LISTA_STRING:
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
# Para la lista se le asignarán c/u de los valores de los elementos de la lista a la VARIABLE_ITERACION
# Para el string se le asignarán c/u de las letras del string a la VARIABLE_ITERACION

# Sintaxis para DICCIONARIO:
# for LLAVE, VALOR in DICCIONARIO.items():
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR


# Un programa que sume n cantidad de numeros. El usuario debe de digitar n

n = int(input("Digite cantidad de numeros a sumar: "))

acc = 0
# for i in range(0, n):
# for i in range(0, n, 1):
for i in range(n):  # se asume que INICIO es 0 y que INCREMENTO es 1 si no se especifican
    x = float(input("Digite x: "))
    acc += x  # es equivalente a acc = acc + x

print(f"La suma de los numeros digitados es {acc}")
