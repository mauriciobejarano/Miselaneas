class Carrera:
    def __init__(self, nombre, estudiante, descripcion, edad, username, password):
        self.estudiante = estudiante
        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion
        self.username = username
        self.password = password

    def getCarrera(self):
        return self.estudiante, self.nombre, self.edad, self.descripcion, self.username, self.password
    

class Estudiante:
    def __init__(self, nombre, carrera, email, telefono, met_pago ):
        self.nombre = nombre
        self.carrera = carrera
        self.email = email
        self.telefono = telefono
        self.met_pago = met_pago

    def getEstudiante(self):
        return self.nombre, self.carrera, self.email, self.telefono, self.met_pago
    
class Instructor:
    def __init__(self, nombre, disponibilidad, asignatura):
        self.nombre = nombre
        self.disponibilidad = disponibilidad
        self.asignatura = asignatura

    def getInstructor(self):
        return self.nombre, self.disponibilidad, self.asignatura
    
class Asignatura:
    def __init__(self, nombre, descripcion, instructor, horario):
        self.nombre = nombre
        self.descripcion = descripcion
        self.instructor = instructor
        self.horario = horario
    
    def getAsignatura(self):
        return self.nombre, self.descripcion, self.instructor, self.horario
    

class Inscripcion:
    def __init__(self, detalles, requerimientos, fecha):
        self.detalles = detalles
        self.requerimientos = requerimientos
        self.fecha = fecha

    def getinscripcion(self):
        return self.detalles, self.requerimientos, self.fecha


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
    
class Transacciones:
    def __init__(self, detalle, fecha):
        self.detalle = detalle
        self.fecha = fecha

    def getTransacciones(self):
        return self.detalle, self.fecha
    