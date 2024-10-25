# A5_Teuflische_Folge.py

# Einlesen des Startwerts als Ganzzahl größer als 1
startwert = int(input("Geben Sie einen Startwert (ganzzahlig, größer als 1) ein: "))

# Berechnung und Ausgabe der Folge
wert = startwert
print("Teuflische Folge:")
print(wert)

while wert != 1:
    if wert % 2 == 0:  # Gerade Zahl
        wert = wert / 2
    else:  # Ungerade Zahl
        wert = (3 * wert + 1) / 2
    print(wert)
