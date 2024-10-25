'''
Aufgabe: Verflixte Sieben
=========================  

Ein altbekanntes Spiel, genannt Verflixte Sieben, bringt jede
noch so langweilige Party wieder in Schwung. Es funktioniert wie folgt:
Alle Gäste sitzen an einem Tisch und müssen der Reihe nach die natürlichen Zahlen
von Anfang an aufsagen, also jeder eine Zahl, 1, 2, 3 usw. Das ist natürlich zu einfach, 
also sind zur Erschwernis des Spiels folgende Zahlen nicht erlaubt:

- Alle Vielfachen von 7.
- Alle Zahlen, die als letzte Ziffer eine 7 enthalten.

An ihrer Stelle muss der Gast mit Piep antworten. Ist man bei 100 angelangt, ist das Spiel zu Ende.

Arbeitsauftrag:

- Schreiben Sie ein Python-Skript, das die ersten 100 Zahlen oder Piep nacheinander auf der Konsole ausgibt.
- Nutzen Sie eine geeignete Schleifenstruktur.

Zeit: 15 Minuten.
'''

for x in range(1, 101):
    if x % 7 == 0 or x % 10 == 7:
        print("Piep!")
    else:
        print(x)


