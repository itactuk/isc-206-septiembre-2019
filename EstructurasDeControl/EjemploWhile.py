# Un programa que sume n cantidad de numeros. El usuario debe de digitar n

n = int(input("Digite cantidad de numeros a sumar: "))

i = 0
acc = 0

# while CONDICION:
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR
#   INSTRUCCIONES_A_REPETIR

while i < n:
    i += 1  # i = i + 1
    x = float(input("Digite x: "))
    acc += x  # es equivalente a acc = acc + x

print(f"La suma de los numeros digitados es {acc}")
