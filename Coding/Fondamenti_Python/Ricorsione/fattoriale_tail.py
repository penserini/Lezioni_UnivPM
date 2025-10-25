# Fattoriale con ricorsione in coda
def fattoriale_tail(n, acc=1):
    if n == 0:
        return acc
    return fattoriale_tail(n - 1, acc * n)

#Main
print("è:",fattoriale_tail(int(input("Fattoriale di: "))))