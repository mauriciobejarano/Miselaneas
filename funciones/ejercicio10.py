


def potencia(x,y):#Definimos la funcion "potencia"
    i=1
    potent=x
    while(i<y): #Mientras i sea menor al exponente, se ira sumando de 1 en 1 y potencia sera el mismo valor de x multiplicado por si mismo
        i+=1
        potent*=x
    if y<=0: #Si el exponente es igual o menor a 0, el resultado de la potencia sera 1
        potent=1
    
    return potent

x=int(input('Ingrese la base: '))#Creamos una variable donde pedir el primer numero
y=int(input('Ingrese el exponente: '))#Creamos una variable donde pedir el segundo numero
print(potencia(x,y))#Imprimimos la funcion con las variables "x","y"