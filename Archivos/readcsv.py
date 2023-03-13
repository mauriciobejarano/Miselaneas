from organizacion import *
import csv

listaOrganizaciones = []

with open('C:\\Users\\APRENDIZ\\Documents\\1-REPOlocal-MB\\Archivos\\enterprises.csv') as csvDataFile:
    
    csvReader = csv.reader(csvDataFile)
    
    for emp in csvReader:
        org = Organizacion(emp[2], emp[3], emp[4], emp[6],emp[7])
        listaOrganizaciones.append(org)
print(listaOrganizaciones) 
for emp in listaOrganizaciones:
    print(emp.nombreySitio())       