def positivos():
    print('Intentando crear funcion de positivos xd')
    for i in range(5,10,20):
        print(i)

def negativos():
    print('segundo intento de crear funcion negativos en modulo')
    for i in range(-5,-10,-20):
        print(i)

def impares():
    print('creando tercera funcion en modulo')
    for i in range(1,30,2):
        print(i)

def primos():
    print('cuarta funcion en mi modulo de python')
    for i in range(1,50,1):
        print(i)

def celcius_a_kelvin(temperatura):
    print('quinta y ultima funcion en modulo de python')
    return temperatura + 273.15

temperatura_k = celcius_a_kelvin(30)
print('La temperatura en K es: ', temperatura_k )

