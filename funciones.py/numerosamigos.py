def sumaDivisores(num):
    sum = 0
    for i in range(1, num):
        if num%i == 0:
            suma += 1
        return suma

def amigos(num):
    sum = 0
    if  num == sumaDivisores:
        return ('son amigos')
    else:
        return('no son amigos')

print(amigos(220, 284))
