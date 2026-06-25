# 14 - Cálculo de Fatorial. Implemente o exercício de fatorial dos 
# slides com tratamento para números negativos.
import math

def fatorial(n):
    try:
        if n < 0:
            raise ValueError("Número negativo!")
        return math.factorial(n)
    except ValueError as e:
        return e

# Teste:
print(fatorial(5))  # 120
print(fatorial(-1)) # Erro