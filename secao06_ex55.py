rang= int(input('digite o numero: '))
lista=[]
if rang >=1:
    for num in range(2,rang+1):
        score = 0 
        for i in range(1,num+1):
            if (num%1 == 0) and (num%i == 0): 
                score += 1
        
        if score <= 2:
            lista.append(num)  
    print(lista)
    print(sum(lista))
else:
    print('numero invalido')