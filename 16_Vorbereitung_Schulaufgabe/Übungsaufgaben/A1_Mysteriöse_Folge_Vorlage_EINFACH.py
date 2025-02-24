def mystische_folge(len):
    
    # Sonderfall für Länge 1.
    if len == 1:
        return [1]
    
    # Sonderfall für Länge 2.
    elif len == 2:
        return [1, 1]
    
    # Regulärer Fall.
    elif len > 2:
        
        folge = [1, 1]
        
        # TODO.
        
        
        return folge
        
    
    # Sinnlose Eingabe.
    else:
        return []
    

laenge = int(input("Bis zu welcher Länge soll die mysteriöse Folge berechnet werden? "))
print("Die mysteriöse Folge der Länge {} lautet:".format(laenge))
print(mystische_folge(laenge))
    