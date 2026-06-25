# 3 - Conversão de String para Inteiro. Peça ao usuário um valor e 
# tente convertê-lo para inteiro. Use try/except para tratar 
# entradas inválidas.
def converter_inteiro():
    try:
        return int(input("Digite um valor: "))
    except ValueError:
        return "Erro: Valor inválido!"

# Teste:
print(converter_inteiro())
