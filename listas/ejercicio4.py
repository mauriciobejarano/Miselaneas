import random

vec=[]
for i in range (10, 25):
    vec.insert(i,round(random.random()*100))
print(vec)


def ordenamineto_burbuja(vec):
    for n in range(len(vec) -1, 0, -1):
        for i in range(n):
            if vec[i] > vec[i + 1]:
                temp = vec[i]
                vec[i] = vec[i + 1]
                vec[i + 1] = temp
print(vec)

