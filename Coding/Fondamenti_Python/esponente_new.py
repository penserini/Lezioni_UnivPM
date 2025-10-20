def exp(base, esp): # definizione di una 'funzione'
    potenza = 1
    for i in range(esp, 0, -1):
        potenza = potenza * base
    
    return potenza

# Main
print("Inserisci base: ", end='', flush=True)
base = float(input())
print("Inserisci l'esponente: ", end='', flush=True)
esp = int(input())
if esp >= 0:
    potenza = exp(base, esp) # richiama/esegue la funzione 'exp(..,..)'
    print("L'elevamento a potenza risulta: " + str(potenza))
