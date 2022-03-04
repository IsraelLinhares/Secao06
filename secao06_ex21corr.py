from math import prod

num = int(input('digite um numero de inicio: '))
num2 = int(input('digite um numero de termino: '))
listai = []
listap = []
for i in range(num , num2+1):
    if i%2 == 0:
        listap.append(i)
        print(listap)
    else:
        listai.append(i)
        print(listai)

print(f'a soma dos numeros pares do intervalo: {sum(listap)}')
print(f'a a multiplicação dos impares do intervalo: {prod(listai)}')
