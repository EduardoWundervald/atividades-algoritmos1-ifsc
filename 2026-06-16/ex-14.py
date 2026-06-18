# 14 - Função que valida formato de e-mail.
def validar_email(email):
    import re
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(padrao, email))

print("\n14. 'exemplo@email.com' valido?", validar_email("exemplo@email.com"))
print(" 'email_invalido.com' válido?", validar_email("email_invalido.com"))