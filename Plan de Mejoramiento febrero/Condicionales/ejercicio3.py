"""En el siguinte ejercico veremos el uso de el elif el cual resuelve que 
podamos hacer diferentes conciones en una misma estructura dependiento de
el primer if que se haya codificado, en este caso en particular nos permite evaluar cual sera su puntuacion final"""

bonificacion = 240000
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento y de ahi te dara una bonificacion o no
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento, si el usuario ingresa un especio vacio este se invalidara
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f$" % (puntos * bonificacion))