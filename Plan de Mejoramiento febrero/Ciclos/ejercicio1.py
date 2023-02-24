#A continuacion veremos los primeros usos de los bucles en pithon con el ciclo for
#en este caso un uso sencillo y didactico de su uso 
palabra = input("Introduce una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])