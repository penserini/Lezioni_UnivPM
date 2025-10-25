# Calcola la somma dei primi N numeri interi, fornito N in input
def somma_tail(n, acc=0):
    if n == 0:
        return acc  # caso base: restituisce direttamente l’accumulatore
    return somma_tail(n - 1, acc + n)  # chiamata ricorsiva in coda

# MAIN
print("Inserisci un numero intero: ", end='', flush=True)
n=int(input())
print("",n) # serve solamente a visualizzare il numero inserito 
            # (poiché non c'è un terminale in Jupyter)
print("La somma dei primi ",n," numeri è: ",somma_tail(n))