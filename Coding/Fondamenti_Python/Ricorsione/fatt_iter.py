# Fattoriale con approccio iterativo
def fattoriale_iter(n):
    risultato = 1
    for i in range(1, n + 1):
        #risultato *= i   # questo è equivalente alla riga 6
        risultato = risultato * i
    return risultato

# MAIN
print("è:",fattoriale_iter(int(input("Fattoriale di: "))))