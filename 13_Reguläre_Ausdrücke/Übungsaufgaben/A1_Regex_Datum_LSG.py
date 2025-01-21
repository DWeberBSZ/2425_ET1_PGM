"""
Übungsaufgabe: Datum auf Gültigkeit überprüfen
==============================================
Ziel dieser Aufgabe ist die Überprüfung eines Datums auf ein korrektes Format.

Es gelten folgende Vorgaben:
- Der Tag muss aus 1 oder 2 Ziffern zwischen 1-31 bestehen.
- Der Monat muss aus 1 oder 2 Ziffern zwischen 1-12 bestehen.
- Das Jahr muss aus exakt 4 Ziffern bestehen.
- Zwischen den Bereichen muss ein Punkt . stehen

BEISPIELE FÜR KORREKTES DATUM:
- 12.03.1991
- 1.04.1987
- 03.5.0001

BEISPIELE FÜR FALSCHE DATUM:
- 12.03.191
- 1-04-87
- 32.1.1990

HINWEIS: 
Zur Vereinfachung müssen Sie nicht zusätzlich überprüfen, 
ob der Tag (z.B. 31) tatsächlich zum Monat (z.B. 2) passt. 

Lesen Sie ein Datum von der Konsole ein und teilen Sie dem Benutzer mit,
ob er ein gültiges Datum eingegeben hat oder nicht.

Zeit: 30 Minuten, Einzelarbeit
"""
import re

# Eingabe:
date = input("Bitte geben Sie ein Datum ein: ")

# Verarbeitung mit Regex:
date_pattern_re = re.compile(r"(\d{1,2})\.(\d{1,2})\.(\d{4})")
mo = date_pattern_re.search(date) 

if mo != None: # Doppelte Negierung
    valid = True
    # Prüfen, ob Wertebereich eingehalten wird:
    if int(mo.group(1)) < 1 or int(mo.group(1)) > 31:
        valid = False
    
    if int(mo.group(2)) < 1 or int(mo.group(2)) > 12:
        valid = False
else:
    valid = False


# Ausgabe:
if valid:
    print("Das Datum ist gültig!\n")
else:
    print("Das Datum ist nicht gültig!")



