print("Inserisci la 'base': ", end='', flush=True)
base = float(input())
print("Inserisci l''esponente': ", end='', flush=True)
esp = int(input())
if esp >= 0:
    potenza = 1
    for i in range(esp, 0, -1): # range: l'estremo inferiore '0' non è incluso
        potenza = potenza * base
    print("L'elevamento a potenza risulta: " + str(potenza))
