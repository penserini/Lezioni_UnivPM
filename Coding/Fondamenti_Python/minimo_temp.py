min = 100
while True:    #This simulates a Do Loop
    print("Inserisci una temperatura °C: ", end='', flush=True)
    temp = float(input())
    if min > temp:
        min = temp
    print("Vuoi inserire un'altra temperatura (S/N)? ", end='', flush=True)
    ris = input()
    if not(ris == "S" or ris == "s"): break   #Exit loop
print("La temperatura minima risulta temp = " + str(min) + " °C")
