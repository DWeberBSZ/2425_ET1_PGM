# ====================================================
# OBERER PROGRAMMTEIL: Definition der Variablen und Funktionen:
anzahl_buecher = 24
anzahl_teilnehmer = 0

# 1. Kunden begrüßen
#   > Es wird die Person mit dem übergebenen Namen gegrüßt.
def begruessen(name):
    print(f"Herzlich Willkommen {name}!")



# 2. Kassieren
#   > Es werden 3 Kunden abkassiert und überprüft, ob noch Bücher vorhanden sind.
#
#   TODO: 
#   ARBEITSAUFTRAG: 
#       - Definieren Sie hier eine Funktion kassieren() und rufen Sie diese im unteren Programmteil 3x auf.
#         HINWEIS: Hier sind KEINE Eingabeparameter notwendig.
#

if anzahl_buecher > 0:
    anzahl_buecher -= 1
    print("Vielen Dank für Ihren Einkauf bei Leselust & Wissen GmbH!")
else:
    print("Es sind leider keine Bücher mehr vorrätig.")



if anzahl_buecher > 0:
    anzahl_buecher += 1
    print("Vielen Dank für Ihren Einkauf bei Leselust & Wissen GmbH!")
else:
    print("Es sind leider keine Bücher mehr vorrätig.")



if anzahl_bucher > 0:
    anzahl_buecher -= 1
    print("Vielen Dank für Ihren Einkauf bei Leselust & Wissen GmbH!")
else:
    print("Es sind leider keine Bücher mehr vorrätig.")


# 3. Lesung anmelden.
#   > Es werden insgesamt 4 Lesungen angemeldet und überprüft, 
#   > ob die maximale Teilnehmerzahl von 10 Teilnehmern noch nicht erreicht wurde.
#
#   TODO: 
#   ARBEITSAUFTRAG: 
#       - Definieren Sie hier die Funktion lesung_anmelden() und rufen Sie diese im unteren Programmteil 4x auf.
#       HINWEIS: Hier sind KEINE Eingabeparameter notwendig.
#

if anzahl_teilnehmer < 10:

    anzahl_teilnehmer += 1
    print("Herzlich Willkommen zu unserer Lesung!")

else:
    print("Sie können leider nicht zu unserer Lesung angemeldet werden.")
    print("Die maximale Teilnehmerzahl wurde bereits erreicht!")




if anzahl_teilnehmer < 10:

    anzahl_teilnehmer += 1
    print("Herzlich Willkommen zu unserer Lesung!")

else:
    print("Sie können leider nicht zu unserer Lesung angemeldet werden.")
    print("Die maximale Teilnehmerzahl wurde bereits erreicht!")




if anzahl_teilnehmer < 10:

    print("Herzlich Willkommen zu unserer Lesung!")

else:
    print("Sie können leider nicht zu unserer Lesung angemeldet werden.")
    print("Die maximale Teilnehmerzahl wurde bereits erreicht!")




if anzahl_tilnehmer < 10:

    anzahl_teilnehmer += 1
    print("Herzlich Willkommen zu unserer Lesung!")

else:
    print("Sie können leider nicht zu unserer Lesung angemeldet werden.")
    print("Die maximale Teilnehmerzahl wurde bereits erreicht!")





# ====================================================
# UNTERER PROGRAMMTEIL: Hauptprogramm für Aufruf der Funktionen:

# 1. Begrüßen von 6 Personen:
begruessen("Sarah")
begruessen("Klaus")
begruessen("Manfred")
begruessen("Anita")
begruessen("Paul")
begruessen("Silvia")

# 2. Kassieren von 3 Kunden:
# TODO:
# ARBEITSAUFTRAG: Rufen Sie die Funktion kassieren() hier 3x OHNE Eingabeparameter auf:




# 3. Anmelden von 4 Lesungen:
# TODO:
# ARBEITSTAUFTRAG: Rufen Sie die Funktion lesung_anmelden() hier 4x OHNE Eingabeparameter auf:




# ====================================================