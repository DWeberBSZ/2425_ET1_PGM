# FRAGE: Wie legt man ein leeres Dictionary an?
leeres_dict = { } # Das ist ein leeres Dictionary
leeres_dict = dict() # Das würde auch gehen!

# Das geht übrigens auch mit Listen!
leere_liste = [ ] 
leere_liste = list() 

# Wiederholung: Elemente zu einer Liste hinzufügen:
meine_liste = []
a = 5
meine_liste.append(a) # Somit wird ein Element zur Liste hinzugefügt.

# So funktioniert das mit Dictionaries:
mein_dictionary = { }
# ...
# ... 
mein_dictionary["1234"] = "Eier" # Bei Dictionaries könnt ihr noch nicht existente Indizes "erfinden" UND Werte zuweisen
print(mein_dictionary["1234"]) # <- an dieser Stelle funktioniert das!

# Dictionaries in einer Schleife:

# Wiederholung Zunächst mit Listen:
kurze_liste = [1, 2, 3, 4, 5]

# Werte der Liste auf der Konsole ausgeben:
for x in kurze_liste:
    print(x)

# So funktioniert mit Dictionarys:
artikel = {"1234" : "Milch", "5678": "Gewürz", "9876" : "Haferflocken"}
for x in artikel:
    print(x) # Hier werden die Schlüssel (Keys) ausgegeben!
    print(artikel[x])

# In Python kann man trotzdem sowohl Schlüssel als auch Werte erhalten:
for key, value in artikel.items():
    print(f"Schlüssel: {key}, Wert: {value}")