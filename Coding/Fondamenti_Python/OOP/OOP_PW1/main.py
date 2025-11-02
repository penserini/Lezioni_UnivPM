from persona import Persona
from studente import Studente
from dirigente import Dirigente

nome = "Loris"
cognome = "Penserini"
eta = "50"
interessi = "Droni"

Persona1 = Persona(nome,cognome,eta,interessi)
print("\033c", end="") # ripulisce il terminale
print("SALUTO DI PERSONA_1:")
print(Persona1.get_pag_benvenuto())
print()

nome = "Mario"
cognome = "Rossi"
eta = "55"
interessi = "Ciclismo"

Studente1 = Studente(nome,cognome,eta,interessi)
Studente1.setIndStudio("Sitemi Informativi Aziendali")
print("SALUTO DI STUDENTE_1:")
print(Studente1.getPagBenvenutoStud())
print()

nome = "Giovanna"
cognome = "Rossini"
eta = "35"
interessi = "Aerobica"

Dirigente1 = Dirigente(nome,cognome,eta,interessi)
Dirigente1.setScuola("IIS POLO3 FANO")
print("SALUTO DI DIRIGENTE_1:")
print(Dirigente1.getPagBenvenutoDir())
