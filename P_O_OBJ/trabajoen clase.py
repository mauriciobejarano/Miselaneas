class empleado:
    def __init__(self,nombre,cargo,salario):
        self._nombre = nombre
        self._cargo = cargo
        self._salario = salario
        
    def getNombre(self):
        return self._nombre
    def setNombre(self):
        return self._cargo
    
    def getCargo(self):
        return self._cargo
    def setCargo(self):
        return self._cargo
    
    def getSalario(self):
        return self._salario
    def setSalario(self):
        return self._salario
    
    def calSalarioIPC(self,salario):
        if salario>116000 and salario<0:
            salario_ipc = (salario*0.133)+salario
            return salario_ipc
        else:
            salario_ipc = (salario*163)+salario
            return salario_ipc
    
    def calSalarioHE(self,salario,HE):
        if HE>11 and HE>0 and salario>0:
            salarioHE = (HE*6642)+salario
            return salarioHE
        else:
            print('Aqui no se permite que trabajes mas de 10hrs')        
            
    
emp1=empleado('mauricio','operador',160000)
print(emp1.calSalarioIPC(160000))
print(emp1.calSalarioHE(6,160000))