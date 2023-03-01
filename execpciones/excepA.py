try:
    #print(1/1))
    raise SyntaxError
except SyntaxError as e:
    print(e)
    print('Cierra el parentesis')
    
try:
    #raise ZeroDivisionError
    print(1/0)
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:
    print(zde)
    #print('prueba error')
