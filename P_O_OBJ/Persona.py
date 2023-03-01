class Persona:   #en esta linea de codigo se crea la primera clase llamada "persona"
    def __init__(self,nombre): #las clases tambien deben definirse, se inicializa el constructor y añadimos el "self" para referirnos a esta clase 
        self.__nombre=nombre    #usamos el "self" para referirnos a esta clase y decimos que la clase persona tiene un atributo llamado nombre
        print('') # Esta linea de codigo imprime la cadena para demostar que se a inicializado el constructor

    def getNombre(self): #en esta lina de codigo definimos el getter el cual nos  permitira acceder al atributo en esta clase
        return self.__nombre #en esata linea nos retornara el atributo nombre de esta clase
    
    def setNombre(self, nombre):  # en esta linea de codigo se define el fijador o modificador del atrivuto en esa clase
        self.__nombre=nombre   # en esta linea  se fijara el valor en esta clase y con los caracteres especiales "__" le daremos caracteristica de dato privado

    def metodo(self):   #en esta linea de codigo definiremos el metodo self que como vimos anteriormente nos ayuda a referirnos a la clase que estamos trabajando
        print('Soy un método') # Esta linea de  codigo solo imprimira la cadena de texto para hacernos caer en cuenta que "self" es un metodo de las clases

#ob=Persona('Ana')   # aqui asignaremos "persona" como objeto co el atributo"Ana"
#print(ob.getNombre())  # en esta linea imprimira el objeto al cual se accede con el metodo "get"
#ob.setNombre('Maria')   #esta linea se modificara el valor existente de la clase a "Maria" con el metodo "set"
#print(ob.getNombre())  # esta linea de codigo imprimira el nuevo valor accediendo a la clase con el metodo "get"
#ob.metodo()
#print(type(ob))

class Documento(Persona):                            #se crea una clase hija "se identifica que pertenece a la clase padre por el (persona)" 
    def __init__(self,nombre,ficha):                #se inicia el constructor de la clase hija 
        Persona.__init__(self,nombre)               #se llama el constructor de la clase padre  
        self.__ficha=ficha                          #se crea una nuevo atributo el cual pertenece a la clase hija "aprendiz"

    def getDoc(self):                             #Esta función sirve para poder visualizar el "atributo" nombre de la clase  hija "aprendiz"
        return self.__ficha                         #devuelve lo que tiene guardado en atributo nombre

app=Documento('Pedro',1234009415)
print('Documento: ')                              #un objeto al cual se le da una clase , como por ejemplo "aprendiz"
print(app.getDoc())
print('Nombre: ')                              #imprime lo que tiene guardado el "atributo" "ficha"
print(app.getNombre())                             #imprime lo que tiene guardado el "atributo" "nombre de la clase padre"