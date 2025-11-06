from persona import Persona
from studente import Studente

Persona1 = Persona("Luca", "Rossi", 40, "lettura")
Studente1 = Studente("Giulia", "Bianchi", 22, "musica", "Ingegneria Informatica")
Studente2 = Studente(ind_studio="Matematica")

print(Persona1.get_pag_benvenuto())
print(Studente1.get_pag_benvenuto())   # chiamerà la versione ridefinita (IF)
print(Studente2.get_pag_benvenuto())   # chiamerà la versione ridefinita (ELSE)
