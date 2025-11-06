from veicolo import Veicolo

class Auto(Veicolo):
    def avvia(self):
        print("Accendo il motore dell’auto")

    def ferma(self):
        print("Spengo il motore dell’auto")

class Bicicletta(Veicolo):
    def avvia(self):
        print("Inizio a pedalare")

    def ferma(self):
        print("Smetto di pedalare")
