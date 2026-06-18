# 10 - Função que calcula juros compostos.
def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

print("\n10. Juros de 1000 a 10% por 2 anos:", juros_compostos(1000, 0.10, 2))