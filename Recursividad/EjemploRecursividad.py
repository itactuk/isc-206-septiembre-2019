
def factorial_recursivo(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)
