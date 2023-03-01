def try_syntax(numerator, denominator): # en esta linea se define su propio error 
    try:  #bloque try donde se generara el error
        print(f'In the try block: {numerator}/{denominator}') #imprime la operacion a ejecutarse
        result = numerator / denominator  # realiza la operacion anteriormente expuesta
    except ZeroDivisionError as zde:  ## en esta linea de codigo es ponen los errores que pueden ser suceptibles a currir en el bloque try y cambia el nombre a zde
        print(zde)
    else:   # genera un escape en caso de que no se cumpla el except anterior
        print('The result is:', result) # imprime el resultado de la operacion anterior
        return result
    finally:  #en esta linea imprime donde finalisa el bloque try, se ejecuta primero que else
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0))