"""En el siguente veremos uno de los condicionales que python nos puede
ofrecer para resolver diferentes tipos de situaciones que se nos puedan
presentar en el ambito de la programación, veremos el uso de el condicional
if y como se usa, en este caso tomar decicion segun el caso que le digamos"""


edad = int(input("Introduce tu edad: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10

print("El precio de la entrada es", precio, "$.")