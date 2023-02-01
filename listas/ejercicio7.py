import random

vec = []
cont1 = 0
sum = 0 
prom = 0


for i in range (10, 25):
    vec.insert(i,round(random.random()*100))
print(vec)


for i in range(len(vec)):
    cont1 += 1
    sum += vec[i]
    prom = sum/cont1
print("La suma de los numeros de la lista es: ",sum)
print("El promedio de los numeros de la lista es: ",round(prom))