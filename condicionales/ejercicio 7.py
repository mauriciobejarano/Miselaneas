horas = int(input('Ingresa las horas trabajadas: '))
if horas > 40:
    extras = horas - 40
    pago = (40+16) + (extras+20)
else:
    pago = horas * 16
print('El pago semanal por', horas, 'horas es $', pago)