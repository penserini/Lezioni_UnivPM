def somma(n):
    if n == 1:
        return 1
    
    return somma(n-1) + n

# MAIN
print("Inserisci un numero intero: ", end = '', flush = True)
nIniz = int(input(""))
risp = somma(nIniz)
print("")
print("la somma dei primi",nIniz,"numeri interi è:", risp)


