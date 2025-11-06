from studente import Studente

nome = "Mario"
cognome = "Rossi"
eta = "18"
interessi = "Ciclismo"

Studente1 = Studente(nome,cognome,eta,interessi)
Studente1.setIndStudio("Sitemi Informativi Aziendali")
print("Nome, Cognome e Età dello STUDENTE_1:")
print("Nome: " + Studente1.getNomeStud() + " " + Studente1.getCognomeStud() + 
      " - Età: " + Studente1.getEtaStud() + " anni")
print()


