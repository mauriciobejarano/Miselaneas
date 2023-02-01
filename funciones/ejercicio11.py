
import random
def llenar_lista(lista):#Definimos una funcion para llenar una lista con numeros aleatorios entre 1 y 100 en un rango aleatorio de 10 a 25 numeros
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)#La variable lista sera igual a la de la funcion anterior
rango=len(lista)#El rango es la longitud de la lista
lista2=lista [:]#Se creara otra lista con los valores de la primera lista usando la rebanada

print('La lista sin ordenar es:',lista)#Imprimimos lista sin ordenar

def burbuja_descendente(lista):
    intercambio=True
    while intercambio: #Mientras el intercambio sea verdad, sera falso momentaneamente
        intercambio=False
        for i in range(len(lista)-1):#Para i en rango de la longitud del vector menos 1
            if lista[i]<lista[i+1]:#Si el primer valor de la lista es menor al segundo, se van a intercambiar, si no se dejan igual y se comparan los 2 siguientes valores--
                lista[i],lista[i+1]=lista[i+1],lista[i]#Ya que i se ira sumando un espacio en la lista por cada ejecucion del for
                intercambio=True#Volvemos a decir que el intercambio sera verdad
    return lista


def burbuja_ascendente(lista2):
    intercambio2=True
    while intercambio2: #Mientras el intercambio sea verdad, sera falso momentaneamente
        intercambio2=False
        for j in range(len(lista2)-1):#Para i en rango de la longitud del vector menos 1
            if lista2[j]>lista2[j+1]:#Si el primer valor de la lista es mayor al segundo, se van a intercambiar, si no se dejan igual y se comparan los 2 siguientes valores--
                lista2[j],lista2[j+1]=lista2[j+1],lista2[j]#Ya que i se ira sumando un espacio en la lista por cada ejecucion del for
                intercambio2=True#Volvemos a decir que el intercambio sera verdad
    return lista2


print('La lista ordenada en forma descendente es:',burbuja_descendente(lista))#Imprimimos la funcion con la lisya ordenada de forma descendencte
print('La lista ordenada en forma ascendente es:',burbuja_ascendente(lista2))#Imprimimos la funcion con la lisya ordenada de forma ascendente