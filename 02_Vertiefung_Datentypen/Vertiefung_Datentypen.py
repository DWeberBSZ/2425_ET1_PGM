""" 
18.09.24
╔══════════════════════════════════╗
║     VERTIEFUNG ZU DATENTYPEN     ║
╚══════════════════════════════════╝
""" 

# s. Buch, Kapitel 
# - 2.1, 2.2 (Variablen)

# DATENTYP einer Variable herausfinden:
# In ANDEREN Programmiersprachen, nicht in PYTHON:
# int a = 0;


# in PYTHON geht das so:
a = 0
b = True # Bool, Wahrheitswert
z = "Dominik Weber"
y = -0.45

typ_von_a = type(a)
print(typ_von_a)

# Kurzform vom oberen:
print(type(b))
print(type(z))
print(type(y))

# Speichern eines Dokuments: Strg + S

ist_b_float = isinstance(b, float) # Hier kommt True oder False raus
print(ist_b_float)

# MERKEN: Funktionen type() und isinstance()

# IMPLIZITE TYPUMWANDLUNG:
print(10/4) # Ergebnis: 2.5, Datentyp: float, NICHT: int
print(10+4.5)

# EXPLIZITE TYPUMWANDLUNG:
# Kennen wir von str(), int(), float()
# Wichtig: Informationen müssen "kompatibel" sein
print(int(4.8)) # Hier wird nur der Wert VOR dem Komma verwendet!!!

exp_bool = bool(0) # False!
exp_bool = bool(1) # True!
exp_bool = bool("False") # True!
exp_bool = bool("0") # True!
exp_bool = bool("") # False!

print(exp_bool)

# Regel: 
# Zeichenketten: "" -> False, "..." -> True
# Zahlen: 0 -> False, alles andere -> True
# "Alles, was nicht verboten ist, ist erlaubt!"



























