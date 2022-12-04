"""Otra forma de accceder a los datos de una lista es atraves
 de los rangos  que se les pueden dar como los veremos a continuación"""
lista = ['primero','segundo','tercero','cuarto','quinto','sexto']
lista2 = lista[1:4]

print(lista2)

lista2[0:2] = ['otro', 'y otro']
print(lista2)
