i = 0
while i == 0:
     R1 = int(input('digite um numero: '))
     R2 = int(input('digite um numero: '))
     if R1 == 0 or R2 ==0:
          i = 1
          print('resistência igual a zero')
     else:     
          print(f'({R1} * {R2}) / ({R1}+{R2}) = {(R1 * R2)/(R1+R2)}')
    
