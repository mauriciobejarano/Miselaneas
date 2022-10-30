n = int(input('Ingrese un numero: '))
contador = 0
def multiple(valor, multiple):
    return True if valor % multiple == 0 else False

multiples_5=[]

for i in range(1, n):
    if multiple(i, 5):
        multiples_5.append(i)
print('Los multiples de 5 son: ',multiples_5)