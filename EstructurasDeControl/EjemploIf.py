# Sintaxis de if
# if CONDICION:
#   INSTRUCCIONES
#

# Sintaxis de if ... else
# if CONDICION:
#   INSTRUCCIONES_IF  # Solo se van a ejecutar si CONDICION es TRUE
# else:
#   INSTRUCCIONES_ELSE # Solo se van a ejecutar si CONDICION es FALSE

# Sintaxis de if ... elif ... else
# if CONDICION:
#   INSTRUCCIONES_IF  # Solo se van a ejecutar si CONDICION es TRUE
# elif CONDICION_2:   # Pueden haber multiples elif
#   INSTRUCCIONES_ELIF  # Solo se ejecuta si CONDICION es FALSE y CONDICION_2 es TRUE
# else:
#   INSTRUCCIONES_ELSE # Solo se van a ejecutar si CONDICION es FALSE y CONDICION_2 es FALSE

# Hacer un programa que determine si un numero digitado por el usuario es par o no
n = int(input("Diga numero entero: "))

if n % 2 == 1:
    print("Es impar")
    print("Bien hecho")
else:
    print("Es par")
    print("Pudo ser mejor")

print("Se termino el programa")


# Hacer un programa que determine en que generacion estas
# <1990 son viejos
# entre 1990 a 2000 menos viejos
# de 2001-2010 gente bonita
# mayor 2010 bebes

ano = float(input("Introduzca el año de nacimiento: "))
if ano < 1990:
    print("Viejo")
elif ano >= 1990 and ano <= 2000:
    print("Menos viejo")
elif ano >=2001 and ano <= 2010:
    print("Gente bonita")
else:
    print("Eres un bebé")

# otra manera de lograr lo mismo de abajo
# esta manera es menos estética y menos organizada
ano = float(input("Introduzca el año de nacimiento: "))
if ano < 1990:
    print("Viejo")
else:
    if ano >= 1990 and ano <= 2000:
        print("Menos viejo")
    else:
        if ano >=2001 and ano <= 2010:
            print("Gente bonita")
        else:
            print("Eres un bebé")

# otra manera de lograr lo mismo de abajo
# esta manera es menos eficiente, ya que todas las condiciones se tienen que probar siempre
ano = float(input("Introduzca el año de nacimiento: "))
if ano < 1990:
    print("Viejo")
if ano >= 1990 and ano <= 2000:
    print("Menos viejo")
if ano >=2001 and ano <= 2010:
    print("Gente bonita")
if ano > 2010:
    print("Eres un bebé")































