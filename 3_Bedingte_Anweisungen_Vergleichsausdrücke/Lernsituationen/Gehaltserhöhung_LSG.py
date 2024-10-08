# Eingabe
jahr = int(input("Bitte Gehaltsjahr eingeben: "))
gehalt = 0

# Verarbeitung
if jahr == 1:
    gehalt = 4000
else:
    gehalt = 4300 + (jahr - 2) * 100

# Ausgabe
print("Das neue Gehalt: " + str(gehalt))