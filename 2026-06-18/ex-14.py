# 14 - Função que valida expressões matemáticas (parênteses balanceados).
def validar_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0

print("\n14. Parenteses balanceados:")
print(" '(a+b)*(c-d)':", validar_parenteses("(a+b)*(c-d)"))
print(" '((x+y)':", validar_parenteses("((x+y)"))