from cane import Cane
from gatto import Gatto

# Funzione che accetta "qualunque cosa" con il metodo parla()
def fai_parlare(animale):
    animale.parla()
    
fai_parlare(Gatto())
fai_parlare(Cane())