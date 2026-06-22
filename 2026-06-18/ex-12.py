# 12 - Função que gera permutações de uma lista.
def permutacoes(lista):
    from itertools import permutations
    return list(permutations(lista))

print("\n12. Permutações:")
print(" [1,2,3]:", permutacoes([1,2,3])[:5]) # Mostrando apenas as 5 primeiras