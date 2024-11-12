import random                
# Teilaufgabe 1: 
# Definieren Sie eine Liste lotto für die Lottozahlen mit sechs Standardwerten (0)
lotto = [0, 0, 0, 0, 0, 0]


# Teilaufgabe 2 bereits erledigt:
for x in range(0, len(lotto)):
    lotto[x] = random.randint(1, 6)
    
print("Folgende Kombination wurde gezogen: ")
print(lotto)

# Zusatzaufgabe: Anstelle der Zeilen 8 und 9:
#for x, value in enumerate(lotto): # Die Funktion enumerate liefert zwei Informationen: Den Index und den dazugehörigen Wert.
#    lotto[x] = random.randint(1, 6)