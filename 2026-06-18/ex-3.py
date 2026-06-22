# 3 - Função que valida CPF.
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = 11 - (soma % 11)
    d1 = 0 if d1 > 9 else d1
    
    # Cálculo do segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = 11 - (soma % 11)
    d2 = 0 if d2 > 9 else d2
    
    return int(cpf[9]) == d1 and int(cpf[10]) == d2

print("\n3. Validar CPF:")
print(" 529.982.247-25:", validar_cpf("529.982.247-25"))
print(" 111.111.111-11:", validar_cpf("111.111.111-11"))