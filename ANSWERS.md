## Teorifrågor

### 1️⃣ Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?  

### Enhetstest

Enhetstester är oftast mindre tester som verifierar en avgränsad del av koden. Vanligtvis testas en enskild funktion eller metod 
isolerat från externa beroenden. Sådana beroenden kan simuleras med exempelvis mock-objekt.

Enhetstester används under utvecklingsarbetet för att kontrollera att koden fungerar som avsett och för att tidigt upptäcka 
fel. Vid TDD (Test-Driven Development) skriver man testerna innan man implementerar funktionaliteten. Det är också vanligt 
att automatisera enhetstesterna i CI/CD, så att de körs exempelvis när kod pushas till GitHub eller när en pull request skapas.

Exempel:  
När metoden toggleFavorite() i klassen BookStore enhetstestas verifieras, med hjälp av ett mockat objekt, att metoden 
anropar add() respektive remove() i klassen FavoriteBooks.

### Integrationstest

Integrationstester används under utvecklingsarbetet för att verifiera att olika delar av systemet fungerar tillsammans. Det kan 
exempelvis handla om samspelet mellan funktioner, metoder och klasser, kommunikation med API eller interaktion med databaser. 
Även integrationen mellan frontend och backend kan testas.

Till skillnad från isolerade enhetstester används här de verkliga implementationerna av de delar som ska integreras. Externa 
beroenden, exempelvis databaser och API, kan också vara verkliga, beroende på vad testet ska verifiera. Precis som enhetstester 
automatiseras integrationstester ofta i CI/CD.

Exempel:  
När metoden toggleFavorite() i klassen BookStore integrationstestas verifieras att den samverkar korrekt med metoderna add() och remove() i klassen FavoriteBooks. Testerna kontrollerar att böcker faktiskt läggs till i respektive tas bort från favoritlistan.

### Regressionstest

Regressionstester syftar till att säkerställa att befintlig funktionalitet fortfarande fungerar efter förändringar i koden. Sådana 
förändringar kan exempelvis vara felrättningar, ny funktionalitet eller refaktorering av befintlig kod.

Regressionstester kan bestå av tidigare skrivna enhets-, integrations- eller end-to-end-tester. De körs på nytt för att kontrollera 
att ändringarna inte har orsakat nya fel i funktionalitet som tidigare fungerade. Det är vanligt att automatisera regressionstester i 
CI/CD, exempelvis när kod pushas till GitHub eller när en pull request skapas.

### Prestandatest

Prestandatester används för att undersöka ett systems prestanda under olika belastningsförhållanden. Målet är att säkerställa 
att systemet uppfyller kraven på stabilitet, kapacitet, svarstider och resursförbrukning.

Testerna kan utföras både vid hög belastning och under lång tid för att upptäcka exempelvis långsamma svarstider, flaskhalsar 
och minnesläckor som inte nödvändigtvis upptäcks med andra testmetoder.

Exempel:  
Läslistan skulle kunna testas för att mäta hur snabbt sidan laddas när katalogen innehåller tusentals böcker. 
Ett annat test skulle kunna undersöka hur webbplatsen presterar när många användare besöker den samtidigt.

### 2️⃣ Beskriv hur det går till när man arbetar med TDD

TDD (Test-Driven Development) innebär att man utvecklar kod utifrån automatiserade testfall som baseras på krav. När man har bestämt 
vilket beteende som ska implementeras arbetar man enligt cykeln RED – GREEN – REFACTOR.

RED:
Man börjar med att skriva ett test som verifierar det önskade beteendet utifrån kravet. När testet körs förväntas det misslyckas
eftersom funktionaliteten ännu inte är implementerad. Det är viktigt att kontrollera att testet misslyckas av rätt anledning.

GREEN:
Man skriver minsta möjliga mängd kod för att få testet att passera. Målet är att uppfylla kravet utan att lägga till mer 
funktionalitet än vad som behövs.

REFACTOR:
Man förbättrar kodens struktur, läsbarhet och underhållbarhet utan att ändra dess funktionella beteende. Efter refaktoreringen 
körs testerna igen för att säkerställa att funktionaliteten fortfarande fungerar.

Om kraven förändras uppdaterar eller kompletterar man testfallen så att de motsvarar de nya kraven och implementerar därefter 
den ändrade funktionaliteten.

Vid TDD utvecklar man en mindre del av funktionaliteten i taget. När cykeln RED – GREEN – REFACTOR är klar börjar man om med 
nästa krav eller beteende.

TDD passar bra i agila utvecklingsteam eftersom arbetet sker stegvis och fel kan upptäckas tidigt. Det blir också enklare att 
förändra och vidareutveckla koden. De automatiserade testerna hjälper till att upptäcka regressioner när koden ändras.

### 3️⃣ Beskriv hur BDD skiljer sig från TDD.
TDD (Test-Driven Development) är en utvecklingsmetod där man skriver automatiserade tester utifrån definierade krav innan man 
implementerar funktionaliteten. Testerna styr utvecklingen och hjälper till att verifiera att koden fungerar som avsett.

BDD (Behavior-Driven Development) fokuserar i stället på att beskriva och verifiera ett systems beteende utifrån användarens 
perspektiv. Scenarierna formuleras på ett sätt som är lätt att förstå även för personer utan programmeringskunskaper, 
exempelvis produktägare och andra intressenter.

I BDD används ofta Gherkin för att beskriva scenarier enligt strukturen Given – When – Then:

    Given: Beskriver förutsättningarna inför testet.

    When: Beskriver händelsen eller handlingen som testas.

    Then: Beskriver det förväntade resultatet.

Exempel i Gherkin:

Scenario: Beräkna nettolön med 33 procent skatt
  Given att bruttolönen är 32000 kronor
  When skatten beräknas med 33 procent
  Then ska nettolönen vara 21440 kronor

TDD och BDD kan med fördel kombineras i ett projekt eftersom de kompletterar varandra. TDD kan exempelvis användas vid utveckling 
av backend-funktioner för att stegvis implementera och verifiera den underliggande logiken. BDD kan användas för att beskriva 
systemets förväntade beteende ur ett användarperspektiv och skapa en gemensam förståelse mellan utvecklare, testare och produktägare.

Med Gherkin och exempelvis Behave kan scenarierna dessutom automatiseras och användas för att verifiera funktionalitet genom hela 
systemet, exempelvis i frontend och i integrationen mellan frontend och backend.



### 4️⃣ Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. 
### Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? 
#### Motivera ditt val.
 
Jag skulle använda en kombination av olika testtyper och arbeta enligt TDD och BDD.

Inledningsvis skulle jag fokusera på enhets- och integrationstester. Med TDD skulle jag utveckla funktionaliteten stegvis 
genom att först skriva tester och sedan implementera koden. Enhetstesterna skulle verifiera enskilda funktioner och metoder, 
medan integrationstesterna skulle kontrollera att olika delar av systemet, exempelvis backend, API och datalagring, fungerar 
tillsammans.

Jag skulle även automatisera regressionstester så att befintlig funktionalitet kontrolleras när ny funktionalitet tillkommer 
eller koden ändras. Efter större förändringar eller driftsättningar skulle jag använda smoketester för att snabbt kontrollera att systemets grundläggande funktioner fungerar.

Med hjälp av BDD skulle jag utgå från user stories och acceptanskriterier som tagits fram i samarbete med produktägare och 
andra intressenter. Dessa skulle ligga till grund för automatiserade E2E-tester som verifierar viktiga användarflöden genom 
hela systemet, exempelvis att en användare kan hitta en bok och lägga till den som favorit.

Slutligen skulle jag använda prestandatester om det fanns krav på svarstider, antal samtidiga användare eller systemets kapacitet.

Tillsammans skulle testningen verifiera systemets funktionalitet, samspelet mellan olika komponenter och de viktigaste användarflödena. 
Genom att noggrant planera E2E-testerna tillsammans med kravställare och andra intressenter skulle risken minska för att systemet 
inte motsvarar kundens förväntningar.
