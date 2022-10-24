def cantidad_dias(mes):
    if mes.lower() in ('Enero','Marzo', 'Julio','Agosto', 'Octubre', 'Diciembre'):
        return '31'
    elif mes.lower() == 'Febrero':
        return '28/29'
    else:
        return '30'


nombre_mes = input('Ingrese el nombre del mes: ')

print(cantidad_dias (nombre_mes))