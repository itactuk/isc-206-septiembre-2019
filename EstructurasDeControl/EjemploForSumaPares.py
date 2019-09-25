# Programa que suma los numeros pares digitados que se encuentran en un rango digitado por el usuario

v_inicial = int(input("Digite rango inferior: "))
v_final = int(input("Digite rango superior (no inclusive): "))

acumulador = 0

if v_inicial % 2 == 1:
    v_inicial += 1

for i in range(v_inicial, v_final, 2):
    acumulador += i

print(f"La suma de los numeros pares entre {v_inicial} y {v_final} es {acumulador}")
