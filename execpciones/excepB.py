values = (1, 0)       #En esta linea de codigo se le asigna a la variable una tupla la cual se usara como atributo mas adelante
#x,y=19,30
#print(divmod(10,3))
try:
    q, r = divmod(*values)
    #print('q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)