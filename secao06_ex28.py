num = int(input('digite um numero: '))
E = 1
for n in range(1,num+1):
    for i in range(2,n):
        n = n * i
    E = E + 1/n
    print(E)