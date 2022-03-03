
i = True
while i:
     print('''
digite 1 para subtração
digite 2 para adição
digite 3 para multiplicação
digite 4 para divisão

''')
     num= input('digite o numero: ')
     if num == '1' or  num == '2' or  num == '0':
          if num == '1':
                    num1= int(input('digite um numero '))
                    num2= int(input('digite um numero '))
                    print(f'a soma é: {num1 + num2}')
                    R= input('deseja continuar? s/n: ')
                    if R != 'n' or R != 'não':
                         continue
                    else:
                         i = False
          elif num == '2':
                    num1= int(input('digite um numero '))
                    num2= int(input('digite um numero '))
                    print(f'a subtração é: {num1 - num2}')
                    R= input('deseja continuar? s/n: ')
                    if R != 'n' or R != 'não':
                         continue
                    else:
                         i = False
          elif num == '3':
                    num1= int(input('digite um numero '))
                    num2= int(input('digite um numero '))
                    print(f'a subtração é: {num1 * num2}')
                    R= input('deseja continuar? s/n: ')
                    if R != 'n' or R != 'não':
                         continue
                    else:
                         i = False   
          elif num == '4':
                    num1= int(input('digite um numero '))
                    num2= int(input('digite um numero '))
                    print(f'a subtração é: {num1 / num2}')
                    R= input('deseja continuar? s/n: ')
                    if R != 'n' or R != 'não':
                         continue
                    else:
                         i = False   
     else:
          print('numero invalido') 
          continue