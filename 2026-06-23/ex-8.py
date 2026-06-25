# 8 - Validador de CPF. Crie uma função que valida CPF 
# (apenas estrutura: 11 dígitos). Use raise para invalidação.
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido: deve ter 11 dígitos")
    return True

# Teste:
try:
    validar_cpf("12345678901") # OK
    validar_cpf("123")         # Erro
except ValueError as e:
    print(e)