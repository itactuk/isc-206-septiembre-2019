
num1 = int(input("Ingrese el primer número "))
num2 = int(input("Ingrese el segundo número "))

while num2 != 0:
    resto = num2
    num2 = num1 % num2
    num1 = resto

print("El MCD es : ", num1)
