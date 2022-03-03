
lista=[]
for num in range(2000000):

    score = 0 
    for i in range(1,num+1):
        if (num%1 == 0) and (num%i == 0): 
            score += 1
       
    if score <= 2:
        lista.append(num)  
print(sum(lista))