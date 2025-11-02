from persona import Persona

class Studente(Persona):
    def setIndStudio(self,ind_studio):
        self.ind_studio = ind_studio
    
    def getPagBenvenutoStud(self):
        self.saluto_persona = self.get_pag_benvenuto()
        return self.saluto_persona + ", e frequento " + self.ind_studio
