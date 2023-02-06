"""El usuario ingresara una divisa si se encuentra en el diccionario mostrara el simbolo de la moneda
de lo contrario le indicara que no se encuentra"""

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥', 'Libra':'£', 'Rupia':'₹', 'Rublo':'₽'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))