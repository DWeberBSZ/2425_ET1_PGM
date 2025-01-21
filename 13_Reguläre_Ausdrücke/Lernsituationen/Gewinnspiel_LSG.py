import re 

win_codes = list()

def is_win_code(text):

    # Anlegen eines Regex-Objekts mit unserem Muster (Pattern).
    # win_code_pattern_re = re.compile(r"\d\d\d-(\d\d\d)-(\d\d\d\d)")
    # Alternativ:
    win_code_pattern_re = re.compile(r"\d{3}-(\d{3})-(\d{4})")

    # WIEDERHOLUNGEN können mit {} realisiert werden
    # z.B. {3} für exakt 3 Wiederholungen
    # z.B. {3,5} für 3 bis 5 Wiederholungen (inklusiv!!!)
    
    # ANDERE ARTEN VON WIEDERHOLUNGEN:
    # Asteriks * -> Keine Wiederholung oder beliebig viele, 0...n
    # Plus + - Eine Wiederholung oder beliebig viele, 1...n

    # Variable text auf regulären Ausdruck mit Funktion search() überprüfen.
    mo = win_code_pattern_re.search(text) # Gibt ein Match-Objekt zurück (mo) oder None, wenn nichts gefunden wurde.

    # Prüfen, ob Muster gefunden wurde und ein Gewinn vorliegt.
    if mo != None:
        # Überprüfe Gewinnbedingungen.
        bedingung_1 = int(mo.group(1)) > 500
        # Zusatzaufgabe:
        bedingung_2 = False
        for char in mo.group(2):
            if int(char) == 7 or int(char) == 4:
                bedingung_2 = True
        
        if bedingung_1 and bedingung_2:
            return True
        else: 
            return False
    else:
        return False


with open("win_codes.txt", "r") as file:

    for line in file: # Alle Zeilen durchlaufen.
        if is_win_code(line.strip()):
            win_codes.append(line.strip())

print(win_codes)

# OPTIONAL: Zusätzlich in separater Datei abspeichern:
with open("win_codes_won.txt", "w") as file:
    for win_code in win_codes:
        file.write(win_code + "\n")


