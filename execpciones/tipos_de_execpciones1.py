numero = int(input('Ingrese el numero: '))
contador = 0
for i in range(1, numero+1):
    if numero%i == 0:
            print(i)
        contador = contador+1

print("La cantidad de divisores de" ,numero, "es" ,contador)