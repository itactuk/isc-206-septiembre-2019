# in
# not in

# in se utiliza para ver si un elemento se encuentra en una lista
nombre = "Stanley"
listado_estudiantes = ["Stanley", "Daniel", "Maxy", "Lia", "Alexandra"]
print(nombre in listado_estudiantes) # la pregunta es: el nombre se encuentra en el listado
print(nombre not in listado_estudiantes) # False
print("Jenny" in listado_estudiantes)
print("Jose" in [1,4,4654,6, "Miguel"])

# is
# is not

# is se utilizar para ver si dos objetos son iguales. Usualmente se usa con None
estudiante = None
print(estudiante is None)
print(estudiante is not None)
estudiante = "Maxy"
print(estudiante is None)
print(estudiante is not None)
