M4 — Tests

Utförande

Bekräftade först att alla tester passerade. Testa felet genom att skapa två objekt ("mjölk" och "bröd") och sedan radera "bröd", vilket visade att teckenantalet  inte uppdaterades. Skrev backend/tests/test\_bugjakt.py för att testa de.



Röd test

Testet misslyckades först:
FAILED tests/test\_bugjakt.py::test\_delete\_item\_updates\_stats

assert {'count': 1, 'total\_characters': 9} == {'count': 1, 'total\_characters': 4}

Åtgärd och grön test

Rättade raderingsfunktionen så att den subtraherar det raderade objektets teckenantal från \_total\_characters.
Därefter fixade de problemet
