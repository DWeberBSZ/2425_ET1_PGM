import re 

win_codes = list()

# Reguläre Ausdrücke, kurz Regex genannt, sind Beschreibungen für ein Textmuster. 
# Ein \d in einem Regex steht zum Beispiel für ein Ziffernzeichen, d. h. eine beliebige einzelne Ziffer von 0 bis 9. 
# Der Regex \d\d\d-\d\d\d-\d\d\d wird von Python verwendet, um dasselbe Textmuster zu finden, 
# das auch die vorherige Funktion isPhoneNumber() gefunden hat: 
# eine Zeichenfolge aus drei Zahlen, einem Bindestrich, drei weiteren Zahlen, einem weiteren Bindestrich und vier Zahlen. 
# Jede andere Zeichenfolge würde nicht mit dem Regex \d\d\d-\d\d\d-\d\d\d übereinstimmen.

def is_win_code(text):

    # Anlegen eines Regex-Objekts mit unserem Muster (Pattern).
    win_code_pattern_re = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    # Alternativ:
    # win_code_pattern_re = re.compile(r"\d{3}-\d{3}-\d{4}")

    # Variable text auf regulären Ausdruck mit Funktion search() überprüfen.
    mo = win_code_pattern_re.search(text) # Gibt ein Match-Objekt zurück (mo) oder None, wenn nichts gefunden wurde.

    # Prüfen, ob Muster gefunden wurde und ein Gewinn vorliegt.
    if mo != None:
        print(mo.group())
        return True
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


