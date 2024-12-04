""" 
04.12.24
╔═════════════════════════════════════╗
║ REFERENZEN & KOPIEREN VON SEQUENZEN ║
╚═════════════════════════════════════╝
""" 
a = [1, 2, 3] # 1. In a wird eine Liste [1,2,3] abgespeichert
b = a # 2. Liste wird in b abgespeichert
a[0] = 4 # 3. Erstes Element von Liste a wird mit 4 überschrieben.

print(f"Inhalt von a: {a}, ID: {id(a)}") # 4, 2, 3
print(f"Inhalt von b: {b}, ID: {id(b)}") # 1, 2, 3

# Vorschlag von Alexander:
# "Man kann Listen ordentlich kopieren"
import copy
#b = a.copy() # Hier wird tatsächlich eine KOPIE erzeugt!
b = copy.copy(a) # FLACHE KOPIE! -> Kopiert nur "oberste" Ebene

print("Nach dem ordentlichen Kopieren:")
print(f"Inhalt von a: {a}") 
print(f"Inhalt von b: {b}")

a[0] = 3

print(f"Inhalt von a: {a}, ID: {id(a)}") 
print(f"Inhalt von b: {b}, ID: {id(b)}")


c = [1, 2, [3, 4]]
d = copy.deepcopy(c) # TIEFE KOPIE! -> kopiert alle Referenzen

print(f"Inhalt von c: {c}, ID: {id(c)}, ID innere Liste: {id(c[2])}") 
print(f"Inhalt von d: {d}, ID: {id(d)}, ID innere Liste: {id(d[2])}")


