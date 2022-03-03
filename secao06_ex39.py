from re import A


base = int(input('digite o o tamanho da base em centimetros: '))
alt = int(input('digite a altura em centimetros: '))

if base > 0 or alt > 0:
     area = alt*base/2   
     print('a area é:',area)
else:
    print('numero invalido')
