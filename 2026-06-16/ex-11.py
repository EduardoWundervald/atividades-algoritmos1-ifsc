# 11 - Função que retorna valores únicos de duas listas.
def unicos_entre_listas(lista1, lista2):
    return list(set(lista1) | set(lista2))

print("\n11. Únicos entre [1,2,3] e [3,4,5]:", unicos_entre_listas([1,2,3], [3,4,5]))