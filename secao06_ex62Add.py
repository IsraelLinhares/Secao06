# #add um numero a informar

# unidad_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
# um_dezenove_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
# dezen_list = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
# cent_list = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
# soma = ''

# #um até dezenove
# for i in range(len(um_dezenove_list)):
#     soma += um_dezenove_list[i]

# #dezenas apenas(20,90)
# for i in range(len(dezen_list)):
#     soma += dezen_list[i]

  
# #dezenas e unidades
# for i in range(len(dezen_list)):
#     for i2 in range(len(unidad_list)):
#         soma+=f'{dezen_list[i]}e{unidad_list[i2]}'

#  #centenas com 1 até 19
# for i in range(len(cent_list)):
#     for i2 in range(len(um_dezenove_list)):
#         soma+=f'{cent_list[i]}e{um_dezenove_list[i2]}'

# #centenas e dezenas apenas
# for i in range(len(cent_list)):
#     for i2 in range(len(dezen_list)):
#         soma+=f'{cent_list[i]}e{dezen_list[i2]}'

# #centenas , dezenas e unidades (121, 999)
# for i in range(len(cent_list)):
#     for i2 in range(len(dezen_list)):
#         for i3 in range(len(unidad_list)):
#             soma+=f'{cent_list[i]}e{dezen_list[i2]}e{unidad_list[i3]}'
              
# soma+='cemmil'



    
# print(len(soma))


# #add um numero a informar



lista_centenas = ['cem','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
unidad_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove']
um_dezenove_list = ['um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezen_list = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
cent_list = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
soma = ''


#um até dezenove
for i in range(len(um_dezenove_list)):
    soma += um_dezenove_list[i]+' '

# #dezenas apenas(20,90)
# for i in range(len(dezen_list)):
#     soma += dezen_list[i]+' '

soma += """








"""



lista_de_dezenUni = []
#fazer essa lista para o if
#dezenas e unidades
for i in range(len(dezen_list)):
    for i2 in range(len(unidad_list)):
        soma+=f'{dezen_list[i]}e{unidad_list[i2]}'+' '
        lista_de_dezenUni.append(f'{dezen_list[i]}e{unidad_list[i2]}')
 #centenas com 1 até 19

lista_centenas_19 = []
soma += """






"""
for i in range(len(cent_list)):
    for i2 in range(len(um_dezenove_list)):
        soma+=f'{cent_list[i]}e{um_dezenove_list[i2]}'+' '
        lista_centenas_19.append(f'{cent_list[i]}e{um_dezenove_list[i2]}')
#centenas e dezenas apenas

centenas_dezenas = []
soma += """






"""
for i in range(len(cent_list)):
    for i2 in range(len(dezen_list)):
        soma+=f'{cent_list[i]}e{dezen_list[i2]}'+' '
        centenas_dezenas.append(f'{cent_list[i]}e{dezen_list[i2]}')
soma += """






"""
#centenas , dezenas e unidades (121, 999)
for i in range(len(cent_list)):
    for i2 in range(len(dezen_list)):
        for i3 in range(len(unidad_list)):
            soma+=f'{cent_list[i]}e{dezen_list[i2]}e{unidad_list[i3]}'+' '
soma += """






"""
for i in lista_centenas:
    soma+=i+' '
              
soma+=' mil'
All = len(soma)



#transformando o numero em string 


numero_de_corte = ''
n = int(input('digite: '))

if n <= 19:
    numero_de_corte = um_dezenove_list[n-1]
elif n == 1000:
    numero_de_corte = 'mil'
elif len(str(n)) == 3 and int(str(n)[1])==0 and int(str(n)[2])==0 :
    numero_de_corte =  lista_centenas[int(str(n)[0])-1]

elif len(str(n)) == 3 and int(str(n)[2])==0 :
    numero_de_corte = (f'{cent_list[int(str(n)[0])-1]}e{dezen_list[int(str(n)[1])-2]}')

elif n%10 == 0:
    numero_de_corte = dezen_list[(n//10) -2]

elif n >= 20 and n <= 99:
    n = str(n)
    numero_de_corte = f'{dezen_list[int(n[0])-2]}e{unidad_list[int(n[1])-1]}'
elif len(str(n)) == 3 and int(str(n)[1:3]) <= 19 :
    numero_de_corte = f'{cent_list[int(str(n)[0])-1]}e{um_dezenove_list[int(str(n)[1:])-1]}'
elif len(str(n)) == 3:
    numero_de_corte = (f'{cent_list[int(str(n)[0])-1]}e{dezen_list[int(str(n)[1])-2]}e{unidad_list[int(str(n)[2])-1]}')


print(numero_de_corte)
print(soma)
# soma = soma.split()
# corte = soma.index(numero_de_corte)
# soma_cortada = soma[:corte+1]
# print(soma_cortada)

