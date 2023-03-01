try: # bloque de codigo que es posible a generar fallo
   # print(1/1))   # en esta linea se simula el syntax error 
    raise SyntaxError  # en esta linea se simula el syntax error 
except SyntaxError as e: # en esta linea se da escape si se genera sintax error en la linea de arriba, como vimos se ejecutara devido a la simulacion del mismo
    print(e)  
    print('Cierra el parentesis')  #esta linea imprime una salida al error que se ocaciona para que el usurio corrija 
    
try:  # bloque de codigo que es posible a generar fallo
    #raise ZeroDivisionError
    print(1/0) # imprime la operacion a ejecutar
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:  # en esta linea se da escape si se genera sintax error en la linea de arriba, como vimos se ejecutara devido a la simulacion del mismo y cambia el nombre a zde
    print(zde)  # llama el error que se genero
    #print('prueba error')
