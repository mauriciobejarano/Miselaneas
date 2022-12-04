"""En el siguiente ejercicio apresiaremos como funciona los
diccionarios en python, cada referencia sera asiganda despues de 2 puntos
tambien veremos como cambiar un valor a un diccionario y poner otro"""
diccionario={'animal': 'gato',
             'cosa':'piedra',
             'planta':'lechuga'}
print(diccionario)

print(diccionario['animal'])

print(diccionario['planta'])

diccionario['planta'] = 'coliflor'

print(diccionario['planta'])
