# print('digite 0 para sair do loop')
# i = 1
# lista = []
# listaP = []
# while i == 1:
#     try:
#         num = int(input('digite um numero: '))
#         if num == 0:
#             
#             print(f'soma dos numeros digitados: {sum(lista)}')
#             print(f'numeros digitados: {len(lista)}')
#             print(f'média dos numeros digitados: {sum(lista)/len(lista)}')
#             print(f'o maior dos numeros digitados: {max(lista)}')
#             print(f'o menor dos numeros digitados: {min(lista)}')
#             print(f'os pares dos numeros digitados: {listaP}')
#             print(f'a média dos pares dos numeros digitados: {sum(listaP)/len(listaP)}')
#             i = 2
#         lista.append(num)
#         if num%2 == 0:
#             listaP.append(num)
#     except ValueError:
#         print('caractere invalido')


# sem  lista


somaAll = 0
somaP = 0
cont = 0
max = 0
pares = ''
i = 1
a = 1
countP = 0
while a == 1:

    try:
        num = int(input('digite o primeiro numero: '))
        a = 2
        if num%2 == 0:
            pares += str(num) + ', '
            countP += 1
        if num > max:
            max = num
        somaAll += num
        cont += 1
    except:
        print('caractere invalido')
while i == 1:
    print('a partir de agora digite 0 para sair do loop')

    try:
        num_anterior = num
        num = int(input('digite um numero: '))
        if num == 0:
            print(f'soma dos numeros digitados: {somaAll}')
            print(f'numeros digitados: {cont}')
            print(f'média dos numeros digitados: {somaAll/cont}')
            print(f'o maior dos numeros digitados: {max}')
            print(f'o menor dos numeros digitados: {min}')
            print(f'os pares entre os numeros digitados: {pares}')
            print(f'a média dos pares dos numeros digitados: {somaP/countP}')
            
            i = 2


        if num < num_anterior:
            min = num
        if num%2 == 0:
            pares += str(num) + ', '
            countP += 1
            somaP += num
        if num > max:
            max = num
        somaAll += num
        cont += 1
    except ValueError:
        print('caractere invalido')

