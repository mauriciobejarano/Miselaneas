atletas_olimpicos = {}

while True:
    name = input('Ingresa el nombre del atleta: ')
    if name == '':
        break
    
    score = int(input('Ingrese el puntaje del atleta (0 - 10): '))
    if score not in range(0, 11):
        break

    if name in atletas_olimpicos:
        atletas_olimpicos[name] += (score,)
    else:
        atletas_olimpicos[name] = (score,)

for name in sorted(atletas_olimpicos.keys()):
    adding = 0
    counter = 0
    for score in atletas_olimpicos[name]:
        adding += score
        counter += 1
    print('El atleta:',name,'tiene un promedio de:',adding/counter)

print('El promedio mas alto es:'.max(atletas_olimpicos[name]))
print('El promedio mas bajo es:'.min(atletas_olimpicos[name]))