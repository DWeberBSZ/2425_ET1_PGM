"""
Aufgabe: Qualität von Passwörtern bewerten
==========================================

Schreiben Sie eine Funktion, welche die Qualität von Passwörtern nach einem einfachen Punktesystem bewertet.
Es gelten folgende Regeln:

- Passwort mit 7 oder weniger Zeichen: immer 0 Punkte
- ab 8 Zeichen: +1 Punkt
- enthält sowohl Groß- als auch Kleinschreibung: +1 Punkt
- enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
- enthält zumindest eine Ziffer: +1 Punkt
- enthält zumindest ein Sonderzeichen: +1 Punkt

QUELLE: Fachbuch, Michael Kofler "Python, der Grundkurs"

Zeit: 20 Minuten, Einzelarbeit.
"""


def password_quality(password):
    quality = 0

    if len(password) <= 7: # Passwort mit 7 oder weniger Zeichen
        return quality

    quality += 1 # ab 8 Zeichen

    # Restliche Regeln mit for-Schleife:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special_char = False
    different_chars = set()
    special_chars = "[@_!#$%^&*()<>?}{~:]"

    for char in password:

        if char.islower(): 
            has_lower = True

        if char.isupper():
            has_upper = True

        if char.isdigit():
            has_digit = True

        if char in special_chars:
            has_special_char = True

        different_chars.add(char)

    if has_lower and has_upper: # Enthält sowohl Groß- als auch Kleinschreibung:
        quality += 1

    if len(different_chars) > 6: # Enthält mehr als sechs unterschiedliche Zeichen
        quality += 1

    if has_digit: # Enthält zumindest eine Ziffer
        quality += 1

    if has_special_char: # Enthält zumindest ein Sonderzeichen
        quality += 1

    return quality

quality = password_quality("abc")
print(f"Qualität des Passworts: {quality}")

quality = password_quality("abcdefghij")
print(f"Qualität des Passworts: {quality}")

quality = password_quality("ab1122$$!!")
print(f"Qualität des Passworts: {quality}")

quality = password_quality("abcd1234$!")
print(f"Qualität des Passworts: {quality}")


    

    
        
