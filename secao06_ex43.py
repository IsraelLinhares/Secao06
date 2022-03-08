from cmath import sqrt


i = 1
while i == 1:
     num = int(input('digite um numero: '))
     if num < 0:
          i = 2
     print(f'raiz quadrada: {sqrt(num)}')
     print(f'o quadrado: {num**2}')
     print(f'o cubo: {num**3}')
     