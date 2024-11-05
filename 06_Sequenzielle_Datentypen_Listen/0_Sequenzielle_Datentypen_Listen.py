""" 
05.11.24
╔═════════════════════════════════════╗
║  SEQUENZIELLE DATENTYPEN (LISTEN)   ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 7.1


""" 
╔═════════════════════════════════════╗
║        ERGÄNZUNG ZU STRINGS         ║
╚═════════════════════════════════════╝
""" 

# Einen sequenziellen Datentypen kennen wir schon:
txt = "Das ist eine Zeichenkette." # Das ist ein sequenzieller Datentyp!
txt = 'Das ist auch eine Zeichenkette.'

# Mit jedem Durchlauf wird ein neues Element der Sequenz 0...9 in der Variable x gespeichert.
#for x in range(10): # range liefert eine SEQUENZ: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#    print(x)

# Mithilfe einer FOR-SCHLEIFE kann man durch eine Sequenz durchlaufen:
for buchstabe in txt:
    print(buchstabe)

# Weitere Beispiele mit Strings (Zeichenketten):
txt = "Hello \nWorld." # \ leitet Sonderzeichen ein. \n -> Zeilenumbruch (Enter)
txt = "Hello \\ World." # es wird der Backslash auf der Konsole ausgegeben.
txt = r"Hello \n World." # Raw-String, Sonderzeichen werden nicht interpretiert.

#pfad = r"C:\Users\webd\" # Raw-Strings eignen sich z.B. für Dateipfade unter Windows

print(txt)

"""
╔═════════════════════════════════════╗
║        EINFÜHRUNG IN LISTEN         ║
╚═════════════════════════════════════╝
""" 

meine_liste = [3, 99, "Ein Text"]  # Diese Liste hat 3 Einträge!!!!

# MERKE: In einer Liste können verschiedene Datentypen gespeichert werden!

# Datentyp der Liste überprüfen:
print(type(meine_liste))

# FRAGE: Wie viele Elemente hat diese Liste?
zweite_liste = [42, 65, [45, 89], 88]

# Länge einer Liste mithilfe der len-Funktion in Erfahrung bringen:
print("Die Länge der zweiten Liste: ", len(zweite_liste))

# Listen können nach der Definition auch noch angepasst / erweitert werden.

zweite_liste.append("Das ist ein weiteres Element")
print("Die Länge der zweiten Liste: ", len(zweite_liste))

dritte_liste = [1, 2, 3]
dritte_liste.extend([4, 5, 6]) # extend erweitert die Liste um eine andere Liste: [1, 2, 3, 4, 5, 6]
#dritte_liste.append([4, 5, 6]) # append erweitert die Liste um ein Element: [1, 2, 3, [4, 5, 6]]
print(dritte_liste)

# Es gibt auch unveränderliche "Listen": Tupel
mein_tupel = (3, 99, "Ein Text") # Ein Tupel wird mit runden Klammern geschrieben (), eine Liste mit []

# FRAGE: Was heißt in diesem Zusammenhang "unveränderlich"?
# Ein Tupel kann NACH DER DEFINTION nicht mehr verändert werden.



