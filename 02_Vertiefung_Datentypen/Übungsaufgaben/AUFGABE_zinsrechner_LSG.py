""" 
Aufgabe: Zinsrechner
====================

- Ziel der Aufgabe ist die Entwicklung eines Zinsrechners.
- Der Zinsrechner soll nach folgender Formel funktionieren:

    Endkapital = Startkapital * Rendite^Laufzeit
    
- Die Laufzeit wird in Jahren angegeben und beschränkt sich auf ganze Zahlen.

AUFGABENSTELLUNG:
=================
Schreiben Sie ein Python-Skript, das die Werte für das Startkapital, die Rendite (in Prozent)
und die Laufzeit in Jahren von der Konsole einliest und in Variablen speichert.

Verwenden Sie zur Kontrolle für die Berechnung des Endkapitals die folgenden Werte:
    - Startkapital in €: 100€
    - Rendite in %: 10%
    - Laufzeit: 7 Jahre
Das Endkapital beträgt mit diesen Werten 194.87 €.

Geben Sie das Endkapital in folgender Form auf der Konsole aus:
"Ihr Endkapital beträgt 194.87€."

TIPP:
    Für die Berechnung mit der Formel muss die Rendite in Prozent auf 100% bzw. 1 addiert werden,
    also z.B. 1.1 für eine Rendite von 10%.

Zeit: 20 Minuten, Einzelarbeit oder Partnerarbeit
"""

startkapital = float(input("Bitte Geben Sie Ihr Startkapital ein: "))
rendite_prozent = float(input("Bitte Geben Sie Ihre Rendite in % an: "))
laufzeit = int(input("Bitte Geben Sie Ihre Laufzeit in Jahren an: "))

endkapital = startkapital * (1+rendite_prozent/100)**laufzeit
print("Ihr Endkapital beträgt "  + str(endkapital) + " €")