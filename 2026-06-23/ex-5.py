# 5 - Exceção Personalizada Saldo Insuficiente. Crie uma exceção 
# SaldoInsuficienteError e uma função para sacar de uma conta bancária.
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    return saldo - valor

# Teste:
try:
    print(sacar(100, 50))  # 50
    print(sacar(100, 200)) # Erro
except SaldoInsuficienteError as e:
    print(e)