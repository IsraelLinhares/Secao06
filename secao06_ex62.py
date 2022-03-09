unidad = ['zero','um','dois','treis','quatro','cinco','seis','sete','oito','nove']
dezeAlg = ['onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','deznove']
dezenAll = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
cent = ['cem','duzentos','trezetos','quatroscentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
lista = []
for i in range(1,1001):
    if i <= 9:
        lista.append(unidad[i+1])
        
