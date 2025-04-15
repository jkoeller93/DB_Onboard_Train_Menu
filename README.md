# DB_Onboard_Train_Menu: Analyse des gastronomischen Angebotes der Deutschen Bahn 

Diese Web-App bietet dir alle Informationen über das gastronomische Speisen- und Getänkeangebot in den Fernverkehrszügen der Deutschen Bahn
### Funktionen
- Home – Allgemeine Informationen und Statistiken zum gastronomischen Angebot

- Food – Detaillierte Informationen und Analysen zum Speisenangebot

- Beverages – Detaillierte Informationen und Analysen zum Getränkeangebot (in Bearbeitung)

### Genutzte APIs
Die App bezieht ihre Daten aus verschiedenen Quellen:

- Web Archive: https://web.archive.org/

- Online-Speisekarte der Deutschen Bahn: https://db-bordgastronomie.de/digitalespeisekarte

- Analoge Speisekarten der Deutschen Bahn

## Installation & Nutzung


### Klone das Repository:
git clone <REPO_URL>
cd <REPO_ORDNER>

## Installiere die Abhängigkeiten:

pip install -r requirements.txt

## Starte die App mit:

streamlit run main.py

## Nutzung:

Datei "main.py"

- Von dieser Seite werden die anderen Seiten gesteuert
- Diese Datei aufrufen über streamlit run main.py
- Inhalte der anderen Seite werden hier importiert
- enthält das Layout von Streamlit

Datei "Home.py"

- Enthält den Code für die Seite "Home"
- Allgemeine Informationen zur Speisekarte wie Statistiken etc.

Datei "food.py"

- Enthält den Code für die Seite "food"
- Informationen und Analysen nur für die Speisen

Datei "beverages.py"

- Enthält den Code für die Seite "beverages"
- Informationen und Analyse nur für die Getränke (aktuell noch keine Daten hinterlegt)
