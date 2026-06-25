# 1 - Divisão com Tratamento de Erros. Crie uma função que recebe 
# dois números e retorna o resultado da divisão. Trate: a) Divisão por 
# zero b) Entradas não numéricas.
def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero!"
    except TypeError:
        return "Erro: Entrada não numérica!"

# Teste:
print(divisao(10, 2))  # 5.0
print(divisao(10, 0))  # Erro
print(divisao("a", 2)) # Erro