def sumaDivisores(num):
    suma = 0
    for i in range(1, num):
        if num%i == 0:
            sum += 1
        return suma

def primo(num):
    sum = sumaDivisores(num)
    if sum == 1:
        return 'Es primo'
    else:
        return 'No es primo'

print(primo(20))