codigo = input("Informe o código do cargo: ")
salario = float(input("Informe o salário: "))
diferenca = 0
if(codigo=="101"):
    diferenca = salario * 0.1
    salario_novo = salario + diferenca
elif(codigo=="102"):
    diferenca = salario * 0.2
    salario_novo = salario + diferenca
elif(codigo=="103"):
    diferenca = salario * 0.3
    salario_novo = salario + diferenca
else:
    diferenca = salario * 0.4
    salario_novo = salario + diferenca

print(f"Salário novo: {salario_novo}")
print(f"Diferença: {diferenca}")
print(f"Salário antigo: {salario}")