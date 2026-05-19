ano = int(input("Informe quantos anos tem: "))
mes = int(input(f"{ano} e quantos meses? "))
dia = int(input(f"{ano} e {mes} e quantos dias? "))
total_dias = (ano*365)+(mes*30)+dia
print(f"Total de dias de vida: {total_dias}")
