cal_a_puntos = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0
}

total_puntos = 0
total_creditos = 0
while True:
    calificacion = input("Digite calificación: ")
    calificacion = calificacion.upper().strip()
    if calificacion in cal_a_puntos:
        puntos = cal_a_puntos[calificacion]
    else:
        print("Error. Calificacion no valida. Vuelva a digitar")
        continue

    creditos = int(input("Digite creditos: "))

    total_puntos += creditos * puntos
    total_creditos += creditos

    continuar = input("Desea continuar? [Si]/[No]")
    if continuar.upper().strip() ==  "NO":
        break

indice = total_puntos/total_creditos
print(f"Total puntos: {total_puntos}")
print(f"Total creditos: {total_creditos}")
print(f"Indice actual: {indice}")

condicion_ac_ac = input("Condicion Academica Actual: ")
condicion_ac_ac = condicion_ac_ac.upper().strip()
if indice > 2:
    print("Condicion Normal")
elif condicion_ac_ac == "PRIMERA PRUEBA":
    print("Segunda Prueba")
elif condicion_ac_ac == "SEGUNDA PRUEBA":
    print("Retirado de la carrera")
else:
    print("Se digito una condicion academica incorrecta")

