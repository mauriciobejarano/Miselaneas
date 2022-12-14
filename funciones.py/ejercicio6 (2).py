




def costo_minutos(Minutos):#Definimos la funcion "costo_minutos"
    if Minutos<=3 and Minutos>0:#Intervalos con if
        return 'La llamada costó 200 pesos'
    elif Minutos>3:
        Minutos=((Minutos-3)*50)+200 #Ecuacion para determinar el resto de los minutos
        return Minutos
    else:
        return 'El numero ingresado no es valido'

Minutos=int(input('Ingrese la cantidad de minutos usados: '))#Creamos una variable donde pedir el numero
print(costo_minutos(Minutos))#Imprimimos la funcion y dentro la variable "Minutos"