class Persona(object):
    # Costruttore: viene chiamato quando si crea un nuovo oggetto
    def __init__(self, nome, cognome, eta, interessi):
        # Attributi dell'oggetto (proprietà)
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__interessi = interessi
        self.saluto = f"Buongiorno, sono {nome} {cognome}"

    # Metodo che restituisce la frase di saluto
    def get_pag_benvenuto(self):
        self.saluto = f"Buongiorno, sono {self.__nome} {self.__cognome}"
        return self.saluto

    def _getNome(self):        
        return self.__nome
    
    def _getCognome(self):        
        return self.__cognome
    
    def _getEta(self):        
        return self.__eta
    
    def _getInteressi(self):        
        return self.__interessi
