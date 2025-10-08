n = int(input("Specifica il numero degli elementi di INPUT: "))
i = 1
while(i < n+1):
    print("Inserisci il ", i, "° elemento: ", end='', flush=True)
    nReale = float(input(""))
    nReale = nReale **2
    print("Quadrato del ", i, "° numero inserito è: ", nReale)
    i = i + 1
    