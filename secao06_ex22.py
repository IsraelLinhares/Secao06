lista = []
num = int(input('digite sua nota: '))
while num >= 10 and num <= 20:
    lista.append(num)
    num = int(input('digite sua nota: '))
print(f'sua média é:{sum(lista)/len(lista)}')
