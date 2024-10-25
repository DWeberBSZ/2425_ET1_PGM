""" 
15.10.24
╔═════════════════════════════════════╗
║ WIEDERHOLUNGSSTRUKTUREN (SCHLEIFEN) ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 8.3 / 8.4

# Wozu benötigt man Schleifen?
# Antwort: Zum wiederholten Ausführen von Anweisungen!

""" 
╔════════════════╗
║ WHILE-SCHLEIFE ║
╚════════════════╝
""" 

# Beispiel: Summe der Zahlen von 1 bis einschließlich 100 auf der Konsole ausgeben (mittels while-Schleife)

# Unfertige LÖSUNG:
#zahl = 1
#while zahl <= 100:
#    print(zahl)
#    zahl = zahl + 1

# Frage: Welcher Wert steht nach der Bearbeitung der Schleife in zahl?
# Antwort: 101

# Fertige LÖSUNG:
zahl = 1
summe = 0 # Zusätzliche Variable für die Summe
while zahl <= 100:
    summe = summe + zahl
    zahl = zahl + 1

print(f"Summe: {summe}")

# Summe der Zahlen von 1 bis 100 = 1 + 2 + 3 + 4 + 5 + ... = ?
# Nach 1. Durchlauf: summe = 1
# Nach 2. Durchlauf: summe = 1 + 2 = 3
# Nach 3. Durchlauf: summe = 1 + 2 + 3 = 6
# ....

print(f"Wert von zahl nach der Bearbeitung der Schleife: {zahl}")

# Wir programmieren ein kleines "Spiel":

while True: # Endlosschleife
    zahl = int(input("Bitte gebe eine Zahl ein: "))

    if zahl < 0:
        print("Du hast eine negative Zahl eingegeben.")
        break # Das Spiel wird dadurch beendet.

    if zahl == 0:
        print("Du hast 0 eingegeben. Der aktuelle Schleifendurchlauf wird übersprungen.")
        continue # Verlässt den aktuellen Schleifendurchlauf und führt alle darauffolgenden Durchläufe noch aus

    print("Du hast eine positive Zahl eingegeben.")

# <-- Hier landet man bei break
print("Das Spiel wurde beendet.")

""" 
╔══════════════╗
║ FOR-SCHLEIFE ║
╚══════════════╝
""" 
