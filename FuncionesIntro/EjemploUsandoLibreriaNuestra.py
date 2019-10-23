import FuncionesIntro.libreria_ecuaciones as eq

while True:
    print("Menu: ")
    print("1. Ec cuadratica ")
    print("2. Ec 1er grado ")
    print("3. Salir del programa")
    opcion = input("Digite opcion: ").strip()
    if opcion == '1':
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        print("El resultado es: ", eq.raices_eq_cuadratica(a, b, c))
    elif opcion == '2':
        a = float(input("a: "))
        b = float(input("b: "))
        print("El resultado es: ", eq.raices_eq_primer_grado(a, b))
    elif opcion == '3':
        break
    else:
        print("Se digito opcion inválida")
