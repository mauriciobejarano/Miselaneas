class Aprendiz:                               #Se crea la clase aprendiz 
    
    def __init__(self,nombre):                #se inicializa el contructor de la clase  con los con el objeto nombre
        self.__nombre=nombre                  # se le asigana el valor al objeto nombre
        self.__cursos=[]                      # se crea otro objeto llamado cursos el cual almacenara los valores en una lista

    def agregarCurso(self,titulo):            #se define una funcion e inicializa el constructor del metodo agregar curso
        self.__cursos.append(titulo)          # a todos los cursos que se agregen se añadiran al atrivuto titulo

    def getCursos(self):                      # se crea el metodo get el cual accedera a los valores  de cursos en la clase Aprendiz
        return self.__cursos                  #retornara los valores que encuentre en este objeto

class Curso:                                  #se crea la clase curso
    def __init__(self,titulo):                #se inicializa el constructor en esta clase  con el atributo Titulo
        self.__titulo=titulo                  # se le asigna al objeto Titulo un valor

    def getTitulo(self):                     #se define el metodo get en la clase Curso
        return self.__titulo                 #retornara el valor que encuentre en el objeto titulo
    
a=Aprendiz('Martha')                         #se llama el objeto aprendiz asignado a una variable y el cual tendra el atributo "martha"
c1=Curso('Python Intermedio')                #se llama el objeto aprendiz asignado a una variable y el cual tendra el atributo "python intermedio"
c2=Curso('Python Basico')                    #se llama el objeto aprendiz asignado a una variable y el cual tendra el atributo "python basico"
c3=Curso('Introduccion a Java')              #se llama el objeto aprendiz asignado a una variable y el cual tendra el atributo "Introduccion a Java"  

a.agregarCurso(c1)                           #cada curso se agregara a el objeto agrgarCurso y se asignara al objeto aprendiz"martha"
a.agregarCurso(c2)                           #cada curso se agregara a el objeto agrgarCurso y se asignara al objeto aprendiz"martha"
a.agregarCurso(c3)                           #cada curso se agregara a el objeto agrgarCurso y se asignara al objeto aprendiz"martha"

print(a.getCursos())                         #imprimira los valores o cursos a los cuales se ha incrito el aprendix "martha"


for curso in a.getCursos():                  #usara un for para acceder cada uno de los valores de Cursos
    print(curso.getTitulo())                 #imprimira cada uno de los valores inscritos, imprimiend uno po uno