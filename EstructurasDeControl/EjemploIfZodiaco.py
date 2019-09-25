
mes = 4
dia = 3

fecha_valida = True

if mes in [1,3,5,7,8,10,12]:
    if dia > 31:
        print("Dia invalido")
        fecha_valida = False
elif mes == 2:
    if dia > 29:
        print("Dia invalido")
        fecha_valida = False
elif mes in [2,4,6,9,11]:
    if dia > 30:
        print("Dia invalido")
        fecha_valida = False
else:
    print("Mes invalido")
    fecha_valida = False

if fecha_valida:
    if mes == 4:  # mes es abril
        if dia <= 19:  # seria aries
            print("Es aries")
        else:
            print("Es tauro")
    elif mes == 5: # mes es mayo
        if dia <= 20:
            print("Es Tauro")

if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("Es Tauro")
