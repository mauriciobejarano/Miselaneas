palabra = str(input('Ingresa una palabra: ')) 
caracter = str(input('Escriba el caracter que quiere ver cuantas veces se repite en la palabra: '))

contador = 0 

for letra in palabra: 
    if caracter in palabra: 
        if caracter == letra:
            contador +=1
print('el caracter >',caracter,'< se repite',contador,'veces')
print(contador)