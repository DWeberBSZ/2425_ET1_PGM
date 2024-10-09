paketnummer = 0
fach = 0

paketnummer = int(input("Bitte gebe die Paketnummer ein: "))

if paketnummer % 4 == 0 or paketnummer % 5 == 0:
    
    fach = 1

    if paketnummer % 100 == 0: # zusätzlich

        fach = 2

        if paketnummer % 400 == 0:

            fach = 3

else:

    fach = 4

print(f"Fach: {fach}")
