

def division_resta (numero1,numero2):#Creamos la funcion "division_resta"
    numero3=numero1
    contador=0
    if numero2>numero1: #Si el segundo numero es mayor, intercambiaran valores
        numero1=numero2
        numero2=numero3
    while numero1>=numero2: #Mientras el primero es el mayor, el menor le ira restando al mayor mientras que el contador aumentara
        numero1-=numero2
        contador+=1
    return contador, numero2

numero1=int(input('Ingrese el primer numero: '))#Creamos una variable donde pedir el primer numero
numero2=int(input('Ingrese el segundo numero: '))#Creamos una variable donde pedir el segundo numero
print(division_resta(numero1,numero2))#Imprimimos la funcion con las variables "numero1","numero2"