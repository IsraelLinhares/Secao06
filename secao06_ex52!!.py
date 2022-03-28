num= int(input('digite o numero: '))
resto1 = num%100
resto2 = resto1%50
resto3 = resto2%20
resto4 = resto3%10
resto5 = resto4%5
resto6 = resto5%2
resto7 = resto6%1
print(f'{num//100} notas de 100R$')
print(f'{resto1//50} notas de 50R$')
print(f'{resto2//20} notas de 20R$')
print(f'{resto3//10} notas de 10R$')
print(f'{resto4//5} notas de 5R$')
print(f'{resto5//2} notas de 2R$')
print(f'{resto6//1} moedas de 1R$')
