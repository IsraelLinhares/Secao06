


n= 1
while n == 1:
  num = input('digite um numero: ')
  mul1 =input('digite um numero: ')
  mul2 = input('digite um numero: ')
  if num.isnumeric() and mul1.isnumeric() and mul2.isnumeric():
    num = int(num)
    mul1 = int(mul1)
    mul2 = int(mul2)
    for i in range(num+1):
      if i%mul1 == 0 or i%mul2 ==0: 
        print(i)
    n = 2
  else:
    print('!!digite apenas numeros!!')
    