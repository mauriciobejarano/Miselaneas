import random
filas = round(random.randint(2,5))
lista = [[]for i in range(filas)]
print(lista)
col = round(random.randint(2,5))
for i in (lista):
    for j in range(col):
        i.append(round(random.random()*100))
print(lista)

lista1 = [[round(random.random()*100) for i in range(col)]for i in range(filas)]
print(lista1)