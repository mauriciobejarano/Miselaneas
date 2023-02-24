"""Función que calcula el máximo común divisor de dos números.
Parámetros: - n: Es un número entero., - m: Es un número entero.
Devuelve: El máximo común divisor de n y m.
    """

def mcd(n, m):
  
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n


print(mcd(30,72))
