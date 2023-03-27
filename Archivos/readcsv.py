from organizacion import *                                        #En esta linea de codigo  se traera todas las funciones de la clase "organización"
import csv                                                        #En esta linea de codigo se taera el modulo CVS para poder leer el documento

listaOrganizaciones = []                                          #En esta linea de codigo se asignaran todas las organizaciones en una lista

with open('C:\\Users\\APRENDIZ\\Documents\\1-REPOlocal-MB\\Archivos\\enterprises.csv') as csvDataFile: #Esta linea de codigo una el with para crear un bloque de codigo para manipular archivos en la direccion absoluta que le he dado y le asignare un nombre a ese archivo
    
    csvReader = csv.reader(csvDataFile)                     # el nombre del archivo sera igual al modulo y el lector CSV
    
    for emp in csvReader:                                   #usaremos un for para recorrer el archivo dato pot dato e el formato CSV 
        org = Organizacion(emp[2], emp[3], emp[4], emp[6],emp[7])  #los nombres de las organizaciones usaran las finciones que habremos designado  en el archivo Organizaciones 
        listaOrganizaciones.append(org)                    #las organizaciones se almacenaran en las lista anteriormente declarada
print(listaOrganizaciones)                                 # imprimira las organizaiones que se hayan almasenado segun los parametro declarados en las funciones del archivo Organizaciones
for emp in listaOrganizaciones:                            #usaremos un for para recorer las lista anteriormente llenada
    print(emp.nombreySitio())                              # imprimira cada uno de los valores con lo parametro de funcion la cual devolvera nombre y sitio en la web