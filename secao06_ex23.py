L = 0
while L == 0:
    num = input('numero: ')
    if num.isnumeric() and num.isnumeric() > 0:
        num = int(num)
        for i in range(1, num+1):
            if (num%i) == 0:
                print(i)
        L = 1
    else:
        print('digite numeros positivos')