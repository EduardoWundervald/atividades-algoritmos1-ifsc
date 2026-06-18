# 6 - Função que calcula o MDC (algoritmo de Euclides).
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

print("\n6. MDC de 48 e 18:", mdc(48, 18))
print(" MDC de 21 e 14:", mdc(21, 14))