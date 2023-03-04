class Curso:                                #En esta linea de codigo se define la clase Curso
    def __init__(self,titulo):              #En esta linea de codigo se inicializa el constructor de la clase
        self.__titulo=titulo                #Aqui se define el objeto que almacenara la clase

    def getTitulo(self):                    #En esta linea se define el get el cual accede a la clase y al objeto que se almacena en ella
        return self.__titulo                #Devuelve el valor que se almacena en el objeto

class Aprendiz:                             #Se defefine otra clase llamada Aprendiz
    def __init__(self,nombre):              #En esta linea se define y inicializa el constructor de la clase Aprendiz
        self.__nombre=nombre                #Aqui se define el objeto
        self.__cursos=[]                    #Aqui se define otro objeo para que se almacene en una lista

    def agregarCurso(self,nombreCursito):   #Se define un metodo llamado agregarCurso el cual almacena los cursos a los que se  inscribira
        cursito=Curso(nombreCursito)        #se define el valor del objeto
        self.__cursos.append(cursito)       #cada cursito que se inscriba sera añadido al objeto cursitos

    def getCursos(self):                    #Se define el get el cual accedera al objeto de la clase 
        return self.__cursos                #Retornara el valor de el objeto cursito
    
ap=Aprendiz('Sofia')                        #En esta linea se le asigna valor a la clase aprendiz el cual sera "Sofía"
ap.agregarCurso('Python Basico')            #En esta  linea de codigo usara uno de los metodos definidos en los objetos y agregara los cursos "python basico"
ap.agregarCurso('Python Intermedio')        #En esta linea de codigo usara el metodo agragar curso y adicionara python intermedio, estos seran asigandos al objeto Sofia, en caso de que este sea borrado se eliminaran tambien los cursos con el

for c in ap.getCursos():                    #Usara un for para acceder a los valores del objeto mostrando los 2 que se añadieron anteriormente
    print(c.getTitulo())                    #imprimira el titulo de los cursos que se añadieron

