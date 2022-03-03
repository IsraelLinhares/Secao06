num= int(input('digite o numero: '))

val = 0
if num > 1:
    for i in range(1,num+1):
        if (num%1 == 0) and (num%i == 0):

            val += 1    

    if val <=2:

        print('numero primo')

    else:
        print('numero não primo')
        
else:
    print('número invalido')

