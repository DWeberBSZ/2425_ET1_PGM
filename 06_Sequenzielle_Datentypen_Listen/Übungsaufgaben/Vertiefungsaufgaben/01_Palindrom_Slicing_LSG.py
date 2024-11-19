wort = "Madam"
wort_lower = wort.lower()
        
if wort_lower == wort_lower[::-1]:
    print(f"Das Wort {wort} ist ein Palindrom.")
else:
    print(f"Das Wort {wort} ist kein Palindrom.")
        