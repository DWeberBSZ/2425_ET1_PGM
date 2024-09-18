""" 
Aufgabe: BMI berechnen
=======================

- Ziel der Aufgabe ist die Berechnung Ihres BMIs (Body Maß Index).
- Der BMI berechnet sich mit folgender Formel: BMI = Gewicht(kg) / Größe(m)^2

a) Berechnen Sie den BMI mit festen Werten für das Gewicht und die Größe im Programmcode.
b) Berechnen Sie den BMI mithilfe von Variablen für das Gewicht und die Größe.

- Geben Sie das Ergebnis des BMIs auf der Konsole in folgender Form aus:

"Ihr BMI ist: 24.5"

Zusatzaufgabe: 
==============
- Berechnen Sie den BMI, indem Sie die Werte Gewicht und Größe von der Konsole einlesen und in zwei Variablen speichern.
- Sie werden hierbei vermutlich auf einen Fehler stoßen, recherchieren Sie im Internet nach einer Lösung.

Zeit: 20 Minuten, Einzelarbeit oder Partnerarbeit
"""

# Teilaufgabe a)
bmi = 80 / 1.8**2
print("Ihr BMI ist: " + str(bmi))

# Teilaufgabe b)
gewicht_kg = 80
groesse_m = 1.8
bmi = gewicht_kg / groesse_m**2
print("Ihr BMI ist: " + str(bmi))

# Zusatzaufgabe:
gewicht_kg = input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: ")
groesse_m = input("Bitte geben Sie Ihre Größe in Metern ein: ")
bmi = float(gewicht_kg) / float(groesse_m)**2 # Datentypkonvertierung nach float (Kommazahl)
print("Ihr BMI ist: " + str(bmi)) # Datentypkonvertierung nach string (Zeichenkette)