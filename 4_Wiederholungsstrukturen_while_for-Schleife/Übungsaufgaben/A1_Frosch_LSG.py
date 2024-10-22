'''
Aufgabe: Frosch überquert die Straße
====================================  

In dieser Aufgabe lernen wir einen besonderen Frosch kennen, 
so wie ihn sich nur Mathematiker ausdenken können. 
Besonders seine Art, eine Straße zu überqueren, 
macht es zweifelhaft, ob er in der realen Welt überleben könnte.

Er überquert eine 2,5 Meter breite Straße wie folgt: 
Mit dem ersten Sprung legt er die erstaunliche Distanz von einem Meter 
zurück. Dann springt er wegen zunehmender Erschöpfung 
mit jedem weiteren Sprung nur noch halb so weit wie beim 
jeweils vorherigen Sprung.

Arbeitsauftrag:

- Schreiben Sie ein Python-Skript, mit welcher Hilfe Sie 
  herausfinden können, ob der Frosch es auf die andere 
  Straßenseite schafft.

Zeit: 15 Minuten.
'''

# Vorgabe der Variablen.
sprung_gesamt = 0   # Zurückgelegter Weg.
sprungweite = 1.0
durchläufe = 0

while sprung_gesamt < 2.5 and durchläufe < 100: # Variante 1 zum Beenden mit and

    sprung_gesamt = sprung_gesamt + sprungweite # Frosch springt.
    sprungweite = sprungweite / 2
    durchläufe += 1

    print(f"Zurückgelegter Weg: {sprung_gesamt}")

    # Variante 2 zum Beenden
    #if durchläufe == 100:
    #    break


    
    
