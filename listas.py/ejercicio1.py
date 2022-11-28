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
    if (vec[i]<prom):
        print(vec[i],': esta debajo del promedio ')
    elif vec[i]>prom:
        print(vec[i],' :esta por ensima del promedio')
    elif vec[i]== prom:
        print (vec[i],' :es igual al promedio')



