# 10 - Função que resolve equação quadrática.
def resolver_equacao_quadratica(a, b, c):
    import math
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return (raiz1, raiz2)

print("\n10. Equação quadrática:")
print(" x^2 - 5x + 6:", resolver_equacao_quadratica(1, -5, 6))
print(" x^2 + 1:", resolver_equacao_quadratica(1, 0, 1))