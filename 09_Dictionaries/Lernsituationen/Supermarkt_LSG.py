'''
Gesamtlernziel: 
================
Ziel ist die Programmierung eines Skripts, welches mithilfe eines Dictionaries
Zahlencodes (Barcodes) den entsprechenden Artikelbezeichnungen zuordnet. 


Aufgabenstellung:
================
Erweiteren Sie den nachfolgenden Programmausschnitt, sodass das Skript wiederholt Barcodes von
der Konsole einliest und die zugehörigen Artikelbezeichnungen auf der Konsole wieder ausgibt.

Implementieren Sie hierfür folgende drei Schritte:

Schritt 1: 

Definieren Sie ein Dictionary mit dem Namen 'artikel' mit folgenden Schlüssel-Werte-Paaren:

------------------------------------------------------
|     Schlüssel     |              Wert               |
|     (Barcode)     |      (Artikelbezeichnung)       |
------------------------------------------------------
|        "1"        |             "Waffeln"           |
|        "2"        |             "Gewürz"            |
|        "3"        |   "Scanvorgang abgeschlossen."  |
-------------------------------------------------------


Schritt 2: 

Lesen Sie innerhalb der vorgegebenen while-Schleife einen Barcode mit der input-Funktion ein, 
und speichern Sie den eingelesenen Wert in einer Variable mit dem Namen 'barcode'. 
Verwenden Sie hierbei folgende Eingabeaufforderung: "Bitte Barcode scannen: ".


Schritt 3:

Sofern der Artikel im Dictionary hinterlegt ist und der User den Scanvorgang fortsetzen möchte,
soll mit der print-Funktion die Artikelbezeichnung des zugehörigen Barcodes auf der Konsole
in folgender Form ausgegeben werden (z.B. für Waffeln):  "Eingescannt: Waffeln". 
Verwenden Sie für den Zugriff auf das Dictionary die Variable 'barcode' als Schlüssel.

Hinweise: 

Die "echten" Barcodes wurden hier durch die Ziffern 1, 2 und 3 ersetzt.
Sie benötigen keinen Barcodescanner, sondern können die Barcodes über die Tastatur eingeben.  
In Wirklichkeit entspricht ein Barcode einer größeren Zahl.


Hilfsmittel:
================
    - Diskussion  mit Nachbarin / Nachbar, maximal 3 Personen zusammen, am Platz sitzen bleiben
    - Webseite: https://www.python-kurs.eu/python3_dictionaries.php
    - Beliebige Dokumentation im Internet
    - Lehrkraft, bei Fragen melden: Ich komme zum Platz

Zeit: 
================
15 Minuten, bis 
'''

# Schritt 1. Definition eines Dictionaries mit dem Namen 'artikel'.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
artikel = { "1" : "Waffeln" , "2" : "Gewürz", "3" : "Scanvorgang abgeschlossen" }
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

while True:

    # Schritt 2. Einlesen einer Zahl (Barcode) von der Konsole und speichern in Variable 'barcode'.
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    barcode = input("Bitte Barcode scannen: ")
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    # Falls Barcode (Schlüssel) im Dictionary hinterlegt ist.
    if barcode in artikel: # Hier wird der Schlüssel überprüft!
        
        if barcode != "3": 
            # Scanvorgang fortsetzen.
            
            # Schritt 3. Ausgabe der Artikelbezeichnug auf der Konsole.
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            print("Eingescannt: " + artikel[barcode])
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            
        else:
            # Scanvorgang abgeschlossen: Beende Schleife.
            print(artikel[barcode])
            break
        
    else:
        # Falls Barcode (Schlüssel) nicht in Dictionary hinterlegt ist.
        print("Artikel ist nicht hinterlegt.")