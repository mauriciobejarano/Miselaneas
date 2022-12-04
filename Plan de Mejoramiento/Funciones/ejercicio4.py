"""En el siguiente ejemplo veremos el uso de variables con el uso de
funciones cuando una variable es declarada global"""
x = 5
def funcion2():
    global x
    x = x + 5
    print('La variable x dentro de funcion2 vale: ', x)

def main():
    funcion2()
    global x
    x = x + 10
    
    print('La variable x dentro de main vale:   ', x)

main()