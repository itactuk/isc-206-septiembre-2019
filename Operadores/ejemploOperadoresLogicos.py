# Nada mas sobre valores booleanos (True o False)

edad_rango_menor = 18
edad_rango_mayor = 30

edad_stanley = 22

# and
print(True and False)  # False
print(edad_stanley >= edad_rango_menor and edad_stanley <= edad_rango_mayor)  # True. El and se usa para rangos

# or
print(True or False)  # True
print(edad_stanley < edad_rango_menor or edad_stanley > edad_rango_mayor)  # True. El or se usa para rangos que no solapen

# not
print(not True) # False
tiene_hambre = False
print(not tiene_hambre)  # True

