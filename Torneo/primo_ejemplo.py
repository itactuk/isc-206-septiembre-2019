
def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def halla_factor_primo_mas_grande(numero):
    maximo = 1
    for i in range(1, numero+1):
        if numero % i == 0 and es_primo(i):
            maximo = i
    return maximo

def main():
    print(halla_factor_primo_mas_grande(6))

if __name__ == '__main__':
    main()
