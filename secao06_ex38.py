

for i in range(1, 376):
    a = 0
    b = 0
    c = 0
    for j in range(1, 376):

        a = j
        b = i
        c = (a ** 2 + b ** 2) ** 0.5

        if b > a:
            if (a + b + c) == 1000:

                print(f"valor de 'a' = {a}")
                print(f"valor de 'b' = {b}")
                print(f"valor de 'c' = {int(c)}")
                print()