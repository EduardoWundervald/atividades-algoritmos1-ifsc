evento = int(input("Quantos segundos durou o evento? "))
horas = evento // 3600
minutos = (evento % 3600) // 60
segundos = (evento % 3600) % 60
print(f"O evento durou: {horas} horas, {minutos} minutos e {segundos} segundos.")