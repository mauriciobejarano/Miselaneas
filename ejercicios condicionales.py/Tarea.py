import random

vec = []
cont1 = 0
sum = 0 
prom = 0
moda = 0
median = 0
desvsatand = 0

for i in range (10, 25):
    vec.insert(i,round(random.random()*100))
print(vec)


for i in range(len(vec)):
    cont1 += 1
    sum += vec[i]
    prom = sum/cont1








def median(dataset):
    data = sorted(dataset)
    index = len(vec) // 2
    
    
    if len(dataset) % 2 != 0:
        return data[index]
    
    
    return (data[index - 1] + data[index]) / 2



print ('La suma total es: ', sum)
print ('El promedio es: ',prom)
print ()
print ('La mediana de los datos es: ',median(vec))


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

print ('La suma total es: ', sum)
print ('El promedio es: ',round(prom))
