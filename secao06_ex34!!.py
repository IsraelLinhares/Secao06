i = 1
num = 0
Point = 0
while i == 1:
    num += 20
    Point = 0

    for j in range(3,21):

        if num%j != 0:
            Point += 1
    if Point == 0:
        i = 2
        print(num)
