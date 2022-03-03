
t1 = 0
t2 = 1
t3 = 0
soma = 0
while t3 < 4000000:
     t3 = t1 + t2
     t1 = t2
     t2 = t3
     if t3%2==0:
          soma+=t3
print('a soma dos numeros pares da sequência de fibonacci é: ', soma)