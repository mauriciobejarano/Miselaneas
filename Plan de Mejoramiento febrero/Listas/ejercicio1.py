"""El usuario ingresara edades al azar y el programa los ordenara de mayor a menor"""
edades = []
for i in range(6):
    edades.append(int(input("Introduce una edad en numero: ")))
edades.sort()
print("Los números ganadores son " + str(edades))