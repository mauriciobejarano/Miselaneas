spotify={}
canciones={}
def añadirArtista (diccionario):
    while True:
        artista=input("Ingrese nombre del artista  ")
        if artista =="":
            break
        if artista in diccionario.keys():
            canciones=diccionario[artista]
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
        else:
            canciones={}
            cancion=ingresarCanciones(artista,canciones)
            diccionario[artista]=cancion
    
    return diccionario

def ingresarCanciones (artista,diccionario):
    print(diccionario)
    while True:
        print("Ingrese nombre de la canción", end=":  ")
        cancion=input()
        if cancion =="":
            break
        print("ingrese el genero de la canción ",end=": ")
        genero=input()
        if genero=="":
            break
        print("ingrese la duración de la canción",end=": ")
        duracion=input()
        if duracion=="":
            break
        if cancion in diccionario:
            print("ATENCIÓN::::LA CANCIÓN YA FUE AGREGADA AL SPOTIFY")
        else:
            diccionario[cancion]=(genero,duracion,)
        print("Vas  a seguir agregando canciones para: ",artista,"\n Presione Enter para salir o cualquier tecla para seguir",end=":    ")
        sigue=input()
        if sigue=="":
            break
    return diccionario

def buscarArtista (diccionario):
    nombre=input("Ingrese el nombre del artista a buscar:  ")
    print(diccionario.keys())
    if nombre in diccionario.keys():
        print("El artista se encuentra en nuestra lista de reproducción\n y estas son sus canciones:")
        musica=diccionario[nombre]
        for cla,valor in musica.items(): 
            print (cla,"genero:",valor[0],"duración:",valor[1],sep=" -> ",end="minutos \n")
    else:
        print("El artista no se encuentra en nuestra lista de reproducción")

def buscarCancion (diccionario):
    cancion=input("Ingrese el nombre de la cancion a buscar: ")
    for j in diccionario:
        musica=diccionario[j]
        if cancion in musica.keys():
            return print ("La canción se encuentra en el Spotify y el artista es: ",j)
    print("no se encontro la canción en el Spotify")


def eliminarArtista (artista,diccionario):
    if artista in diccionario.keys():
        del diccionario[artista]
    return diccionario

def ordenarAlfabeticamente (diccionario):
    orden=sorted(diccionario.items())
    print("Biblioteca SPOTIFY ordenada alfabeticamente x Artista: \n",orden)

def masCanciones (diccionario):
    mayor=0
    for x in diccionario:
        cancion=len(diccionario[x])
        if cancion > mayor:
            mayor=cancion
            actor=x
    return (actor, mayor)

def masLarga(diccionario):
    #print(diccionario)
    lista=[]
    for x in diccionario:
        canciones=diccionario[x]
        #print(canciones)
        larga=0
        for can,j in canciones.items():
            valor=j
            tiempo=int(valor[1])
            if larga<tiempo:
                larga=tiempo
                cancionmay=can
        lista+=[x,cancionmay,larga]
        mayor=0
        artistamayor=[]
        for x in range(2,len(lista),3):
            if lista[x]>mayor:
                artistamayor=lista[x-2],lista[x-1],lista[x]
                mayor=lista[x] 
    return (artistamayor)

def masCorta(diccionario):
    #print(diccionario)
    lista=[]
    for x in diccionario:
        canciones=diccionario[x]
        #print(canciones)
        larga=99999999999999
        for can,j in canciones.items():
            valor=j
            tiempo=int(valor[1])
            if tiempo<larga:
                larga=tiempo
                cancionmen=can
        lista+=[x,cancionmen,larga]
        menor=99999999999
        artistamenor=[]
        for x in range(2,len(lista),3):
            if menor>lista[x]:
                artistamenor=lista[x-2],lista[x-1],lista[x]
                menor=lista[x]
    print (lista) 
    return (artistamenor)

def menu ():
    while True:
        print ("BIENVENIDO A LA BIBLIOTECA SPOTIFY")
        print ("Seleccione el número de la lista según lo que desee")
        print (" 1 Añadir Artista")
        print (" 2 Buscar Artista")
        print (" 3 Buscar Cancion")
        print (" 4 Eliminar Artista")
        print (" 5 Ordenar Alfabeticamente")
        print (" 6 El que tiene mas canciones")
        print (" 7 El que tiene la canción mas larga")
        print (" 8 El que tiene la canción mas Corta")
        print (" 9 Salir")
        seleccion=input()
        match seleccion:
            case "1":
                print(añadirArtista(spotify))
            case "2":
                buscarArtista(spotify)
            case "3":
                buscarCancion(spotify)
            case "4":
                nombre=input("Ingrese el nombre del artista a eliminar:  ")
                print("Nueva Biblioteca Spotify: ",eliminarArtista(nombre,spotify))
            case "5":
                ordenarAlfabeticamente(spotify)
            case "6":
                mayor=masCanciones (spotify)
                print("El artista con mas canciones es:",mayor[0],"con ",mayor[1]," canciones",sep="  ")
            case "7":
                larga=masLarga(spotify)
                print ("El artista con la canción más larga es: ")
                print (larga[0], " con la canción ",larga[1]," y la duración es: ",larga[2])
            case "8":
                corta=masCorta(spotify)
                print ("El artista con la canción más corta es: ")
                print (corta[0], " con la canción ",corta[1]," y la duración es: ",corta[2])
            case "9":
                print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                break
            case _:
                print("digitastes un número incorrecto")


menu()
