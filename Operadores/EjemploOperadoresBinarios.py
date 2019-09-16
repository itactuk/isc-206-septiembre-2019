# & y binaria
print(bin(0b100 & 0b110)) # 0b100
# | o binaria (o inclusiva)
print(bin(0b100 | 0b110)) # 0b110
# ^ xor binario (o exclusiva)
print(bin(0b100 ^ 0b110)) # 0b010   # 0b10 es equivalente
# ~ complemento a uno ~(x+1)
print(bin(~0b100)) # -0b101
# << rodamiento de bits hachia la izquierda
print(bin(0b100 << 3)) # 0b100000  # rodar los bits 3 veces a la izquierda equivale a multiplicar por 2 tres veces
# >> rodamiento de bits hacia la derecha
print(bin(0b100 >> 2)) # 0b1  # rodar los bits 2 veces a la derecha equivale a dividir por 2 dos veces
