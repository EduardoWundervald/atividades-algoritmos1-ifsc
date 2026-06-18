#13 - Função que verifica se um número é múltiplo de outro
def eh_multiplo(a, b):
    return a % b == 0

print(eh_multiplo(12, 4))
print(eh_multiplo(12, 5))