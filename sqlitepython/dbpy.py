import sqlite3                                                #En esta linea de codigo se importa el modulo que hara conexion con la base de datos
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')         
con=sqlite3.connect('sqlitepython/conpython.db')              #En esta linea  se crea una variable la cual se encargara de hacer conexion con la carpeta donde se encuentra el archivo
print(type(con))                                              #Esta linea imprimira que tip de dato es el archivo que se encuentra en la ruta absoluta
micursor=con.cursor()                                         #Crearemos un cursor para poder navegar entre los datos
print(type(micursor))                                         #Imprimira el typo de dato que recorrera el cursor
sentencia="SELECT * from alumno;"                             #Se crea la primera sentencia sql que le dara una orden a la base de datos
micursor.execute(sentencia)                                   #Ejecutara la sentencia que anteriormente hemos creado para que nos muestre los datos solicitaddos
for fila in micursor.fetchall():                              #Se usara un for para iterar el archivo y nos muestre cada uno de los datos en orden y separados
    print(fila[0])                                            # imprimira todos ls valores que haya en la fila 0
    print(fila[1])                                            # imprimira todos ls valores que haya en la fila 1
    print(fila[2])                                            # imprimira todos ls valores que haya en la fila 2
    print(fila[3])                                            # imprimira todos ls valores que haya en la fila 4
    print('-'*50)                                             # de todos los valores que tenemos no  devolvera solo50.


def modificar(conexion, tabla, campo, dato, id):
    micursor = conexion.cursor()
    sentencia = f"UPDATE {tabla} SET {campo} = '{dato}' WHERE {id} = '{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación exitosa !!!')
    
def eliminar(conexion, tabla, campo, dato):
    micursor = conexion.cursor()
    sentencia = f"DELETE FROM {tabla} WHERE {campo} = '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación exitosa !!!')