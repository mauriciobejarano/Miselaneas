class Vehiculo:                                # En esta linea de codigo se crea la clase padre Vehiculo
    def __init__(self,placa,conductor):        # Se inicializa el constructor de la clase coon los atributos (placa y conductor)
        self.__placa=placa                     # Se asigana el valor que le demos al atributo (placa)
        self.__conductor=conductor             # Se asigna el valor que le demos al atributo (conductor)
    def getConductor(self):                    # Se crea el get en la clase vehiculo el cual tendra que devolver el valor de conductor
        return self.__conductor                # Devolvera el valor que se haya almacenado en el atributo conductor
    def getPlaca(self):                        # Se crea el get en la clase placa el cual tendra que devolver el valor de placa
        return self.__placa                    # Retornara el valor que se haya almacenado en el atributo placa 