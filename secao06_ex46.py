from ast import Num
import random
  
r1 = random.randint(1, 10)
tentativas = []
while r1 < 1001:
     num = int(input('digite o numero: '))
     if num > r1:
          print('muito grande')
          tentativas.append(num)
          continue
     
     elif num < r1:
          print('muito pequeno')
          tentativas.append(num)
          continue
     elif num == r1:
          tentativas.append(num)
          print(f'acertou!!\nforam usadas {len(tentativas)} tentativas')
          
          i = 1222
