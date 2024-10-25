""" # Start des Kommentars
17.09.24
╔══════════════════════════════════╗
║    VARIABLEN UND DATENTYPEN      ║
╚══════════════════════════════════╝
""" # Ende des mehrzeiligen Kommentars!

# s. Buch, Kapitel # Das ist ein Kommentar!!! Der hat keinen Einfluss auf den Programmablauf!
# - 2.1, 2.2 (Variablen)
# - 3.1 (Operatoren)

# DEFINITION einer Variable: ANLEGEN einer Variable
y = 8 # der Wert 8 wird in die Variable y kopiert!
x = 6 # WICHTIG: Jede Variable braucht einen STARTWERT

# Sinnvoller Startwert für Variablen mit "Wörtern"
z = ""
 
y = y + 5 # Was steht in y drin?
print(y)

y += 5 # Das ist die kurze Version von Zeile 19
print(y)

y = y + x # Was steht in y drin?
print(y) # Vorschlag Mathias: 24, korrekt!

# y = y - x 
# y -= x # kurze Variante von Zeile 28

print(x/y) # 6 / 24 = 1/4 = 0.25

# x /= y kurz für x = x / y

# x = y / x -> das geht nicht kürzer!

# Frage: Wie schaut's mit periodischen Brüchen aus?
print(1/3)

print(10%3) # Das % ist der sog. MODULO-Operator, was macht der?
# % gibt den REST einer Ganzzahldivision aus!
# im Beispiel: 10 / 3 = 3 Rest: 1


# DATENTYPEN
# Der Datentyp ist die "Charaktereigenschaft" einer Varible
# also, z.B. 
# Ganzzahl (int)
a = 5
b = -3
# Kommazahl (float), 
c = 0.25 # WICHTIG: Das Komma ist der Punkt!!!
# Wahrheitswert (bool),
ist_wahr = True # oder False
 
# Wörter / Sätze / Zeichenketten / String (string)
vorname = "Dominik" # ... müssen in Anführungszeichen geschrieben werden!
nachname = 'Weber'

alter = input("Bitte gebe dein Alter an: ") # "32"
print(alter)

# input() liefert immer eine Zeichenkette und KEINE Zahl zurück!