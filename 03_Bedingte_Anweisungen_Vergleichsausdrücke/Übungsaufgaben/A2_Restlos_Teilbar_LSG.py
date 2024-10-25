'''
Aufgabe: Restlos teilbar?
=================================

Arbeitsauftrag:

- Schreiben Sie ein Python-Skript, welches zwei Ganzzahlen von der Konsole einliest
  und überprüft, ob die erste Ganzzahl restlos durch die zweite Ganzzahl teilbar ist.
  
- Geben Sie das Ergebnis als Textinformation auf der Konsole aus.

HINWEIS: Erinnern Sie sich an den Modulo-Operator ;-)
'''

# Zwei Ganzzahlen von der Konsole einlesen
zahl1 = int(input("Bitte geben Sie die erste Ganzzahl ein: "))
zahl2 = int(input("Bitte geben Sie die zweite Ganzzahl ein: "))

# Überprüfen, ob zahl1 durch zahl2 restlos teilbar ist
if zahl1 % zahl2 == 0:
    ist_teilbar = True
else:
    ist_teilbar = False

# Ergebnis als Wahrheitswert ausgeben
print(f"Ist die erste Ganzzahl durch die zweite Ganzzahl teilbar? {ist_teilbar}")