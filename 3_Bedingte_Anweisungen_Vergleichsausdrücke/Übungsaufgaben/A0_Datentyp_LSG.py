"""
Aufgabe: Datentyp erkennen
========================== 

Erweitern Sie den untenstehenden Programmcode, sodass für alle uns bekannten Datentypen
(int, float, bool, str) eine entsprechende Ausgabe auf der Konsole ausgegeben wird.

Testen Sie das Programm, indem Sie der Variablen a Werte von verschiedenen Datentypen zuweisen.

Zeit: 10 Minuten, Einzelarbeit.
"""

# Mögliche Lösung: 

a = True # Verschiedene Datentypen ausprobieren.

if isinstance(a, bool): 
    print("Die Variable ist vom Typ Bool.")
    
else: 
    if isinstance(a, float):
        print("Die Variable ist vom Typ Float.")
        
    else:
        if isinstance(a, int):
            print("Die Variable ist vom Typ Integer.")
            
        else:
            if isinstance(a, str):
                print("Die Variable ist vom Typ String.")
                
# Kürzere Variante:
a = True # Verschiedene Datentypen ausprobieren.

if isinstance(a, bool): 
    print("Die Variable ist vom Typ Bool.")
    
elif isinstance(a, float):
    print("Die Variable ist vom Typ Float.")
        
elif isinstance(a, int):
    print("Die Variable ist vom Typ Integer.")
            
elif isinstance(a, str):
    print("Die Variable ist vom Typ String.")



    

