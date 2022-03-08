
print('a soma dos primeiros 100 numeros naturais ')
result1=0
num = 0 

for i in range(101):
    result1+=i**2
    num += i 
print(f'a soma dos quadrados dos 100 primeiros numeros naturais é: {num**2 - result1}')