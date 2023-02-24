palabra = str(input('Ingresa una palabra: ')) 

letras_dic = dict()  
contador = 0 

for letra in palabra: 
    if letra in letras_dic: 
        if letras_dic[letra] == 1: 
            contador += 1 
        letras_dic[letra] += 1 
    else:
        letras_dic[letra] = 1 
    

print(letras_dic)
print(contador)
