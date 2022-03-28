#try para fazer validação:
valid = 1
i = 0
res = []
com = []
ind = []
while valid == 1:
    a= input('digite quantas o número de pessoas na cidade: ')
    price = input('digite o preço do kwh: ')
    if a.isnumeric() and price.isnumeric():
        print('''tipos de consumidores:

                1- Resindencial
                2- Comercial
                3- industrial

        ''')
        a = int(a)
        price = int(price)
        while i < a:

            i += 1
            num = input('digite o codigo do consumidor: ')
            if num ==  '1':
                try:
                    gasto = int(input('digite o gasto de khw: '))
                    res.append(gasto)
                except ValueError:
                    print('digite números')
                    i = i - 1
                
                
            elif num == '2':
                try:
                    gasto = int(input('digite o gasto de khw: '))
                    com.append(gasto)
                except ValueError:
                    print('digite números')
                    i = i - 1

            elif num == '3':
                try:
                    gasto = int(input('digite o gasto de khw: '))
                    ind.append(gasto)
                except ValueError:
                    print('digite números')
                    i = i - 1
            else: 
                print('numero invalido')
                i = i - 1
            cidade = [sum(res), sum(com), sum(ind)]
            max_cidade = max(cidade)
            min_cidade = min(cidade)

        print(f'o habitantes que mais gastaram foram do codigo: {cidade.index(max_cidade)+1}')
        print(f'o habitantes que menos gastaram foram do codigo: {cidade.index(min_cidade)+1}')
        print(f'o consumo médio dos habitantes: {(sum(cidade)*price)/a} R$')
        print(f'''
        o consumo dos consumidores 1 foi: {sum(res)} kwh
        o consumo dos consumidores 2 foi: {sum(com)} kwh
        o consumo dos consumidores 3 foi: {sum(ind)} kwh

        ''')
        valid = 2
    else:
        print('digite numeros!')
