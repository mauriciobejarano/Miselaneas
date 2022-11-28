print('Ingrese un numero entre 0 y 99.999: ')
num = int(input())
if(num<0 or num>99999):
    print('¡¡El numero ingresado es invalido!!')
else:
    if(num<10):
        print('El numero ingresado tiene 1 cifra')
    elif(num<100):
        print('El numero tiene 2 cifras')
    elif(num<1000):
        print('El numero tiene 3 cifras')
    elif(num<10000):
        print('El numero tiene 4 cifras')
    elif(num<100000):
        print('El numero tiene 5 cifras')
    