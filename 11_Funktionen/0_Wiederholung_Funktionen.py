""" 
07.01.25
╔═════════════════════════════════════╗
║     WIEDERHOLUNG ZU FUNKTIONEN      ║
╚═════════════════════════════════════╝
""" 
# s. Buch, Kapitel 9

# Wozu braucht man Funktionen?
# - Code wird wiederverwendbar!
# - Fehler können dadurch einfacher behoben werden! -> Fehler muss nur 1x behoben werden!
# - Weniger Kosten in der Softwareentwicklung!
# - Das Programm wird übersichtlicher

# ################### TEIL 1: FUNKTIONSDEFINITIONEN ########################
# Verwendung von Funktionen:
# 1. Definition einer Funktion
def hello_func(name): 
    # Name der Funktion: hello_func
    # Übergabeparameter: name
    # def: Schlüsselwort für die Definition einer Funktion
    ausgabe = f"Hallo {name}"
    return ausgabe

def hello_func_no_return(name):
    if name == "":
        return
    
    print(f"Hallo {name}")
    # KEIN RÜCKGABEWERT!
    # Optional:
    

# ################### TEIL 2: HAUPTPROGRAMM ########################
# 2. Aufruf der Funktion
#ergebnis = 2 + 2
ergebnis = hello_func("Daniel") # Rückgabewert in einer Variable speichern mit =
print(ergebnis)

# Vorschlag von Daniel: mit input()
eingabe_name = input("Bitte geben deinen Namen ein: ")
ergebnis = hello_func(eingabe_name) # Rückgabewert in einer Variable speichern mit =
print(ergebnis)

hello_func_no_return("")

for x in range(10):
    hello_func_no_return(f"Schüler {x}")