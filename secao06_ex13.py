i= 12
while i > 10:
    num1 = int(input('digite um numero: ')) 

    for i in range(num1+1):
        if i%2 == 0:
            print(i)   
            i = 9
    else:
        print('numero invalido')        
