## Teorifrågor

### 1️⃣ Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?  

Enhetstest är oftast mindre tester som verifierar en mindre del av koden. Ofta testas en enskild 
funktion eller metod isolerat utan några externa beroenden. Externa beroenden brukar då simuleras eller Mockas.  
Enhetest är vanligt tidigt i utvecklingsfasen. De syftar till att kontollera att koden fungerar som avsett och 
för att tidigt hitta eventuella fel. Man använder ofta TDD och skriver då enhetstestena innan man skriver koden. 
Vanligt är också att man automatiserar testerna, inte minst i CI/CD då testerna körs vid interaktion med GitHub, 
t.ex. vid Push och Pull.

Integrationstest körs under utvecklingsarbetet för att verifiera att olika delar av koden fungerar tillsammans. Det 
kan t.ex. vara samspelet mellan funktioner, metoder, klasser. API'er, kommunikationer eller lagring. Tester av 
interaktion mellan Frontend och Backend kan vara integrationstester. Till skillnad mot enhetstest används riktiga 
beroenden och ofta riktiga databaser och kommunikationsvägar. Liksom vid enhetstest är det vanligt att automatisera 
testerna i CI/CD.

Regressionstest syftar till att säkerställa att systemet fungerar som tidigare efter ändringar i koden. Det kan vara 
då man rättat andra fel, lagt till ny funktionalitet eller refaktorerat befintlig kod. Regressionstester är ofta gamla 
enhetstester eller integrationstester som körs i syftet att kontrollera att koden fortafarnde fungerar som tidigare.  
Det är vanligt att köra regressionstesterna i CI/CD för att automatiskt regressionstesta kod vid t.ex. Push.

Presetandatester används för att testa ett systems förmåga vid belastning. Man vill säkerställa att systemet motsvarar
kraven på stabilitet, kapacitet, hastighet och förbrukning av resureser. Man testar ofta systemet under hög belastning 
och under lång tid. Testerna kan hitta fel som normalt inte upptäcks med övriga testmetoder. 

### 2️⃣ Beskriv hur det går till när man arbetar med TDD.

TDD (Test Driven Development) innebär att man utvecklar koden utifrån färdiga automatiska testfall som baserats på krav. 
Då man har bestämt vilket beteende (krav) som ska implementeras arbetar man enligt stegen RED - GREEN - REFACTOR. 

RED:  
Man börjar med att skriva ett test som är designat för att testa kravet. När man kör testet förväntas det misslyckas 
då det inte finns någon kod att testa.

GREEN:  
Man skriver minimalt med kod så att testfallet lyckas. 

REFACTOR:  
Man förbättrar koden avseende struktur och läsbarhet utan att ändra funktionen. Skulle det längre fram krävas ändringar 
i kodens funktion ändrar man först testet för att motsvara de nya kraven. Därefter ändrar man koden.

Då man arbetar enligt TDD utvecklar man en mindre del av koden i taget. Då man är färdig med cykeln RED - GREEN - REFACTOR
börjar man om med ett nytt krav.

TDD passar bra för arbete i agila utvecklarteam. Man utvecklar då koden stegvis och kan tidigt upptäcka fel i koden. Man 
enkelt anpassa koden vid förändringar i kraven och minskar risken regressionsfel.  

### 3️⃣ Beskriv hur BDD skiljer sig från TDD.
TDD är en utvecklingsmetod där man utifrån definierade krav skriver testfall som i sin tur bestämmer hur koden ska
implementeras. BDD (Behavior Driven Development) används för att beskriva och testa ett system och dess beteende. 
Man använder beskrivande scenarier som är enkla att förstå även för icke utvecklare. 

I BDD utgår man ifrån ett användarperspektiv för att beskriva hur ett system ska bete sig. Man kan använda enkla GIVEN - 
WHEN - THEN scenarier i Gherkin för att beskriva scenarierna. 

GIVEN : Beskriver förutsättningarna inför testet  
WHEN: Beskriver själva händelsen som ska testas  
THEN: Beskriver det förväntade resultatet av handlingen

Exempel i Gherkin:
Scenario: Löneskatten är 33 %
GIVEN: Att lönen är 32 000 kr
WHEN: Skatten beräknas
THEN: Ska nettolönen vara 21 440 kr

Man kan i ett projekt kombinera TDD och BDD där de kan komplettera varann. Man kan t.ex använda TDD då man utvecklar 
Backend för att grundläggande implementera och verifiera funktioner. Man kan använda BDD för att beskriva systemet för 
produktägare och stakeholders på ett förståligt sätt. Man kan sen med fördel använda Gherkin och t.ex. Behave för att 
verifiera användarscenarier i Frontend.



### 4️⃣ Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. 
#### Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? 
Motivera ditt val.
 
Jag skulle använda en kombination av olika testtyper och arbeta enligt TDD och BDD.

Inledningsvis skulle jag fokusera på enhetstester och integrationstester. Med TDD skulle jag utveckla funktionaliteten 
stegvis genom att först skriva tester och sedan implementera koden. Enhetstesterna skulle verifiera enskilda funktioner 
och metoder, medan integrationstesterna skulle kontrollera att exempelvis frontend, backend och datalagring fungerade tillsammans.

Jag skulle även automatisera regressionstester så att befintlig funktionalitet kontrolleras när ny funktionalitet tillkommer 
eller koden ändras. Efter större förändringar eller driftsättningar skulle jag använda smoketester för att snabbt kontrollera 
att systemets grundläggande funktioner fungerade.

Med hjälp av BDD skulle jag utgå från user stories och acceptanskriterier som tagits fram i samarbete med produktägare och andra 
intressenter. Dessa skulle ligga till grund för E2E-tester som verifierar viktiga användarflöden genom hela systemet, exempelvis 
att en användare kan hitta en bok och lägga till den som favorit.

Slutligen skulle jag använda prestandatester om det fanns krav på svarstider, samtidiga användare eller systemets kapacitet. 

Tillsammans skulle all testning verifiera systemets funktionalitet, interaktioner mellan komponenter och identifierade användarflöden.
Då E2E testningen noga planerats med olika kravställare skulle sannolikheten för att systemet i slutändan skulle motsvara kundens 
förväntningar vara stora.