class Organizacion:
    def __init__(self, Name, Website, Country, Industry, funded):
        self.__Name = Name
        self.__Website = Website
        self.__Country = Country
        self.__Industry = Industry
        self.__funded = funded
        
    def nombreySitio(self):
        return self.__Name+' '+self.__Website 