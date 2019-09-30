# Este es un ejemplo para iterar sobre un diccionario

diccionario_matricula_nombre={
    "20160716": "Alexandra",
    "20160261": "Roniell",
    "20151753": "Stanly"
}

for matricula, nombre in diccionario_matricula_nombre.items():
    print(f"Matricula: {matricula} - Nombre: {nombre}")
