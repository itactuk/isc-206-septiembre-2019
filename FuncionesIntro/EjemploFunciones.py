# funcion que halle el maximo de una lista de numeros

def hallar_el_maximo(lista_de_numeros):
    el_mas_alto = -999999999999999999999999999999999999999999999
    for numero_actual in lista_de_numeros:
        if numero_actual > el_mas_alto:
            el_mas_alto = numero_actual
    return el_mas_alto

def calc_fuerza(ac, masa):
    fuerza = ac * masa
    return fuerza

dict_car_int={
    "1": 1,
    "2": 2,
    "3": 3,
}
def int(string):
    acc = 0
    for s in string:
        d = dict_car_int[s]
        acc *= 10
        acc += d
    return acc

lista_n = []
n = int(input("Cantidad de numeros a digitar: "))
for i in range(n):
    numero = int(input("Digite un numero: "))
    lista_n.append(numero)  # La funcion append agrega un elemento a una lista

numero_mayor = hallar_el_maximo(lista_n)
print(f"El mayor es {numero_mayor}")
print(f"El mayor es {hallar_el_maximo(lista_n)}")

print(hallar_el_maximo([1,2,4,4,5,7,8,2,46,2436,6]))

print(calc_fuerza(2, 5))

lista_fuerzas = []
for aceleracion in range(6, 20):
    f = calc_fuerza(aceleracion, 5)
    lista_fuerzas.append(f)
print(f"La fuerza mayor es {hallar_el_maximo(lista_fuerzas)}")
