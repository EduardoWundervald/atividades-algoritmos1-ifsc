# 6 - Múltiplos Tipos de Erro. Crie uma função que calcula raiz quadrada. 
# Trate: a) Números negativos b) Tipos não numéricos.
import math

def calcular_raiz(numero):
    try:
        if numero < 0:
            raise ValueError("Número negativo!")
        return math.sqrt(numero)
    except TypeError:
        return "Erro: Tipo inválido!"

# Teste:
print(calcular_raiz(4))   # 2.0
print(calcular_raiz(-4))  # Erro
print(calcular_raiz("abc")) # Erro