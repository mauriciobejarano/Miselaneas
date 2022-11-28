rang = int(input("Cunatos numeros desea que se muestren: "))
if rang <= 5:
    print("¡¡debe tener minimo 5 elementos!!")
if rang >=20:
    print("¡¡deb tener maximo 20 elementos!!")
else:
    fib = [0,1]
for i in range(rang - 2):
    fib.append(fib[-1] + fib[-2])
print(fib)