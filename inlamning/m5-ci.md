Vad jag gjorde

Statuskontroll: Jag konfigurerade main-grenen så att kontrollen Lint and test backend krävs för att kunna slå ihop (merga) ändringar.



Röd PR (misslyckad kontroll): Jag skapade PR med ett kodfel från Ruff och CI-kontrollen misslyckades



Grön PR (godkänd kontroll): Jag rättade felet och skickade upp ändringen till samma PR. Kontrollen blev grön och godkänd, och ändringarna slogs ihop med main.



Manuell start av arbetsflöde: I en ny PR lade jag till workflow\_dispatch: i .github/workflows/ci.yml. Efter att den mergats startade jag CI-flödet manuellt under GitHub Actions på main-grenen och bekräftade att det genomfördes utan fel.



Röd PR

Det avsiktliga linter felet från Ruff gjorde att CI-kontrollen misslyckades:



F401 `os` imported but unused

F404 `from \_\_future\_\_` imports must occur at the beginning of the file



Found 3 errors.

Error: Process completed with exit code 1.

Så länge den obligatoriska kontrollen var röd var det inte möjligt att merga PR-förfrågan till main.



Grön PR

När felet togs bort och koden rättades, blev Lint and test backend kontrollen godkänd och grön. Därefter kunde PR mergas till main.



Manuellt arbetsflöde

För att kunna starta CI-flödet för hand lades följande inställning till i .github/workflows/ci.yml:



YAML

workflow\_dispatch:

Därefter startades CI-flow manuellt från gränssnittet i GitHub Actions på main-grenen. Körningen lyckades helt utan problem.



Bevis

Skärmdumparna verifierar och visar:



Ruff error som visades vid merge





Lyckade manuella körningen av CI-flödet i GitHub Actions.

