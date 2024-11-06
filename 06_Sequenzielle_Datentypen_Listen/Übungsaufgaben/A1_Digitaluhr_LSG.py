"""
Übungsaufgabe: Digitaluhr
=========================

Arbeitsauftrag:
 - Programmieren Sie eine Digitaluhr, die sekündlich die Uhrzeit in folgender Form auf der Konsole ausgibt: Stunde:Minute:Sekunde. (24h-Format)
 - Verwenden Sie drei Integer-Variablen für Stunde, Minute und Sekunde.
 - Starten bzw. initialisieren Sie das Programm mit der Uhrzeit 23:50:50 und prüfen Sie bei der Ausführung des Programms, 
   ob die Zeitumbrüche korrekt erfolgen (z.B. von Sekunde 59 auf Sekunde 0 bzw. Stunde 23 auf Stunde 0).
 - Das Programm soll sich für unsere Zwecke bei Erreichen der Zeit 00:00:59 selbständig beenden.

HINWEIS: Verwenden Sie die sleep-Funktion mit folgender Import-Anweisung in der ersten Zeile Ihres Programms: from time import sleep

TIPP: Zum Testen des Programms ist es hilfreich die Zeit etwas schneller vergehen zu lassen! ;-)

Zeit: 20 Minuten, Einzelarbeit
"""

from time import sleep

stunde = 23
minute = 50
sekunde = 50

while True:
    
    sleep(1)
    sekunde = sekunde + 1
    
    if sekunde == 60:
      minute = minute + 1
      sekunde = 0
        
    if minute == 60:
      stunde = stunde + 1
      minute = 0
        
    if stunde == 24:
      stunde = 0
        
    if sekunde == 59 and minute == 0 and stunde == 0:
      break
    
    print(f"{stunde:02d}:{minute:02d}:{sekunde:02d}")