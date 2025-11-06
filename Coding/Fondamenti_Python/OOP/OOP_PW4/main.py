from persona import Persona
from studente import Studente

Persona1 = Persona("Luca", "Rossi", 40, "lettura")
Studente1 = Studente("Giulia", "Bianchi", 22, "musica", "Ingegneria Informatica")

print(Persona1.get_pag_benvenuto())
print(Studente1.get_pag_benvenuto())   # chiamerà la versione ridefinita
