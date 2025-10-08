# Dichiarazione delle variabili
numero1 = int(input("Inserisci il primo numero intero: "))
numero2 = int(input("Inserisci il secondo numero intero: "))

# Determinazione del maggiore
if numero1 > numero2:
    print("Il numero maggiore è:", numero1)
elif numero2 > numero1:
    print("Il numero maggiore è:", numero2)
else:
    print("I due numeri sono uguali.")
