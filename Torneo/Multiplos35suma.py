

def suma_multiplos_3_5(limite=1000):
    suma = 0
    for i in range(limite):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma

print(suma_multiplos_3_5(1000))
