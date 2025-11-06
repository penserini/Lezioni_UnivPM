from abc import ABC, abstractmethod

# Classe astratta = interfaccia
class Veicolo(ABC):
    
    @abstractmethod
    def avvia(self):
        pass

    @abstractmethod
    def ferma(self):
        pass
    