
num = int(input('digite um numero: '))
final1 = 0
final2 = 0
final3 = 0
print('\nsequência 1\n')

for i in range(1,num+1):
    final1+= i
print(final1)

print('sequência 2 \n ')

for i in range(1,(num*2-1)+1):
    if i%2 == 0:
      final2-= i
    else:
        final2+=i
print(final2)

print('sequência 3 \n ')

for i in range(1,(num*2-1)+1):
    if i%2 != 0:
      final3+= i
print(final3)
