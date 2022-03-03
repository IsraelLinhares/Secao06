i = 1
lista =[]
print('um um numero menor ou igual a 0 para parar o loop')
while i == 1:
     num = int(input('digite um numero: '))
     if num <= 0:
          i = 2
     else:
          lista.append(num)

print(f'o maior numero foi: {max(lista)} e o menor foi: {min(lista)}')