"""en este ejercicio los meses y su respectivo numero de mes estan en un diccionarios
al usuario se le pedire que ingrese un dia en formato ddmmaa y el sistema debe devolver el mismo valor en texto"""


meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])