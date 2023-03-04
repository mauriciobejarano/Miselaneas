class A1:                                 #En esta linea de codigo se crea la clase A1
    def __init__(self):                   #Aqui se inicializa el constructor definiendolo que pertenece a la clase A1
        pass                              #Dejara la clase vacia pero no inexistente
    def saludo(self):                     #define la funcion saludo para esta clase
        print('Hola desde A1')            #Imprimira el valor del objeto de  la clase A1 el cual es saludo y se le a asignado"Hola desde A1"

class A2:                                 #En esta linea de codigo se crea la clase A2
    def __init__(self):                   #Aqui se inicializa el constructor definiendolo que pertenece a la clase A2
        pass                              #Dejara la clase vacia pero no inexistente
    def saludo(self):                     #Definira la funcion saludo en la clase 
        print('Hola desde A2')            #imprimira el valor del objeto saludo de la clase A2 y el valor asignado es "Hola desde A2"


class B(A2,A1):                           #Se crea la subclase B el cual llamara metos de las clase padre A2,A1 
    def __init__(self):                   #imicializara el constructor definido en la clase B
        pass                              #Dejara que la clase este vacia pero no inexistente
    def saludo(self):                     #definira la funcion saludo en esta clase 
        print('Hola desde B')             #imprime el valor que se a asignado al objeto el cual es "Hola dese B"
    def __str__(self):                          #Este metodo permite mostrar la cadena de texto y no la ubicaion del objeto
        return 'Soy un objeto de la clase B'    #rtornara la cadena de texto asignada al objeto el cual sera "soy un objeto de la clase B"
obj=B()                                         #Llamara a la clase b con todos sus funciones
print(obj.__str__())                            #imprimira la funcion __str__ que acepta el tipo de dato cadena y lo devovera en la consola
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())