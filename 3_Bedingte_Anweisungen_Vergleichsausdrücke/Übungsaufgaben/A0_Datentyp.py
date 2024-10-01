"""
Aufgabe: Datentyp erkennen
========================== 

Erweitern Sie den untenstehenden Programmcode, sodass für alle uns bekannten Datentypen
(int, float, bool, str) eine entsprechende Ausgabe auf der Konsole ausgegeben wird.

Testen Sie das Programm, indem Sie der Variablen a Werte von verschiedenen Datentypen zuweisen.

Zeit: 10 Minuten, Einzelarbeit.
"""

a = False # Verschiedene Datentypen ausprobieren.

if isinstance(a, bool): # WAHR oder FALSCH
    print("Die Variable ist vom Typ Bool.")
    
else: 
    if isinstance(a, float):
        print("Die Variable ist vom Typ Float.")
        
    # ...

    

