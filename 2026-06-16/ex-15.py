# 15 - Função que calcula diferença de dias entre datas (usando datetime).
def diferenca_dias(data1, data2):
    from datetime import datetime
    d1 = datetime.strptime(data1, "%d/%m/%Y")
    d2 = datetime.strptime(data2, "%d/%m/%Y")
    return abs((d2 - d1).days)

print("\n15. Dias entre 01/01/2023 e 01/02/2023:", diferenca_dias("01/01/2023", "01/02/2023"))