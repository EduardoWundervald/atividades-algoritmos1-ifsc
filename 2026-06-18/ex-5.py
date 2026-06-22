# 5 - Função que mescla listas ordenadas.
def mesclar_listas_ordenadas(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:] or lista2[j:])
    return resultado

print("\n5. Mesclar listas ordenadas:")
print(" [1,3,5] e [2,4,6]:", mesclar_listas_ordenadas([1,3,5], [2,4,6]))
print(" [10,20] e [15,25,30]:", mesclar_listas_ordenadas([10,20], [15,25,30]))