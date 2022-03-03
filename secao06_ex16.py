num1 = int(input('digite um numero: ')) 
lista=[]
for i in range(num1+1):
    if i%2 != 0:
        lista.append(i)
lista.sort(reverse=True) 
print(*lista) 
