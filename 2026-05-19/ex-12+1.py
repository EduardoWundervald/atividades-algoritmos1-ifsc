inicio = int(input("Informe o início do intervalo: "))
final = int(input("Informe o final do intervalo: "))

for i in range(inicio, final+1):
    if(i>1):
        primo = True
        for divisor in range(2, i):
            if(i%divisor==0):
                primo = False
                break
        if(primo == True):
            print(i)