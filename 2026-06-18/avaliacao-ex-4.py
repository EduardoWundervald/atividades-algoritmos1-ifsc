mins = int(input("Informe a quantidade em minutos: "))

horas = mins // 60
minutos = mins % 60

print(f"{mins} minutos equivalem a {horas:02d} horas e {minutos:02d} minutos, ou {horas:02d}:{minutos:02d}.")

"""
Você pode instruir a f-string a formatar um
número inteiro (d) para que ele ocupe um espaço
de 2 dígitos (2), preenchendo com zeros (0)
à esquerda se necessário. A sintaxe para isso é :02d.

{horas:02d}: Pega o valor da variável horas e o formata para ter dois
dígitos (ex: 2 vira 02, 10 continua 10).
{minutos:02d}: Faz o mesmo para a variável minutos.
"""