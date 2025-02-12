FARBE_X = '\033[92m'
FARBE_O = '\033[94m'
ENDC = '\033[0m'

# 1. Anlegen einer Klasse mit Schlüsselwort class ...
class TicTacToe:

    def __init__(self):
        # Hier werden Standardwerte für die Attribute vergeben!
        # Das hier sind die Attribute der Klasse!
        # MERKE: Alle notwendigen Attribute werden in der __init__()-Methode angelegt
        # Diese Informationen waren vorher global im Programm!
        # Jetzt sind sie im Kontext dieser Klasse angesiedelt!
        self.spielfeld = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.spieler_am_zug = "X"
        self.spieler_eingabe = ""

        # Das ist eine Methode.
        self.spielfeld_zeichnen()

        # WICHTIG: Vor allen Attributen und Methoden INNERHALB der Klasse muss self. stehen!

    # Ab hier stehen unsere Methoden (identisch zu vorher!)
    # Einrücken nicht vergessen!
    """ (1) Programmbaustein: Spielfeld zeichnen """
    def spielfeld_zeichnen(self):
        """
        DIESE FUNKTION IST BEREITS FERTIG! HIER MÜSSEN UND DÜRFEN KEINE ÄNDERUNGEN VORGENOMMEN WERDEN!

        Die Funktion spielfeld_zeichnen() "zeichnet" das Spielfeld auf der Konsole mithilfe von print()-Anweisungen.
        Felder, welche vom Spieler X bespielt wurden, werden in der Farbe Grün ausgegeben.
        Felder, welche vom Spieler O bespielt wurden, werden in der Farbe Blau ausgegeben.

        Übergabeparameter: Keine.
        Rückgabewert: Keinen.
        """

        def farbe(feld):
            if feld == "X":
                return "{0}{1:^5s}{2}".format(FARBE_X, feld, ENDC)

            elif feld == "O":
                return "{0}{1:^5s}{2}".format(FARBE_O, feld, ENDC)

            else:
                return "{0:^5s}".format(feld)

        # Spielfeld auf der Konsole ausgeben.
        print("\n{}|{}|{}\n".format(farbe(self.spielfeld[0]), farbe(self.spielfeld[1]), farbe(self.spielfeld[2])))
        print("{}|{}|{}\n".format(farbe(self.spielfeld[3]), farbe(self.spielfeld[4]), farbe(self.spielfeld[5])))
        print("{}|{}|{}\n".format(farbe(self.spielfeld[6]), farbe(self.spielfeld[7]), farbe(self.spielfeld[8])))


    """ (2) Programmbaustein: Benutzereingabe anfordern """
    def eingabe_anfordern(self):
        """
        DIESE FUNKTION IST BEREITS FERTIG! HIER MÜSSEN UND DÜRFEN KEINE ÄNDERUNGEN VORGENOMMEN WERDEN!

        Die Funktion eingabe_anfordern() liest das zu bespielende Feld des aktuellen Spielers als Ziffer ein (0 - 8),
        prüft die Eingabe auf Plausibilität und ruft gegebenenfalls weitere Funktionen zum Speichern und Laden des
        Spielstands auf.

        Gültige Eingaben sind die Ziffern 0 - 8 für das zu bespielende Feld und die Zeichenketten "s" und "l",
        zum Speichern (s) und Laden (l) des Spielstands in einer Textdatei. Die Eingabe des Spielers wird mit der
        Eingabetaste bestätigt. Ist die Eingabe ungültig, so wird der aktuelle Spieler so lange erneut aufgefordert eine
        Eingabe vorzunehmen, bis diese gültig ist.

        Gültige Eingaben sind:
        * Eine Ziffer im Gültigkeitsbereichs des Spielfelds, also Ziffern zwischen 0 und 8 (jeweils einschließlich).
        * Die Zeichenkette "s" zum Speichern des aktuellen Spielstands in einer Textdatei.
        * Die Zeichenkette "l" zum Laden des Spielstands aus einer Textdatei.

        Alle sonstigen Eingaben sind ungültig.

        WICHTIG: Die Funktion eingabe_anfordern() nimmt selbst noch keine Änderungen am Status des Spielfelds, also an der
        Liste 'spielfeld', vor. Sie nimmt lediglich die Eingabe des aktuellen Spielers entgegen. Die Aktualisierung des
        Status des Spielfelds ist Aufgabe der Funktion spielfeld_status_aktualisieren().

        Übergabeparameter: Keine.

        Rückgabewert: Die Funktion liefert als Rückgabewert die Ziffer des zu bespielendes Feldes als Integerwert (0 - 8),
        welcher direkt als Index für die Aktualisierung der Liste des Spielfelds verwendet werden kann. Wird die Funktion
        verlassen, kann davon ausgegangen werden, dass die Eingabe und somit der Index gültig ist.
        """

        # Diese Schleife wird so lange ausgeführt, bis eine gültige Eingabe erfasst wird.
        while True:

            if self.spieler_am_zug == "X":
                print("{1}Spieler {0} am Zug.{2}".format(self.spieler_am_zug, FARBE_X, ENDC))

            else:
                print("{1}Spieler {0} am Zug.{2}".format(self.spieler_am_zug, FARBE_O, ENDC))

            eingabe = input("Bitte Feldnummer eingeben (0 - 8): ")

            # Prüfen, ob Eingabe einer Ziffer entspricht und ob sie zu einer Ganzzahl konvertiert werden kann.
            if eingabe.isdigit():

                # Zeichenkette zu Ganzzahl konvertieren.
                int_eingabe = int(eingabe)

                # Prüfen, ob Feldnummer im gültigen Bereich zwischen 0 und 8.
                if 0 <= int_eingabe <= 8:

                    # Prüfen, ob Feldnummer noch nicht belegt.
                    if self.spielfeld[int_eingabe] != "X" and self.spielfeld[int_eingabe] != "O":
                        # Eingabe ist gültig: Beende Schleife und gebe Eingabe des Spielers als Rückgabewert (int) zurück.
                        break

                    else:
                        print("Feld ist bereits belegt. Nochmal!")
                else:
                    print("Eingabe ist nicht im gültigen Bereich 0 - 8. Nochmal!")

            elif eingabe == "s":
                # Interpretiere Kommando, s: Spielstand speichern.
                self.spielstand_speichern()

            elif eingabe == "l":
                # Interpretiere Kommando, l: Spielstand laden.
                self.spielstand_laden()

            else:
                # Eingabe ist ungültig.
                print("Eingabe nicht erkannt! Nochmal!")

        return int_eingabe


    """ (3) Programmbaustein: Spieler wechseln """
    def spieler_wechseln(self):
        """
        DIESE FUNKTION IST BEREITS FERTIG! HIER MÜSSEN UND DÜRFEN KEINE ÄNDERUNGEN VORGENOMMEN WERDEN!

        Die Funktion spieler_wechseln() wechselt den aktuellen Spieler von "X" nach "O" bzw. umgekehrt.

        Übergabeparameter: Keine.

        Rückgabewert: Keinen.
        """

        if self.spieler_am_zug == "X":
            self.spieler_am_zug = "O"
        else:
            self.spieler_am_zug = "X"


    """ (4) Programmbaustein: Spielfeldstatus aktualisieren """
    def spielfeld_status_aktualisieren(self, index_eingabe):
        """
        Die Funktion spielfeld_status_aktualisieren() nimmt die Eingabe des aktuellen Spielers (das zu bespielende Feld) in
        Form eines Integerwerts (0 - 8) als Übergabeparameter entgegen.

        Der Übergabeparameter kann direkt als Index für den Zugriff auf die Liste des Spielfelds verwendet werden.

        Die Liste 'spielfeld' soll an der Stelle des übergebenen Index auf 'X' bzw. 'O' gesetzt werden.
        Der zu setzende Wert (ob 'X' oder 'O') befindet sich in der Variable 'spieler_am_zug'.

        Übergabeparameter:
        * index_eingabe: Integerwerts (0 - 8) als Index des zu bespielenden Felds des aktuellen Spielers.

        Rückgabewert: Keinen.
        """

        # Aktualisiere Status des Spielfelds durch Aktualisierung der Liste.
        self.spielfeld[index_eingabe] = self.spieler_am_zug

    """ (5) Programmbaustein: Sieg überprüfen """
    def sieg_pruefen(self):
        """
        Die Funktion sieg_pruefen() überprüft, ob das Spiel zum aktuellen Zeitpunkt von einem der Spieler gewonnen wurde.

        Siegbedingung: Das Spiel wird von einem Spieler gewonnen, wenn dieser entweder in einer Zeile, in einer Spalte oder
        in einer der Diagonalen alle seine Marken gesetzt hat.

        Ein Spiel kann auch als unentschieden gewertet werden:

        Bedingung für Unentschieden: Das Spiel wird als unentschieden gewertet, wenn keiner der Spieler bisher gewonnen hat
        und keine freien Felder mehr zum Bespielen zur Verfügung stehen.

        Die Funktion sieg_pruefen() soll folgendes Schnittstellenverhalten umsetzen:

        Übergabeparameter: Keine

        Rückgabewert: True, falls Bedingung für Sieg oder Unentschieden zutrifft
        Rückgabewert: False, falls Bedingung für Sieg oder Unentschieden nicht zutrifft
        """
        index_zeilen = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        index_spalten = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        index_diagonalen = [[0, 4, 8], [2, 4, 6]]

        # Prüfen auf Zeilen.
        for indizes in index_zeilen:
            if self.spielfeld[indizes[0]] == self.spielfeld[indizes[1]] == self.spielfeld[indizes[2]]:
                print(f"Spieler {self.spielfeld[indizes[0]]} hat das Spiel gewonnen!")
                return True

        # Prüfen auf Spalten.
        for indizes in index_spalten:
            if self.spielfeld[indizes[0]] == self.spielfeld[indizes[1]] == self.spielfeld[indizes[2]]:
                print(f"Spieler {self.spielfeld[indizes[0]]} hat das Spiel gewonnen!")
                return True

        # Prüfen auf Diagonalen.
        for indizes in index_diagonalen:
            if self.spielfeld[indizes[0]] == self.spielfeld[indizes[1]] == self.spielfeld[indizes[2]]:
                print(f"Spieler {self.spielfeld[indizes[0]]} hat das Spiel gewonnen!")
                return True

        # Prüfen auf Unentschieden.
        for feld in self.spielfeld:
            if feld != "X" and feld != "O":
                # Kein Unentschieden, da noch nicht alle Felder bespielt wurden.
                return False

        # Unentschieden, da alle Felder bespielt wurden und es keinen Sieger gibt.
        print("Das Spiel ist unentschieden!")
        return True


    """ (6) Programmbaustein: Spielstand speichern """
    def spielstand_speichern(self):
        """
        Die Funktion spielstand_speichern() speichert den aktuellen Spielstand über die Laufzeit des Programms hinaus in
        einer Textdatei. Innerhalb der Funktion soll im aktuellen Ordner eine Textdatei spielstand.txt zum Schreiben
        angelegt werden. Sofern die Textdatei bereits vorhanden ist, soll diese überschrieben werden.

        Übergabeparameter: Keine
        Rückgabewert: Keinen.
        """

        # Spielstand speichern.
        with open("spielstand.txt", "w") as datei:
            for feld in self.spielfeld:
                datei.write("{}\n".format(feld))

            datei.write("{}\n".format(self.spieler_am_zug))

        print("Spielstand gespeichert.")


    """ (7) Programmbaustein: Spielstand laden """
    def spielstand_laden(self):

        # Spielstand laden.
        with open("spielstand.txt", "r") as datei:

            zeilennummer = 0
            for zeile in datei:
                if zeilennummer <= 8:
                    # Aktualisiere Liste des Spielfelds mit Inhalten aus der Datei.
                    self.spielfeld[zeilennummer] = zeile.replace("\n", "")
                else:
                    # Aktualisiere den Spieler, der gerade am Zug ist.
                    self.spieler_am_zug = zeile.replace("\n", "")

                zeilennummer += 1

        print("Spielstand geladen.")

        # Aktuelles Spielfeld nochmal zeichnen.
        self.spielfeld_zeichnen()

    def spiel_starten(self):

        while True:
            # 1. Eingabe des jeweiligen Spielers anfordern.
            spieler_eingabe = self.eingabe_anfordern()

            # 2. Status des Spielfelds aktualisieren.
            self.spielfeld_status_aktualisieren(spieler_eingabe)

            # 3. Spielfeld zeichnen.
            self.spielfeld_zeichnen()

            # 4. Spieler wechseln.
            self.spieler_wechseln()

            # 5. Sieg bzw. Unentschieden prüfen.
            gewonnen = self.sieg_pruefen()

            if gewonnen == True:
                break

        print("Das Spiel ist beendet.")

# Hautprogramm:
ttt = TicTacToe() # Hier wird eine Instanz / ein Objekt von TicTacToe initialisiert!
# Im Hintergrund wird beim Anlegen des Objekts die init()-Methode aufgerufen!
ttt.spiel_starten() # Hier wird die Methode spiel_starten() aufgerufen
