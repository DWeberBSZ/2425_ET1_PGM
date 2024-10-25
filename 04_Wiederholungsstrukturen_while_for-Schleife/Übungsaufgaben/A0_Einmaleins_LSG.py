"""
Aufgabe: Einmaleins
=================== 

a) Schreiben Sie ein Python-Skript, welches mithilfe einer while-Schleife
   das Einmaleins der Zahlen von 1 bis 20 berechnet und nacheinander auf
   der Konsole ausgibt.

b) Verwenden Sie anstatt einer while-Schleife eine gleichwertige for-Schleife
   mit der range-Funktion.

HINWEIS: Berechnen Sie ausschließlich die POTENZGRÖßEN 1*1, 2*2, 3*3, ... bis 20.

Zeit: 20 Minuten, Einzelarbeit.
"""

zahl = 1
einmaleins = 0

# a) Mit while-Schleife
while zahl <= 20:
    einmaleins = zahl**2
    print(f"Einmaleins: {einmaleins}")
    zahl += 1
