import sys
from sys import path
path.append('C:\Users\carlo\OneDrive\Documentos\Carlos PYTHON\modulos')




def sumar_fracciones(fracciones):
    suma = 0

    for f in fracciones:
        suma += f[0]/f[1]
    
    return round(suma)



def restar_fracciones(fracciones):
    resta = 0

    for f in fracciones:
        resta -= f[0]/f[1]
    
    return round(resta)



def multiplicar_fracciones(fracciones):
    multiplicacion = 0

    for f in fracciones:
        multiplicacion *= f[0]/f[1]
    
    return round(multiplicacion)

def fraccionar (fracciones):        
    while True:
        try:
            print('Seleccione una opcion para la operar la fraccion')
            print("1- suma")
            print("2- resta")
            print("3- multiplicacion")
            print("4- salir")
            z=int(input())
            match z:
                case 1:
                    print('El resultado a la suma de las fracciones', fracciones, 'es: ')
                    print(sumar_fracciones(fracciones))
                    break
                case 2:
                    print('El resultado a la resta de las fracciones', fracciones, 'es: ')
                    print(restar_fracciones(fracciones))
                    break
                case 3:
                    print('El resultado a la multiplicación de las fracciones', fracciones, 'es: ')
                    print(multiplicar_fracciones(fracciones))
                    break
                case 4:
                    print('Adios, vuelve pronto :D')
                    break
                case _:
                    print("Esta opcion no existe")
        except:
            print("Ingreso un valor no soportado por el sistema\n")