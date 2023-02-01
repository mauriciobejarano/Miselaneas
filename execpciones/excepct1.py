from math import sqrt

a, b ,c = input("ingrese los numeros que desea, !separar por comas¡").split(',')
a = int(a)
b = int(b)
c = int(c)

def resolver(a, b, c):
    
    try:
        x1 = b + sqrt(b**2 - 4*a*c) / (2*a)
        x2 = b - sqrt(b**2 - 4*a*c) / (2*a)
        resultado={
            'positivo': x1,
            'negativo': x2
        }
    except ValueError:
        print('!NO ES POSIBLE SACAR LA RAIZ')
    except ZeroDivisionError:
        print('!NO SE PUEDE DIVIDIR POR CERO')
    except:
        print('!ERROR DE SINTAXIS')

resolver(a,b,c)