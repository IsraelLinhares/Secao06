num = int(input('digite um numero: '))
lista = []
for i in range(1, num):
    if (num%i) == 0:
        lista.append(i)

print(sum(lista))
