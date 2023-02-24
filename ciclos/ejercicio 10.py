n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
i = 1
mcd = 1

while(i< 9):
    if (n1%i == 0 and n2%i == 0):
        mcd = mcd * i
        n1 = n1 // i
        n2 = n2 // i

    i = i + 1

print("El mcd es: ",mcd)