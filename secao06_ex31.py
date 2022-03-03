
num = int(input('digite um numero: '))
final1 = 0

print('\nsequência 1\n')
cima = 1
for baixo in range(1,num+1):
  final1 += cima/baixo
  cima += 2
print(final1)

