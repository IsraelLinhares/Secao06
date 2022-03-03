a= int(input('digite o numero: '))
b= int(input('digite o numero: '))

lista=[]
for num in range(a+1,b):

    score = 0 
    for i in range(1,num+1):
        if (num%1 == 0) and (num%i == 0): 
            score += 1
       
    if score <= 2:
        lista.append(num)  
print(lista)
print(f'existem {len(lista)} primos entre {a} e {b}')