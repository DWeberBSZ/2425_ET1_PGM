"""
Aufgabe: Datentyp erkennen
========================== 

Erweitern Sie den untenstehenden Programmcode, sodass für alle uns bekannten Datentypen
(int, float, bool, str) eine entsprechende Ausgabe auf der Konsole ausgegeben wird.

Testen Sie das Programm, indem Sie der Variablen a Werte von verschiedenen Datentypen zuweisen.

Zeit: 10 Minuten, Einzelarbeit.
"""

a = True # Verschiedene Datentypen ausprobieren.

if isinstance(a, bool): # WAHR oder FALSCH
    print("Die Variable ist vom Typ Bool.")

# FRAGE: Was ist der Vorteil mit der Verwendung von else?
# ANTWORT: Das Programm wird schneller
else:
    if isinstance(a, float):
        print("Die Variable ist vom Typ Float.")
    else:  
        if isinstance(a, int):
            print("Die Variable ist vom Datentyp Int.")
        else:
            if isinstance(a, str):
                print("Die Variable ist vom Datentyp String.")

# if BEDINGUNG:
#    pass
# elif:
#    ...

if isinstance(a, bool): # WAHR oder FALSCH
    print("Die Variable ist vom Typ Bool.")

# FRAGE: Was ist der Vorteil mit der Verwendung von else?
# ANTWORT: Das Programm wird schneller
elif isinstance(a, float):
        print("Die Variable ist vom Typ Float.")
elif isinstance(a, int):
        print("Die Variable ist vom Datentyp Int.")
elif isinstance(a, str):
        print("Die Variable ist vom Datentyp String.")


# Ein Bool ist eine Teilmenge von Integer
# Ähnlich: Apfel ist Obst, aber Obst ist kein Apfel



    

