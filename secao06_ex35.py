num1 = int(input('digite o valor inicial:  '))
num2 = int(input('digite o valor final: '))

result=0
for i in range(num1,num2+1):
    if i%2 !=0:
        result+=i
print(f'a soma dos impares entre esses numeros é: {result}')