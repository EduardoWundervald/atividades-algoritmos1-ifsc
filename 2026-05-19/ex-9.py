hora_inicio = int(input("Informe a hora de início do jogo: "))
fora_final = int(input("Informe a hora final do jogo: "))

if(hora_inicio<fora_final):
    duracao = fora_final - hora_inicio
else:
    duracao = (24 - hora_inicio) + fora_final

print(f"O jogo durou {duracao} horas")