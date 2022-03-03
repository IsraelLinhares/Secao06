lista=[]
i= 12
while i > 10:
    num1 = int(input('digite um numero: ')) 

    if num1%2==0:
        for i in range(num1+1):
            if i%2 == 0:
                lista.append(i)
        lista.sort(reverse=True) 
        print(*lista) 
        i = 9
    else:
        print('numero invalido')