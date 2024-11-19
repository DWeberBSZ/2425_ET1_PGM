""" 
19.11.24
╔═════════════════════════════════════╗
║ MANIPULATION VON SEQUENZEN (LISTEN) ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 7.1

"""
╔═════════════════════════════════════╗
║         ELEMENTE ANSPRECHEN         ║
╚═════════════════════════════════════╝
"""
meine_liste = [0, 2, 4, 6, 23, 45, 7]
print(meine_liste)

# 3. Element aus der Liste ansprechen und auf der Konsole ausgeben:
#print(meine_liste[2]) # Index einer Liste fängt bei 0 an! -> Erste Element

# LETZTES Element aus der Liste ansprechen:
#print(meine_liste[6]) # Das ist die SCHLECHTESTE Variante!
#print(meine_liste[len(meine_liste)-1]) # Das ist die ZWEITSCHLECHTESTE Variante! 
#print(meine_liste[-1]) # Das ist die BESTE Variante!

# VORLETZTES Element aus der Liste ansprechen:
#print(meine_liste[-2]) # Das ist die BESTE Variante!

# AUFGABE: Letztes und vorletztes Element aus der Liste vertauschen:
tmp = meine_liste[-2]
meine_liste[-2] = meine_liste[-1] # <-----
meine_liste[-1] = tmp
print(meine_liste)

# Das ist der sogenannte DREICKSTAUSCH!

"""
╔═════════════════════════════════════╗
║  BEREICHE ANSPRECHEN MIT SLICING    ║
╚═════════════════════════════════════╝
"""
meine_liste = [3, 5, 34, 8, 32, 67, 98]

print(meine_liste[0:-1:2]) # START:ENDE:SCHRITTWEITE, ähnlich range(0, 10, 2) (da aber mit Kommas)
print(meine_liste[::2]) # Kein Endwert!!! -> unleich -1!!!
print(meine_liste[-1:0:-2]) # FRAGE: Was wird hier ausgegeben?

# Vorschlag AM: 98, 32, 34

txt = "Das ist ein String"
print(txt[0])



