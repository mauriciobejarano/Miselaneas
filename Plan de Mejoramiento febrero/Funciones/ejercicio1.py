"""En el siguientwe ejercicio veremos la implementación de las funciones
en python la cual la estructura se tiene que difinir para que luego pueda
ser llamada"""

def media(numeros):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(numeros)/len(numeros)

print(media([1, 5, 3, 7, 9]))
print(media([2.5, 7.2, 4.8, 1.7, 20.4, 19.9]))