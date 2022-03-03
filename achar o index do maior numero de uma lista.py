resin_gasto = [12]
comer_gasto = [231]
indus_gasto = [3122]
lista = [sum(resin_gasto),sum(comer_gasto),sum(indus_gasto)]
max_lista = max(lista)

print(lista.index(max_lista))