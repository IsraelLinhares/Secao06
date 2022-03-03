lista = []
for i in range(1, 11):
    num1 = int(input('digite um numero: ')) 
    if num1 > 0:
        lista.append(num1)
    else:
        print("numero inválido")
print(sum(lista)/10)   
  
