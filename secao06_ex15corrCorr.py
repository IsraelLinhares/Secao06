
lista = []
i = 1
while i == 1:
    num = input('digite um numero: ')
    if num.isnumeric():
        num = int(num)
        if num%2==0 or num == 0:
            print('numero invalido')
            continue
        for j in range(1,num+1):
            if j%2 == 1:
                lista.append(j)
        print(lista)
        i = 2