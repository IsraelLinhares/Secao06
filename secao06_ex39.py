i = 1
while i == 1:
     base = input('digite o o tamanho da base em centimetros: ')
     alt = input('digite a altura em centimetros: ')
     if base.isnumeric() and alt.isnumeric():
          base = int(base)     
          alt = int(alt)     
          if base > 0 and alt > 0:
               area = alt*base/2   
               print('a area é:',area)
               i = 2
          else:
            print('numero invalido')
     else:
          print('numero invalido')
