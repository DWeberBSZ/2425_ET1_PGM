for ticketnummer in range(1, 11):

    input("Taste drücken, um Ticket zu ziehen.")

    print(f"Sie haben das Ticket mit der Nummer {ticketnummer} gezogen.")

    match ticketnummer:
        case 1 | 2:
            print("Glückwunsch, Sie waren der Erste!")
        case 5:
            print("Die Hälfte der Tickets ist verbraucht!")
        case 8:
            print("Es sind nur noch zwei Tickets verfügbar!")
        case 9:
            print("Knapp! Sie waren der Vorletzte!")
        case 10:
            print("Glück gehabt, Sie haben das letzte Ticket erwischt!")

print("Jetzt sind keine Tickets mehr verfügbar!")
