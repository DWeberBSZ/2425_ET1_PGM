# WIEDERHOLUNGSFRAGEN:
# ====================
# W1: Der folgende Code löst einen Fehler aus. Warum?
x = 1
y = 2
print(x+y+z)

# Antwort: Die Variable z ist nicht "beschrieben", besser: definiert


# W2: Welchen Datentyp hat die Variable i nach der Zuweisung i = 3?
# Antwort: Integer (int), Ganzzahl


# W3: Welche Werte gibt das folgende Programm aus?
a = "abcde" # a = "abcde"
b = a       # b = "abcde"
a = a+"fg"  # a = "abcdefg"
print(b)    # b wird ausgegeben: b = "abcde"
# Ausgabe auf der Konsole: "abcde"


# W4: Der folgende Code ist fehlerhaft. Was könnte der Grund sein?
n = 22.7
msg = "Die Temperatur beträgt " + n + " Grad."

# Korrekte Lösung: msg = "Die Temperatur beträgt " + str(n) + " Grad." 

# Antwort: Mit + kann man nicht eine Zahl und eine Zeichenkette zusammenhängen.
# Entweder man ADDIERT mit + ZAHLEN.
# Oder: Man hängt mit + Strings zusammen.