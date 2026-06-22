# 13 - Função que calcula raiz quadrada (método Newton).
def raiz_quadrada_newton(n, precisao=1e-10):
    x = n
    while True:
        raiz = 0.5 * (x + n / x)
        if abs(raiz - x) < precisao:
            return raiz
        x = raiz

print("\n13. Raiz quadrada (Newton):")
print(" √25:", raiz_quadrada_newton(25))
print(" √2:", raiz_quadrada_newton(2))