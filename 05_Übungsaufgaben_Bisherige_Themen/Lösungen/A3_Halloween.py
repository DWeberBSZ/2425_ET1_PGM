# A3_Halloween.py

# Tage bis Halloween festlegen
tage_bis_halloween = 6

# Countdown-Schleife bis Halloween
for tage in range(tage_bis_halloween, -1, -1):
    
    print(f"Noch {tage} Tage bis Halloween.")
    
    if tage == 2:
        print("Nur noch zwei Tage bis Halloween!")
    elif tage == 1:
        print("Morgen ist Halloween!")
    elif tage == 0:
        print("Es ist Halloween!")

# Alternative:
# while tage_bis_halloween >= 0:
    
#     print(f"Noch {tage_bis_halloween} Tage bis Halloween.")
    
#     if tage_bis_halloween == 2:
#         print("Nur noch zwei Tage bis Halloween!")
#     elif tage_bis_halloween == 1:
#         print("Morgen ist Halloween!")
#     elif tage_bis_halloween == 0:
#         print("Es ist Halloween!")

#     tage_bis_halloween -= 1


