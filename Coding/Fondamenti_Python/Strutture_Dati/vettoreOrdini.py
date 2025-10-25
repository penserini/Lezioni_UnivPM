'''
Calcola lo sconto sull'ordine di un prodotto in base alle quantità ordinate:
10 < Q <= 20 applica il 5% di sconto
Q > 20       applica il 10% di sconto
1 <= Q <= 10 il prezzo rimane PU*Q senza sconto

USEREMO COME SINONIMI 'LISTA' e 'VETTORE'
'''
def calcolapVett(qVett, pVett, pu):
    for i in range(0, len(pVett), 1):
        if qVett[i] > 10 and qVett[i] <= 20:
            pVett[i] = qVett[i] * pu * 0.95
        else:
            if qVett[i] > 20:
                pVett[i] = qVett[i] * pu * 0.9
            else:
                pVett[i] = qVett[i] * pu

def caricaqVett(qVett):
    print("")
    print("QUANTITA' ORDINATE")
    for i in range(0, len(qVett), 1):
        print("Inserisci quantità per ordine n° " + str(i + 1) + ": ", end='', flush=True)
        qVett[i] = int(input())

def stampapVett(pVett):
    print("")
    print("CALCOLO PREZZI DEGLI ORDINI INCLUSIVI DI EVENTUALI TIPOLOGIE DI SCONTO")
    for i in range(0, len(pVett), 1):
        print("Prezzo ordine n° " + str(i + 1) + ": " + str(pVett[i]) + " €")

# Main
print("Specifica il numero di ordini per un articolo: ", end='', flush=True)
ordini = int(input())
print("Inserisci il prezzo-unitario (€): ", end='', flush=True)
pu = float(input())
qVett = [0] * (ordini) # produce una lista = [0,0,...,0] di lunghezza pari a 'ordini'
pVett = [0] * (ordini) # produce una lista = [0,0,...,0] di lunghezza pari a 'ordini'

caricaqVett(qVett)
calcolapVett(qVett, pVett, pu)
stampapVett(pVett)
