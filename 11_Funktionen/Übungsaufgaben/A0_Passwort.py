"""
Aufgabe: Qualität von Passwörtern bewerten
==========================================

Schreiben Sie eine Funktion, welche die Qualität von Passwörtern nach einem einfachen Punktesystem bewertet.
Es gelten folgende Regeln:

- Passwort mit 7 oder weniger Zeichen: immer 0 Punkte
- ab 8 Zeichen: +1 Punkt
- enthält sowohl Groß- als auch Kleinschreibung: +1 Punkt -> isupper(), islower()
- enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt -> Datentyp set() (wie Liste nur, dass jeder Eintrag nur 1x vorkommen darf)
- enthält zumindest eine Ziffer: +1 Punkt -> isdigit()
- enthält zumindest ein Sonderzeichen: +1 Punkt -> Alle Sonderzeichen in Liste speichern und Abfragen ob Zeichen in Liste

QUELLE: Fachbuch, Michael Kofler "Python, der Grundkurs"

Zeit: 20 Minuten, Einzelarbeit.
"""

def password_quality(password):
    punkte = 0
    # Hier muss das Passwort überprüft werden.
    # ...
    return punkte


    

    
        
