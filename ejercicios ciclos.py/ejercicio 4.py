num = int(input("Ingrese un numero hasta : "))
if num > 1:
    cont = 0
    for i in range(2,num):
        resto = num %i
        
        if resto == 0:
            cont += 1
    if cont == 0:
        print("El {} es un numero primo".format(num))
    else:
        print("El {} no es un numero primo".format(num))
else:
    print("El {} no es un numero primo".format(num))