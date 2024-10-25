# A1_Minimum.py

# Definition und Initialisierung der Variablen
zahl1 = 0
zahl2 = 0
zahl3 = 0
minimum = 0

# Einlesen der drei Kommazahlen
zahl1 = float(input("Geben Sie die erste Zahl ein: "))
zahl2 = float(input("Geben Sie die zweite Zahl ein: "))
zahl3 = float(input("Geben Sie die dritte Zahl ein: "))

# Bestimmen der kleinsten Zahl
if zahl1 < zahl2 and zahl1 < zahl3:
    minimum = zahl1

elif zahl2 < zahl3:
    minimum = zahl2
    
else:
    minimum = zahl3

# Ausgabe der kleinsten Zahl
print("Die kleinste Zahl ist:", minimum)