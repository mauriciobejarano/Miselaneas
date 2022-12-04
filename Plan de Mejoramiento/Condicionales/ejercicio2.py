"""En este ejercicio veremos como es la utilikzación del condicional if cuando se anida
esto significara que resolvera simultaneamente lo que desee que evalue."""

a = 1
b = 1
c = 1

if (a == b):
    if (b == c):
        print('a es igual b igual c ')
    else:
        print('a es igual a b pero b y c son diferentes')
else:
    print('a y b son diferentes')