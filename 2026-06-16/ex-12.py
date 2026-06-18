# 12 - Função que converte decimal para binário.
def decimal_para_binario(n):
    return bin(n)[2:]

print("\n12. 10 em binário:", decimal_para_binario(10))
print(" 42 em binário:", decimal_para_binario(42))