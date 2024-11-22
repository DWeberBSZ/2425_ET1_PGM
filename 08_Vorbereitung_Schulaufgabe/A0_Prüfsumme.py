"""
Übungsaufgabe: Prüfsumme berechnen
==================================

Ziel dieser Aufgabe ist die Berechnung einer Prüfsumme von Kommazahlen innerhalb einer Liste.

- Die Zahlen liegen als Zeichenkette kodiert nacheinander innerhalb einer Liste. 
- Jede Kommazahl ist auf genau zwei Nachkommastellen angegeben.
- Für die Berechnung der Prüfsumme sind nur folgende Ziffern relevant:
    - Die Ziffer direkt VOR dem Dezimalpunkt
    - Die Ziffer direkt NACH dem Dezimalpunkt

AUFGABENSTELLUNG:
- Schreiben Sie ein Python-Skript, das alle relevanten Ziffern aufaddiert und auf der Konsole ausgibt.

"""

values = ['78.22', '6.41', '18.24', '4.49', '44.82', '43.09', '643.77', '3.71', '29.38', 
 '79.07', '95.54', '7.75', '24.65', '5.16', '7467.32', '6.68', '61.68', '91.61', 
 '31.90', '334.08', '23.77', '28.26', '49.75', '915.84', '10.13', '1.87', '46.71', 
 '7.91', '35.66', '6.83']
