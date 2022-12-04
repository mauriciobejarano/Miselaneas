"""En el siguiente ejemplo veremos el uso de las funciones pero esta vez para hacer calculos 
matematicos con parametros reales o argumentos los cuales para ser mostrados primero se tiene
que llamar"""

def calculo_dos_datos():
    numero_1 = eval(input('Introduce el primer numero: '))
    numero_2 = eval(input('introduce el segundo numero: '))
    resultado = ((numero_1 - numero_2)**2) + 1
    print("n/El primer numero introducido ha sido: ",numero_1)
    print("n/El segundo numero introducido ha sido:",numero_2)
    print('La diferencia entre ellos elevada al cuadrado y luego sumado uno es:', resultado)

def main():
    for i in range(0,3):
        calculo_dos_datos()

main()