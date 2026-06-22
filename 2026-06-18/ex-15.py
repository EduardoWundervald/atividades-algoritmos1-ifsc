# 15 - Função que implementa ordenação topológica (grafos).
def ordenacao_topologica(grafo):
    grau_entrada = {no: 0 for no in grafo}
    for no, vizinhos in grafo.items():
        for vizinho in vizinhos:
            grau_entrada[vizinho] = grau_entrada.get(vizinho, 0) + 1
            
    fila = [no for no, grau in grau_entrada.items() if grau == 0]
    ordenada = []
    
    while fila:
        no = fila.pop(0)
        ordenada.append(no)
        for vizinho in grafo.get(no, []):
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)
                
    return ordenada if len(ordenada) == len(grau_entrada) else None

print("\n15. Ordenação topológica:")
grafo = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
print(" Ordem topológica:", ordenacao_topologica(grafo))