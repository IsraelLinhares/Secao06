

a= int(input('digite quantas o número de pessoas na cidade: '))
price = int(input('digite o preço do kwh: '))

print('''tipos de consumidores:

        1- Resindencial
        2- Comercial
        3- industrial

''')
resin_gasto = []
comer_gasto = []
indus_gasto = []
lista = [sum(resin_gasto),sum(comer_gasto),sum(indus_gasto)]
max_lista = max(lista)
min_lista = min(lista)

for user in range(1,a+1):
    type= input(f'digite o codigo do consumidor {user}: ')
    if type == '1':
        qnt = int(input(f'digite a quantidade de kwh gasta pelo consumidor {user}: '))
        resin_gasto.append(qnt)
    elif type == '2':
        qnt = int(input(f'digite a quantidade de kwh gasta pelo consumidor {user}: '))
        comer_gasto.append(qnt)
    elif type == '3':
        qnt = int(input(f'digite a quantidade de kwh gasta pelo consumidor {user}: '))
        indus_gasto.append(qnt)
    else:
        print('codigo invalido')
        break
lista = [sum(resin_gasto),sum(comer_gasto),sum(indus_gasto)]

if lista.index(max_lista) == 0:
    print(f'os usuários resindenciais foram os que mais gastaram')
elif lista.index(max_lista) == 1:
    print(f'os usuários comerciais foram os que mais gastaram')
else:
    print(f'os usuários industriais foram os que mais gastaram')

if lista.index(min_lista) == 0:
    print(f'os usuários resindenciais foram os que menos gastaram')
elif lista.index(min_lista) == 1:
    print(f'os usuários comerciais foram os que menos gastaram')
else:
    print(f'os usuários industriais foram os que menos gastaram')


if sum(resin_gasto) > 0:
    print(f'os usuários resindenciais gastaram em média: {(sum(resin_gasto)/len(resin_gasto))*price} R$')
else:
    print(f'os usuários resindenciais gastaram em média: 0')
if sum(comer_gasto) > 0:
    print(f'os usuários comerciais gastaram em média: {(sum(comer_gasto)/len(comer_gasto))*price} R$')
else:
    print(f'os usuários comerciais gastaram em média: 0')
if sum(indus_gasto) > 0:
    print(f'os usuários industriais gastaram em média: {(sum(indus_gasto)/len(indus_gasto))*price} R$')
else:
    print(f'os usuários industriais gastaram em média: 0')
print(f'\nos usuários resindenciais gastaram: {sum(resin_gasto)*price} R$')
print(f'os usuários comerciais gastaram: {sum(comer_gasto)*price} R$')
print(f'os usuários industriais gastaram: {sum(indus_gasto)*price} R$')



