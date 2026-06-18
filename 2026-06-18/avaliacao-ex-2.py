import time
n = [0,1,2,3,4,5,6,7,8,9,10]
for i in reversed(n):
    print(i)
    time.sleep(1)

print("Foguete lançado!")

import time

# Mesma solução, mas a contagem é gerada dinamicamente pelo range
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)

print("Foguete lançado!")
