""" 
24.09.24
╔══════════════════════════════════╗
║  BEDINGTE ANWEISUNGEN (IF-ELSE)  ║
╚══════════════════════════════════╝
""" 

# s. Buch, Kapitel 8.1

# Mit bedingten Anweisungen kann der PROGRAMMABLAUF gesteuert werden.
# Das Programm arbeitet in Abhängigkeit von BEDINGUNGEN nur bestimmte Anweisungen ab.

"""
Arbeitsauftrag:
===============
Informieren Sie sich zu bedingten Anweisungen mithilfe des Fachbuchs.

- Lesen Sie Kapitel 8.1 "if-Verzweigung" im Fachbuch

Zeit: 8 Minuten, bis 12:40
"""

""" Bedingte Anweisung, auch genannt: "if-Anweisung"

Aufbau einer if-Anweisung:

if BEDINGUNG:   # : nicht vergessen
    Anweisung 1 # Anweisungen mit TAB einrücken!
    Anweisung 2 # Die Anweisungsfolge innerhalb einer if-Anweisung nennt sich ANWEISUNGSBLOCK
    ...
    
else: # Der else-Zweig ist optional
    Anweisung 1
    Anweisung 2
    ...
    

WICHTIG: Die BEDINGUNG muss sich zu True oder False auswerten lassen!
    - Entweder: Verwendung von True, False oder einer Variable vom Datentyp bool
    - Oder: Vergleichsaudrücke -> machen wir später!

"""

a = 5.4
ist_int = isinstance(a, int)

# MERKE: Der else-Zweig einer if-Anweisung gehört auf die gleiche
# "Höhe" wie die zugehörige if-Anweisung.

# INNERHALB eines Zweigs können WEITERE if-else-Anweisungen stehen
# (mit entsprechender Einrückung)

if ist_int:
    print("Die Variable ist vom Datentyp Integer.")
else:
    print("Die Variable ist NICHT vom Datentyp Integer.")

    if isinstance(a, float):
        print("Die Variable ist vom Datentyp float.")

# VERGLEICHSOPERATOREN
# ====================

# ==  Prüfen auf Gleichheit! NICHT ZU VERWECHSELN MIT Zuweisungsoperator =
# !=  Prüfen auf Ungleichheit!
# >   Größer als 
# <   Kleiner als
# >=  Größer oder gleich als
# <=  Kleiner oder gleich als

# Das ERGEBNIS einer Vergleichoperatoren ist ein WAHRHEITSWERT:
# True, False

alter_al = 42
alter_to = 20

# Frage: Ist Al älter als To?

if alter_al > alter_to:
    print("Al ist älter To.")
else:
    # TODO.
    pass      

# Ergänzung: Prüfen auf Un-/Gleichheit funktioniert NICHT NUR mit Zahlen.













