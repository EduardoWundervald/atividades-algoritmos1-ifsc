# 1 - Função que resolve Torre de Hanói (imprime passos).
def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova disco {n} de {origem} para {destino}")
    hanoi(n - 1, auxiliar, destino, origem)

print("\n1. Torre de Hanói (3 discos):")
hanoi(3, 'A', 'C', 'B')