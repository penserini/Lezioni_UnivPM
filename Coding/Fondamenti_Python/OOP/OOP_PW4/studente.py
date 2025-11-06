from persona import Persona

class Studente(Persona):
    def __init__(self, nome, cognome, eta, interessi, ind_studio):
        super().__init__(nome, cognome, eta, interessi)
        self.ind_studio = ind_studio

    # OVERRIDING: ridefinizione del metodo del genitore
    def get_pag_benvenuto(self):
        # richiama comunque il metodo del genitore (opzionale)
        saluto_base = super().get_pag_benvenuto()
        return f"{saluto_base}, e frequento {self.ind_studio}"
    