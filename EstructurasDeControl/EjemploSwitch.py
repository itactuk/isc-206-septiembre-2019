# Programa que lea del usuario el mes en formato numerico y le diga al usuario cual es el nombre del mes

# Ejemplo:
# El usuario digita 1
# El programa le debe decir: "Enero"

diccionario_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

mes_numerico = int(input("Digite el numero del mes: "))

# if mes_numerico <= 0 or mes_numerico >= 12:
#     print("Error ")
#
# if not (mes_numerico >= 1 and mes_numerico <= 12): # esto es equivalente a la condicion de arriba
#     print("Error")

if mes_numerico not in diccionario_meses: # not in solo chequea el valor de la izquierda de los 2 puntos
    print("Error. Mes no valido")
else:
    print("El mes es: " + diccionario_meses[mes_numerico])


