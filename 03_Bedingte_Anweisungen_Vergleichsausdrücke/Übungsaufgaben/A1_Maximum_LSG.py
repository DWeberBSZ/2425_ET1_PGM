'''
Aufgabe: Maximum von drei Zahlen
=================================

Arbeitsauftrag:

- Erstellen Sie ein Programm, welches nacheinander drei Ganzzahlen von der Konsole einliest
  und in drei Variablen abspeichert.
  
- Unterscheiden Sie mithilfe von bedingten Anweisungen, welche der drei Zahlen die größte ist
  und geben Sie die größte der drei Zahlen in folgender Form auf der Konsole aus:

  "Das Maximum der drei Zahlen ist xx."

Zeit: 20 Minuten, Einzelarbeit.
'''


zahl1 = int(input("Bitte gebe Zahl 1 ein: ")) # DEFINITION von Variablen.
zahl2 = int(input("Bitte gebe Zahl 2 ein: "))
zahl3 = int(input("Bitte gebe Zahl 3 ein: "))

max = zahl1 # Annahme: zahl1 ist die größte Zahl, Variable für aktuelles MAXIMUM

# "Wenn Annahme falsch ist, wird max im Folgenden überschrieben"
if zahl2 > max:
    max = zahl2 # max mit zahl2 überschreiben, d.h. mein "neues" Maximum ist zahl2
    
if zahl3 > max:
  max = zahl3 # max mit zahl3 überschreiben
        
print(f"Das Maximum der drei Zahlen ist {max}.")
# Stringformatierung: Einbetten von Variablen in den String.

    

