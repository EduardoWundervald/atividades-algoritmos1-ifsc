# 6 - Função que calcula caminho crítico (simulação).
def caminho_critico(tarefas):
    tempo_cedo = {tarefa: 0 for tarefa in tarefas}
    for tarefa, (duracao, deps) in tarefas.items():
        if deps:
            tempo_cedo[tarefa] = max(tempo_cedo[dep] for dep in deps) + duracao
        else:
            tempo_cedo[tarefa] = duracao
    return max(tempo_cedo.values(), default=0)

print("\n6. Caminho crítico:")
tarefas = {
    'A': (5, []),
    'B': (3, ['A']),
    'C': (2, ['A']),
    'D': (4, ['B', 'C'])
}
print(" Duração total:", caminho_critico(tarefas))