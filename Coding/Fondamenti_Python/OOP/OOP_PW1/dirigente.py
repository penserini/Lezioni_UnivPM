from persona import Persona

class Dirigente(Persona):
    def setScuola(self,scuola):
        self.scuola = scuola
    
    def getPagBenvenutoDir(self):
        self.saluto_persona = self.get_pag_benvenuto()
        return self.saluto_persona + ", e dirigo la scuola " + self.scuola
    