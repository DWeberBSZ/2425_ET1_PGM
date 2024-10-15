paketnummer = 0
fach = 0

while True: # Endlosschleife

    paketnummer = int(input("Paketnummer oder Beenden (0): "))

    if paketnummer == 0:
        break # Verlässt den aktuellen Schleifendurchlauf und ALLE darauffolgenden Durchläufe

    if paketnummer % 4 == 0 or paketnummer % 5 == 0:
        
        fach = 1

        if paketnummer % 100 == 0:

            fach = 2

            if paketnummer % 400 == 0:

                fach = 3

    else:

        fach = 4

    print(f"Fach: {fach}")

# <--- Hier landet man nach dem break Statement
    
print("Das Programm wurde durch die Eingabe von 0 beendet.");
