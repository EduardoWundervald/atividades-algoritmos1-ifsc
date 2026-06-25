# 11 - Relançamento de Exceção. Modifique o validador de CPF para 
# registrar o erro em log e relançar a exceção.
import logging

def validar_cpf_log(cpf):
    try:
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido")
    except ValueError as e:
        logging.error(f"Erro de CPF: {cpf} - {e}")
        raise

# Teste:
try:
    validar_cpf_log("123")
except ValueError as e:
    print(e)