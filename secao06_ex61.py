

for i in range(100,1000):

    for i2 in range(100,1000):
        R = str(i*i2)
        if R[::1] == R[::-1]:
            print(f'{R} = {i} * {i2}')
            
