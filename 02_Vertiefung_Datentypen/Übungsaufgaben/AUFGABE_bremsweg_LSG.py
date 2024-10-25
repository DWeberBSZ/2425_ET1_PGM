"""
Aufgabe: Bremsweg
====================

In der Fahrschule lernt man folgende Faustformeln zur Berechnung von Anhaltewegen:

Reaktionsweg (in m) = (Geschwindigkeit (km/h) / 10) * 3
Bremsweg (in m)     = (Geschwindigkeit (km/h) / 10) * (Geschwindigkeit (km/h) / 10)
Anhalteweg (in m)   = Reaktionsweg + Bremsweg

AUFGABENSTELLUNG:
=================
- Lesen Sie die Geschwindigkeit in km/h mit der input-Anweisung von der Konsole ein.
- Führen Sie die Berechnung des Anhaltewegs mit geeigneten Variablen und Zuweisungen durch.
- Geben Sie das Ergebnis des Anhaltewegs auf der Konsole aus.
- Kontrollieren Sie das Ergebnis mit einem Taschenrechner.

Zeit: 10 Minuten, Einzelarbeit oder Partnerarbeit
"""
geschwindigkeit = input("Geben Sie die Geschwindkeit (km/h) ein: ")
geschwindigkeit = float(geschwindigkeit)

reaktionsweg = (geschwindigkeit / 10) * 3
bremsweg = (geschwindigkeit / 10) * (geschwindigkeit / 10)
anhalteweg = reaktionsweg + bremsweg

# kurze Variante von den drei Zeilen oben:
anhalteweg = (geschwindigkeit / 10) * 3 + (geschwindigkeit / 10)**2

# Eine formatierte Ausgabe!
# Der Datentyp ist hier "egal" -> Hier passiert eine IMPLIZITE TYPUMWANDLUNG nach String.
# Verwendung von {VARIABLE}
# Verwendung: f"{VARIABLE}" -> Geschweifte Klammer: Alt Gr + 7 bzw. 0
print(f"Der Anhalteweg beträgt {anhalteweg} Meter.")

