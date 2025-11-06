from persona import Persona

p = Persona()
p.saluta()         # funziona: wrapper passa None al dispatcher
p.saluta("Luca")   # str
p.saluta(30)       # int