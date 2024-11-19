liste_1 = [3, 5, 7, 8, 10, 2]
liste_2 = []

for x in range(len(liste_1)): # Index von 0 bis Länge von liste_1 - 1
    umgekehrt = liste_1[len(liste_1)- 1 -x]
    liste_2.append(umgekehrt)

print(liste_2)
    
# Alternativ:
#for x in range(len(liste_1)-1, -1, -1):
#    umgekehrt = liste_1[x]
#    liste_2.append(umgekehrt)

#print(liste_2)
