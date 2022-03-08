

a= int(input('digite quantas o número de pessoas na cidade: '))
price = int(input('digite o preço do kwh: '))

print('''tipos de consumidores:

        1- Resindencial
        2- Comercial
        3- industrial

''')
i = 0
res = []
com = []
ind = []
cidade = [sum(res), sum(com), sum(ind)]
max_cidade = max(cidade)
while i < a:
    cidade = [sum(res), sum(com), sum(ind)]
    max_cidade = max(cidade)
    i += 1
    num = int(input('digite o codigo do consumidor: '))
    gasto = int(input('digite o gasto de khw: '))
    if num == 1:
        res.append(gasto)
        
    elif num ==2:
        com.append(gasto)

    elif num ==3:
        ind.append(gasto)
    else: 
        print('numero invalido')
        continue

print(f'o habitantes que mais gastaram foram do codigo {print(cidade.index(max_cidade))}')

