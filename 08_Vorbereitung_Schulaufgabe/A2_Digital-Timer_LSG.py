from time import sleep

sekunde_start = 0

while True:
    print(f"\nGesetzte Startzeit: {sekunde_start} Sekunden. \n")
    print("Bitte wählen Sie eine der folgenden Funktionalitäten:")
    print(" set     Startzeit setzen.")
    print(" add     Addiere 5 Sekunden zur aktuellen Startzeit.")
    print(" start   Timer starten.")

    eingabe = input()

    if eingabe == "set": 
    
        print("> Startzeit setzen.")
        
        sekunde_start = int(input("Geben Sie die Sekunden ein: "))
        
        print(f"> Startzeit auf {sekunde_start} Sekunden gesetzt.")
        
    elif eingabe == "add": 
    
        print("> Addiere 5 Sekunden zur aktuellen Startzeit.")
        sekunde_start += 5
        
    elif eingabe == "start":
    
        print("> Timer gestartet.")
        
        for countdown_sek in range(sekunde_start, 0, -1):
            print(f"{countdown_sek}")
            
            sleep(1)
            
        print("++++ Timer abgelaufen ++++")
        
    else:
        print("Ungültige Eingabe. Bitte wählen Sie erneut.")
