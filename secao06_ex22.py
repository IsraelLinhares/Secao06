"""
numero ou caractere
"""

i = 0
lista = []
while i == 0:
    num = input('numero: ')
    if num.isnumeric() and num.isnumeric() > 0:
        num = int(num)
        if num >= 10 and num <= 20:    
            lista.append(num)
        elif  num <= 0 and lista == []:
            print('numero invalido')
        else:
            print(f'a média é: {sum(lista)/len(lista)}')
            i = 1
    else:
        print('invalido')