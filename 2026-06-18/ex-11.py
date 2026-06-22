# 11 - Função que simula automato finito.
def automato_finito(estados, alfabeto, transicoes, estado_inicial, estados_finais, cadeia):
    estado_atual = estado_inicial
    for simbolo in cadeia:
        if (estado_atual, simbolo) not in transicoes:
            return False
        estado_atual = transicoes[(estado_atual, simbolo)]
    return estado_atual in estados_finais

print("\n11. Autômato finito:")
# Autômato que aceita strings com número par de 'a's
estados = {'q0', 'q1'}
alfabeto = {'a', 'b'}
transicoes = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q1'
}
print(" 'aab' (par de a's?):", automato_finito(estados, alfabeto, transicoes, 'q0', {'q0'}, "aab"))
print(" 'aba' (par de a's?):", automato_finito(estados, alfabeto, transicoes, 'q0', {'q0'}, "aba"))