"""En este ejercicio veremos como es la utilización del condicional if cuando se anida
esto significara que resolvera simultaneamente lo que desee que evalue, en este caso se puede generar un menu con el bucle
dando por terminado un sistema de ordenes de lo que desees"""

#Uso de un menú con los tipos de sanwiches
print("Bienvenido a la Sanwich Italian.\nTipos de sandwiches\n\t1- Vegetariano\n\t2- Tradicional\n")
tipo = input("Introduce el número correspondiente al tipo de Sandwich que quieres: ")
# Decisión sobre el tipo de sanwich
if tipo == "1":
    print("Ingredientes de sandwich vegetariano\n\t 1- Pepinillos\n\t2- Aguacate\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Sandwich vegetariano con cebolla, tomate, lechuga y ", end="")
    if ingrediente == "1":
        print("PEPINILLOS")
    else: 
        print("AGUACATE")
else:
    print("Ingredientes de Sanwich tradicional\n\t1- Pollo\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Tu elección fue:\nSandwich Tradicional con queso, tomate, cebolla, lechuga y ", end="")
    if ingrediente == "1":
        print("POLLO")
    elif ingrediente == "2":
        print("jAMÓN")
    else:
        print("SALMÓN")