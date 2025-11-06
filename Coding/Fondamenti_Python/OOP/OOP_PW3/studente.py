from persona import Persona

class Studente(Persona):
    def setIndStudio(self,ind_studio):
        self.ind_studio = ind_studio
    
    def getPagBenvenutoStud(self):
        self.saluto_persona = self.get_pag_benvenuto()
        return self.saluto_persona + ", e frequento " + self.ind_studio
    
    def getNomeStud(self):        
        return self._getNome()
    
    def getCognomeStud(self):        
        return self._getCognome()
        
    def getEtaStud(self):        
        return self._getEta()
    
    def getInteressiStud(self):        
        return self._getInteressi()

    '''
    Questi metodi non funzionano più poiché tentano di accedere a variabili
    "private" della classe "Persona"
    
    def getNomeStud(self):        
        return self.nome
    
    def getCognomeStud(self):        
        return self.cognome
        
    def getEtaStud(self):        
        return self.eta
    '''
    
