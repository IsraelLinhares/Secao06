num1 = int(input('digite um numero: ')) 
lista=[]
i= 12
while i > 10:
    for i in range(1,num1+1):
        if i%2 != 0:
            lista.append(i)
    lista.sort() 
    print(*lista) 
    i = 9
else:
    print('numero invalido')