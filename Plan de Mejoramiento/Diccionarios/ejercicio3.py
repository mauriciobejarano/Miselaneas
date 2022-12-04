"""En el siguiente ejemplo veremos com o se puede eliminar una 
referencia de un diccionario y cambiamos su valor"""
inventario = {'manzanas':439,'bananas': 700,
              'peras': 643, 'naranjas': 525  }

print(inventario)

del inventario['peras']
print(inventario)

inventario['bananas'] = 655
print(inventario)

len(inventario)