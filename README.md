# Unterrichtsmaterialien für das Fach Programmierung (24/25)

Herzlich Willkommen auf dem github-Repository für das Fach Programmierung an der Technikerschule Neumarkt!

Hier finden Sie den Programmcode zum Unterricht. 

**WICHTIG**: Dieses Repository ist public und read-only: Es ist ÖFFENTLICH zugänglich, aber Sie besitzen nur Leserechte.

## Getting Started

### Installation von Python und Texteditor
Um mit der Python-Programmierung zu starten, brauchen wir:
* Eine Installation des Python-Interpreters: `https://www.python.org/downloads/`
* Einen Texteditor: Wir starten mit dem Text-Editor Notepad++: `https://notepad-plus-plus.org/downloads/`

**WICHTIG**: Bei der Installation von Python ist darauf zu achten, dass man die folgende Option auf der ersten Seite aktiviert: 

*Add Python 3.xx to PATH*

Bei Notepad++ eignet sich am besten der Installer in der 64-bit Version.

### Installation und Einrichtung von git
Die Unterrichtsmaterialen werden auf dem öffentlichen Cloud-Speicher github bereitgestellt. Hierfür brauchen Sie zunächst das Programm git.

* Download des Programms git: `https://git-scm.com/downloads`

Installieren Sie git mit den Standardeinstellungen im Installationsprozess. Nehmen Sie hier bitte keine Änderungen vor.

### Erstellen eines github-Accounts
Für den Zugriff auf den Cloud-Speicher benötigen Sie einen github-Account. Der Account ist kostenlos und erfordert keine persönlichen Daten.

* Registrieren Sie sich mit Ihrer Schul-E-Mailadresse auf github: `https://github.com/ > Sign Up`

Aktivieren Sie Ihren Account mit der Bestätigungsmail und richten Sie github beim Login ohne spezielle Personalisierung ein > `"Skip Personalization"`.

### Lokalen Ordner zur Speicherung einrichten
**WICHTIG**: Die Anweisungen dieser Sektion müssen nur einmalig für die Einrichtung durchgeführt werden!

Zunächst müssen Sie festlegen, in welchem Ordner die Dateien auf Ihrem Rechner gespeichert und synchronisiert werden sollen. 

* Erstellen Sie einen lokalen Ordner für die Unterrichtsmaterialien: `Rechtsklick > Neuer Ordner > „Unterrichtsmaterial Programmierung“`

Anschließend müssen Sie den lokalen Ordner mit dem github Repository in der Cloud (github) verknüpfen.

* Laden Sie die Dateien aus github erstmalig herunter: `Rechtsklick im neuen Ordner > Open Git Bash here`
* Geben Sie den Git-Befehl zum erstmaligen Herunterladen in die Konsole ein:

`git clone https://github.com/DWeberBSZ/2425_ET1_PGM.git`

## Workflow im Unterricht
![image](https://github.com/user-attachments/assets/b636b7b5-403a-45db-9eaa-3b0657a33bbb)

### Lokale Inhalte aktualisieren ("Pullen")

**WICHTIG**: Diese Anweisungen sollten nach jeder Unterrichtstunde durchgeführt werden!

Die Unterrichtsmaterialien können über das Programm git von github heruntergeladen und lokal im angelegten Ordner aktualisiert werden. 

* „Pullen“ der neuesten Unterrichtsmaterialien: `Rechtsklick im Ordner > Open Git Bash here`
* Git-Befehl zum Aktualisieren in Konsole eingeben: `git pull`

!!!! **In diesem synchronisierten Ordner mit dem Unterrichtsmaterial sollten Sie keine Änderungen vornehmen. Änderungen in diesem Ordner von Ihnen werden beim Aktualisieren überschrieben. Verwenden Sie für Ihre eigenen Programme einen separaten Ordner !!!!**
