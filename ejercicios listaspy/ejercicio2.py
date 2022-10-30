import random


vec=[] 
x=1
c=0
cont1 = 0

for i in range (10, 25):
    vec.insert(i,round(random.random()*100))
print(vec)


for i in range(len(vec)):
    cont1 + 1
    c=0
    if vec[i] % x == 0:
        c = c +1
    x = x +1
    if c == 0:
        print('El numero',vec[i] ,'es primo')
    else:
        print('El numero',vec[i],'no es primo')