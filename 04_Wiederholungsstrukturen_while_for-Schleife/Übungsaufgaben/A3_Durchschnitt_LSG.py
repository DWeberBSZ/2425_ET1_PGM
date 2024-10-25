"""
Aufgabe: Durchschnitt ganzer Zahlen
====================================

- Erstellen Sie ein Python-Skript, das mithilfe einer for-Schleife den Durchschnitt aller 
ganzen Zahlen von 1 bis 30 (inklusiv) bestimmt.

- Verwenden Sie hierfür die range-Funktion mit geeigneten Grenzen.


Zeit: 10 Minuten, Einzelarbeit
"""
sum = 0
anzahl = 30

# 1. Schritt: Summe berechnen
for i in range(anzahl):
    sum += (i+1)

# 2. Schritt: Durchschnitt berechnen
average = sum / anzahl

print(f"Der Durchschnitt ist: {average}")