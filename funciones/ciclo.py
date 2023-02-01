def sumaDivisores(num):
    sum = 0
    for i in range(1, num):
        if num%i == 0:
            suma += 1
        return suma

def perfectos(num):
    suma = sumaDivisores(num)
    if sum == num:
        return 'perfecto'
    else:
        return 'imperfecto'

print(perfectos(20))


