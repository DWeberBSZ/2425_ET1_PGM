for ticketnummer in range (1, 11):

    input("Taste drücken, um Ticket zu ziehen.")

    print(f"Sie haben das Ticket mit der Nummer {ticketnummer} gezogen.")

    if ticketnummer == 1:
        print("Glückwunsch, Sie waren der Erste!")
        
    else:
        if ticketnummer == 5:
            print("Die Hälfte der Tickets ist verbraucht!")
        
        else:
            if ticketnummer == 8:
                print("Es sind nur noch zwei Tickets verfügbar!")
        
            else: 
                if ticketnummer == 9:
                    print("Knapp! Sie waren der Vorletzte!")
        
                else:
                    if ticketnummer == 10:
                        print("Glück gehabt, Sie haben das letzte Ticket erwischt!")

print("Jetzt sind keine Tickets mehr verfügbar!")