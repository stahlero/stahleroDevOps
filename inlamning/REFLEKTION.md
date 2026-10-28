Individuell reflektion

1. Produktens livscykel

I början av kursen jobbade jag mest med att få själva applikationen att fungera och förstå hur projektets olika delar hänger ihop. I M1 satte jag upp repot och började arbeta med applikationen. Under de följande milstolparna jobbade jag bland annat med Docker, tester och GitHub Actions. Jag lärde mig också hur pull requests och branch protection används för att undvika att ändringar går direkt till main utan kontroll.

När jag kom till CI i M5 började jag förstå nyttan med att låta tester och kontroller köras automatiskt. I stället för att själv behöva kontrollera allt varje gång kunde jag se i GitHub Actions om testerna gick igenom. I M6 lade jag till publicering av images till GitHub Container Registry, så att applikationen kunde hämtas på servern utan att jag behövde bygga den där manuellt.

I M7 satte jag upp en virtuell maskin manuellt i cpouta och fick applikationen att fungera där. I M8 gjorde jag sedan samma typ av infrastruktur med Terraform. Det tog lite tid att få konfigurationen rätt, men det blev tydligare hur resurserna hänger ihop och hur de kan skapas igen med samma konfiguration. I M9 kopplade jag ihop resten med automatisk deployment via SSH och GitHub Actions. Jag testade det genom att ändra rubriken i frontend och kontrollera att ändringen syntes på den körande applikationen efter att arbetsflödena hade körts.

Under kursen förändrades mitt sätt att jobba från att mest följa instruktioner och göra saker manuellt till att försöka få stegen att fungera tillsammans. Jag märkte också att det inte räcker att applikationen fungerar på min egen dator men också online.

2. Vad går sönder utan automation?

En del där jag märkte nyttan med automation var deploymenten i M9. Utan den skulle jag behöva logga in på servern själv, hämta rätt images och starta om containrarna varje gång jag ändrade applikationen. Det skulle fungera, men det finns större risk att jag glömmer något steg eller råkar använda en gammal version. Med den automatiska kedjan publiceras images först och deploymenten körs efteråt. Jag kan sedan kontrollera i github actions om båda stegen lyckades.

Även testerna och CI är viktiga. Om jag skulle hoppa över dem och bara kontrollera att appen ser ut att fungera, skulle jag kunna missa fel som inte syns direkt i webbläsaren. När kontrollerna körs vid ändringar får jag en varning tidigare, innan jag går vidare till nästa steg.

Terraform var också användbart eftersom det blev lättare att återskapa infrastrukturen än att komma ihåg alla inställningar från den manuella uppsättningen. Det betyder inte att allt löser sig automatiskt. Konfigurationen måste fortfarande vara rätt, och jag behövde själv felsöka när något inte fungerade.

Det jag främst tar med mig från kursen är att automation inte tar bort behovet av att förstå vad man gör. Den minskar antalet manuella steg och gör det lättare att upprepa processen på samma sätt. Jag förstår nu bättre hur kod, tester, images och deployment bildar en helhet, där problem i ett steg kan påverka resten.