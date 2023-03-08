class Carrera:                                                      
    def __init__(self,nombre, estudiante, description, edad, username,password):                                        
        self.estudiante = estudiante  
        self.nombre = nombre
        self.description = description
        self.edad = edad
        self.__username = username
        self.__password = password
        idcarrera = idcarrera          
    
    def getCarrera(self):
        return self.estudiante, self.nombre, self.description, self.edad, self.username, self.password                                          

                    

class Estudiante:                                                  
    def __init__(self,nombre, carrera, email, telefono, mpago):                                   
        self.nombre = nombre
        self.carrera = carrera
        self.email = email
        self.telefono = telefono
        self.mpago = mpago
    
    def getEstudiante(self):
        return self.nombre, self.carrera, self.email, self.telefono, self.mpago       
    
class Instructor:
        def __init__(self,nombre, asignatura, disponibilidad):
            self.nombre = nombre
            self.asignatura = asignatura
            self.disponibilidad = disponibilidad
            
        def getInstructor(self):
            return self.nombre, self.asignatura, self.disponibilidad
   
    
class Asignatura:
        def __init__(self,nombre, descripcion, instructor, horario, aula, duracion):
            self.nombre = nombre
            self.descripcion = descripcion
            self.instructor = instructor
            self.horario = horario
            self.aula = aula
            self.duracion = duracion
            
        def getAsignatura(self):
            return self.nombre, self. descripcion, self.instructor, self.horario, self.aula, self.duracion
        
class Inscripcion:
    def __init__(self,detalle, requerimientos, fecha):
        self.detalle = detalle
        self.requerimientos = requerimientos
        self.fecha = fecha
        
    def getInscripcion(self):
        return self.detalle, self.requerimientos, self.fecha
    
    
class Curso:
    def __init__(self, descripcion, fecha, nivel, creditos, asignaturas, semestres):
        self.descripcion = descripcion
        self.fecha = fecha
        self.nivel = nivel
        self.creditos = creditos
        self.asignaturas = asignaturas
        self.semestres = semestres
        
    def getCurso(self):
        return self.descripcion, self.fecha, self.nivel, self.creditos, self.asignaturas, self.semestres
    
class Transaccion:
    def __init__(self, detalle, fecha):
        self.detalle = detalle
        self.fecha = fecha
        
    def getTransaccion(self):
        return self.detalle, self.fecha


est=Estudiante('Andres','Arquitectura', 'andresg12@email.com', 3012568974, 'Debito')
ins=Instructor('Fabian','Fisica', 'Disponible')
print('Estudiante: ')                              
print(est.getnombre())
print('Nombre: ')                              
print(est.getcarrera())                             