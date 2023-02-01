

def obrero_horas(horas):#Definimos la funcion "obrero_horas"
    h2=horas-40
    if horas<=40:#Intervalos con if
        horas*= 2600
        return horas
    elif horas>40:
        horas=40
        horas*=2600
        h2*=5000
        return (horas+h2)

horas=int(input('Ingrese la cantidad de horas trabajadas: '))#Creamos una variable donde pedir el numero
print('El salario por las obras trabajadas es de',obrero_horas(horas),'pesos')#Imprimimos la funcion y dentro la variable "horas"