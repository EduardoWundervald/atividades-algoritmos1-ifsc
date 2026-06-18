# 1 - Função que calcula fatorial (iterativo).
def fatorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print("\n1. Fatorial de 5:", fatorial(5))
print(" Fatorial de 0:", fatorial(0))
print(" Fatorial de -3:", fatorial(-3))