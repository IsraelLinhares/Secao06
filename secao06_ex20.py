print('digite 1000 para parar o loop')

num = 0
lista = []
while  num != 1000:
    num = int(input('digite um numero de inicio: '))
    if (num%2)==0 and num != 0:
        print("é par")
        lista.append(num)    
    else:
        print('não é par') 
        
print(f'o numero de pares digitado foi: {len(lista)}')