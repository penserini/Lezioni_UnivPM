# Fattoriale con ricorsione semplice
def fattoriale_ric(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale_ric(n - 1)
    
#Main
print("è:",fattoriale_ric(int(input("Fattoriale di: "))))   