# 8 - Função que remove duplicatas de uma lista.
def remover_duplicatas(lista):
    return list(set(lista))

print("\n8. Remover duplicatas [1,2,2,3,3,3]:", remover_duplicatas([1,2,2,3,3,3]))