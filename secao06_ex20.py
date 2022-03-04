print('digite 1000 para parar o loop')

num = 0
listap = []
lista = []
while  num != 1000:
    num = int(input('digite um numero: '))
    lista.append(num)    
    
    if (num%2)==0 and num != 0:
        print("é par")
        listap.append(num)    
    else:
        print('não é par') 
        
print(f'foi digitado {len(lista)} numeros e o numero de pares digitado foi: {len(listap)}')