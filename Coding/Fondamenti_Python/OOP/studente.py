from persona import Persona

class Studente(Persona):
    # Simulazione di OVERLOADING del costruttore
    def __init__(self, nome="", cognome="", eta=None, interessi=None, ind_studio=None):
        # costruttore “flessibile”: accetta diversi tipi di input
        if nome and cognome and eta and interessi:
            super().__init__(nome, cognome, eta, interessi)
        else:
            super().__init__("Sconosciuto", "", 0, "nessuno")
        self.ind_studio = ind_studio or "corso non specificato"

    def get_pag_benvenuto(self):
        return f"Buongiorno, sono {self.getNome()} {self.getCognome()}, e frequento {self.ind_studio}"
    