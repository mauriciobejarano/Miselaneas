n = int(input('Ingrese numero de veces a ejecutar: '))
if  n > 0:

    positivos = 0 
    

    for i in range (m):
        dato = int(input('Ingrese un numero N: '))

        if dato > 0 :
            positivos += 1
        elif dato < 0:
            print('Fin de la operacion')
            print('La cantidad de numeros positivos fue: ',positivos,)
