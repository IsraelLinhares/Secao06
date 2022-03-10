

unidad_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
um_dezenove_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezen_list = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
cent_list = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
soma = ''

#um até dezenove
for i in range(len(um_dezenove_list)):
    soma += um_dezenove_list[i]

#dezenas apenas(20,90)
for i in range(len(dezen_list)):
    soma += dezen_list[i]

  
#dezenas e unidades
for i in range(len(dezen_list)):
    for i2 in range(len(unidad_list)):
        soma+=f'{dezen_list[i]}e{unidad_list[i2]}'

 #centenas com 1 até 19
for i in range(len(cent_list)):
    for i2 in range(len(um_dezenove_list)):
        soma+=f'{cent_list[i]}e{um_dezenove_list[i2]}'

#centenas e dezenas apenas
for i in range(len(cent_list)):
    for i2 in range(len(dezen_list)):
        soma+=f'{cent_list[i]}e{dezen_list[i2]}'

#centenas , dezenas e unidades (121, 999)
for i in range(len(cent_list)):
    for i2 in range(len(dezen_list)):
        for i3 in range(len(unidad_list)):
            soma+=f'{cent_list[i]}e{dezen_list[i2]}e{unidad_list[i3]}'
              
soma+='cemmil'



    
print(len(soma))


