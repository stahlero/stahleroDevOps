M7 – VM i cPouta

Jag skapade en Ubuntu VM i cpouta och kopplade en floating IP till den. Jag konfigurerade Security Group med SSH på port 22 och appen på port 8080.

Jag installerade Docker och Docker Compose på vm:n och körde backend och frontend från GHCR med Docker Compose.

Jag testade appen från VM:n med:

curl http://localhost:8080/api/health

och fick {"status":"ok"}.

Jag testade även från min egen dator via floating IP:

curl http://86.50.20.64:8080/api/health

vilket gav HTTP 200 och {"status":"ok"}.

Appen fungerade även i webbläsaren via nip.io:

http://86-50-20-64.nip.io:8080/

Bilder med i committen