def mystische_folge(len):
    
    # Sonderfall für Länge 1.
    if len == 1:
        return [1]
    
    # Sonderfall für Länge 2.
    if len == 2:
        return [1, 1]
    
    # Regulärer Fall.
    if len > 2:

        folge = [1, 1]

        # Listen-Index: liste[n] = liste[n-1] + liste[n-2]
        for n in range(2, len): # Länge: 3
            folge.append(folge[n-1] + folge[n-2])
    
        return folge
    # Sinnlose Eingabe.
    else:
        return []
    

laenge = int(input("Bis zu welcher Länge soll die mysteriöse Folge berechnet werden? "))
print("Die mysteriöse Folge der Länge {} lautet:".format(laenge))
print(mystische_folge(laenge))
    