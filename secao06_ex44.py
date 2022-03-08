
num= int(input('digite o numero: '))
t1 = 0
t2 = 1
t3 = 1
if num > 0:
     print(0)

     while num > t3:
          print(t3)
          t3 = t1 + t2
          t1 = t2
          t2 = t3
          if t3 >= num:
               print(t3)
else: 
     print('numero invalido')