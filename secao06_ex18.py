num1 = int(input('digite um quantos numeros devem ser lidos: ')) 
lista = []
for i in range(1, num1+1):
    num2 = int(input('digite um numero: ')) 
    lista.append(num2)
print(f'o maior numero é {max(lista)} e foi repetido {lista.count(max(lista))} vezes')

