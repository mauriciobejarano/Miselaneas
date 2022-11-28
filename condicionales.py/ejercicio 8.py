def fecha_dia_siguiente(agnio, mes, dia):
    biciesto = False

    if agnio % 400 == 0:
        biciesto = True
    elif agnio% 4 == 0:
        biciesto = True
    
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if biciesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            agnio += 1
        else:
            mes += 1
    
    return (agnio, mes, dia)

print(fecha_dia_siguiente(2022, 10, 23 ))