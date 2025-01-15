"""
Übungsaufgabe: E-Mail-Adresse erkennen
======================================
Ziel dieser Aufgabe ist das Herausfiltern von bestimmten E-Mail-Adressen aus einem korrupten Textdokument.

Gegeben ist das Textdokument mail_addresses.txt mit E-Mail-Adressen. 
Leider haben sich ein paar fehlerhafte Zeilen eingeschlichen. 
Sie müssen herausfinden, welche Zeilen überhaupt eine E-Mail-Adresse darstellen… 

Die gesuchten E-Mail-Adressen haben immer das folgende Format: 
- Für die drei Zeichen vor dem Klammeraffen @ soll folgendes gelten: 
    - Ein Zeichen, das keine Ziffer (0-9) ist 
    - Zwei Zeichen, die entweder Buchstabe, Ziffer oder der Unterstrich sind
- Es folgt der Klammeraffe @
- Die E-Mail-Adressen sollen alle mit der Domain bsz-neumarkt.de enden

HINWEIS: Nutzen Sie als Hilfestellung Tabelle 7-1 im Kapitel "Character Classes" der folgenden Website:
https://automatetheboringstuff.com/2e/chapter7/

Speichern Sie die relevanten E-Mail-Adressen in einer separaten Datei ab.

ZUSATZAUFGABE:
Geben Sie den Inhalt vor dem Klammeraffen @ während des Programmablaufs zusätzlich auf der Konsole aus.

Zeit: 20 Minuten, Einzelarbeit
"""