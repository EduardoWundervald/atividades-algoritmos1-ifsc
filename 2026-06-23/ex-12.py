# 12 - Exceção Personalizada Idade. Crie IdadeInvalidaError e 
# valide se idade está entre 0-120 anos.
class IdadeInvalidaError(Exception):
    pass

def validar_idade(idade):
    if not (0 <= idade <= 120):
        raise IdadeInvalidaError("Idade deve ser entre 0 e 120")

# Teste:
try:
    validar_idade(25)  # OK
    validar_idade(150) # Erro
except IdadeInvalidaError as e:
    print(e)