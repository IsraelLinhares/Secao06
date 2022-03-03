rang= int(input('digite o numero: '))
lista=[]
soma = 0

for i in range(1,rang+1):
    soma = soma+i
    lista = list(range(soma - (i-1),soma+1))
    print(lista)