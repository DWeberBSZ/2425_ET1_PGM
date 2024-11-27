import random

versuche = 0
zahl = 0
zufaellig = random.randint(1, 10)
zahl_erraten = False

while versuche < 3 and not zahl_erraten:

    zahl = int(input("Ihre Zahl bitte: "))

    if zahl < zufaellig:
        print("Zahl zu klein.")
    elif zahl > zufaellig:
        print("Zahl zu groß.")
    else:
        zahl_erraten = True
        print("Zahl erraten, gewonnen!")

    versuche += 1

if not zahl_erraten:
    print("Spiel verloren.")