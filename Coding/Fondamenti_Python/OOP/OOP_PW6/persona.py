from functools import singledispatchmethod

class Persona:
    # wrapper "pubblico": accetta anche nessun argomento
    def saluta(self, arg=None):
        return self._saluta(arg)   # passa SEMPRE un argomento al dispatcher

    # dispatcher "privato"
    @singledispatchmethod
    def _saluta(self, arg):
        print("Ciao, piacere di conoscerti!")  # fallback
    
    # Sono metodi che iniziano con "_" e non con un nome per indicare
    # che non vengono chiamati direttamente.
    @_saluta.register(type(None))
    def _(self, _):
        print("Ciao, piacere di conoscerti!")

    @_saluta.register(str)
    def _(self, nome):
        print(f"Ciao {nome}, benvenuto!")

    @_saluta.register(int)
    def _(self, eta):
        print(f"Hai {eta} anni? Piacere di conoscerti!")