import numpy as np


num = int(input('digite um numero de inicio: '))
num2 = int(input('digite um numero de termino: '))
lista = [num]
listap = [num, num2]
for i in range(num+1 , num2-1):
    if i%2 == 0:
        listap.append(i)
    else:
        lista.append(i)
print(f'a soma dos intervalos pares é {sum(listap)} e a multiplicação é dos intervalos ìmpares é : {np.multiply(lista,lista)}' )