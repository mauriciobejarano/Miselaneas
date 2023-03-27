class Organizacion:                                                # se creara la clase organización 
    def __init__(self, Name, Website, Country, Industry, funded):  #definiremos los parametros de la clase 
        self.__Name = Name                                         #le asiganaremos los valores a cada uno de los parametros
        self.__Website = Website                                   #le asiganaremos los valores a cada uno de los parametros
        self.__Country = Country                                   #le asiganaremos los valores a cada uno de los parametros
        self.__Industry = Industry                                 #le asiganaremos los valores a cada uno de los parametros
        self.__funded = funded                                     #le asiganaremos los valores a cada uno de los parametros
        
    def nombreySitio(self):                                        #definiremos una funcion para que nos devuelva los datos requeridos de el archivo CVS en este caso queremos que nos devuelva el nombre de la empresa y su sitio web
        return self.__Name+' '+self.__Website 