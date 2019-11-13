

# Crearnos un programa que cree un archivo

# Si usamos with no tenemos que cerrar el archivo
# esta es la manera recomendable
with open("mi_archivo.txt", "w") as f:
    f.write("Hola\nQue hacehjklhkljhkjl?")
    for i in range(1000):
        f.write(f"{i}\t\n")


with open("mi_archivo.csv", "w") as f:
    f.write(f"Nombre, Apellido\n")
    for i in range(1000):
        f.write(f"{i}, {i+1}\n")
