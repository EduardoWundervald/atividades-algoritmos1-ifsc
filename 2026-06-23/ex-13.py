# 13 - Validador de Senha. Crie função que levanta exceção se senha 
# não tiver: 8+ caracteres, Pelo menos 1 número, Pelo menos 1 maiúscula.
import re

def validar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha curta (mínimo 8 caracteres)")
    if not re.search(r'\d', senha):
        raise ValueError("Senha precisa de pelo menos 1 número")
    if not re.search(r'[A-Z]', senha):
        raise ValueError("Senha precisa de pelo menos 1 letra maiúscula")

# Teste:
try:
    validar_senha("Python3") # OK
    validar_senha("abc")     # Erro
except ValueError as e:
    print(e)