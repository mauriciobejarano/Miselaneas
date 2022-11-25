def es_un_numero_perfecto(numero):
    suma = 0

    for i in range(numero):
        if numero % i == 0:
            suma += i
        else:
            print("El numero no es perfecto!")

    return suma == numero

es_un_numero_perfecto = int(input("Ingrese un numero: "))
print("El numero",es_un_numero_perfecto,"es perfecto")