paketnummer = 0
fach = 0


paketnummer = int(input("Paketnummer oder Beenden (0): "))

# Solange (while) BEDINGUNG zutrifft.
while paketnummer != 0: # 1. Schritt: Abfrage der Bedingung im Schleifenkopf

    # 2. Schritt: Abarbeiten der Anweisungen INNERHALB von der Schleife ("Alles, was eingerückt ist.")
    if paketnummer % 4 == 0 or paketnummer % 5 == 0:
        
        fach = 1

        if paketnummer % 100 == 0:

            fach = 2

            if paketnummer % 400 == 0:

                fach = 3

    else:

        fach = 4

    print(f"Fach: {fach}")
    
    paketnummer = int(input("Paketnummer oder Beenden (0): "))

    # 3. Schritt: Zurückspringen zum Schleifenkopf (Zeile 8)

# <--- Hier wird nach der Schleife weitergemacht (Wenn die Bedingung nicht mehr zutrifft)!

print("Das Programm wurde durch die Eingabe von 0 beendet.")
