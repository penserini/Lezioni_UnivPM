class Persona:
    def __init__(self, nome="", cognome="", eta=None, interessi=None):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__interessi = interessi
        self.saluto = f"Buongiorno, sono {nome} {cognome}"

    def get_pag_benvenuto(self):
        return self.saluto
     
    def getNome(self):
        return self.__nome
    
    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta
    
    def getInteressi(self):
        return self.__interessi
