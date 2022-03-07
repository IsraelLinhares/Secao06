num = int(input('digite um numero para o inicio: '))
a = num
while a > 0:
    a += 1
    if a%11 == 0 or a%13 == 0 or a%17 == 0:
        print(a)
        a = 0
    