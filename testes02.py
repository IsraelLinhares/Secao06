

lista_centenas = ['cem','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
unidad_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
um_dezenove_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezen_list = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
cent_list = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
lista = []
a = 0
cent_count = 0
for i in range(1,999):
    if i%100 == 0:
        cent_count+=1
    if i >= 101:
        a = str(i)
        a = int(a[1:])
    if a >= 1 and a <= 19:
        lista.append(f'{cent_list[cent_count]}e{um_dezenove_list[a-1]}')
print(lista)