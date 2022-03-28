
import random 

num = int(input('digite o numero de vezes para jogar o dado: '))

d1 = 0
d2 = 0

for i in range(1, num+1):
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 6)
  print(f"jogada {i}:\ndado um: {d1}\ndado dois: {d2}")

  list = [d2,d1]
  list.sort()
  if list[0] < list[1]:
    print(f'{list[0]} < {list[1]}')
  else:
    print(f'{list[0]} = {list[1]}')
  

