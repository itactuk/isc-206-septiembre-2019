# Escribe un programa que cuente la cantidad de espacios que tiene el texto digitado por el usuario

# Hola como estas. Yo bien

texto = input("Escriba el texto para contar espacios: ")
acc = 0

for caracter in texto:
    if caracter == ' ':
        acc += 1

print(f"Cantidad de espacios: {acc}")
