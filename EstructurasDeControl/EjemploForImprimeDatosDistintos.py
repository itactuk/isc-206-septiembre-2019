# Ejemplo for que imprime información distinta

caracteres_posibles = "qwertyuiopasdfghjklzxcvbnm"

for c1 in caracteres_posibles:
    print(f"Se imprimiran todas las combinaciones que empiezan con {c1}")
    for c2 in caracteres_posibles:
        print(c1 + c2)

for i in range(0, 10):
    print("Maxy" + str(i))
