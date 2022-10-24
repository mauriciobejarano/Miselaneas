print('Ingrese una nota entre 0 a 10: ')
num = int(input())
if(num<0 or num>10):
    print('¡¡La nota ingresada no es invalida!!')
else:
    if(num>=0) and (num<=5):
        print('Su nota es insuficiente!!')
    elif(num>=6) and (num<=7):
        print('Su nota es suficiente!!')
    elif(num>=8) and (num<=10):
        print('Su nota es buena!!')
   