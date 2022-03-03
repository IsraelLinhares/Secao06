
num1 = int(input('digite o numero: '))
num2 = int(input('digite o numero: '))
rang = int(input('digite o numero: '))


original_list = []

for i in range(rang+1):
  mul1 = num1*i
  mul2 = num2*i
  original_list.append(mul1)
  original_list.append(mul2)
  
convert_list_to_set = set(original_list)

original_list = list(convert_list_to_set)
original_list.sort()
print(*original_list[0:rang])