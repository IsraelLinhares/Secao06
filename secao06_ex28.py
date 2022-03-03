numero = int(input("Fatorial de: ") )
fator=1
div = 1
for n in range(1,numero+1):
    fator *= n
    div += 1/fator
print(div)

