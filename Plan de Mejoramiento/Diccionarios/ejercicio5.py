#En el siguiente ejemplo veremos el uso completo de los diccionarios en pthon
#se puede observar tenemos el sistema para adjuntar datos dentro de un diccionario
#y como imprimir los datos que ingresamos en ellos

provincias = {}


def agregar_distrito_provincia(distrito, provincia):
    global provincias
    if not provincia in provincias:
        provincias[provincia] = []
    provincias[provincia].append(distrito)


def imprimir_distritos_de_provincia(provincia):
    if not provincia in provincias:
        print("No hay distritos registrados")
        return

    print("Los distritos de " + provincia + " son: ")
    for distrito in provincias[provincia]:
        print(distrito)


eleccion = ""
while eleccion != "3":
    eleccion = input("""
1. Agregar distrito
2. Mostrar distritos de provincia
3. Salir
Seleccione: """)
    if eleccion == "1":
        distrito = input("Ingrese el distrito: ")
        provincia = input("Ingrese la provincia al que pertenece: ")
        agregar_distrito_provincia(distrito, provincia)
        print("Agregado")
    elif eleccion == "2":
        provincia = input("Ingrese la provincia: ")
        imprimir_distritos_de_provincia(provincia)