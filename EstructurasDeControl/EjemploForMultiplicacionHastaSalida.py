# Hacer un programa que pueda multiplicar los numeros digitados por el usuario hasta que el usuario digite salida
entrada = ""
resultado = 1

while entrada != "salida":
    entrada = input("Digite un numero para multiplicar o escriba salida para salir del programa: ")
    entrada = entrada.strip()  # esto quita los espacios a la derecha e izquierda
    entrada = entrada.lower()  # esto convierte a entrada en minuscula
    if entrada != "salida":
        resultado *= float(entrada)
print(f"El resultado de multiplicar todos los numeros es {resultado}")


# otra forma de implementarlo
while True:
    entrada = input("Digite un numero para multiplicar o escriba salida para salir del programa: ")
    entrada = entrada.strip()  # esto quita los espacios a la derecha e izquierda
    entrada = entrada.lower()  # esto convierte a entrada en minuscula
    if entrada == "salida":
        break
    resultado *= float(entrada)
print(f"El resultado de multiplicar todos los numeros es {resultado}")

