
print('''

digite 1 para converter km/h para m/s
digite 2 para converter m/s para km/h 
digite 0 para parar o loop
 

''')
i = True
while i:
     num= input('digite o numero: ')
     if num == '1' or  num == '2' or  num == '0':
          if num == '1':
                    Km= int(input('digite o numero em km/h: '))
                    print('conversão para m/s: ', Km *3.6)
          elif num == '2':
                    m= int(input('digite o numero em m/s: '))
                    print('conversão para km/h: ', m/3.6)   
          elif num == '0':
                    print('fim do loop')
                    i = False
     else:
          print('numero invalido') 
          

