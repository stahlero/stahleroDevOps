M2 — Review
Grenskydd
main-grenen skyddas av ett GitHub-regelsätt. Direktpushar är blockerade och ändringar kräver pull-förfrågningar. Eftersom det är solotarbete krävs 0 godkännanden.

Pull-förfrågan
Skapade och sammanfogade PR:

Gren: m2-first-pr

Syfte: M2-granskning

Dokumenterade egengranskning i en PR-kommentar och sammanfogade till main.

Konfliktövning
Skapade två grenar från samma utgångspunkt: conflict-a och conflict-b. Båda ändrade samma rad i README.md.

conflict-a sammanfogades först, vilket skapade en konflikt i nästa PR. Konflikten löstes lokalt och skickades upp. Repositoryt kontrollerades med git grep '<<<<<<<'.