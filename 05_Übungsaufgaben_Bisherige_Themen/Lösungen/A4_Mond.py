# A4_Mond.py

# Anfangswerte
dicke_papier = 0.0001  # Anfangsdicke des Papiers in Metern
entfernung_mond = 380000000  # Entfernung zum Mond in Metern
faltungen = 0

# Faltprozess
while dicke_papier <= entfernung_mond:
    dicke_papier *= 2
    faltungen += 1

# Ausgabe der Anzahl der Faltungen
print("Anzahl der Faltvorgänge, um den Mond zu erreichen:", faltungen)
