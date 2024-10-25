# A2_Katzenjahre.py

# Einlesen des Katzenalters als nicht-negative Ganzzahl
katzenjahre = int(input("Geben Sie das Alter der Katze in Katzenjahren ein: "))

# Berechnung der Menschenjahre
if katzenjahre == 1:
    menschenjahre = 15
elif katzenjahre == 2:
    menschenjahre = 21
elif katzenjahre == 3:
    menschenjahre = 27
elif katzenjahre > 3:
    menschenjahre = 27 + (katzenjahre - 3) * 4
else:
    menschenjahre = 0

# Ausgabe des Alters in Menschenjahren
print(f"{katzenjahre} Katzenjahr(e) entspricht umgerechnet {menschenjahre} Menschenjahren.")
