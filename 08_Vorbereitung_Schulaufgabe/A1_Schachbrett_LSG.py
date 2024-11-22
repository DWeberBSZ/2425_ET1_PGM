"""
Übungsaufgabe: Schachbrett
==========================

Die Geschichte des Schachbretts und der Reiskörner handelt von einem weisen Mann, der vom Kö
nig eine bescheidene Bitte äußert: Er möchte Reiskörner auf einem Schachbrett haben, wobei die 
Anzahl auf jedem Feld verdoppelt wird. Auf dem ersten Feld liegt ein Reiskorn, auf dem zweiten Feld 
liegen zwei Reiskörner, auf dem dritten Feld liegen vier Reiskörner, und so weiter… 

Berechnen Sie mithilfe eines Python-Skripts, wie viele Reiskörner auf dem letzten Feld liegen. Geben 
Sie das Ergebnis auf der Konsole in folgender Form aus:

HINWEIS: Ein Schachbrett hat 64 Felder.
"""

anzahl = 1

for x in range(1, 64):
    anzahl = anzahl*2
    
print(f"Auf dem letzten Feld liegen {anzahl} Reiskörner")

