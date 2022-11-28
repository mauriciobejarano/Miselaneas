
def validar_dia(dia):
    print('dia')


validar_dia = int(input('ingrese un numero de l dia de la semana: '))

try:
    if validar_dia == 1:
        print('lunes')
    elif validar_dia == 2:
        print('martes')
    elif validar_dia == 3:
        print('miercoles')
    elif validar_dia == 4:
        print('jueves')
    elif validar_dia == 5:
        print('viernes')
    elif validar_dia == 6:
        print('sabado')
    elif validar_dia == 7:
        print('domingo')
    else:
        print('solo se admiten valores de 1 a 7')  
except ValueError:
    print('Solo se admiiten valores numericos')
except TypeError:
    print('Solo se admiiten valores numericos')
except:
    print('no se que hacer con',validar_dia)