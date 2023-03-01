values = (1, 0)       #En esta linea de codigo se le asigna a la variable una tupla la cual se usara como atributo mas adelante
#x,y=19,30
#print(divmod(10,3)) 
try:                  #este es el bloque de codigo try donde se pondra el codigo suceptible a errores
    q, r = divmod(*values) # Esta linea de codigo permite dividir los dos numeros de la variabley devolver el residuo
    #print('q=',q)
    print(f'q={q}') # esta linea de codigo permite imprimir la operacion y el texto en un solo bloque
    print(f'r={r}')   # bis la linea de arriba
except (ZeroDivisionError, TypeError) as e: # en esta linea de codigo es ponen los errores que pueden ser suceptibles a currir en el bloque try
    
    print(type(e), e) # imprime la respuesta si se da el caso de arriba