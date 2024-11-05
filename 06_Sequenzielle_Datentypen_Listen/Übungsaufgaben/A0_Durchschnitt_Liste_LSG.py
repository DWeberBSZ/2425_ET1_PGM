'''
Übungsaufgabe: Durchschnitt einer Liste
========================================

Arbeitsauftrag:
    - Berechnen Sie das arithmetische Mittel aller Elemente in folgender Liste: [8, 23, 19, 57, 70, 3]
    - Verzichten Sie zunächst auf die Verwendung der Python sum-Funktion. 
    - Geben Sie das Ergebnis auf der Konsole aus.

ZUSATZAUFGABE: Führen Sie die Berechnung anschließend mit der Python sum-Funktion durch.

Zeit: 15 Minuten, Einzelarbeit
'''
meine_liste = [8, 23, 19, 57, 70, 3]

# Längere Lösung:
summe = 0
anzahl = 0
for x in meine_liste:
    summe = summe + x
    anzahl = anzahl + 1
    
print(summe/anzahl)

# Kurze Lösung:
print(sum(meine_liste) / len(meine_liste))