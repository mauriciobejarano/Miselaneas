"""en este ejemplo como podemos consultar las llaves que tenemos en el diccinario ya sea para mostar
incluir o borrar un elemento"""
inventario = {'manzanas':439,'bananas': 700,
              'peras': 643, 'naranjas': 525  }

print(inventario)

del inventario['peras']
print(inventario)

inventario['bananas'] = 655
print(inventario)

len(inventario)



print(inventario.keys())
print(inventario.values())
print(inventario.items())