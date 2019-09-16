# Haremos un programa que le pide al usuario la velocidad incial, la velocidad final y el tiempo
# para calcular la aceleracion en dicho lapso

velocidad_inicial = "10"  # esto es un ejemplo mas visual para que vean la conversion de string a float
velocidad_inicial = float(velocidad_inicial)

velocidad_inicial = float(input("Digite la velocidad inicial (m/s): "))
velocidad_final = input("Digite la velocidad final(m/s): ")  # lee velocidad final como string
velocidad_final = float(velocidad_final)  # convierte velocidad final a float
print("Digite el tiempo (s): ")
tiempo = float(input())

aceleracion = (velocidad_final - velocidad_inicial) / tiempo

print(f"La aceleracion es {aceleracion} m/s^2")

