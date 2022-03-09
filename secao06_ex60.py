print('digite 0 para sair do loop')
i = 1
lista = []
listaP = []
while i == 1:
    try:
        num = int(input('digite um numero: '))
        lista.append(num)
        if num%2 == 0:
            listaP.append(num)
        if num == 0:
            lista.pop()
            listaP.pop()
            print(f'soma dos numeros digitados: {sum(lista)}')
            print(f'numeros digitados: {len(lista)}')
            print(f'média dos numeros digitados: {sum(lista)/len(lista)}')
            print(f'o maior dos numeros digitados: {max(lista)}')
            print(f'o menor dos numeros digitados: {min(lista)}')
            print(f'os pares dos numeros digitados: {listaP}')
            print(f'a média dos pares dos numeros digitados: {sum(listaP)/len(listaP)}')
            i = 2
    except ValueError:
        print('caractere invalido')
   