"""Función que calcula el mínimo común múltiplo de dos números.
Parámetros: n Es un número entero y m Es un número entero.
Devuelve: El mínimo común múltiplo de n y m."""

def mcm(n, m):
    
    if n > m:
        mayorque = n
    else:
        mayorque = m
    while (mayorque % n != 0) or (mayorque % m != 0):
        mayorque += 1
    return mayorque

print(mcm(24,36))