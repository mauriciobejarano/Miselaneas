"""En el siguiente ejmplo veremos los diferentes tipos de datos
que pueden tener las funciones con funciones matematicas para hacer calculos"""
def calculo_multiple(a, b):
    sum = a + b
    res = a - b
    mul = a * b
    return(sum, res, mul, a / b, a ** b)

def main():
    print('Introduce los dos valores sobre los que se haran los calculos: ')
    num1 = eval(input('Numero 1: '))
    num2 = eval(input('Numero 2: '))
    suma, resta, multiplicacion, divicion, potencia = calculo_multiple (num1, num2)

    print('La suma es: ', suma)
    print('La resta es: ', resta)
    print('La multiplicación es: ',multiplicacion)
    print('La divición es: ', divicion)
    print('La potencia es: ', potencia)

main()