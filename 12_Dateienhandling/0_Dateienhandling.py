""" 
07.01.25
╔═════════════════════════════════════╗
║           DATEIENHANDLING           ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 14

# Heutiges Ziel:
# Wir lernen Werkzeuge kennen, um mit Dateien umzugehen
# Beispiel: Abspeichern eines Spielstands (später: TicTacToe)

# Einstiegsfrage: Was ist denn überhaupt eine Datei?
# Vorschlag: Ansammlung von Daten / Informationen
# Vorschlag: Inhalt benötigt ein bestimmtes Format, Dateitypen/Dateiformate
# Vorschlag: Ansammlung von 0en und 1en
# Vorschlag: Dateien werden von Programmen genutzt

# Das Wort "Datei" ist ein Kunstwort aus:
# - Daten -> Informationen
# - Kartei -> Ordnung / Ablage

# Dateien sind auf einem Medium identifizierbar und abrufbar!
# Wie wird die "Art" der Datei bestimmt?
# AM: "Über die Endung" - stimmt für Windows!
# Linux: Unter Linux gibt's keine Dateiendungen
# Linux Mint -> Kostenlos runterladen! Portable OS!!!

# 3 Schritte beim Öffnen / Bearbeiten von Dateien

# 2. Lesen / Schreiben / Bearbeiten
# 3. Schließen <--- ganz wichtig!

# 1. Öffnen
fobj = open("yellow_snow.txt", "r") # Modus: r -> read, w -> write, a -> append)

# 2. Lesen
for zeile in fobj:
    print(zeile)

# Alternative: 
alle_zeilen = fobj.readlines()

# 3. Schließen
fobj.close()

# 2. Variante: In eine Datei schreiben
fobj2 = open("yellow_snow.txt", "w")
# Wenn Datei bereits vorhanden ist: ÜBERSCHREIBEN!

fobj2.write("Das ist eine Zeile\n")
fobj2.write("Das ist eine zweite Zeile\n")

fobj2.close()

# 3. Variante:
fobj2 = open("yellow_snow.txt", "a") # Modus: Append
# Wenn Datei bereits vorhanden ist: Zeilen hinzufügen!

fobj2.write("Das ist eine Zeile\n")
fobj2.write("Das ist eine zweite Zeile")
fobj2.close()

# Eine Abkürzung:
with open("yellow_snow.txt", "r") as fobj3:
    # Hier kommen die Anweisungen für die Datei rein!
    # <-- Eingerückt um einen Block
    # Das ist identisch zu open, bearbeiten, close!!!
    # Vorteil: Datei wird immer automatisch geschlossen!!!!
    pass





