print("Digita il numero delle temperature: ", end='', flush=True)
ntemp = int(input())
print("Inserisci una temperatura °C: ", end='', flush=True)
temp = float(input())
min = temp
max = temp
while ntemp > 1:
    print("Inserisci una temperatura °C: ", end='', flush=True)
    temp = float(input())
    if min > temp:
        min = temp
    else:
        if max < temp:
            max = temp
    ntemp = ntemp - 1
print("La temperatura minima risulta temp = ", min, "°C")
print("La temperatura massima risulta temp = " + str(max) + " °C")
