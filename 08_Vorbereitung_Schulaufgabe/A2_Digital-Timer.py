from time import sleep

sekunde_start = 0

while True:
    print(f"\nGesetzte Startzeit: {sekunde_start} Sekunden. \n")
    print("Bitte wählen Sie eine der folgenden Funktionalitäten:")
    print(" set     Startzeit setzen.")
    print(" add     Addiere 5 Sekunden zur aktuellen Startzeit.")
    print(" start   Timer starten.")

    eingabe = input()

    # ...