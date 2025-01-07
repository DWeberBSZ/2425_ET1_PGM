""" 
07.01.25
╔═════════════════════════════════════╗
║      VERTIEFUNG ZU FUNKTIONEN       ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 9

# !!! Variablen in Funktionen !!!
# Beispiel 1:
#def print_var_x():
#    print(x)

#x = 3
#print_var_x()

# Vorschlag RB: Er pintet das nicht, weil er x in der Funktion nicht kennt (wird nicht übergeben)
# Vorschlag TT: Die Variable x müsste in der Funktion mit 'global' beschrieben werden.

# Das funktioniert! Die Funktion kann auf globale Variablen von "außerhalb" LESEND zugreifen!
# Lokale Variablen: Variablen, die innerhalb einer Funktion definiert wurden.
# Gloablen Variablen: Variablen, die außerhalb einer Funktion (im Hauptprogramm) definiert wurden.

# Beispiel 2:
#def print_var_y():
#    y = 5 # lokale Variable y definiert
#    print(y) # lokale Variable y wird ausgegeben

#print_var_y() # Funktion wird aufgerufen und ausgeführt
#print(y) # Wird versucht auf eine globale Variable y zuzugreifen!

# Vorschlag TH: Das innerhalb der Funktion macht er, das außerhalb nicht!

# Beispiel 3:
#def print_var_z():
#    z = 5 # Lokale Variable z
#    print(z)
#    # Lokale Variablen haben Vorrang vor globalen Variablen!

#z = 3 # Globale Variable z
#print_var_z()
#print(z)

# Beispiel 4:
# LESENDER ZUGRIFF auf globale Variablen innerhalb Funktion: OK!
# SCHREIBENDER ZUGRIFF auf globale Variablen innerhalb Funktion: NICHT OK! AUSSER: 
# def print_var_z2():

#     global z  # Optional
#     z = z + 3
#     print(z)

# z = 3 # Globale Variablen sind IM ALLGEMEINEN SHITTY!
# print_var_z2()

# Vorschlag: RB: Er nimmt in der Funktion die globale Variable z
# Vorschlag: DN: Er greift in der Funktion lesend darauf zu, gibt dann 3 aus.
# Vorschlag ME: 

# In Python könnt ihr "mehr als einen" Rückgabewert zurückgeben.
def return_multiple_values():
    a = 5
    my_list = list()
    name = "Osama"

    return (a, my_list, name) # Das hier ist EIN Tupel mit DREI Werten

b, meine_list, vorname = return_multiple_values()