sal = 2000
j = 0.015

print(f'em 1995 ele ganhava 2000')
for i in range(26):
     print(f'em {1996+i} ele recebia {round(sal + (sal*j))} R$')
     j = j*2
print('em 2021 ele recebe 1006634960 R$')