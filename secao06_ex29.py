total = 0

for i in range(1, 6):
    fator = 2*i

    for t in range(1, fator):
        fator*=t

    total += i/fator

print(total)