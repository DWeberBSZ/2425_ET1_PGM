'''
Übungsaufgabe: Supermarkt
=========================

- Ziel ist die Erstellung eines Python-Skripts, welches einen Einkaufsvorgang 
mithilfe einer Liste und einer for-Schleife simuliert.

- Der Einkaufswagen soll als Liste implementiert werden.

- Erstellen Sie ein Python-Skript, welches insgesamt 10 Artikel als 
Zeichenkette von der Konsole einliest und dem Einkaufswagen hinzufügt.

VORGABE: 
Wenn ein gleichnamiger Artikel schon im Einkaufswagen ist, soll er nicht hinzugefügt werden.

- Informieren Sie sich hierfür zum Schlüsselwort 'in' mithilfe einer Internetrecherche.

Siehe auch Buch, Kapitel 7.1.

Zeit: 20 Minuten, Einzelarbeit.
'''

einkaufswagen = []

artikel = input("Gebe einen Artikel ein:")

for i in range(10):

    if artikel in einkaufswagen:
        print("Der Artikel ist bereits im Einkaufswagen.")
    else:
        einkaufswagen.append(artikel)
        
    artikel = input("Gebe einen Artikel ein:")
    
print(f"Der Inhalt des Einkaufswagens ist: {einkaufswagen}")



    

