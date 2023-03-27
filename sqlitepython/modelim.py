def modificar(conexion, tabla, campo, dato, id):
    micursor = conexion.cursor()
    sentencia = f"UPDATE {tabla} SET {campo} = '{dato}' WHERE {id} = '{id}'"
    micursor.execute(sentencia)
    com.commit()
    print('Modificación exitosa !!!')
    
def eliminar(conexion, tabla, campo, dato):
    micursor = conexion.cursor()
    sentencia = f"DELETE FROM {tabla} WHERE {campo} = '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación exitosa !!!')