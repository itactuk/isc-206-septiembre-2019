# Escribe un programa que dibuje el patrón de abajo. La cantidad de líneas debe de ser proporcionada por el usuario y puede variar entre una corrida y otra.
#   *
#  **
# ***

linea = int(input("Digite cantidad lineas: "))

for linea_actual in range(linea):
    for j in range(linea - 1 - linea_actual):
        print(' ', end='') # el end del final es para evitar cambio de linea
    for k in range(linea_actual + 1):
        print('*', end='')
    print()
