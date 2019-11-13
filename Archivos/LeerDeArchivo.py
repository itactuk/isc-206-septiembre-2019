
# Estoy leyendo el archivo y sumando todos los numeros a partir de la linea 2

with open("mi_archivo.txt", "r") as f:
    contenido_archivo = f.read()  # Lee todo el contenido
    print(contenido_archivo)  # Imprime todo el contenido
    # Empezare a procesar la informacion
    lineas = contenido_archivo.split('\n')
    lineas = lineas[2:]
    acc = 0
    for num in lineas:
        if num == '':
            continue
        num = int(num)
        acc += num
    print(f"La suma es {acc}")


# Otra forma que usa la RAM mas eficientemente
with open("mi_archivo.txt", "r") as f:
    f.readline()  # Salto la 1era linea
    f.readline()  # Salto la 2da linea
    acc = 0
    for num in f:  # asigna cada una de las lineas restantes a num, una por una
        if num == '':
            continue
        num = int(num)
        acc += num
    print(f"La suma es {acc}")
