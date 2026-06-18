# 5 - Função que gera lista de números pares até n.
def pares_ate(n):
    return [x for x in range(0, n+1, 2)]

print("\n5. Pares até 10:", pares_ate(10))