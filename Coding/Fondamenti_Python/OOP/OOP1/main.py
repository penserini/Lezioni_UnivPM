from Persona import Persona
from Studente import Studente

nome = "Loris"
cognome = "Penserini"
eta = "50"
interessi = "Droni"

Persona1 = Persona(nome,cognome,eta,interessi)
print("\033c", end="") # ripulisce il terminale
print("SALUTO DI PERSONA_1:")
print(Persona1.get_pag_benvenuto())
print()

Studente1 = Studente(nome,cognome,eta,interessi)
Studente1.setIndStudio("Sitemi Informativi Aziendali")
print("SALUTO DI STUDENTE_1:")
print(Studente1.getPagBenvenutoStud())
