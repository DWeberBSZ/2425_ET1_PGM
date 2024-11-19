wort = "Madam"
wort_lower = wort.lower()
ist_palindrom = True

for x in range(len(wort_lower)):
    if wort_lower[x] != wort_lower[-1-x]:
        # kein Palindrom.
        ist_palindrom = False
        
if ist_palindrom == True:
    print(f"Das Wort {wort} ist ein Palindrom.")
else:
    print(f"Das Wort {wort} ist kein Palindrom.")
        