i = 0
list=[]
while i == 0:
     R1 = int(input('digite uma idade: '))
     list.append(R1)
     if R1 <= 0 :
          i = 1
          print(f'a media é: {sum(list)/len(list)} ')
 