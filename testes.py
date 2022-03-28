
lista_centenas = ['cem','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
unidad_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
um_dezenove_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezen_list = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
cent_list = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']

lista = []
dezen_count = 0
Unidad_count = -1
cent_count = 0
a = 0
for i in range(1,999):
    Unidad_count +=1
    if i >= 101:
        a = str(i)
        a = int(a[1:])


    if i%100 == 0:
        lista.append(lista_centenas[cent_count])
        cent_count += 1


    if a >= 1 and a <= 19:


        lista.append(f'{cent_list[cent_count]}e')


    if i < 99 and i%10 == 0:
        lista.append(dezen_list[dezen_count])  
        dezen_count += 1
        Unidad_count = -1
    elif i <= 18:
        lista.append(um_dezenove_list[i-1])
    elif i >= 21 and i <= 99:
        lista.append(f'{dezen_list[dezen_count-1]}e{unidad_list[Unidad_count]}')
lista.append('mil')  
print(lista)

# for i in range(100):
#     if i < 99 and i%10 == 0:
#         print(i//10)
