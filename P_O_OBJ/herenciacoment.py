class Vehiculo:                                                     # se crea la clase vehiculo 
    def __init__(self,tipo):                                        # se crea el contructor "tambien se utiliza el self para decir q pertenece a esa clase"
        self.tipo=tipo  # se crea el contructor "tambien            # se crea un nuevo atributo
    def descripcion(self):                                          # se crea un metodo el cual se llama "descripcion", "self"para identificar que pertenece a la clase vehiculo
        print('Soy generico no tengo descripcion',self.tipo)        # se imprime un mensaje con el atributo
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                              # se utiliza el get para poder ver q tiene guardado el atributo "tipo"
        return self.tipo                                            # devuelve lo q hay guardado en el atributo
        #return Vehiculo.tipo
    def __str__(self):                                              # el "__str__" sirve para poder saber a q clase pertenece , dependiendo de la posición 
        return 'Soy objeto de la clase Vehiculo'                    # devuelve un mensaje " el q quiera" o tambien se puede el q ya esta por definido en python

class Herramienta:                                                  # se crea la clase herramienta
    def __init__(self,proposito):                                   # se crea el constructor de la clase herramienta "con el self para poder decir a q clase pertenece"
        self.__proposito=proposito                                  # se crea el atributo para la clase herramienta
    def getProposito(self):                                         # se crea el get para poder visualizar lo que tiene guardado en el atributo 
        return self.__proposito                                     # devuelve lo q tiene guardado el atributo 
    def __str__(self):                                              # lo mismo q en la parte de arriba se utiliza "el STR para poder saber donde pertenece el obj"
        return 'Soy objeto de la clase Herramienta'                 # mensaje  para saber donde es el objeto
class Terrestre(Vehiculo,Herramienta):                              # una sub clase la cual tiene herencia de las dos MEGA clases " vehiculo y herramienta"    
    def __init__(self,tipo,proposito):                              # el constructor de esta nueva sub clase 
        Herramienta.__init__(self,proposito)                        # se inicializa el constructor del las MEGA-clases 
        Vehiculo.__init__(self,tipo)                                # se inicializa el constructor del las MEGA-clases
    def datos(self):                                                # un nuevo metodo  llamado "datos "
        print('Tipo: ',super().getTipo())                           # el super es para saber que pertenece a una MEGA clase
        print('Tipo: ',super().getProposito())                      # el super sirve tipo como motor de busqueda el cual entrara alas super clases y buscara lo requerido
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")                                   # se crea un objeto y se le da a una clase 
t.datos()                                                          # se utiliza el metodo datos con el objeto
print(t.__str__())                                                 # imprime donde esta el objeto 
