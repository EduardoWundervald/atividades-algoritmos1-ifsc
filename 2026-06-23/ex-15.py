# 15 - Sistema de Tentativas. Crie função que executa uma operação 
# perigosa com 3 tentativas antes de falhar.
def operacao_perigosa():
    for tentativa in range(1, 4):
        try:
            num = float(input(f"Tentativa {tentativa}/3: "))
            return 10 / num
        except (ValueError, ZeroDivisionError):
            print("Entrada inválida!")
    raise Exception("Falha após 3 tentativas")

# Teste:
try:
    print("Resultado:", operacao_perigosa())
except Exception as e:
    print(e)