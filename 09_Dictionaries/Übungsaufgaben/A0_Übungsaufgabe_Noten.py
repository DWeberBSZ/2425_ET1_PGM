'''
Übungsaufgabe: Durchschnittspunktzahl mit Dictionary berechnen.
================================================================

Gegeben ist ein Dictionary mit Schülern und den jeweiligen 
Punktzahlen ihrer Prüfungen.

Schreiben Sie ein Programm, das die Durchschnittspunktzahl 
für jeden Schüler berechnet und in einem neuen Dictionary abspeichert.

Geben Sie anschließend für jeden Schüler den Namen und die zugehörige 
Durchschnittspunktzahl auf der Konsole aus.

HINWEIS: Greifen Sie für die Berechnung des Durchschnitts auf die
Funktionen sum() und len() zurück.
'''

# Das Dictionary mit Schülern und ihren Noten
# Eingabe
noten = {
    'Max': [85, 90, 92],
    'Anna': [78, 85, 80],
    'Tom': [90, 88, 94],
    'Lisa': [82, 75, 88]
}

durchschnitt = dict()

# Verarbeitung
for key, value in noten.items(): # items liefert Schlüssel + Wert
    # z.B. für den ersten Durchlauf: 
    # key = 'Max', 
    # value = [85, 90, 92]
    durchschnitt[key] = sum(value) / len(value)
    #print(f"{key}:{durchschnitt[key]}")


# Ausgabe
for key in durchschnitt:
    print(f"{key}:{durchschnitt[key]}")