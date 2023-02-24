import sys
from sys import path
path.append('C:\\Users\\carlo\\OneDrive\\Documentos\\Carlos PYTHON\\modulos')
import mate as m

while True:
    x=int(input('Cuantas fracciones desea operar? '))
    if x>1 :

        numeros=[]
        for i in range(x):
            numeros.append([])
            for j in range (1):
                numeros[i].append(int(input('ingrese numerador: ')))
                numeros[i].append(int(input('ingrese denominador: ')))

        print('Su fraccion es: ', numeros)
        print()
        

        print(m.fraccionar(numeros))

        while True:
            y=int(input('Desea seguir operando fracciones? \n 1- Si \n 2- No \n'))
            match y:
                case 1:
                    break
                case 2:
                    print('Adios, vuelve pronto :D')
                    break
                case _:
                    print("Esta opcion no existe")
                    continue

        if y == 2:
            break

    else: 
        print('El numero de fracciones debe ser mayor a 1')