M6 – CD-avbildningar
Arbetsflöde för publicering
Uppdaterade .github/workflows/publish-images.yml via en PR:

Lade till workflow_dispatch för manuell start och ett steg som visar bildtaggar i sammanfattningen.

Flödet publicerar backend- och frontend-avbildningar till GHCR när koden slås ihop med main.

Körning av arbetsflödet
Automatiskt: Kördes direkt när PR:en mergades till main. Båda avbildningarna byggdes och publicerades.

Manuellt: Startade flödet manuellt via workflow_dispatch. Sammanfattningen visade både latest-taggen och commit-SHA.

Publika paket och anonym Docker pull
Gjorde template-app-backend och template-app-frontend publika på GHCR så att de kan hämtas utan inloggning.

Loggade ut från GHCR och hämtade backendem anonymt:


docker logout ghcr.io
docker pull ghcr.io/stahlero/template-app-backend:latest
Startade containern lokalt och testade hälsokontrollen:

curl http://localhost:8000/api/health
Svaret blev {"status":"ok"} med HTTP status 200 OK.

Maskering av hemligheter
Skapade testgrenen secrets-masking-demo och lade till ett tillfälligt steg som skrev ut GITHUB_TOKEN. GitHub maskerade värdet i loggen (***). Grenen raderades efter testet utan att mergas till main.

M6 är gjort med bilder:

Arbetsflödet för publicering uppdaterat (både automatiskt och manuellt).

Paketen är publika och hämtades anonymt med Docker.

Healthstatus returnerade status 200 OK.

Maskering av hemligheter funkar

