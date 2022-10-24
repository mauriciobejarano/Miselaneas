x = int(input('Digite el primer numero: '))
y = int(input('Digite el segundo numero: '))
z = int(input('Digite el tercer numero: '))

menor = min(x, y, z)
mayor = max(x, y, z)
valor_medio = (x + y + z) - menor - mayor

print(valor_medio)

print()
