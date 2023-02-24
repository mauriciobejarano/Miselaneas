"""En este ejercico le daremos uso al usuario para que ingrese una serie de datos
los caules seran almacenados y posteriormente introducidos en un diccionnario el cual
al final mostara toda la informacion que el usuario ingreso, una excelente manera de ver
como funcionan los formularios"""


nombre = input('¿Cual es tu nombre? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección actual? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])